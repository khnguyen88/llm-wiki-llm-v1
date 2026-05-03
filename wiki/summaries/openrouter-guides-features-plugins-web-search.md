---
title: "OpenRouter Web Search Plugin (Deprecated)"
summary: "The deprecated OpenRouter web plugin that augmented LLM responses with real-time web search results, replaced by the openrouter:web_search server tool"
type: summary
sources:
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
tags:
  - openrouter
  - web-search
  - plugins
  - deprecated
  - domain-filtering
  - exa
  - firecrawl
  - parallel
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Web Search Plugin (Deprecated)

## Key Points

- The `web` plugin is deprecated; the `openrouter:web_search` server tool replaces it with model-controlled search timing (0-N calls) instead of always-once execution ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- The `:online` model suffix (e.g., `"openai/gpt-5.2:online"`) is a shortcut for the `web` plugin, equivalent to `{ "model": "openrouter/auto", "plugins": [{ "id": "web" }] }`; it can be combined with `:free` as `"openai/gpt-oss-20b:free:online"` ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- Web search results are standardized in the API response `message.annotations` array using the `url_citation` type, with `url`, `title`, `content`, `start_index`, and `end_index` fields ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- The plugin supports four engines: `native` (provider built-in), `exa` (keyword + embeddings search), `firecrawl` (BYOK), and `parallel`; `undefined` defaults to native where available, falling back to Exa ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- Domain filtering uses `include_domains` and `exclude_domains` (vs. `allowed_domains`/`excluded_domains` in the server tool), with engine-specific compatibility: Exa supports both simultaneously, Parallel supports both but mutually exclusively, Firecrawl returns a 400 error, and native providers vary ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- xAI models with web search enabled automatically receive an `x_search` tool alongside `web_search`; the top-level `x_search_filter` parameter supports `allowed_x_handles`, `excluded_x_handles`, `from_date`, `to_date`, `enable_image_understanding`, and `enable_video_understanding` ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- Exa and Parallel search cost $4 per 1,000 results via OpenRouter credits; Firecrawl uses your own Firecrawl credits; native search pricing is passed through from providers via `web_search_options.search_context_size` ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Quotes

> "For xAI models, the web search plugin enables both Web Search and X Search." ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md:17]

> "Using web search will incur extra costs, even with free models." ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md:18]

> "allowed_x_handles and excluded_x_handles are mutually exclusive — you cannot use both in the same request. If validation fails, the filter is silently dropped and a basic x_search tool is used instead." ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md:112-114]

## Notes

- The `search_prompt` parameter in the plugin configuration lets users customize the prompt text that attaches web results to the message stream; the default prompt instructs the model to cite sources using markdown links named by domain ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- Firecrawl setup requires accepting Terms of Service at openrouter.ai/settings/plugins, which creates a Firecrawl account linked to your email with a free hobby plan (100,000 credits) ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- The Exa search engine uses an "auto" method combining keyword search and embeddings-based search ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- Native search context sizes (`low`, `medium`, `high`) control how much search data is retrieved and are specified via `web_search_options.search_context_size` (distinct from the server tool's `search_context_size` parameter) ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/exa]]
- [[entities/firecrawl]]
- [[entities/parallel]]
- [[entities/anthropic]]
- [[concepts/web_search]]
- [[concepts/plugins]]
- [[concepts/online_variant]]
- [[concepts/server_tools]]