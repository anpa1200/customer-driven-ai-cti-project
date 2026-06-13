---
id: gate-evidence-packs
title: Gate Evidence Packs
sidebar_label: Gate Evidence Packs
slug: /practitioner-package/gate-evidence-packs
description: "Gate evidence packs for the customer-driven CTI project: analyst-validated evidence and confidence ratings at each methodology phase gate."
---

# Gate Evidence Packs

The sample package includes Gate A-F evidence packs under `examples/gates/`.

| Gate | File | Result |
|---|---|---|
| Gate A: PIR Approval | `gate-a-pir-approval.md` | Pass |
| Gate B: Scenario Approval | `gate-b-scenario-approval.md` | Pass |
| Gate C: Hunt Approval | `gate-c-hunt-approval.md` | Pass |
| Gate D: Detection Design Approval | `gate-d-detection-design-approval.md` | Pass with tuning conditions |
| Gate E: Production Approval | `gate-e-production-approval.md` | Conditional pass |
| Gate F: Final Delivery Approval | `gate-f-final-delivery-approval.md` | Pass |

Gate E remains conditional because production starts in monitor-only mode before standard SOC escalation.
