# Intent To Workflow Map

Use this map to convert user requests into deterministic FastMCP execution steps.

## Build A New Server

1. Read: `fastmcpdocs/getting-started/quickstart.md`
2. Read: `references/03-server-playbook.md`
3. Base example: `fastmcp-main/examples/simple_echo.py`
4. Validate with: `fastmcp-main/tests/server`

## Add Auth To Existing Server

1. Read: `fastmcpdocs/servers/auth/authentication.md`
2. Read: `references/05-auth-providers-transforms-tasks.md`
3. Base examples: `fastmcp-main/examples/auth/*`
4. Validate with: `fastmcp-main/tests/server/auth`

## Add Providers Or Composition

1. Read: `fastmcpdocs/servers/providers/overview.md`
2. Read: `fastmcpdocs/servers/providers/mounting.md`
3. Base examples: `fastmcp-main/examples/mount_example.py`, `fastmcp-main/examples/providers/sqlite/server.py`
4. Validate with: `fastmcp-main/tests/server/test_providers.py`

## Add Tasks / Long Running Work

1. Read: `fastmcpdocs/servers/tasks.md`
2. Read: `fastmcpdocs/clients/tasks.md`
3. Base examples: `fastmcp-main/examples/tasks/server.py`, `fastmcp-main/examples/tasks/client.py`
4. Validate with: `fastmcp-main/tests/server/tasks`, `fastmcp-main/tests/client/tasks`

## Add Transforms / Visibility / Versioning

1. Read: `fastmcpdocs/servers/transforms/transforms.md`
2. Read: `fastmcpdocs/servers/visibility.md`
3. Base examples: `fastmcp-main/examples/namespace_activation/server.py`, `fastmcp-main/examples/versioning/version_filters.py`
4. Validate with transform and visibility tests under `fastmcp-main/tests/server`

## Build Client Integrations

1. Read: `fastmcpdocs/clients/client.md`
2. Read: `fastmcpdocs/clients/transports.md`
3. Read: `references/04-client-playbook.md`
4. Validate with: `fastmcp-main/tests/client`

## Use FastMCP CLI For Operations

1. Read: `fastmcpdocs/clients/cli.md`
2. Read: `references/06-cli-config-deployment-integrations.md`
3. Validate with: `fastmcp-main/tests/cli`

## Debug Docs/Code Mismatch

1. Find docs page in: `references/10-guides-full-index-generated.md`
2. Find source module in: `references/02-doc-code-crosswalk-generated.md`
3. Find linked API symbols in: `references/11-python-sdk-full-index-generated.md`
4. Confirm expected behavior from tests in: `references/13-examples-tests-matrix-generated.md`
