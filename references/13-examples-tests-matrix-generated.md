# Super-Big Examples And Tests Matrix (Generated)

Generated at: `2026-02-19 19:44:34Z`

## Summary

| Topic | Example files | Test files |
|---|---:|---:|
| `auth` | 28 | 50 |
| `cli` | 4 | 31 |
| `config` | 15 | 5 |
| `general` | 53 | 77 |
| `middleware-logging` | 0 | 14 |
| `prompts` | 2 | 3 |
| `providers-composition` | 11 | 41 |
| `resources` | 2 | 7 |
| `sampling` | 5 | 8 |
| `tasks` | 6 | 33 |
| `telemetry-observability` | 1 | 4 |
| `transforms-versioning` | 6 | 16 |
| `transports` | 1 | 13 |

## Table of Contents

- [auth](#auth)
- [cli](#cli)
- [config](#config)
- [general](#general)
- [middleware-logging](#middleware-logging)
- [prompts](#prompts)
- [providers-composition](#providers-composition)
- [resources](#resources)
- [sampling](#sampling)
- [tasks](#tasks)
- [telemetry-observability](#telemetry-observability)
- [transforms-versioning](#transforms-versioning)
- [transports](#transports)

## auth

### Example Files

| Path | Lines |
|---|---:|
| `examples/auth/authkit_dcr/README.md` | 25 |
| `examples/auth/authkit_dcr/client.py` | 33 |
| `examples/auth/authkit_dcr/server.py` | 32 |
| `examples/auth/aws_oauth/README.md` | 47 |
| `examples/auth/aws_oauth/client.py` | 42 |
| `examples/auth/aws_oauth/requirements.txt` | 2 |
| `examples/auth/aws_oauth/server.py` | 59 |
| `examples/auth/azure_oauth/README.md` | 51 |
| `examples/auth/azure_oauth/client.py` | 32 |
| `examples/auth/azure_oauth/server.py` | 44 |
| `examples/auth/discord_oauth/README.md` | 33 |
| `examples/auth/discord_oauth/client.py` | 32 |
| `examples/auth/discord_oauth/server.py` | 35 |
| `examples/auth/github_oauth/README.md` | 31 |
| `examples/auth/github_oauth/client.py` | 32 |
| `examples/auth/github_oauth/server.py` | 35 |
| `examples/auth/google_oauth/README.md` | 34 |
| `examples/auth/google_oauth/client.py` | 32 |
| `examples/auth/google_oauth/server.py` | 37 |
| `examples/auth/mounted/README.md` | 39 |
| `examples/auth/mounted/client.py` | 50 |
| `examples/auth/mounted/server.py` | 121 |
| `examples/auth/scalekit_oauth/README.md` | 55 |
| `examples/auth/scalekit_oauth/client.py` | 41 |
| `examples/auth/scalekit_oauth/server.py` | 58 |
| `examples/auth/workos_oauth/README.md` | 27 |
| `examples/auth/workos_oauth/client.py` | 32 |
| `examples/auth/workos_oauth/server.py` | 37 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/client/auth/__init__.py` | 0 |
| `tests/client/auth/test_oauth_cimd.py` | 164 |
| `tests/client/auth/test_oauth_client.py` | 358 |
| `tests/client/auth/test_oauth_static_client.py` | 274 |
| `tests/client/client/test_auth.py` | 82 |
| `tests/client/test_oauth_callback_xss.py` | 159 |
| `tests/integration_tests/auth/__init__.py` | 0 |
| `tests/integration_tests/auth/test_github_provider_integration.py` | 394 |
| `tests/server/auth/__init__.py` | 0 |
| `tests/server/auth/oauth_proxy/__init__.py` | 0 |
| `tests/server/auth/oauth_proxy/conftest.py` | 312 |
| `tests/server/auth/oauth_proxy/test_authorization.py` | 200 |
| `tests/server/auth/oauth_proxy/test_client_registration.py` | 43 |
| `tests/server/auth/oauth_proxy/test_config.py` | 452 |
| `tests/server/auth/oauth_proxy/test_e2e.py` | 244 |
| `tests/server/auth/oauth_proxy/test_oauth_proxy.py` | 102 |
| `tests/server/auth/oauth_proxy/test_tokens.py` | 503 |
| `tests/server/auth/oauth_proxy/test_ui.py` | 101 |
| `tests/server/auth/providers/__init__.py` | 0 |
| `tests/server/auth/providers/test_auth0.py` | 98 |
| `tests/server/auth/providers/test_aws.py` | 107 |
| `tests/server/auth/providers/test_azure.py` | 1417 |
| `tests/server/auth/providers/test_descope.py` | 238 |
| `tests/server/auth/providers/test_discord.py` | 83 |
| `tests/server/auth/providers/test_github.py` | 140 |
| `tests/server/auth/providers/test_google.py` | 136 |
| `tests/server/auth/providers/test_introspection.py` | 551 |
| `tests/server/auth/providers/test_scalekit.py` | 220 |
| `tests/server/auth/providers/test_supabase.py` | 202 |
| `tests/server/auth/providers/test_workos.py` | 167 |
| `tests/server/auth/test_auth_provider.py` | 105 |
| `tests/server/auth/test_authorization.py` | 733 |
| `tests/server/auth/test_cimd.py` | 1209 |
| `tests/server/auth/test_debug_verifier.py` | 169 |
| `tests/server/auth/test_enhanced_error_responses.py` | 370 |
| `tests/server/auth/test_jwt_issuer.py` | 287 |
| `tests/server/auth/test_jwt_provider.py` | 1121 |
| `tests/server/auth/test_oauth_consent_flow.py` | 1274 |
| `tests/server/auth/test_oauth_mounting.py` | 384 |
| `tests/server/auth/test_oauth_proxy_redirect_validation.py` | 401 |
| `tests/server/auth/test_oauth_proxy_storage.py` | 212 |
| `tests/server/auth/test_oidc_proxy.py` | 878 |
| `tests/server/auth/test_redirect_validation.py` | 200 |
| `tests/server/auth/test_remote_auth_provider.py` | 542 |
| `tests/server/auth/test_ssrf_protection.py` | 447 |
| `tests/server/auth/test_static_token_verifier.py` | 112 |
| `tests/server/http/test_bearer_auth_backend.py` | 179 |
| `tests/server/http/test_http_auth_middleware.py` | 94 |
| `tests/server/test_auth_integration.py` | 1242 |
| `tests/utilities/test_auth.py` | 177 |

## cli

### Example Files

| Path | Lines |
|---|---:|
| `examples/atproto_mcp/src/atproto_mcp/_atproto/_client.py` | 16 |
| `examples/diagnostics/client_with_tracing.py` | 161 |
| `examples/persistent_state/client.py` | 85 |
| `examples/skills/client.py` | 66 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/cli/__init__.py` | 1 |
| `tests/cli/test_cimd_cli.py` | 208 |
| `tests/cli/test_cli.py` | 621 |
| `tests/cli/test_client_commands.py` | 557 |
| `tests/cli/test_cursor.py` | 433 |
| `tests/cli/test_discovery.py` | 668 |
| `tests/cli/test_generate_cli.py` | 918 |
| `tests/cli/test_goose.py` | 298 |
| `tests/cli/test_install.py` | 443 |
| `tests/cli/test_project_prepare.py` | 306 |
| `tests/cli/test_run.py` | 697 |
| `tests/cli/test_server_args.py` | 135 |
| `tests/cli/test_shared.py` | 29 |
| `tests/cli/test_with_argv.py` | 91 |
| `tests/client/__init__.py` | 0 |
| `tests/client/client/__init__.py` | 0 |
| `tests/client/client/test_client.py` | 719 |
| `tests/client/client/test_error_handling.py` | 166 |
| `tests/client/client/test_initialize.py` | 115 |
| `tests/client/client/test_session.py` | 137 |
| `tests/client/client/test_timeout.py` | 50 |
| `tests/client/telemetry/__init__.py` | 0 |
| `tests/client/telemetry/test_client_tracing.py` | 633 |
| `tests/client/test_elicitation.py` | 1132 |
| `tests/client/test_logs.py` | 242 |
| `tests/client/test_notifications.py` | 124 |
| `tests/client/test_openapi.py` | 202 |
| `tests/client/test_progress.py` | 70 |
| `tests/client/test_roots.py` | 44 |
| `tests/fs/test_discovery.py` | 353 |
| `tests/utilities/test_cli.py` | 195 |

## config

### Example Files

| Path | Lines |
|---|---:|
| `examples/apps/qr_server/fastmcp.json` | 13 |
| `examples/atproto_mcp/fastmcp.json` | 11 |
| `examples/config_server.py` | 46 |
| `examples/fastmcp_config/env_interpolation_example.json` | 20 |
| `examples/fastmcp_config/fastmcp.json` | 13 |
| `examples/fastmcp_config/full_example.fastmcp.json` | 27 |
| `examples/fastmcp_config/server.py` | 39 |
| `examples/fastmcp_config/simple.fastmcp.json` | 7 |
| `examples/fastmcp_config_demo/README.md` | 55 |
| `examples/fastmcp_config_demo/fastmcp.json` | 14 |
| `examples/fastmcp_config_demo/server.py` | 70 |
| `examples/memory.fastmcp.json` | 7 |
| `examples/screenshot.fastmcp.json` | 7 |
| `examples/smart_home/hub.fastmcp.json` | 9 |
| `examples/smart_home/lights.fastmcp.json` | 9 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/cli/test_config.py` | 461 |
| `tests/cli/test_mcp_server_config_integration.py` | 293 |
| `tests/cli/test_mcp_server_config_schema.py` | 172 |
| `tests/cli/test_run_config.py` | 312 |
| `tests/test_mcp_config.py` | 984 |

## general

### Example Files

| Path | Lines |
|---|---:|
| `examples/apps/qr_server/README.md` | 35 |
| `examples/apps/qr_server/pyproject.toml` | 13 |
| `examples/apps/qr_server/qr_server.py` | 170 |
| `examples/atproto_mcp/README.md` | 156 |
| `examples/atproto_mcp/demo.py` | 260 |
| `examples/atproto_mcp/pyproject.toml` | 24 |
| `examples/atproto_mcp/src/atproto_mcp/__init__.py` | 3 |
| `examples/atproto_mcp/src/atproto_mcp/__main__.py` | 9 |
| `examples/atproto_mcp/src/atproto_mcp/_atproto/__init__.py` | 20 |
| `examples/atproto_mcp/src/atproto_mcp/_atproto/_posts.py` | 420 |
| `examples/atproto_mcp/src/atproto_mcp/_atproto/_profile.py` | 33 |
| `examples/atproto_mcp/src/atproto_mcp/_atproto/_read.py` | 124 |
| `examples/atproto_mcp/src/atproto_mcp/_atproto/_social.py` | 108 |
| `examples/atproto_mcp/src/atproto_mcp/py.typed` | 0 |
| `examples/atproto_mcp/src/atproto_mcp/server.py` | 149 |
| `examples/atproto_mcp/src/atproto_mcp/settings.py` | 17 |
| `examples/atproto_mcp/src/atproto_mcp/types.py` | 142 |
| `examples/complex_inputs.py` | 30 |
| `examples/custom_tool_serializer_decorator.py` | 72 |
| `examples/desktop.py` | 32 |
| `examples/echo.py` | 30 |
| `examples/elicitation.py` | 47 |
| `examples/get_file.py` | 39 |
| `examples/memory.py` | 341 |
| `examples/persistent_state/README.md` | 51 |
| `examples/persistent_state/server.py` | 42 |
| `examples/run_with_tracing.py` | 59 |
| `examples/screenshot.py` | 34 |
| `examples/simple_echo.py` | 14 |
| `examples/skills/README.md` | 104 |
| `examples/skills/download_skills.py` | 82 |
| `examples/skills/sample_skills/code-review/SKILL.md` | 40 |
| `examples/skills/sample_skills/pdf-processing/SKILL.md` | 28 |
| `examples/skills/sample_skills/pdf-processing/reference.md` | 47 |
| `examples/skills/server.py` | 49 |
| `examples/smart_home/README.md` | 15 |
| `examples/smart_home/pyproject.toml` | 19 |
| `examples/smart_home/src/smart_home/__init__.py` | 3 |
| `examples/smart_home/src/smart_home/__main__.py` | 9 |
| `examples/smart_home/src/smart_home/hub.py` | 31 |
| `examples/smart_home/src/smart_home/lights/__init__.py` | 0 |
| `examples/smart_home/src/smart_home/lights/hue_utils.py` | 34 |
| `examples/smart_home/src/smart_home/lights/server.py` | 318 |
| `examples/smart_home/src/smart_home/py.typed` | 0 |
| `examples/smart_home/src/smart_home/settings.py` | 12 |
| `examples/tags_example.py` | 141 |
| `examples/testing_demo/README.md` | 84 |
| `examples/testing_demo/pyproject.toml` | 18 |
| `examples/testing_demo/server.py` | 61 |
| `examples/testing_demo/tests/test_server.py` | 160 |
| `examples/testing_demo/uv.lock` | 1871 |
| `examples/text_me.py` | 72 |
| `examples/tool_result_echo.py` | 41 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/__init__.py` | 0 |
| `tests/conftest.py` | 301 |
| `tests/contrib/__init__.py` | 1 |
| `tests/contrib/test_bulk_tool_caller.py` | 288 |
| `tests/contrib/test_component_manager.py` | 602 |
| `tests/contrib/test_mcp_mixin.py` | 339 |
| `tests/deprecated/__init__.py` | 1 |
| `tests/deprecated/conftest.py` | 9 |
| `tests/deprecated/openapi/test_openapi.py` | 170 |
| `tests/deprecated/server/__init__.py` | 1 |
| `tests/deprecated/server/test_include_exclude_tags.py` | 25 |
| `tests/deprecated/test_deprecated.py` | 23 |
| `tests/deprecated/test_exclude_args.py` | 122 |
| `tests/deprecated/test_function_component_imports.py` | 121 |
| `tests/deprecated/test_import_server.py` | 714 |
| `tests/deprecated/test_openapi_deprecations.py` | 53 |
| `tests/deprecated/test_settings.py` | 64 |
| `tests/deprecated/test_tool_serializer.py` | 181 |
| `tests/experimental/__init__.py` | 0 |
| `tests/integration_tests/__init__.py` | 0 |
| `tests/integration_tests/conftest.py` | 72 |
| `tests/integration_tests/test_github_mcp_remote.py` | 123 |
| `tests/integration_tests/test_timeout_fix.py` | 51 |
| `tests/server/__init__.py` | 0 |
| `tests/server/test_app_state.py` | 26 |
| `tests/server/test_context.py` | 498 |
| `tests/server/test_dependencies.py` | 1159 |
| `tests/server/test_event_store.py` | 238 |
| `tests/server/test_file_server.py` | 134 |
| `tests/server/test_icons.py` | 342 |
| `tests/server/test_input_validation.py` | 365 |
| `tests/server/test_log_level.py` | 90 |
| `tests/server/test_pagination.py` | 436 |
| `tests/server/test_run_server.py` | 98 |
| `tests/server/test_server.py` | 436 |
| `tests/server/test_server_docket.py` | 227 |
| `tests/server/test_server_lifespan.py` | 507 |
| `tests/server/test_tool_annotations.py` | 255 |
| `tests/test_apps.py` | 552 |
| `tests/test_json_schema_generation.py` | 231 |
| `tests/tools/__init__.py` | 0 |
| `tests/tools/test_standalone_decorator.py` | 138 |
| `tests/tools/test_tool_future_annotations.py` | 170 |
| `tests/tools/test_tool_timeout.py` | 192 |
| `tests/tools/tool/__init__.py` | 0 |
| `tests/tools/tool/test_callable.py` | 102 |
| `tests/tools/tool/test_content.py` | 550 |
| `tests/tools/tool/test_output_schema.py` | 534 |
| `tests/tools/tool/test_results.py` | 184 |
| `tests/tools/tool/test_title.py` | 95 |
| `tests/tools/tool/test_tool.py` | 606 |
| `tests/utilities/__init__.py` | 1 |
| `tests/utilities/json_schema_type/__init__.py` | 0 |
| `tests/utilities/json_schema_type/test_advanced.py` | 913 |
| `tests/utilities/json_schema_type/test_constraints.py` | 132 |
| `tests/utilities/json_schema_type/test_containers.py` | 201 |
| `tests/utilities/json_schema_type/test_formats.py` | 114 |
| `tests/utilities/json_schema_type/test_json_schema_type.py` | 170 |
| `tests/utilities/json_schema_type/test_unions.py` | 128 |
| `tests/utilities/openapi/__init__.py` | 1 |
| `tests/utilities/openapi/conftest.py` | 222 |
| `tests/utilities/openapi/test_allof_requestbody.py` | 227 |
| `tests/utilities/openapi/test_direct_array_schemas.py` | 323 |
| `tests/utilities/openapi/test_director.py` | 462 |
| `tests/utilities/openapi/test_legacy_compatibility.py` | 192 |
| `tests/utilities/openapi/test_models.py` | 478 |
| `tests/utilities/openapi/test_nullable_fields.py` | 385 |
| `tests/utilities/openapi/test_parser.py` | 460 |
| `tests/utilities/openapi/test_schemas.py` | 644 |
| `tests/utilities/openapi/test_transitive_references.py` | 842 |
| `tests/utilities/test_components.py` | 417 |
| `tests/utilities/test_inspect.py` | 1111 |
| `tests/utilities/test_json_schema.py` | 630 |
| `tests/utilities/test_skills.py` | 269 |
| `tests/utilities/test_tests.py` | 10 |
| `tests/utilities/test_typeadapter.py` | 273 |
| `tests/utilities/test_types.py` | 673 |

## middleware-logging

### Example Files

| Path | Lines |
|---|---:|
| _none_ | 0 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/server/middleware/__init__.py` | 0 |
| `tests/server/middleware/test_caching.py` | 633 |
| `tests/server/middleware/test_dereference.py` | 136 |
| `tests/server/middleware/test_error_handling.py` | 638 |
| `tests/server/middleware/test_initialization_middleware.py` | 432 |
| `tests/server/middleware/test_logging.py` | 654 |
| `tests/server/middleware/test_middleware.py` | 1129 |
| `tests/server/middleware/test_ping.py` | 241 |
| `tests/server/middleware/test_rate_limiting.py` | 457 |
| `tests/server/middleware/test_response_limiting.py` | 155 |
| `tests/server/middleware/test_timing.py` | 305 |
| `tests/server/middleware/test_tool_injection.py` | 509 |
| `tests/server/test_logging.py` | 192 |
| `tests/utilities/test_logging.py` | 100 |

## prompts

### Example Files

| Path | Lines |
|---|---:|
| `examples/prompts_as_tools/client.py` | 77 |
| `examples/prompts_as_tools/server.py` | 86 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/prompts/__init__.py` | 0 |
| `tests/prompts/test_prompt.py` | 688 |
| `tests/prompts/test_standalone_decorator.py` | 138 |

## providers-composition

### Example Files

| Path | Lines |
|---|---:|
| `examples/filesystem-provider/mcp/prompts/assistant.py` | 39 |
| `examples/filesystem-provider/mcp/resources/config.py` | 55 |
| `examples/filesystem-provider/mcp/tools/calculator.py` | 24 |
| `examples/filesystem-provider/mcp/tools/greeting.py` | 28 |
| `examples/filesystem-provider/server.py` | 29 |
| `examples/in_memory_proxy_example.py` | 82 |
| `examples/mount_example.fastmcp.json` | 4 |
| `examples/mount_example.py` | 111 |
| `examples/providers/sqlite/README.md` | 59 |
| `examples/providers/sqlite/server.py` | 137 |
| `examples/providers/sqlite/setup_db.py` | 102 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/fs/test_provider.py` | 421 |
| `tests/server/mount/__init__.py` | 0 |
| `tests/server/mount/test_advanced.py` | 489 |
| `tests/server/mount/test_filtering.py` | 101 |
| `tests/server/mount/test_mount.py` | 542 |
| `tests/server/mount/test_prompts.py` | 50 |
| `tests/server/mount/test_proxy.py` | 306 |
| `tests/server/mount/test_resources.py` | 136 |
| `tests/server/providers/__init__.py` | 0 |
| `tests/server/providers/local_provider_tools/__init__.py` | 0 |
| `tests/server/providers/local_provider_tools/test_context.py` | 162 |
| `tests/server/providers/local_provider_tools/test_decorator.py` | 341 |
| `tests/server/providers/local_provider_tools/test_enabled.py` | 132 |
| `tests/server/providers/local_provider_tools/test_local_provider_tools.py` | 274 |
| `tests/server/providers/local_provider_tools/test_output_schema.py` | 284 |
| `tests/server/providers/local_provider_tools/test_parameters.py` | 416 |
| `tests/server/providers/local_provider_tools/test_tags.py` | 99 |
| `tests/server/providers/openapi/__init__.py` | 1 |
| `tests/server/providers/openapi/test_comprehensive.py` | 960 |
| `tests/server/providers/openapi/test_deepobject_style.py` | 346 |
| `tests/server/providers/openapi/test_end_to_end_compatibility.py` | 221 |
| `tests/server/providers/openapi/test_openapi_features.py` | 984 |
| `tests/server/providers/openapi/test_openapi_performance.py` | 137 |
| `tests/server/providers/openapi/test_parameter_collisions.py` | 225 |
| `tests/server/providers/openapi/test_performance_comparison.py` | 286 |
| `tests/server/providers/openapi/test_server.py` | 311 |
| `tests/server/providers/proxy/__init__.py` | 0 |
| `tests/server/providers/proxy/test_proxy_client.py` | 430 |
| `tests/server/providers/proxy/test_proxy_server.py` | 734 |
| `tests/server/providers/proxy/test_stateful_proxy_client.py` | 201 |
| `tests/server/providers/test_base_provider.py` | 91 |
| `tests/server/providers/test_fastmcp_provider.py` | 446 |
| `tests/server/providers/test_local_provider.py` | 834 |
| `tests/server/providers/test_local_provider_prompts.py` | 481 |
| `tests/server/providers/test_local_provider_resources.py` | 984 |
| `tests/server/providers/test_skills_provider.py` | 644 |
| `tests/server/providers/test_skills_vendor_providers.py` | 201 |
| `tests/server/providers/test_transforming_provider.py` | 299 |
| `tests/server/telemetry/test_provider_tracing.py` | 133 |
| `tests/server/test_providers.py` | 448 |
| `tests/server/versioning/test_mounting.py` | 343 |

## resources

### Example Files

| Path | Lines |
|---|---:|
| `examples/resources_as_tools/client.py` | 52 |
| `examples/resources_as_tools/server.py` | 65 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/resources/__init__.py` | 0 |
| `tests/resources/test_file_resources.py` | 121 |
| `tests/resources/test_function_resources.py` | 334 |
| `tests/resources/test_resource_template.py` | 1089 |
| `tests/resources/test_resource_template_meta.py` | 25 |
| `tests/resources/test_resources.py` | 356 |
| `tests/resources/test_standalone_decorator.py` | 154 |

## sampling

### Example Files

| Path | Lines |
|---|---:|
| `examples/sampling/README.md` | 62 |
| `examples/sampling/server_fallback.py` | 88 |
| `examples/sampling/structured_output.py` | 110 |
| `examples/sampling/text.py` | 78 |
| `examples/sampling/tool_use.py` | 125 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/client/sampling/__init__.py` | 0 |
| `tests/client/sampling/handlers/__init__.py` | 0 |
| `tests/client/sampling/handlers/test_anthropic_handler.py` | 247 |
| `tests/client/sampling/handlers/test_openai_handler.py` | 100 |
| `tests/client/test_sampling.py` | 1488 |
| `tests/server/sampling/__init__.py` | 0 |
| `tests/server/sampling/test_prepare_tools.py` | 111 |
| `tests/server/sampling/test_sampling_tool.py` | 292 |

## tasks

### Example Files

| Path | Lines |
|---|---:|
| `examples/task_elicitation.py` | 82 |
| `examples/tasks/.envrc` | 10 |
| `examples/tasks/README.md` | 60 |
| `examples/tasks/client.py` | 160 |
| `examples/tasks/docker-compose.yml` | 10 |
| `examples/tasks/server.py` | 75 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/cli/test_tasks.py` | 51 |
| `tests/client/tasks/test_client_prompt_tasks.py` | 102 |
| `tests/client/tasks/test_client_resource_tasks.py` | 107 |
| `tests/client/tasks/test_client_task_notifications.py` | 209 |
| `tests/client/tasks/test_client_task_protocol.py` | 85 |
| `tests/client/tasks/test_client_tool_tasks.py` | 87 |
| `tests/client/tasks/test_task_context_validation.py` | 210 |
| `tests/client/tasks/test_task_result_caching.py` | 325 |
| `tests/server/tasks/__init__.py` | 1 |
| `tests/server/tasks/test_context_background_task.py` | 442 |
| `tests/server/tasks/test_custom_subclass_tasks.py` | 184 |
| `tests/server/tasks/test_notifications.py` | 148 |
| `tests/server/tasks/test_progress_dependency.py` | 155 |
| `tests/server/tasks/test_resource_task_meta_parameter.py` | 287 |
| `tests/server/tasks/test_server_tasks_parameter.py` | 388 |
| `tests/server/tasks/test_sync_function_task_disabled.py` | 229 |
| `tests/server/tasks/test_task_capabilities.py` | 44 |
| `tests/server/tasks/test_task_config.py` | 393 |
| `tests/server/tasks/test_task_dependencies.py` | 273 |
| `tests/server/tasks/test_task_elicitation_relay.py` | 191 |
| `tests/server/tasks/test_task_meta_parameter.py` | 314 |
| `tests/server/tasks/test_task_metadata.py` | 63 |
| `tests/server/tasks/test_task_methods.py` | 217 |
| `tests/server/tasks/test_task_mount.py` | 965 |
| `tests/server/tasks/test_task_prompts.py` | 91 |
| `tests/server/tasks/test_task_protocol.py` | 81 |
| `tests/server/tasks/test_task_proxy.py` | 169 |
| `tests/server/tasks/test_task_resources.py` | 107 |
| `tests/server/tasks/test_task_return_types.py` | 662 |
| `tests/server/tasks/test_task_security.py` | 47 |
| `tests/server/tasks/test_task_status_notifications.py` | 160 |
| `tests/server/tasks/test_task_tools.py` | 101 |
| `tests/server/tasks/test_task_ttl.py` | 87 |

## telemetry-observability

### Example Files

| Path | Lines |
|---|---:|
| `examples/diagnostics/server.py` | 125 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/server/telemetry/__init__.py` | 1 |
| `tests/server/telemetry/test_server_tracing.py` | 340 |
| `tests/telemetry/__init__.py` | 1 |
| `tests/telemetry/test_module.py` | 83 |

## transforms-versioning

### Example Files

| Path | Lines |
|---|---:|
| `examples/namespace_activation/README.md` | 55 |
| `examples/namespace_activation/client.py` | 76 |
| `examples/namespace_activation/server.py` | 73 |
| `examples/versioning/client_version_selection.py` | 81 |
| `examples/versioning/version_filters.py` | 91 |
| `examples/versioning/versioned_components.py` | 101 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/deprecated/test_add_tool_transformation.py` | 79 |
| `tests/server/test_session_visibility.py` | 768 |
| `tests/server/test_tool_transformation.py` | 285 |
| `tests/server/transforms/test_prompts_as_tools.py` | 210 |
| `tests/server/transforms/test_resources_as_tools.py` | 227 |
| `tests/server/transforms/test_visibility.py` | 275 |
| `tests/server/versioning/__init__.py` | 0 |
| `tests/server/versioning/test_calls.py` | 361 |
| `tests/server/versioning/test_filtering.py` | 492 |
| `tests/server/versioning/test_versioning.py` | 258 |
| `tests/tools/tool_transform/__init__.py` | 0 |
| `tests/tools/tool_transform/test_args.py` | 456 |
| `tests/tools/tool_transform/test_metadata.py` | 244 |
| `tests/tools/tool_transform/test_schemas.py` | 555 |
| `tests/tools/tool_transform/test_tool_transform.py` | 606 |
| `tests/utilities/test_version_check.py` | 315 |

## transports

### Example Files

| Path | Lines |
|---|---:|
| `examples/persistent_state/client_stdio.py` | 88 |

### Test Files

| Path | Lines |
|---|---:|
| `tests/client/client/test_transport.py` | 137 |
| `tests/client/test_sse.py` | 200 |
| `tests/client/test_stdio.py` | 364 |
| `tests/client/test_streamable_http.py` | 291 |
| `tests/client/transports/__init__.py` | 0 |
| `tests/client/transports/test_transports.py` | 42 |
| `tests/client/transports/test_uv_transport.py` | 120 |
| `tests/server/http/__init__.py` | 0 |
| `tests/server/http/test_custom_routes.py` | 105 |
| `tests/server/http/test_http_dependencies.py` | 168 |
| `tests/server/http/test_http_middleware.py` | 234 |
| `tests/server/http/test_stale_access_token.py` | 159 |
| `tests/server/test_streamable_http_no_redirect.py` | 85 |

