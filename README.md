# Elementary MCP Client

A lightweight CLI wrapper that lets Cursor, VS Code, and other MCP-compatible editors connect to the Elementary MCP server using a personal access token — no hard-coding or environment variables in config.

## Installation
The package is not yet published, so installation must be from the project's directory
```bash
cd elementary-mcp-client
pip install -e .
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