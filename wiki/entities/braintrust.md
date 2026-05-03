---
title: "Braintrust"
summary: "An end-to-end platform for evaluating, monitoring, and improving LLM applications, integrable with OpenRouter as a Broadcast destination"
type: entity
sources:
  - raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md
tags:
  - braintrust
  - observability
  - llm-evaluation
  - monitoring
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Braintrust

An end-to-end platform for evaluating, monitoring, and improving LLM applications. ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]

## Key Facts

- Configurable as a [[concepts/broadcast|Broadcast]] destination in [[entities/openrouter|OpenRouter]], receiving LLM request/response traces for observability ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- API keys are created in Braintrust Account Settings; Project IDs are found in project settings ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Default API base URL is `https://api.braintrust.dev`; can be overridden in the OpenRouter configuration ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Supports four standard metadata keys for trace structure: `trace_id`, `trace_name`, `span_name`, `generation_name` ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- The `user` request field maps to Braintrust's `user_id` in metadata; `session_id` maps to `session_id` in metadata ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Custom metadata keys are included in the span's metadata object; tags are passed through for filtering in the Braintrust UI ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Receives per-call metrics: token counts (prompt, completion, total), cached token usage, reasoning token counts, cost breakdown (input, output, total), and duration/timing ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[entities/arize_ai]]
- [[summaries/openrouter-guides-features-broadcast-braintrust]]