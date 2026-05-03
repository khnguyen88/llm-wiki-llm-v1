---
title: "Vision Models"
summary: "Multi-modal LLMs that accept both text and images as input, producing text output; named with 'vision' or 'VL' suffix"
type: concept
sources:
  - raw/articles/How to navigate LLM model names.md
  - raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md
tags:
  - llm
  - vision
  - multi-modal
  - model-selection
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.85
provenance: extracted
---

# Vision Models

Vision models are an emerging category of LLMs that accept both text and images as input and produce text as output. They are named with a "vision" or "VL" suffix in model names. ^[raw/articles/How to navigate LLM model names.md]

## Key Points

- Vision models are multi-modal: they process text and images together, enabling tasks like asking questions about an image, describing image content, or image-to-text conversion ^[raw/articles/How to navigate LLM model names.md]
- "Vision-instruct" models combine vision capability with instruction-following, serving as general chat models that also handle vision tasks ^[raw/articles/How to navigate LLM model names.md]
- Example: granite-vision-3.2-2b ^[raw/articles/How to navigate LLM model names.md]
- On OpenRouter, vision models are required for processing image inputs and are automatically filtered based on request content containing images ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Images can be sent to vision-capable models using the `image_url` content type in the message array, supporting both URL-based and base64-encoded formats ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Supported image MIME types for vision model input: `image/png`, `image/jpeg`, `image/webp`, `image/gif` ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- When sending images, the text prompt should precede the image content in the message array; if images must come first, they should be placed in the system prompt ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]

## Related

- [[concepts/model_naming]]
- [[concepts/instruction_tuning]]
- [[concepts/multimodal]]
- [[entities/openrouter]]