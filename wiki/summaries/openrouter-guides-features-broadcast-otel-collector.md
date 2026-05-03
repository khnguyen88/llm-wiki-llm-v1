---
title: "Openrouter Guides Features Broadcast Otel Collector"
summary: "Guide for configuring OpenRouter's OpenTelemetry Collector broadcast destination to send traces to any OTLP-compatible backend"
type: summary
sources:
  - raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - opentelemetry
  - otlp
  - tracing
  - observability
  - axiom
  - jaeger
  - grafana-tempo
  - honeycomb
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Otel Collector

## Key Points

- OpenRouter can send traces to any backend that supports the OpenTelemetry Protocol (OTLP) over HTTP, including Axiom, Jaeger, Grafana Tempo, Honeycomb, Lightstep, and self-hosted collectors ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- Configuration requires enabling Broadcast in Settings > Observability, then adding an OpenTelemetry Collector destination with an OTLP endpoint URL and optional authentication headers ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- Custom metadata from the `trace` field maps to OTLP span attributes: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- Arbitrary `trace` metadata keys are included as span attributes under the `trace.metadata.*` namespace; standard GenAI semantic conventions (`gen_ai.*`) are used for model, token usage, and cost attributes ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- The `user` field maps to `user.id` and `session_id` maps to `session.id` in span attributes ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- When Privacy Mode is enabled, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) continues to be sent ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- The configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

## Notes

- Axiom setup requires endpoint `https://api.axiom.co/v1/traces` with `Authorization: Bearer xaat-xxx` and `X-Axiom-Dataset: your-dataset` headers ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- Self-hosted collectors need an OTLP receiver configured on a publicly accessible endpoint, typically ending in `/v1/traces` ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- OpenRouter sends traces using OTLP/HTTP protocol with JSON encoding; backends must accept OTLP over HTTP on `/v1/traces` ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/open_telemetry]]
- [[entities/axiom]]
- [[concepts/observability]]
- [[concepts/data_privacy]]