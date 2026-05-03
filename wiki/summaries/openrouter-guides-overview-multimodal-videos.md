---
title: "Openrouter Guides Overview Multimodal Videos"
summary: "OpenRouter supports video input via the video_url content type on the Chat Completions API, accepting both direct URLs and base64-encoded data URLs, with provider-specific URL support variations"
type: summary
sources:
  - raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md
tags:
  - openrouter
  - multimodal
  - video
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Overview Multimodal Videos

## Key Points

- Video input uses the `video_url` content type on the `/api/v1/chat/completions` endpoint, with the `url` field accepting either a direct URL or a base64-encoded data URL ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Direct URLs are more efficient for publicly accessible videos; base64-encoded data URLs are required for local files or private videos ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Supported video formats: `video/mp4`, `video/mpeg`, `video/mov`, `video/webm` ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Video URL support varies by provider: Google Gemini on AI Studio only accepts YouTube links; Google Gemini on Vertex AI does not support video URLs at all (requires base64) ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Video inputs are currently only supported via the API, not through the OpenRouter chatroom interface ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Best practices include compressing videos, trimming to relevant segments, reducing resolution when possible, and splitting long videos into shorter segments ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Common use cases: video summarization, object/activity recognition, scene understanding, sports analysis, surveillance, and educational content analysis ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

## Quotes

> "OpenRouter only sends video URLs to providers that explicitly support them. For example, Google Gemini on AI Studio only supports YouTube links (not Vertex AI)." ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

> "Video inputs are currently only supported via the API. Video uploads are not available in the OpenRouter chatroom interface at this time." ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

## Notes

- The source provides complete code examples in TypeScript SDK, Python, and TypeScript (fetch) for both URL-based and base64-encoded video input
- Quality vs. size trade-offs: high quality (1080p+) for detailed analysis, medium (720p) for general tasks, lower (480p) for basic scene understanding ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/video_input]]
- [[concepts/multimodal]]
- [[entities/google_vertex_ai]]
- [[entities/google_gemini]]
- [[concepts/models_api]]