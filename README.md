# Elementary MCP Client

A lightweight CLI wrapper that lets Cursor, VS Code, and other MCP-compatible editors connect to the Elementary MCP server using a personal access token — no hard-coding or environment variables in config.

## Installation
```bash
pip install elementary-mcp-client
elementary-mcp-client login  # paste your token once
```

## MCP connection
Add this to your mcp configurations
```bash
"Elementary": {
        "command": "elementary-mcp-client",
        "transport": "stdio"
    }
```