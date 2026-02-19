# Super-Big Source Reverse Index (Generated)

Generated at: `2026-02-19 20:23:15Z`

## Summary

| Top subsystem | Files | Files with SDK page |
|---|---:|---:|
| `server` | 107 | 105 |
| `utilities` | 36 | 36 |
| `client` | 30 | 30 |
| `cli` | 19 | 18 |
| `contrib` | 9 | 0 |
| `experimental` | 5 | 0 |
| `resources` | 5 | 5 |
| `tools` | 5 | 5 |
| `prompts` | 3 | 3 |
| `_vendor` | 2 | 0 |
| `__init__.py` | 1 | 0 |
| `decorators.py` | 1 | 1 |
| `dependencies.py` | 1 | 1 |
| `exceptions.py` | 1 | 1 |
| `mcp_config.py` | 1 | 1 |
| `settings.py` | 1 | 1 |
| `telemetry.py` | 1 | 1 |

## Table of Contents

- [server (107)](#server)
- [utilities (36)](#utilities)
- [client (30)](#client)
- [cli (19)](#cli)
- [contrib (9)](#contrib)
- [experimental (5)](#experimental)
- [resources (5)](#resources)
- [tools (5)](#tools)
- [prompts (3)](#prompts)
- [_vendor (2)](#_vendor)
- [__init__.py (1)](#__init__.py)
- [decorators.py (1)](#decorators.py)
- [dependencies.py (1)](#dependencies.py)
- [exceptions.py (1)](#exceptions.py)
- [mcp_config.py (1)](#mcp_config.py)
- [settings.py (1)](#settings.py)
- [telemetry.py (1)](#telemetry.py)

## server

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/server/__init__.py` | 6 | python-sdk/fastmcp-server-__init__.md |
| `src/fastmcp/server/apps.py` | 142 | python-sdk/fastmcp-server-apps.md |
| `src/fastmcp/server/auth/__init__.py` | 37 | python-sdk/fastmcp-server-auth-__init__.md |
| `src/fastmcp/server/auth/auth.py` | 675 | python-sdk/fastmcp-server-auth-auth.md |
| `src/fastmcp/server/auth/authorization.py` | 182 | python-sdk/fastmcp-server-auth-authorization.md |
| `src/fastmcp/server/auth/cimd.py` | 799 | python-sdk/fastmcp-server-auth-cimd.md |
| `src/fastmcp/server/auth/handlers/authorize.py` | 326 |  |
| `src/fastmcp/server/auth/jwt_issuer.py` | 246 | python-sdk/fastmcp-server-auth-jwt_issuer.md |
| `src/fastmcp/server/auth/middleware.py` | 96 | python-sdk/fastmcp-server-auth-middleware.md |
| `src/fastmcp/server/auth/oauth_proxy/__init__.py` | 14 | python-sdk/fastmcp-server-auth-oauth_proxy-__init__.md |
| `src/fastmcp/server/auth/oauth_proxy/consent.py` | 478 | python-sdk/fastmcp-server-auth-oauth_proxy-consent.md |
| `src/fastmcp/server/auth/oauth_proxy/models.py` | 252 | python-sdk/fastmcp-server-auth-oauth_proxy-models.md |
| `src/fastmcp/server/auth/oauth_proxy/proxy.py` | 1796 | python-sdk/fastmcp-server-auth-oauth_proxy-proxy.md |
| `src/fastmcp/server/auth/oauth_proxy/ui.py` | 309 | python-sdk/fastmcp-server-auth-oauth_proxy-ui.md |
| `src/fastmcp/server/auth/oidc_proxy.py` | 425 | python-sdk/fastmcp-server-auth-oidc_proxy.md |
| `src/fastmcp/server/auth/providers/__init__.py` | 0 | python-sdk/fastmcp-server-auth-providers-__init__.md |
| `src/fastmcp/server/auth/providers/auth0.py` | 123 | python-sdk/fastmcp-server-auth-providers-auth0.md |
| `src/fastmcp/server/auth/providers/aws.py` | 194 | python-sdk/fastmcp-server-auth-providers-aws.md |
| `src/fastmcp/server/auth/providers/azure.py` | 722 | python-sdk/fastmcp-server-auth-providers-azure.md |
| `src/fastmcp/server/auth/providers/debug.py` | 114 | python-sdk/fastmcp-server-auth-providers-debug.md |
| `src/fastmcp/server/auth/providers/descope.py` | 198 | python-sdk/fastmcp-server-auth-providers-descope.md |
| `src/fastmcp/server/auth/providers/discord.py` | 247 | python-sdk/fastmcp-server-auth-providers-discord.md |
| `src/fastmcp/server/auth/providers/github.py` | 240 | python-sdk/fastmcp-server-auth-providers-github.md |
| `src/fastmcp/server/auth/providers/google.py` | 278 | python-sdk/fastmcp-server-auth-providers-google.md |
| `src/fastmcp/server/auth/providers/in_memory.py` | 364 | python-sdk/fastmcp-server-auth-providers-in_memory.md |
| `src/fastmcp/server/auth/providers/introspection.py` | 262 | python-sdk/fastmcp-server-auth-providers-introspection.md |
| `src/fastmcp/server/auth/providers/jwt.py` | 550 | python-sdk/fastmcp-server-auth-providers-jwt.md |
| `src/fastmcp/server/auth/providers/oci.py` | 170 | python-sdk/fastmcp-server-auth-providers-oci.md |
| `src/fastmcp/server/auth/providers/scalekit.py` | 201 | python-sdk/fastmcp-server-auth-providers-scalekit.md |
| `src/fastmcp/server/auth/providers/supabase.py` | 170 | python-sdk/fastmcp-server-auth-providers-supabase.md |
| `src/fastmcp/server/auth/providers/workos.py` | 345 | python-sdk/fastmcp-server-auth-providers-workos.md |
| `src/fastmcp/server/auth/redirect_validation.py` | 212 | python-sdk/fastmcp-server-auth-redirect_validation.md |
| `src/fastmcp/server/auth/ssrf.py` | 356 | python-sdk/fastmcp-server-auth-ssrf.md |
| `src/fastmcp/server/context.py` | 1359 | python-sdk/fastmcp-server-context.md |
| `src/fastmcp/server/dependencies.py` | 1309 | python-sdk/fastmcp-server-dependencies.md |
| `src/fastmcp/server/elicitation.py` | 464 | python-sdk/fastmcp-server-elicitation.md |
| `src/fastmcp/server/event_store.py` | 177 | python-sdk/fastmcp-server-event_store.md |
| `src/fastmcp/server/http.py` | 383 | python-sdk/fastmcp-server-http.md |
| `src/fastmcp/server/lifespan.py` | 198 | python-sdk/fastmcp-server-lifespan.md |
| `src/fastmcp/server/low_level.py` | 344 | python-sdk/fastmcp-server-low_level.md |
| `src/fastmcp/server/middleware/__init__.py` | 15 | python-sdk/fastmcp-server-middleware-__init__.md |
| `src/fastmcp/server/middleware/authorization.py` | 309 | python-sdk/fastmcp-server-middleware-authorization.md |
| `src/fastmcp/server/middleware/caching.py` | 521 | python-sdk/fastmcp-server-middleware-caching.md |
| `src/fastmcp/server/middleware/dereference.py` | 78 | python-sdk/fastmcp-server-middleware-dereference.md |
| `src/fastmcp/server/middleware/error_handling.py` | 216 | python-sdk/fastmcp-server-middleware-error_handling.md |
| `src/fastmcp/server/middleware/logging.py` | 256 | python-sdk/fastmcp-server-middleware-logging.md |
| `src/fastmcp/server/middleware/middleware.py` | 205 | python-sdk/fastmcp-server-middleware-middleware.md |
| `src/fastmcp/server/middleware/ping.py` | 70 | python-sdk/fastmcp-server-middleware-ping.md |
| `src/fastmcp/server/middleware/rate_limiting.py` | 231 | python-sdk/fastmcp-server-middleware-rate_limiting.md |
| `src/fastmcp/server/middleware/response_limiting.py` | 125 | python-sdk/fastmcp-server-middleware-response_limiting.md |
| `src/fastmcp/server/middleware/timing.py` | 156 | python-sdk/fastmcp-server-middleware-timing.md |
| `src/fastmcp/server/middleware/tool_injection.py` | 116 | python-sdk/fastmcp-server-middleware-tool_injection.md |
| `src/fastmcp/server/mixins/__init__.py` | 7 | python-sdk/fastmcp-server-mixins-__init__.md |
| `src/fastmcp/server/mixins/lifespan.py` | 217 | python-sdk/fastmcp-server-mixins-lifespan.md |
| `src/fastmcp/server/mixins/mcp_operations.py` | 400 | python-sdk/fastmcp-server-mixins-mcp_operations.md |
| `src/fastmcp/server/mixins/transport.py` | 339 | python-sdk/fastmcp-server-mixins-transport.md |
| `src/fastmcp/server/openapi/__init__.py` | 55 | python-sdk/fastmcp-server-openapi-__init__.md |
| `src/fastmcp/server/openapi/components.py` | 28 | python-sdk/fastmcp-server-openapi-components.md |
| `src/fastmcp/server/openapi/routing.py` | 46 | python-sdk/fastmcp-server-openapi-routing.md |
| `src/fastmcp/server/openapi/server.py` | 124 | python-sdk/fastmcp-server-openapi-server.md |
| `src/fastmcp/server/providers/__init__.py` | 71 | python-sdk/fastmcp-server-providers-__init__.md |
| `src/fastmcp/server/providers/aggregate.py` | 261 | python-sdk/fastmcp-server-providers-aggregate.md |
| `src/fastmcp/server/providers/base.py` | 578 | python-sdk/fastmcp-server-providers-base.md |
| `src/fastmcp/server/providers/fastmcp_provider.py` | 686 | python-sdk/fastmcp-server-providers-fastmcp_provider.md |
| `src/fastmcp/server/providers/filesystem.py` | 226 | python-sdk/fastmcp-server-providers-filesystem.md |
| `src/fastmcp/server/providers/filesystem_discovery.py` | 327 | python-sdk/fastmcp-server-providers-filesystem_discovery.md |
| `src/fastmcp/server/providers/local_provider/__init__.py` | 11 | python-sdk/fastmcp-server-providers-local_provider-__init__.md |
| `src/fastmcp/server/providers/local_provider/decorators/__init__.py` | 15 | python-sdk/fastmcp-server-providers-local_provider-decorators-__init__.md |
| `src/fastmcp/server/providers/local_provider/decorators/prompts.py` | 256 | python-sdk/fastmcp-server-providers-local_provider-decorators-prompts.md |
| `src/fastmcp/server/providers/local_provider/decorators/resources.py` | 240 | python-sdk/fastmcp-server-providers-local_provider-decorators-resources.md |
| `src/fastmcp/server/providers/local_provider/decorators/tools.py` | 328 | python-sdk/fastmcp-server-providers-local_provider-decorators-tools.md |
| `src/fastmcp/server/providers/local_provider/local_provider.py` | 465 | python-sdk/fastmcp-server-providers-local_provider-local_provider.md |
| `src/fastmcp/server/providers/openapi/__init__.py` | 39 | python-sdk/fastmcp-server-providers-openapi-__init__.md |
| `src/fastmcp/server/providers/openapi/components.py` | 397 | python-sdk/fastmcp-server-providers-openapi-components.md |
| `src/fastmcp/server/providers/openapi/provider.py` | 433 | python-sdk/fastmcp-server-providers-openapi-provider.md |
| `src/fastmcp/server/providers/openapi/routing.py` | 109 | python-sdk/fastmcp-server-providers-openapi-routing.md |
| `src/fastmcp/server/providers/proxy.py` | 938 | python-sdk/fastmcp-server-providers-proxy.md |
| `src/fastmcp/server/providers/skills/__init__.py` | 59 | python-sdk/fastmcp-server-providers-skills-__init__.md |
| `src/fastmcp/server/providers/skills/_common.py` | 101 |  |
| `src/fastmcp/server/providers/skills/claude_provider.py` | 44 | python-sdk/fastmcp-server-providers-skills-claude_provider.md |
| `src/fastmcp/server/providers/skills/directory_provider.py` | 153 | python-sdk/fastmcp-server-providers-skills-directory_provider.md |
| `src/fastmcp/server/providers/skills/skill_provider.py` | 449 | python-sdk/fastmcp-server-providers-skills-skill_provider.md |
| `src/fastmcp/server/providers/skills/vendor_providers.py` | 142 | python-sdk/fastmcp-server-providers-skills-vendor_providers.md |
| `src/fastmcp/server/providers/wrapped_provider.py` | 140 | python-sdk/fastmcp-server-providers-wrapped_provider.md |
| `src/fastmcp/server/proxy.py` | 41 | python-sdk/fastmcp-server-proxy.md |
| `src/fastmcp/server/sampling/__init__.py` | 10 | python-sdk/fastmcp-server-sampling-__init__.md |
| `src/fastmcp/server/sampling/run.py` | 701 | python-sdk/fastmcp-server-sampling-run.md |
| `src/fastmcp/server/sampling/sampling_tool.py` | 183 | python-sdk/fastmcp-server-sampling-sampling_tool.md |
| `src/fastmcp/server/server.py` | 2131 | python-sdk/fastmcp-server-server.md |
| `src/fastmcp/server/tasks/__init__.py` | 38 | python-sdk/fastmcp-server-tasks-__init__.md |
| `src/fastmcp/server/tasks/capabilities.py` | 42 | python-sdk/fastmcp-server-tasks-capabilities.md |
| `src/fastmcp/server/tasks/config.py` | 140 | python-sdk/fastmcp-server-tasks-config.md |
| `src/fastmcp/server/tasks/elicitation.py` | 346 | python-sdk/fastmcp-server-tasks-elicitation.md |
| `src/fastmcp/server/tasks/handlers.py` | 217 | python-sdk/fastmcp-server-tasks-handlers.md |
| `src/fastmcp/server/tasks/keys.py` | 91 | python-sdk/fastmcp-server-tasks-keys.md |
| `src/fastmcp/server/tasks/notifications.py` | 300 | python-sdk/fastmcp-server-tasks-notifications.md |
| `src/fastmcp/server/tasks/requests.py` | 474 | python-sdk/fastmcp-server-tasks-requests.md |
| `src/fastmcp/server/tasks/routing.py` | 76 | python-sdk/fastmcp-server-tasks-routing.md |
| `src/fastmcp/server/tasks/subscriptions.py` | 212 | python-sdk/fastmcp-server-tasks-subscriptions.md |
| `src/fastmcp/server/telemetry.py` | 131 | python-sdk/fastmcp-server-telemetry.md |
| `src/fastmcp/server/transforms/__init__.py` | 244 | python-sdk/fastmcp-server-transforms-__init__.md |
| `src/fastmcp/server/transforms/namespace.py` | 193 | python-sdk/fastmcp-server-transforms-namespace.md |
| `src/fastmcp/server/transforms/prompts_as_tools.py` | 175 | python-sdk/fastmcp-server-transforms-prompts_as_tools.md |
| `src/fastmcp/server/transforms/resources_as_tools.py` | 190 | python-sdk/fastmcp-server-transforms-resources_as_tools.md |
| `src/fastmcp/server/transforms/tool_transform.py` | 96 | python-sdk/fastmcp-server-transforms-tool_transform.md |
| `src/fastmcp/server/transforms/version_filter.py` | 124 | python-sdk/fastmcp-server-transforms-version_filter.md |
| `src/fastmcp/server/transforms/visibility.py` | 526 | python-sdk/fastmcp-server-transforms-visibility.md |

## utilities

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/utilities/__init__.py` | 1 | python-sdk/fastmcp-utilities-__init__.md |
| `src/fastmcp/utilities/async_utils.py` | 69 | python-sdk/fastmcp-utilities-async_utils.md |
| `src/fastmcp/utilities/auth.py` | 91 | python-sdk/fastmcp-utilities-auth.md |
| `src/fastmcp/utilities/cli.py` | 269 | python-sdk/fastmcp-utilities-cli.md |
| `src/fastmcp/utilities/components.py` | 242 | python-sdk/fastmcp-utilities-components.md |
| `src/fastmcp/utilities/exceptions.py` | 49 | python-sdk/fastmcp-utilities-exceptions.md |
| `src/fastmcp/utilities/http.py` | 8 | python-sdk/fastmcp-utilities-http.md |
| `src/fastmcp/utilities/inspect.py` | 494 | python-sdk/fastmcp-utilities-inspect.md |
| `src/fastmcp/utilities/json_schema.py` | 404 | python-sdk/fastmcp-utilities-json_schema.md |
| `src/fastmcp/utilities/json_schema_type.py` | 650 | python-sdk/fastmcp-utilities-json_schema_type.md |
| `src/fastmcp/utilities/lifespan.py` | 56 | python-sdk/fastmcp-utilities-lifespan.md |
| `src/fastmcp/utilities/logging.py` | 238 | python-sdk/fastmcp-utilities-logging.md |
| `src/fastmcp/utilities/mcp_server_config/__init__.py` | 25 | python-sdk/fastmcp-utilities-mcp_server_config-__init__.md |
| `src/fastmcp/utilities/mcp_server_config/v1/__init__.py` | 0 | python-sdk/fastmcp-utilities-mcp_server_config-v1-__init__.md |
| `src/fastmcp/utilities/mcp_server_config/v1/environments/__init__.py` | 6 | python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-__init__.md |
| `src/fastmcp/utilities/mcp_server_config/v1/environments/base.py` | 29 | python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-base.md |
| `src/fastmcp/utilities/mcp_server_config/v1/environments/uv.py` | 271 | python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-uv.md |
| `src/fastmcp/utilities/mcp_server_config/v1/mcp_server_config.py` | 447 | python-sdk/fastmcp-utilities-mcp_server_config-v1-mcp_server_config.md |
| `src/fastmcp/utilities/mcp_server_config/v1/sources/__init__.py` | 0 | python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-__init__.md |
| `src/fastmcp/utilities/mcp_server_config/v1/sources/base.py` | 29 | python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-base.md |
| `src/fastmcp/utilities/mcp_server_config/v1/sources/filesystem.py` | 216 | python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-filesystem.md |
| `src/fastmcp/utilities/openapi/__init__.py` | 61 | python-sdk/fastmcp-utilities-openapi-__init__.md |
| `src/fastmcp/utilities/openapi/director.py` | 220 | python-sdk/fastmcp-utilities-openapi-director.md |
| `src/fastmcp/utilities/openapi/formatters.py` | 355 | python-sdk/fastmcp-utilities-openapi-formatters.md |
| `src/fastmcp/utilities/openapi/json_schema_converter.py` | 344 | python-sdk/fastmcp-utilities-openapi-json_schema_converter.md |
| `src/fastmcp/utilities/openapi/models.py` | 88 | python-sdk/fastmcp-utilities-openapi-models.md |
| `src/fastmcp/utilities/openapi/parser.py` | 825 | python-sdk/fastmcp-utilities-openapi-parser.md |
| `src/fastmcp/utilities/openapi/schemas.py` | 593 | python-sdk/fastmcp-utilities-openapi-schemas.md |
| `src/fastmcp/utilities/pagination.py` | 80 | python-sdk/fastmcp-utilities-pagination.md |
| `src/fastmcp/utilities/skills.py` | 253 | python-sdk/fastmcp-utilities-skills.md |
| `src/fastmcp/utilities/tests.py` | 270 | python-sdk/fastmcp-utilities-tests.md |
| `src/fastmcp/utilities/timeout.py` | 47 | python-sdk/fastmcp-utilities-timeout.md |
| `src/fastmcp/utilities/types.py` | 496 | python-sdk/fastmcp-utilities-types.md |
| `src/fastmcp/utilities/ui.py` | 626 | python-sdk/fastmcp-utilities-ui.md |
| `src/fastmcp/utilities/version_check.py` | 153 | python-sdk/fastmcp-utilities-version_check.md |
| `src/fastmcp/utilities/versions.py` | 285 | python-sdk/fastmcp-utilities-versions.md |

## client

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/client/__init__.py` | 30 | python-sdk/fastmcp-client-__init__.md |
| `src/fastmcp/client/auth/__init__.py` | 4 | python-sdk/fastmcp-client-auth-__init__.md |
| `src/fastmcp/client/auth/bearer.py` | 17 | python-sdk/fastmcp-client-auth-bearer.md |
| `src/fastmcp/client/auth/oauth.py` | 400 | python-sdk/fastmcp-client-auth-oauth.md |
| `src/fastmcp/client/client.py` | 848 | python-sdk/fastmcp-client-client.md |
| `src/fastmcp/client/elicitation.py` | 80 | python-sdk/fastmcp-client-elicitation.md |
| `src/fastmcp/client/logging.py` | 54 | python-sdk/fastmcp-client-logging.md |
| `src/fastmcp/client/messages.py` | 128 | python-sdk/fastmcp-client-messages.md |
| `src/fastmcp/client/mixins/__init__.py` | 13 | python-sdk/fastmcp-client-mixins-__init__.md |
| `src/fastmcp/client/mixins/prompts.py` | 303 | python-sdk/fastmcp-client-mixins-prompts.md |
| `src/fastmcp/client/mixins/resources.py` | 342 | python-sdk/fastmcp-client-mixins-resources.md |
| `src/fastmcp/client/mixins/task_management.py` | 157 | python-sdk/fastmcp-client-mixins-task_management.md |
| `src/fastmcp/client/mixins/tools.py` | 405 | python-sdk/fastmcp-client-mixins-tools.md |
| `src/fastmcp/client/oauth_callback.py` | 242 | python-sdk/fastmcp-client-oauth_callback.md |
| `src/fastmcp/client/progress.py` | 38 | python-sdk/fastmcp-client-progress.md |
| `src/fastmcp/client/roots.py` | 76 | python-sdk/fastmcp-client-roots.md |
| `src/fastmcp/client/sampling/__init__.py` | 69 | python-sdk/fastmcp-client-sampling-__init__.md |
| `src/fastmcp/client/sampling/handlers/__init__.py` | 0 | python-sdk/fastmcp-client-sampling-handlers-__init__.md |
| `src/fastmcp/client/sampling/handlers/anthropic.py` | 389 | python-sdk/fastmcp-client-sampling-handlers-anthropic.md |
| `src/fastmcp/client/sampling/handlers/openai.py` | 405 | python-sdk/fastmcp-client-sampling-handlers-openai.md |
| `src/fastmcp/client/tasks.py` | 551 | python-sdk/fastmcp-client-tasks.md |
| `src/fastmcp/client/telemetry.py` | 47 | python-sdk/fastmcp-client-telemetry.md |
| `src/fastmcp/client/transports/__init__.py` | 38 | python-sdk/fastmcp-client-transports-__init__.md |
| `src/fastmcp/client/transports/base.py` | 82 | python-sdk/fastmcp-client-transports-base.md |
| `src/fastmcp/client/transports/config.py` | 170 | python-sdk/fastmcp-client-transports-config.md |
| `src/fastmcp/client/transports/http.py` | 151 | python-sdk/fastmcp-client-transports-http.md |
| `src/fastmcp/client/transports/inference.py` | 154 | python-sdk/fastmcp-client-transports-inference.md |
| `src/fastmcp/client/transports/memory.py` | 90 | python-sdk/fastmcp-client-transports-memory.md |
| `src/fastmcp/client/transports/sse.py` | 95 | python-sdk/fastmcp-client-transports-sse.md |
| `src/fastmcp/client/transports/stdio.py` | 543 | python-sdk/fastmcp-client-transports-stdio.md |

## cli

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/cli/__init__.py` | 3 | python-sdk/fastmcp-cli-__init__.md |
| `src/fastmcp/cli/__main__.py` | 5 |  |
| `src/fastmcp/cli/auth.py` | 13 | python-sdk/fastmcp-cli-auth.md |
| `src/fastmcp/cli/cimd.py` | 218 | python-sdk/fastmcp-cli-cimd.md |
| `src/fastmcp/cli/cli.py` | 976 | python-sdk/fastmcp-cli-cli.md |
| `src/fastmcp/cli/client.py` | 966 | python-sdk/fastmcp-cli-client.md |
| `src/fastmcp/cli/discovery.py` | 375 | python-sdk/fastmcp-cli-discovery.md |
| `src/fastmcp/cli/generate.py` | 808 | python-sdk/fastmcp-cli-generate.md |
| `src/fastmcp/cli/install/__init__.py` | 26 | python-sdk/fastmcp-cli-install-__init__.md |
| `src/fastmcp/cli/install/claude_code.py` | 240 | python-sdk/fastmcp-cli-install-claude_code.md |
| `src/fastmcp/cli/install/claude_desktop.py` | 210 | python-sdk/fastmcp-cli-install-claude_desktop.md |
| `src/fastmcp/cli/install/cursor.py` | 318 | python-sdk/fastmcp-cli-install-cursor.md |
| `src/fastmcp/cli/install/gemini_cli.py` | 237 | python-sdk/fastmcp-cli-install-gemini_cli.md |
| `src/fastmcp/cli/install/goose.py` | 209 | python-sdk/fastmcp-cli-install-goose.md |
| `src/fastmcp/cli/install/mcp_json.py` | 191 | python-sdk/fastmcp-cli-install-mcp_json.md |
| `src/fastmcp/cli/install/shared.py` | 174 | python-sdk/fastmcp-cli-install-shared.md |
| `src/fastmcp/cli/install/stdio.py` | 156 | python-sdk/fastmcp-cli-install-stdio.md |
| `src/fastmcp/cli/run.py` | 444 | python-sdk/fastmcp-cli-run.md |
| `src/fastmcp/cli/tasks.py` | 110 | python-sdk/fastmcp-cli-tasks.md |

## contrib

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/contrib/bulk_tool_caller/__init__.py` | 3 |  |
| `src/fastmcp/contrib/bulk_tool_caller/bulk_tool_caller.py` | 133 |  |
| `src/fastmcp/contrib/bulk_tool_caller/example.py` | 17 |  |
| `src/fastmcp/contrib/component_manager/__init__.py` | 3 |  |
| `src/fastmcp/contrib/component_manager/component_manager.py` | 121 |  |
| `src/fastmcp/contrib/component_manager/example.py` | 59 |  |
| `src/fastmcp/contrib/mcp_mixin/__init__.py` | 8 |  |
| `src/fastmcp/contrib/mcp_mixin/example.py` | 52 |  |
| `src/fastmcp/contrib/mcp_mixin/mcp_mixin.py` | 283 |  |

## experimental

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/experimental/sampling/__init__.py` | 0 |  |
| `src/fastmcp/experimental/sampling/handlers/__init__.py` | 5 |  |
| `src/fastmcp/experimental/sampling/handlers/openai.py` | 5 |  |
| `src/fastmcp/experimental/server/openapi/__init__.py` | 40 |  |
| `src/fastmcp/experimental/utilities/openapi/__init__.py` | 35 |  |

## resources

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/resources/__init__.py` | 24 | python-sdk/fastmcp-resources-__init__.md |
| `src/fastmcp/resources/function_resource.py` | 340 | python-sdk/fastmcp-resources-function_resource.md |
| `src/fastmcp/resources/resource.py` | 466 | python-sdk/fastmcp-resources-resource.md |
| `src/fastmcp/resources/template.py` | 590 | python-sdk/fastmcp-resources-template.md |
| `src/fastmcp/resources/types.py` | 172 | python-sdk/fastmcp-resources-types.md |

## tools

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/tools/__init__.py` | 12 | python-sdk/fastmcp-tools-__init__.md |
| `src/fastmcp/tools/function_parsing.py` | 201 | python-sdk/fastmcp-tools-function_parsing.md |
| `src/fastmcp/tools/function_tool.py` | 469 | python-sdk/fastmcp-tools-function_tool.md |
| `src/fastmcp/tools/tool.py` | 511 | python-sdk/fastmcp-tools-tool.md |
| `src/fastmcp/tools/tool_transform.py` | 1001 | python-sdk/fastmcp-tools-tool_transform.md |

## prompts

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/prompts/__init__.py` | 12 | python-sdk/fastmcp-prompts-__init__.md |
| `src/fastmcp/prompts/function_prompt.py` | 480 | python-sdk/fastmcp-prompts-function_prompt.md |
| `src/fastmcp/prompts/prompt.py` | 432 | python-sdk/fastmcp-prompts-prompt.md |

## _vendor

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/_vendor/__init__.py` | 1 |  |
| `src/fastmcp/_vendor/docket_di/__init__.py` | 163 |  |

## __init__.py

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/__init__.py` | 35 |  |

## decorators.py

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/decorators.py` | 41 | python-sdk/fastmcp-decorators.md |

## dependencies.py

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/dependencies.py` | 44 | python-sdk/fastmcp-dependencies.md |

## exceptions.py

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/exceptions.py` | 43 | python-sdk/fastmcp-exceptions.md |

## mcp_config.py

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/mcp_config.py` | 371 | python-sdk/fastmcp-mcp_config.md |

## settings.py

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/settings.py` | 338 | python-sdk/fastmcp-settings.md |

## telemetry.py

| Source module | Lines | Linked SDK pages |
|---|---:|---|
| `src/fastmcp/telemetry.py` | 122 | python-sdk/fastmcp-telemetry.md |

