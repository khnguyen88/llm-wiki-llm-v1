---
title: "OpenRouter Models API Overview"
summary: "OpenRouter's Models API provides standardized metadata for 300+ models, with query parameters for filtering by output modality and supported features"
type: summary
sources:
  - raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md
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

# OpenRouter Models API Overview

## Key Points

- The Models API (`/api/v1/models`) returns standardized JSON metadata for 300+ models, cached at the edge for production reliability ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- The `output_modalities` query parameter filters models by output type: `text` (default), `image`, `audio`, `embeddings`, or `all` ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- The `supported_parameters` query parameter filters models by API parameters they support (e.g., `?supported_parameters=tools` for tool-capable models) ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- Each model object includes: `id`, `canonical_slug`, `name`, `context_length`, `architecture`, `pricing`, `top_provider`, `supported_parameters`, `default_parameters`, and `expiration_date` ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- Pricing objects break down cost per token type: `prompt`, `completion`, `request`, `image`, `web_search`, `internal_reasoning`, `input_cache_read`, and `input_cache_write` — a value of `"0"` indicates the feature is free ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- The `canonical_slug` field provides a permanent identifier that never changes, unlike model `id` values which may vary ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- Tokenization varies across models: some tokenize by multi-character chunks (GPT, Claude, Llama) while others tokenize by character (PaLM), affecting token counts and costs even for identical inputs ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

## Quotes

> "Different models tokenize text in different ways... This means that token counts (and therefore costs) will vary between models, even when inputs and outputs are the same." ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

## Notes

- An RSS feed for new models is available at `/api/v1/models?use_rss=true` ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- The `/v1/models/count` endpoint supports the same `output_modalities` parameter for consistent count results ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]
- The `expiration_date` field signals model endpoint deprecation; `null` means not deprecated ^[raw/document/openrouter/openrouter-003-guides-overview-models-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/models_api]]
- [[concepts/token_optimization]]
- [[concepts/structured_output]]
- [[concepts/prompt_caching]]