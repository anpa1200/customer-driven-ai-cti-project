---
id: schemas-and-validation
title: Schemas and Validation
sidebar_label: Schemas and Validation
slug: /standard/schemas-and-validation
---

# Schemas and Validation

The Practitioner Package includes machine-readable examples and validation checks.

## Schemas

- `examples/schemas/pir-register.schema.json`
- `examples/schemas/sir-register.schema.json`
- `examples/schemas/detection-backlog.schema.json`
- `examples/schemas/telemetry-event.schema.json`

## JSON Examples

- `examples/json/pir-register.example.json`
- `examples/json/detection.example.json`
- `examples/json/telemetry-event.example.json`

## Telemetry Schema

The telemetry schema example maps the synthetic cloud identity event format to ECS-style and OCSF-style field names.

See `examples/telemetry-schema.md`.

## CI Validation

The repository **MUST** pass:

```bash
npm run validate:examples
npm run typecheck
npm run build
```

The GitHub Actions validation workflow runs these checks on push and pull request.
