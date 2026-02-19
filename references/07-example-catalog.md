# Example Catalog

## Core Entry Examples

| Path | Demonstrates |
|---|---|
| `examples/simple_echo.py` | Minimal server with a simple tool |
| `examples/echo.py` | Basic tool calls and server setup |
| `examples/config_server.py` | Config-backed server pattern |
| `examples/text_me.py` | Tool behavior with external effects pattern |

## Composition And Providers

| Path | Demonstrates |
|---|---|
| `examples/mount_example.py` | Mounting and composition |
| `examples/in_memory_proxy_example.py` | Proxying between server/client in memory |
| `examples/filesystem-provider/server.py` | Filesystem provider usage |
| `examples/providers/sqlite/server.py` | Custom/provider-backed data source |

## Config And Runtime

| Path | Demonstrates |
|---|---|
| `examples/fastmcp_config/server.py` | Reading server config artifacts |
| `examples/fastmcp_config/*.json` | Config schema variants |
| `examples/fastmcp_config_demo/server.py` | End-to-end config demo |
| `examples/memory.py` | Stateful server patterns |

## Tasks, Elicitation, And Advanced MCP Features

| Path | Demonstrates |
|---|---|
| `examples/tasks/server.py` | Task-enabled server |
| `examples/tasks/client.py` | Client-side task interaction |
| `examples/task_elicitation.py` | Task elicitation flow |
| `examples/elicitation.py` | Elicitation primitives |

## Transforms And Versioning

| Path | Demonstrates |
|---|---|
| `examples/namespace_activation/server.py` | Namespace transform activation |
| `examples/prompts_as_tools/server.py` | Prompts exposed as tools |
| `examples/resources_as_tools/server.py` | Resources exposed as tools |
| `examples/versioning/version_filters.py` | Version filter transforms |
| `examples/versioning/versioned_components.py` | Versioned component exposure |

## Sampling

| Path | Demonstrates |
|---|---|
| `examples/sampling/text.py` | Text sampling |
| `examples/sampling/tool_use.py` | Tool-use through sampling handlers |
| `examples/sampling/structured_output.py` | Structured output sampling |
| `examples/sampling/server_fallback.py` | Fallback handler behavior |

## Authentication

| Path | Demonstrates |
|---|---|
| `examples/auth/google_oauth/server.py` | Google OAuth provider wiring |
| `examples/auth/github_oauth/server.py` | GitHub OAuth provider wiring |
| `examples/auth/aws_oauth/server.py` | AWS Cognito-style OAuth workflow |
| `examples/auth/azure_oauth/server.py` | Azure auth provider setup |
| `examples/auth/workos_oauth/server.py` | WorkOS OAuth setup |
| `examples/auth/mounted/server.py` | Auth with mounted components |

## Diagnostic And Testing Patterns

| Path | Demonstrates |
|---|---|
| `examples/diagnostics/server.py` | Tracing and diagnostics hooks |
| `examples/diagnostics/client_with_tracing.py` | Client tracing setup |
| `examples/testing_demo/server.py` | Test-focused server design |
