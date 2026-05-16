---
id: normative-language
title: Normative Language
sidebar_label: Normative Language
slug: /standard/normative-language
---

# Normative Language

This project uses requirement keywords to make the methodology standard-like and auditable.

## Keywords

- **MUST** means the requirement is mandatory.
- **MUST NOT** means the behavior is prohibited.
- **REQUIRED** means the artifact, evidence, or control is mandatory.
- **SHOULD** means the requirement is recommended unless a documented exception exists.
- **MAY** means the item is optional.
- **OPTIONAL** means the item is not required for gate approval.

## Core Requirements

- Every PIR **MUST** name a customer decision, owner, and time horizon.
- Every SIR **MUST** define data source, evidence type, owner, due date, and closure condition.
- AI-generated content **MUST NOT** be accepted as evidence without traceable source material.
- Every detection **MUST** name required telemetry, mapped behavior, owner, test plan, and rollback path.
- ATT&CK mappings are behavior-backed: detections **MUST NOT** force a technique when evidence does not support one.
- Every gate decision **MUST** include accepted evidence, blockers, and approval owner.
- Production promotion **MUST** require replay or pilot evidence.

## Exception Handling

Exceptions **MUST** be documented with:

- exception owner;
- affected requirement;
- reason;
- expiry or review date;
- residual risk.

## Cross-Links

- [Artifact Contracts](artifact-contracts.md) — output artifacts that these requirements govern
- [Full Workflow Quick Reference](../workflow/full-workflow-quick-reference.md) — phase-by-phase application of MUST/SHOULD requirements
- [CTI Analyst Field Manual — Evidence Labels](https://anpa1200.github.io/cti-analyst-field-manual/docs/01-cti-foundations/evidence-labels) — canonical labels referenced in SIR and evidence requirements
- [CTI Analyst Field Manual — Detection Readiness Levels](https://anpa1200.github.io/cti-analyst-field-manual/docs/08-cti-to-detection/detection-readiness-levels) — DRL model that production promotion MUST satisfy

## References

- [RFC 2119 — Key words for use in RFCs (IETF)](https://www.rfc-editor.org/rfc/rfc2119) — definition of MUST/SHOULD/MAY used in this standard
