---
title: "Image Generation"
summary: "The capability of AI models to produce images from text prompts via API endpoints, with configuration for aspect ratio, resolution, and model-specific features"
type: concept
sources:
  - raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md
  - raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md
tags:
  - image-generation
  - multimodal
  - openrouter
  - api
  - server-tools
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Image Generation

Image generation on OpenRouter uses the Chat Completions and Responses endpoints with a `modalities` parameter to request image output. The `modalities` value depends on model capabilities: `["image", "text"]` for models that output both (e.g., Gemini), or `["image"]` for image-only models (e.g., Sourceful, Flux). ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

## Key Points

- Image generation is requested by setting `modalities: ["image", "text"]` or `modalities: ["image"]` in the chat completions request, depending on whether the model also produces text ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Generated images are returned as base64-encoded PNG data URLs in the `images` field of the assistant message (`message.images[].image_url.url`) ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- The `image_config` parameter controls aspect ratio (10 standard ratios from 1:1 to 21:9, plus 4 extended ratios on `google/gemini-3.1-flash-image-preview`), image size (0.5K–4K), and Sourceful-specific features (font rendering, super resolution) ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Streaming is supported: set `stream: true` and process `delta.images` from SSE chunks ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Models are discoverable via the `output_modalities=image` query parameter on the Models API, by filtering on the Models page, or via the Chatroom Image button ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

## Details

### Aspect Ratios and Image Sizes

Standard aspect ratios and their pixel dimensions: `1:1` → 1024×1024, `2:3` → 832×1248, `3:2` → 1248×832, `3:4` → 864×1184, `4:3` → 1184×864, `4:5` → 896×1152, `5:4` → 1152×896, `9:16` → 768×1344, `16:9` → 1344×768, `21:9` → 1536×672. The `0.5K` image size and extended aspect ratios (`1:4`, `4:1`, `1:8`, `8:1`) are exclusive to `google/gemini-3.1-flash-image-preview`. ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

### Sourceful-Exclusive Features

The `font_inputs` parameter renders custom text in generated images using specified fonts (max 2, $0.03 each). The `super_resolution_references` parameter enhances low-quality elements in an input image using reference images (max 4, $0.20 each), but only works with image-to-image requests. ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

### Response Format

The assistant message includes an `images` array where each element has `type: "image_url"` and `image_url.url` containing a base64 data URL. Some models can generate multiple images in a single response. Image dimensions vary by model capabilities. ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

### Server Tool Image Generation

OpenRouter also provides image generation via the `openrouter:image_generation` server tool, which works differently from the modalities-based approach. Instead of requesting image output via the `modalities` parameter, the model decides when an image is needed and calls the tool with a text prompt. OpenRouter generates the image server-side and returns a URL. The default model is `openai/gpt-image-1`, configurable via `parameters.model`. Supported configuration parameters include `quality`, `size`, `aspect_ratio`, `background`, `output_format`, `output_compression`, and `moderation` — all passed directly to the underlying image generation API. ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]

The server tool returns `{ "status": "ok", "imageUrl": "https://..." }` on success or `{ "status": "error", "error": "..." }` on failure. The model may generate multiple images in a single request. This tool works with both the Chat Completions and Responses APIs. ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/sourceful]]
- [[concepts/multimodal]]
- [[concepts/models_api]]
- [[concepts/streaming_output]]
- [[concepts/server_tools]]
- [[summaries/openrouter-guides-features-server-tools-image-generation]]