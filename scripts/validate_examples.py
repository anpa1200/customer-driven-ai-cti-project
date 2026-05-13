#!/usr/bin/env python3
"""Validate synthetic practitioner package artifacts."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_CSV_HEADERS = {
    "examples/registers/evidence-register.csv": [
        "evidence_id",
        "date_utc",
        "source_id",
        "source_type",
        "claim",
        "artifact",
        "admiralty_rating",
        "confidence",
        "owner",
        "status",
    ],
    "examples/registers/pir-register.csv": [
        "pir_id",
        "decision_owner",
        "decision",
        "question",
        "time_horizon",
        "status",
        "confidence_threshold",
    ],
    "examples/registers/sir-register.csv": [
        "sir_id",
        "pir_id",
        "question",
        "data_source",
        "evidence_type",
        "owner",
        "due_date",
        "status",
    ],
    "examples/datasets/cloud_identity_events.csv": [
        "event_time_utc",
        "event_source",
        "user",
        "src_ip",
        "operation",
        "target",
        "result",
        "correlation_id",
    ],
}

REQUIRED_FILES = [
    "examples/rules/privileged-mfa-backup-deletion.yml",
    "examples/queries/sentinel-kql-privileged-mfa-backup-deletion.kql",
    "examples/queries/splunk-cloud-identity-backup-deletion.spl",
    "examples/replay/replay-cloud-identity.py",
    "examples/gates/gate-a-pir-approval.md",
    "examples/gates/gate-b-scenario-approval.md",
    "examples/gates/gate-c-hunt-approval.md",
    "examples/gates/gate-d-detection-design-approval.md",
    "examples/gates/gate-e-production-approval.md",
    "examples/gates/gate-f-final-delivery-approval.md",
    "examples/reports/executive-report.md",
    "static/img/workflow-output/01-register-dashboard.svg",
    "static/img/workflow-output/02-replay-output.svg",
    "static/img/workflow-output/03-gate-status.svg",
    "static/img/workflow-output/04-executive-summary.svg",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_csv_headers() -> None:
    for rel_path, expected in REQUIRED_CSV_HEADERS.items():
        path = ROOT / rel_path
        if not path.exists():
            fail(f"missing CSV file: {rel_path}")
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            try:
                actual = next(reader)
            except StopIteration:
                fail(f"empty CSV file: {rel_path}")
        if actual != expected:
            fail(f"unexpected headers in {rel_path}: {actual}")


def validate_required_files() -> None:
    for rel_path in REQUIRED_FILES:
        path = ROOT / rel_path
        if not path.exists():
            fail(f"missing required file: {rel_path}")
        if path.stat().st_size == 0:
            fail(f"empty required file: {rel_path}")


def validate_sigma() -> None:
    sigma = (ROOT / "examples/rules/privileged-mfa-backup-deletion.yml").read_text(encoding="utf-8")
    for token in ["title:", "id:", "logsource:", "detection:", "condition:", "level: high"]:
        if token not in sigma:
            fail(f"Sigma rule missing token: {token}")


def validate_queries() -> None:
    kql = (ROOT / "examples/queries/sentinel-kql-privileged-mfa-backup-deletion.kql").read_text(encoding="utf-8")
    spl = (ROOT / "examples/queries/splunk-cloud-identity-backup-deletion.spl").read_text(encoding="utf-8")
    if "AuditLogs" not in kql or "AzureActivity" not in kql:
        fail("KQL query must reference AuditLogs and AzureActivity")
    if "saw_mfa_change=1" not in spl or "saw_backup_delete=1" not in spl:
        fail("SPL query must include MFA and backup deletion predicates")


def validate_replay_result() -> None:
    result_path = ROOT / "examples/replay/replay-result.json"
    if not result_path.exists():
        return
    result = json.loads(result_path.read_text(encoding="utf-8"))
    if result.get("alert_count") != 1:
        fail("replay-result.json must contain exactly one alert")


def main() -> None:
    validate_required_files()
    validate_csv_headers()
    validate_sigma()
    validate_queries()
    validate_replay_result()
    print("Example artifact validation passed.")


if __name__ == "__main__":
    main()
