# SEO and AI-searchability fixes

Status at preparation time (2026-08-14): validated locally and awaiting publication. Search-engine submission remains a post-deployment human action.

## Issue 4 — Docusaurus metadata

- `docusaurus.config.ts` centralizes the browser-title suffix on `1200km`, declares the exact portfolio `og:site_name`, uses the existing full-workflow project cover instead of the AP logo, and enables the metadata build plugin.
- `src/pages/index.tsx` separates the visible project name from the site-title suffix and supplies the root value-statement description.
- `seo/descriptions.json` is the source of truth for 27 unique indexable-route descriptions, each 140–160 characters.
- `src/theme/DocItem/Metadata/index.js` applies those authored values and Twitter parity during server rendering, hydration, and client-side navigation.
- `seo-metadata-plugin.cjs` enforces title, description, canonical, social-parity, image, uniqueness, and branded-404 rules during every production build.

## Issue 7 — HexStrike destinations

- `docusaurus.config.ts` labels both third-party navigation destinations as `HexStrike AI (upstream project)`.
- `docs/ecosystem.md` labels both `github.com/0x4m4/hexstrike-ai` destinations as `HexStrike AI (upstream project)`.
- No `github.com/anpa1200/Hexstrike-AI` destination exists in this sub-site, so no owner/fork label was required here.

## Issue 8 — accurate sitemap dates

- `docusaurus.config.ts` enables Git-derived document update times and date-valued sitemap entries, including the custom root route.
- `.github/workflows/deploy.yml` checks out full Git history so generated dates do not collapse to the deployment commit.
- `.github/workflows/validate.yml` also checks out full Git history because its validation job runs the production build and verifies the same Git-derived dates.

## Issue 9 — structured data

- `src/pages/index.tsx` emits an absolute-URL root `BreadcrumbList`.
- `seo-metadata-plugin.cjs` preserves framework breadcrumbs, adds a valid fallback when needed, and exposes document update times as `article:modified_time`.
- `src/theme/DocItem/Metadata/index.js` exposes the same modified time and social metadata in the hydrated application head.

## Exact touched-file manifest

- `.github/workflows/deploy.yml`
- `.github/workflows/validate.yml`
- `SEO-FIXES.md`
- `docs/ecosystem.md`
- `docusaurus.config.ts`
- `seo-metadata-plugin.cjs`
- `seo/descriptions.json`
- `src/pages/index.tsx`
- `src/theme/DocItem/Metadata/index.js`

## Validation

- `npm run build` passed in a full-history worktree.
- Audited 27 indexable routes: 27 exact branded titles, 27 unique compliant descriptions, 27 canonical URLs, 27 Open Graph/Twitter parity matches, 27 project-cover matches, and 27 valid `BreadcrumbList` blocks.
- All 26 document routes expose `article:modified_time`; the custom root uses its Git date in the sitemap.
- `build/sitemap.xml` contains 27 URLs and 27 `<lastmod>` values.

## Deploy and human follow-ups

1. Publish this source repository and verify the deployment workflow completes successfully.
2. Rebuild the 1200km.com aggregate sitemap after the sub-site is live.
3. Resubmit the aggregate sitemap in Google Search Console and Bing Webmaster Tools, then inspect the project root and representative documentation URLs.
