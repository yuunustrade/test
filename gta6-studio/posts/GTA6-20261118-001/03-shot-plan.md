# Shot plan: GTA6-20261118-001

Pillar: news
Viewer promise: In ~30 s you know when GTA 6 unlocks on your PS5 (midnight local time, country by country, NZ first) and what to check before then.
Runtime target: 30.5 s (12 caption cards, text-only render; VO ON_HOLD)
Footage mode: news-explainer. ALL visuals are original graphics made by us. No gameplay, no Rockstar/PlayStation/Xbox logos, key art, trailer frames or store/console UI. Platform names appear only as plain text.
Verified claims used: FACT-0001, FACT-0002, FACT-0003, FACT-0006
Unverified interpretations (NOT to be stated as fact): any Xbox console or pre-load time (FACT-0004/0007), PC status (FACT-0008), per-time-zone unlocks inside multi-zone countries, unlock times for any country other than NZ. The NZ=UK 11:00 time is OUR CONVERSION and is labelled inside the graphic.
Spoiler level: none

**Graphic prefix:** `G_` = `media/graphics/GTA6-20261118-001_`. All are 1080x1920 PNG with framing `fit` (it is the native size, so nothing is cropped). Images are static. The editor may add a slow 1.00→1.04 zoom per segment if the renderer supports it; this is optional.
**Safe zones (checked against tools/render_short.py):** lower captions use MarginV 620, so caption text occupies roughly y 1100–1300. All graphic content sits in x 80–950, y 160–1070. Nothing important is in the bottom 620 px or the right 130 px. The top ~150 px is empty too (platform header).
**Captions:** burned in by the editor at `position: "lower"`, using the exact on-screen text from 02-script.md. The graphics deliberately do not repeat the caption sentences. Exceptions: the "OUR CONVERSION / not an official time" tag (beat 6) and the source line (beats 4–5) are baked into the graphic so they stay visible for the whole card, as the script requires.
**Audio (all beats):** text-only render, VO ON_HOLD. Music only if a licensed track is cleared in asset_manifest (none yet), otherwise silent or a short tick SFX that we own. No game audio exists.

| # | Time | Narration (VO) | On-screen text (caption) | Story function | Visual source + in/out | Framing | Audio | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 00:00.0–00:02.0 | When does GTA 6 hit your PS5? | WHEN DOES GTA 6 HIT YOUR PS5? | Hook: open the question | `G_01_hook_clock_ps5.png` 0–2.0 s | fit | VO (on hold) | HOOK FRAME. Large pink clock with a teal "?" bubble and a plain-text "PS5" badge (no logo). It shows exactly what the hook asks: a time question about PS5. |
| 2 | 00:02.0–00:04.2 | Not everywhere at the same moment. | Not everywhere at the same moment. | Context: rolling launch | `G_02_world_clocks.png` 0–2.2 s | fit | VO | Five unlabelled clocks, each showing a different time, plus wave lines. Unlabelled on purpose, so no country time is implied. FACT-0003 |
| 3 | 00:04.2–00:06.5 | Release day: November 19, 2026. | RELEASE DAY: 19 NOV 2026 | Context: date | `G_03_calendar_19nov.png` 0–2.3 s | fit | VO | Calendar page: NOV / 19 / 2026. FACT-0001 |
| 4 | 00:06.5–00:09.0 | On PS5, it's midnight local time. | PS5: MIDNIGHT, LOCAL TIME | Demo: the rule | `G_04_clock_midnight.png` 0–2.5 s | fit | VO | Clock at 00:00 with a digital "00:00" readout and a small plain-text PS5 badge. The baked-in source line reads "Source: PlayStation Blog, 10 Nov 2026" (y≈1042). FACT-0003 |
| 5a | 00:09.0–00:10.4 | Country by country, starting in New Zealand. | Country by country. Starts: New Zealand. | Demo: NZ first | `G_05a_sweep_nz.png` 0–1.4 s | fit | VO | Clock strip. Only the "NZ" clock is lit pink at 00:00. A WESTWARD arrow is shown, and the source line stays. FACT-0003 |
| 5b | 00:10.4–00:11.8 | (cont.) | (same caption continues) | Demo: sweep begins | `G_05b_sweep_2.png` 0–1.4 s | fit | VO | The second clock lights up. The other clocks are unlabelled, so no country is named. Source line stays. |
| 6 | 00:11.8–00:15.0 | Our math: 11am UK time, November 18. | NZ midnight = 11:00 UK, 18 Nov / OUR CONVERSION | Demo: concrete example | `G_06_nz_uk_conversion.png` 0–3.2 s | fit | VO | NZ clock "00:00 19 NOV" = UK clock "11:00 18 NOV". The yellow "OUR CONVERSION" pill and the line "not an official time" are baked in, so they stay visible for the whole card. Arithmetic: 00:00 NZDT (UTC+13) 19 Nov = 11:00 GMT 18 Nov. |
| 7a | 00:15.0–00:16.0 | Your turn: when your country hits midnight. | YOUR TURN = YOUR COUNTRY'S MIDNIGHT | Payoff | `G_07a_sweep_3.png` 0–1.0 s | fit | VO | The sweep continues (3 lit). No source line, because this is a recap of the same claim. FACT-0003 |
| 7b | 00:16.0–00:17.0 | (cont.) | (cont.) | Payoff | `G_07b_sweep_4.png` 0–1.0 s | fit | VO | 4 lit |
| 7c | 00:17.0–00:17.8 | (cont.) | (cont.) | Payoff | `G_07c_sweep_all.png` 0–0.8 s | fit | VO | All 5 lit |
| 8 | 00:17.8–00:20.3 | Several time zones? Check PlayStation Support. | Several time zones? Check PlayStation Support. | Payoff: caveat | `G_08_timezones_info.png` 0–2.5 s | fit | VO | Three clocks one hour apart and an "i" info icon. No logo or page screenshot. It makes no claim about how multi-zone countries unlock. |
| 9 | 00:20.3–00:22.5 | Heads up: it's not on PS4. | Heads up: NOT on PS4 | Payoff: platform | `G_09_not_ps4.png` 0–2.2 s | fit | VO | Plain-text "PS4" badge (grey, red strike-through) and "PS5" badge with a green tick. No console images or logos. FACT-0002 |
| 10 | 00:22.5–00:25.0 | Pre-ordered? Pre-load opened November 10. | Pre-ordered? Pre-load opened 10 Nov | Close: action | `G_10_download_bar.png` 0–2.5 s | fit | VO | Generic download arrow icon, a full bar with "100%" and a "10 NOV" tag. It does not imitate PlayStation UI. FACT-0006 |
| 11 | 00:25.0–00:27.8 | You need at least 212GB free. | Need at least 212GB free | Close: action | `G_11_storage_212gb.png` 0–2.8 s | fit | VO | Generic drive icon, "212GB" in large type and a storage bar with a "MIN" marker. FACT-0006 |
| 12 | 00:27.8–00:30.5 | Xbox player? Check Rockstar Support for times. | Xbox player? Check Rockstar Support for times. | Close / end card | `G_12_end_info.png` 0–2.7 s | fit | VO | Neutral "?" circle with no logos and no Xbox time. End on this card: no handle, no follow bait. |

