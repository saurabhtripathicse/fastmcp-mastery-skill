#!/usr/bin/env python3
"""Install fastmcp-mastery from this repo into multiple coding platforms.

GitHub-only flow:
1) Clone this repository.
2) Run this script to copy the canonical skill into platform locations.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

SKILL_NAME = "fastmcp-mastery"
PROJECT_SKILL_REL = Path(".agents") / "skills" / SKILL_NAME
CLAUDE_SKILL_REL = Path(".claude") / "skills" / SKILL_NAME
WINDSURF_SKILL_REL = Path(".windsurf") / "skills" / SKILL_NAME
WINDSURF_GLOBAL_SKILL_REL = Path(".codeium") / "windsurf" / "skills" / SKILL_NAME
SOURCE_ITEMS = ("SKILL.md", "agents", "references", "scripts", "LICENSE")

ALL_PLATFORMS = {"claude", "codex", "replit", "cursor", "windsurf", "cline"}
PROJECT_PLATFORMS = {"codex", "replit", "cursor", "windsurf", "cline"}


def parse_platforms(value: str) -> set[str]:
    parts = {p.strip().lower() for p in value.split(",") if p.strip()}
    if not parts:
        raise SystemExit("At least one platform is required.")
    if "all" in parts:
        return set(ALL_PLATFORMS)

    unknown = sorted(parts - ALL_PLATFORMS)
    if unknown:
        raise SystemExit(f"Unknown platforms: {', '.join(unknown)}")
    return parts


def copy_source_items(
    source_root: Path,
    destination_root: Path,
    clean: bool,
    dry_run: bool,
) -> None:
    if clean and destination_root.exists():
        print(f"[clean] {destination_root}")
        if not dry_run:
            shutil.rmtree(destination_root)

    if not destination_root.exists():
        print(f"[mkdir] {destination_root}")
        if not dry_run:
            destination_root.mkdir(parents=True, exist_ok=True)

    for item in SOURCE_ITEMS:
        source = source_root / item
        target = destination_root / item
        if not source.exists():
            raise SystemExit(f"Missing source item: {source}")

        if source.is_dir():
            print(f"[copy-dir] {source} -> {target}")
            if not dry_run:
                shutil.copytree(
                    source,
                    target,
                    dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
                )
        else:
            print(f"[copy-file] {source} -> {target}")
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)


def render_template(template_path: Path, skill_rel_path: str) -> str:
    template = template_path.read_text()
    return template.replace("__SKILL_PATH__", skill_rel_path)


def write_text(path: Path, content: str, dry_run: bool) -> None:
    print(f"[write] {path}")
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def install_cursor_rule(
    templates_root: Path,
    project_root: Path,
    skill_rel_path: str,
    dry_run: bool,
) -> None:
    template = templates_root / "cursor" / "fastmcp-mastery.mdc"
    content = render_template(template, skill_rel_path)
    destination = project_root / ".cursor" / "rules" / "fastmcp-mastery.mdc"
    write_text(destination, content, dry_run=dry_run)


def install_windsurf_rule(
    templates_root: Path,
    project_root: Path,
    skill_rel_path: str,
    dry_run: bool,
) -> None:
    template = templates_root / "windsurf" / "fastmcp-mastery.md"
    content = render_template(template, skill_rel_path)
    destination = project_root / ".windsurf" / "rules" / "fastmcp-mastery.md"
    write_text(destination, content, dry_run=dry_run)


def install_windsurf_skill(
    source_root: Path,
    destination_root: Path,
    clean: bool,
    dry_run: bool,
) -> None:
    copy_source_items(source_root, destination_root, clean=clean, dry_run=dry_run)


def install_cline_rule(
    templates_root: Path,
    project_root: Path,
    skill_rel_path: str,
    dry_run: bool,
) -> None:
    template = templates_root / "cline" / "fastmcp-mastery.md"
    body = render_template(template, skill_rel_path).strip()
    start = "<!-- FASTMCP-MASTERY:START -->"
    end = "<!-- FASTMCP-MASTERY:END -->"
    block = f"{start}\n{body}\n{end}\n"
    destination = project_root / ".clinerules"
    if destination.exists():
        existing = destination.read_text()
    else:
        existing = ""

    if start in existing and end in existing:
        before = existing.split(start, 1)[0]
        after = existing.split(end, 1)[1]
        merged = f"{before}{block}{after.lstrip()}"
    else:
        spacer = "\n" if existing and not existing.endswith("\n") else ""
        merged = f"{existing}{spacer}{block}"

    write_text(destination, merged, dry_run=dry_run)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Install fastmcp-mastery skill/adapters from this repo to platform locations."
    )
    parser.add_argument(
        "--platforms",
        default="all",
        help="Comma-separated list: all,claude,codex,replit,cursor,windsurf,cline",
    )
    parser.add_argument(
        "--project",
        default=".",
        help="Project root for project-based installs (default: current directory).",
    )
    parser.add_argument(
        "--home",
        default=str(Path.home()),
        help="Home directory for personal installs (default: current user home).",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove target skill directory before copying.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned actions without writing files.",
    )
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    skill_root = script_path.parent.parent
    templates_root = skill_root / "platform-adapters"

    selected = parse_platforms(args.platforms)
    project_root = Path(args.project).expanduser().resolve()
    home_root = Path(args.home).expanduser().resolve()
    skill_rel = str(PROJECT_SKILL_REL).replace("\\", "/")

    if "claude" in selected:
        claude_dest = home_root / CLAUDE_SKILL_REL
        print("\n== Installing for Claude Code ==")
        copy_source_items(skill_root, claude_dest, clean=args.clean, dry_run=args.dry_run)
        claude_project_dest = project_root / CLAUDE_SKILL_REL
        print("\n== Installing for Claude Code (project scope) ==")
        copy_source_items(skill_root, claude_project_dest, clean=args.clean, dry_run=args.dry_run)

    if "codex" in selected:
        codex_user_dest = home_root / PROJECT_SKILL_REL
        print("\n== Installing for Codex (user scope) ==")
        copy_source_items(skill_root, codex_user_dest, clean=args.clean, dry_run=args.dry_run)

    if selected & PROJECT_PLATFORMS:
        project_skill_dest = project_root / PROJECT_SKILL_REL
        print("\n== Installing project skill bundle (.agents/skills) ==")
        copy_source_items(skill_root, project_skill_dest, clean=args.clean, dry_run=args.dry_run)

    if "cursor" in selected:
        print("\n== Installing Cursor rule ==")
        install_cursor_rule(templates_root, project_root, skill_rel, dry_run=args.dry_run)

    if "windsurf" in selected:
        print("\n== Installing Windsurf native skill ==")
        install_windsurf_skill(
            skill_root,
            project_root / WINDSURF_SKILL_REL,
            clean=args.clean,
            dry_run=args.dry_run,
        )
        print("\n== Installing Windsurf native skill (global) ==")
        install_windsurf_skill(
            skill_root,
            home_root / WINDSURF_GLOBAL_SKILL_REL,
            clean=args.clean,
            dry_run=args.dry_run,
        )
        print("\n== Installing Windsurf rule ==")
        install_windsurf_rule(templates_root, project_root, skill_rel, dry_run=args.dry_run)

    if "cline" in selected:
        print("\n== Installing Cline .clinerules block ==")
        install_cline_rule(templates_root, project_root, skill_rel, dry_run=args.dry_run)

    print("\nDone.")


if __name__ == "__main__":
    main()
