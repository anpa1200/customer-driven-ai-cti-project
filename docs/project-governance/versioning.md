---
id: versioning
title: Versioning
sidebar_label: Versioning
slug: /project-governance/versioning
---

# Versioning

Current release: **v1.0.0**

This project uses semantic versioning for public methodology and artifact changes.

## Version Rules

- MAJOR versions indicate incompatible methodology or artifact contract changes.
- MINOR versions add backward-compatible modules, schemas, examples, or workflow phases.
- PATCH versions fix wording, links, validation behavior, or examples without changing requirements.

## Release Artifacts

Each release SHOULD include:

- `VERSION`
- `CHANGELOG.md`
- `ROADMAP.md`
- `DEPRECATED.md`
- passing validation and build checks

## Compatibility

Published examples SHOULD remain reproducible for the release line in which they were introduced.
