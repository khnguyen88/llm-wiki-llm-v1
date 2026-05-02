---
title: "OpenTelemetry"
summary: "A vendor-neutral observability framework for distributed tracing, metrics, and logs that the Agent SDK integrates with via OTLP export"
type: entity
sources:
  - raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md
tags:
  - opentelemetry
  - observability
  - tracing
  - metrics
  - otlp
  - agent-sdk
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
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

## Related

- [[entities/agent_sdk]]
- [[concepts/observability]]
- [[concepts/cost_tracking]]