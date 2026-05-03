---
title: "Google Gemini"
summary: "Google's multimodal AI model family with both implicit and explicit prompt caching support on OpenRouter, accessible via AI Studio and Vertex AI"
type: entity
sources:
  - raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md
  - raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
  - raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md
tags:
  - google
  - gemini
  - multimodal
  - video
  - llm
  - structured-outputs
  - prompt-caching
  - reasoning-tokens
  - thinking-levels
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Google Gemini

Google's multimodal AI model family available through two deployment paths — AI Studio and Vertex AI — with both implicit and explicit prompt caching support on OpenRouter. ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md] ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Key Facts

- Available on OpenRouter with the model slug `google/gemini-2.5-flash` (used in documentation examples) ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- When accessed via AI Studio, Google Gemini only supports YouTube links for video input — direct video file URLs are not accepted ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- When accessed via Vertex AI, Google Gemini does not support video URLs at all — base64-encoded data URLs must be used instead ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Supports video input through the `video_url` content type on OpenRouter's Chat Completions API ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Supports structured outputs (JSON Schema-constrained responses) on OpenRouter ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- Gemini 2.5 Pro and 2.5 Flash support implicit caching on OpenRouter: automatic caching with no manual setup, no cache write or storage costs, cached tokens at reduced pricing ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Implicit caching TTL averages 3-5 minutes; minimum cacheable tokens vary by model (2.5 Flash and 2.5 Pro each have their own thresholds) ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- OpenRouter supports explicit `cache_control` breakpoints for Gemini caching, similar to Anthropic; only the last breakpoint is used for Gemini caching, but multiple breakpoints are safe and help maintain Anthropic compatibility ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Gemini has a single `systemInstruction` field; cached content treats the system prompt as immutable — dynamic content should be placed in a later `user` message rather than after a cached block in the first system message ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- OpenRouter simplifies Gemini cache management: no need to manually create, update, or delete caches, and no need to manage cache names or TTL explicitly ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Related

- [[entities/google_vertex_ai]]
- [[entities/openrouter]]
- [[concepts/video_input]]
- [[concepts/multimodal]]
- [[concepts/structured_output]]
- [[concepts/prompt_caching]]
- [[summaries/openrouter-guides-features-structured-outputs]]
- [[summaries/openrouter-guides-best-practices-prompt-caching]]