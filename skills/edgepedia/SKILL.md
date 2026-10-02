---
name: edgepedia
description: Look up people, places, events, organizations, and concepts in Edgepedia, a free encyclopedia with citations, through its keyless JSON API. Use when a question needs a sourced encyclopedia answer and the Edgepedia MCP server is not connected.
---

# Edgepedia

Edgepedia is a free encyclopedia by EdgeChat: over 300k articles with citations. Its API needs no key.

## Search

```bash
curl -s "https://www.edgechat.ai/api/v1/search?q=Mount%20Fuji&limit=5"
```

Search for a subject's name, not a question. Other names and misspellings work; a misspelling may return `did_you_mean`. Each result has a `slug`, a `title`, its link, and an `excerpt` (the opening sentences), which often answers a simple fact on its own.

## Read an article

```bash
curl -s "https://www.edgechat.ai/api/v1/articles/mount-fuji"
```

Use a result's `slug`. Returns the article as Markdown, its topic path, its last-updated date, and its `credit` line. By id: `/api/v1/articles?id={id}`.

## Rules

- Link each article you use, and show its `credit` line with any text you quote.
- Stay under 600 requests a minute; cache what you read.
- Full reference: https://www.edgechat.ai/developers
