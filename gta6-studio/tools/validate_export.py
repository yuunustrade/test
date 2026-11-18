#!/usr/bin/env python3
"""Check an exported short against the publishing spec. Fails closed.

Usage:
    python3 tools/validate_export.py <video.mp4> [--min 5] [--max 60]

Checks: file exists, 1080x1920, H.264 video, AAC audio present, duration in range,
frame rate <= 60, yuv420p. Prints sha256 for the approval record. Exit 1 on any failure.
"""
import hashlib
import json
import os
import subprocess
import sys


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    path = args[0]
    lo = float(args[args.index("--min") + 1]) if "--min" in args else 5.0
    hi = float(args[args.index("--max") + 1]) if "--max" in args else 60.0

    fails = []
    if not os.path.isfile(path):
        print(f"FAIL: file not found: {path}")
        sys.exit(1)

    r = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format",
                        "-of", "json", path], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL: ffprobe could not read file\n{r.stderr}")
        sys.exit(1)
    info = json.loads(r.stdout)
    v = [s for s in info["streams"] if s["codec_type"] == "video"]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"]
    dur = float(info["format"].get("duration", 0))

    if not v:
        fails.append("no video stream")
    else:
        v = v[0]
        if (v.get("width"), v.get("height")) != (1080, 1920):
            fails.append(f"resolution {v.get('width')}x{v.get('height')} (need 1080x1920)")
        if v.get("codec_name") != "h264":
            fails.append(f"video codec {v.get('codec_name')} (need h264)")
        if v.get("pix_fmt") != "yuv420p":
            fails.append(f"pixel format {v.get('pix_fmt')} (need yuv420p)")
        num, den = (v.get("avg_frame_rate", "0/1").split("/") + ["1"])[:2]
        fps = float(num) / float(den or 1) if float(den or 1) else 0
        if not 23 <= fps <= 60:
            fails.append(f"frame rate {fps:.2f} (need 23–60)")
    if not a:
        fails.append("no audio stream")
    elif a[0].get("codec_name") != "aac":
        fails.append(f"audio codec {a[0].get('codec_name')} (need aac)")
    if not lo <= dur <= hi:
        fails.append(f"duration {dur:.2f}s outside {lo}-{hi}s")

    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"file:     {path}\nduration: {dur:.2f}s\nsha256:   {sha}")
    if fails:
        print("RESULT: FAIL")
        for f in fails:
            print(f"  - {f}")
        sys.exit(1)
    print("RESULT: PASS (technical spec only — human must still watch it on desktop AND phone)")


if __name__ == "__main__":
    main()
