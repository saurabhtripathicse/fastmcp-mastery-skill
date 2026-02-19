# CLI, Config, Deployment, Integrations

## CLI

### Docs

- `fastmcpdocs/clients/cli.md`
- `fastmcpdocs/clients/generate-cli.md`
- `fastmcpdocs/patterns/cli.md`

### Source

- `fastmcp-main/src/fastmcp/cli/cli.py`
- `fastmcp-main/src/fastmcp/cli/run.py`
- `fastmcp-main/src/fastmcp/cli/client.py`
- `fastmcp-main/src/fastmcp/cli/discovery.py`
- `fastmcp-main/src/fastmcp/cli/install`

### Notes

Use CLI for discovery, list/call workflows, and installation shortcuts for desktop/editor MCP configs.

## MCP Config

### Docs

- `fastmcpdocs/integrations/mcp-json-configuration.md`
- `fastmcpdocs/deployment/server-configuration.md`

### Source

- `fastmcp-main/src/fastmcp/mcp_config.py`
- `fastmcp-main/src/fastmcp/utilities/mcp_server_config/v1`

### Examples

- `fastmcp-main/examples/fastmcp_config`
- `fastmcp-main/examples/fastmcp_config_demo`

## Deployment And Runtime

### Docs

- `fastmcpdocs/deployment/running-server.md`
- `fastmcpdocs/deployment/http.md`
- `fastmcpdocs/deployment/prefect-horizon.md`

### Source

- `fastmcp-main/src/fastmcp/server/http.py`
- `fastmcp-main/src/fastmcp/settings.py`
- `fastmcp-main/src/fastmcp/server/telemetry.py`

### Validation

Use server integration tests for transport-level behavior before deploying.

## Integrations

`fastmcpdocs/integrations` is mostly environment-specific setup guidance.

### High-value integration docs

- `openai.md`, `anthropic.md`, `chatgpt.md`, `claude-desktop.md`, `claude-code.md`, `cursor.md`, `gemini-cli.md`, `goose.md`
- auth providers: `auth0.md`, `aws-cognito.md`, `azure.md`, `descope.md`, `github.md`, `google.md`, `oci.md`, `scalekit.md`, `supabase.md`, `workos.md`
- protocol/interop: `openapi.md`, `fastapi.md`, `mcp-json-configuration.md`

### Rule

Treat integration docs as setup overlays. Confirm protocol behavior in core server/client modules and tests.
