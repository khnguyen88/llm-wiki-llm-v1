---
title: "Openrouter Guides Overview Multimodal Video Generation"
summary: "OpenRouter's asynchronous video generation API supporting text-to-video, image-to-video, and reference-to-video workflows with polling, webhooks, and provider passthrough parameters"
type: summary
sources:
  - raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md
tags:
  - openrouter
  - video-generation
  - multimodal
  - api
  - async
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Overview Multimodal Video Generation

## Key Points

- Video generation on OpenRouter uses an asynchronous API at `POST /api/v1/videos` — requests return a job ID immediately, and clients poll `GET /api/v1/videos/{jobId}` until the status is `completed` ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Model discovery via a dedicated `GET /api/v1/videos/models` endpoint that returns supported resolutions, aspect ratios, sizes, pricing SKUs, and allowed passthrough parameters per model ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Two image-based generation modes: `frame_images` for image-to-video (specifying first or last frame) and `input_references` for reference-to-video (style guidance); `frame_images` takes precedence when both are provided ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Webhook notifications available via `callback_url` per-request or workspace-level default, with HMAC-SHA256 signature verification using `X-OpenRouter-Signature` headers ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Video generation is not eligible for Zero Data Retention because generated output must be temporarily retained by the provider for retrieval after the async job completes ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Supported resolutions: 480p, 720p, 1080p, 1K, 2K, 4K; supported aspect ratios: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 9:21 ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]
- Provider-specific parameters (e.g., `personGeneration`, `negativePrompt` for Google Vertex) can be passed through the `provider.options` field, keyed by provider slug ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

## Quotes

> Unlike text or image generation, video generation is asynchronous because generating video takes significantly longer. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md:2]

> Video generation is not eligible for Zero Data Retention (ZDR). Because video generation is asynchronous, the generated video output must be retained by the provider for a short period of time so that it can be retrieved after generation is complete. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

## Notes

- Job statuses follow the sequence: `pending` → `in_progress` → `completed` or `failed`
- Completed videos are downloaded via `GET /api/v1/videos/{jobId}/content?index=0` or from `unsigned_urls` in the poll response
- The `size` parameter (e.g., `1280x720`) is interchangeable with `resolution` + `aspect_ratio`
- Webhook events include: `video.generation.completed`, `video.generation.failed`, `video.generation.cancelled`, `video.generation.expired`
- Each webhook delivery carries an `X-OpenRouter-Idempotency-Key` header of the form `<job_id>-<status>` for retry deduplication

## Related

- [[entities/openrouter]]
- [[concepts/video_generation]]
- [[concepts/video_input]]
- [[concepts/multimodal]]
- [[concepts/zero_data_retention]]
- [[concepts/streaming_output]]
- [[summaries/openrouter-guides-overview-multimodal-videos]]