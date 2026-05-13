---
id: complete-worked-case
title: Complete Worked Case
sidebar_label: Complete Worked Case
slug: /practitioner-package/complete-worked-case
description: Full synthetic PIR-to-detection-to-pilot-to-executive-report case.
---

# Complete Worked Case: PIR to Detection to Pilot to Executive Report

## 1. Customer Decision

Meridian Freight Group's CISO needs to decide whether cloud identity activity against privileged administrators justifies a 30-day detection engineering sprint.

## 2. PIR

**PIR-001:** Are privileged cloud identities being used in a way that could enable backup deletion before ransomware deployment?

Decision owner: CISO  
Time horizon: 30 days  
Confidence threshold: Moderate

## 3. SIRs

| SIR | Question | Data source | Closure |
|---|---|---|---|
| SIR-001 | Which privileged identities changed MFA settings before backup-resource activity? | Entra ID Audit Log | Closed |
| SIR-002 | Did any privileged session enumerate or modify backup vaults? | Azure Activity Log | Closed |
| SIR-003 | Can Sentinel detect the sequence with acceptable false-positive risk? | Microsoft Sentinel | Closed |

## 4. Evidence

The evidence register contains four accepted evidence items:

- EV-001: Privileged user registered a new MFA method.
- EV-002: Backup vault deletion was attempted.
- EV-003: Detection fired during replay.
- EV-004: Gate E approval granted with pilot conditions.

## 5. Threat Scenario

An adversary obtains a privileged cloud administrator session, performs a suspicious MFA method change, enumerates backup resources, weakens protection, and attempts backup vault deletion.

ATT&CK mapping: T1098 Account Manipulation  
Primary data sources: Entra ID Audit Log and Azure Activity

## 6. Hunt Hypothesis

If a privileged cloud account is being prepared for destructive action, then MFA method changes may occur shortly before backup vault enumeration, backup configuration weakening, or deletion attempts.

## 7. Detection Design

DET-001 detects privileged MFA changes followed by backup vault deletion or protection weakening within 2 hours.

Artifacts:

- Sigma: `examples/rules/privileged-mfa-backup-deletion.yml`
- Sentinel KQL: `examples/queries/sentinel-kql-privileged-mfa-backup-deletion.kql`
- Splunk SPL: `examples/queries/splunk-cloud-identity-backup-deletion.spl`

## 8. Replay

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

## 9. Pilot

Pilot health summary:

| Date | Alerts | True positives | False positives | Notes |
|---|---:|---:|---:|---|
| 2026-05-06 | 3 | 1 | 2 | Change-window tuning required |
| 2026-05-07 | 1 | 1 | 0 | Replay positive detected |
| 2026-05-08 | 0 | 0 | 0 | No alerts |

Final pilot state: DRL-8.

## 10. Gate Decisions

![Gate status](/img/workflow-output/03-gate-status.svg)

| Gate | Result |
|---|---|
| Gate A | Pass |
| Gate B | Pass |
| Gate C | Pass |
| Gate D | Pass with tuning conditions |
| Gate E | Conditional pass |
| Gate F | Pass |

## 11. Executive Report

Recommendation: move DET-001 to production in monitor-only mode for 7 days, then promote to standard SOC escalation if false-positive controls remain stable.

![Executive summary](/img/workflow-output/04-executive-summary.svg)

## 12. Final Delivery Package

The final package includes:

- PIR/SIR register
- Evidence register
- Detection backlog and health register
- Sigma rule and SIEM queries
- Replay dataset and replay result
- Gate A-F evidence packs
- Executive report

Residual risk: the detection depends on Entra ID Audit and Azure Activity log completeness. If either source is delayed or disabled, DRL must be demoted and Gate E must be reopened.
