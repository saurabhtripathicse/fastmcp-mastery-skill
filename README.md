# FastMCP Mastery Skill

A super-sized FastMCP skill package for Codex, Claude, Cursor, Windsurf, Cline, and Replit.

This repository is designed to reduce hallucinations by forcing docs -> source -> examples -> tests cross-checking.

## What Is In This Repo

- `SKILL.md`: primary routing and execution guidance
- `references/`: playbooks, snippet library, generated indexes, and feature coverage map
- `scripts/build_fastmcp_crosswalk.py`: generates docs-to-code crosswalk
- `scripts/build_super_big_references.py`: generates full indexes and matrices
- `scripts/install_platform_adapters.py`: installs this skill into multiple coding platforms
- `platform-adapters/`: templates for Cursor/Windsurf/Cline rules
- `agents/openai.yaml`: UI metadata for skill-enabled environments

No fixed local folder names are required. The skill works with whichever FastMCP docs/source locations exist in your workspace.

## Quick Start (Install Everywhere)

```bash
git clone https://github.com/saurabhtripathicse/fastmcp-mastery-skill.git
cd fastmcp-mastery-skill
python3 scripts/install_platform_adapters.py --platforms all --project /path/to/your/project --clean
```

Preview changes without writing files:

```bash
python3 scripts/install_platform_adapters.py --platforms all --project /path/to/your/project --dry-run
```

## Platform Integration Guide

### Codex

- User-scope install target: `~/.agents/skills/fastmcp-mastery`
- Project-scope install target: `/path/to/project/.agents/skills/fastmcp-mastery`
- Trigger in prompts with: `$fastmcp-mastery`

### Claude Code

- User-scope install target: `~/.claude/skills/fastmcp-mastery`
- Project-scope install target: `/path/to/project/.claude/skills/fastmcp-mastery`
- Trigger with: `$fastmcp-mastery` or by requesting FastMCP-specific help

### Cursor

- Rule file: `/path/to/project/.cursor/rules/fastmcp-mastery.mdc`
- Skill bundle used by rule: `/path/to/project/.agents/skills/fastmcp-mastery`
- Cursor applies the rule automatically based on rule scope

### Windsurf

- Project skill: `/path/to/project/.windsurf/skills/fastmcp-mastery`
- Global skill: `~/.codeium/windsurf/skills/fastmcp-mastery`
- Rule file: `/path/to/project/.windsurf/rules/fastmcp-mastery.md`
- Project skill bundle for cross-tool compatibility: `/path/to/project/.agents/skills/fastmcp-mastery`

### Cline

- Appends/updates managed block in: `/path/to/project/.clinerules`
- Uses project skill path: `/path/to/project/.agents/skills/fastmcp-mastery`

### Replit

- Replit integration uses the project bundle path: `/path/to/project/.agents/skills/fastmcp-mastery`

Install selected platforms only:

```bash
python3 scripts/install_platform_adapters.py --platforms claude,cursor,windsurf --project /path/to/your/project
```

## Update Existing Installs

```bash
git pull
python3 scripts/install_platform_adapters.py --platforms all --project /path/to/your/project --clean
```

## Key Reference Artifacts

- `references/02-doc-code-crosswalk-generated.md`
- `references/10-guides-full-index-generated.md`
- `references/11-python-sdk-full-index-generated.md`
- `references/12-source-reverse-index-generated.md`
- `references/13-examples-tests-matrix-generated.md`
- `references/16-feature-coverage-map.md`

## Regenerate Indexes

Run when local FastMCP docs/source content changes:

```bash
python3 scripts/build_fastmcp_crosswalk.py --docs-root /path/to/docs-root --source-repo /path/to/source-repo
python3 scripts/build_super_big_references.py --docs-root /path/to/docs-root --source-repo /path/to/source-repo
```

## Validate Skill

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" .
```

## Repository Notes

- Python bytecode artifacts are ignored (`__pycache__/`, `*.pyc`).
- The skill is intentionally large and reference-heavy for advanced FastMCP analysis.
