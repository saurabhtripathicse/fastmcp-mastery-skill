# Architecture And Layout

## Analyzed Documentation Folders (`fastmcpdocs`)

This folder is a markdown export/mirror of FastMCP documentation.

| Folder | Files | Purpose |
|---|---:|---|
| `apps` | 2 | App/UI features and low-level app APIs |
| `clients` | 17 | Client SDK usage, transports, auth, tasks, CLI |
| `deployment` | 4 | Running servers, HTTP, config, Horizon deployment |
| `development` | 3 | Contributing, tests, releases |
| `getting-started` | 6 | Installation, quickstart, upgrade guides |
| `integrations` | 26 | External platform and client integrations |
| `patterns` | 3 | Testing and CLI usage patterns |
| `python-sdk` | 208 | Auto-generated API reference from source modules |
| `root` | 2 | Changelog/updates pages |
| `servers` | 38 | Core server concepts, features, auth, providers, transforms |

## Source Repository Layout (`fastmcp-main`)

| Path | What it contains |
|---|---|
| `docs` | Mintlify docs source (`.mdx`) for gofastmcp.com |
| `src/fastmcp` | Python library implementation |
| `examples` | End-to-end usage patterns and templates |
| `tests` | Behavioral contracts for each subsystem |
| `skills` | Built-in FastMCP skills (small set) |

## Python Package Subsystems (`src/fastmcp`)

| Subsystem | File count | Role |
|---|---:|---|
| `server` | 108 | Server runtime, auth, providers, tasks, middleware, transforms |
| `client` | 30 | Client API, transports, sampling, tasks, callbacks |
| `utilities` | 38 | Shared helpers (schema, logging, openapi, config helpers) |
| `cli` | 19 | `fastmcp` command implementations |
| `tools` | 5 | Tool abstraction, conversion, transforms |
| `resources` | 5 | Resource and template abstractions |
| `prompts` | 3 | Prompt abstractions |

## Practical Relationship: Docs -> Code -> Examples -> Tests

Use this chain for every feature:

1. Find conceptual page in `fastmcpdocs`.
2. Map to source module in `src/fastmcp`.
3. Open matching example in `examples`.
4. Confirm expected behavior in `tests`.

This avoids stale assumptions from docs-only reading and reduces implementation mistakes.

## Important Note About `python-sdk`

`fastmcpdocs/python-sdk` is API reference output. It is not hand-written guide content.

- Best for: signatures, class/method inventory, source links.
- Less ideal for: choosing patterns or architecture.
- Combine it with `servers/*.md` and `clients/*.md` guides for context.
