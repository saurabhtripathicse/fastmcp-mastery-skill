# Documentation To Code Crosswalk

## Coverage Summary

- Non-`python-sdk` documentation pages analyzed: `101`
- Pages mapping directly to `fastmcp-main/docs/*.mdx`: `99`
- Special root mappings: `root/changelog.md` -> `docs/changelog.mdx`, `root/updates.md` -> `docs/updates.mdx`
- `python-sdk` pages analyzed: `208`
- `python-sdk` pages mapped to `src/fastmcp/*`: `208`

## Topical Mapping

| Topic | Docs page(s) | Primary source modules |
|---|---|---|
| Server core | `servers/server.md` | `src/fastmcp/server/server.py` |
| Tools | `servers/tools.md` | `src/fastmcp/tools/function_tool.py`, `src/fastmcp/tools/tool.py` |
| Resources | `servers/resources.md` | `src/fastmcp/resources/resource.py`, `src/fastmcp/resources/template.py` |
| Prompts | `servers/prompts.md` | `src/fastmcp/prompts/function_prompt.py`, `src/fastmcp/prompts/prompt.py` |
| Context and DI | `servers/context.md`, `servers/dependency-injection.md` | `src/fastmcp/server/context.py`, `src/fastmcp/server/dependencies.py` |
| Middleware | `servers/middleware.md`, `servers/logging.md` | `src/fastmcp/server/middleware/*` |
| Providers | `servers/providers/*.md` | `src/fastmcp/server/providers/*` |
| Transforms and visibility | `servers/transforms/*.md`, `servers/visibility.md` | `src/fastmcp/server/transforms/*` |
| Auth and authorization | `servers/auth/*.md`, `servers/authorization.md` | `src/fastmcp/server/auth/*` |
| Tasks and progress | `servers/tasks.md`, `servers/progress.md`, `servers/pagination.md` | `src/fastmcp/server/tasks/*`, `src/fastmcp/server/context.py` |
| Client core | `clients/client.md` | `src/fastmcp/client/client.py` |
| Client transports | `clients/transports.md` | `src/fastmcp/client/transports/*` |
| Client auth | `clients/auth/*.md` | `src/fastmcp/client/auth/*` |
| Client sampling | `clients/sampling.md` | `src/fastmcp/client/sampling/*` |
| CLI | `clients/cli.md`, `patterns/cli.md` | `src/fastmcp/cli/*` |
| MCP config | `integrations/mcp-json-configuration.md` | `src/fastmcp/mcp_config.py`, `src/fastmcp/utilities/mcp_server_config/*` |
| Deployment | `deployment/*.md` | `src/fastmcp/server/http.py`, `src/fastmcp/settings.py` |

## `python-sdk` Section Distribution

| Group | Files |
|---|---:|
| `server` | 105 |
| `utilities` | 36 |
| `client` | 30 |
| `cli` | 18 |
| `tools` | 5 |
| `resources` | 5 |
| `prompts` | 3 |
| `settings`, `dependencies`, `telemetry`, `decorators`, `mcp_config`, `exceptions` | 1 each |

## Regenerate Full Mapping

Run this command to produce a complete machine-generated mapping table for every file:

```bash
python3 scripts/build_fastmcp_crosswalk.py --docs-root /path/to/fastmcpdocs --source-repo /path/to/fastmcp-main
```

Generated file:

- `02-doc-code-crosswalk-generated.md`
