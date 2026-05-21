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

An open-source platform by Comet for evaluating, testing, and monitoring LLM applications, integrated as a Broadcast destination on OpenRouter. ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

## Key Facts

- Developed by Comet (https://www.comet.com/site/products/opik/) ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Open-source platform for evaluating, testing, and monitoring LLM applications ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Available as a Broadcast destination on OpenRouter, configured in Settings > Observability ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Configuration requires a Comet API key (prefix `opik_...`), workspace name, and project name ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Supports custom metadata on traces and spans for organizing and filtering LLM evaluations ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Maps four standard `trace` keys: `trace_id` → trace metadata (`openrouter_trace_id`), `trace_name` → Trace Name, `span_name` → Span Name, `generation_name` → Span Name ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Uses UUIDv7 format for internal trace and span IDs; original OpenRouter IDs are stored as `openrouter_trace_id` and `openrouter_observation_id` in metadata ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Cost information (input, output, total) is automatically added to span metadata ^[001a-raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

## Related

- [[004-wiki/concepts/broadcast]]
- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/concepts/data-privacy]]