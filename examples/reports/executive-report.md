# Executive Report: Cloud Identity to Backup Deletion

## Executive Summary

Meridian Freight Group should prioritize a cloud identity detection engineering sprint because a privileged account sequence can connect identity control changes to backup vault destruction attempts within a short operational window.

The synthetic worked case demonstrates that the team can move from a CISO decision to PIR/SIRs, evidence, detection logic, replay validation, pilot monitoring, and final delivery.

## Business Impact

- Backup deletion could prevent recovery of route optimization databases.
- Recovery failure could disrupt cold-chain delivery commitments.
- Operational disruption could trigger SLA penalties and customer trust impact.

## Detection Outcome

DET-001 detects a privileged MFA method change followed by backup vault deletion or protection weakening within 2 hours.

## Metrics

| Metric | Result |
|---|---|
| Replay true positives | 1 |
| Replay false negatives | 0 |
| Pilot alerts | 4 |
| Pilot true positives | 2 |
| Pilot false positives | 2 |
| Final DRL | 8 |

## Recommendation

Move DET-001 to production in monitor-only mode for 7 days, then promote to standard SOC escalation if false-positive controls remain stable.

## Residual Risk

The detection depends on Entra ID Audit and Azure Activity log completeness. If either source is delayed or disabled, DRL must be demoted and Gate E must be reopened.
