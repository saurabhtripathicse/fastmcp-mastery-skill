#!/usr/bin/env python3
"""Generate a feature coverage report for FastMCP docs navigation pages.

This report validates:
- v3 docs pages in fastmcp-main/docs/docs.json are present in fastmcpdocs
- those pages are indexed in references/10-guides-full-index-generated.md
- key client feature pages are explicitly present and indexed
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")


def collect_pages(node: object, pages: list[str]) -> None:
    if isinstance(node, str):
        pages.append(node)
        return
    if isinstance(node, list):
        for item in node:
            collect_pages(item, pages)
        return
    if isinstance(node, dict):
        for key in ("pages", "groups", "dropdowns"):
            if key in node:
                collect_pages(node[key], pages)


def parse_indexed_pages(index_markdown: str) -> set[str]:
    indexed: set[str] = set()
    for line in index_markdown.splitlines():
        line = line.strip()
        if not line.startswith("| `") or ".md`" not in line:
            continue
        parts = line.split("`")
        if len(parts) < 2:
            continue
        path = parts[1]
        if not path.endswith(".md"):
            continue
        page_id = path[:-3]
        if page_id.startswith("root/"):
            page_id = page_id.split("/", 1)[1]
        indexed.add(page_id)
    return indexed


def main() -> None:
    workspace = Path("/Users/saurabhtripathi/project-zero")
    docs_json = workspace / "fastmcp-main/docs/docs.json"
    docs_root = workspace / "fastmcpdocs"
    guides_index = (
        workspace
        / "skills/fastmcp-mastery/references/10-guides-full-index-generated.md"
    )
    output = (
        workspace
        / "skills/fastmcp-mastery/references/16-feature-coverage-report-generated.md"
    )

    nav = json.loads(docs_json.read_text())
    v3 = nav["navigation"]["versions"][0]

    raw_pages: list[str] = []
    collect_pages(v3, raw_pages)

    # Preserve order while deduplicating
    seen: set[str] = set()
    ordered_pages: list[str] = []
    for p in raw_pages:
        if p not in seen:
            seen.add(p)
            ordered_pages.append(p)

    target_pages = [
        p
        for p in ordered_pages
        if not p.startswith("v2/")
        and not p.endswith((".png", ".jpg", ".jpeg", ".svg", ".webp"))
    ]

    missing_in_docs: list[str] = []
    for page in target_pages:
        direct = docs_root / f"{page}.md"
        root_alt = docs_root / "root" / f"{Path(page).name}.md"
        if not direct.exists() and not root_alt.exists():
            missing_in_docs.append(page)

    indexed = parse_indexed_pages(guides_index.read_text(errors="ignore"))
    missing_in_index = [
        page
        for page in target_pages
        if page not in indexed and f"root/{page}" not in indexed
    ]

    client_features = [
        "clients/client",
        "clients/transports",
        "clients/cli",
        "clients/generate-cli",
        "clients/tools",
        "clients/resources",
        "clients/prompts",
        "clients/notifications",
        "clients/sampling",
        "clients/elicitation",
        "clients/tasks",
        "clients/progress",
        "clients/logging",
        "clients/roots",
        "clients/auth/oauth",
        "clients/auth/cimd",
        "clients/auth/bearer",
    ]

    feature_rows: list[tuple[str, bool, bool]] = []
    for page in client_features:
        exists = (docs_root / f"{page}.md").exists()
        in_index = page in indexed
        feature_rows.append((page, exists, in_index))

    lines: list[str] = []
    lines.append("# Feature Coverage Report (Generated)")
    lines.append("")
    lines.append(f"Generated at: `{now_utc()}`")
    lines.append("")
    lines.append("## Inputs")
    lines.append("")
    lines.append(f"- docs nav source: `{docs_json}`")
    lines.append(f"- docs mirror: `{docs_root}`")
    lines.append(f"- guides index: `{guides_index}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(
        f"- v3 navigation pages checked (non-v2, non-image): **{len(target_pages)}**"
    )
    lines.append(f"- missing in `fastmcpdocs`: **{len(missing_in_docs)}**")
    lines.append(
        f"- missing in `10-guides-full-index-generated.md`: **{len(missing_in_index)}**"
    )
    lines.append("")
    lines.append("## Client Feature Checklist")
    lines.append("")
    lines.append("| Page | In `fastmcpdocs` | In guides index |")
    lines.append("|---|---:|---:|")
    for page, exists, in_index in feature_rows:
        lines.append(f"| `{page}` | {int(exists)} | {int(in_index)} |")
    lines.append("")

    if missing_in_docs:
        lines.append("## Missing In `fastmcpdocs`")
        lines.append("")
        for page in missing_in_docs:
            lines.append(f"- `{page}`")
        lines.append("")

    if missing_in_index:
        lines.append("## Missing In Guides Index")
        lines.append("")
        for page in missing_in_index:
            lines.append(f"- `{page}`")
        lines.append("")

    lines.append("## Verdict")
    lines.append("")
    if not missing_in_docs and not missing_in_index and all(
        exists and in_index for _, exists, in_index in feature_rows
    ):
        lines.append(
            "Coverage is complete for website navigation pages and key client features."
        )
    else:
        lines.append(
            "Coverage is incomplete. Resolve missing entries listed above and regenerate."
        )

    output.write_text("\n".join(lines) + "\n")
    print(f"Wrote: {output}")


if __name__ == "__main__":
    main()

