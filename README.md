<p align="center"><img src="icon.png" width="96" alt="Edgepedia"></p>

# Edgepedia MCP server

The official MCP server for [Edgepedia](https://www.edgechat.ai/edgepedia), a free encyclopedia by [EdgeChat](https://www.edgechat.ai): over 300k articles with citations, and constantly growing. It lets an AI assistant search Edgepedia and read whole articles.

**Address:** `https://www.edgechat.ai/mcp` (Streamable HTTP). No key, no sign-up, read-only.

Listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=ai.edgechat/edgepedia) as `ai.edgechat/edgepedia`.

## Connect

**Claude Code**
```bash
claude mcp add --transport http edgepedia https://www.edgechat.ai/mcp
```

**Claude (web and desktop):** Settings → Connectors → Add custom connector → `https://www.edgechat.ai/mcp`

**ChatGPT:** turn on Developer mode (Settings → Security and login), then Plugins → + → Server URL `https://www.edgechat.ai/mcp`, Authentication: No Auth. In a chat, type `@Edgepedia`.

**Cursor** (`~/.cursor/mcp.json`)
```json
{ "mcpServers": { "edgepedia": { "url": "https://www.edgechat.ai/mcp" } } }
```

**VS Code** (`.vscode/mcp.json`)
```json
{ "servers": { "edgepedia": { "type": "http", "url": "https://www.edgechat.ai/mcp" } } }
```

**Any other client:** add `https://www.edgechat.ai/mcp` as a Streamable HTTP server.

## Tools

| Tool | Input | Returns |
|---|---|---|
| `search` | `query`: a subject's name, not a question | Matching articles: id, title, link, and the opening sentences. Other names and misspellings work ("Zhu Yuanzhang" finds the Hongwu Emperor). Words that name a topic ("science fiction writers") also return that topic. |
| `fetch` | `id`: an article's or topic's id; `citations` (optional) | One article as Markdown, with its link, date, topic, license, and credit line. `citations: false` swaps inline source links for `[n]` markers, about a quarter shorter. A topic's id lists its articles. |

Both tools are annotated read-only. Try asking:

- *When did Mount Fuji last erupt? Use Edgepedia.*
- *Who was Zhu Yuanzhang? Use Edgepedia.*
- *Give me the credit line for Edgepedia's Marie Curie article.*

## No MCP client?

- **Plain JSON API**, same reads: [www.edgechat.ai/developers](https://www.edgechat.ai/developers) ([OpenAPI](https://www.edgechat.ai/openapi.json)). Every article is also Markdown at its own address: [www.edgechat.ai/koala.md](https://www.edgechat.ai/koala.md).
- **Agent Skill:** [`skills/edgepedia/SKILL.md`](skills/edgepedia/SKILL.md) teaches an agent to use that API.
- **Examples** in [`examples/`](examples): `curl`, Python, and JavaScript, with no dependencies.

## Limits

600 calls a minute and 100,000 a day per IP address, for the API and the MCP server alike. Please cache.

## License

Articles are under the [Edgepedia Community License 1.0](https://www.edgechat.ai/edgepedia/license): free with credit, commercial use included, and AI training is open to everyone. Show each article's `credit` line, with its link, wherever you show its text.

This repository's own files (documentation, configuration, and examples) are under the [MIT License](LICENSE).

## Links

- Read Edgepedia: [www.edgechat.ai/edgepedia](https://www.edgechat.ai/edgepedia)
- What's new: [www.edgechat.ai/edgepedia/updates](https://www.edgechat.ai/edgepedia/updates)
- Edgepedia on your Mac, offline, in EdgeChat: [www.edgechat.ai/download](https://www.edgechat.ai/download)
- Something broken? [Report it](https://www.edgechat.ai/bugreport), or open an issue here.
- Privacy: [www.edgechat.ai/privacy](https://www.edgechat.ai/privacy)
