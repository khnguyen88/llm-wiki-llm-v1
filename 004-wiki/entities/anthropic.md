---
title: "Anthropic"
summary: "AI research company that builds Claude models, with provider-specific prompt caching configuration on OpenRouter including automatic and explicit cache breakpoint modes"
type: entity
sources:
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
  - raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - anthropic
  - claude
  - llm
  - provider
  - beta-features
  - structured-outputs
  - prompt-caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Anthropic

AI research company that builds the Claude family of models. On OpenRouter, Anthropic requires explicit `cache_control` configuration for prompt caching (unlike providers that enable it automatically), supports both automatic and explicit cache breakpoint modes, and offers specific beta features accessible through provider-specific headers. ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md] ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Key Facts

- Provider slug on OpenRouter: `"anthropic"` ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Three beta features can be passed via the `x-anthropic-beta` header: fine-grained tool streaming, interleaved thinking, and structured outputs ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Multiple beta features can be combined by comma-separating their header values ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- OpenRouter automatically manages some Anthropic features: prompt caching and extended context are enabled based on model capabilities; structured outputs for `response_format.type: "json_schema"` are auto-applied ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Strict tool use (`strict: true` on tools) requires the `structured-outputs-2025-11-13` header to be explicitly passed; without it, OpenRouter strips the `strict` field and routes normally ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Anthropic models supporting structured outputs on OpenRouter: Sonnet 4.5, Opus 4.1+ ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- Two prompt caching modes on OpenRouter: automatic caching (top-level `cache_control` field) and explicit cache breakpoints (per-block `cache_control`) ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Automatic caching (top-level `cache_control`) is only supported when routed to the Anthropic provider directly; Amazon Bedrock and Google Vertex AI do not support it ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Explicit per-block `cache_control` breakpoints work across all Anthropic-compatible providers including Amazon Bedrock and Google Vertex AI ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Cache writes with 5-minute TTL are charged at 1.25x the base input price; cache writes with 1-hour TTL are charged at 2x the base input price; cache reads are charged at a reduced rate ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Default cache TTL is 5 minutes, extendable to 1 hour via `"ttl": "1h"` in the `cache_control` object; 1-hour TTL for explicit breakpoints is supported across all Claude model providers (Anthropic, Amazon Bedrock, Google Vertex AI) ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Maximum of four explicit cache breakpoints per request ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Supported Claude models for prompt caching: Claude Opus 4.7, Claude Opus 4.6, Claude Opus 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Sonnet 4, Claude Sonnet 3.7 (deprecated), Claude Haiku 4.5, Claude Haiku 3.5 ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Minimum cacheable prompt length varies by model: 4096 tokens (Opus 4.7, Opus 4.6, Opus 4.5, Haiku 4.5), 2048 tokens (Sonnet 4.6, Haiku 3.5), 1024 tokens (Sonnet 4.5, Opus 4.1, Opus 4, Sonnet 4, Sonnet 3.7) ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

### Anthropic Beta Features on OpenRouter

| Feature | Header Value | Description |
|---|---|---|
| Fine-Grained Tool Streaming | `fine-grained-tool-streaming-2025-05-14` | Granular streaming events during tool calls |
| Interleaved Thinking | `interleaved-thinking-2025-05-14` | Thinking/reasoning interleaved with regular output |
| Structured Outputs | `structured-outputs-2025-11-13` | Strict tool use with schema-validated parameters |

^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[concepts/provider_routing]]
- [[concepts/prompt_caching]]
- [[concepts/provider_sticky_routing]]
- [[concepts/structured_output]]
- [[summaries/openrouter-guides-features-structured-outputs]]
- [[summaries/openrouter-guides-best-practices-prompt-caching]]