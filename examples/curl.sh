#!/bin/sh
# Call the Edgepedia MCP server with curl: list the tools, search, then fetch.
URL=https://www.edgechat.ai/mcp

call() {
  curl -s "$URL" \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json, text/event-stream' \
    -H 'MCP-Protocol-Version: 2025-06-18' \
    -d "$1"
  echo
}

call '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
call '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"search","arguments":{"query":"Mount Fuji"}}}'
call '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"fetch","arguments":{"id":"mount-fuji","citations":false}}}'