Spare: `G_00_bg_dark.png` is the plain brand background (the same gradient and faint grid, with no content). Use it as a fallback or a padding frame. No beat requires it.

Visual changes: 15 segments in 30.5 s. The longest hold is 3.2 s (beat 6, a dense comparison card that needs reading time). In the hook and demo (0–15 s), every change comes within 1.4–3.2 s. There is no dead air.

### Graphic → beat index
| File | Beat(s) |
|---|---|
| media/graphics/GTA6-20261118-001_00_bg_dark.png | spare / fallback |
| media/graphics/GTA6-20261118-001_01_hook_clock_ps5.png | 1 (hook) |
| media/graphics/GTA6-20261118-001_02_world_clocks.png | 2 |
| media/graphics/GTA6-20261118-001_03_calendar_19nov.png | 3 |
| media/graphics/GTA6-20261118-001_04_clock_midnight.png | 4 |
| media/graphics/GTA6-20261118-001_05a_sweep_nz.png | 5a |
| media/graphics/GTA6-20261118-001_05b_sweep_2.png | 5b |
| media/graphics/GTA6-20261118-001_06_nz_uk_conversion.png | 6 |
| media/graphics/GTA6-20261118-001_07a_sweep_3.png | 7a |
| media/graphics/GTA6-20261118-001_07b_sweep_4.png | 7b |
| media/graphics/GTA6-20261118-001_07c_sweep_all.png | 7c |
| media/graphics/GTA6-20261118-001_08_timezones_info.png | 8 |
| media/graphics/GTA6-20261118-001_09_not_ps4.png | 9 |
| media/graphics/GTA6-20261118-001_10_download_bar.png | 10 |
| media/graphics/GTA6-20261118-001_11_storage_212gb.png | 11 |
| media/graphics/GTA6-20261118-001_12_end_info.png | 12 |

Provenance: all 16 PNGs were generated programmatically with Pillow from shapes plus the Inter and DejaVu Sans Mono fonts (system fonts, OFL/free licences). The generator is `posts/GTA6-20261118-001/make_graphics.py`; to regenerate, run `python3 make_graphics.py media/graphics`. They contain no AI-generated imagery, no third-party art and no logos. The rights reviewer should add them to data/asset_manifest.csv as origin_type `original_graphic`.

## Shots still NEEDED (footage scout / owner to capture)
| Need ID | Exact description | Length | Must show | Suggested capture method |
|---|---|---|---|---|
| none | This is a graphics-only news-explainer. Every beat is covered by an original graphic above. No gameplay or official media is needed or allowed. | — | — | — |

Optional (not blocking): a licensed or owned music bed or tick SFX for the text-only render. No music file is cleared yet.
