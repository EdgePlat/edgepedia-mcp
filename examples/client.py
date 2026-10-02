"""Search Edgepedia and read an article through its MCP server. Python 3 standard library only."""
import json
import sys
import urllib.request

URL = "https://www.edgechat.ai/mcp"


def call(tool, arguments):
    body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool, "arguments": arguments}}
    request = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "MCP-Protocol-Version": "2025-06-18",
    })
    with urllib.request.urlopen(request) as response:
        result = json.load(response)["result"]
    return json.loads(result["content"][0]["text"])


subject = " ".join(sys.argv[1:]) or "Mount Fuji"
first = call("search", {"query": subject})["results"][0]
print(first["title"], first["url"])
article = call("fetch", {"id": first["id"], "citations": False})
print(article["text"][:600])
print("\n" + article["metadata"]["credit"])
