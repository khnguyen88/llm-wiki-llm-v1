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

An open semantic convention for AI and LLM tracing, maintained at [github.com/Arize-ai/openinference](https://github.com/Arize-ai/openinference), that standardizes how span attributes are labeled for prompts, completions, embeddings, and tool calls. ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Key Facts

- Developed under the [[entities/arize_ai|Arize AI]] organization as an open specification ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Used by [[entities/arize_ai|Arize]] to structure trace data received from [[entities/openrouter|OpenRouter]] Broadcast via OTLP payloads ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Defines standard trace metadata keys: `trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id` ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Token usage, costs, and model parameters are automatically included as OpenInference-compatible attributes in Broadcast traces ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Related

- [[entities/arize_ai]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[entities/open_telemetry]]
- [[summaries/openrouter-guides-features-broadcast-arize]]