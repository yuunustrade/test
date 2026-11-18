# QC checklist: [POST_ID] — round [N]

Every item must be PASS for VIDEO_QC_PASSED. Any FAIL routes back to the owning agent.

| # | Check | Owner if FAIL | PASS/FAIL | Evidence / note |
|---|---|---|---|---|
| 1 | Every factual statement maps to a confirmed FACT-ID with a source URL | researcher | | |
| 2 | No rumor/leak/"confirmed"/"secret"/"first" wording without proof | writer | | |
| 3 | Hook (0–2 s) is supported by what is actually on screen | writer / visual-planner | | |
| 4 | There is a real payoff in the video, not only in the caption | writer | | |
| 5 | Every asset in edit.json has a CLEARED row in asset_manifest.csv | footage-scout | | |
| 6 | No leaked/pre-release footage, isolated cutscenes, major spoilers | footage-scout | | |
| 7 | No AI imagery presented as gameplay; illustrations labeled | visual-planner | | |
| 8 | Captions match narration word-for-word and on-screen action | editor | | |
| 9 | Critical detail is not cropped out of the 9:16 frame | editor | | |
| 10 | Captions inside safe zone (not under platform UI) | editor | | |
| 11 | validate_export.py PASS (1080x1920, h264, aac, duration) | editor | | |
| 12 | All music/SFX licensed for the platform; no game radio/trailer audio | sound | | |
| 13 | Speech clearly audible over music/game audio | sound | | |
| 14 | No implied Rockstar/Take-Two affiliation | publisher-prep | | |
| 15 | Per-platform captions accurate, credited, not copied across platforms | publisher-prep | | |

Verdict: PASS | FAIL (route to: ...)
Note: automated QC cannot watch the video like a human. The owner must still watch on desktop AND phone.
