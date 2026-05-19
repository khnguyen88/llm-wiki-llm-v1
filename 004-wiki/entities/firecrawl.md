---
title: "Firecrawl"
summary: "A web scraping and search API (firecrawl.dev) that integrates with OpenRouter's web search server tool on a BYOK basis"
type: entity
sources:
  - raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md
  - raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
tags:
  - search-engine
  - openrouter
  - web-search
  - web-fetch
  - byok
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Firecrawl

A web scraping and search API (firecrawl.dev) that integrates with OpenRouter's web search server tool on a BYOK (Bring Your Own Key) basis. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

## Key Facts

- Uses your own Firecrawl API key, configured via OpenRouter plugin settings at openrouter.ai/settings/plugins ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Accepting Firecrawl's Terms of Service creates a Firecrawl account linked to your email, starting with a free hobby plan and 100,000 credits ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Firecrawl searches use your Firecrawl credits directly — no additional charge from OpenRouter ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Does not support domain filtering (`allowed_domains` or `excluded_domains`); returns an error if domain filters are set ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Does not support `search_context_size` ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Does not support `user_location` for location-biased results ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Also available as a fetch engine for the `openrouter:web_fetch` server tool, providing page content extraction via Firecrawl's scrape API (BYOK) ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- In web fetch mode, Firecrawl supports domain filtering and content truncation, with no hard limit on fetches per request ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Web fetch pricing with Firecrawl: uses your Firecrawl credits directly, no additional charge from OpenRouter ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- In the deprecated `web` plugin, Firecrawl setup requires accepting Terms of Service at openrouter.ai/settings/plugins, which automatically creates a Firecrawl account linked to your email with a free hobby plan and 100,000 credits ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- The plugin's domain filtering uses `include_domains` and `exclude_domains` (vs. `allowed_domains`/`excluded_domains` in the server tool); Firecrawl does not support domain filtering and returns a 400 error if filters are set ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/exa]]
- [[entities/parallel]]
- [[concepts/web_search]]
- [[concepts/server_tools]]
- [[concepts/byok]]
- [[concepts/web_fetch]]
- [[summaries/openrouter-guides-features-plugins-web-search]]