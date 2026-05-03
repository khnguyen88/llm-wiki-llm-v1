---
title: "Reasoning Details"
summary: "A structured API field (reasoning_details) returned by reasoning models containing typed reasoning objects (summary, encrypted, text) with provider-specific formats, used for preserving reasoning across multi-turn conversations"
type: concept
sources:
  - raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md
tags:
  - reasoning-details
  - openrouter
  - api
  - streaming
  - reasoning
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Reasoning Details

The `reasoning_details` field contains a structured array of reasoning detail objects returned by reasoning models. It standardizes reasoning output across providers with typed objects (summary, encrypted, text) and provider-specific format identifiers. It appears in `choices[].message.reasoning_details` for non-streaming responses and `choices[].delta.reasoning_details` for streaming responses. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

## Key Points

- `reasoning_details` is an array of typed reasoning objects in the response, located at `choices[].message.reasoning_details` (non-streaming) or `choices[].delta.reasoning_details` (streaming) ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- Three object types: `reasoning.summary` (high-level reasoning summary), `reasoning.encrypted` (encrypted/protected reasoning data), and `reasoning.text` (raw text reasoning with optional signature) ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- All reasoning detail objects share common fields: `id` (unique identifier), `format` (provider-specific format version), and `index` (sequential position) ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- Six format identifiers: `unknown`, `openai-responses-v1`, `azure-openai-responses-v1`, `xai-responses-v1`, `anthropic-claude-v1` (default), and `google-gemini-v1` ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- When preserving reasoning across turns, the entire sequence of consecutive reasoning blocks must match the model's original output; blocks cannot be rearranged or modified ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

## Details

### Reasoning Detail Types

**Summary type (`reasoning.summary`)**: Contains a high-level summary of the reasoning process. Fields: `type`, `summary` (string), `id`, `format`, `index`. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

**Encrypted type (`reasoning.encrypted`)**: Contains encrypted reasoning data that may be redacted or protected. Fields: `type`, `data` (base64-encoded string), `id`, `format`, `index`. In streaming responses, encrypted content may appear as `[REDACTED]`. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

**Text type (`reasoning.text`)**: Contains raw text reasoning with optional signature verification. Fields: `type`, `text` (string), `signature` (optional, e.g., `sha256:abc123...`), `id`, `format`, `index`. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

### Streaming Behavior

In streaming responses, each reasoning detail chunk is sent as it becomes available. The `reasoning_details` array in each chunk may contain one or more reasoning objects. For encrypted reasoning, content may appear as `[REDACTED]`. The complete reasoning sequence is built by concatenating all chunks in order. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

### Preserving Reasoning Details

Use `reasoning_details` (over the simpler `reasoning` string field) when working with models that return special reasoning types such as encrypted or summarized reasoning. Passing back the full `reasoning_details` block preserves the structure needed for those models to continue reasoning from where they left off. This is particularly important for tool calling: when a model invokes a tool and pauses to await results, including the original reasoning details ensures reasoning continuity. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

The `reasoning_details` functionality works identically across all supported reasoning models. Code using `reasoning_details` can switch between providers (e.g., `openai/gpt-5.2` to `anthropic/claude-sonnet-4.5`) without structural changes. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

## Related

- [[concepts/reasoning_tokens]]
- [[concepts/extended_thinking]]
- [[concepts/tool_calling]]
- [[entities/openrouter]]
- [[entities/openai]]
- [[entities/google_gemini]]
- [[summaries/openrouter-guides-best-practices-reasoning-tokens]]