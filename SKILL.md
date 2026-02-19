---
name: fastmcp-mastery
description: FastMCP-only implementation and debugging workflow that maps docs pages to source code, examples, and tests. Use when building or extending FastMCP servers/clients, transports, auth/OAuth, providers/transforms/tasks, CLI/config, or when reducing hallucination risk by grounding answers in code.
---

# FastMCP Mastery

## Overview
Use this skill to connect FastMCP documentation to the actual Python implementation and examples. Route each request to the smallest relevant reference file, then verify behavior in source code and tests before implementing changes.

## Optional Local Validation Inputs
This skill is self-contained. If local FastMCP checkouts are available, use them to validate behavior:

- docs markers: `python-sdk/`, `getting-started/`, guide markdown tree
- source markers: `src/fastmcp/`, `examples/`, `tests/`

If those local checkouts are unavailable, rely on bundled references in this skill.

## Execution Workflow

1. Classify the request.
2. Load only the matching reference file from `references/`.
3. Jump from docs to code using `references/02-doc-code-crosswalk.md`.
4. Validate assumptions against `tests` and `examples`.
5. Implement or explain using runnable snippets from `references/08-snippet-library.md`.
6. For large-scope tasks, use the generated super-big indexes.
7. Refresh generated artifacts when needed.

## Request Routing

| Request type | Load this first |
|---|---|
| "What is in this repo / where do I start?" | `references/00-reading-order.md` |
| "How are folders and docs organized?" | `references/01-architecture-and-layout.md` |
| "Which doc maps to which source module?" | `references/02-doc-code-crosswalk.md` |
| "Build or debug a server" | `references/03-server-playbook.md` |
| "Build or debug a client" | `references/04-client-playbook.md` |
| "Auth, providers, transforms, tasks" | `references/05-auth-providers-transforms-tasks.md` |
| "CLI, config, deployment, integrations" | `references/06-cli-config-deployment-integrations.md` |
| "Need example to copy or adapt" | `references/07-example-catalog.md` |
| "Need ready-to-run code snippets" | `references/08-snippet-library.md` |
| "Need tests and debugging strategy" | `references/09-testing-and-debugging.md` |
| "Need full docs index by section" | `references/10-guides-full-index-generated.md` |
| "Need full python-sdk symbol index" | `references/11-python-sdk-full-index-generated.md` |
| "Need source -> sdk reverse mapping" | `references/12-source-reverse-index-generated.md` |
| "Need examples/tests by topic" | `references/13-examples-tests-matrix-generated.md` |
| "Need large-scale navigation strategy" | `references/14-super-big-navigation.md` |
| "Need intent to execution mapping" | `references/15-intent-to-workflow-map.md` |
| "Need feature checklist coverage" | `references/16-feature-coverage-map.md` |

## Crosswalk Maintenance
Regenerate the full local crosswalk and super-big indexes when repository contents change:

```bash
python3 scripts/build_fastmcp_crosswalk.py --docs-root /path/to/docs --source-repo /path/to/repo
python3 scripts/build_super_big_references.py --docs-root /path/to/docs --source-repo /path/to/repo
```

Generated output:

- `references/02-doc-code-crosswalk-generated.md`
- `references/10-guides-full-index-generated.md`
- `references/11-python-sdk-full-index-generated.md`
- `references/12-source-reverse-index-generated.md`
- `references/13-examples-tests-matrix-generated.md`

## Fast Path Commands
Use these commands for high-speed navigation:

```bash
cd /path/to/repo
rg --files src/fastmcp
rg --files examples
rg --files tests
rg "class FastMCP|def create_proxy" src/fastmcp/server/server.py
rg "class Client|def call_tool" src/fastmcp/client/client.py
```

## Output Standard
When producing guidance or code changes, include:

- Relevant docs page path
- Matching source path from `src/fastmcp`
- At least one example path from `examples`
- At least one test path from `tests` for expected behavior
