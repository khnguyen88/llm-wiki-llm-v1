---
title: "Arize AI"
summary: "An evaluation and observability platform for AI agents providing tracing, evals, and prompt optimization via the Arize AX product"
type: entity
sources:
  - raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md
tags:
  - arize
  - observability
  - tracing
  - evaluation
  - openinference
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Arize AI

An evaluation and observability platform developed by Arize AI; its Arize AX product offers tools for agent tracing, evals, prompt optimization, and more. ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Key Facts

- Arize AX provides agent tracing, evaluations, prompt optimization, and related observability tools ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Integrates with [[entities/openrouter|OpenRouter]] via [[concepts/broadcast|Broadcast]]; traces are sent using the [[entities/openinference|OpenInference]] semantic convention over OTLP ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Configuration requires four values: API Key (from Space Settings > API Keys), Space Key (from Space Settings), Model ID (for organizing traces), and an optional Base URL (default `https://otlp.arize.com`) ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- The `trace` field in API requests maps custom metadata to Arize span attributes; standard keys (`trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id`) map to dedicated Arize fields, while arbitrary keys map to the `metadata.*` namespace ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- The `user` and `session_id` request fields map to Arize span attributes for user identification and session tracking ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Token usage, costs, and model parameters are automatically included as OpenInference-compatible attributes ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- When [[concepts/broadcast|Broadcast]] Privacy Mode is enabled, prompt and completion content is excluded from traces while all other trace data continues normally ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/openinference]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[summaries/openrouter-guides-features-broadcast-arize]]