---
id: complete-worked-case
title: Complete Worked Case
sidebar_label: Complete Worked Case
slug: /practitioner-package/complete-worked-case
description: Full synthetic PIR-to-detection-to-pilot-to-executive-report case.
---

# Complete Worked Case: Cloud Identity to Backup Deletion

This is a complete synthetic case. It is designed to show the full operating chain, not isolated examples.

## 1. Customer Decision

Meridian Freight Group's CISO needs to decide whether cloud identity activity against privileged administrators justifies a 30-day detection engineering sprint.

Customer profile:

| Field | Value |
|---|---|
| Organization | Meridian Freight Group |
| Sector | Logistics and cold-chain transportation |
| Crown jewel | Production backup vault for route optimization databases |
| Primary risk | Recovery failure after destructive cloud activity |
| Security stack | Entra ID, Azure Activity, Microsoft Sentinel, Defender for Endpoint |

Decision: approve or defer a 30-day detection engineering sprint for cloud identity and backup protection.

## 2. PIR

**PIR-001:** Are privileged cloud identities being used in a way that could enable backup deletion before ransomware deployment?

Decision owner: CISO  
Time horizon: 30 days  
Confidence threshold: Moderate

Normative check:

- The PIR **MUST** name a decision owner: CISO.
- The PIR **MUST** be time bounded: 30 days.
- The PIR **MUST** support a decision: approve or defer sprint.

## 3. SIRs

| SIR | Question | Data source | Closure |
|---|---|---|---|
| SIR-001 | Which privileged identities changed MFA settings before backup-resource activity? | Entra ID Audit Log | Closed |
| SIR-002 | Did any privileged session enumerate or modify backup vaults? | Azure Activity Log | Closed |
| SIR-003 | Can Sentinel detect the sequence with acceptable false-positive risk? | Microsoft Sentinel | Closed |

## 4. Collection

Collection tasks:

| Task | Source | Output |
|---|---|---|
| COL-001 | Entra ID Audit Log | MFA method changes for privileged users |
| COL-002 | Azure Activity Log | Backup vault read, write, and delete operations |
| COL-003 | Sentinel replay | Detection result and alert fields |
| COL-004 | SOC review | Pilot false-positive classification |

Collection constraints:

- Raw production logs **MUST NOT** be placed into this public repository.
- Synthetic replay data **MAY** be used for public validation.
- Customer-specific identifiers **MUST** be redacted or replaced.

## 5. CTI Analysis

The evidence register contains four accepted evidence items:

- EV-001: Privileged user registered a new MFA method.
- EV-002: Backup vault deletion was attempted.
- EV-003: Detection fired during replay.
- EV-004: Gate E approval granted with pilot conditions.

Assessment:

We assess with moderate confidence that the event pattern is consistent with a cloud identity pathway to recovery inhibition. The assessment is based on same-user, same-source-IP, short-window sequencing across MFA change and backup vault operations. The case does not attribute activity to a named threat actor.

Key analytic constraint:

TTP similarity **MUST NOT** be used as attribution. The case supports defensive prioritization, not actor naming.

## 6. Threat Modeling

An adversary obtains a privileged cloud administrator session, performs a suspicious MFA method change, enumerates backup resources, weakens protection, and attempts backup vault deletion.

ATT&CK mapping: T1098 Account Manipulation  
Primary data sources: Entra ID Audit Log and Azure Activity

Related behavior:

- T1098 Account Manipulation
- T1490 Inhibit System Recovery
- T1485 Data Destruction

Defensive mapping:

- Account monitoring
- Log analysis
- Cloud account monitoring

Mapping file: `examples/attack-mappings/det-001-attack-d3fend.yaml`

## 7. Telemetry Validation

Telemetry requirements:

| Requirement | Source | Status |
|---|---|---|
| MFA method changes | Entra ID Audit Log | Available |
| Backup vault read/write/delete | Azure Activity Log | Available |
| Actor correlation | User principal + correlation ID | Available |
| Replay validation | Synthetic CSV dataset | Available |

Telemetry schema:

