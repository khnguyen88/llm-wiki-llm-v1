---
title: "OpenRouter Broadcast Grafana Cloud Integration"
summary: "Guide for configuring OpenRouter Broadcast to send traces to Grafana Cloud via the OTLP HTTP/JSON endpoint, including credential setup, TraceQL querying, and custom metadata mapping"
type: summary
sources:
  - raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - grafana
  - tracing
  - otlp
  - observability
  - traceql
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Broadcast Grafana Cloud Integration

## Key Points

- Grafana Cloud receives OpenRouter traces via the standard OTLP HTTP/JSON endpoint using Tempo for distributed tracing ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Configuration requires three Grafana Cloud credentials: OTLP base URL (e.g., `https://otlp-gateway-prod-us-west-0.grafana.net`), numeric Instance ID, and API key with `traces:write` scope ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Broadcast is enabled in OpenRouter at Settings > Observability; the Grafana Cloud configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- OpenRouter traces include resource attributes (`service.name: openrouter`, `service.version: 1.0.0`) and span attributes (`gen_ai.operation.name`, `gen_ai.system`, `gen_ai.request.model`, `gen_ai.response.model`, token usage, finish reason) ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Custom metadata from the `trace` field maps to span attributes under the `trace.metadata.*` namespace; `user` maps to `user.id` and `session_id` maps to `session.id` ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Five standard `trace` keys map to Grafana fields: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Privacy Mode strips prompt and completion content from traces while preserving all other data (token usage, costs, timing, model information, custom metadata) ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Quotes

> "OpenRouter sends traces via the standard OTLP HTTP/JSON endpoint." ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md:6]

> "Custom metadata keys from the `trace` field appear under the `trace.metadata.*` namespace in span attributes." ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md:142]

> "The configuration only saves if the test passes." ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md:58]

## Notes

- Traces may take 1-2 minutes to appear in Grafana Cloud after sending a request ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- The OTLP gateway URL format is `https://otlp-gateway-prod-{region}.grafana.net`, distinct from the main Grafana dashboard URL ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Grafana Cloud offers two methods for viewing traces: Explore with TraceQL and Drilldown > Traces ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Related

- [[entities/grafana_cloud]]
- [[entities/openrouter]]
- [[entities/open_telemetry]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[concepts/traceql]]
- [[concepts/data_privacy]]