<p align="center"><img src="icon.png" width="96" alt="Edgepedia"></p>

# Edgepedia MCP server

The official MCP server for [Edgepedia](https://www.edgechat.ai/edgepedia), a free encyclopedia by [EdgeChat](https://www.edgechat.ai): over 300k articles with citations, and constantly growing. It lets an AI assistant search Edgepedia and read whole articles.

**Address:** `https://www.edgechat.ai/mcp` (Streamable HTTP). No key, no sign-up, read-only.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23121636.svg)](https://doi.org/10.5281/zenodo.23121636)

Listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=ai.edgechat/edgepedia) as `ai.edgechat/edgepedia`.

## Corpus 1.6

[Edgepedia 1.6, released October 11, 2026](https://www.edgechat.ai/edgepedia/updates#2026-10-11), adds 14,827 articles on Nobel laureates and other leading thinkers, religion, and economics, and rewrites 10,118 more. Edgepedia now holds 381,770 articles. [Edgepedia 1.6.1](https://www.edgechat.ai/edgepedia/updates#1.6.1), the same day, adds 132,755 links from articles to the articles they mention, which `connect` follows. The current release is [Edgepedia 1.6.3](https://www.edgechat.ai/edgepedia/updates#1.6.3) (October 12, 2026), which removes potential private information of living individuals.

Inspect [the API root](https://www.edgechat.ai/api/v1) for current `corpus_version`, `corpus_updated`, and `release_notes` metadata. The MCP initialization instructions include the same metadata. Corpus releases and MCP package versions are independent: corpus 1.6 does not mean MCP package version 1.6.

## Connect

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Edgepedia-0098FF?logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=edgepedia&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fwww.edgechat.ai%2Fmcp%22%7D) [![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=edgepedia&config=eyJ1cmwiOiJodHRwczovL3d3dy5lZGdlY2hhdC5haS9tY3AifQ%3D%3D)

**Claude Code**
```bash
claude mcp add --transport http edgepedia https://www.edgechat.ai/mcp
```

**Claude (web and desktop):** Settings → Connectors → Add custom connector → `https://www.edgechat.ai/mcp`

**ChatGPT** (paid plans): turn on Developer mode (Settings → Security and login), then Plugins → + → New Plugin → Server URL `https://www.edgechat.ai/mcp`, Authentication: No Auth. In a chat, type `@Edgepedia`.

**Cursor** (`~/.cursor/mcp.json`)
```json
{ "mcpServers": { "edgepedia": { "url": "https://www.edgechat.ai/mcp" } } }
```

**VS Code** (`.vscode/mcp.json`)
```json
{ "servers": { "edgepedia": { "type": "http", "url": "https://www.edgechat.ai/mcp" } } }
```

**Gemini CLI**
```bash
gemini extensions install https://github.com/EdgePlat/edgepedia-mcp
```

**Any other client:** add `https://www.edgechat.ai/mcp` as a Streamable HTTP server.

## Tools

| Tool | Input | Returns |
|---|---|---|
| `search` | `query`: a subject's name, not a question | Matching articles: id, title, link, and the published summary, falling back to the article opening when no summary is available. Other names and misspellings work ("Zhu Yuanzhang" finds the Hongwu Emperor). Words that name a topic ("science fiction writers") also return that topic. |
| `fetch` | `id`: an article's or topic's id; `citations` (optional) | One article as Markdown, with its link, date, topic, license, and credit line. `citations: false` swaps inline source links for `[n]` markers, about a quarter shorter. A topic's id lists its articles. Optional: up to 10 ids at once, one section, a token budget, or only the passages that match your words. |
| `related` | `id`: an article's id | Articles related to it: its topic-mates, a few from each neighboring topic, and its geography neighbors. |
| `connect` | `from`, `to`: two article ids | The shortest chain of in-text links from one article to the other (at most 6 hops), with the sentence that makes each hop. |
| `resolve` | `name`, and optionally `context`: words from the text around it | Which article a name means, with a confidence and the alternatives ("Jaguar" beside "British car maker" is Jaguar Land Rover; beside "big cat" it is the animal). |

All five tools are annotated read-only. Try asking:

- *When did Mount Fuji last erupt? Use Edgepedia.*
- *Who was Zhu Yuanzhang? Use Edgepedia.*
- *How is Marie Curie connected to Mount Fuji? Use Edgepedia.*
- *Give me the credit line for Edgepedia's Marie Curie article.*

## Reference cards

Use the [reference-card builder](https://www.edgechat.ai/developers#reference-cards) to find an article, choose automatic, light, or dark appearance, and copy its embed code. Each card shows the title, complete published summary, Edgepedia credit, and a link to the full article. The optional sizing script adjusts the iframe height; without it, the card remains readable and scrollable.

The standalone [HTML example](examples/reference-card.html) embeds [Cantor's diagonal argument](https://www.edgechat.ai/embed/ep9kcz7eym?theme=auto), using canonical article ID `ep9kcz7eym`:

```html
<iframe data-edgepedia-card src="https://www.edgechat.ai/embed/ep9kcz7eym?theme=auto"
  title="Edgepedia: Cantor&#39;s diagonal argument" loading="lazy" referrerpolicy="no-referrer"
  sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"
  style="width:100%;height:360px;border:0"></iframe>
<script async src="https://www.edgechat.ai/assets/edgepedia-embed.js" referrerpolicy="no-referrer"></script>
```

## No MCP client?

- **Plain JSON API**, same reads: [www.edgechat.ai/developers](https://www.edgechat.ai/developers) ([OpenAPI](https://www.edgechat.ai/openapi.json)). Every article is also Markdown at its own address: [www.edgechat.ai/koala.md](https://www.edgechat.ai/koala.md).
- **Agent Skill:** [`skills/edgepedia/SKILL.md`](skills/edgepedia/SKILL.md) teaches an agent to use that API.
- **Examples** in [`examples/`](examples): `curl`, Python, and JavaScript, with no dependencies.

## Limits

600 calls a minute and 100,000 a day per IP address, for the API and the MCP server alike. Please cache.

## License

Articles are under the [Edgepedia Community License 1.0](https://www.edgechat.ai/edgepedia/license): free with credit, commercial use included, and AI training is open to everyone. For other uses, organizations over USD 100 million in revenue or 100 million monthly users license separately. Show each article's `credit` line, with its link, wherever you show its text.

This repository's own files (documentation, configuration, and examples) are under the [MIT License](LICENSE).

## Links

- Read Edgepedia: [www.edgechat.ai/edgepedia](https://www.edgechat.ai/edgepedia)
- What's new: [www.edgechat.ai/edgepedia/updates](https://www.edgechat.ai/edgepedia/updates)
- Edgepedia on your Mac, offline, in EdgeChat: [www.edgechat.ai/download](https://www.edgechat.ai/download)
- Something broken? [Report it](https://www.edgechat.ai/bugreport), or open an issue here.
- Privacy: [www.edgechat.ai/privacy](https://www.edgechat.ai/privacy)
