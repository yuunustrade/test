#!/usr/bin/env python3
"""Create a new post folder with a unique ID and status file.

Usage:
    python3 tools/new_post.py "<one-line idea>" [--pillar discovery] [--date YYYYMMDD]

Creates posts/GTA6-YYYYMMDD-NNN/status.json and prints the ID.
"""
import datetime
import json
import os
import sys

STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATUSES = [
    "IDEA_NEW", "RESEARCHING", "FACT_VERIFIED", "SCRIPT_DRAFT", "SHOTS_PLANNED",
    "RIGHTS_REVIEWED", "EDITING", "RENDER_READY", "SOUND_DONE", "VIDEO_QC_PASSED",
    "AWAITING_HUMAN_APPROVAL", "POST_APPROVED", "SCHEDULED", "PUBLISHED_VERIFIED",
    "METRICS_12H", "METRICS_24H", "METRICS_72H", "ARCHIVED",
    "ON_HOLD", "REJECTED", "FAILED", "TAKEDOWN_REVIEW",
]


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("--"):
        print(__doc__)
        sys.exit(1)
    idea = args[0]
    pillar = args[args.index("--pillar") + 1] if "--pillar" in args else "undecided"
    try:
        import zoneinfo
        now = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Rome"))
    except Exception:
        now = datetime.datetime.utcnow()
    date = args[args.index("--date") + 1] if "--date" in args else now.strftime("%Y%m%d")

    posts = os.path.join(STUDIO, "posts")
    n = 1
    while os.path.exists(os.path.join(posts, f"GTA6-{date}-{n:03d}")):
        n += 1
    pid = f"GTA6-{date}-{n:03d}"
    folder = os.path.join(posts, pid)
    os.makedirs(folder)
    status = {
        "post_id": pid,
        "idea": idea,
        "pillar": pillar,
        "status": "IDEA_NEW",
        "fact_ids": [],
        "asset_ids": [],
        "render_path": None,
        "qc_rounds": 0,
        "approval_status": "pending",
        "publish_status": "draft",
        "platforms": ["youtube_shorts", "tiktok"],
        "timezone": "Europe/Rome",
        "scheduled_local": None,
        "live_urls": {},
        "history": [{"at": now.isoformat(timespec="minutes"), "status": "IDEA_NEW", "by": "new_post"}],
        "errors": [],
        "allowed_statuses": STATUSES,
    }
    with open(os.path.join(folder, "status.json"), "w") as f:
        json.dump(status, f, indent=2)
    print(pid)


if __name__ == "__main__":
    main()
