# Intent To Workflow Map

Use this map to convert user requests into deterministic FastMCP execution steps.

## Build A New Server

1. Read: `getting-started/quickstart.md`
2. Read: `references/03-server-playbook.md`
3. Base example: `examples/simple_echo.py`
4. Validate with: `tests/server`

## Add Auth To Existing Server

1. Read: `servers/auth/authentication.md`
2. Read: `references/05-auth-providers-transforms-tasks.md`
3. Base examples: `examples/auth/*`
4. Validate with: `tests/server/auth`

## Add Providers Or Composition

1. Read: `servers/providers/overview.md`
2. Read: `servers/providers/mounting.md`
3. Base examples: `examples/mount_example.py`, `examples/providers/sqlite/server.py`
4. Validate with: `tests/server/test_providers.py`

## Add Tasks / Long Running Work

1. Read: `servers/tasks.md`
2. Read: `clients/tasks.md`
3. Base examples: `examples/tasks/server.py`, `examples/tasks/client.py`
4. Validate with: `tests/server/tasks`, `tests/client/tasks`

## Add Transforms / Visibility / Versioning

1. Read: `servers/transforms/transforms.md`
2. Read: `servers/visibility.md`
3. Base examples: `examples/namespace_activation/server.py`, `examples/versioning/version_filters.py`
4. Validate with transform and visibility tests under `tests/server`

## Build Client Integrations

1. Read: `clients/client.md`
2. Read: `clients/transports.md`
3. Read: `references/04-client-playbook.md`
4. Validate with: `tests/client`

## Use FastMCP CLI For Operations

1. Read: `clients/cli.md`
2. Read: `references/06-cli-config-deployment-integrations.md`
3. Validate with: `tests/cli`

## Debug Docs/Code Mismatch

1. Find docs page in: `references/10-guides-full-index-generated.md`
2. Find source module in: `references/02-doc-code-crosswalk-generated.md`
3. Find linked API symbols in: `references/11-python-sdk-full-index-generated.md`
4. Confirm expected behavior from tests in: `references/13-examples-tests-matrix-generated.md`
