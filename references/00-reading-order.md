# FastMCP Reading Order

## Goal
Use this guide to analyze FastMCP quickly without loading all docs at once.

## Minimal Reading Sequence

1. Read `01-architecture-and-layout.md` to understand repo shape.
2. Read `02-doc-code-crosswalk.md` to map docs to implementation.
3. Read one playbook file based on task type:
   - Server work: `03-server-playbook.md`
   - Client work: `04-client-playbook.md`
   - Auth/providers/transforms/tasks: `05-auth-providers-transforms-tasks.md`
   - CLI/deployment/integrations: `06-cli-config-deployment-integrations.md`
4. Pull a runnable pattern from `08-snippet-library.md`.
5. Validate behavior via `09-testing-and-debugging.md`.

## Decision Matrix

| If the user asks about... | Start with | Then verify in |
|---|---|---|
| Basic "how to build a server" | `03-server-playbook.md` | `fastmcp-main/examples/simple_echo.py` |
| Tool/resource/prompt registration | `03-server-playbook.md` | `fastmcp-main/src/fastmcp/server/server.py` |
| Client transports and calls | `04-client-playbook.md` | `fastmcp-main/src/fastmcp/client/transports` |
| OAuth, token verification, auth providers | `05-auth-providers-transforms-tasks.md` | `fastmcp-main/src/fastmcp/server/auth` |
| Dynamic capabilities and composition | `05-auth-providers-transforms-tasks.md` | `fastmcp-main/src/fastmcp/server/providers` |
| fastmcp CLI usage | `06-cli-config-deployment-integrations.md` | `fastmcp-main/src/fastmcp/cli` |
| Real usage patterns | `07-example-catalog.md` | `fastmcp-main/examples` |
| Regression risk / expected behavior | `09-testing-and-debugging.md` | `fastmcp-main/tests` |

## High-Signal Paths

- Primary docs mirror: `/Users/saurabhtripathi/project-zero/fastmcpdocs`
- Canonical docs source: `/Users/saurabhtripathi/project-zero/fastmcp-main/docs`
- Python SDK source: `/Users/saurabhtripathi/project-zero/fastmcp-main/src/fastmcp`
- Runnable examples: `/Users/saurabhtripathi/project-zero/fastmcp-main/examples`
- Behavioral contract: `/Users/saurabhtripathi/project-zero/fastmcp-main/tests`
