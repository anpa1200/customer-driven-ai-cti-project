---
id: artifact-contracts
title: Artifact Contracts
sidebar_label: Artifact Contracts
slug: /standard/artifact-contracts
---

# Artifact Contracts

Artifact contracts define the minimum fields expected for reusable project outputs.

## PIR Register

A PIR register row **MUST** include:

- `pir_id`
- `decision_owner`
- `decision`
- `question`
- `time_horizon`
- `status`
- `confidence_threshold`

## SIR Register

A SIR register row **MUST** include:

- `sir_id`
- `pir_id`
- `question`
- `data_source`
- `evidence_type`
- `owner`
- `due_date`
- `status`

## Detection Backlog

A detection backlog row **MUST** include:

- `detection_id`
- `title`
- `scenario_id`
- `technique`
- `data_source`
- `drl`
- `status`
- `owner`
- `priority`

## Gate Evidence Pack

A gate evidence pack **MUST** include:

- gate result;
- scope;
- required evidence table;
- blockers or explicit statement that no blockers remain;
- approver or owner;
- date or review point.
