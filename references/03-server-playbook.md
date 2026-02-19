# Server Playbook

## Core Docs

Start here for server work:

- `fastmcpdocs/servers/server.md`
- `fastmcpdocs/servers/tools.md`
- `fastmcpdocs/servers/resources.md`
- `fastmcpdocs/servers/prompts.md`
- `fastmcpdocs/servers/context.md`

## Core Source Modules

- Server entry: `fastmcp-main/src/fastmcp/server/server.py`
- Runtime context: `fastmcp-main/src/fastmcp/server/context.py`
- Dependency wiring: `fastmcp-main/src/fastmcp/server/dependencies.py`
- Low-level wrapper: `fastmcp-main/src/fastmcp/server/low_level.py`
- HTTP runtime: `fastmcp-main/src/fastmcp/server/http.py`
- Lifespan: `fastmcp-main/src/fastmcp/server/lifespan.py`

## Core Components Model

FastMCP server behavior centers around four MCP component classes:

1. Tools: executable operations.
2. Resources: read-only data endpoints.
3. Resource templates: parameterized resources.
4. Prompts: reusable message templates.

When extending behavior, check all affected component types, not only tools.

## Recommended Build Sequence (Server)

1. Define server object (`FastMCP(...)`).
2. Add tools/resources/prompts via decorators or provider registration.
3. Add transforms and middleware deliberately.
4. Add auth only if transport and deployment need it.
5. Select transport (`stdio` for local, `http` for remote).
6. Add tests for expected MCP behavior.

## Transport Decision

- Use `stdio` for local editor-driven usage and simple subprocess launching.
- Use `http` for hosted/shared services and authenticated remote clients.
- Use `sse` only when target clients specifically require it.

## Middleware Checklist

Modules:

- `server/middleware/error_handling.py`
- `server/middleware/logging.py`
- `server/middleware/caching.py`
- `server/middleware/rate_limiting.py`
- `server/middleware/authorization.py`
- `server/middleware/response_limiting.py`

Apply middleware in explicit order. Verify side effects with tests in `tests/server`.

## Example Paths To Reuse

- Minimal server: `fastmcp-main/examples/simple_echo.py`
- Config-backed server: `fastmcp-main/examples/config_server.py`
- Mounting/composition: `fastmcp-main/examples/mount_example.py`
- Tags/visibility: `fastmcp-main/examples/tags_example.py`
- Versioning: `fastmcp-main/examples/versioning`

## Tests That Define Expected Behavior

- `fastmcp-main/tests/server/test_providers.py`
- `fastmcp-main/tests/server/test_dependencies.py`
- `fastmcp-main/tests/server/test_pagination.py`
- `fastmcp-main/tests/server/test_logging.py`
- `fastmcp-main/tests/server/tasks`
- `fastmcp-main/tests/server/auth`
