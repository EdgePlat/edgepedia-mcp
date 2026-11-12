<p align="center"><img src="icon.png" width="96" alt="Edgepedia"></p>

# Edgepedia MCP server

The official MCP server for [Edgepedia](https://www.edgepedia.org), a free encyclopedia by [Biostate AI](https://www.biostate.ai/): more than 500,000 articles with citations, and constantly growing. It lets an AI assistant search Edgepedia and read whole articles.

**Address:** `https://www.edgepedia.org/mcp` (Streamable HTTP). No key, no sign-up, read-only.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23121636.svg)](https://doi.org/10.5281/zenodo.23121636)

Listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=ai.edgechat/edgepedia) as `ai.edgechat/edgepedia`.

## Corpus 1.9

The current release is [Edgepedia 1.9.2](https://www.edgepedia.org/edgepedia/updates#1.9.2) (November 11, 2026), which corrects references, uniformly applies Simplified Chinese, and counts how often each article is mentioned, so search ranks better. It follows [Edgepedia 1.9.1](https://www.edgepedia.org/edgepedia/updates#1.9.1) (November 1, 2026), which put plots back behind the Spoilers section in 24,257 film and series articles; Edgepedia holds 519,064 articles.

Earlier releases: [Edgepedia updates](https://www.edgepedia.org/edgepedia/updates).

Inspect [the API root](https://www.edgepedia.org/api/v1) for current `corpus_version`, `corpus_updated`, and `release_notes` metadata. The MCP initialization instructions include the same metadata. Corpus releases and MCP package versions are independent: corpus 1.9 does not mean MCP package version 1.9.

## Connect

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Edgepedia-0098FF?logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=edgepedia&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fwww.edgepedia.org%2Fmcp%22%7D) [![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=edgepedia&config=eyJ1cmwiOiJodHRwczovL3d3dy5lZGdlcGVkaWEub3JnL21jcCJ9)

**Claude Code**
```bash
claude mcp add --transport http edgepedia https://www.edgepedia.org/mcp
```

**Claude (web and desktop):** Settings → Connectors → Add custom connector → `https://www.edgepedia.org/mcp`

**ChatGPT** (paid plans): turn on Developer mode (Settings → Security and login), then Plugins → + → New Plugin → Server URL `https://www.edgepedia.org/mcp`, Authentication: No Auth. In a chat, type `@Edgepedia`.

**Cursor** (`~/.cursor/mcp.json`)
```json
{ "mcpServers": { "edgepedia": { "url": "https://www.edgepedia.org/mcp" } } }
```

**VS Code** (`.vscode/mcp.json`)
```json
{ "servers": { "edgepedia": { "type": "http", "url": "https://www.edgepedia.org/mcp" } } }
```

**Gemini CLI**
```bash
gemini extensions install https://github.com/EdgePlat/edgepedia-mcp
```

**Any other client:** add `https://www.edgepedia.org/mcp` as a Streamable HTTP server.

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
- *What is Mwindo Fossae on Pluto? Use Edgepedia.*
- *Who was Zhu Yuanzhang? Use Edgepedia.*
- *How is Marie Curie connected to Mount Fuji? Use Edgepedia.*
- *Give me the credit line for Edgepedia's Marie Curie article.*

## Reference cards

Use the [reference-card builder](https://www.edgepedia.org/developers#reference-cards) to find an article, choose automatic, light, or dark appearance, and copy its embed code. Each card shows the title, complete published summary, Edgepedia credit, and a link to the full article. The optional sizing script adjusts the iframe height; without it, the card remains readable and scrollable.

The standalone [HTML example](examples/reference-card.html) embeds [Cantor's diagonal argument](https://www.edgepedia.org/embed/ep9kcz7eym?theme=auto), using canonical article ID `ep9kcz7eym`:

```html
<iframe data-edgepedia-card src="https://www.edgepedia.org/embed/ep9kcz7eym?theme=auto"
  title="Edgepedia: Cantor&#39;s diagonal argument" loading="lazy" referrerpolicy="no-referrer"
  sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"
  style="width:100%;height:360px;border:0"></iframe>
<script async src="https://www.edgepedia.org/assets/edgepedia-embed.js" referrerpolicy="no-referrer"></script>
```

## No MCP client?

- **Plain JSON API**, same reads: [www.edgepedia.org/developers](https://www.edgepedia.org/developers) ([OpenAPI](https://www.edgepedia.org/openapi.json)). Every article is also Markdown at its own address: [www.edgechat.ai/koala.md](https://www.edgechat.ai/koala.md).
- **Agent Skill:** [`skills/edgepedia/SKILL.md`](skills/edgepedia/SKILL.md) teaches an agent to use that API.
- **Examples** in [`examples/`](examples): `curl`, Python, and JavaScript, with no dependencies.

## Limits

600 calls a minute and 100,000 a day per IP address, for the API and the MCP server alike. Please cache.

## License

Articles are under the [Edgepedia Community License 1.0](https://www.edgepedia.org/edgepedia/license): free with credit, commercial use included, and AI training is open to everyone. For other uses, organizations over USD 100 million in revenue or 100 million monthly users license separately. Show each article's `credit` line, with its link, wherever you show its text.

This repository's own files (documentation, configuration, and examples) are under the [MIT License](LICENSE).

## Links

- Read Edgepedia: [www.edgepedia.org](https://www.edgepedia.org)
- What's new: [www.edgepedia.org/edgepedia/updates](https://www.edgepedia.org/edgepedia/updates)
- Edgepedia offline, in EdgeChat: [www.edgechat.ai/download](https://www.edgechat.ai/download)
- Something broken? [Report it](https://www.edgechat.ai/bugreport), or open an issue here.
- Privacy: [www.edgepedia.org/edgepedia/privacy](https://www.edgepedia.org/edgepedia/privacy)
