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

- [[entities/arize_ai|Arize AI]] is an evaluation and observability platform offering agent tracing, evals, and prompt optimization; integrates with OpenRouter via Broadcast ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Setup requires four configuration values: API Key, Space Key, Model ID, and an optional Base URL (default `https://otlp.arize.com`) ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Broadcast must be enabled in OpenRouter Settings > Observability before configuring any destination ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- The Test Connection button verifies the configuration; settings only persist if the test passes ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Arize uses the [[entities/openinference|OpenInference]] semantic convention for tracing; custom metadata from the `trace` field is sent as span attributes in the OTLP payload ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Five standard trace metadata keys map to Arize fields: `trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id` ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Privacy Mode strips prompt and completion content from traces while preserving token usage, costs, timing, model information, and custom metadata ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Notes

- The `user` and `session_id` request fields map to Arize span attributes for user identification and session tracking ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Custom metadata keys beyond the five standard ones are included as span attributes under the `metadata.*` namespace ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]
- Token usage, costs, and model parameters are automatically included as OpenInference-compatible attributes ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

## Related

- [[entities/arize_ai]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/openinference]]
- [[concepts/observability]]