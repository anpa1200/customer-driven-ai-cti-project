# Gate E: Production Approval Evidence Pack

## Gate Result

Conditional pass.

## Pilot Summary

| Date | Alerts | TP | FP | Notes |
|---|---:|---:|---:|---|
| 2026-05-06 | 3 | 1 | 2 | Change-window tuning required |
| 2026-05-07 | 1 | 1 | 0 | Replay positive detected |
| 2026-05-08 | 0 | 0 | 0 | No alert activity |

## Required Evidence

| Requirement | Evidence | Status |
|---|---|---|
| Replay test completed | `replay-result.json` | Pass |
| Pilot health recorded | `detection-health-register.csv` | Pass |
| Tuning documented | Approved change-window exclusion | Pass |
| Rollback owner named | Detection Engineer | Pass |
| SOC owner named | SOC Lead | Pass |

## Production Conditions

- Deploy in monitor-only mode for first 7 days.
- Review all suppressions weekly for 30 days.
- Escalate any failed deletion attempt from unmanaged IP as high severity.
