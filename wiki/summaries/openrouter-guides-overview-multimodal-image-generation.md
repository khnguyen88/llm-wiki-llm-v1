---
title: "OpenRouter Image Generation"
summary: "How to generate images via OpenRouter's Chat Completions and Responses APIs, including model discovery, configuration options, and streaming support"
type: summary
sources:
  - raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md
tags:
  - openrouter
  - image-generation
  - multimodal
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Image Generation

## Key Points

- OpenRouter supports image generation via the Chat Completions and Responses endpoints; the `modalities` parameter controls output format — `["image", "text"]` for models that output both, `["image"]` for image-only models ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Image generation models are discoverable via the Models API (`?output_modalities=image`), the Models page (filter by output modality), or the Chatroom (click the Image button) ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- The `image_config` parameter supports `aspect_ratio` (10 ratios from 1:1 to 21:9), `image_size` (0.5K–4K), `font_inputs` (Sourceful only, $0.03 each, max 2), and `super_resolution_references` (Sourceful only, $0.20 each, max 4) ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Generated images are returned as base64-encoded PNG data URLs in the `images` field of the assistant message; some models can produce multiple images per response ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Image generation works with streaming: set `stream: true` and process `delta.images` from SSE chunks ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- `google/gemini-3.1-flash-image-preview` supports extended aspect ratios (1:4, 4:1, 1:8, 8:1) and 0.5K resolution not available on other models ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Compatible models include `google/gemini-3.1-flash-image-preview`, `google/gemini-2.5-flash-image`, `black-forest-labs/flux.2-pro`, `black-forest-labs/flux.2-flex`, and `sourceful/riverflow-v2-standard-preview` ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

## Notes

- The source document provides complete TypeScript SDK, Python, and TypeScript fetch examples for basic generation, configuration, and streaming workflows.
- Aspect ratio values map to specific pixel dimensions (e.g., `1:1` → 1024×1024, `16:9` → 1344×768, `21:9` → 1536×672).
- Sourceful's `font_inputs` feature requires the rendered text to also appear in the prompt for best results; line breaks or double spaces separate headlines and sub-headers within the same font input.
- Sourceful's `super_resolution_references` only works with image-to-image requests (ignored when no images are in `messages`); output matches the input image size, so larger inputs yield higher-quality results.

## Related

- [[entities/openrouter]]
- [[entities/sourceful]]
- [[concepts/image_generation]]
- [[concepts/multimodal]]
- [[concepts/models_api]]
- [[concepts/streaming_output]]