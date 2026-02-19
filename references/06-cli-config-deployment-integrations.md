# CLI, Config, Deployment, Integrations

## CLI

### Docs

- `clients/cli.md`
- `clients/generate-cli.md`
- `patterns/cli.md`

### Source

- `src/fastmcp/cli/cli.py`
- `src/fastmcp/cli/run.py`
- `src/fastmcp/cli/client.py`
- `src/fastmcp/cli/discovery.py`
- `src/fastmcp/cli/install`

### Notes

Use CLI for discovery, list/call workflows, and installation shortcuts for desktop/editor MCP configs.

## MCP Config

### Docs

- `integrations/mcp-json-configuration.md`
- `deployment/server-configuration.md`

### Source

- `src/fastmcp/mcp_config.py`
- `src/fastmcp/utilities/mcp_server_config/v1`

### Examples

- `examples/fastmcp_config`
- `examples/fastmcp_config_demo`

## Deployment And Runtime

### Docs

- `deployment/running-server.md`
- `deployment/http.md`
- `deployment/prefect-horizon.md`

### Source

- `src/fastmcp/server/http.py`
- `src/fastmcp/settings.py`
- `src/fastmcp/server/telemetry.py`

### Validation

Use server integration tests for transport-level behavior before deploying.

## Integrations

`integrations` is mostly environment-specific setup guidance.

### High-value integration docs

- `openai.md`, `anthropic.md`, `chatgpt.md`, `claude-desktop.md`, `claude-code.md`, `cursor.md`, `gemini-cli.md`, `goose.md`
- auth providers: `auth0.md`, `aws-cognito.md`, `azure.md`, `descope.md`, `github.md`, `google.md`, `oci.md`, `scalekit.md`, `supabase.md`, `workos.md`
- protocol/interop: `openapi.md`, `fastapi.md`, `mcp-json-configuration.md`

### Rule

Treat integration docs as setup overlays. Confirm protocol behavior in core server/client modules and tests.
