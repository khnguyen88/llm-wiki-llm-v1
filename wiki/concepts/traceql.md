---
title: "TraceQL"
summary: "A query language for Grafana Tempo that filters and searches distributed traces using resource and span attributes, duration, and status"
type: concept
sources:
  - raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md
tags:
  - traceql
  - grafana
  - tracing
  - query-language
  - observability
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# TraceQL

A query language for Grafana Tempo used to filter and search distributed traces by resource attributes, span attributes, duration, status, and custom metadata. OpenRouter Broadcast traces sent to Grafana Cloud can be queried using TraceQL. ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Key Points

- Accessed via the Explore view in Grafana Cloud by selecting a Tempo data source and switching to the TraceQL tab ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Queries OpenRouter traces using `{ resource.service.name = "openrouter" }` as the base filter ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Supports filtering by model: `{ resource.service.name = "openrouter" && span.gen_ai.request.model = "openai/gpt-4-turbo" }` ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Supports duration queries for slow requests: `{ resource.service.name = "openrouter" && duration > 5s }` ^[raw/document/openrouter/openrouter/055-guides-features-broadcast-grafana-2026-04-29.md]
- Supports filtering by user ID, error status, and model name patterns using `=`, `=~` (regex), and comparison operators ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Custom metadata from OpenRouter's `trace` field is queryable under the `trace.metadata.*` namespace: `{ resource.service.name = "openrouter" && span.trace.metadata.environment = "production" }` ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Details

TraceQL is the native query language for Grafana Tempo, the distributed tracing backend included in Grafana Cloud. When OpenRouter Broadcast sends traces to Grafana Cloud, they become queryable through TraceQL in the Explore view. OpenRouter traces use the `openrouter` service name and include span attributes following the OpenTelemetry GenAI semantic conventions (`gen_ai.*`).

Custom metadata attached to OpenRouter requests via the `trace` field appears as span attributes under the `trace.metadata.*` namespace, enabling filtering by arbitrary keys such as environment, alert ID, or other application-specific identifiers. The `user` and `session_id` request fields map to `user.id` and `session.id` span attributes respectively, also queryable via TraceQL. ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Related

- [[entities/grafana_cloud]]
- [[entities/openrouter]]
- [[entities/open_telemetry]]
- [[concepts/broadcast]]
- [[concepts/observability]]