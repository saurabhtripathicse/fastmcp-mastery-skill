# Snippet Library

All snippets are intentionally minimal and designed for quick adaptation.

## 1) Minimal Server With One Tool

```python
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## 2) Add Resource And Prompt

```python
from fastmcp import FastMCP

mcp = FastMCP("Data Server")

@mcp.resource("data://config")
def config() -> dict[str, str]:
    return {"env": "dev", "region": "us"}

@mcp.prompt
def summarize(topic: str) -> str:
    return f"Summarize the current state of: {topic}"
```

## 3) Run Server Over HTTP

```python
from fastmcp import FastMCP

mcp = FastMCP("Remote Server")

@mcp.tool
def health() -> str:
    return "ok"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
```

## 4) Async Client Tool Call

```python
import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def main() -> None:
    async with client:
        result = await client.call_tool("add", {"a": 2, "b": 3})
        print(result)

asyncio.run(main())
```

## 5) Run Server Via CLI

```bash
fastmcp run my_server.py:mcp
fastmcp run my_server.py:mcp --transport http --port 8000
```

## 6) Discover And Invoke With CLI

```bash
fastmcp discover
fastmcp list my_server.py
fastmcp call my_server.py add a=2 b=3
```

## 7) Create A Proxy Server

```python
from fastmcp.server.server import create_proxy

# proxy target can be URL, Client, FastMCP instance, script path, or MCP config
proxy = create_proxy("http://localhost:8000/mcp", name="Proxy Server")

if __name__ == "__main__":
    proxy.run()
```

## 8) Basic Test Skeleton

```python
import pytest
from fastmcp import FastMCP, Client

server = FastMCP("Test Server")

@server.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@pytest.mark.anyio
async def test_greet_tool() -> None:
    async with Client(server) as client:
        result = await client.call_tool("greet", {"name": "FastMCP"})
        assert "FastMCP" in str(result)
```

## 9) Strict Input Validation Mode

```python
from fastmcp import FastMCP

mcp = FastMCP("Strict Server", strict_input_validation=True)

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b
```

## 10) Server-Level Pagination

```python
from fastmcp import FastMCP

# list operations return paginated responses when page size is set
mcp = FastMCP("Paged Server", list_page_size=50)
```

## 11) Add Logging Middleware

```python
from fastmcp import FastMCP
from fastmcp.server.middleware.logging import LoggingMiddleware

mcp = FastMCP("Logged Server")
mcp.add_middleware(LoggingMiddleware())
```

## 12) Add Timing Middleware

```python
from fastmcp import FastMCP
from fastmcp.server.middleware.timing import TimingMiddleware

mcp = FastMCP("Timed Server")
mcp.add_middleware(TimingMiddleware())
```

## 13) Add Namespace Transform

```python
from fastmcp import FastMCP
from fastmcp.server.transforms import Namespace

mcp = FastMCP("Transformed Server")
mcp.add_transform(Namespace("api"))
```

## 14) Add Resources-As-Tools Transform

```python
from fastmcp import FastMCP
from fastmcp.server.transforms import ResourcesAsTools

mcp = FastMCP("Resource Tool Server")
mcp.add_transform(ResourcesAsTools())
```

## 15) Add Prompts-As-Tools Transform

```python
from fastmcp import FastMCP
from fastmcp.server.transforms import PromptsAsTools

mcp = FastMCP("Prompt Tool Server")
mcp.add_transform(PromptsAsTools())
```

## 16) Add Filesystem Provider

```python
from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.providers.filesystem import FileSystemProvider

mcp = FastMCP(
    "Filesystem Provider Server",
    providers=[FileSystemProvider(Path(__file__).parent / "mcp", reload=True)],
)
```

## 17) Mount One Server Into Another

```python
from fastmcp import FastMCP

root = FastMCP("Root")
child = FastMCP("Child")

@child.tool
def hello() -> str:
    return "from child"

root.mount(child, namespace="child")
```

## 18) Client Against In-Process Server

```python
import asyncio
from fastmcp import FastMCP, Client

mcp = FastMCP("InProcess")

@mcp.tool
def ping() -> str:
    return "pong"

async def main() -> None:
    async with Client(mcp) as client:
        result = await client.call_tool("ping", {})
        print(result)

asyncio.run(main())
```

## 19) Client Bearer Token Auth

```python
import asyncio
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

client = Client("https://example.com/mcp", auth=BearerAuth("YOUR_TOKEN"))

async def main() -> None:
    async with client:
        print(await client.list_tools())

asyncio.run(main())
```

## 20) Client OAuth Shortcut

```python
import asyncio
from fastmcp import Client

# Uses FastMCP OAuth flow when server requires it
client = Client("https://example.com/mcp", auth="oauth")

async def main() -> None:
    async with client:
        print(await client.list_tools())

asyncio.run(main())
```

## Source Alignment

Before copying snippets into production code, align with:

- `fastmcp-main/src/fastmcp/server/server.py`
- `fastmcp-main/src/fastmcp/client/client.py`
- `fastmcp-main/examples`
- `fastmcp-main/tests`
