#!/usr/bin/env python3
"""Import Medium article images into the Docusaurus static asset tree."""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.error import URLError


ROOT = Path(__file__).resolve().parents[1]
FEED_URL = "https://medium.com/feed/@1200km"
USER_AGENT = "Mozilla/5.0 (compatible; customer-driven-ai-cti-project-image-importer/1.0)"


@dataclass(frozen=True)
class Article:
    slug: str
    title: str
    medium_id: str
    url: str


ARTICLES = [
    Article(
        slug="workflow",
        title="Customer-Driven AI CTI Project: Full Workflow Quick Reference",
        medium_id="customer-driven-ai-cti-project-c0db3cdc1830",
        url="https://medium.com/@1200km/customer-driven-ai-cti-project-c0db3cdc1830",
    ),
    Article(
        slug="part-1-foundations",
        title="Part 1: Foundations",
        medium_id="customer-driven-ai-cti-project-template-part-1-foundations-745861507d03",
        url="https://medium.com/@1200km/customer-driven-ai-cti-project-template-part-1-foundations-745861507d03",
    ),
    Article(
        slug="part-2a-execution-guide",
        title="Part 2A: Phase-by-Phase Execution Guide",
        medium_id="customer-driven-ai-cti-project-template-part-2a-phase-by-phase-execution-guide-f9751a8bcb59",
        url="https://medium.com/@1200km/customer-driven-ai-cti-project-template-part-2a-phase-by-phase-execution-guide-f9751a8bcb59",
    ),
    Article(
        slug="part-2b-reference-toolkit",
        title="Part 2B: Reference Toolkit",
        medium_id="customer-driven-ai-cti-project-template-part-2b-reference-toolkit-3a56fab0b943",
        url="https://medium.com/@1200km/customer-driven-ai-cti-project-template-part-2b-reference-toolkit-3a56fab0b943",
    ),
]


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def extension_for(url: str) -> str:
    path = url.split("?", 1)[0].lower()
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        if path.endswith(ext):
            return ".jpg" if ext == ".jpeg" else ext
    return ".png"


def extract_images(feed_xml: bytes) -> dict[str, list[str]]:
    root = ET.fromstring(feed_xml)
    by_article: dict[str, list[str]] = {article.slug: [] for article in ARTICLES}
    article_by_id = {article.medium_id: article for article in ARTICLES}

    for item in root.findall("./channel/item"):
        link = item.findtext("link") or ""
        article = next((a for marker, a in article_by_id.items() if marker in link), None)
        if not article:
            continue

        encoded = item.find("{http://purl.org/rss/1.0/modules/content/}encoded")
        content = encoded.text if encoded is not None and encoded.text else ""
        urls = re.findall(r'<img[^>]+src="([^"]+)"', content)
        urls = [html.unescape(url) for url in urls if "medium.com/_/stat" not in url]
        by_article[article.slug] = urls

    return by_article


def write_gallery(manifest: list[dict[str, str]]) -> None:
    gallery = ROOT / "docs" / "infographics.md"
    sections: list[str] = [
        "---",
        "id: infographics",
        "title: Infographics",
        "sidebar_label: Infographics",
        "slug: /infographics",
        "description: Imported infographic images from the published Medium article series.",
        "---",
        "",
        "# Infographics",
        "",
        "Imported image assets from the published Medium article series.",
        "",
    ]

    for article in ARTICLES:
        entries = [item for item in manifest if item["article_slug"] == article.slug]
        sections.extend([f"## {article.title}", "", f"Source: [{article.url}]({article.url})", ""])
        for item in entries:
            sections.extend(
                [
                    f"### Image {item['index']}",
                    "",
                    f"![{article.title} image {item['index']}]({item['site_path']})",
                    "",
                ]
            )

    gallery.write_text("\n".join(sections), encoding="utf-8")


def main() -> int:
    try:
        feed = fetch(FEED_URL)
    except URLError as exc:
        print(f"Failed to fetch Medium RSS feed: {exc}", file=sys.stderr)
        return 1

    by_article = extract_images(feed)
    manifest: list[dict[str, str]] = []
    asset_root = ROOT / "static" / "img" / "articles"
    asset_root.mkdir(parents=True, exist_ok=True)

    for article in ARTICLES:
        article_dir = asset_root / article.slug
        article_dir.mkdir(parents=True, exist_ok=True)
        for index, url in enumerate(by_article.get(article.slug, []), start=1):
            digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:10]
            filename = f"{index:02d}-{digest}{extension_for(url)}"
            output_path = article_dir / filename
            if not output_path.exists():
                output_path.write_bytes(fetch(url))

            site_path = f"/img/articles/{article.slug}/{filename}"
            manifest.append(
                {
                    "article_slug": article.slug,
                    "article_title": article.title,
                    "article_url": article.url,
                    "index": f"{index:02d}",
                    "source_url": url,
                    "file": str(output_path.relative_to(ROOT)),
                    "site_path": site_path,
                }
            )

    manifest_path = ROOT / "content" / "medium" / "image-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    write_gallery(manifest)

    print(f"Imported {len(manifest)} images.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
