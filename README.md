# FastMCP Mastery Skill

A super-sized Codex skill for working with FastMCP using local evidence from:

- `fastmcpdocs` (documentation mirror)
- `fastmcp-main` (source code, examples, tests)

This skill is designed to reduce hallucination risk by forcing docs -> source -> examples -> tests cross-checking.

## Contents

- `SKILL.md`: main routing and execution guidance
- `references/`: playbooks, snippet library, and generated indexes
- `scripts/build_fastmcp_crosswalk.py`: generates docs-to-code crosswalk
- `scripts/build_super_big_references.py`: generates large indexes for guides, SDK pages, source reverse map, and examples/tests matrix

## Key Generated Artifacts

- `references/02-doc-code-crosswalk-generated.md`
- `references/10-guides-full-index-generated.md`
- `references/11-python-sdk-full-index-generated.md`
- `references/12-source-reverse-index-generated.md`
- `references/13-examples-tests-matrix-generated.md`

## Regenerate Indexes

Run when `fastmcpdocs` or `fastmcp-main` changes:

```bash
python3 scripts/build_fastmcp_crosswalk.py
python3 scripts/build_super_big_references.py
```

## Validate Skill

```bash
python3 /Users/saurabhtripathi/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## Repository Notes

- Python bytecode artifacts are ignored (`__pycache__/`, `*.pyc`).
- The skill is intentionally large and reference-heavy for advanced FastMCP analysis.
