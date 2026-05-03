---
title: "Models API"
summary: "OpenRouter's standardized API endpoint for browsing and querying metadata about available LLM models, with filters for modality and supported parameters"
type: concept
sources:
  - raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md
  - raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md
tags:
  - openrouter
  - api
  - models
  - metadata
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Models API

A standardized REST API endpoint (`/api/v1/models`) that provides comprehensive metadata for 300+ models available on OpenRouter, cached at the edge for production reliability. ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

## Key Points

- Returns a JSON array of model objects under the `data` key, each with standardized fields for identification, capabilities, pricing, and provider details ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- Supports `output_modalities` query parameter to filter by output type: `text` (default), `image`, `audio`, `embeddings`, or `all` ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- `?output_modalities=image` returns only image generation models; `?output_modalities=text,image` returns models that support both text and image output ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Supports `supported_parameters` query parameter to filter by API capabilities (e.g., `?supported_parameters=tools`) ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- Each model includes a `canonical_slug` that never changes, providing a stable reference separate from the `id` field ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- Pricing is broken down per token type (prompt, completion, request, image, web_search, internal_reasoning, input_cache_read, input_cache_write); `"0"` means free ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

## Details

The response schema consists of nested objects: the root `data` array contains Model objects, each with `architecture`, `pricing`, and `top_provider` sub-objects. The Architecture object specifies input/output modalities, tokenizer, and instruct type. The Pricing object enumerates per-token and per-operation costs in USD. The Top Provider object exposes provider-specific limits (`context_length`, `max_completion_tokens`) and moderation status. ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

The `supported_parameters` array on each model lists which OpenAI-compatible parameters work with that model: `tools`, `tool_choice`, `max_tokens`, `temperature`, `top_p`, `reasoning`, `include_reasoning`, `structured_outputs`, `response_format`, `stop`, `frequency_penalty`, `presence_penalty`, and `seed`. ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

Tokenization varies across model families. Models like GPT, Claude, and Llama tokenize by multi-character chunks, while PaLM tokenizes by character. This means identical inputs produce different token counts and therefore different costs across models. The `usage` field in API responses provides actual token counts for verification. ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/token_optimization]]
- [[concepts/structured_output]]
- [[concepts/prompt_caching]]
- [[summaries/openrouter-guides-overview-models]]
- [[concepts/image_generation]]
- [[summaries/openrouter-guides-overview-multimodal-image-generation]]