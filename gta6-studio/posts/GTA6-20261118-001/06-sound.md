# 06 — Sound: GTA6-20261118-001

**Sound designer time:** ~00:15 Europe/Rome, 19 Nov 2026 (approximate)
**Draft in:** `media/exports/GTA6-20261118-001_DRAFT.mp4` (30.51 s, 17 caption cards, silent AAC track)
**Narration mode (playbook):** licensed AI voice. Provider + API key are **NOT configured**.
**Audio on disk:** `media/audio/` contains only `.gitkeep`. There are no `licensed-audio` rows in `data/asset_manifest.csv`.

## Current mix: NOTHING (silent)
- VO: none. Music: none. SFX: none. Game audio: n/a (news-explainer, no gameplay).
- Loudness of the current draft (`ffmpeg ... loudnorm=print_format=summary`): **Input Integrated -inf LUFS, True Peak -inf dBTP**. It is digital silence.
- No re-render was done and `edit.json` is unchanged, because no cleared audio exists.

---

## 1. VO recording sheet

**Rules for whoever voices it**
- Read the words **exactly** as written. The captions in `edit.json` are these words, and they must match.
- AI voice: use only a licensed provider the owner has set up, on a plan whose terms allow commercial use on YouTube and TikTok. Free tiers often do **not** allow that, and the weekly budget is 0, so any paid plan needs the owner's approval. Use a stock/library voice. **Never** clone or imitate a real person, including Rockstar or GTA cast members, trailer narrators or streamers.
- Owner's own voice: also fine if the owner chooses it. In that case this is the owner's script to read.
- Delivery: sharp, curious, confident, like a friend who checked the facts. Not a hype announcer, and never sounding official. Medium-fast pace (about 2.6 words/s), with energy rising on the hook and a calm, helpful close.
- Deliver as: `media/audio/GTA6-20261118-001_vo.wav`, 48 kHz, mono or stereo, 24-bit (16-bit is OK). Use one continuous take, about 30–31 s, with no music or SFX baked in. Leave 0.1–0.2 s of room tone at the head.

**Pronunciation**
| Written | Say |
|---|---|
| GTA 6 | "G-T-A six" |
| PS5 / PS4 | "P-S five" / "P-S four" |
| November 19, 2026 | "November nineteenth, twenty twenty-six" |
| 11am | "eleven a.m." |
| November 18 / November 10 | "November eighteenth" / "November tenth" |
| 212GB | "two hundred twelve gigabytes" (UK read "two hundred and twelve" is fine too) |
| PlayStation Support / Rockstar Support | say them in full, with no emphasis that could sound like an endorsement |

**Per-card timing.** Marks: **bold** = stress; `/` = short breath (about 0.15 s); `//` = beat pause (about 0.3 s). Card windows come from `edit.json`.

| # | Window (s) | Target | Line (with marks) | Note |
|---|---|---|---|---|
| 1 | 0.0–2.0 | 1.8 s | When does **GTA 6** hit **your** PS5? | Start with energy and real question intonation. No lead-in breath over 0.1 s. |
| 2 | 2.0–4.2 | 2.0 s | **Not** everywhere / at the **same** moment. | |
| 3 | 4.2–6.5 | 2.3 s | Release day: / **November nineteenth**, twenty twenty-six. | **Tightest card** (about 14 syllables). Read it brisk and clean. Running up to 0.3 s into card 4 is acceptable. |
| 4 | 6.5–9.0 | 2.3 s | On PS5, / it's **midnight** / **local** time. | Put the key stress on "local". |
| 5 | 9.0–10.4 | 1.2 s | Country / by country, | Keep going, no full stop. |
| 6 | 10.4–11.8 | 1.3 s | starting in **New Zealand**. // | Small payoff lift. |
| 7 | 11.8–15.0 | 2.8 s | **Our math**: / **eleven a.m.** UK time, / November eighteenth. | "Our math" stays clearly audible. It is the spoken label that this is our own conversion, not an official time. Do not drop or rush it. |
| 8 | 15.0–16.0 | 0.7 s | Your **turn**: / | |
| 9 | 16.0–17.8 | 1.6 s | when **your country** / hits **midnight**. // | |
| 10 | 17.8–19.0 | 1.0 s | **Several** time zones? | Question intonation. |
| 11 | 19.0–20.3 | 1.2 s | Check PlayStation Support. | Neutral, helpful. |
| 12 | 20.3–22.5 | 1.9 s | Heads up: / it's **not** on **PS4**. // | Firm on "not". |
| 13 | 22.5–23.5 | 0.8 s | Pre-**ordered**? | |
| 14 | 23.5–25.0 | 1.4 s | Pre-load **opened** / November tenth. | Past tense, a fact, not a call to action. |
| 15 | 25.0–27.8 | 2.4 s | You need **at least** / **two hundred twelve gigabytes** free. | "at least" matters (it is the minimum). |
| 16 | 27.8–28.9 | 0.9 s | **Xbox** player? | |
| 17 | 28.9–30.5 | 1.4 s | Check Rockstar Support / for times. | End clean, no sign-off, no "follow". Let it ring out about 0.2 s before the cut. |

