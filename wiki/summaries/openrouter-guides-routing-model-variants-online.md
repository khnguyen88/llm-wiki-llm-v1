---
title: "Openrouter Guides Routing Model Variants Online"
summary: "The `:online` model variant on OpenRouter is deprecated; web search capability is now provided via the `openrouter:web_search` server tool"
type: summary
sources:
  - raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md
tags:
  - openrouter
  - model-variants
  - web-search
  - deprecated
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Routing Model Variants Online

## Key Points

- The `:online` variant is deprecated; use the `openrouter:web_search` server tool instead, which gives the model control over when and how often to search ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- `:online` was accessed by appending `:online` to any model ID (e.g., `"openai/gpt-5.2:online"`) ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- The `:online` suffix is exactly equivalent to using the `web` plugin with `openrouter/auto` routing ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- Applications that already provide a `web_search` tool (e.g., OpenAI's built-in web search tool type) have it automatically recognized and hoisted to `openrouter:web_search`, so the `:online` suffix can be safely removed ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- The Online variant incorporated relevant web search results into model responses, providing access to real-time information and current events beyond the model's training data ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]

## Notes

- The replacement `openrouter:web_search` server tool is recommended over `:online` because it gives the model agency over search timing and frequency, rather than always attaching search results
- The legacy `web` plugin is still documented separately from the server tool approach

## Related

- [[entities/openrouter]]
- [[concepts/online_variant]]
- [[concepts/model_variants]]
- [[concepts/plugins]]