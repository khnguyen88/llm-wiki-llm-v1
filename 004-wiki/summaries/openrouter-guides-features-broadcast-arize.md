---
title: "Openrouter Guides Features Broadcast Arize"
summary: "How to configure OpenRouter Broadcast to send traces to Arize AI, including credential setup, OpenInference metadata mapping, and privacy mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md
tags:
  - openrouter
  - arize
  - observability
  - broadcast
  - openinference
  - tracing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Arize

## Key Points

- [[004-wiki/entities/arize-ai|Arize AI]] is an evaluation and observability platform offering agent tracing, evals, and prompt optimization; integrates with OpenRouter via Broadcast ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Setup requires four configuration values: API Key, Space Key, Model ID, and an optional Base URL (default `https://otlp.arize.com`) ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Broadcast must be enabled in OpenRouter Settings > Observability before configuring any destination ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- The Test Connection button verifies the configuration; settings only persist if the test passes ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Arize uses the [[004-wiki/entities/openinference|OpenInference]] semantic convention for tracing; custom metadata from the `trace` field is sent as span attributes in the OTLP payload ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Five standard trace metadata keys map to Arize fields: `trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id` ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Privacy Mode strips prompt and completion content from traces while preserving token usage, costs, timing, model information, and custom metadata ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Notes

- The `user` and `session_id` request fields map to Arize span attributes for user identification and session tracking ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Custom metadata keys beyond the five standard ones are included as span attributes under the `metadata.*` namespace ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Token usage, costs, and model parameters are automatically included as OpenInference-compatible attributes ^[001a-raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Related

- [[004-wiki/entities/arize-ai]]
- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/entities/openinference]]
- [[004-wiki/concepts/observability]]