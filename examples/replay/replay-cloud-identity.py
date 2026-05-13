#!/usr/bin/env python3
"""Replay the synthetic cloud identity dataset and evaluate the example detection."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "examples" / "datasets" / "cloud_identity_events.csv"
OUTPUT = ROOT / "examples" / "replay" / "replay-result.json"


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def main() -> None:
    events = []
    with DATASET.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            row["event_time"] = parse_time(row["event_time_utc"])
            events.append(row)

    alerts = []
    for event in events:
        if event["operation"] != "Add authentication method":
            continue
        user = event["user"]
        start = event["event_time"]
        end = start + timedelta(hours=2)
        matches = [
            candidate
            for candidate in events
            if candidate["user"] == user
            and start <= candidate["event_time"] <= end
            and candidate["operation"]
            in {
                "Microsoft.RecoveryServices/vaults/delete",
                "Microsoft.RecoveryServices/vaults/backupconfig/write",
            }
        ]
        if matches:
            alerts.append(
                {
                    "alert_name": "Privileged MFA Change Followed by Backup Deletion Attempt",
                    "actor": user,
                    "mfa_time_utc": event["event_time_utc"],
                    "matched_operations": [match["operation"] for match in matches],
                    "correlation_id": event["correlation_id"],
                    "result": "detected",
                }
            )

    result = {
        "dataset": str(DATASET.relative_to(ROOT)),
        "event_count": len(events),
        "alert_count": len(alerts),
        "alerts": alerts,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
