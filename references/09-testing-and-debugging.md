# Testing And Debugging

## Test Surface Overview

FastMCP test coverage is broad and should be treated as behavior contracts.

High-volume areas:

- `fastmcp-main/tests/server` (largest surface)
- `fastmcp-main/tests/client`
- `fastmcp-main/tests/utilities`
- `fastmcp-main/tests/tools`
- `fastmcp-main/tests/cli`

## Subsystem Test Mapping

| Subsystem | Test paths |
|---|---|
| Server core | `tests/server/test_*.py` |
| Server auth | `tests/server/auth` |
| Server tasks | `tests/server/tasks` |
| Client core and transports | `tests/client/client`, `tests/client/transports` |
| Client auth | `tests/client/auth` |
| Client sampling/tasks | `tests/client/sampling`, `tests/client/tasks` |
| Tools/resources/prompts | `tests/tools`, `tests/resources`, `tests/prompts` |
| Config and utilities | `tests/test_mcp_config.py`, `tests/utilities` |

## Practical Debugging Flow

1. Reproduce issue with a minimal example from `examples/`.
2. Locate nearest tests by subsystem.
3. Read source module and test side by side.
4. Add/adjust tests before changing implementation.
5. Re-run focused tests, then broader suite.

## Useful Commands

```bash
# Fast search in source/tests
rg "pattern" /Users/saurabhtripathi/project-zero/fastmcp-main/src/fastmcp
rg "pattern" /Users/saurabhtripathi/project-zero/fastmcp-main/tests

# Example: run focused server auth tests
cd /Users/saurabhtripathi/project-zero/fastmcp-main
uv run pytest tests/server/auth -q

# Example: run focused client tests
uv run pytest tests/client -q
```

## Regression Guardrails

- For feature changes, update at least one test in the affected subsystem.
- For docs-code mismatch, prioritize behavior confirmed by tests.
- For integration-specific issues, reproduce with the closest example under `examples/` before patching core modules.