Total spoken words: 75. Target VO length is 30.0–30.5 s. If the take runs 30.5–31.5 s, the editor extends the last segment and retimes the caption cards to the waveform (keeping the same split points). Do not speed it up past natural speech.

**Paste-ready text for an AI voice tool (plain).** Punctuation creates the pauses.
```
When does GTA 6 hit your PS5?
Not everywhere, at the same moment.
Release day: November nineteenth, twenty twenty-six.
On PS5, it's midnight local time.
Country by country, starting in New Zealand.
Our math: eleven a.m. UK time, November eighteenth.
Your turn: when your country hits midnight.
Several time zones? Check PlayStation Support.
Heads up: it's not on PS4.
Pre-ordered? Pre-load opened November tenth.
You need at least two hundred twelve gigabytes free.
Xbox player? Check Rockstar Support for times.
```
(The numbers are spelled out so that TTS cannot misread them. The captions keep the numeric form "November 19, 2026 / 11am / 212GB", which reads the same.)

**SSML variant** (only if the provider supports `<break>`; otherwise use the plain version):
```
<speak>
When does <emphasis>GTA 6</emphasis> hit your PS5?<break time="150ms"/>
Not everywhere at the same moment.<break time="150ms"/>
Release day: November nineteenth, twenty twenty-six.<break time="150ms"/>
On PS5, it's midnight <emphasis>local</emphasis> time.<break time="150ms"/>
Country by country, starting in New Zealand.<break time="300ms"/>
Our math: eleven a.m. UK time, November eighteenth.<break time="300ms"/>
Your turn: when your country hits midnight.<break time="250ms"/>
Several time zones? Check PlayStation Support.<break time="200ms"/>
Heads up: it's <emphasis>not</emphasis> on PS4.<break time="250ms"/>
Pre-ordered? Pre-load opened November tenth.<break time="150ms"/>
You need at least two hundred twelve gigabytes free.<break time="200ms"/>
Xbox player? Check Rockstar Support for times.
</speak>
```

**Prep before handing the file over** (the render tool does not normalise loudness, so the VO has to arrive at the target level):
```
ffmpeg -i raw_vo.wav -af "highpass=f=80,loudnorm=I=-14:TP=-1.5:LRA=7" -ar 48000 media/audio/GTA6-20261118-001_vo.wav
```
After that, add an `asset_manifest.csv` row (origin `ai-voice` or `own-recording`, provider + plan/terms URL or "owner's own voice", status CLEARED).

---

## 2. Music brief (no track chosen, none downloaded)

- **Mood:** a "countdown to midnight" feel. Tense but friendly anticipation, clean and modern, not aggressive. Think minimal electronic / synthwave-lite pulse with a soft ticking or hi-hat motif. **No vocals.** Nothing that sounds like GTA themes, trailer music or radio-station songs.
- **BPM:** 95–110 (about 100 suits the 2–2.5 s card rhythm; at 100 BPM 1 bar = 2.4 s).
- **Length:** at least 31 s, or a clean loop (the renderer loops and trims). Ideally a light lift around 15 s (the "Your turn" card) and a resolve or soft end near 30 s.
- **Mix role:** a bed only. It sits well under the VO and must never compete with the numbers (dates, 11am, 212GB).

