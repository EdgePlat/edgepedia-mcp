# Installing the Edgepedia MCP server

Edgepedia's MCP server is hosted. Nothing installs or runs locally, and it needs no key or account.

- Address: `https://www.edgepedia.org/mcp`
- Transport: Streamable HTTP

## Cline

Add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "edgepedia": {
      "type": "streamableHttp",
      "url": "https://www.edgepedia.org/mcp",
      "disabled": false
    }
  }
}
```

## Check it works

Call `search` with `{"query": "Mount Fuji"}`. The first result has the id `mount-fuji`. Then call `fetch` with `{"id": "mount-fuji"}`: it returns the article as Markdown, with a `credit` line to show with any text you quote.
