---
title: "Context Compression"
summary: "An OpenRouter plugin that compresses prompts exceeding a model's context window using middle-out truncation"
type: concept
sources:
  - raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md
tags:
  - openrouter
  - plugins
  - context-window
  - token-optimization
  - message-transforms
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Context Compression

An OpenRouter plugin that compresses prompts exceeding a model's context window using middle-out truncation. ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

## Key Points

- Uses middle-out truncation to compress prompts that exceed the model's context window length ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Categorized under "Message Transforms" in the OpenRouter documentation, alongside response healing ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Runs exactly once per request when enabled, unlike server tools which the model invokes dynamically ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Can be combined with other plugins in a single request ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Enabled per-request via `plugins: [{ id: "context-compression" }]`; works with any model ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- Removes or truncates messages from the middle of the prompt until it fits within the model's context window ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- When Anthropic's Claude models enforce a maximum message count, the plugin keeps half the messages from the start and half from the end ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]
- Models with 8k (8,192 tokens) or less context length default to context compression; disable with `plugins: [{"id": "context-compression", "enabled": false}]` ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]

## Details

Context compression addresses the problem of prompts that are too long for a model's context window. Rather than simply truncating from the beginning or end, middle-out truncation preserves the most important content from both the start and end of the prompt while compressing or removing the middle section. This is particularly useful when working with long documents or conversations that exceed a model's token limit. ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

When context compression is enabled, OpenRouter first tries to find models whose context length is at least half of the total required tokens (input + completion). For example, if a prompt requires 10,000 tokens total, models with at least 5,000 context length will be considered. If no models meet this criteria, OpenRouter falls back to using the model with the highest available context length. The compression then attempts to fit the content within the chosen model's context window by removing or truncating content from the middle. ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]

Middle-out compression is based on the research finding that LLMs pay less attention to the middle of sequences, making it a principled choice for which content to sacrifice when a prompt exceeds the context window. ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]

If context compression is disabled and total tokens exceed the model's context length, the request fails with an error message suggesting to either reduce the length or enable context compression. ^[raw/document/openrouter/openrouter-042-guides-features-message-transforms-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/plugins]]
- [[concepts/context_window]]
- [[concepts/token_optimization]]
- [[concepts/model_fallback]]
- [[entities/anthropic]]
- [[summaries/openrouter-guides-features-plugins-overview]]
- [[summaries/openrouter-guides-features-message-transforms]]