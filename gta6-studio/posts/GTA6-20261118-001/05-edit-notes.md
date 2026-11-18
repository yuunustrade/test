# 05 — Edit notes: GTA6-20261118-001

**Draft render:** `media/exports/GTA6-20261118-001_DRAFT.mp4` (30.51 s, 1080x1920, H.264 + silent AAC, 30 fps)
**EDL:** `posts/GTA6-20261118-001/edit.json`
**Editor time:** ~23:55 Europe/Rome, 18 Nov 2026 (approximate)

## Inputs and rights
- All 15 segments use original graphics G01–G12 (incl. G05A/B, G07A/B/C). Every file has a `CLEARED` row in `data/asset_manifest.csv`. G00 (spare) not used.
- No voiceover and no music in the EDL: none is cleared yet (VO ON_HOLD, music pending the sound agent). The draft is intentionally silent (AAC track present, max volume -91 dB). No game audio exists.

## Cut / structure
- Nothing was cut. 15 image segments in shot-plan order, durations exactly as planned (2.0, 2.2, 2.3, 2.5, 1.4, 1.4, 3.2, 1.0, 1.0, 0.8, 2.5, 2.2, 2.5, 2.8, 2.7 = 30.5 s).
- All context needed for accuracy is kept: the baked-in "Source: PlayStation Blog, 10 Nov 2026" line (beats 4–5) and the "OUR CONVERSION / not an official time" tag (beat 6) are part of the graphics and stay up for their whole cards.

## Crop / framing
- All segments `framing: "fit"`. The PNGs are native 1080x1920, so nothing is cropped or scaled. No zoom applied (the optional 1.00→1.04 push is not supported by the renderer for images; left for the polish pass).

## Captions
- Text = the **Narration (exact words)** column of 02-script.md, word for word, including punctuation, so captions will match the VO when it is recorded. (The shot plan's caps-styled "On-screen text" variants were not used; the editor spec requires narration match.)
- Position `lower` (renderer: DejaVu Sans Bold 76, MarginV 620).
- A calibration render showed that lines wider than ~910 px (PIL-measured at 76 px) auto-wrap, which pushed 4 of the cards to 3–4 lines. To keep every card at ≤ 2 lines without changing words, I used explicit `\n` breaks and split five long beats into two consecutive cards at their natural pause (each split also lines up with an existing segment change where one exists):
  - Beat 5: "Country by country," (9.0–10.4) / "starting in\nNew Zealand." (10.4–11.8) — matches 5a/5b.
  - Beat 7: "Your turn:" (15.0–16.0) / "when your country\nhits midnight." (16.0–17.8) — matches 7a / 7b+7c.
  - Beat 8: "Several time zones?" (17.8–19.0) / "Check\nPlayStation Support." (19.0–20.3).
  - Beat 10: "Pre-ordered?" (22.5–23.5) / "Pre-load opened\nNovember 10." (23.5–25.0).
  - Beat 12: "Xbox player?" (27.8–28.9) / "Check Rockstar\nSupport for times." (28.9–30.5).
- Result: 17 caption cards, every card 1–2 lines and ≤ 7 words; concatenated text equals the 75-word narration.

## Frame check (every caption card)
Frames `media/edits/GTA6-20261118-001_frame_1.png` … `_frame_17.png`, one per caption card (mid-card timestamps 1.0, 3.1, 5.35, 7.75, 9.7, 11.1, 13.4, 15.5, 16.9, 18.4, 19.65, 21.4, 23.0, 24.25, 26.4, 28.35, 29.7 s). Viewed all 17, plus pixel measurement:
- Caption text bounding box over all cards: x 133–885, y 1159–1298. All cards are 1 or 2 lines, none wraps.
- Graphic content ends at y ≈ 1060 at the lowest point (source line on beats 4–5, y 1030–1060), so there is a gap of at least ~100 px. **No caption overlaps any graphic.**
- Platform UI: bottom 20 % starts at y 1536, right 12 % at x 950. Captions clear both by 238 px (vertical) and 65 px (horizontal).
- Subject in frame on every card. "OUR CONVERSION" pill and "not an official time" visible throughout beat 6; source line visible through beats 4–5; PS4 strike-through legible.
- Minor cosmetic: renderer margins (L110/R170) put caption centre ~30 px left of frame centre; graphics are centred. Not a readability issue.

## Validator
```
$ python3 tools/validate_export.py media/exports/GTA6-20261118-001_DRAFT.mp4 --min 10 --max 60
file:     media/exports/GTA6-20261118-001_DRAFT.mp4
duration: 30.51s
sha256:   01d368c20e2c6f08791adee22779b2c0b26f4583eee22cb0273d6aa434fb07bc
RESULT: PASS (technical spec only — human must still watch it on desktop AND phone)
```

## Polish recipe (DaVinci Resolve or CapCut)
1. New 1080x1920, 30 fps timeline. Import the 15 PNGs from `media/graphics/GTA6-20261118-001_*.png` and lay them out with the durations above (or import the DRAFT as a reference track).
2. Optional slow push-in on each still: Transform zoom 1.00→1.04 over the clip (Resolve: Inspector keyframes or Dynamic Zoom; CapCut: Animation → In "Zoom in" slow / keyframes). Keep the source line and the OUR CONVERSION pill inside the frame.
3. Hard cuts throughout; for 5a→5b and 7a→7b→7c a 2–4 frame cross-dissolve makes the sweep feel animated.
4. Captions: import the 17 cards from `edit.json` (or retype word for word), bold sans 70–80 px, white with black outline, centred horizontally, bottom of text box at y ≈ 1300. Keep ≤ 2 lines.
5. When the sound agent clears VO/music: drop VO on A1, retime caption cards to the VO waveform (same split points), music on A2 at about -20 dB ducked under VO. Do not add any audio without a CLEARED manifest row.
6. Export H.264 1080x1920, 30 fps, AAC 48 kHz, then re-run `tools/validate_export.py`.
