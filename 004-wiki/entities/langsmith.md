---
title: "LangSmith"
summary: "LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications, available as a Broadcast destination in OpenRouter"
type: entity
sources:
  - raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md
tags:
  - langsmith
  - langchain
  - observability
  - tracing
  - llm-engineering
  - broadcast
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# LangSmith

LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications. ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

## Key Facts

- Available as a [[004-wiki/concepts/broadcast|Broadcast]] destination in [[004-wiki/entities/openrouter|OpenRouter]], configured in Settings > Observability ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Authentication uses a LangSmith API key (prefix `lsv2_pt_...`) created in Settings > API Keys ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Default endpoint is `https://api.smith.langchain.com`; configurable for self-hosted instances ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Receives trace data via the [[004-wiki/entities/open-telemetry|OpenTelemetry]] protocol at the `/otel/v1/traces` endpoint, ensuring compatibility with native tracing infrastructure ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Trace data includes GenAI semantic conventions (model name, token counts, costs, request parameters), LangSmith-specific attributes (trace name, span kind, user ID, custom metadata), and error handling events ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Maps five metadata keys: `trace_id` (Trace ID), `trace_name` (Run Name), `span_name` (Run Name), `generation_name` (Run Name), `parent_span_id` (Parent Run ID) ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Observation types map to LangSmith run types: GENERATION → `llm`, SPAN → `chain`, EVENT → `tool` ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- The `user` field maps to Langsmith User ID and `session_id` maps to LangSmith Session ID for conversation tracking ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Custom metadata keys are passed as span attributes and viewable in run details; string arrays in metadata become comma-separated tags ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Trace details include input/output messages, token usage (prompt, completion, total), cost information, model and provider information, and timing/latency metrics ^[001a-raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/entities/open-telemetry]]
- [[004-wiki/concepts/data-privacy]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/entities/langfuse]]
- [[004-wiki/summaries/openrouter-guides-features-broadcast-langsmith]]