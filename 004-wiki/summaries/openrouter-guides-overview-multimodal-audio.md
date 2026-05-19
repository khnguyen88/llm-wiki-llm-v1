---
title: "OpenRouter Guides Overview Multimodal Audio"
summary: "OpenRouter audio API guide covering base64-encoded audio input via input_audio content type and streaming audio output with voice/format configuration"
type: summary
sources:
  - raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md
tags:
  - openrouter
  - audio
  - multimodal
  - streaming
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Guides Overview Multimodal Audio

## Key Points

- Audio input uses the `input_audio` content type in the `/api/v1/chat/completions` endpoint; audio files must be base64-encoded with a format specification — direct URLs are not supported for audio content ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Audio output requires setting `modalities: ["text", "audio"]` and providing an `audio` configuration object with `voice` and `format` parameters; audio output must use streaming (`stream: true`) ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Supported audio input formats include `wav`, `mp3`, `aiff`, `aac`, `ogg`, `flac`, `m4a`, `pcm16`, and `pcm24`, though format support varies by model ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Audio output streaming delivers data incrementally via `delta.audio` fields containing `data` (base64 audio chunks) and `transcript` (text) in SSE chunks ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Available audio output voices include `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`; available output formats include `wav`, `mp3`, `flac`, `opus`, and `pcm16` — both vary by model ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- Models supporting audio input can be discovered by filtering for audio input modality on the Models page; models supporting audio output can be filtered by audio output modality ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]

## Quotes

- "Audio files must be base64-encoded - direct URLs are not supported for audio content." ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]
- "Audio output requires streaming (`stream: true`)." ^[raw/document/openrouter/openrouter-008-guides-overview-multimodal-audio-2026-04-29.md]

## Notes

- The source provides TypeScript SDK, Python, and TypeScript (fetch) code examples for both audio input and audio output workflows
- Audio input example uses `google/gemini-2.5-flash` model; audio output example uses `openai/gpt-4o-audio-preview` model
- The streaming chunk format for audio output mirrors the SSE pattern used for text and image streaming on OpenRouter

## Related

- [[entities/openrouter]]
- [[concepts/multimodal]]
- [[concepts/streaming_output]]
- [[concepts/models_api]]