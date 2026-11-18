# Footage & rights: GTA6-20261118-001

Reviewed by: footage_scout (rights clerk), 2026-11-18 (time approximate)
Footage mode: news-explainer. All visuals are our own original graphics. No gameplay, official media, creator clips, logos or third-party images are used.

## Checks performed
- **Files and format:** ffprobe confirms all 16 files in `media/graphics/GTA6-20261118-001_*.png` exist, decode as PNG and are 1080x1920. They are static images, so "in/out" means hold duration.
- **Generator:** `posts/GTA6-20261118-001/make_graphics.py` builds every image with `Image.new` plus Pillow drawing primitives and text. It has no `Image.open`, no network or URL access and no external image paths. The only external files it reads are two fonts.
- **Reproducibility:** I re-ran the generator into a scratch directory. All 16 outputs are pixel-identical to the files in `media/graphics/`, so the generator script is the full provenance.
- **Fonts:**
  - `Inter-Bold.otf` / `Inter-SemiBold.otf` come from the Debian package `fonts-inter`. Per `/usr/share/doc/fonts-inter/copyright` the licence is OFL-1.1 and Apache-2.0. OFL states that its terms do not apply to documents created with the fonts.
  - `DejaVuSansMono-Bold.ttf` comes from the package `fonts-dejavu-mono`. Per `/usr/share/doc/fonts-dejavu-mono/copyright` it uses the Bitstream Vera licence, a permissive font licence. That package's GPL-2+ applies only to `debian/*` packaging.
  - Both licences permit use in rendered video.
- **Visual inspection** (contact sheet of all 16): only shapes, clocks, icons and text. There are no logos, key art, trailer frames, console images or store/console UI.
- **Trademark text:** "PS5" (G01, G04, G09) and "PS4" (G09) appear only as plain-text badges in Inter. These are nominative references with no logo artwork. There is no "GTA" wordmark or Rockstar/PlayStation/Xbox branding.
- **On-screen source lines:** G04, G05A and G05B carry the baked-in line "Source: PlayStation Blog, 10 Nov 2026". This is a text attribution only. G06 carries the baked-in "OUR CONVERSION" pill and the line "not an official time".
- **Spoilers:** none.
- **Brand/handle:** none printed, which matches the playbook placeholder rule.

## Shot to asset map
| Beat | Time | asset_id | File | In/out (hold) | Rights status |
|---|---|---|---|---|---|
| 1 | 00:00.0-00:02.0 | GTA6-20261118-001-G01 | media/graphics/GTA6-20261118-001_01_hook_clock_ps5.png | 0-2.0 s | CLEARED |
| 2 | 00:02.0-00:04.2 | GTA6-20261118-001-G02 | media/graphics/GTA6-20261118-001_02_world_clocks.png | 0-2.2 s | CLEARED |
| 3 | 00:04.2-00:06.5 | GTA6-20261118-001-G03 | media/graphics/GTA6-20261118-001_03_calendar_19nov.png | 0-2.3 s | CLEARED |
| 4 | 00:06.5-00:09.0 | GTA6-20261118-001-G04 | media/graphics/GTA6-20261118-001_04_clock_midnight.png | 0-2.5 s | CLEARED (source line baked in) |
| 5a | 00:09.0-00:10.4 | GTA6-20261118-001-G05A | media/graphics/GTA6-20261118-001_05a_sweep_nz.png | 0-1.4 s | CLEARED (source line baked in) |
| 5b | 00:10.4-00:11.8 | GTA6-20261118-001-G05B | media/graphics/GTA6-20261118-001_05b_sweep_2.png | 0-1.4 s | CLEARED (source line baked in) |
| 6 | 00:11.8-00:15.0 | GTA6-20261118-001-G06 | media/graphics/GTA6-20261118-001_06_nz_uk_conversion.png | 0-3.2 s | CLEARED (OUR CONVERSION tag baked in) |
| 7a | 00:15.0-00:16.0 | GTA6-20261118-001-G07A | media/graphics/GTA6-20261118-001_07a_sweep_3.png | 0-1.0 s | CLEARED |
| 7b | 00:16.0-00:17.0 | GTA6-20261118-001-G07B | media/graphics/GTA6-20261118-001_07b_sweep_4.png | 0-1.0 s | CLEARED |
| 7c | 00:17.0-00:17.8 | GTA6-20261118-001-G07C | media/graphics/GTA6-20261118-001_07c_sweep_all.png | 0-0.8 s | CLEARED |
| 8 | 00:17.8-00:20.3 | GTA6-20261118-001-G08 | media/graphics/GTA6-20261118-001_08_timezones_info.png | 0-2.5 s | CLEARED |
| 9 | 00:20.3-00:22.5 | GTA6-20261118-001-G09 | media/graphics/GTA6-20261118-001_09_not_ps4.png | 0-2.2 s | CLEARED |
| 10 | 00:22.5-00:25.0 | GTA6-20261118-001-G10 | media/graphics/GTA6-20261118-001_10_download_bar.png | 0-2.5 s | CLEARED |
| 11 | 00:25.0-00:27.8 | GTA6-20261118-001-G11 | media/graphics/GTA6-20261118-001_11_storage_212gb.png | 0-2.8 s | CLEARED |
| 12 | 00:27.8-00:30.5 | GTA6-20261118-001-G12 | media/graphics/GTA6-20261118-001_12_end_info.png | 0-2.7 s | CLEARED |
| spare | - | GTA6-20261118-001-G00 | media/graphics/GTA6-20261118-001_00_bg_dark.png | any | CLEARED (fallback/padding) |

All rows are recorded in `data/asset_manifest.csv`.

## Audio
- No music or SFX is cleared in `data/asset_manifest.csv`. **Audio is pending the sound agent.**
- VO is ON_HOLD under the playbook because no licensed voice provider is configured.
- Until the sound agent clears a licensed or owned file, render silent. Do not add any track or tick SFX that has no manifest row.
- No game audio is used.

## Official media / creator clips
- None used and none needed. Nothing was added to `watchlist.md`, and no permission requests were drafted.

## Capture list for the owner
- None. Every planned visual shot has a CLEARED asset.
