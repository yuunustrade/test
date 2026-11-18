#!/usr/bin/env python3
"""Render a DRAFT 9:16 short from an edit decision list (posts/<ID>/edit.json).

Usage:
    python3 tools/render_short.py posts/<POST_ID>/edit.json [--dry-run]

Paths inside edit.json are relative to the gta6-studio/ folder.
Only uses local files listed in the EDL. It never downloads anything.

edit.json schema (see templates/edit.example.json):
{
  "post_id": "GTA6-20261119-001",
  "fps": 30,
  "output": "media/exports/GTA6-20261119-001_DRAFT.mp4",
  "segments": [
    {"type": "video", "file": "media/raw/clip.mp4", "in": 12.0, "out": 14.5,
     "framing": "cover", "x": 0.5, "y": 0.5, "zoom": 1.0, "game_audio": 0.35},
    {"type": "image", "file": "media/graphics/card.png", "duration": 3, "framing": "fit"},
    {"type": "color", "color": "black", "duration": 1.5}
  ],
  "captions": [{"start": 0.0, "end": 1.8, "text": "Hook line", "position": "lower"}],
  "voiceover": {"file": "media/audio/vo.wav", "volume": 1.0},
  "music": {"file": "media/audio/track.mp3", "volume": 0.18, "duck": true}
}

framing: "cover" = fill 9:16 by cropping (x/y choose the crop centre 0..1, zoom >= 1 punches in)
         "fit"   = whole frame visible over a blurred copy of itself
caption position: "lower" (default, above platform UI), "center", "upper"
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

W, H = 1080, 1920
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "DejaVu Sans"


def die(msg):
    print(f"RENDER FAILED: {msg}", file=sys.stderr)
    sys.exit(1)


def run(cmd, dry):
    print("$ " + " ".join(cmd))
    if dry:
        return
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:], file=sys.stderr)
        die("ffmpeg returned an error (see above)")


def has_audio(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
         "stream=index", "-of", "csv=p=0", path], capture_output=True, text=True)
    return bool(r.stdout.strip())


def resolve(p):
    full = p if os.path.isabs(p) else os.path.join(STUDIO, p)
    if not os.path.isfile(full):
        die(f"missing file: {p}")
    return full


def video_filter(seg, fps):
    framing = seg.get("framing", "cover")
    if framing == "fit":
        vf = (f"split[a][b];"
              f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness=-0.08[bg];"
              f"[b]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
              f"[bg][fg]overlay=(W-w)/2:(H-h)/2")
    else:
        z = max(1.0, float(seg.get("zoom", 1.0)))
        x = min(1.0, max(0.0, float(seg.get("x", 0.5))))
        y = min(1.0, max(0.0, float(seg.get("y", 0.5))))
        sw, sh = int(W * z), int(H * z)
        vf = (f"scale={sw}:{sh}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H}:(iw-{W})*{x}:(ih-{H})*{y}")
    return f"{vf},fps={fps},format=yuv420p,setsar=1"


def render_segment(i, seg, fps, tmp, dry):
    out = os.path.join(tmp, f"seg{i:03d}.mp4")
    t = seg.get("type", "video")
    enc = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
           "-c:a", "aac", "-ar", "48000", "-ac", "2"]
    silence = ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]

    if t == "video":
        src = resolve(seg["file"])
        start, end = float(seg["in"]), float(seg["out"])
        dur = end - start
        if dur <= 0:
            die(f"segment {i}: out must be after in")
        gain = float(seg.get("game_audio", 0.35))
        use_audio = gain > 0 and (dry or has_audio(src))
        fc = f"[0:v]{video_filter(seg, fps)}[v]"
        if use_audio:
            fc += (f";[0:a]volume={gain},aresample=48000,"
                   f"aformat=channel_layouts=stereo,apad[a]")
            amap = "[a]"
        else:
            amap = "1:a"
        cmd = ["ffmpeg", "-y", "-ss", str(start), "-t", str(dur), "-i", src, *silence,
               "-filter_complex", fc, "-map", "[v]", "-map", amap, "-t", str(dur), *enc, out]
    elif t == "image":
        src = resolve(seg["file"])
        dur = float(seg["duration"])
        fc = f"[0:v]{video_filter(seg, fps)}[v]"
        cmd = ["ffmpeg", "-y", "-loop", "1", "-t", str(dur), "-i", src, *silence,
               "-filter_complex", fc, "-map", "[v]", "-map", "1:a", "-t", str(dur), *enc, out]
    elif t == "color":
        dur = float(seg["duration"])
        color = seg.get("color", "black")
        cmd = ["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c={color}:s={W}x{H}:r={fps}:d={dur}",
               *silence, "-map", "0:v", "-map", "1:a", "-t", str(dur),
               "-pix_fmt", "yuv420p", *enc, out]
    else:
        die(f"segment {i}: unknown type '{t}'")
    run(cmd, dry)
    return out, dur


def ass_time(s):
    s = max(0.0, s)
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{sec:05.2f}"


def write_ass(captions, path):
    align = {"lower": 2, "center": 5, "upper": 8}
    lines = [
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}",
        "WrapStyle: 0", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
        "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, "
        "BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        # lower captions sit ~1/3 up from the bottom, clear of TikTok/Shorts UI
        f"Style: lower,{FONT},76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,2,110,170,620,1",
        f"Style: center,{FONT},84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,5,110,170,0,1",
        f"Style: upper,{FONT},76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,8,110,170,300,1",
        "", "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    for c in captions:
        pos = c.get("position", "lower")
        if pos not in align:
            die(f"caption position must be one of {list(align)}")
        text = str(c["text"]).replace("{", "(").replace("}", ")").replace("\n", "\\N")
        lines.append(f"Dialogue: 0,{ass_time(float(c['start']))},{ass_time(float(c['end']))},"
                     f"{pos},,0,0,0,,{text}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if len(args) != 1:
        die(__doc__)
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            die(f"{tool} is not installed")
    with open(args[0], encoding="utf-8") as f:
        edl = json.load(f)

    fps = int(edl.get("fps", 30))
    segs = edl.get("segments") or die("edit.json has no segments")
    output = os.path.join(STUDIO, edl.get("output") or
                          f"media/exports/{edl.get('post_id', 'UNTITLED')}_DRAFT.mp4")
    os.makedirs(os.path.dirname(output), exist_ok=True)

    tmp = tempfile.mkdtemp(prefix="render_")
    try:
        parts, total = [], 0.0
        for i, seg in enumerate(segs):
            p, d = render_segment(i, seg, fps, tmp, dry)
            parts.append(p)
            total += d
        with open(os.path.join(tmp, "list.txt"), "w") as f:
            f.writelines(f"file '{p}'\n" for p in parts)

        cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "list.txt"]
        vchain = "[0:v]null"
        if edl.get("captions"):
            write_ass(edl["captions"], os.path.join(tmp, "captions.ass"))
            vchain = "[0:v]ass=captions.ass"
        fc = [f"{vchain}[v]"]
        mix = ["[0:a]"]
        idx = 1
        vo, mus = edl.get("voiceover"), edl.get("music")
        if vo:
            cmd += ["-i", resolve(vo["file"])]
            fc.append(f"[{idx}:a]volume={vo.get('volume', 1.0)},aresample=48000,"
                      f"aformat=channel_layouts=stereo,asplit[vo][vokey]")
            mix.append("[vo]")
            vo_idx = idx
            idx += 1
        if mus:
            cmd += ["-stream_loop", "-1", "-i", resolve(mus["file"])]
            fc.append(f"[{idx}:a]volume={mus.get('volume', 0.18)},aresample=48000,"
                      f"aformat=channel_layouts=stereo,atrim=0:{total:.3f}[mus]")
            if vo and mus.get("duck", True):
                fc.append("[mus][vokey]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[musd]")
                mix.append("[musd]")
            else:
                mix.append("[mus]")
            idx += 1
        if vo and not (mus and mus.get("duck", True)):
            fc.append("[vokey]anullsink")
        if len(mix) > 1:
            fc.append(f"{''.join(mix)}amix=inputs={len(mix)}:duration=first:normalize=0,"
                      f"alimiter=limit=0.95[a]")
        else:
            fc.append("[0:a]anull[a]")

        cmd += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                "-t", f"{total:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(fps),
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-movflags", "+faststart", output]
        print(f"(cwd {tmp})")
        if not dry:
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                run(cmd, dry)
            finally:
                os.chdir(cwd)
        else:
            run(cmd, dry)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if dry:
        print("DRY RUN: nothing rendered.")
    else:
        print(f"DRAFT RENDERED: {os.path.relpath(output, STUDIO)} ({total:.1f}s). "
              f"Run tools/validate_export.py on it next. It is NOT approved.")


if __name__ == "__main__":
    main()
