---
title: "Openrouter Guides Features Server Tools Image Generation"
summary: "OpenRouter's image generation server tool lets any model generate images from text prompts via the openrouter:image_generation tool type, with configurable model, quality, size, and format parameters"
type: summary
sources:
  - raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md
tags:
  - openrouter
  - server-tools
  - image-generation
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Server Tools Image Generation

## Key Points

- The `openrouter:image_generation` server tool enables any model on OpenRouter to generate images from text prompts; the model decides when image generation is needed and crafts the prompt, and OpenRouter executes the generation server-side ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]
- Activated by including `{ "type": "openrouter:image_generation" }` in the `tools` array of a Chat Completions or Responses API request; no client-side implementation needed ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]
- Defaults to `openai/gpt-image-1` as the image generation model; configurable via the `parameters.model` field ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]
- Supports eight configuration parameters: `model`, `quality`, `size`, `aspect_ratio`, `background`, `output_format`, `output_compression`, and `moderation`; all except `model` are passed directly to the underlying image generation API ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]
- Response returns `{ "status": "ok", "imageUrl": "https://..." }` on success or `{ "status": "error", "error": "..." }` on failure ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]
- The model may generate multiple images in a single request if needed ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]
- Image generation cost is in addition to standard LLM token costs for processing the request and response ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]

## Notes

- Server tools are currently in beta; API and behavior may change ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]
- This server-tool approach to image generation is distinct from the `modalities`-based image generation described in the multimodal overview, which returns base64 data URLs directly in the response; the server tool returns an image URL instead

## Related

- [[entities/openrouter]]
- [[concepts/image_generation]]
- [[concepts/server_tools]]
- [[summaries/openrouter-guides-features-server-tools-overview]]