---
title: "OpenRouter Multimodal Capabilities Overview"
summary: "OpenRouter supports multiple input/output modalities beyond text — images, PDFs, audio, video, image generation, video generation, and text-to-speech — through a unified chat completions API and dedicated endpoints"
type: summary
sources:
  - raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md
tags:
  - openrouter
  - multimodal
  - api
  - images
  - audio
  - video
  - pdf
  - tts
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Multimodal Capabilities Overview

## Key Points

- OpenRouter supports seven modalities beyond text: image input, image generation, PDF processing, audio input/output, video input, video generation, and text-to-speech ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Most multimodal inputs use the same `/api/v1/chat/completions` endpoint with different content types in the message array (`image_url`, `file`, `input_audio`, `video_url`) ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Text-to-speech uses a separate dedicated endpoint at `/api/v1/audio/speech`, compatible with the OpenAI Audio Speech API ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Video generation uses an asynchronous API at `/api/v1/videos` — submit a prompt, receive a job ID, then poll until the video is ready ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Both URLs and base64-encoded data are accepted for multimodal inputs; URLs are recommended for public content while base64 is required for local files ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Audio input is only supported via base64 encoding (no URL support); video URL support varies by provider (e.g., Gemini on AI Studio only accepts YouTube links) ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Model compatibility is automatic: OpenRouter filters available models based on request content, and not all models support every modality ^[raw/document/openrouter/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Multiple modalities can be combined in a single request (text, images, PDFs, audio, video together) ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]

## Quotes

> "OpenRouter supports multiple input and output modalities beyond text, allowing you to send images, PDFs, audio, and video files to compatible models, or generate speech from text through our unified API." ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md:10-12]

## Notes

- Pricing varies by modality: images per image or as input tokens, PDFs free for text extraction but paid for OCR, audio as tokens based on duration, video as tokens based on duration and resolution ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- The Models page at `https://openrouter.ai/models` allows filtering by supported input modalities

## Related

- [[entities/openrouter]]
- [[concepts/multimodal]]
- [[concepts/vision_models]]
- [[concepts/streaming_output]]
- [[concepts/models_api]]