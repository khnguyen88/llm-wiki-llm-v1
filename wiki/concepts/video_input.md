---
title: "Video Input"
summary: "A multimodal input type on OpenRouter using the video_url content type to send video files — via direct URL or base64-encoded data URL — to models with video processing capabilities"
type: concept
sources:
  - raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md
  - raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md
tags:
  - video
  - multimodal
  - api
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Video Input

Video input on OpenRouter uses the `video_url` content type within the `/api/v1/chat/completions` message array to send video content to models that support video processing. Only models with video capabilities handle these requests. ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

## Key Points

- The `video_url` content type sends a `url` field that can be either a direct URL (for publicly accessible videos) or a base64-encoded data URL (for local or private videos) ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Supported video formats: `video/mp4`, `video/mpeg`, `video/mov`, `video/webm` ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Video URL support varies by provider: OpenRouter only sends video URLs to providers that explicitly support them ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Video input is currently available only via the API, not through the OpenRouter chatroom interface ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Models supporting video can be found by filtering for video input modality on the OpenRouter Models page ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

## Details

### Provider-Specific URL Support

Video URL handling differs across providers. Google Gemini on AI Studio only accepts YouTube links (e.g., `https://www.youtube.com/watch?v=...`), not direct video file URLs. Google Gemini on Vertex AI does not support video URLs at all — base64-encoded data URLs must be used instead. Other providers should be checked individually for video URL support. ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

### Base64 Encoding

For local or private videos, base64-encoded data URLs are required. The format follows the pattern `data:video/mp4;base64,{encoded_string}`. This increases request payload size compared to direct URLs, so compression and trimming are recommended before encoding. ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

### Best Practices

File size considerations: compress videos when possible, trim to relevant segments, and reduce resolution (720p vs. 4K) when high detail is not needed. Different models have different maximum video duration limits — check model-specific documentation. For long videos, consider splitting into shorter segments and focusing on key moments. Quality trade-offs: 1080p+ for detailed analysis and text recognition; 720p for general tasks; 480p for basic scene understanding and action recognition. ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

### Troubleshooting

If a video is not processing: verify the model supports video input (`input_modalities` includes `"video"`), confirm the provider supports video URLs for URL-based requests, try base64 encoding as a fallback, check the video format is supported, and verify the file is not corrupted. For large file errors: compress, reduce resolution or frame rate, trim duration, or switch to a URL if the provider supports it. ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/google_gemini]]
- [[entities/google_vertex_ai]]
- [[concepts/multimodal]]
- [[concepts/vision_models]]
- [[concepts/models_api]]
- [[concepts/video_generation]]