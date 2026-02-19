# Super-Big Python SDK Index (Generated)

Generated at: `2026-02-19 19:44:34Z`

## Summary

| Group | Files | Total functions | Total classes |
|---|---:|---:|---:|
| `server` | 105 | 108 | 178 |
| `utilities` | 36 | 69 | 33 |
| `client` | 30 | 12 | 35 |
| `cli` | 18 | 56 | 1 |
| `resources` | 5 | 4 | 13 |
| `tools` | 5 | 5 | 10 |
| `prompts` | 3 | 1 | 7 |
| `decorators` | 1 | 2 | 1 |
| `dependencies` | 1 | 0 | 0 |
| `exceptions` | 1 | 0 | 10 |
| `mcp_config` | 1 | 2 | 6 |
| `settings` | 1 | 0 | 2 |
| `telemetry` | 1 | 4 | 0 |

## Table of Contents

- [server (105)](#server)
- [utilities (36)](#utilities)
- [client (30)](#client)
- [cli (18)](#cli)
- [resources (5)](#resources)
- [tools (5)](#tools)
- [prompts (3)](#prompts)
- [decorators (1)](#decorators)
- [dependencies (1)](#dependencies)
- [exceptions (1)](#exceptions)
- [mcp_config (1)](#mcp_config)
- [settings (1)](#settings)
- [telemetry (1)](#telemetry)

## server

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-server-__init__.md` | `fastmcp.server` | `src/fastmcp/server/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-apps.md` | `fastmcp.server.apps` | `src/fastmcp/server/apps.py` | `fastmcp/server/apps.py` | 2 | 3 | app_config_to_meta_dict, resolve_ui_mime_type, ResourceCSP, ResourcePermissions, AppConfig |
| `python-sdk/fastmcp-server-auth-__init__.md` | `fastmcp.server.auth` | `src/fastmcp/server/auth/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-auth-auth.md` | `fastmcp.server.auth.auth` | `src/fastmcp/server/auth/auth.py` | `fastmcp/server/auth/auth.py` | 0 | 7 | AccessToken, TokenHandler, PrivateKeyJWTClientAuthenticator, AuthProvider, TokenVerifier, RemoteAuthProvider |
| `python-sdk/fastmcp-server-auth-authorization.md` | `fastmcp.server.auth.authorization` | `src/fastmcp/server/auth/authorization.py` | `fastmcp/server/auth/authorization.py` | 3 | 1 | require_scopes, restrict_tag, run_auth_checks, AuthContext |
| `python-sdk/fastmcp-server-auth-cimd.md` | `fastmcp.server.auth.cimd` | `src/fastmcp/server/auth/cimd.py` | `fastmcp/server/auth/cimd.py` | 0 | 6 | CIMDDocument, CIMDValidationError, CIMDFetchError, CIMDFetcher, CIMDAssertionValidator, CIMDClientManager |
| `python-sdk/fastmcp-server-auth-jwt_issuer.md` | `fastmcp.server.auth.jwt_issuer` | `src/fastmcp/server/auth/jwt_issuer.py` | `fastmcp/server/auth/jwt_issuer.py` | 1 | 1 | derive_jwt_key, JWTIssuer |
| `python-sdk/fastmcp-server-auth-middleware.md` | `fastmcp.server.auth.middleware` | `src/fastmcp/server/auth/middleware.py` | `fastmcp/server/auth/middleware.py` | 0 | 1 | RequireAuthMiddleware |
| `python-sdk/fastmcp-server-auth-oauth_proxy-__init__.md` | `fastmcp.server.auth.oauth_proxy` | `src/fastmcp/server/auth/oauth_proxy/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-auth-oauth_proxy-consent.md` | `fastmcp.server.auth.oauth_proxy.consent` | `src/fastmcp/server/auth/oauth_proxy/consent.py` | `fastmcp/server/auth/oauth_proxy/consent.py` | 0 | 1 | ConsentMixin |
| `python-sdk/fastmcp-server-auth-oauth_proxy-models.md` | `fastmcp.server.auth.oauth_proxy.models` | `src/fastmcp/server/auth/oauth_proxy/models.py` | `fastmcp/server/auth/oauth_proxy/models.py` | 0 | 6 | OAuthTransaction, ClientCode, UpstreamTokenSet, JTIMapping, RefreshTokenMetadata, ProxyDCRClient |
| `python-sdk/fastmcp-server-auth-oauth_proxy-proxy.md` | `fastmcp.server.auth.oauth_proxy.proxy` | `src/fastmcp/server/auth/oauth_proxy/proxy.py` | `fastmcp/server/auth/oauth_proxy/proxy.py` | 0 | 1 | OAuthProxy |
| `python-sdk/fastmcp-server-auth-oauth_proxy-ui.md` | `fastmcp.server.auth.oauth_proxy.ui` | `src/fastmcp/server/auth/oauth_proxy/ui.py` | `fastmcp/server/auth/oauth_proxy/ui.py` | 2 | 0 | create_consent_html, create_error_html |
| `python-sdk/fastmcp-server-auth-oidc_proxy.md` | `fastmcp.server.auth.oidc_proxy` | `src/fastmcp/server/auth/oidc_proxy.py` | `fastmcp/server/auth/oidc_proxy.py` | 0 | 2 | OIDCConfiguration, OIDCProxy |
| `python-sdk/fastmcp-server-auth-providers-__init__.md` | `fastmcp.server.auth.providers` | `src/fastmcp/server/auth/providers/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-auth-providers-auth0.md` | `fastmcp.server.auth.providers.auth0` | `src/fastmcp/server/auth/providers/auth0.py` | `fastmcp/server/auth/providers/auth0.py` | 0 | 1 | Auth0Provider |
| `python-sdk/fastmcp-server-auth-providers-aws.md` | `fastmcp.server.auth.providers.aws` | `src/fastmcp/server/auth/providers/aws.py` | `fastmcp/server/auth/providers/aws.py` | 0 | 2 | AWSCognitoTokenVerifier, AWSCognitoProvider |
| `python-sdk/fastmcp-server-auth-providers-azure.md` | `fastmcp.server.auth.providers.azure` | `src/fastmcp/server/auth/providers/azure.py` | `fastmcp/server/auth/providers/azure.py` | 1 | 2 | EntraOBOToken, AzureProvider, AzureJWTVerifier |
| `python-sdk/fastmcp-server-auth-providers-debug.md` | `fastmcp.server.auth.providers.debug` | `src/fastmcp/server/auth/providers/debug.py` | `fastmcp/server/auth/providers/debug.py` | 0 | 1 | DebugTokenVerifier |
| `python-sdk/fastmcp-server-auth-providers-descope.md` | `fastmcp.server.auth.providers.descope` | `src/fastmcp/server/auth/providers/descope.py` | `fastmcp/server/auth/providers/descope.py` | 0 | 1 | DescopeProvider |
| `python-sdk/fastmcp-server-auth-providers-discord.md` | `fastmcp.server.auth.providers.discord` | `src/fastmcp/server/auth/providers/discord.py` | `fastmcp/server/auth/providers/discord.py` | 0 | 2 | DiscordTokenVerifier, DiscordProvider |
| `python-sdk/fastmcp-server-auth-providers-github.md` | `fastmcp.server.auth.providers.github` | `src/fastmcp/server/auth/providers/github.py` | `fastmcp/server/auth/providers/github.py` | 0 | 2 | GitHubTokenVerifier, GitHubProvider |
| `python-sdk/fastmcp-server-auth-providers-google.md` | `fastmcp.server.auth.providers.google` | `src/fastmcp/server/auth/providers/google.py` | `fastmcp/server/auth/providers/google.py` | 0 | 2 | GoogleTokenVerifier, GoogleProvider |
| `python-sdk/fastmcp-server-auth-providers-in_memory.md` | `fastmcp.server.auth.providers.in_memory` | `src/fastmcp/server/auth/providers/in_memory.py` | `fastmcp/server/auth/providers/in_memory.py` | 0 | 1 | InMemoryOAuthProvider |
| `python-sdk/fastmcp-server-auth-providers-introspection.md` | `fastmcp.server.auth.providers.introspection` | `src/fastmcp/server/auth/providers/introspection.py` | `fastmcp/server/auth/providers/introspection.py` | 0 | 1 | IntrospectionTokenVerifier |
| `python-sdk/fastmcp-server-auth-providers-jwt.md` | `fastmcp.server.auth.providers.jwt` | `src/fastmcp/server/auth/providers/jwt.py` | `fastmcp/server/auth/providers/jwt.py` | 0 | 5 | JWKData, JWKSData, RSAKeyPair, JWTVerifier, StaticTokenVerifier |
| `python-sdk/fastmcp-server-auth-providers-oci.md` | `fastmcp.server.auth.providers.oci` | `src/fastmcp/server/auth/providers/oci.py` | `fastmcp/server/auth/providers/oci.py` | 0 | 1 | OCIProvider |
| `python-sdk/fastmcp-server-auth-providers-scalekit.md` | `fastmcp.server.auth.providers.scalekit` | `src/fastmcp/server/auth/providers/scalekit.py` | `fastmcp/server/auth/providers/scalekit.py` | 0 | 1 | ScalekitProvider |
| `python-sdk/fastmcp-server-auth-providers-supabase.md` | `fastmcp.server.auth.providers.supabase` | `src/fastmcp/server/auth/providers/supabase.py` | `fastmcp/server/auth/providers/supabase.py` | 0 | 1 | SupabaseProvider |
| `python-sdk/fastmcp-server-auth-providers-workos.md` | `fastmcp.server.auth.providers.workos` | `src/fastmcp/server/auth/providers/workos.py` | `fastmcp/server/auth/providers/workos.py` | 0 | 3 | WorkOSTokenVerifier, WorkOSProvider, AuthKitProvider |
| `python-sdk/fastmcp-server-auth-redirect_validation.md` | `fastmcp.server.auth.redirect_validation` | `src/fastmcp/server/auth/redirect_validation.py` | `fastmcp/server/auth/redirect_validation.py` | 2 | 0 | matches_allowed_pattern, validate_redirect_uri |
| `python-sdk/fastmcp-server-auth-ssrf.md` | `fastmcp.server.auth.ssrf` | `src/fastmcp/server/auth/ssrf.py` | `fastmcp/server/auth/ssrf.py` | 6 | 4 | format_ip_for_url, is_ip_allowed, resolve_hostname, validate_url, ssrf_safe_fetch, ssrf_safe_fetch_response, SSRFError, SSRFFetchError, ValidatedURL, SSRFFetchResponse |
| `python-sdk/fastmcp-server-context.md` | `fastmcp.server.context` | `src/fastmcp/server/context.py` | `fastmcp/server/context.py` | 3 | 2 | set_transport, reset_transport, set_context, LogData, Context |
| `python-sdk/fastmcp-server-dependencies.md` | `fastmcp.server.dependencies` | `src/fastmcp/server/dependencies.py` | `fastmcp/server/dependencies.py` | 21 | 4 | get_task_context, register_task_session, get_task_session, is_docket_available, require_docket, transform_context_annotations, TaskContextInfo, ProgressLike, InMemoryProgress, Progress |
| `python-sdk/fastmcp-server-elicitation.md` | `fastmcp.server.elicitation` | `src/fastmcp/server/elicitation.py` | `fastmcp/server/elicitation.py` | 4 | 4 | parse_elicit_response_type, handle_elicit_accept, get_elicitation_schema, validate_elicitation_json_schema, ElicitationJsonSchema, AcceptedElicitation, ScalarElicitationType, ElicitConfig |
| `python-sdk/fastmcp-server-event_store.md` | `fastmcp.server.event_store` | `src/fastmcp/server/event_store.py` | `fastmcp/server/event_store.py` | 0 | 3 | EventEntry, StreamEventList, EventStore |
| `python-sdk/fastmcp-server-http.md` | `fastmcp.server.http` | `src/fastmcp/server/http.py` | `fastmcp/server/http.py` | 4 | 3 | set_http_request, create_base_app, create_sse_app, create_streamable_http_app, StreamableHTTPASGIApp, StarletteWithLifespan, RequestContextMiddleware |
| `python-sdk/fastmcp-server-lifespan.md` | `fastmcp.server.lifespan` | `src/fastmcp/server/lifespan.py` | `fastmcp/server/lifespan.py` | 1 | 3 | lifespan, Lifespan, ContextManagerLifespan, ComposedLifespan |
| `python-sdk/fastmcp-server-low_level.md` | `fastmcp.server.low_level` | `src/fastmcp/server/low_level.py` | `fastmcp/server/low_level.py` | 0 | 2 | MiddlewareServerSession, LowLevelServer |
| `python-sdk/fastmcp-server-middleware-__init__.md` | `fastmcp.server.middleware` | `src/fastmcp/server/middleware/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-middleware-authorization.md` | `fastmcp.server.middleware.authorization` | `src/fastmcp/server/middleware/authorization.py` | `fastmcp/server/middleware/authorization.py` | 0 | 1 | AuthMiddleware |
| `python-sdk/fastmcp-server-middleware-caching.md` | `fastmcp.server.middleware.caching` | `src/fastmcp/server/middleware/caching.py` | `fastmcp/server/middleware/caching.py` | 0 | 14 | CachableResourceContent, CachableResourceResult, CachableToolResult, CachableMessage, CachablePromptResult, SharedMethodSettings |
| `python-sdk/fastmcp-server-middleware-dereference.md` | `fastmcp.server.middleware.dereference` | `src/fastmcp/server/middleware/dereference.py` | `fastmcp/server/middleware/dereference.py` | 0 | 1 | DereferenceRefsMiddleware |
| `python-sdk/fastmcp-server-middleware-error_handling.md` | `fastmcp.server.middleware.error_handling` | `src/fastmcp/server/middleware/error_handling.py` | `fastmcp/server/middleware/error_handling.py` | 0 | 2 | ErrorHandlingMiddleware, RetryMiddleware |
| `python-sdk/fastmcp-server-middleware-logging.md` | `fastmcp.server.middleware.logging` | `src/fastmcp/server/middleware/logging.py` | `fastmcp/server/middleware/logging.py` | 1 | 3 | default_serializer, BaseLoggingMiddleware, LoggingMiddleware, StructuredLoggingMiddleware |
| `python-sdk/fastmcp-server-middleware-middleware.md` | `fastmcp.server.middleware.middleware` | `src/fastmcp/server/middleware/middleware.py` | `fastmcp/server/middleware/middleware.py` | 1 | 3 | make_middleware_wrapper, CallNext, MiddlewareContext, Middleware |
| `python-sdk/fastmcp-server-middleware-ping.md` | `fastmcp.server.middleware.ping` | `src/fastmcp/server/middleware/ping.py` | `fastmcp/server/middleware/ping.py` | 0 | 1 | PingMiddleware |
| `python-sdk/fastmcp-server-middleware-rate_limiting.md` | `fastmcp.server.middleware.rate_limiting` | `src/fastmcp/server/middleware/rate_limiting.py` | `fastmcp/server/middleware/rate_limiting.py` | 0 | 5 | RateLimitError, TokenBucketRateLimiter, SlidingWindowRateLimiter, RateLimitingMiddleware, SlidingWindowRateLimitingMiddleware |
| `python-sdk/fastmcp-server-middleware-response_limiting.md` | `fastmcp.server.middleware.response_limiting` | `src/fastmcp/server/middleware/response_limiting.py` | `fastmcp/server/middleware/response_limiting.py` | 0 | 1 | ResponseLimitingMiddleware |
| `python-sdk/fastmcp-server-middleware-timing.md` | `fastmcp.server.middleware.timing` | `src/fastmcp/server/middleware/timing.py` | `fastmcp/server/middleware/timing.py` | 0 | 2 | TimingMiddleware, DetailedTimingMiddleware |
| `python-sdk/fastmcp-server-middleware-tool_injection.md` | `fastmcp.server.middleware.tool_injection` | `src/fastmcp/server/middleware/tool_injection.py` | `fastmcp/server/middleware/tool_injection.py` | 4 | 3 | list_prompts, get_prompt, list_resources, read_resource, ToolInjectionMiddleware, PromptToolMiddleware, ResourceToolMiddleware |
| `python-sdk/fastmcp-server-mixins-__init__.md` | `fastmcp.server.mixins` | `src/fastmcp/server/mixins/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-mixins-lifespan.md` | `fastmcp.server.mixins.lifespan` | `src/fastmcp/server/mixins/lifespan.py` | `fastmcp/server/mixins/lifespan.py` | 0 | 1 | LifespanMixin |
| `python-sdk/fastmcp-server-mixins-mcp_operations.md` | `fastmcp.server.mixins.mcp_operations` | `src/fastmcp/server/mixins/mcp_operations.py` | `fastmcp/server/mixins/mcp_operations.py` | 0 | 1 | MCPOperationsMixin |
| `python-sdk/fastmcp-server-mixins-transport.md` | `fastmcp.server.mixins.transport` | `src/fastmcp/server/mixins/transport.py` | `fastmcp/server/mixins/transport.py` | 0 | 1 | TransportMixin |
| `python-sdk/fastmcp-server-openapi-__init__.md` | `fastmcp.server.openapi` | `src/fastmcp/server/openapi/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-openapi-components.md` | `fastmcp.server.openapi.components` | `src/fastmcp/server/openapi/components.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-openapi-routing.md` | `fastmcp.server.openapi.routing` | `src/fastmcp/server/openapi/routing.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-openapi-server.md` | `fastmcp.server.openapi.server` | `src/fastmcp/server/openapi/server.py` | `fastmcp/server/openapi/server.py` | 0 | 1 | FastMCPOpenAPI |
| `python-sdk/fastmcp-server-providers-__init__.md` | `fastmcp.server.providers` | `src/fastmcp/server/providers/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-providers-aggregate.md` | `fastmcp.server.providers.aggregate` | `src/fastmcp/server/providers/aggregate.py` | `fastmcp/server/providers/aggregate.py` | 0 | 1 | AggregateProvider |
| `python-sdk/fastmcp-server-providers-base.md` | `fastmcp.server.providers.base` | `src/fastmcp/server/providers/base.py` | `fastmcp/server/providers/base.py` | 0 | 1 | Provider |
| `python-sdk/fastmcp-server-providers-fastmcp_provider.md` | `fastmcp.server.providers.fastmcp_provider` | `src/fastmcp/server/providers/fastmcp_provider.py` | `fastmcp/server/providers/fastmcp_provider.py` | 0 | 5 | FastMCPProviderTool, FastMCPProviderResource, FastMCPProviderPrompt, FastMCPProviderResourceTemplate, FastMCPProvider |
| `python-sdk/fastmcp-server-providers-filesystem.md` | `fastmcp.server.providers.filesystem` | `src/fastmcp/server/providers/filesystem.py` | `fastmcp/server/providers/filesystem.py` | 0 | 1 | FileSystemProvider |
| `python-sdk/fastmcp-server-providers-filesystem_discovery.md` | `fastmcp.server.providers.filesystem_discovery` | `src/fastmcp/server/providers/filesystem_discovery.py` | `fastmcp/server/providers/filesystem_discovery.py` | 4 | 1 | discover_files, import_module_from_file, extract_components, discover_and_import, DiscoveryResult |
| `python-sdk/fastmcp-server-providers-local_provider-__init__.md` | `fastmcp.server.providers.local_provider` | `src/fastmcp/server/providers/local_provider/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-providers-local_provider-decorators-__init__.md` | `fastmcp.server.providers.local_provider.decorators` | `src/fastmcp/server/providers/local_provider/decorators/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-providers-local_provider-decorators-prompts.md` | `fastmcp.server.providers.local_provider.decorators.prompts` | `src/fastmcp/server/providers/local_provider/decorators/prompts.py` | `fastmcp/server/providers/local_provider/decorators/prompts.py` | 0 | 1 | PromptDecoratorMixin |
| `python-sdk/fastmcp-server-providers-local_provider-decorators-resources.md` | `fastmcp.server.providers.local_provider.decorators.resources` | `src/fastmcp/server/providers/local_provider/decorators/resources.py` | `fastmcp/server/providers/local_provider/decorators/resources.py` | 0 | 1 | ResourceDecoratorMixin |
| `python-sdk/fastmcp-server-providers-local_provider-decorators-tools.md` | `fastmcp.server.providers.local_provider.decorators.tools` | `src/fastmcp/server/providers/local_provider/decorators/tools.py` | `fastmcp/server/providers/local_provider/decorators/tools.py` | 0 | 1 | ToolDecoratorMixin |
| `python-sdk/fastmcp-server-providers-local_provider-local_provider.md` | `fastmcp.server.providers.local_provider.local_provider` | `src/fastmcp/server/providers/local_provider/local_provider.py` | `fastmcp/server/providers/local_provider/local_provider.py` | 0 | 1 | LocalProvider |
| `python-sdk/fastmcp-server-providers-openapi-__init__.md` | `fastmcp.server.providers.openapi` | `src/fastmcp/server/providers/openapi/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-providers-openapi-components.md` | `fastmcp.server.providers.openapi.components` | `src/fastmcp/server/providers/openapi/components.py` | `fastmcp/server/providers/openapi/components.py` | 0 | 3 | OpenAPITool, OpenAPIResource, OpenAPIResourceTemplate |
| `python-sdk/fastmcp-server-providers-openapi-provider.md` | `fastmcp.server.providers.openapi.provider` | `src/fastmcp/server/providers/openapi/provider.py` | `fastmcp/server/providers/openapi/provider.py` | 0 | 1 | OpenAPIProvider |
| `python-sdk/fastmcp-server-providers-openapi-routing.md` | `fastmcp.server.providers.openapi.routing` | `src/fastmcp/server/providers/openapi/routing.py` | `fastmcp/server/providers/openapi/routing.py` | 0 | 2 | MCPType, RouteMap |
| `python-sdk/fastmcp-server-providers-proxy.md` | `fastmcp.server.providers.proxy` | `src/fastmcp/server/providers/proxy.py` | `fastmcp/server/providers/proxy.py` | 5 | 8 | default_proxy_roots_handler, default_proxy_sampling_handler, default_proxy_elicitation_handler, default_proxy_log_handler, default_proxy_progress_handler, ProxyTool, ProxyResource, ProxyTemplate, ProxyPrompt, ProxyProvider, FastMCPProxy |
| `python-sdk/fastmcp-server-providers-skills-__init__.md` | `fastmcp.server.providers.skills` | `src/fastmcp/server/providers/skills/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-providers-skills-claude_provider.md` | `fastmcp.server.providers.skills.claude_provider` | `src/fastmcp/server/providers/skills/claude_provider.py` | `fastmcp/server/providers/skills/claude_provider.py` | 0 | 1 | ClaudeSkillsProvider |
| `python-sdk/fastmcp-server-providers-skills-directory_provider.md` | `fastmcp.server.providers.skills.directory_provider` | `src/fastmcp/server/providers/skills/directory_provider.py` | `fastmcp/server/providers/skills/directory_provider.py` | 0 | 1 | SkillsDirectoryProvider |
| `python-sdk/fastmcp-server-providers-skills-skill_provider.md` | `fastmcp.server.providers.skills.skill_provider` | `src/fastmcp/server/providers/skills/skill_provider.py` | `fastmcp/server/providers/skills/skill_provider.py` | 0 | 4 | SkillResource, SkillFileTemplate, SkillFileResource, SkillProvider |
| `python-sdk/fastmcp-server-providers-skills-vendor_providers.md` | `fastmcp.server.providers.skills.vendor_providers` | `src/fastmcp/server/providers/skills/vendor_providers.py` | `fastmcp/server/providers/skills/vendor_providers.py` | 0 | 7 | CursorSkillsProvider, VSCodeSkillsProvider, CodexSkillsProvider, GeminiSkillsProvider, GooseSkillsProvider, CopilotSkillsProvider |
| `python-sdk/fastmcp-server-providers-wrapped_provider.md` | `fastmcp.server.providers.wrapped_provider` | `src/fastmcp/server/providers/wrapped_provider.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-proxy.md` | `fastmcp.server.proxy` | `src/fastmcp/server/proxy.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-sampling-__init__.md` | `fastmcp.server.sampling` | `src/fastmcp/server/sampling/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-sampling-run.md` | `fastmcp.server.sampling.run` | `src/fastmcp/server/sampling/run.py` | `fastmcp/server/sampling/run.py` | 9 | 2 | determine_handler_mode, call_sampling_handler, execute_tools, prepare_messages, prepare_tools, extract_tool_calls, SamplingResult, SampleStep |
| `python-sdk/fastmcp-server-sampling-sampling_tool.md` | `fastmcp.server.sampling.sampling_tool` | `src/fastmcp/server/sampling/sampling_tool.py` | `fastmcp/server/sampling/sampling_tool.py` | 0 | 1 | SamplingTool |
| `python-sdk/fastmcp-server-server.md` | `fastmcp.server.server` | `src/fastmcp/server/server.py` | `fastmcp/server/server.py` | 2 | 2 | default_lifespan, create_proxy, StateValue, FastMCP |
| `python-sdk/fastmcp-server-tasks-__init__.md` | `fastmcp.server.tasks` | `src/fastmcp/server/tasks/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-server-tasks-capabilities.md` | `fastmcp.server.tasks.capabilities` | `src/fastmcp/server/tasks/capabilities.py` | `fastmcp/server/tasks/capabilities.py` | 1 | 0 | get_task_capabilities |
| `python-sdk/fastmcp-server-tasks-config.md` | `fastmcp.server.tasks.config` | `src/fastmcp/server/tasks/config.py` | `fastmcp/server/tasks/config.py` | 0 | 2 | TaskMeta, TaskConfig |
| `python-sdk/fastmcp-server-tasks-elicitation.md` | `fastmcp.server.tasks.elicitation` | `src/fastmcp/server/tasks/elicitation.py` | `fastmcp/server/tasks/elicitation.py` | 3 | 0 | elicit_for_task, relay_elicitation, handle_task_input |
| `python-sdk/fastmcp-server-tasks-handlers.md` | `fastmcp.server.tasks.handlers` | `src/fastmcp/server/tasks/handlers.py` | `fastmcp/server/tasks/handlers.py` | 1 | 0 | submit_to_docket |
| `python-sdk/fastmcp-server-tasks-keys.md` | `fastmcp.server.tasks.keys` | `src/fastmcp/server/tasks/keys.py` | `fastmcp/server/tasks/keys.py` | 3 | 0 | build_task_key, parse_task_key, get_client_task_id_from_key |
| `python-sdk/fastmcp-server-tasks-notifications.md` | `fastmcp.server.tasks.notifications` | `src/fastmcp/server/tasks/notifications.py` | `fastmcp/server/tasks/notifications.py` | 5 | 0 | push_notification, notification_subscriber_loop, ensure_subscriber_running, stop_subscriber, get_subscriber_count |
| `python-sdk/fastmcp-server-tasks-requests.md` | `fastmcp.server.tasks.requests` | `src/fastmcp/server/tasks/requests.py` | `fastmcp/server/tasks/requests.py` | 4 | 0 | tasks_get_handler, tasks_result_handler, tasks_list_handler, tasks_cancel_handler |
| `python-sdk/fastmcp-server-tasks-routing.md` | `fastmcp.server.tasks.routing` | `src/fastmcp/server/tasks/routing.py` | `fastmcp/server/tasks/routing.py` | 1 | 0 | check_background_task |
| `python-sdk/fastmcp-server-tasks-subscriptions.md` | `fastmcp.server.tasks.subscriptions` | `src/fastmcp/server/tasks/subscriptions.py` | `fastmcp/server/tasks/subscriptions.py` | 1 | 0 | subscribe_to_task_updates |
| `python-sdk/fastmcp-server-telemetry.md` | `fastmcp.server.telemetry` | `src/fastmcp/server/telemetry.py` | `fastmcp/server/telemetry.py` | 4 | 0 | get_auth_span_attributes, get_session_span_attributes, server_span, delegate_span |
| `python-sdk/fastmcp-server-transforms-__init__.md` | `fastmcp.server.transforms` | `src/fastmcp/server/transforms/__init__.py` | `fastmcp/server/transforms/__init__.py` | 0 | 5 | GetToolNext, GetResourceNext, GetResourceTemplateNext, GetPromptNext, Transform |
| `python-sdk/fastmcp-server-transforms-namespace.md` | `fastmcp.server.transforms.namespace` | `src/fastmcp/server/transforms/namespace.py` | `fastmcp/server/transforms/namespace.py` | 0 | 1 | Namespace |
| `python-sdk/fastmcp-server-transforms-prompts_as_tools.md` | `fastmcp.server.transforms.prompts_as_tools` | `src/fastmcp/server/transforms/prompts_as_tools.py` | `fastmcp/server/transforms/prompts_as_tools.py` | 0 | 1 | PromptsAsTools |
| `python-sdk/fastmcp-server-transforms-resources_as_tools.md` | `fastmcp.server.transforms.resources_as_tools` | `src/fastmcp/server/transforms/resources_as_tools.py` | `fastmcp/server/transforms/resources_as_tools.py` | 0 | 1 | ResourcesAsTools |
| `python-sdk/fastmcp-server-transforms-tool_transform.md` | `fastmcp.server.transforms.tool_transform` | `src/fastmcp/server/transforms/tool_transform.py` | `fastmcp/server/transforms/tool_transform.py` | 0 | 1 | ToolTransform |
| `python-sdk/fastmcp-server-transforms-version_filter.md` | `fastmcp.server.transforms.version_filter` | `src/fastmcp/server/transforms/version_filter.py` | `fastmcp/server/transforms/version_filter.py` | 0 | 1 | VersionFilter |
| `python-sdk/fastmcp-server-transforms-visibility.md` | `fastmcp.server.transforms.visibility` | `src/fastmcp/server/transforms/visibility.py` | `fastmcp/server/transforms/visibility.py` | 9 | 1 | is_enabled, get_visibility_rules, save_visibility_rules, create_visibility_transforms, get_session_transforms, enable_components, Visibility |

## utilities

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-utilities-__init__.md` | `fastmcp.utilities` | `src/fastmcp/utilities/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-utilities-async_utils.md` | `fastmcp.utilities.async_utils` | `src/fastmcp/utilities/async_utils.py` | `fastmcp/utilities/async_utils.py` | 2 | 0 | call_sync_fn_in_threadpool, gather |
| `python-sdk/fastmcp-utilities-auth.md` | `fastmcp.utilities.auth` | `src/fastmcp/utilities/auth.py` | `fastmcp/utilities/auth.py` | 3 | 0 | decode_jwt_header, decode_jwt_payload, parse_scopes |
| `python-sdk/fastmcp-utilities-cli.md` | `fastmcp.utilities.cli` | `src/fastmcp/utilities/cli.py` | `fastmcp/utilities/cli.py` | 3 | 0 | is_already_in_uv_subprocess, load_and_merge_config, log_server_banner |
| `python-sdk/fastmcp-utilities-components.md` | `fastmcp.utilities.components` | `src/fastmcp/utilities/components.py` | `fastmcp/utilities/components.py` | 1 | 2 | get_fastmcp_metadata, FastMCPMeta, FastMCPComponent |
| `python-sdk/fastmcp-utilities-exceptions.md` | `fastmcp.utilities.exceptions` | `src/fastmcp/utilities/exceptions.py` | `fastmcp/utilities/exceptions.py` | 2 | 0 | iter_exc, get_catch_handlers |
| `python-sdk/fastmcp-utilities-http.md` | `fastmcp.utilities.http` | `src/fastmcp/utilities/http.py` | `fastmcp/utilities/http.py` | 1 | 0 | find_available_port |
| `python-sdk/fastmcp-utilities-inspect.md` | `fastmcp.utilities.inspect` | `src/fastmcp/utilities/inspect.py` | `fastmcp/utilities/inspect.py` | 6 | 6 | inspect_fastmcp_v2, inspect_fastmcp_v1, inspect_fastmcp, format_fastmcp_info, format_mcp_info, format_info, ToolInfo, PromptInfo, ResourceInfo, TemplateInfo, FastMCPInfo, InspectFormat |
| `python-sdk/fastmcp-utilities-json_schema.md` | `fastmcp.utilities.json_schema` | `src/fastmcp/utilities/json_schema.py` | `fastmcp/utilities/json_schema.py` | 3 | 0 | dereference_refs, resolve_root_ref, compress_schema |
| `python-sdk/fastmcp-utilities-json_schema_type.md` | `fastmcp.utilities.json_schema_type` | `src/fastmcp/utilities/json_schema_type.py` | `fastmcp/utilities/json_schema_type.py` | 1 | 1 | json_schema_to_type, JSONSchema |
| `python-sdk/fastmcp-utilities-lifespan.md` | `fastmcp.utilities.lifespan` | `src/fastmcp/utilities/lifespan.py` | `fastmcp/utilities/lifespan.py` | 1 | 0 | combine_lifespans |
| `python-sdk/fastmcp-utilities-logging.md` | `fastmcp.utilities.logging` | `src/fastmcp/utilities/logging.py` | `fastmcp/utilities/logging.py` | 3 | 0 | get_logger, configure_logging, temporary_log_level |
| `python-sdk/fastmcp-utilities-mcp_server_config-__init__.md` | `fastmcp.utilities.mcp_server_config` | `src/fastmcp/utilities/mcp_server_config/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-__init__.md` | `fastmcp.utilities.mcp_server_config.v1` | `src/fastmcp/utilities/mcp_server_config/v1/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-__init__.md` | `fastmcp.utilities.mcp_server_config.v1.environments` | `src/fastmcp/utilities/mcp_server_config/v1/environments/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-base.md` | `fastmcp.utilities.mcp_server_config.v1.environments.base` | `src/fastmcp/utilities/mcp_server_config/v1/environments/base.py` | `fastmcp/utilities/mcp_server_config/v1/environments/base.py` | 0 | 1 | Environment |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-uv.md` | `fastmcp.utilities.mcp_server_config.v1.environments.uv` | `src/fastmcp/utilities/mcp_server_config/v1/environments/uv.py` | `fastmcp/utilities/mcp_server_config/v1/environments/uv.py` | 0 | 1 | UVEnvironment |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-mcp_server_config.md` | `fastmcp.utilities.mcp_server_config.v1.mcp_server_config` | `src/fastmcp/utilities/mcp_server_config/v1/mcp_server_config.py` | `fastmcp/utilities/mcp_server_config/v1/mcp_server_config.py` | 1 | 2 | generate_schema, Deployment, MCPServerConfig |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-__init__.md` | `fastmcp.utilities.mcp_server_config.v1.sources` | `src/fastmcp/utilities/mcp_server_config/v1/sources/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-base.md` | `fastmcp.utilities.mcp_server_config.v1.sources.base` | `src/fastmcp/utilities/mcp_server_config/v1/sources/base.py` | `fastmcp/utilities/mcp_server_config/v1/sources/base.py` | 0 | 1 | Source |
| `python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-filesystem.md` | `fastmcp.utilities.mcp_server_config.v1.sources.filesystem` | `src/fastmcp/utilities/mcp_server_config/v1/sources/filesystem.py` | `fastmcp/utilities/mcp_server_config/v1/sources/filesystem.py` | 0 | 1 | FileSystemSource |
| `python-sdk/fastmcp-utilities-openapi-__init__.md` | `fastmcp.utilities.openapi` | `src/fastmcp/utilities/openapi/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-utilities-openapi-director.md` | `fastmcp.utilities.openapi.director` | `src/fastmcp/utilities/openapi/director.py` | `fastmcp/utilities/openapi/director.py` | 0 | 1 | RequestDirector |
| `python-sdk/fastmcp-utilities-openapi-formatters.md` | `fastmcp.utilities.openapi.formatters` | `src/fastmcp/utilities/openapi/formatters.py` | `fastmcp/utilities/openapi/formatters.py` | 5 | 0 | format_array_parameter, format_deep_object_parameter, generate_example_from_schema, format_json_for_description, format_description_with_responses |
| `python-sdk/fastmcp-utilities-openapi-json_schema_converter.md` | `fastmcp.utilities.openapi.json_schema_converter` | `src/fastmcp/utilities/openapi/json_schema_converter.py` | `fastmcp/utilities/openapi/json_schema_converter.py` | 2 | 0 | convert_openapi_schema_to_json_schema, convert_schema_definitions |
| `python-sdk/fastmcp-utilities-openapi-models.md` | `fastmcp.utilities.openapi.models` | `src/fastmcp/utilities/openapi/models.py` | `fastmcp/utilities/openapi/models.py` | 0 | 4 | ParameterInfo, RequestBodyInfo, ResponseInfo, HTTPRoute |
| `python-sdk/fastmcp-utilities-openapi-parser.md` | `fastmcp.utilities.openapi.parser` | `src/fastmcp/utilities/openapi/parser.py` | `fastmcp/utilities/openapi/parser.py` | 1 | 1 | parse_openapi_to_http_routes, OpenAPIParser |
| `python-sdk/fastmcp-utilities-openapi-schemas.md` | `fastmcp.utilities.openapi.schemas` | `src/fastmcp/utilities/openapi/schemas.py` | `fastmcp/utilities/openapi/schemas.py` | 2 | 0 | clean_schema_for_display, extract_output_schema_from_responses |
| `python-sdk/fastmcp-utilities-pagination.md` | `fastmcp.utilities.pagination` | `src/fastmcp/utilities/pagination.py` | `fastmcp/utilities/pagination.py` | 1 | 1 | paginate_sequence, CursorState |
| `python-sdk/fastmcp-utilities-skills.md` | `fastmcp.utilities.skills` | `src/fastmcp/utilities/skills.py` | `fastmcp/utilities/skills.py` | 4 | 3 | list_skills, get_skill_manifest, download_skill, sync_skills, SkillSummary, SkillFile, SkillManifest |
| `python-sdk/fastmcp-utilities-tests.md` | `fastmcp.utilities.tests` | `src/fastmcp/utilities/tests.py` | `fastmcp/utilities/tests.py` | 3 | 1 | temporary_settings, run_server_in_process, run_server_async, HeadlessOAuth |
| `python-sdk/fastmcp-utilities-timeout.md` | `fastmcp.utilities.timeout` | `src/fastmcp/utilities/timeout.py` | `fastmcp/utilities/timeout.py` | 2 | 0 | normalize_timeout_to_timedelta, normalize_timeout_to_seconds |
| `python-sdk/fastmcp-utilities-types.md` | `fastmcp.utilities.types` | `src/fastmcp/utilities/types.py` | `fastmcp/utilities/types.py` | 7 | 5 | get_fn_name, get_cached_typeadapter, issubclass_safe, is_class_member_of_type, find_kwarg_by_type, create_function_without_params, FastMCPBaseModel, Image, Audio, File, ContextSamplingFallbackProtocol |
| `python-sdk/fastmcp-utilities-ui.md` | `fastmcp.utilities.ui` | `src/fastmcp/utilities/ui.py` | `fastmcp/utilities/ui.py` | 7 | 0 | create_page, create_logo, create_status_message, create_info_box, create_detail_box, create_button_group |
| `python-sdk/fastmcp-utilities-version_check.md` | `fastmcp.utilities.version_check` | `src/fastmcp/utilities/version_check.py` | `fastmcp/utilities/version_check.py` | 2 | 0 | get_latest_version, check_for_newer_version |
| `python-sdk/fastmcp-utilities-versions.md` | `fastmcp.utilities.versions` | `src/fastmcp/utilities/versions.py` | `fastmcp/utilities/versions.py` | 6 | 2 | parse_version_key, version_sort_key, compare_versions, is_version_greater, max_version, min_version, VersionSpec, VersionKey |

## client

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-client-__init__.md` | `fastmcp.client` | `src/fastmcp/client/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-client-auth-__init__.md` | `fastmcp.client.auth` | `src/fastmcp/client/auth/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-client-auth-bearer.md` | `fastmcp.client.auth.bearer` | `src/fastmcp/client/auth/bearer.py` | `fastmcp/client/auth/bearer.py` | 0 | 1 | BearerAuth |
| `python-sdk/fastmcp-client-auth-oauth.md` | `fastmcp.client.auth.oauth` | `src/fastmcp/client/auth/oauth.py` | `fastmcp/client/auth/oauth.py` | 1 | 3 | check_if_auth_required, ClientNotFoundError, TokenStorageAdapter, OAuth |
| `python-sdk/fastmcp-client-client.md` | `fastmcp.client.client` | `src/fastmcp/client/client.py` | `fastmcp/client/client.py` | 0 | 3 | ClientSessionState, CallToolResult, Client |
| `python-sdk/fastmcp-client-elicitation.md` | `fastmcp.client.elicitation` | `src/fastmcp/client/elicitation.py` | `fastmcp/client/elicitation.py` | 1 | 1 | create_elicitation_callback, ElicitResult |
| `python-sdk/fastmcp-client-logging.md` | `fastmcp.client.logging` | `src/fastmcp/client/logging.py` | `fastmcp/client/logging.py` | 2 | 0 | default_log_handler, create_log_callback |
| `python-sdk/fastmcp-client-messages.md` | `fastmcp.client.messages` | `src/fastmcp/client/messages.py` | `fastmcp/client/messages.py` | 0 | 1 | MessageHandler |
| `python-sdk/fastmcp-client-mixins-__init__.md` | `fastmcp.client.mixins` | `src/fastmcp/client/mixins/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-client-mixins-prompts.md` | `fastmcp.client.mixins.prompts` | `src/fastmcp/client/mixins/prompts.py` | `fastmcp/client/mixins/prompts.py` | 0 | 1 | ClientPromptsMixin |
| `python-sdk/fastmcp-client-mixins-resources.md` | `fastmcp.client.mixins.resources` | `src/fastmcp/client/mixins/resources.py` | `fastmcp/client/mixins/resources.py` | 0 | 1 | ClientResourcesMixin |
| `python-sdk/fastmcp-client-mixins-task_management.md` | `fastmcp.client.mixins.task_management` | `src/fastmcp/client/mixins/task_management.py` | `fastmcp/client/mixins/task_management.py` | 0 | 1 | ClientTaskManagementMixin |
| `python-sdk/fastmcp-client-mixins-tools.md` | `fastmcp.client.mixins.tools` | `src/fastmcp/client/mixins/tools.py` | `fastmcp/client/mixins/tools.py` | 0 | 1 | ClientToolsMixin |
| `python-sdk/fastmcp-client-oauth_callback.md` | `fastmcp.client.oauth_callback` | `src/fastmcp/client/oauth_callback.py` | `fastmcp/client/oauth_callback.py` | 2 | 2 | create_callback_html, create_oauth_callback_server, CallbackResponse, OAuthCallbackResult |
| `python-sdk/fastmcp-client-progress.md` | `fastmcp.client.progress` | `src/fastmcp/client/progress.py` | `fastmcp/client/progress.py` | 1 | 0 | default_progress_handler |
| `python-sdk/fastmcp-client-roots.md` | `fastmcp.client.roots` | `src/fastmcp/client/roots.py` | `fastmcp/client/roots.py` | 2 | 0 | convert_roots_list, create_roots_callback |
| `python-sdk/fastmcp-client-sampling-__init__.md` | `fastmcp.client.sampling` | `src/fastmcp/client/sampling/__init__.py` | `fastmcp/client/sampling/__init__.py` | 1 | 0 | create_sampling_callback |
| `python-sdk/fastmcp-client-sampling-handlers-__init__.md` | `fastmcp.client.sampling.handlers` | `src/fastmcp/client/sampling/handlers/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-client-sampling-handlers-anthropic.md` | `fastmcp.client.sampling.handlers.anthropic` | `src/fastmcp/client/sampling/handlers/anthropic.py` | `fastmcp/client/sampling/handlers/anthropic.py` | 0 | 1 | AnthropicSamplingHandler |
| `python-sdk/fastmcp-client-sampling-handlers-openai.md` | `fastmcp.client.sampling.handlers.openai` | `src/fastmcp/client/sampling/handlers/openai.py` | `fastmcp/client/sampling/handlers/openai.py` | 0 | 1 | OpenAISamplingHandler |
| `python-sdk/fastmcp-client-tasks.md` | `fastmcp.client.tasks` | `src/fastmcp/client/tasks.py` | `fastmcp/client/tasks.py` | 0 | 5 | TaskNotificationHandler, Task, ToolTask, PromptTask, ResourceTask |
| `python-sdk/fastmcp-client-telemetry.md` | `fastmcp.client.telemetry` | `src/fastmcp/client/telemetry.py` | `fastmcp/client/telemetry.py` | 1 | 0 | client_span |
| `python-sdk/fastmcp-client-transports-__init__.md` | `fastmcp.client.transports` | `src/fastmcp/client/transports/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-client-transports-base.md` | `fastmcp.client.transports.base` | `src/fastmcp/client/transports/base.py` | `fastmcp/client/transports/base.py` | 0 | 2 | SessionKwargs, ClientTransport |
| `python-sdk/fastmcp-client-transports-config.md` | `fastmcp.client.transports.config` | `src/fastmcp/client/transports/config.py` | `fastmcp/client/transports/config.py` | 0 | 1 | MCPConfigTransport |
| `python-sdk/fastmcp-client-transports-http.md` | `fastmcp.client.transports.http` | `src/fastmcp/client/transports/http.py` | `fastmcp/client/transports/http.py` | 0 | 1 | StreamableHttpTransport |
| `python-sdk/fastmcp-client-transports-inference.md` | `fastmcp.client.transports.inference` | `src/fastmcp/client/transports/inference.py` | `fastmcp/client/transports/inference.py` | 1 | 0 | infer_transport |
| `python-sdk/fastmcp-client-transports-memory.md` | `fastmcp.client.transports.memory` | `src/fastmcp/client/transports/memory.py` | `fastmcp/client/transports/memory.py` | 0 | 1 | FastMCPTransport |
| `python-sdk/fastmcp-client-transports-sse.md` | `fastmcp.client.transports.sse` | `src/fastmcp/client/transports/sse.py` | `fastmcp/client/transports/sse.py` | 0 | 1 | SSETransport |
| `python-sdk/fastmcp-client-transports-stdio.md` | `fastmcp.client.transports.stdio` | `src/fastmcp/client/transports/stdio.py` | `fastmcp/client/transports/stdio.py` | 0 | 7 | StdioTransport, PythonStdioTransport, FastMCPStdioTransport, NodeStdioTransport, UvStdioTransport, UvxStdioTransport |

## cli

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-cli-__init__.md` | `fastmcp.cli` | `src/fastmcp/cli/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-cli-auth.md` | `fastmcp.cli.auth` | `src/fastmcp/cli/auth.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-cli-cimd.md` | `fastmcp.cli.cimd` | `src/fastmcp/cli/cimd.py` | `fastmcp/cli/cimd.py` | 2 | 0 | create_command, validate_command |
| `python-sdk/fastmcp-cli-cli.md` | `fastmcp.cli.cli` | `src/fastmcp/cli/cli.py` | `fastmcp/cli/cli.py` | 6 | 0 | with_argv, version, inspector, run, inspect, prepare |
| `python-sdk/fastmcp-cli-client.md` | `fastmcp.cli.client` | `src/fastmcp/cli/client.py` | `fastmcp/cli/client.py` | 7 | 0 | resolve_server_spec, coerce_value, parse_tool_arguments, format_tool_signature, list_command, call_command |
| `python-sdk/fastmcp-cli-discovery.md` | `fastmcp.cli.discovery` | `src/fastmcp/cli/discovery.py` | `fastmcp/cli/discovery.py` | 2 | 1 | discover_servers, resolve_name, DiscoveredServer |
| `python-sdk/fastmcp-cli-generate.md` | `fastmcp.cli.generate` | `src/fastmcp/cli/generate.py` | `fastmcp/cli/generate.py` | 4 | 0 | serialize_transport, generate_cli_script, generate_skill_content, generate_cli_command |
| `python-sdk/fastmcp-cli-install-__init__.md` | `fastmcp.cli.install` | `src/fastmcp/cli/install/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-cli-install-claude_code.md` | `fastmcp.cli.install.claude_code` | `src/fastmcp/cli/install/claude_code.py` | `fastmcp/cli/install/claude_code.py` | 4 | 0 | find_claude_command, check_claude_code_available, install_claude_code, claude_code_command |
| `python-sdk/fastmcp-cli-install-claude_desktop.md` | `fastmcp.cli.install.claude_desktop` | `src/fastmcp/cli/install/claude_desktop.py` | `fastmcp/cli/install/claude_desktop.py` | 3 | 0 | get_claude_config_path, install_claude_desktop, claude_desktop_command |
| `python-sdk/fastmcp-cli-install-cursor.md` | `fastmcp.cli.install.cursor` | `src/fastmcp/cli/install/cursor.py` | `fastmcp/cli/install/cursor.py` | 5 | 0 | generate_cursor_deeplink, open_deeplink, install_cursor_workspace, install_cursor, cursor_command |
| `python-sdk/fastmcp-cli-install-gemini_cli.md` | `fastmcp.cli.install.gemini_cli` | `src/fastmcp/cli/install/gemini_cli.py` | `fastmcp/cli/install/gemini_cli.py` | 4 | 0 | find_gemini_command, check_gemini_cli_available, install_gemini_cli, gemini_cli_command |
| `python-sdk/fastmcp-cli-install-goose.md` | `fastmcp.cli.install.goose` | `src/fastmcp/cli/install/goose.py` | `fastmcp/cli/install/goose.py` | 3 | 0 | generate_goose_deeplink, install_goose, goose_command |
| `python-sdk/fastmcp-cli-install-mcp_json.md` | `fastmcp.cli.install.mcp_json` | `src/fastmcp/cli/install/mcp_json.py` | `fastmcp/cli/install/mcp_json.py` | 2 | 0 | install_mcp_json, mcp_json_command |
| `python-sdk/fastmcp-cli-install-shared.md` | `fastmcp.cli.install.shared` | `src/fastmcp/cli/install/shared.py` | `fastmcp/cli/install/shared.py` | 3 | 0 | parse_env_var, process_common_args, open_deeplink |
| `python-sdk/fastmcp-cli-install-stdio.md` | `fastmcp.cli.install.stdio` | `src/fastmcp/cli/install/stdio.py` | `fastmcp/cli/install/stdio.py` | 2 | 0 | install_stdio, stdio_command |
| `python-sdk/fastmcp-cli-run.md` | `fastmcp.cli.run` | `src/fastmcp/cli/run.py` | `fastmcp/cli/run.py` | 7 | 0 | is_url, create_client_server, create_mcp_config_server, load_mcp_server_config, run_command, run_v1_server_async |
| `python-sdk/fastmcp-cli-tasks.md` | `fastmcp.cli.tasks` | `src/fastmcp/cli/tasks.py` | `fastmcp/cli/tasks.py` | 2 | 0 | check_distributed_backend, worker |

## resources

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-resources-__init__.md` | `fastmcp.resources` | `src/fastmcp/resources/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-resources-function_resource.md` | `fastmcp.resources.function_resource` | `src/fastmcp/resources/function_resource.py` | `fastmcp/resources/function_resource.py` | 1 | 3 | resource, DecoratedResource, ResourceMeta, FunctionResource |
| `python-sdk/fastmcp-resources-resource.md` | `fastmcp.resources.resource` | `src/fastmcp/resources/resource.py` | `fastmcp/resources/resource.py` | 0 | 3 | ResourceContent, ResourceResult, Resource |
| `python-sdk/fastmcp-resources-template.md` | `fastmcp.resources.template` | `src/fastmcp/resources/template.py` | `fastmcp/resources/template.py` | 3 | 2 | extract_query_params, build_regex, match_uri_template, ResourceTemplate, FunctionResourceTemplate |
| `python-sdk/fastmcp-resources-types.md` | `fastmcp.resources.types` | `src/fastmcp/resources/types.py` | `fastmcp/resources/types.py` | 0 | 5 | TextResource, BinaryResource, FileResource, HttpResource, DirectoryResource |

## tools

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-tools-__init__.md` | `fastmcp.tools` | `src/fastmcp/tools/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-tools-function_parsing.md` | `fastmcp.tools.function_parsing` | `src/fastmcp/tools/function_parsing.py` | `fastmcp/tools/function_parsing.py` | 0 | 1 | ParsedFunction |
| `python-sdk/fastmcp-tools-function_tool.md` | `fastmcp.tools.function_tool` | `src/fastmcp/tools/function_tool.py` | `fastmcp/tools/function_tool.py` | 1 | 3 | tool, DecoratedTool, ToolMeta, FunctionTool |
| `python-sdk/fastmcp-tools-tool.md` | `fastmcp.tools.tool` | `src/fastmcp/tools/tool.py` | `fastmcp/tools/tool.py` | 1 | 2 | default_serializer, ToolResult, Tool |
| `python-sdk/fastmcp-tools-tool_transform.md` | `fastmcp.tools.tool_transform` | `src/fastmcp/tools/tool_transform.py` | `fastmcp/tools/tool_transform.py` | 3 | 4 | forward, forward_raw, apply_transformations_to_tools, ArgTransform, ArgTransformConfig, TransformedTool, ToolTransformConfig |

## prompts

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-prompts-__init__.md` | `fastmcp.prompts` | `src/fastmcp/prompts/__init__.py` | `` | 0 | 0 |  |
| `python-sdk/fastmcp-prompts-function_prompt.md` | `fastmcp.prompts.function_prompt` | `src/fastmcp/prompts/function_prompt.py` | `fastmcp/prompts/function_prompt.py` | 1 | 3 | prompt, DecoratedPrompt, PromptMeta, FunctionPrompt |
| `python-sdk/fastmcp-prompts-prompt.md` | `fastmcp.prompts.prompt` | `src/fastmcp/prompts/prompt.py` | `fastmcp/prompts/prompt.py` | 0 | 4 | Message, PromptArgument, PromptResult, Prompt |

## decorators

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-decorators.md` | `fastmcp.decorators` | `src/fastmcp/decorators.py` | `fastmcp/decorators.py` | 2 | 1 | resolve_task_config, get_fastmcp_meta, HasFastMCPMeta |

## dependencies

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-dependencies.md` | `fastmcp.dependencies` | `src/fastmcp/dependencies.py` | `` | 0 | 0 |  |

## exceptions

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-exceptions.md` | `fastmcp.exceptions` | `src/fastmcp/exceptions.py` | `fastmcp/exceptions.py` | 0 | 10 | FastMCPError, ValidationError, ResourceError, ToolError, PromptError, InvalidSignature |

## mcp_config

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-mcp_config.md` | `fastmcp.mcp_config` | `src/fastmcp/mcp_config.py` | `fastmcp/mcp_config.py` | 2 | 6 | infer_transport_type_from_url, update_config_file, StdioMCPServer, TransformingStdioMCPServer, RemoteMCPServer, TransformingRemoteMCPServer, MCPConfig, CanonicalMCPConfig |

## settings

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-settings.md` | `fastmcp.settings` | `src/fastmcp/settings.py` | `fastmcp/settings.py` | 0 | 2 | DocketSettings, Settings |

## telemetry

| API page | Module | Source module | GitHub src hint | Functions | Classes | Sample symbols |
|---|---|---|---|---:|---:|---|
| `python-sdk/fastmcp-telemetry.md` | `fastmcp.telemetry` | `src/fastmcp/telemetry.py` | `fastmcp/telemetry.py` | 4 | 0 | get_tracer, inject_trace_context, record_span_error, extract_trace_context |

