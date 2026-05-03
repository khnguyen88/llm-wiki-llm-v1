---
title: "Comet Opik"
summary: "An open-source platform by Comet for evaluating, testing, and monitoring LLM applications, available as a Broadcast destination on OpenRouter"
type: entity
sources:
  - raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md
tags:
  - opik
  - observability
  - llm-evaluation
  - tracing
  - broadcast
  - open-source
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Comet Opik

An open-source platform by Comet for evaluating, testing, and monitoring LLM applications, integrated as a Broadcast destination on OpenRouter. ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

## Key Facts

- Developed by Comet (https://www.comet.com/site/products/opik/) ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Open-source platform for evaluating, testing, and monitoring LLM applications ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Available as a Broadcast destination on OpenRouter, configured in Settings > Observability ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Configuration requires a Comet API key (prefix `opik_...`), workspace name, and project name ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Supports custom metadata on traces and spans for organizing and filtering LLM evaluations ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Maps four standard `trace` keys: `trace_id` → trace metadata (`openrouter_trace_id`), `trace_name` → Trace Name, `span_name` → Span Name, `generation_name` → Span Name ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Uses UUIDv7 format for internal trace and span IDs; original OpenRouter IDs are stored as `openrouter_trace_id` and `openrouter_observation_id` in metadata ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Cost information (input, output, total) is automatically added to span metadata ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

## Related

- [[concepts/broadcast]]
- [[entities/openrouter]]
- [[concepts/observability]]
- [[concepts/data_privacy]]