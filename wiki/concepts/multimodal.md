---
title: "Multimodal"
summary: "The capability of AI platforms to process and generate content across multiple modalities — text, images, audio, video, and PDFs — through unified or dedicated API endpoints"
type: concept
sources:
  - raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md
  - raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md
  - raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md
  - raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md
  - raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md
  - raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md
tags:
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

# Multimodal

Multimodal refers to the capability of AI platforms to accept multiple types of input beyond text (images, PDFs, audio, video) and produce multiple types of output (text, images, audio, video). On OpenRouter, most multimodal inputs use the same `/api/v1/chat/completions` endpoint with different content types specified in the message content array. ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]

## Key Points

- OpenRouter supports seven modalities: image input, image generation, PDF processing, audio input/output, video input, video generation, and text-to-speech ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Content types in the message array: `image_url` for images, `file` for PDFs, `input_audio` for audio, `video_url` for video ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Text-to-speech uses a separate endpoint at `/api/v1/audio/speech` (OpenAI-compatible) ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Video generation uses an asynchronous API at `/api/v1/videos` with job polling ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- Multiple modalities can be combined in a single request ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]
- For image inputs, the text prompt should be sent before images in the content array; if images must come first, they should be placed in the system prompt ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- Multiple images can be sent in separate content array entries within a single request; the maximum number varies by provider and model ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]
- Image generation (output) uses `modalities: ["image", "text"]` or `modalities: ["image"]` on the Chat Completions endpoint; images are returned as base64 PNG data URLs in the `images` response field ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- Image generation models are discoverable via `?output_modalities=image` on the Models API, by filtering on the Models page, or via the Chatroom Image button ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- The `image_config` parameter provides control over aspect ratio (10 standard ratios plus 4 extended on Gemini 3.1), resolution (0.5K–4K), and Sourceful-exclusive features (font rendering, super resolution) ^[raw/document/openrouter/openrouter-006-guides-overview-multimodal-image-generation-2026-04-29.md]
- PDF input uses the `file` content type with direct URLs or base64-encoded data URLs; three processing engines (`mistral-ocr`, `cloudflare-ai`, `native`) are configurable via the `plugins` parameter; responses include `file` annotations with a hash for skipping re-parsing in follow-up requests ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- Audio input uses the `input_audio` content type and requires base64 encoding with a `format` field — direct URLs are not supported for audio, unlike images and PDFs ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Audio output requires `modalities: ["text", "audio"]` and an `audio` config with `voice` and `format` fields; streaming is mandatory for audio output (`stream: true`) ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Audio output voices include `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`; output formats include `wav`, `mp3`, `flac`, `opus`, `pcm16` — availability varies by model ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Video input uses the `video_url` content type with direct URLs or base64-encoded data URLs; supported formats are `video/mp4`, `video/mpeg`, `video/mov`, `video/webm`; video URL support varies by provider (e.g., Google Gemini on AI Studio only accepts YouTube links, Vertex AI requires base64) ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Video input is only available via the API, not the OpenRouter chatroom interface ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Video generation uses a dedicated async API at `/api/v1/videos` (not Chat Completions) with submit-poll-download workflow; models discoverable via `?output_modalities=video` on the Models API or the dedicated `/api/v1/videos/models` endpoint ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Video generation supports `frame_images` (image-to-video) and `input_references` (reference-to-video with style guidance); `frame_images` takes precedence when both are present ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

## Details

### Input Format Support

OpenRouter accepts two input formats for multimodal content. URLs are recommended for publicly accessible content because they avoid base64 encoding overhead and reduce request payload size. Base64 encoding is required for local files or private content. ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]

Audio is an exception: URL-based audio input is not supported; all audio must be submitted as base64 with a format specification (e.g., `wav`, `mp3`, `flac`, `ogg`, `aiff`, `aac`, `m4a`, `pcm16`, `pcm24`). Video URL support also varies by provider — for example, Google Gemini on AI Studio only accepts YouTube links. ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md] ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]

### Image Input Formats

For image inputs specifically, both direct URLs and base64-encoded data URIs are supported. URLs are more efficient for publicly accessible images because they avoid the encoding overhead and reduce request payload size. Base64 encoding is required for local files or private images, using the format `data:image/jpeg;base64,{encoded_string}`. Supported image content types are `image/png`, `image/jpeg`, `image/webp`, and `image/gif`. ^[raw/document/openrouter/openrouter-005-guides-overview-multimodal-images-2026-04-29.md]

### Model Compatibility

Not all models support every modality. OpenRouter automatically filters available models based on the content type of a request. Vision models are required for image processing, file-compatible models for PDFs, audio-capable models for audio, and video-capable models for video. The Models page allows filtering by input modality support. ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]

### Pricing by Modality

Pricing varies: images are typically priced per image or as input tokens; PDFs offer free text extraction but charge for OCR; audio input is priced as input tokens based on duration; audio output as completion tokens; video as input tokens based on duration and resolution. ^[raw/document/openrouter/openrouter-004-guides-overview-multimodal-overview-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/vision_models]]
- [[concepts/models_api]]
- [[concepts/streaming_output]]
- [[concepts/image_generation]]
- [[summaries/openrouter-guides-overview-multimodal-image-generation]]
- [[concepts/pdf_input]]
- [[summaries/openrouter-guides-overview-multimodal-pdfs]]
- [[summaries/openrouter-guides-overview-multimodal-audio]]
- [[concepts/video_input]]
- [[summaries/openrouter-guides-overview-multimodal-videos]]
- [[concepts/video_generation]]
- [[summaries/openrouter-guides-overview-multimodal-video-generation]]
- [[entities/google_gemini]]