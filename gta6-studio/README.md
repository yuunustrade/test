# GTA 6 Studio — multi-agent Shorts pipeline

An independent, faceless GTA 6 short-video operation run by Claude Code subagents.
Built from the *GTA 6 Faceless Content Page Playbook* (18 Nov 2026).

## The team (`.claude/agents/`)

| # | Agent | Job | Writes |
|---|---|---|---|
| 1 | `gta6-researcher` | Finds ideas; verifies claims against official sources | `facts.md`, `01-research.md` |
| 2 | `gta6-writer` | Hook, story beats, timed script, platform copy | `02-script.md` |
| 3 | `gta6-visual-planner` | 9:16 shot plan, list of shots still needed | `03-shot-plan.md` |
| 4 | `gta6-footage-scout` | Matches shots to cleared footage, logs rights | `04-footage.md`, `data/asset_manifest.csv` |
| 5 | `gta6-editor` | Builds `edit.json`, renders draft MP4, validates | `edit.json`, `05-edit-notes.md`, `media/exports/` |
| 6 | `gta6-sound` | VO script, licensed music, mix and loudness | `06-sound.md` |
| 7 | `gta6-qc` | Audits everything; routes failures back | `07-qc.md` |
| 8 | `gta6-publisher` | Per-platform captions + approval request (never posts) | `08-publish-package.md` |
| 9 | `gta6-analyst` | 12/24/72h metrics, daily/weekly reports | `scoreboard.csv`, `reports/` |

## Commands

- `/make-short <idea>`: runs agents 1→8 with a QC fix loop (max 3 rounds), then hands you an approval request.
- `/make-short GTA6-20261119-001`: resumes a post (e.g. after you've captured missing shots).
- `/gta6-ideas [theme]`: finds and ranks new ideas.
- `/gta6-report daily | weekly | metrics <numbers>`: analytics.

## Status flow

```
IDEA_NEW → FACT_VERIFIED → SCRIPT_DRAFT → SHOTS_PLANNED → RIGHTS_REVIEWED → RENDER_READY
→ SOUND_DONE → VIDEO_QC_PASSED → AWAITING_HUMAN_APPROVAL → (you post) → PUBLISHED_VERIFIED
→ METRICS_12H/24H/72H → ARCHIVED          any step → ON_HOLD | REJECTED | FAILED | TAKEDOWN_REVIEW
```

## What you do (the human gates)

1. Fill the `UNDECIDED` lines in `playbook.md` (brand, footage mode, narration).
2. Drop your own gameplay captures into `media/raw/` (if footage mode is `own-capture`).
3. Record VO / pick licensed music when the sound agent asks.
4. Watch every draft on desktop **and** phone, answer APPROVE / REVISE / REJECT.
5. Post it yourself (or via Buffer), then paste the live URLs back.
6. Paste 12h/24h/72h numbers into `/gta6-report metrics`.

## Tools (`tools/`, run from `gta6-studio/`)

```bash
python3 tools/new_post.py "idea" --pillar discovery   # new post folder + ID
python3 tools/render_short.py posts/<ID>/edit.json    # draft 1080x1920 MP4 with captions, VO, ducked music
python3 tools/validate_export.py media/exports/<ID>_DRAFT.mp4 --min 10 --max 60
```

Needs `ffmpeg`/`ffprobe` and Python 3.9+. See `templates/edit.example.json` for the edit format.

## Hard limits (by design)

- No agent can post, schedule, spend money, or touch account settings.
- No agent downloads other creators' videos. Footage = your captures, cleared official media, written-permission submissions, or original graphics.
- Every claim needs a confirmed FACT with a primary source; every asset needs a CLEARED manifest row.
- Never store passwords, tokens or 2FA codes anywhere in this folder.
