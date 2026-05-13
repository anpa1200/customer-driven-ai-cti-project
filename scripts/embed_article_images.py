#!/usr/bin/env python3
"""Embed imported Medium images into the corresponding documentation pages."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "content" / "medium" / "image-manifest.json"

DOCS = {
    "workflow": ROOT / "docs" / "workflow" / "full-workflow-quick-reference.md",
    "part-1-foundations": ROOT / "docs" / "methodology" / "foundations.md",
    "part-2a-execution-guide": ROOT / "docs" / "methodology" / "phase-by-phase-execution-guide.md",
    "part-2b-reference-toolkit": ROOT / "docs" / "methodology" / "reference-toolkit.md",
}


WORKFLOW_TARGETS = [
    "Phase 0: Project Charter and Guardrails",
    "Phase 1: Customer Decision and PIR Definition",
    "Phase 2: Crown-Jewel and Business-Impact Mapping",
    "Phase 3: Telemetry and Data Readiness Assessment",
    "Phase 4: External CTI Source Intake and Validation",
    "Phase 5: Threat Scenario Development",
    "Phase 6: Hypothesis-Driven Threat Hunting Backlog",
    "Phase 7: Detection Engineering Design",
    "Phase 8: Detection-as-Code Implementation",
    "Phase 9: Test Data, Simulation, and Replay",
    "Phase 10: SOC Triage and Incident Workflow",
    "Phase 11: Pilot Deployment and Tuning",
    "Phase 12: Production Deployment",
    "Phase 13: Executive and Technical Reporting",
    "Phase 14: Continuous Improvement and Maturity Loop",
    "Quality Gates",
]

PART_1_TARGETS = [
    "Claim-to-Action Chain",
    "Chain Validation",
    "Confidence Language",
    "Minimum Confidence Criteria",
    "Source Reliability",
    "Rating AI-Generated Intelligence",
    "Example Score Table",
    "Readiness-Based Mode Selection",
    "Mode 1: Lightweight Assessment",
    "AI OPSEC Classification",
    "AI Operating Controls",
    "Prompt-Injection Handling",
    "Pre-Screening Data Classification Tiers",
    "Approved AI Tool Register",
    "Public AI SaaS Acceptability Decision Table",
    "Project Roles",
    "RACI Matrix",
    "Delivery Artifacts",
    "CTI Information Sharing Standards",
    "Intelligence Requirements",
    "Definitions",
    "Customer Attack Surface and Trust Boundary Map",
    "D3FEND Countermeasure Mapping",
    "Detection Readiness Levels",
    "DRL Transition Evidence Requirements",
    "Detection CI/CD Requirements",
    "Effort Sizing",
    "Complexity Decision Matrix",
]

PART_2A_TARGETS = [
    "Phase 0: Project Charter and Guardrails",
    "Activities",
    "Success Metric Floors",
    "Validation Tests",
    "Repository Setup",
    "Validation Tests",
    "Validation Tests",
    "Validation Tests",
    "Validation Tests",
    "IOC Emergency Unblock Procedure",
    "Validation Tests",
    "Validation Tests",
    "AI Usage",
    "Validation Tests",
    "Validation Tests",
    "Validation Tests",
    "Validation Tests",
    "Phase 11: Pilot Deployment and Tuning",
    "Validation Tests",
    "Validation Tests",
    "Validation Tests",
    "Metrics",
    "Validation Tests",
    "References",
]


def load_manifest() -> dict[tuple[str, int], dict[str, str]]:
    entries = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {(entry["article_slug"], int(entry["index"])): entry for entry in entries}


def image_block(images: dict[tuple[str, int], dict[str, str]], slug: str, index: int) -> str:
    entry = images[(slug, index)]
    alt = f"{entry['article_title']} infographic {entry['index']}"
    return f"\n![{alt}]({entry['site_path']})\n"


def insert_after_heading(text: str, heading_prefix: str, block: str) -> str:
    pos = text.find(heading_prefix)
    if pos < 0:
        raise RuntimeError(f"heading prefix not found: {heading_prefix}")
    line_end = text.find("\n", pos)
    insert_pos = line_end + 1
    if block.strip() in text[insert_pos : insert_pos + 500]:
        return text
    return text[:insert_pos] + block + text[insert_pos:]


def insert_before_heading(text: str, heading: str, block: str, start: int) -> tuple[str, int]:
    candidates = [f"## {heading}", f"### {heading}"]
    positions = [(text.find(candidate, start), candidate) for candidate in candidates]
    positions = [(pos, candidate) for pos, candidate in positions if pos >= 0]
    if not positions:
        raise RuntimeError(f"heading not found after {start}: {heading}")
    pos, candidate = min(positions, key=lambda item: item[0])
    if block.strip() in text[max(0, pos - 500) : pos + 500]:
        return text, pos + len(candidate)
    text = text[:pos] + block + "\n" + text[pos:]
    return text, pos + len(block) + len(candidate)


def embed_sequence(slug: str, first_heading: str, targets: list[str]) -> None:
    images = load_manifest()
    path = DOCS[slug]
    text = path.read_text(encoding="utf-8")
    text = insert_after_heading(text, first_heading, image_block(images, slug, 1))
    cursor = 0
    for index, target in enumerate(targets, start=2):
        text, cursor = insert_before_heading(text, target, image_block(images, slug, index), cursor)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    embed_sequence(
        "workflow",
        "# Customer-Driven AI CTI Project: Full Workflow Quick Reference",
        WORKFLOW_TARGETS,
    )
    embed_sequence(
        "part-1-foundations",
        "## From pure CTI to hands-on detection engineering with strict validation gates",
        PART_1_TARGETS,
    )
    embed_sequence(
        "part-2a-execution-guide",
        "## From pure CTI to hands-on detection engineering with strict validation gates",
        PART_2A_TARGETS,
    )

    images = load_manifest()
    path = DOCS["part-2b-reference-toolkit"]
    text = path.read_text(encoding="utf-8")
    text = insert_after_heading(
        text,
        "## From pure CTI to hands-on detection engineering with strict validation gates",
        image_block(images, "part-2b-reference-toolkit", 1),
    )
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
