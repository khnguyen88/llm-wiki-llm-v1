---
title: "Video Generation"
summary: "An asynchronous API workflow on OpenRouter for generating video from text prompts and optional reference images, using a submit-poll-download pattern with webhook support"
type: concept
sources:
  - raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md
tags:
  - video-generation
  - multimodal
  - api
  - openrouter
  - async
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Video Generation

Video generation on OpenRouter produces video output from text prompts (and optionally reference images) through an asynchronous API at `/api/v1/videos`. Unlike text and image generation which return results inline, video generation requires a submit-poll-download workflow because generation takes significantly longer. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

## Key Points

- The API follows a three-step workflow: `POST /api/v1/videos` to submit (returns job ID and polling URL), poll `GET /api/v1/videos/{jobId}` until status is `completed`, then download from `GET /api/v1/videos/{jobId}/content` or `unsigned_urls` ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Models are discoverable via `GET /api/v1/videos/models` (returns supported resolutions, aspect ratios, pricing SKUs, and passthrough parameters) or via `GET /api/v1/models?output_modalities=video` ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Two image input modes: `frame_images` (image-to-video, specifying `first_frame` or `last_frame`) and `input_references` (reference-to-video, style guidance); `frame_images` takes precedence when both are provided ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Request parameters include `model`, `prompt` (required), and optional `duration`, `resolution`, `aspect_ratio`, `size`, `frame_images`, `input_references`, `generate_audio`, `seed`, `callback_url`, and `provider` ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Video generation is not eligible for Zero Data Retention because the provider must temporarily retain the output for retrieval after the async job completes ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

## Details

### Job Lifecycle

Submitted jobs progress through four statuses: `pending` (queued), `in_progress` (generating), `completed` (ready to download), or `failed` (check `error` field). Completed responses include an `unsigned_urls` array and a `usage` object with cost information. The recommended polling interval is 30 seconds; video generation typically takes 30 seconds to several minutes depending on model and parameters. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

### Webhooks

Instead of polling, clients can receive webhook notifications at a `callback_url` (set per-request or as a workspace default). Four event types are sent: `video.generation.completed`, `video.generation.failed`, `video.generation.cancelled`, and `video.generation.expired`. Each delivery includes an `X-OpenRouter-Idempotency-Key` header of the form `<job_id>-<status>` for safe retry deduplication. A signing secret can be configured in workspace settings; when set, each delivery includes an `X-OpenRouter-Signature` header containing a timestamp and HMAC-SHA256 hash for verification. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

### Image-to-Video vs. Reference-to-Video

The `frame_images` parameter specifies exact first or last frame images for image-to-video generation. Each entry must include a `frame_type` of `first_frame` or `last_frame`. The `input_references` parameter provides style or content reference images for reference-to-video generation, where the model uses images as visual guidance rather than exact frames. If both fields are provided, `frame_images` takes precedence and the request is treated as image-to-video. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

### Supported Output Parameters

Resolutions: 480p, 720p, 1080p, 1K, 2K, 4K. Aspect ratios: 16:9 (widescreen), 9:16 (vertical), 1:1 (square), 4:3 (standard landscape), 3:4 (standard portrait), 21:9 (ultra-wide), 9:21 (ultra-tall). The `size` parameter (e.g., `1280x720`) is interchangeable with `resolution` + `aspect_ratio`. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/video_input]]
- [[concepts/multimodal]]
- [[concepts/zero_data_retention]]
- [[concepts/image_generation]]
- [[summaries/openrouter-guides-overview-multimodal-video-generation]]