#!/usr/bin/env python3
"""Generate a local FastMCP docs-to-code crosswalk markdown file.

Inputs are explicit:
- docs root: exported FastMCP docs directory
- source repo: FastMCP source repository root
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def count_files_by_top_level(root: Path) -> list[tuple[str, int]]:
    counts: list[tuple[str, int]] = []
    for child in sorted(root.iterdir()):
        if child.is_dir():
            counts.append((child.name, sum(1 for _ in child.rglob("*") if _.is_file())))
    return counts


def map_non_sdk_doc_to_mdx(doc_rel: Path, docs_root: Path) -> Path | None:
    mapped = docs_root / doc_rel.with_suffix(".mdx")
    if mapped.exists():
        return mapped

    # root/*.md in the docs export correspond to docs/*.mdx
    if doc_rel.parts and doc_rel.parts[0] == "root":
        root_level = docs_root / (doc_rel.stem + ".mdx")
        if root_level.exists():
            return root_level

    return None


def map_python_sdk_doc_to_src(doc_file: Path, src_root: Path) -> Path | None:
    stem = doc_file.stem
    if not stem.startswith("fastmcp-"):
        return None

    tail = stem[len("fastmcp-") :]
    parts = tail.split("-")

    candidates: list[Path] = []
    if parts:
        candidates.append(src_root / "fastmcp" / ("/".join(parts) + ".py"))
        if len(parts) > 1:
            candidates.append(src_root / "fastmcp" / "/".join(parts[:-1]) / f"{parts[-1]}.py")
        candidates.append(src_root / "fastmcp" / "/".join(parts) / "__init__.py")
        if parts[-1] == "__init__" and len(parts) > 1:
            candidates.append(src_root / "fastmcp" / "/".join(parts[:-1]) / "__init__.py")

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None


def build_markdown(
    docs_root: Path,
    source_repo: Path,
    output_file: Path,
) -> str:
    source_docs_root = source_repo / "docs"
    source_src_root = source_repo / "src"
    source_examples_root = source_repo / "examples"
    source_tests_root = source_repo / "tests"

    non_sdk_docs = sorted(
        p
        for p in docs_root.rglob("*.md")
        if "python-sdk" not in p.parts
    )
    python_sdk_docs = sorted((docs_root / "python-sdk").glob("*.md"))

    non_sdk_rows: list[tuple[str, str | None]] = []
    for page in non_sdk_docs:
        rel = page.relative_to(docs_root)
        mapped = map_non_sdk_doc_to_mdx(rel, source_docs_root)
        non_sdk_rows.append((str(rel), str(mapped.relative_to(source_repo)) if mapped else None))

    sdk_rows: list[tuple[str, str | None]] = []
    sdk_groups = Counter()
    for page in python_sdk_docs:
        rel = page.relative_to(docs_root)
        mapped = map_python_sdk_doc_to_src(page, source_src_root)
        sdk_rows.append((str(rel), str(mapped.relative_to(source_repo)) if mapped else None))

        parts = page.stem.split("-")
        group = parts[1] if len(parts) > 1 and parts[0] == "fastmcp" else parts[0]
        sdk_groups[group] += 1

    unresolved_non_sdk = [row for row in non_sdk_rows if row[1] is None]
    unresolved_sdk = [row for row in sdk_rows if row[1] is None]

    docs_counts = count_files_by_top_level(docs_root)

    example_counts = []
    root_example_files = sum(1 for p in source_examples_root.iterdir() if p.is_file())
    example_counts.append(("_root_files", root_example_files))
    for child in sorted(source_examples_root.iterdir()):
        if child.is_dir():
            example_counts.append((child.name, sum(1 for _ in child.rglob("*") if _.is_file())))

    test_counts = Counter()
    for path in source_tests_root.rglob("*.py"):
        rel = path.relative_to(source_tests_root)
        test_counts[rel.parts[0]] += 1

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    lines: list[str] = []
    lines.append("# Generated FastMCP Crosswalk")
    lines.append("")
    lines.append(f"Generated at: `{now}`")
    lines.append("")
    lines.append("## Inputs")
    lines.append("")
    lines.append("- docs root: provided via `--docs-root`")
    lines.append("- source repo: provided via `--source-repo`")
    lines.append("")
    lines.append("## High-Level Totals")
    lines.append("")
    lines.append(f"- markdown files in docs root: **{len(list(docs_root.rglob('*.md')))}**")
    lines.append(f"- non-`python-sdk` docs pages: **{len(non_sdk_docs)}**")
    lines.append(f"- `python-sdk` API pages: **{len(python_sdk_docs)}**")
    lines.append(f"- unresolved non-`python-sdk` mappings: **{len(unresolved_non_sdk)}**")
    lines.append(f"- unresolved `python-sdk` mappings: **{len(unresolved_sdk)}**")
    lines.append("")
    lines.append("## Docs Root Folder File Counts")
    lines.append("")
    lines.append("| Folder | Files |")
    lines.append("|---|---:|")
    for name, count in docs_counts:
        lines.append(f"| `{name}` | {count} |")
    lines.append("")
    lines.append("## `python-sdk` Group Counts")
    lines.append("")
    lines.append("| Group | Files |")
    lines.append("|---|---:|")
    for group, count in sorted(sdk_groups.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{group}` | {count} |")
    lines.append("")
    lines.append("## Examples Folder Coverage")
    lines.append("")
    lines.append("| Folder | Files |")
    lines.append("|---|---:|")
    for name, count in example_counts:
        lines.append(f"| `{name}` | {count} |")
    lines.append("")
    lines.append("## Tests Folder Coverage")
    lines.append("")
    lines.append("| Top-Level | Files |")
    lines.append("|---|---:|")
    for name, count in sorted(test_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{name}` | {count} |")
    lines.append("")
    lines.append("## Non-`python-sdk` Doc to Source-Docs Mapping")
    lines.append("")
    lines.append("| Docs page | Mapped source docs path |")
    lines.append("|---|---|")
    for page, mapped in non_sdk_rows:
        lines.append(f"| `{page}` | `{mapped}` |" if mapped else f"| `{page}` | `UNMAPPED` |")
    lines.append("")
    lines.append("## `python-sdk` Doc to Source-Code Mapping")
    lines.append("")
    lines.append("| API page (`python-sdk`) | Mapped source module (`src`) |")
    lines.append("|---|---|")
    for page, mapped in sdk_rows:
        lines.append(f"| `{page}` | `{mapped}` |" if mapped else f"| `{page}` | `UNMAPPED` |")

    markdown = "\n".join(lines) + "\n"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(markdown)
    return markdown


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    skill_root = script_dir.parent
    default_output = skill_root / "references" / "02-doc-code-crosswalk-generated.md"

    parser = argparse.ArgumentParser(description="Generate a FastMCP docs-to-code crosswalk file.")
    parser.add_argument(
        "--docs-root",
        required=True,
        help="Path to docs directory",
    )
    parser.add_argument(
        "--source-repo",
        required=True,
        help="Path to source repository",
    )
    parser.add_argument(
        "--output",
        default=str(default_output),
        help="Output markdown file path",
    )
    args = parser.parse_args()

    docs_root = Path(args.docs_root).expanduser()
    source_repo = Path(args.source_repo).expanduser()
    output_file = Path(args.output).expanduser()

    if not docs_root.exists():
        raise SystemExit(f"docs root not found: {docs_root}")
    if not source_repo.exists():
        raise SystemExit(f"source repo not found: {source_repo}")

    build_markdown(docs_root=docs_root, source_repo=source_repo, output_file=output_file)
    print(f"Wrote: {output_file}")


if __name__ == "__main__":
    main()
