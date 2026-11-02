# Changelog

## README — 2026-11-01
- The README names Edgepedia 1.9.1 (November 1, 2026) as the current release: plots back behind the Spoilers section in 24,257 film and series articles. The server itself is unchanged.

## 1.2.1 (2026-10-31)
- The server's instructions and its two search descriptions say "more than 500,000 articles" (Edgepedia 1.9.0 holds 519,064). Tools and behavior are unchanged; the registry entry, `server.json` (with its new tools digest), and the Gemini extension are at 1.2.1.

## README — 2026-10-31
- The README names Edgepedia 1.9.0 (October 31, 2026) as the current release and points to the updates page for earlier ones; the README and the skill say "more than 500,000 articles".

## README — 2026-10-21
- The README names Edgepedia 1.8.0 (October 21, 2026) as the current release and points to the updates page for earlier ones. The server itself is unchanged.

## 1.2.0 (2026-10-07)
- Three new tools: `related` (an article's topic-mates, neighboring topics, and geography neighbors), `connect` (the shortest chain of in-text links between two articles, with the sentence behind each hop), and `resolve` (which article a name means, with a confidence and the alternatives).
- `search` reaches further results with `limit` and `page`, can stay under one topic, and falls back to article text when no title matches. `fetch` takes up to 10 ids at once, one section, a token budget, or only the passages that match a query.
- Results pass their own output schemas, so strict clients accept them. The server also offers prompts, resource templates, and completion.
- Registry entry and this repository at 1.2.0.

## 1.0.2 — 2026-10-03
- Gemini CLI extension (`gemini-extension.json`). The server itself is unchanged.

## 1.0.1 — 2026-10-02
- Registry entry links this repository and the Edgepedia icon. The server itself is unchanged.

## 1.0.0 — 2026-09-20
- `search` and `fetch`, read-only, at `https://www.edgechat.ai/mcp`. Listed in the official MCP Registry as `ai.edgechat/edgepedia`.
