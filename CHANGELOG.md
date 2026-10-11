# Changelog

## 1.2.0 (2026-10-07)
- Three new tools: `related` (an article's topic-mates, neighboring topics, and geography neighbors), `connect` (the shortest chain of in-text links between two articles, with the sentence behind each hop), and `resolve` (which article a name means, with a confidence and the alternatives).
- `search` reaches further results with `limit` and `page`, can stay under one topic, and falls back to article text when no title matches. `fetch` takes up to 10 ids at once, one section, a token budget, or only the passages that match a query.
- Results pass their own output schemas, so strict clients accept them. The server also offers prompts, resource templates, and completion.
- The README describes corpus 1.6 and 1.6.1 (October 11, 2026). Registry entry and this repository at 1.2.0.

## 1.0.2 — 2026-10-03
- Gemini CLI extension (`gemini-extension.json`). The server itself is unchanged.

## 1.0.1 — 2026-10-02
- Registry entry links this repository and the Edgepedia icon. The server itself is unchanged.

## 1.0.0 — 2026-09-20
- `search` and `fetch`, read-only, at `https://www.edgechat.ai/mcp`. Listed in the official MCP Registry as `ai.edgechat/edgepedia`.
