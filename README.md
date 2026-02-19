# FastMCP Mastery Skill

A super-sized Codex skill for working with FastMCP using local evidence from:

- `docs` (documentation mirror)
- `repo` (source code, examples, tests)

This skill is designed to reduce hallucination risk by forcing docs -> source -> examples -> tests cross-checking.

No specific directory names are required. `docs` and `repo` are logical inputs, not fixed folder names.

## Contents

- `SKILL.md`: main routing and execution guidance
- `references/`: playbooks, snippet library, generated indexes, and feature coverage map
- `scripts/build_fastmcp_crosswalk.py`: generates docs-to-code crosswalk
- `scripts/build_super_big_references.py`: generates large indexes for guides, SDK pages, source reverse map, and examples/tests matrix
- `scripts/install_platform_adapters.py`: GitHub-only installer for Claude/Codex/Replit/Cursor/Windsurf/Cline
- `platform-adapters/`: rule templates used by the installer

## Key Reference Artifacts

- `references/02-doc-code-crosswalk-generated.md`
- `references/10-guides-full-index-generated.md`
- `references/11-python-sdk-full-index-generated.md`
- `references/12-source-reverse-index-generated.md`
- `references/13-examples-tests-matrix-generated.md`
- `references/16-feature-coverage-map.md` (maintained checklist)

## Regenerate Indexes

Run when `docs` or `repo` changes:

```bash
python3 scripts/build_fastmcp_crosswalk.py --docs-root /path/to/docs-root --source-repo /path/to/source-repo
python3 scripts/build_super_big_references.py --docs-root /path/to/docs-root --source-repo /path/to/source-repo
```

## Validate Skill

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" .
```

## Install In Codex

```bash
python3 "$CODEX_HOME/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --url https://github.com/<owner>/<repo>.git \
  --method git
```

## GitHub-Only Multi-Platform Install

Clone once, then install everywhere from this repo:

```bash
git clone https://github.com/saurabhtripathicse/fastmcp-mastery-skill.git
cd fastmcp-mastery-skill
python3 scripts/install_platform_adapters.py --platforms all --project /path/to/your/project --clean
```

What this command installs:

- `Claude`: `~/.claude/skills/fastmcp-mastery`
- `Codex/Replit/Project skill bundle`: `/path/to/your/project/.agents/skills/fastmcp-mastery`
- `Cursor` rule: `/path/to/your/project/.cursor/rules/fastmcp-mastery.mdc`
- `Windsurf` rule: `/path/to/your/project/.windsurf/rules/fastmcp-mastery.md`
- `Cline` block: `/path/to/your/project/.clinerules`

Install selected platforms only:

```bash
python3 scripts/install_platform_adapters.py --platforms claude,cursor,windsurf --project /path/to/your/project
```

Preview without writing files:

```bash
python3 scripts/install_platform_adapters.py --platforms all --project /path/to/your/project --dry-run
```

## Repository Notes

- Python bytecode artifacts are ignored (`__pycache__/`, `*.pyc`).
- The skill is intentionally large and reference-heavy for advanced FastMCP analysis.
