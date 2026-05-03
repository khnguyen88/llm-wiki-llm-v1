---
title: "Openrouter Guides Overview Multimodal Tts"
summary: "OpenRouter's text-to-speech API endpoint, compatible with the OpenAI Audio Speech API, supporting per-character pricing and multiple output formats"
type: summary
sources:
  - raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md
tags:
  - openrouter
  - tts
  - multimodal
  - audio
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Overview Multimodal Tts

## Key Points

- OpenRouter provides a dedicated `/api/v1/audio/speech` endpoint for text-to-speech, compatible with the OpenAI Audio Speech API ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- TTS models are discovered via the `output_modalities=speech` query parameter on the Models API or by filtering on the Models page ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- The endpoint returns a raw audio byte stream (not JSON), with `Content-Type` and `X-Generation-Id` response headers ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Two output formats: `mp3` (`audio/mpeg`, compressed, good for storage/playback) and `pcm` (`audio/pcm`, uncompressed, lower latency for real-time streaming) ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Required parameters: `model`, `input`, `voice`; optional: `response_format` (defaults to `pcm`), `speed` (only supported by some providers like OpenAI), `provider` (provider-specific passthrough) ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Pricing is per character of input text, varying by model and provider ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Fully compatible with the OpenAI SDK by setting `base_url` to `https://openrouter.ai/api/v1` ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]

## Quotes

- "The TTS endpoint returns a **raw audio byte stream**, not JSON." ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- "The `speed` parameter is only supported by certain providers (e.g., OpenAI). It is silently ignored by providers that don't support it" ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]

## Notes

- Provider-specific options can be passed via the `provider` parameter, keyed by provider slug (e.g., `openai`), enabling features like custom instructions for tone/style ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Best practice: split long texts into smaller segments and concatenate audio output for improved reliability and reduced latency ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Common troubleshooting: match `response_format` to file extension (don't save `pcm` as `.mp3`), use full model slugs (e.g., `openai/gpt-4o-mini-tts-2025-12-15`), and verify voice availability per provider ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/text_to_speech]]
- [[concepts/multimodal]]
- [[concepts/models_api]]
- [[concepts/streaming_output]]
- [[summaries/openrouter-guides-overview-multimodal-audio]]