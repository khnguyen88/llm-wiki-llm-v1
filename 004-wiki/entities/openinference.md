---
title: "OpenInference"
summary: "An open semantic convention for AI/LLM tracing that standardizes span attributes for prompts, completions, embeddings, and tool calls"
type: entity
sources:
  - raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md
tags:
  - openinference
  - observability
  - tracing
  - semantic-convention
  - arize
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenInference

An open semantic convention for AI and LLM tracing, maintained at [github.com/Arize-ai/openinference](https://github.com/Arize-ai/openinference), that standardizes how span attributes are labeled for prompts, completions, embeddings, and tool calls. ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Key Facts

- Developed under the [[004-wiki/entities/arize_ai|Arize AI]] organization as an open specification ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Used by [[004-wiki/entities/arize_ai|Arize]] to structure trace data received from [[004-wiki/entities/openrouter|OpenRouter]] Broadcast via OTLP payloads ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Defines standard trace metadata keys: `trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id` ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Token usage, costs, and model parameters are automatically included as OpenInference-compatible attributes in Broadcast traces ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Related

- [[004-wiki/entities/arize_ai]]
- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/entities/open_telemetry]]
- [[004-wiki/summaries/openrouter-guides-features-broadcast-arize]]