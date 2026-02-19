# Client Playbook

## Core Docs

- `fastmcpdocs/clients/client.md`
- `fastmcpdocs/clients/transports.md`
- `fastmcpdocs/clients/tools.md`
- `fastmcpdocs/clients/resources.md`
- `fastmcpdocs/clients/prompts.md`
- `fastmcpdocs/clients/tasks.md`
- `fastmcpdocs/clients/auth/oauth.md`
- `fastmcpdocs/clients/auth/bearer.md`

## Core Source Modules

- Main client: `fastmcp-main/src/fastmcp/client/client.py`
- Transport inference: `fastmcp-main/src/fastmcp/client/transports/inference.py`
- HTTP transport: `fastmcp-main/src/fastmcp/client/transports/http.py`
- SSE transport: `fastmcp-main/src/fastmcp/client/transports/sse.py`
- Stdio transport: `fastmcp-main/src/fastmcp/client/transports/stdio.py`
- In-memory transport: `fastmcp-main/src/fastmcp/client/transports/memory.py`

## Client Lifecycle Pattern

1. Construct `Client(...)` with transport target.
2. Enter context via `async with client:`.
3. Call tool/resource/prompt operations.
4. Exit context to close session cleanly.

Never skip client context management in production code.

## Transport Input Types Supported

`Client(...)` accepts multiple transport hints:

- URL string or `AnyUrl`
- local script `Path`
- `FastMCP` server instance
- `MCPConfig` or config dict
- explicit `ClientTransport`

Use this to keep call sites simple while preserving transport flexibility.

## Sampling, Progress, and Message Handling

Key modules:

- Sampling: `client/sampling/*`
- Progress callbacks: `client/progress.py`
- Generic messages: `client/messages.py`
- Elicitation callbacks: `client/elicitation.py`

Attach handlers when your client needs streaming-like updates, tool delegation, or richer telemetry.

## Example Paths To Reuse

- Proxy and in-memory client flow: `fastmcp-main/examples/in_memory_proxy_example.py`
- Persistent state client: `fastmcp-main/examples/persistent_state/client.py`
- Task client: `fastmcp-main/examples/tasks/client.py`
- Auth clients: `fastmcp-main/examples/auth/*/client.py`

## Tests That Define Expected Behavior

- `fastmcp-main/tests/client/client/test_client.py`
- `fastmcp-main/tests/client/transports/test_transports.py`
- `fastmcp-main/tests/client/test_roots.py`
- `fastmcp-main/tests/client/auth/test_oauth_client.py`
- `fastmcp-main/tests/client/test_sampling.py`
