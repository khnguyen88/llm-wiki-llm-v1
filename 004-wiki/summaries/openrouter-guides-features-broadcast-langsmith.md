---
title: "OpenRouter Broadcast LangSmith Integration"
summary: "How to configure LangSmith as a Broadcast destination in OpenRouter to send LLM trace data via the OTEL protocol, with support for custom metadata, hierarchical traces, and Privacy Mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md
tags:
  - openrouter
  - langsmith
  - broadcast
  - observability
  - tracing
  - otep
  - otlp
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Broadcast LangSmith Integration

## Key Points

- LangSmith is LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications, available as a [[concepts/broadcast|Broadcast]] destination in [[entities/openrouter|OpenRouter]] ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Setup requires four steps: obtain a LangSmith API key (prefix `lsv2_pt_...`), enable Broadcast in OpenRouter Settings > Observability, configure LangSmith credentials, and verify with Test Connection ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- LangSmith receives trace data via the OpenTelemetry protocol at the `/otel/v1/traces` endpoint, using GenAI semantic conventions for model name, token counts, costs, and request parameters ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Five metadata keys map to LangSmith trace hierarchy: `trace_id` (Trace ID), `trace_name` (Run Name), `span_name` (Run Name), `generation_name` (Run Name), `parent_span_id` (Parent Run ID) ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Observation types map to LangSmith run types: GENERATION → `llm`, SPAN → `chain`, EVENT → `tool` ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- The `user` field maps to LangSmith User ID and `session_id` maps to LangSmith Session ID for conversation tracking ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- When Privacy Mode is enabled, prompt and completion content is excluded from traces while token usage, costs, timing, model information, and custom metadata are still sent ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

## Notes

- The configuration only saves if the Test Connection check passes, ensuring credentials are valid before activation ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- The default LangSmith endpoint is `https://api.smith.langchain.com`; this can be changed for self-hosted instances ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- Arrays of strings in metadata are passed as tags (comma-separated values) for filtering and organizing traces ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

## Related

- [[entities/langsmith]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/open_telemetry]]
- [[concepts/data_privacy]]
- [[entities/langfuse]]
- [[summaries/openrouter-guides-features-broadcast-overview]]