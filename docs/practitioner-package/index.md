---
id: package-index
title: Practitioner Package
sidebar_label: Overview
slug: /practitioner-package
description: Synthetic sample artifacts for running the Customer-Driven AI CTI Project workflow.
---

# Practitioner Package

This package adds a complete synthetic project kit for the Customer-Driven AI CTI Project methodology.

All data is fake. Meridian Freight Group, users, IP addresses, events, and outcomes are fabricated examples for training, documentation, and replay validation.

## Included Artifacts

| Artifact | Location |
|---|---|
| Fake customer scenario | `examples/scenarios/meridian-freight-cloud-identity-scenario.md` |
| Sample CSV and Markdown registers | `examples/registers/` |
| Example Sigma rule | `examples/rules/privileged-mfa-backup-deletion.yml` |
| Example SIEM queries | `examples/queries/` |
| Test dataset | `examples/datasets/cloud_identity_events.csv` |
| Replay script and result | `examples/replay/` |
| Gate A-F evidence packs | `examples/gates/` |
| Workflow output screenshots | `static/img/workflow-output/` |
| Executive report | `examples/reports/executive-report.md` |

## Validation

Run:

```bash
python3 scripts/validate_examples.py
python3 examples/replay/replay-cloud-identity.py
npm run typecheck
npm run build
```

## Reading Order

1. [Fake Customer Scenario](/docs/practitioner-package/fake-customer-scenario)
2. [Sample Registers](/docs/practitioner-package/sample-registers)
3. [Detection Artifacts](/docs/practitioner-package/detection-artifacts)
4. [Replay Example](/docs/practitioner-package/replay-example)
5. [Gate Evidence Packs](/docs/practitioner-package/gate-evidence-packs)
6. [Workflow Output Screenshots](/docs/practitioner-package/workflow-output-screenshots)
7. [Complete Worked Case](/docs/practitioner-package/complete-worked-case)
