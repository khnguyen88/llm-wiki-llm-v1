---
title: "OpenRouter Multimodal Image Inputs"
summary: "How to send image inputs to multimodal models via OpenRouter's chat completions API, using direct URLs or base64-encoded data"
type: summary
sources:
  - raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md
tags:
  - openrouter
  - multimodal
  - images
  - api
  - base64
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Multimodal Image Inputs

## Key Points

- Image inputs to multimodal models are sent via the `/api/v1/chat/completions` endpoint using a multi-part `messages` parameter with `image_url` content type ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- The `image_url` field accepts either a direct URL or a base64-encoded data URI ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- Multiple images can be sent in separate content array entries within a single request ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- OpenRouter recommends sending the text prompt first, then the images; if images must come first, place them in the system prompt ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- The number of images allowed per request varies by provider and model ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- Direct URLs are more efficient for publicly accessible images; base64 encoding is required for local files or private images ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- Supported image content types: `image/png`, `image/jpeg`, `image/webp`, `image/gif` ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]

## Notes

- The source provides code examples in TypeScript SDK (`@openrouter/sdk`), Python (`requests`), and TypeScript fetch for both URL-based and base64-encoded image submission
- Base64 data URIs use the format `data:image/jpeg;base64,{encoded_string}`

## Related

- [[entities/openrouter]]
- [[concepts/multimodal]]
- [[concepts/vision_models]]
- [[summaries/openrouter-guides-overview-multimodal-overview]]