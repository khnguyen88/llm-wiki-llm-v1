---
title: "Openrouter Guides Features Message Transforms"
summary: "OpenRouter's context compression plugin removes or truncates messages from the middle of prompts that exceed a model's context window, with automatic model selection and a default-on policy for short-context models"
type: summary
sources:
  - raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md
tags:
  - openrouter
  - context-compression
  - plugins
  - message-transforms
  - token-optimization
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Message Transforms

## Key Points

- The context compression plugin is enabled per-request via `plugins: [{ id: "context-compression" }]` and works with any model ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- The plugin removes or truncates messages from the middle of the prompt until it fits within the model's context window ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- When Anthropic's Claude models enforce a maximum message count, the plugin keeps half the messages from the start and half from the end of the conversation ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- When context compression is enabled, OpenRouter first selects models whose context length is at least half the total required tokens (input + completion); if none qualify, it falls back to the model with the highest available context length ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- If context compression is disabled and total tokens exceed the model's context length, the request fails with an error suggesting to reduce length or enable compression ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- Models with 8k (8,192 tokens) or less context length default to using context compression; this can be disabled with `plugins: [{"id": "context-compression", "enabled": false}]` ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- Middle-out compression is chosen because LLMs pay less attention to the middle of sequences ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]

## Quotes

> LLMs pay less attention to the middle of sequences. ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md:30]

> All OpenRouter endpoints with 8k (8,192 tokens) or less context length will default to using context compression. ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md:28-29]

## Notes

- The source refers to this feature as "Message Transforms" in the page title, but the plugin ID is `context-compression`; the underlying mechanism is context compression applied as a message transform

## Related

- [[concepts/context_compression]]
- [[concepts/plugins]]
- [[concepts/context_window]]
- [[concepts/token_optimization]]
- [[concepts/model_fallback]]
- [[entities/openrouter]]
- [[entities/anthropic]]
- [[summaries/openrouter-guides-features-plugins-overview]]