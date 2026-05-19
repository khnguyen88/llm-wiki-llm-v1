---
title: "Openrouter Guides Features Broadcast Sentry"
summary: "Setup guide for sending OpenRouter Broadcast traces to Sentry via OTLP, including custom metadata mapping and privacy mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - sentry
  - otlp
  - observability
  - tracing
  - privacy-mode
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Sentry

## Key Points

- Sentry receives OpenRouter Broadcast traces via the OTLP protocol, requiring both an OTLP Traces Endpoint URL and a Sentry DSN for authentication and trace routing ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Setup requires four steps: obtain Sentry OTLP endpoint and DSN from SDK setup, enable Broadcast in OpenRouter Settings > Observability, configure Sentry with the endpoint URL and DSN, then test and save ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Five standard `trace` metadata keys map to Sentry fields: `trace_id` → Trace ID, `trace_name` → Transaction Name, `span_name` → Span Description, `generation_name` → Span Description, `parent_span_id` → Parent Span ID ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Custom metadata keys from the `trace` field are included as span attributes under the `trace.metadata.*` namespace; the `user` field maps to `user.id` and `session_id` maps to `session.id` ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- Sentry automatically correlates LLM traces with existing application error and performance data when using `parent_span_id` ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- When Privacy Mode is enabled, prompt and completion content is excluded from traces while token usage, costs, timing, model information, and custom metadata are still sent ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- The configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

## Quotes

- "Sentry uses OpenTelemetry for trace ingestion. The OTLP endpoint and DSN are both required for proper authentication and trace routing." ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

## Notes

- The OTLP Traces Endpoint URL follows the format `https://o{org_id}.ingest.us.sentry.io/api/{project_id}/integration/otlp/v1/traces`
- The Sentry DSN follows the format `https://{key}@o{org_id}.ingest.us.sentry.io/{project_id}`
- Both values are obtained from Sentry's Settings > Projects > [Project] > SDK Setup > Client Keys (DSN) > OpenTelemetry tab

## Related

- [[entities/sentry]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/open_telemetry]]
- [[concepts/observability]]
- [[concepts/data_privacy]]