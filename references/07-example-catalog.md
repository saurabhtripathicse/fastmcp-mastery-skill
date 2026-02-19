# Example Catalog

## Core Entry Examples

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/simple_echo.py` | Minimal server with a simple tool |
| `fastmcp-main/examples/echo.py` | Basic tool calls and server setup |
| `fastmcp-main/examples/config_server.py` | Config-backed server pattern |
| `fastmcp-main/examples/text_me.py` | Tool behavior with external effects pattern |

## Composition And Providers

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/mount_example.py` | Mounting and composition |
| `fastmcp-main/examples/in_memory_proxy_example.py` | Proxying between server/client in memory |
| `fastmcp-main/examples/filesystem-provider/server.py` | Filesystem provider usage |
| `fastmcp-main/examples/providers/sqlite/server.py` | Custom/provider-backed data source |

## Config And Runtime

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/fastmcp_config/server.py` | Reading server config artifacts |
| `fastmcp-main/examples/fastmcp_config/*.json` | Config schema variants |
| `fastmcp-main/examples/fastmcp_config_demo/server.py` | End-to-end config demo |
| `fastmcp-main/examples/memory.py` | Stateful server patterns |

## Tasks, Elicitation, And Advanced MCP Features

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/tasks/server.py` | Task-enabled server |
| `fastmcp-main/examples/tasks/client.py` | Client-side task interaction |
| `fastmcp-main/examples/task_elicitation.py` | Task elicitation flow |
| `fastmcp-main/examples/elicitation.py` | Elicitation primitives |

## Transforms And Versioning

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/namespace_activation/server.py` | Namespace transform activation |
| `fastmcp-main/examples/prompts_as_tools/server.py` | Prompts exposed as tools |
| `fastmcp-main/examples/resources_as_tools/server.py` | Resources exposed as tools |
| `fastmcp-main/examples/versioning/version_filters.py` | Version filter transforms |
| `fastmcp-main/examples/versioning/versioned_components.py` | Versioned component exposure |

## Sampling

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/sampling/text.py` | Text sampling |
| `fastmcp-main/examples/sampling/tool_use.py` | Tool-use through sampling handlers |
| `fastmcp-main/examples/sampling/structured_output.py` | Structured output sampling |
| `fastmcp-main/examples/sampling/server_fallback.py` | Fallback handler behavior |

## Authentication

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/auth/google_oauth/server.py` | Google OAuth provider wiring |
| `fastmcp-main/examples/auth/github_oauth/server.py` | GitHub OAuth provider wiring |
| `fastmcp-main/examples/auth/aws_oauth/server.py` | AWS Cognito-style OAuth workflow |
| `fastmcp-main/examples/auth/azure_oauth/server.py` | Azure auth provider setup |
| `fastmcp-main/examples/auth/workos_oauth/server.py` | WorkOS OAuth setup |
| `fastmcp-main/examples/auth/mounted/server.py` | Auth with mounted components |

## Diagnostic And Testing Patterns

| Path | Demonstrates |
|---|---|
| `fastmcp-main/examples/diagnostics/server.py` | Tracing and diagnostics hooks |
| `fastmcp-main/examples/diagnostics/client_with_tracing.py` | Client tracing setup |
| `fastmcp-main/examples/testing_demo/server.py` | Test-focused server design |
