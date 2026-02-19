# Client Playbook

## Core Docs

- `clients/client.md`
- `clients/transports.md`
- `clients/tools.md`
- `clients/resources.md`
- `clients/prompts.md`
- `clients/tasks.md`
- `clients/auth/oauth.md`
- `clients/auth/bearer.md`

## Core Source Modules

- Main client: `src/fastmcp/client/client.py`
- Transport inference: `src/fastmcp/client/transports/inference.py`
- HTTP transport: `src/fastmcp/client/transports/http.py`
- SSE transport: `src/fastmcp/client/transports/sse.py`
- Stdio transport: `src/fastmcp/client/transports/stdio.py`
- In-memory transport: `src/fastmcp/client/transports/memory.py`

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

- Proxy and in-memory client flow: `examples/in_memory_proxy_example.py`
- Persistent state client: `examples/persistent_state/client.py`
- Task client: `examples/tasks/client.py`
- Auth clients: `examples/auth/*/client.py`

## Tests That Define Expected Behavior

- `tests/client/client/test_client.py`
- `tests/client/transports/test_transports.py`
- `tests/client/test_roots.py`
- `tests/client/auth/test_oauth_client.py`
- `tests/client/test_sampling.py`
