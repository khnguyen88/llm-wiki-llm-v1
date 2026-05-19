---
title: "Sentry"
summary: "An application monitoring platform that helps developers identify and fix issues in real-time, with AI monitoring capabilities for tracking LLM performance and errors"
type: entity
sources:
  - raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md
tags:
  - sentry
  - monitoring
  - observability
  - otlp
  - error-tracking
  - llm-monitoring
  - broadcast
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Sentry

An application monitoring platform that helps developers identify and fix issues in real-time, with AI monitoring capabilities for tracking LLM performance and errors. ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

## Key Facts

- Uses OpenTelemetry (OTLP) for trace ingestion; both an OTLP Traces Endpoint and DSN are required for authentication and trace routing ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- OTLP Traces Endpoint is obtained from Settings > Projects > [Project] > SDK Setup > Client Keys (DSN) > OpenTelemetry tab; URL format is `https://o{org_id}.ingest.us.sentry.io/api/{project_id}/integration/otlp/v1/traces` ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- DSN is obtained from the same SDK Setup page; format is `https://{key}@o{org_id}.ingest.us.sentry.io/{project_id}` ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Available as a [[concepts/broadcast|Broadcast]] destination on [[entities/openrouter|OpenRouter]], receiving LLM traces via OTLP protocol ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Maps five standard `trace` metadata keys: `trace_id` → Trace ID, `trace_name` → Transaction Name, `span_name` → Span Description, `generation_name` → Span Description, `parent_span_id` → Parent Span ID ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Custom metadata from the `trace` field maps to `trace.metadata.*` span attributes; the `user` field maps to `user.id` and `session_id` maps to `session.id` ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Automatically correlates LLM traces with existing application error and performance data when `parent_span_id` is provided ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- When [[concepts/data_privacy|Privacy Mode]] is enabled, prompt and completion content is excluded from traces while token usage, costs, timing, model information, and custom metadata are still sent ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Traces can be viewed in Sentry's Performance or Traces view ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/open_telemetry]]
- [[concepts/observability]]
- [[concepts/data_privacy]]
- [[summaries/openrouter-guides-features-broadcast-sentry]]