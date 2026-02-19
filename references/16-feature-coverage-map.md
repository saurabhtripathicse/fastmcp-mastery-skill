# FastMCP Feature Coverage Map

Use this checklist when validating whether the skill covers the major FastMCP feature menu.

## Coverage Matrix

| Feature | Docs paths | Source paths | Example paths | Test paths |
|---|---|---|---|---|
| Transports | `clients/transports.md` | `src/fastmcp/client/transports` | `examples/in_memory_proxy_example.py` | `tests/client/transports/test_transports.py` |
| CLI | `clients/cli.md`, `patterns/cli.md` | `src/fastmcp/cli/cli.py`, `src/fastmcp/cli/run.py` | `examples/simple_echo.py` | `tests/cli/test_cli.py` |
| Generate CLI | `clients/generate-cli.md`, `patterns/cli.md` | `src/fastmcp/cli/generate.py` | `examples/simple_echo.py` | `tests/cli/test_generate_cli.py` |
| Tools | `servers/tools.md`, `clients/tools.md` | `src/fastmcp/server/server.py`, `src/fastmcp/client/mixins/tools.py` | `examples/simple_echo.py` | `tests/server/test_tool_annotations.py` |
| Resources | `servers/resources.md`, `clients/resources.md` | `src/fastmcp/server/server.py`, `src/fastmcp/client/mixins/resources.py` | `examples/resources_as_tools/server.py` | `tests/server/mount/test_resources.py` |
| Prompts | `servers/prompts.md`, `clients/prompts.md` | `src/fastmcp/server/server.py`, `src/fastmcp/client/mixins/prompts.py` | `examples/prompts_as_tools/server.py` | `tests/server/mount/test_prompts.py` |
| Notifications | `clients/notifications.md` | `src/fastmcp/server/tasks/notifications.py`, `src/fastmcp/client/client.py` | `examples/tasks/client.py` | `tests/client/test_notifications.py` |
| Sampling | `servers/sampling.md`, `clients/sampling.md` | `src/fastmcp/client/sampling`, `src/fastmcp/server/server.py` | `examples/sampling/text.py` | `tests/client/test_sampling.py` |
| Elicitation | `servers/elicitation.md`, `clients/elicitation.md` | `src/fastmcp/server/tasks/elicitation.py`, `src/fastmcp/client/elicitation.py` | `examples/elicitation.py` | `tests/client/test_elicitation.py` |
| Tasks | `servers/tasks.md`, `clients/tasks.md` | `src/fastmcp/server/tasks`, `src/fastmcp/client/tasks.py` | `examples/tasks/server.py`, `examples/tasks/client.py` | `tests/server/tasks/test_task_protocol.py` |
| Progress | `servers/progress.md`, `clients/progress.md` | `src/fastmcp/server/tasks/notifications.py`, `src/fastmcp/client/progress.py` | `examples/tasks/server.py` | `tests/client/test_progress.py` |
| Logging | `servers/logging.md`, `clients/logging.md` | `src/fastmcp/server/middleware/logging.py`, `src/fastmcp/client/logging.py` | `examples/tasks/server.py` | `tests/server/test_logging.py` |
| Roots | `clients/roots.md` | `src/fastmcp/client/roots.py` | `examples/skills/client.py` | `tests/client/test_roots.py` |
| Authentication | `servers/auth/authentication.md`, `servers/authorization.md` | `src/fastmcp/server/auth/auth.py`, `src/fastmcp/server/auth/authorization.py` | `examples/auth/github_oauth/server.py` | `tests/server/auth/test_auth_provider.py` |
| OAuth | `clients/auth/oauth.md`, `servers/auth/oauth-proxy.md` | `src/fastmcp/client/auth/oauth.py`, `src/fastmcp/server/auth/oauth_proxy/proxy.py` | `examples/auth/google_oauth/client.py` | `tests/client/auth/test_oauth_client.py` |
| CIMD | `clients/auth/cimd.md`, `servers/auth/oidc-proxy.md` | `src/fastmcp/server/auth/cimd.py`, `src/fastmcp/cli/cimd.py` | `examples/auth/google_oauth/client.py` | `tests/server/auth/test_cimd.py`, `tests/cli/test_cimd_cli.py` |
| Bearer Auth | `clients/auth/bearer.md` | `src/fastmcp/client/auth/bearer.py` | `examples/text_me.py` | `tests/server/http/test_bearer_auth_backend.py` |

## Verification Rule

For any feature request, reference at least:

- one docs page,
- one source file,
- one runnable example (if available),
- one test file.
