---
title: "Claude Code Agent Sdk Observability"
summary: "Agent SDK integrates OpenTelemetry to export traces, metrics, and log events from the CLI subprocess to any OTLP-compatible observability backend"
type: summary
sources:
  - raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md
tags:
  - agent-sdk
  - observability
  - opentelemetry
  - tracing
  - metrics
  - monitoring
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Observability

## Key Points

- The Agent SDK exports OpenTelemetry traces, metrics, and log events to any OTLP-compatible backend (Honeycomb, Datadog, Grafana, Langfuse, or self-hosted collectors) ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- The CLI subprocess produces all telemetry; the SDK itself does not emit telemetry but passes configuration through environment variables to the child process ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Three independent OpenTelemetry signals with separate enable switches: metrics (`OTEL_METRICS_EXPORTER`), log events (`OTEL_LOGS_EXPORTER`), and traces (`OTEL_TRACES_EXPORTER` plus `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`) ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Telemetry is off by default; requires `CLAUDE_CODE_ENABLE_TELEMETRY=1` and at least one exporter to activate ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Four trace span types: `claude_code.interaction` (agent turn), `claude_code.llm_request` (API call), `claude_code.tool` (tool invocation), `claude_code.hook` (hook execution); subagent spans nest under the parent tool span ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- W3C trace context auto-propagation links agent traces to the parent application trace via `TRACEPARENT` injection into the CLI subprocess; commands run via the Bash tool also inherit the trace context ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Sensitive data (prompt text, tool inputs, API bodies) is excluded by default; opt-in variables (`OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_RAW_API_BODIES`) add content to exports ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

## Quotes

- "The SDK does not produce telemetry of its own. Instead, it passes configuration through to the CLI process, and the CLI exports directly to your collector." ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- "Do not set `console` as an exporter value when running through the SDK." ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

## Notes

- For short-lived processes, telemetry batching can cause data loss; reduce export intervals via `OTEL_METRIC_EXPORT_INTERVAL`, `OTEL_LOGS_EXPORT_INTERVAL`, and `OTEL_TRACES_EXPORT_INTERVAL` ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Default service name is `claude-code`; override with `OTEL_SERVICE_NAME` and add resource attributes via `OTEL_RESOURCE_ATTRIBUTES` to filter by agent in multi-agent deployments ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- In Python, `env` merges on top of inherited environment; in TypeScript, `env` replaces it entirely, so include `...process.env` ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Tracing is in beta; span names and attributes may change between releases ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Interactive CLI sessions ignore inbound `TRACEPARENT`; only Agent SDK and `claude -p` runs honor it ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/open_telemetry]]
- [[concepts/observability]]
- [[concepts/cost_tracking]]
- [[concepts/hooks]]