**Where the owner can get a properly licensed track** (budget is 0, so free sources only unless the owner approves spending):
1. **YouTube Audio Library** (YouTube Studio → Audio Library). Filter by mood (e.g. "Dramatic", "Calm") and duration. Prefer tracks marked **no attribution required**. If a track requires attribution, the exact credit line must go in the description. Check that track's license terms on the page **before** using it in our shared render, because the same file also goes to TikTok. If the terms don't clearly cover non-YouTube use, use option 2 on TikTok instead. To put a track in our render: save it to `media/audio/`, then add a manifest row with type `licensed-audio`, source = YouTube Audio Library + track/artist, license URL/terms, status CLEARED.
2. **Platform in-app sounds, added at upload time, NOT in our render:**
   - **TikTok:** "Add sound" in the upload editor. If the account is a **Business** account, only the **Commercial Music Library** is allowed. Personal accounts can use the general library, but only inside TikTok.
   - **YouTube Shorts:** "Add sound" in the Shorts upload/creation flow (YouTube's licensed Shorts library).
   - Consequences: the track is chosen separately per platform. It does **not** carry over between platforms, so never re-upload a TikTok download to YouTube or the reverse. It is not in our DRAFT, so QC and the approver must also approve the **track name and in-app volume** (keep it low under VO, about 15–25 % in the app slider if there is VO; it can be louder for text-only). Record the chosen track per platform in the approval request.
3. **A paid library the owner already holds** (e.g. Epidemic Sound or Artlist), only if the account/plan covers this channel and both platforms. Save the license certificate/URL in the manifest row. No new subscriptions without approval (budget 0).

Not allowed: game radio, GTA trailer music, streamer audio, "no copyright intended" uploads, random "royalty free" YouTube re-uploads, or TikTok-trending songs ripped into our render.

---

## 3. SFX (optional, licensed or self-made only)

Keep it subtle. Two or three hits are enough on a 30 s explainer.
| Time (s) | Cut / event | Suggestion |
|---|---|---|
| 0.0 | Hook card | Soft clock tick or single low "boom-tick" under the first word (very quiet). |
| 9.0 → 10.4 | 05a → 05b sweep | Short airy whoosh (0.3 s) as the midnight highlight moves. |
| 15.0 / 16.0 / 17.0 | 07a → 07b → 07c sweep | Quick whoosh or rising tick sequence. |
| 20.3 | "Not on PS4" strike-through | Muted low hit / "thunk" (not a buzzer, and not any console UI sound). |
| 22.5 | Download bar | Soft UI blip (self-made, **not** a PlayStation system sound). |
| 30.5 | End | No sting. Let the music tail out. |

Sources: YouTube Audio Library sound effects (check terms as above), or self-made with ffmpeg (e.g. filtered `anoisesrc` whoosh, short `sine` blip). `render_short.py` has no SFX track, so SFX must be pre-mixed into the music bed or added in the Resolve/CapCut polish pass (A3). Each SFX file needs its own manifest row. Never use PlayStation/Xbox system sounds or game sounds.

---

## 4. Levels

| Element | Target |
|---|---|
| VO | **-14 LUFS integrated**, true peak ≤ -1.5 dBTP, pre-normalised (see prep command). `edit.json` `"volume": 1.0`. |
| Music | Bed about 18–22 dB under VO in speech. Start with `"volume": 0.15`, `"duck": true` (the renderer sidechains music from the VO: threshold 0.03, ratio 8, attack 20 ms, release 350 ms). |
| Music, text-only version (no VO) | If music goes in our render without VO, set the volume so the whole file lands near -14 LUFS (start around 0.6–0.8 and measure). No ducking applies. |
| Game audio | n/a (no gameplay). Normally 0.2–0.4 under VO. |
| SFX | Peaks at least 6 dB below VO peaks. |
| Output | About -14 LUFS integrated (±1 LU), TP ≤ -1 dBTP. The renderer's `alimiter` caps at 0.95. |

`edit.json` additions once files are CLEARED:
```json
"voiceover": {"file": "media/audio/GTA6-20261118-001_vo.wav", "volume": 1.0},
"music": {"file": "media/audio/<cleared_track_file>", "volume": 0.15, "duck": true}
```
Then: `python3 tools/render_short.py posts/GTA6-20261118-001/edit.json` → `python3 tools/validate_export.py media/exports/GTA6-20261118-001_DRAFT.mp4 --min 10 --max 60` → loudnorm summary. If VO sits below about -16 LUFS in the mix, or music is audible over words, change `volume` and re-render.

---

## 5. Owner decision needed (status ON_HOLD)

**Option A — VO version (playbook default):** provide **one** of:
- `media/audio/GTA6-20261118-001_vo.wav` (owner's own voice, or exported from a licensed AI voice whose plan covers commercial YouTube + TikTok use), plus the provider name and terms URL for the manifest; **or**
- a configured licensed AI voice provider + API key (and owner approval of any cost, since the budget is 0), so the VO can be generated from the script above.

**Plus, optionally, music:** either a licensed file in `media/audio/` with source + license URL (e.g. YouTube Audio Library, terms confirmed to cover TikTok), **or** a decision to add in-app music at upload on each platform.

**Option B — text-only + platform in-app music (valid under the playbook, owner's choice):** the playbook says that until a voice provider is configured "drafts render with on-screen text only and VO is ON_HOLD". Nothing in it forbids publishing a captions-only video, and in-app platform sounds are licensed by the platform for use on that platform, so they are not "unlicensed music". In this option, the current silent DRAFT is the master. Music is added per platform at upload, and the approver signs off on the track name and volume. Trade-off: a silent or music-only Short usually holds attention less well than a voiced one. But this post is time-critical (the rolling PS5 launch is already under way: per our own conversion NZ went live 11:00 UK on 18 Nov, and Rome is at about 00:00 CET 19 Nov as of this note), so B is the fastest legal path. Producer note, outside the sound scope: by the time this posts, several cards (e.g. the "11am UK, November 18" conversion) describe moments that have already passed, so the timeliness of the wording should be re-checked at approval. If B is chosen, the next step is VIDEO_QC on the existing DRAFT. The sound step adds nothing to the file.
