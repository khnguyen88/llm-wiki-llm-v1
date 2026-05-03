---
title: "Text-to-Speech"
summary: "Converting text input into synthesized audio output via dedicated API endpoints, with per-character pricing and multiple format options"
type: concept
sources:
  - raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md
tags:
  - tts
  - audio
  - multimodal
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Text-to-Speech

Text-to-speech (TTS) is the process of converting written text into synthesized audio. On OpenRouter, TTS is handled through a dedicated API endpoint separate from the chat completions interface.

## Key Points

- OpenRouter exposes TTS via `POST /api/v1/audio/speech`, compatible with the OpenAI Audio Speech API ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- TTS models are discovered by filtering the Models API with `output_modalities=speech` or by filtering on the Models page ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- The response is a raw audio byte stream (not JSON), with `Content-Type` and `X-Generation-Id` headers ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Two output formats: `mp3` (compressed, smaller files) and `pcm` (uncompressed, lower latency for real-time streaming) ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]
- Pricing is per character of input text, varying by model and provider ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]

## Details

The TTS endpoint requires three parameters: `model` (a TTS-capable model slug), `input` (the text to synthesize), and `voice` (a voice identifier that varies by provider). Optional parameters include `response_format` (defaults to `pcm`), `speed` (a multiplier only supported by certain providers like OpenAI, silently ignored by others), and `provider` (for provider-specific passthrough options such as OpenAI's `instructions` field for tone/style control). ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]

For long texts, splitting input into smaller segments and concatenating the audio output improves reliability and reduces latency for the first audio chunk. The endpoint is fully compatible with the OpenAI SDK by pointing the client's `base_url` to `https://openrouter.ai/api/v1`. ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]

Common pitfalls include saving `pcm` output with a `.mp3` extension, using incomplete model slugs instead of fully qualified ones (e.g., `gpt-4o-mini-tts` vs. `openai/gpt-4o-mini-tts-2025-12-15`), and assuming voice identifiers are universal across providers. ^[raw/document/openrouter/openrouter-011-guides-overview-multimodal-tts-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/multimodal]]
- [[concepts/models_api]]
- [[concepts/streaming_output]]
- [[summaries/openrouter-guides-overview-multimodal-tts]]