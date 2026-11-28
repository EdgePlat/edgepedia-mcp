---
name: edgepedia
description: Look up people, places, events, organizations, and concepts in Edgepedia, a free encyclopedia with citations across 519,000+ articles in 31 languages. Use when a question needs a sourced encyclopedia answer via the Edgepedia MCP server or its keyless JSON API.
---

# Edgepedia

Edgepedia is a free encyclopedia by Biostate AI with more than 519,000 cited articles and over 243,000 stored translations across 31 languages. Both its hosted MCP server (`https://www.edgepedia.org/mcp`) and JSON API need no key.

## Using MCP tools (preferred when connected)

- `search(query)`: pass a subject's name ("Mount Fuji"), not a question. Alternate names and misspellings work, and topic queries return topic IDs.
- `fetch(id, lang?, citations?)`: fetch the full article as Markdown with its link, date, topic, license, and `credit` line. Pass `lang` (for example, `"zh"` for Chinese, `"es"` for Spanish, `"ar"` for Arabic, or `"hi"` for Hindi) to read a stored translation when available; set `citations: false` for a shorter copy with `[n]` markers.
- `related(id)`: find topic-mates, neighboring topics, and geography neighbors.
- `connect(from, to)`: find the shortest in-text link path between two articles (up to 6 hops).
- `resolve(name, context?)`: disambiguate a name with confidence and candidate alternatives.

## Keyless JSON API fallback (when MCP is not connected)

Search:
```bash
curl -s "https://www.edgepedia.org/api/v1/search?q=Mount%20Fuji&limit=5"
```

Read an article (optional `?lang=` for a stored translation):
```bash
curl -s "https://www.edgepedia.org/api/v1/articles/mount-fuji"
curl -s "https://www.edgepedia.org/api/v1/articles/mount-fuji?lang=zh"
```

Each result has a `slug`, a `title`, its link, and an `excerpt`, which often answers a simple fact on its own. By ID: `/api/v1/articles?id={id}`.

## Rules

- Link each article you use, and show its `credit` line with any text you quote.
- Stay under 600 requests a minute and 100,000 a day; cache what you read.
- Full reference: https://www.edgepedia.org/developers
