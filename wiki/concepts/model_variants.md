---
title: "Model Variants"
summary: "Suffix modifiers on OpenRouter model slugs that change routing behavior or model capabilities, split into static variants (model-specific) and dynamic variants (universal)"
type: concept
sources:
  - raw/document/openrouter/openrouter-015-faq-2026-04-29.md
  - raw/document/openrouter/openrouter-020-guides-routing-model-variants-free-2026-04-29.md
  - raw/document/openrouter/openrouter-021-guides-routing-model-variants-extended-2026-04-29.md
  - raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md
  - raw/document/openrouter/openrouter-023-guides-routing-model-variants-thinking-2026-04-29.md
  - raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md
  - raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md
  - raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md
  - raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md
tags:
  - openrouter
  - model-routing
  - variants
  - pricing
  - performance
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:02Z"
confidence: 0.9
provenance: extracted
---

# Model Variants

Suffix modifiers appended to OpenRouter model slugs that change how a model behaves or how requests are routed. Variants are divided into static variants (available only on specific models) and dynamic variants (applicable to all models). ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Key Points

- Static variants are model-specific suffixes listed in the Models API; dynamic variants work on all models ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- `:free` — model is always provided at no cost with low rate limits ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- `:extended` — model has a longer than usual context length ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- `:thinking` — model supports reasoning by default ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- `:nitro` — sorts providers by throughput for faster response times ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- `:floor` — sorts providers by price for the most cost-effective routing ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- `:exacto` — sorts providers using quality-first signals tuned for tool-calling reliability ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Details

Static variants alter the model's capabilities (`:free` changes pricing, `:extended` changes context window, `:thinking` enables reasoning output). They can only be used with models that support them, and their availability is listed in the Models API response.

Dynamic variants change the provider selection behavior rather than the model itself. `:nitro` prioritizes throughput, `:floor` prioritizes lowest price, and `:exacto` prioritizes quality signals relevant to tool-calling. These can be appended to any model slug.

The `:nitro` variant is activated by appending `:nitro` to any model ID (e.g., `"openai/gpt-5.2:nitro"`). It is exactly equivalent to setting `provider.sort` to `"throughput"` in the request, causing OpenRouter to prioritize providers with the highest tokens-per-second rate. ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]

The `:exacto` variant explicitly activates quality-first provider sorting, using the same three signal classes as [[concepts/auto_exacto]]: tool-calling success/reliability, provider performance metrics, and benchmark data. Unlike Auto Exacto (which runs automatically on tool-calling requests), `:exacto` is an explicit opt-in via the model slug suffix. It is most useful on models with tool-calling support, multiple providers, and meaningful variance in tool-use reliability. ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

The `:thinking` variant enables extended reasoning capabilities for complex problem-solving tasks. It is accessed by appending `:thinking` to a model ID (e.g., `"deepseek/deepseek-r1:thinking"`). Thinking variants provide models with extended reasoning capabilities for more thorough analysis and step-by-step problem solving, particularly useful for tasks that benefit from chain-of-thought reasoning. ^[raw/document/openrouter/openrouter-023-guides-routing-model-variants-thinking-2026-04-29.md]

The `:online` variant is deprecated; it previously attached web search results to prompts. Its replacement is the `openrouter:web_search` server tool, which gives the model control over when and how often to search. The `:online` suffix was a shortcut for the `web` plugin, exactly equivalent to `{ "model": "openrouter/auto", "plugins": [{ "id": "web" }] }`. Applications providing a `web_search` tool have it automatically hoisted to `openrouter:web_search`, so the `:online` suffix can be safely removed as long as the application exposes the tool. ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md] ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]

Some plugins have convenient model variant shortcuts. Appending `:online` to any model ID enables the web search plugin (e.g., `"openai/gpt-5.2:online"` is equivalent to `"openai/gpt-5.2"` with `{ "plugins": [{ "id": "web" }] }`). The `:online` variant and the web search plugin are both deprecated in favor of the `openrouter:web_search` server tool. ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

The `:free` variant is accessed by appending `:free` to any model ID (e.g., `"meta-llama/llama-3.2-3b-instruct:free"`). Free variants provide model access without cost but may have different rate limits or availability compared to their paid counterparts. A separate Free Models Router is available in the Chat Playground for zero-cost inference. ^[raw/document/openrouter/openrouter-020-guides-routing-model-variants-free-2026-04-29.md] The `:free` variant is the manual alternative to the [[concepts/free_models_router|Free Models Router]] (`openrouter/free`), which automatically selects a random free model; using `:free` on a specific model ID gives control over which free model handles the request. ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]

The `:extended` variant is accessed by appending `:extended` to a model ID (e.g., `"anthropic/claude-sonnet-4.5:extended"`). Extended variants provide model versions with larger context windows than the standard version, enabling processing of longer inputs and maintaining more conversation history. ^[raw/document/openrouter/openrouter-021-guides-routing-model-variants-extended-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/models_api]]
- [[concepts/routing_mode]]
- [[concepts/provider_fallback]]
- [[concepts/rate_limiting]]
- [[summaries/openrouter-faq]]
- [[summaries/openrouter-guides-routing-model-variants-free]]
- [[summaries/openrouter-guides-routing-model-variants-extended]]
- [[concepts/exacto]]
- [[summaries/openrouter-guides-routing-model-variants-exacto]]
- [[summaries/openrouter-guides-routing-model-variants-thinking]]
- [[concepts/online_variant]]
- [[summaries/openrouter-guides-routing-model-variants-online]]
- [[concepts/nitro_variant]]
- [[summaries/openrouter-guides-routing-model-variants-nitro]]
- [[concepts/free_models_router]]
- [[summaries/openrouter-guides-routing-routers-free-models-router]]
- [[concepts/plugins]]
- [[summaries/openrouter-guides-features-plugins-overview]]