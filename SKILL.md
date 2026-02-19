---
name: fastmcp-mastery
description: Comprehensive FastMCP implementation, debugging, and integration guide that maps fastmcpdocs pages to fastmcp-main source code, tests, and examples. Use when building or extending FastMCP servers or clients, choosing transports, configuring auth/OAuth, working with providers/transforms/tasks, migrating versions, or troubleshooting behavior seen in FastMCP docs and Python code.
---

# FastMCP Mastery

## Overview
Use this skill to connect FastMCP documentation to the actual Python implementation and examples. Route each request to the smallest relevant reference file, then verify behavior in source code and tests before implementing changes.

## Verify Workspace Inputs
Confirm these paths exist before deep analysis:

- `fastmcpdocs`
- `fastmcp-main`

If one path is missing, continue with available artifacts and state the gap.

## Execution Workflow

1. Classify the request.
2. Load only the matching reference file from `references/`.
3. Jump from docs to code using `references/02-doc-code-crosswalk.md`.
4. Validate assumptions against `fastmcp-main/tests` and `fastmcp-main/examples`.
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

## Crosswalk Maintenance
Regenerate the full local crosswalk and super-big indexes when repository contents change:

```bash
python3 /Users/saurabhtripathi/project-zero/skills/fastmcp-mastery/scripts/build_fastmcp_crosswalk.py
python3 /Users/saurabhtripathi/project-zero/skills/fastmcp-mastery/scripts/build_super_big_references.py
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
rg --files /Users/saurabhtripathi/project-zero/fastmcp-main/src/fastmcp
rg --files /Users/saurabhtripathi/project-zero/fastmcp-main/examples
rg --files /Users/saurabhtripathi/project-zero/fastmcp-main/tests
rg "class FastMCP|def create_proxy" /Users/saurabhtripathi/project-zero/fastmcp-main/src/fastmcp/server/server.py
rg "class Client|def call_tool" /Users/saurabhtripathi/project-zero/fastmcp-main/src/fastmcp/client/client.py
```

## Output Standard
When producing guidance or code changes, include:

- Relevant docs path from `fastmcpdocs`
- Matching source path from `fastmcp-main/src/fastmcp`
- At least one example path from `fastmcp-main/examples`
- At least one test path from `fastmcp-main/tests` for expected behavior
