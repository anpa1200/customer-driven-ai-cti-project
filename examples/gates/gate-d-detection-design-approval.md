# Gate D: Detection Design Approval Evidence Pack

## Gate Result

Pass with tuning conditions.

## Detection

DET-001: Privileged MFA Change Followed by Backup Deletion Attempt

## Artifacts

- Sigma rule: `examples/rules/privileged-mfa-backup-deletion.yml`
- Sentinel KQL: `examples/queries/sentinel-kql-privileged-mfa-backup-deletion.kql`
- Splunk SPL: `examples/queries/splunk-cloud-identity-backup-deletion.spl`
- Dataset: `examples/datasets/cloud_identity_events.csv`

## Required Evidence

| Requirement | Evidence | Status |
|---|---|---|
| Telemetry confirmed at DRL >= 2 | Entra ID Audit and Azure Activity | Pass |
| Rule has named data sources | Sigma and KQL artifacts | Pass |
| False-positive classes documented | Change window and decommissioning cases | Pass |
| D3FEND/defensive mapping documented | Account monitoring and cloud resource activity monitoring | Pass |

## Tuning Conditions

Exclude approved change windows only when ticket ID, approver, admin identity, and expected resource are all present.
