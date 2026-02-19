# Super-Big Navigation Guide

## Purpose
Use this guide to query very large FastMCP documentation quickly without loading everything.

## Generated Artifacts

- `10-guides-full-index-generated.md`: full non-API docs index with source-doc mapping.
- `11-python-sdk-full-index-generated.md`: all `python-sdk` API pages with symbol summaries.
- `12-source-reverse-index-generated.md`: reverse lookup from source modules to SDK pages.
- `13-examples-tests-matrix-generated.md`: topic matrix for examples and tests.

## Task-Based Retrieval Patterns

### Pattern A: "I have a docs page, where is code?"

1. Search page in `10-guides-full-index-generated.md`.
2. Jump to source docs path.
3. Use `02-doc-code-crosswalk-generated.md` to find mapped source module.
4. Validate with matching test folder from `13-examples-tests-matrix-generated.md`.

### Pattern B: "I have a source module, what docs explain it?"

1. Search module path in `12-source-reverse-index-generated.md`.
2. Open linked SDK pages.
3. Open conceptual page in `servers/*`, `clients/*`, or `deployment/*`.

### Pattern C: "I need examples and tests for topic X"

1. Open `13-examples-tests-matrix-generated.md`.
2. Jump to section `auth`, `tasks`, `providers-composition`, etc.
3. Pick minimal example + nearest tests.

### Pattern D: "I need all symbols in subsystem X"

1. Open `11-python-sdk-full-index-generated.md`.
2. Jump to group heading (`server`, `client`, `utilities`, `cli`).
3. Use sample symbols column as function/class index.

## High-Speed Commands

```bash
# Search within generated references
rg "server\.auth\.providers" references/11-python-sdk-full-index-generated.md
rg "providers-proxy" references/13-examples-tests-matrix-generated.md

# Search source + tests together
rg "OAuthProxy|OIDC|TokenVerifier" /path/to/fastmcp-main/src/fastmcp /path/to/fastmcp-main/tests

# Refresh all generated indexes
python3 scripts/build_fastmcp_crosswalk.py --docs-root /path/to/fastmcpdocs --source-repo /path/to/fastmcp-main
python3 scripts/build_super_big_references.py --docs-root /path/to/fastmcpdocs --source-repo /path/to/fastmcp-main
```

## Practical Rule
Never finalize guidance from one page alone. Always include:

- one conceptual docs page,
- one source module,
- one example,
- one test path.
