# Customer-Driven AI CTI Project

Docusaurus-ready documentation site for the Customer-Driven AI CTI Project article series and methodology.

Published project entry point:

https://medium.com/@1200km/customer-driven-ai-cti-project-c0db3cdc1830

## Repository Structure

```text
.
├── .github/workflows/deploy.yml
├── content/medium/
│   ├── image-manifest.json
│   ├── customer-driven-ai-cti-project-workflow.md
│   ├── customer-driven-ai-cti-project-template-part1.md
│   ├── customer-driven-ai-cti-project-template-part2a.md
│   ├── customer-driven-ai-cti-project-template-part2b.md
│   └── customer-driven-ai-cti-project-template-complete.md
├── docs/
│   ├── intro.md
│   ├── infographics.md
│   ├── published-articles.md
│   ├── methodology/
│   │   ├── foundations.md
│   │   ├── phase-by-phase-execution-guide.md
│   │   ├── reference-toolkit.md
│   │   └── complete-template.md
│   └── workflow/
│       └── full-workflow-quick-reference.md
├── src/
├── scripts/
│   └── import_medium_images.py
├── static/
│   └── img/articles/
├── docusaurus.config.ts
├── package.json
└── sidebars.ts
```

## Published Articles

- [Customer-Driven AI CTI Project: Full Workflow Quick Reference](https://medium.com/@1200km/customer-driven-ai-cti-project-c0db3cdc1830)
- [Part 1: Foundations](https://medium.com/@1200km/customer-driven-ai-cti-project-template-part-1-foundations-745861507d03)
- [Part 2A: Phase-by-Phase Execution Guide](https://medium.com/@1200km/customer-driven-ai-cti-project-template-part-2a-phase-by-phase-execution-guide-f9751a8bcb59)
- [Part 2B: Reference Toolkit](https://medium.com/@1200km/customer-driven-ai-cti-project-template-part-2b-reference-toolkit-3a56fab0b943)

## Local Development

```bash
npm install
npm start
```

## Validation

```bash
npm run typecheck
npm run build
```

## Import Medium Images

```bash
python3 scripts/import_medium_images.py
```

The importer reads the public Medium RSS feed, downloads article images into `static/img/articles/`, writes `content/medium/image-manifest.json`, and regenerates `docs/infographics.md`.

## GitHub Pages

The site is configured for GitHub Pages at:

https://anpa1200.github.io/customer-driven-ai-cti-project/

Deployment runs through GitHub Actions from `main`.