- CSV dataset: `examples/datasets/cloud_identity_events.csv`
- Schema: `examples/schemas/telemetry-event.schema.json`
- Field mapping: `examples/telemetry-schema.md`

## 8. Hunt Hypothesis

If a privileged cloud account is being prepared for destructive action, then MFA method changes may occur shortly before backup vault enumeration, backup configuration weakening, or deletion attempts.

Expected artifacts:

- MFA method change on privileged account.
- Backup vault read or backup configuration write.
- Backup vault deletion attempt.
- Shared actor and correlation window.

## 9. Detection Design

DET-001 detects privileged MFA changes followed by backup vault deletion or protection weakening within 2 hours.

Artifacts:

- Sigma: `examples/rules/privileged-mfa-backup-deletion.yml`
- Sentinel KQL: `examples/queries/sentinel-kql-privileged-mfa-backup-deletion.kql`
- Splunk SPL: `examples/queries/splunk-cloud-identity-backup-deletion.spl`
- Detection JSON: `examples/json/detection.example.json`

Detection acceptance requirements:

- Detection **MUST** include owner, data source, ATT&CK mapping, false-positive classes, and replay result.
- Detection **SHOULD** include platform translations for the customer SIEM.
- Detection **MAY** start in monitor-only mode when Gate E approves conditions.

## 10. Replay

Replay command:

```bash
python3 examples/replay/replay-cloud-identity.py
```

Replay result:

```json
{
  "event_count": 8,
  "alert_count": 1,
  "actor": "admin.riley@meridian.example",
  "result": "detected"
}
```

![Replay output](/img/workflow-output/02-replay-output.svg)

## 11. Tuning

Initial pilot produced two false positives from approved administrative change activity.

Tuning rule:

An event may be suppressed only when an approved change ticket includes:

- expected administrator;
- expected resource group;
- approved time window;
- named approver;
- rollback owner.

Suppression **MUST NOT** apply to failed backup deletion attempts from unmanaged IP addresses.

## 12. SOC Handoff

SOC handoff includes:

| Item | Requirement |
|---|---|
| Alert title | Privileged MFA Change Followed by Backup Deletion Attempt |
| Severity | High |
| Initial triage | Verify user, source IP, change ticket, and backup operation |
| Escalation | Cloud security lead and incident commander |
| Containment | Disable session, revoke refresh tokens, block deletion path if confirmed |
| Evidence | Preserve Entra ID Audit and Azure Activity events |

## 13. Pilot

Pilot health summary:

| Date | Alerts | True positives | False positives | Notes |
|---|---:|---:|---:|---|
| 2026-05-06 | 3 | 1 | 2 | Change-window tuning required |
| 2026-05-07 | 1 | 1 | 0 | Replay positive detected |
| 2026-05-08 | 0 | 0 | 0 | No alerts |

Final pilot state: DRL-8.

## 14. Metrics

| Metric | Result |
|---|---|
| Replay events | 8 |
| Replay alerts | 1 |
| Replay false negatives | 0 |
| Pilot alerts | 4 |
| Pilot true positives | 2 |
| Pilot false positives | 2 |
| Final DRL | 8 |

## 15. Gate Decisions

![Gate status](/img/workflow-output/03-gate-status.svg)

| Gate | Result |
|---|---|
| Gate A | Pass |
| Gate B | Pass |
| Gate C | Pass |
| Gate D | Pass with tuning conditions |
| Gate E | Conditional pass |
| Gate F | Pass |

## 16. Executive Summary

Recommendation: move DET-001 to production in monitor-only mode for 7 days, then promote to standard SOC escalation if false-positive controls remain stable.

![Executive summary](/img/workflow-output/04-executive-summary.svg)

Executive report file: `examples/reports/executive-report.md`

## 17. Final Delivery Package

The final package includes:

- PIR/SIR register
- Evidence register
- Detection backlog and health register
- Sigma rule and SIEM queries
- Replay dataset and replay result
- Gate A-F evidence packs
- Executive report

Residual risk: the detection depends on Entra ID Audit and Azure Activity log completeness. If either source is delayed or disabled, DRL must be demoted and Gate E must be reopened.
