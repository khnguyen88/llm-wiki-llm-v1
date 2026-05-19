---
title: "OpenTelemetry"
summary: "A vendor-neutral observability framework for distributed tracing, metrics, and logs that the Agent SDK integrates with via OTLP export"
type: entity
sources:
  - raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md
  - raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md
  - raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md
  - raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md
  - raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md
  - raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md
  - raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md
tags:
  - opentelemetry
  - observability
  - tracing
  - metrics
  - otlp
  - agent-sdk
  - broadcast
  - grafana
  - gen-ai
  - langsmith
  - newrelic
  - axiom
  - jaeger
  - honeycomb
  - sentry
  - lightstep
  - webhook
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# OpenTelemetry

A vendor-neutral observability framework providing standardized APIs and SDKs for distributed tracing, metrics, and logs. The Agent SDK integrates with OpenTelemetry by exporting telemetry from the Claude Code CLI subprocess to any backend that accepts the OpenTelemetry Protocol (OTLP). ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

## Key Facts

- Compatible OTLP backends include Honeycomb, Datadog, Grafana, Langfuse, and self-hosted collectors ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- The Agent SDK emits three independent OpenTelemetry signals: metrics (token and cost counters), log events (prompt and tool result records), and traces (spans for interactions, model requests, tool calls, and hooks) ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Each signal has its own enable switch and exporter, allowing selective activation: `OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER`, `OTEL_TRACES_EXPORTER` ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Traces require an additional beta flag (`CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`) beyond the exporter setting ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- OTLP HTTP transport is configured via `OTEL_EXPORTER_OTLP_PROTOCOL` (typically `http/protobuf`), `OTEL_EXPORTER_OTLP_ENDPOINT`, and `OTEL_EXPORTER_OTLP_HEADERS` ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- The `console` exporter must not be used with the Agent SDK because the SDK uses stdout as its message channel ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- W3C trace context propagation (`TRACEPARENT`/`TRACESTATE`) is automatically injected by the SDK, linking CLI subprocess spans to the parent application's trace ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Resource attributes (`OTEL_SERVICE_NAME`, `OTEL_RESOURCE_ATTRIBUTES`) tag all emitted spans, metrics, and events for filtering in multi-agent deployments ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- OpenRouter Broadcast supports an OpenTelemetry Collector destination for sending traces to any OTLP-compatible backend ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- OpenRouter Broadcast's `parent_span_id` field enables nesting OpenRouter traces under existing OpenTelemetry spans from a user's own tracing instrumentation ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- OpenRouter traces sent to Grafana Cloud use OpenTelemetry GenAI semantic conventions for span attributes: `gen_ai.operation.name`, `gen_ai.system`, `gen_ai.request.model`, `gen_ai.response.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.usage.total_tokens`, `gen_ai.response.finish_reason` ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Grafana Cloud receives OpenRouter traces via the OTLP HTTP/JSON endpoint into Grafana Tempo, enabling distributed tracing queries with TraceQL ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- LangSmith receives OpenRouter traces via the OTEL endpoint at `/otel/v1/traces`, using GenAI semantic conventions for model name, token counts, costs, and request parameters; LangSmith-specific attributes include trace name, span kind, user ID, and custom metadata ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]
- New Relic receives OpenRouter Broadcast traces via the OTLP protocol, with GenAI semantic conventions (`gen_ai.*` attributes) used for model, token, and cost data; custom metadata maps under `trace.metadata.*` span attributes ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- OpenRouter's OpenTelemetry Collector Broadcast destination sends traces via OTLP/HTTP with JSON encoding to any compatible backend; compatible backends include Axiom, Jaeger, Grafana Tempo, Honeycomb, Lightstep, and self-hosted collectors ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- The OTLP Collector destination requires an endpoint URL (e.g., `https://api.axiom.co/v1/traces` for Axiom, `https://your-collector.example.com:4318/v1/traces` for self-hosted) and optional custom HTTP headers for authentication ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- [[entities/sentry|Sentry]] uses OTLP for trace ingestion, receiving OpenRouter Broadcast traces at its OTLP Traces Endpoint (format: `https://o{org_id}.ingest.us.sentry.io/api/{project_id}/integration/otlp/v1/traces`); both the OTLP endpoint and a Sentry DSN are required for authentication and trace routing ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]
- OpenRouter's Webhook Broadcast destination sends traces in OTLP JSON format to any HTTP endpoint; the `resourceSpans` array contains span data with GenAI semantic conventions (`gen_ai.request.model`, `gen_ai.usage.prompt_tokens`, `gen_ai.usage.completion_tokens`) and custom metadata under `trace.metadata.*` namespace ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/openrouter]]
- [[concepts/observability]]
- [[concepts/broadcast]]
- [[concepts/cost_tracking]]
- [[entities/grafana_cloud]]
- [[concepts/traceql]]
- [[entities/langsmith]]
- [[entities/new_relic]]
- [[entities/axiom]]
- [[summaries/openrouter-guides-features-broadcast-otel-collector]]
- [[entities/sentry]]
- [[concepts/webhook]]
- [[summaries/openrouter-guides-features-broadcast-webhook]]