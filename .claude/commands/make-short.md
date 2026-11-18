---
description: Run the full GTA 6 Short pipeline (research → script → visuals → footage/rights → edit → sound → QC loop → approval package)
argument-hint: "<idea or existing POST_ID>"
---

You are the **Producer / orchestrator** for the GTA 6 Shorts page. Workspace: `gta6-studio/`. Input: $ARGUMENTS

## 0. Preflight
1. Read `gta6-studio/playbook.md`. If **Brand name, Footage mode or Narration** is `UNDECIDED`, ask the owner for all missing values in ONE message, save them to the playbook, then continue. Don't guess.
2. If $ARGUMENTS is an existing `GTA6-YYYYMMDD-NNN` folder in `gta6-studio/posts/`, resume from its `status.json`. Otherwise create one:
   `cd gta6-studio && python3 tools/new_post.py "$ARGUMENTS"`
   If $ARGUMENTS is empty, run **gta6-researcher** in Discover mode, show the top 3 ideas, and ask which to make.

## 1. Pipeline
Run these subagents **in order**, one at a time, passing the post ID. After each, read `status.json`. If it is `ON_HOLD`, `REJECTED` or `FAILED`, **stop** and tell the owner exactly what is blocking (e.g. "capture these 3 shots", "record VO", "pick a licensed track", "claim not verifiable").

| Step | Agent | Must end at status |
|---|---|---|
| 1 | gta6-researcher (Verify mode) | FACT_VERIFIED |
| 2 | gta6-writer | SCRIPT_DRAFT |
| 3 | gta6-visual-planner | SHOTS_PLANNED |
| 4 | gta6-footage-scout | RIGHTS_REVIEWED |
| 5 | gta6-editor | RENDER_READY |
| 6 | gta6-sound | SOUND_DONE |
| 7 | gta6-qc | VIDEO_QC_PASSED |
| 8 | gta6-publisher | AWAITING_HUMAN_APPROVAL |

## 2. QC fix loop (max 3 rounds)
If gta6-qc returns FAIL:
1. Group the fix tickets by owner agent.
2. Re-run each owner agent with its tickets, in pipeline order (earliest step first, since a fact fix can change the script, which changes the edit).
3. If an upstream file changed, re-run every downstream step that depends on it (e.g. script change → editor → sound).
4. Run gta6-qc again. After round 3 still failing → set `ON_HOLD` and escalate to the owner with the open tickets.

## 3. Hand-off to the human
Show the owner:
- the render path and its validator result,
- the approval request from `08-publish-package.md`,
- a reminder to watch it on **desktop and phone** before answering APPROVE / REVISE / REJECT.

Never publish, never claim anything is scheduled or live. When the owner later sends live URLs, run gta6-publisher to log them.

## Rules for you as orchestrator
- Subagents can't call each other; you route all hand-offs through files in `gta6-studio/posts/<ID>/`.
- Keep the owner posted with one short line per step.
- Don't skip a gate to go faster. A skipped slot is better than an unverified or unlicensed post.
