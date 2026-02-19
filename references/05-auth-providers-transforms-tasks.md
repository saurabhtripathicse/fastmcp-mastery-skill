# Auth, Providers, Transforms, And Tasks

## Authentication And Authorization

### Docs to read

- `fastmcpdocs/servers/auth/authentication.md`
- `fastmcpdocs/servers/auth/token-verification.md`
- `fastmcpdocs/servers/auth/remote-oauth.md`
- `fastmcpdocs/servers/auth/oauth-proxy.md`
- `fastmcpdocs/servers/auth/oidc-proxy.md`
- `fastmcpdocs/servers/auth/full-oauth-server.md`
- `fastmcpdocs/servers/authorization.md`

### Code to inspect

- `fastmcp-main/src/fastmcp/server/auth/auth.py`
- `fastmcp-main/src/fastmcp/server/auth/authorization.py`
- `fastmcp-main/src/fastmcp/server/auth/middleware.py`
- `fastmcp-main/src/fastmcp/server/auth/oidc_proxy.py`
- `fastmcp-main/src/fastmcp/server/auth/oauth_proxy`
- `fastmcp-main/src/fastmcp/server/auth/providers`

### Tests to trust

- `fastmcp-main/tests/server/auth`
- `fastmcp-main/tests/server/auth/providers`
- `fastmcp-main/tests/server/auth/oauth_proxy`

## Providers

Providers supply dynamic tools/resources/prompts and composition patterns.

### Docs to read

- `fastmcpdocs/servers/providers/overview.md`
- `fastmcpdocs/servers/providers/local.md`
- `fastmcpdocs/servers/providers/filesystem.md`
- `fastmcpdocs/servers/providers/proxy.md`
- `fastmcpdocs/servers/providers/skills.md`
- `fastmcpdocs/servers/providers/custom.md`
- `fastmcpdocs/servers/providers/mounting.md`

### Code to inspect

- `fastmcp-main/src/fastmcp/server/providers/base.py`
- `fastmcp-main/src/fastmcp/server/providers/aggregate.py`
- `fastmcp-main/src/fastmcp/server/providers/local_provider/local_provider.py`
- `fastmcp-main/src/fastmcp/server/providers/filesystem.py`
- `fastmcp-main/src/fastmcp/server/providers/proxy.py`
- `fastmcp-main/src/fastmcp/server/providers/skills`
- `fastmcp-main/src/fastmcp/server/providers/openapi/provider.py`

### Examples

- `fastmcp-main/examples/providers/sqlite/server.py`
- `fastmcp-main/examples/filesystem-provider/server.py`
- `fastmcp-main/examples/mount_example.py`

## Transforms And Visibility

### Docs to read

- `fastmcpdocs/servers/transforms/transforms.md`
- `fastmcpdocs/servers/transforms/namespace.md`
- `fastmcpdocs/servers/transforms/tool-transformation.md`
- `fastmcpdocs/servers/transforms/resources-as-tools.md`
- `fastmcpdocs/servers/transforms/prompts-as-tools.md`
- `fastmcpdocs/servers/visibility.md`
- `fastmcpdocs/servers/versioning.md`

### Code to inspect

- `fastmcp-main/src/fastmcp/server/transforms/namespace.py`
- `fastmcp-main/src/fastmcp/server/transforms/tool_transform.py`
- `fastmcp-main/src/fastmcp/server/transforms/resources_as_tools.py`
- `fastmcp-main/src/fastmcp/server/transforms/prompts_as_tools.py`
- `fastmcp-main/src/fastmcp/server/transforms/version_filter.py`
- `fastmcp-main/src/fastmcp/server/transforms/visibility.py`

### Examples

- `fastmcp-main/examples/namespace_activation/server.py`
- `fastmcp-main/examples/prompts_as_tools/server.py`
- `fastmcp-main/examples/resources_as_tools/server.py`

## Tasks And Long-Running Work

### Docs to read

- `fastmcpdocs/servers/tasks.md`
- `fastmcpdocs/servers/progress.md`
- `fastmcpdocs/servers/elicitation.md`
- `fastmcpdocs/clients/tasks.md`
- `fastmcpdocs/clients/notifications.md`

### Code to inspect

- `fastmcp-main/src/fastmcp/server/tasks`
- `fastmcp-main/src/fastmcp/client/tasks.py`
- `fastmcp-main/src/fastmcp/server/elicitation.py`
- `fastmcp-main/src/fastmcp/client/elicitation.py`

### Examples

- `fastmcp-main/examples/tasks/server.py`
- `fastmcp-main/examples/tasks/client.py`
- `fastmcp-main/examples/task_elicitation.py`

### Tests

- `fastmcp-main/tests/server/tasks`
- `fastmcp-main/tests/client/tasks`
