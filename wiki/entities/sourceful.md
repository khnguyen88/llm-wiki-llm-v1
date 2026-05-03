---
title: "Sourceful"
summary: "An AI model provider offering image generation models with unique features including custom font rendering and super resolution enhancement"
type: entity
sources:
  - raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md
tags:
  - sourceful
  - image-generation
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Sourceful

An AI model provider offering image generation models on OpenRouter, distinguished by exclusive support for custom font rendering and super resolution enhancement features. ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

## Key Facts

- Models available on OpenRouter: `sourceful/riverflow-v2-fast` and `sourceful/riverflow-v2-pro` ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Supports `font_inputs` via `image_config`: renders custom text using specified font files (max 2 per request, $0.03 per font input) ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Each font input requires `font_url` (URL to font file) and `text` (text to render); the text should match exactly what appears in the prompt ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Supports `super_resolution_references` via `image_config`: enhances low-quality elements in an input image using high-quality reference images (max 4 references per request, $0.20 per reference) ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Super resolution only works with image-to-image generation (ignored when no images are present in `messages`); output image size matches the input image size ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/image_generation]]
- [[concepts/multimodal]]