# Gate A: PIR Approval Evidence Pack

## Gate Result

Pass with no critical blockers.

## Scope

- Customer: Meridian Freight Group
- PIR: PIR-001
- Scenario: Cloud identity compromise leading to backup deletion

## Required Evidence

| Requirement | Evidence | Status |
|---|---|---|
| PIR names a customer decision | `pir-register.csv` PIR-001 | Pass |
| PIR has decision owner | CISO listed as owner | Pass |
| SIRs are answerable and bounded | `sir-register.csv` SIR-001 to SIR-003 | Pass |
| Data sources are named | Entra ID Audit, Azure Activity, Sentinel | Pass |
| Confidence threshold is defined | Moderate | Pass |

## Approval

- Approver: CISO Delegate
- Date: 2026-05-02
- Decision: Proceed to scenario and detection design.
