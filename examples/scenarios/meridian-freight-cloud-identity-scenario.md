# Fake Customer Scenario: Meridian Freight Group

## Scenario Status

Synthetic example. No real customer data, infrastructure, logs, users, or indicators are represented.

## Customer Profile

- Customer: Meridian Freight Group
- Sector: Logistics and cold-chain transportation
- Region: Europe and Middle East
- Business model: Time-sensitive delivery for pharmaceutical and defense-adjacent customers
- Security stack: Microsoft Entra ID, Microsoft 365, Azure, Sentinel, Defender for Endpoint, Okta for selected subsidiaries

## Crown Jewels

| Crown jewel | Business owner | Technical owner | Business impact | Primary telemetry |
|---|---|---|---|---|
| Route optimization platform | COO | Cloud Platform Lead | Delivery disruption, SLA penalties | Entra ID, Azure Activity, app logs |
| Backup vault for routing databases | CIO | Infrastructure Lead | Recovery failure, regulatory exposure | Azure Activity, Key Vault, storage logs |
| Customer shipment portal | VP Customer Success | AppSec Lead | Customer trust, contract penalties | WAF, app logs, Entra ID |

## Business Decision

The CISO needs to decide whether identity-focused threat activity against cloud administrators justifies a 30-day detection engineering sprint before the next quarterly board meeting.

## Primary Threat Scenario

An adversary obtains a privileged cloud administrator session, performs suspicious MFA changes, enumerates backup resources, and attempts destructive backup deletion or recovery-lock weakening before ransomware deployment.

## Assumptions

- Entra ID sign-in and audit logs are available in Microsoft Sentinel.
- Azure Activity logs cover backup vault and storage management actions.
- Defender for Endpoint telemetry is available for cloud admin workstations.
- No production containment action is performed from this example without customer approval.

## Evidence Boundary

The sample dataset in `examples/datasets/cloud_identity_events.csv` is fabricated to demonstrate the workflow only. It is designed for replay and validation exercises, not for threat attribution.
