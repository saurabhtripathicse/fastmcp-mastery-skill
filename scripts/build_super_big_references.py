#!/usr/bin/env python3
"""Build super-big FastMCP reference artifacts for the fastmcp-mastery skill.

This script generates exhaustive, derived markdown indexes from local inputs:
- fastmcpdocs
- fastmcp-main
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

GITHUB_SRC_RE = re.compile(r"https://github\.com/PrefectHQ/fastmcp/blob/main/src/([^#\s)]+)")


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")


def count_lines(path: Path) -> int:
    try:
        return len(path.read_text(errors="ignore").splitlines())
    except Exception:
        return 0


def map_non_sdk_doc_to_mdx(doc_rel: Path, docs_root: Path) -> Path | None:
    mapped = docs_root / doc_rel.with_suffix(".mdx")
    if mapped.exists():
        return mapped

    if doc_rel.parts and doc_rel.parts[0] == "root":
        root_level = docs_root / f"{doc_rel.stem}.mdx"
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


def first_h1_title(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# ") and "Source:" not in line:
            return line[2:].strip()
    return None


def first_module_header(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# `") and line.endswith("`"):
            return line[3:-1].strip()
    return None


SYMBOL_HEADING_RE = re.compile(r"^###\s+`([^`]+)`")


def parse_symbol_stats(text: str) -> tuple[int, int, list[str], list[str]]:
    state: str | None = None
    fn_names: list[str] = []
    cls_names: list[str] = []

    for raw in text.splitlines():
        line = raw.strip()

        if line == "## Functions":
            state = "functions"
            continue
        if line == "## Classes":
            state = "classes"
            continue
        if line.startswith("## ") and line not in {"## Functions", "## Classes"}:
            state = None

        symbol_match = SYMBOL_HEADING_RE.match(line)
        if symbol_match:
            name = symbol_match.group(1).strip()
            if not name:
                continue
            if state == "functions":
                fn_names.append(name)
            elif state == "classes":
                cls_names.append(name)

    return len(fn_names), len(cls_names), fn_names, cls_names


def page_group(page: Path) -> str:
    stem_parts = page.stem.split("-")
    if len(stem_parts) > 1 and stem_parts[0] == "fastmcp":
        return stem_parts[1]
    return stem_parts[0]


def collect_non_sdk_rows(docs_root: Path, source_docs_root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for page in sorted(p for p in docs_root.rglob("*.md") if "python-sdk" not in p.parts):
        rel = page.relative_to(docs_root)
        mapped = map_non_sdk_doc_to_mdx(rel, source_docs_root)
        section = rel.parts[0] if len(rel.parts) > 1 else "root"
        rows.append(
            {
                "page": str(rel),
                "section": section,
                "mapped": str(mapped.relative_to(source_docs_root.parent)) if mapped else "UNMAPPED",
                "line_count": str(count_lines(page)),
            }
        )
    return rows


def collect_python_sdk_rows(docs_root: Path, src_root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    sdk_root = docs_root / "python-sdk"
    for page in sorted(sdk_root.glob("*.md")):
        text = page.read_text(errors="ignore")
        mapped = map_python_sdk_doc_to_src(page, src_root)

        module_header = first_module_header(text) or ""
        h1 = first_h1_title(text) or ""
        fn_count, cls_count, fn_names, cls_names = parse_symbol_stats(text)

        github_match = GITHUB_SRC_RE.search(text)
        github_src = github_match.group(1) if github_match else ""

        rows.append(
            {
                "page": str(page.relative_to(docs_root)),
                "group": page_group(page),
                "title": h1,
                "module": module_header,
                "mapped": str(mapped.relative_to(src_root.parent)) if mapped else "UNMAPPED",
                "github_src": github_src,
                "functions": str(fn_count),
                "classes": str(cls_count),
                "sample_functions": ", ".join(fn_names[:6]),
                "sample_classes": ", ".join(cls_names[:6]),
                "line_count": str(count_lines(page)),
            }
        )
    return rows


def collect_source_rows(src_root: Path, sdk_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    reverse: dict[str, list[str]] = defaultdict(list)
    for row in sdk_rows:
        mapped = row["mapped"]
        if mapped != "UNMAPPED":
            reverse[mapped].append(row["page"])

    rows: list[dict[str, str]] = []
    for py in sorted((src_root / "fastmcp").rglob("*.py")):
        rel = py.relative_to(src_root)
        module_key = f"src/{rel}"
        top = rel.parts[1] if len(rel.parts) > 1 else "root"
        rows.append(
            {
                "module": module_key,
                "top": top,
                "line_count": str(count_lines(py)),
                "sdk_pages": ", ".join(reverse.get(module_key, [])),
            }
        )
    return rows


def topic_from_path(path: str) -> str:
    p = path.lower()
    if "auth" in p or "oauth" in p or "oidc" in p:
        return "auth"
    if "task" in p:
        return "tasks"
    if "sampling" in p:
        return "sampling"
    if "provider" in p or "mount" in p or "proxy" in p:
        return "providers-composition"
    if "transform" in p or "namespace" in p or "visibility" in p or "version" in p:
        return "transforms-versioning"
    if "config" in p or "mcp.json" in p:
        return "config"
    if "resource" in p:
        return "resources"
    if "prompt" in p:
        return "prompts"
    if "transport" in p or "sse" in p or "stdio" in p or "http" in p:
        return "transports"
    if "cli" in p or "discover" in p:
        return "cli"
    if "telemetry" in p or "trace" in p or "diagnostic" in p:
        return "telemetry-observability"
    if "middleware" in p or "logging" in p:
        return "middleware-logging"
    return "general"


def collect_examples_tests_rows(source_repo: Path) -> tuple[list[dict[str, str]], list[dict[str, str]], Counter]:
    examples_root = source_repo / "examples"
    tests_root = source_repo / "tests"

    example_rows: list[dict[str, str]] = []
    for path in sorted(examples_root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(source_repo)
        srel = str(rel)
        example_rows.append(
            {
                "path": srel,
                "topic": topic_from_path(srel),
                "line_count": str(count_lines(path)),
            }
        )

    test_rows: list[dict[str, str]] = []
    for path in sorted(tests_root.rglob("*.py")):
        rel = path.relative_to(source_repo)
        srel = str(rel)
        test_rows.append(
            {
                "path": srel,
                "topic": topic_from_path(srel),
                "line_count": str(count_lines(path)),
            }
        )

    topic_counts: Counter = Counter()
    for row in example_rows:
        topic_counts[f"examples::{row['topic']}"] += 1
    for row in test_rows:
        topic_counts[f"tests::{row['topic']}"] += 1

    return example_rows, test_rows, topic_counts


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def build_guides_index(non_sdk_rows: list[dict[str, str]], output: Path) -> None:
    by_section: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in non_sdk_rows:
        by_section[row["section"]].append(row)

    lines: list[str] = []
    lines.append("# Super-Big Guides Index (Generated)")
    lines.append("")
    lines.append(f"Generated at: `{now_utc()}`")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("")
    for section in sorted(by_section):
        lines.append(f"- [{section}](#{section})")
    lines.append("")

    for section in sorted(by_section):
        lines.append(f"## {section}")
        lines.append("")
        lines.append("| Page | Source docs path | Lines |")
        lines.append("|---|---|---:|")
        for row in sorted(by_section[section], key=lambda r: r["page"]):
            lines.append(f"| `{row['page']}` | `{row['mapped']}` | {row['line_count']} |")
        lines.append("")

    write_file(output, "\n".join(lines) + "\n")


def build_python_sdk_index(sdk_rows: list[dict[str, str]], output: Path) -> None:
    by_group: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sdk_rows:
        by_group[row["group"]].append(row)

    lines: list[str] = []
    lines.append("# Super-Big Python SDK Index (Generated)")
    lines.append("")
    lines.append(f"Generated at: `{now_utc()}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Group | Files | Total functions | Total classes |")
    lines.append("|---|---:|---:|---:|")
    for group, rows in sorted(by_group.items(), key=lambda x: (-len(x[1]), x[0])):
        fn_total = sum(int(r["functions"]) for r in rows)
        cls_total = sum(int(r["classes"]) for r in rows)
        lines.append(f"| `{group}` | {len(rows)} | {fn_total} | {cls_total} |")
    lines.append("")

    lines.append("## Table of Contents")
    lines.append("")
    for group, rows in sorted(by_group.items(), key=lambda x: (-len(x[1]), x[0])):
        lines.append(f"- [{group} ({len(rows)})](#{group})")
    lines.append("")

    for group, rows in sorted(by_group.items(), key=lambda x: (-len(x[1]), x[0])):
        lines.append(f"## {group}")
        lines.append("")
        lines.append("| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |")
        lines.append("|---|---|---|---|---:|---:|---|")
        for row in sorted(rows, key=lambda r: r["page"]):
            samples = ", ".join(x for x in [row["sample_functions"], row["sample_classes"]] if x)
            lines.append(
                f"| `{row['page']}` | `{row['module']}` | `{row['mapped']}` | `{row['github_src']}` | {row['functions']} | {row['classes']} | {samples} |"
            )
        lines.append("")

    write_file(output, "\n".join(lines) + "\n")


def build_source_reverse_index(source_rows: list[dict[str, str]], output: Path) -> None:
    by_top: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in source_rows:
        by_top[row["top"]].append(row)

    lines: list[str] = []
    lines.append("# Super-Big Source Reverse Index (Generated)")
    lines.append("")
    lines.append(f"Generated at: `{now_utc()}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Top subsystem | Files | Files with SDK page |")
    lines.append("|---|---:|---:|")
    for top, rows in sorted(by_top.items(), key=lambda x: (-len(x[1]), x[0])):
        covered = sum(1 for r in rows if r["sdk_pages"])
        lines.append(f"| `{top}` | {len(rows)} | {covered} |")
    lines.append("")

    lines.append("## Table of Contents")
    lines.append("")
    for top, rows in sorted(by_top.items(), key=lambda x: (-len(x[1]), x[0])):
        lines.append(f"- [{top} ({len(rows)})](#{top})")
    lines.append("")

    for top, rows in sorted(by_top.items(), key=lambda x: (-len(x[1]), x[0])):
        lines.append(f"## {top}")
        lines.append("")
        lines.append("| Source module | Lines | Linked SDK pages |")
        lines.append("|---|---:|---|")
        for row in sorted(rows, key=lambda r: r["module"]):
            sdk_pages = row["sdk_pages"] if row["sdk_pages"] else ""
            lines.append(f"| `{row['module']}` | {row['line_count']} | {sdk_pages} |")
        lines.append("")

    write_file(output, "\n".join(lines) + "\n")


def build_examples_tests_matrix(
    example_rows: list[dict[str, str]],
    test_rows: list[dict[str, str]],
    topic_counts: Counter,
    output: Path,
) -> None:
    ex_by_topic: dict[str, list[dict[str, str]]] = defaultdict(list)
    te_by_topic: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in example_rows:
        ex_by_topic[row["topic"]].append(row)
    for row in test_rows:
        te_by_topic[row["topic"]].append(row)

    topics = sorted({*ex_by_topic.keys(), *te_by_topic.keys()})

    lines: list[str] = []
    lines.append("# Super-Big Examples And Tests Matrix (Generated)")
    lines.append("")
    lines.append(f"Generated at: `{now_utc()}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Topic | Example files | Test files |")
    lines.append("|---|---:|---:|")
    for topic in topics:
        ex_count = topic_counts[f"examples::{topic}"]
        te_count = topic_counts[f"tests::{topic}"]
        lines.append(f"| `{topic}` | {ex_count} | {te_count} |")
    lines.append("")

    lines.append("## Table of Contents")
    lines.append("")
    for topic in topics:
        lines.append(f"- [{topic}](#{topic})")
    lines.append("")

    for topic in topics:
        lines.append(f"## {topic}")
        lines.append("")
        lines.append("### Example Files")
        lines.append("")
        lines.append("| Path | Lines |")
        lines.append("|---|---:|")
        for row in sorted(ex_by_topic.get(topic, []), key=lambda r: r["path"]):
            lines.append(f"| `{row['path']}` | {row['line_count']} |")
        if not ex_by_topic.get(topic):
            lines.append("| _none_ | 0 |")
        lines.append("")

        lines.append("### Test Files")
        lines.append("")
        lines.append("| Path | Lines |")
        lines.append("|---|---:|")
        for row in sorted(te_by_topic.get(topic, []), key=lambda r: r["path"]):
            lines.append(f"| `{row['path']}` | {row['line_count']} |")
        if not te_by_topic.get(topic):
            lines.append("| _none_ | 0 |")
        lines.append("")

    write_file(output, "\n".join(lines) + "\n")


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    skill_root = script_dir.parent
    default_docs_root = Path.cwd() / "fastmcpdocs"
    default_source_repo = Path.cwd() / "fastmcp-main"
    default_output_dir = skill_root / "references"

    parser = argparse.ArgumentParser(description="Generate super-big FastMCP reference artifacts.")
    parser.add_argument(
        "--docs-root",
        default=str(default_docs_root),
        help="Path to fastmcpdocs",
    )
    parser.add_argument(
        "--source-repo",
        default=str(default_source_repo),
        help="Path to fastmcp-main",
    )
    parser.add_argument(
        "--output-dir",
        default=str(default_output_dir),
        help="Output references directory",
    )
    args = parser.parse_args()

    docs_root = Path(args.docs_root).expanduser()
    source_repo = Path(args.source_repo).expanduser()
    output_dir = Path(args.output_dir).expanduser()

    source_docs_root = source_repo / "docs"
    source_src_root = source_repo / "src"

    non_sdk_rows = collect_non_sdk_rows(docs_root=docs_root, source_docs_root=source_docs_root)
    sdk_rows = collect_python_sdk_rows(docs_root=docs_root, src_root=source_src_root)
    source_rows = collect_source_rows(src_root=source_src_root, sdk_rows=sdk_rows)
    example_rows, test_rows, topic_counts = collect_examples_tests_rows(source_repo=source_repo)

    build_guides_index(non_sdk_rows=non_sdk_rows, output=output_dir / "10-guides-full-index-generated.md")
    build_python_sdk_index(sdk_rows=sdk_rows, output=output_dir / "11-python-sdk-full-index-generated.md")
    build_source_reverse_index(source_rows=source_rows, output=output_dir / "12-source-reverse-index-generated.md")
    build_examples_tests_matrix(
        example_rows=example_rows,
        test_rows=test_rows,
        topic_counts=topic_counts,
        output=output_dir / "13-examples-tests-matrix-generated.md",
    )

    print("Generated:")
    for name in [
        "10-guides-full-index-generated.md",
        "11-python-sdk-full-index-generated.md",
        "12-source-reverse-index-generated.md",
        "13-examples-tests-matrix-generated.md",
    ]:
        print(f"- {output_dir / name}")


if __name__ == "__main__":
    main()
