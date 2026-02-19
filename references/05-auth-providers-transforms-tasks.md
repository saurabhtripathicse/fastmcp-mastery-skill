# Auth, Providers, Transforms, And Tasks

## Table of Contents

- [Authentication And Authorization](#authentication-and-authorization)
- [Providers](#providers)
- [Transforms And Visibility](#transforms-and-visibility)
- [Tasks And Long-Running Work](#tasks-and-long-running-work)

## Authentication And Authorization

### Docs to read

- `servers/auth/authentication.md`
- `servers/auth/token-verification.md`
- `servers/auth/remote-oauth.md`
- `servers/auth/oauth-proxy.md`
- `servers/auth/oidc-proxy.md`
- `servers/auth/full-oauth-server.md`
- `servers/authorization.md`

### Code to inspect

- `src/fastmcp/server/auth/auth.py`
- `src/fastmcp/server/auth/authorization.py`
- `src/fastmcp/server/auth/middleware.py`
- `src/fastmcp/server/auth/oidc_proxy.py`
- `src/fastmcp/server/auth/oauth_proxy`
- `src/fastmcp/server/auth/providers`

### Tests to trust

- `tests/server/auth`
- `tests/server/auth/providers`
- `tests/server/auth/oauth_proxy`

## Providers

Providers supply dynamic tools/resources/prompts and composition patterns.

### Docs to read

- `servers/providers/overview.md`
- `servers/providers/local.md`
- `servers/providers/filesystem.md`
- `servers/providers/proxy.md`
- `servers/providers/skills.md`
- `servers/providers/custom.md`
- `servers/providers/mounting.md`

### Code to inspect

- `src/fastmcp/server/providers/base.py`
- `src/fastmcp/server/providers/aggregate.py`
- `src/fastmcp/server/providers/local_provider/local_provider.py`
- `src/fastmcp/server/providers/filesystem.py`
- `src/fastmcp/server/providers/proxy.py`
- `src/fastmcp/server/providers/skills`
- `src/fastmcp/server/providers/openapi/provider.py`

### Examples

- `examples/providers/sqlite/server.py`
- `examples/filesystem-provider/server.py`
- `examples/mount_example.py`

## Transforms And Visibility

### Docs to read

- `servers/transforms/transforms.md`
- `servers/transforms/namespace.md`
- `servers/transforms/tool-transformation.md`
- `servers/transforms/resources-as-tools.md`
- `servers/transforms/prompts-as-tools.md`
- `servers/visibility.md`
- `servers/versioning.md`

### Code to inspect

- `src/fastmcp/server/transforms/namespace.py`
- `src/fastmcp/server/transforms/tool_transform.py`
- `src/fastmcp/server/transforms/resources_as_tools.py`
- `src/fastmcp/server/transforms/prompts_as_tools.py`
- `src/fastmcp/server/transforms/version_filter.py`
- `src/fastmcp/server/transforms/visibility.py`

### Examples

- `examples/namespace_activation/server.py`
- `examples/prompts_as_tools/server.py`
- `examples/resources_as_tools/server.py`

## Tasks And Long-Running Work

### Docs to read

- `servers/tasks.md`
- `servers/progress.md`
- `servers/elicitation.md`
- `clients/tasks.md`
- `clients/notifications.md`

### Code to inspect

- `src/fastmcp/server/tasks`
- `src/fastmcp/client/tasks.py`
- `src/fastmcp/server/elicitation.py`
- `src/fastmcp/client/elicitation.py`

### Examples

- `examples/tasks/server.py`
- `examples/tasks/client.py`
- `examples/task_elicitation.py`

### Tests

- `tests/server/tasks`
- `tests/client/tasks`
