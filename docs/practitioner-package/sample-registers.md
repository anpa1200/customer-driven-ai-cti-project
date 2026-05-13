---
id: sample-registers
title: Sample Registers
sidebar_label: Sample Registers
slug: /practitioner-package/sample-registers
---

# Sample Registers

The sample registers are provided as CSV files under `examples/registers/`.

## Register Set

- `pir-register.csv`
- `sir-register.csv`
- `evidence-register.csv`
- `detection-backlog.csv`
- `detection-health-register.csv`
- `registers.md`

## PIR Example

```csv
pir_id,decision_owner,decision,question,time_horizon,status,confidence_threshold
PIR-001,CISO,Prioritize a cloud identity detection sprint,Are privileged cloud identities being used in a way that could enable backup deletion before ransomware deployment?,30 days,Approved,Moderate
```

## Register Purpose

The registers show the chain from a customer decision to evidence, SIR closure, detection ownership, pilot health, and final acceptance.
