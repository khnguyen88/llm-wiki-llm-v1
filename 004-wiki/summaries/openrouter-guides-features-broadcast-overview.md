---
title: "OpenRouter Broadcast Feature Overview"
summary: "OpenRouter Broadcast automatically sends request traces to external observability platforms with per-destination filtering, sampling, and privacy controls"
type: summary
sources:
  - raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - observability
  - tracing
  - privacy
  - sampling
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Broadcast Feature Overview

## Key Points

- Broadcast sends trace data for all API requests to configured external observability destinations automatically, with no application code changes required ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- 17 stable destinations are available including Langfuse, Datadog, Grafana Cloud, ClickHouse, S3, Snowflake, and a generic Webhook; 14 more are in development ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Trace data includes request/response content (with multimodal stripped), token usage, cost, timing, model info, and tool usage metadata ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Optional enrichment fields (`user`, `session_id`, `trace` with custom metadata) allow grouping requests by user, session, or hierarchical workflow ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Each destination can be filtered by API key and configured with an independent sampling rate; sampling is deterministic per session so complete sessions stay intact ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Privacy Mode per destination strips prompt and completion content from traces while preserving token counts, costs, timing, and metadata ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Destination credentials are encrypted at rest and traces are sent asynchronously after request completion, adding no latency to API responses ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

## Quotes

- "Sampling is deterministic: when you provide a `session_id`, all traces within that session will be consistently included or excluded together." ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

## Notes

- Organization admins can configure shared Broadcast destinations for all API keys within an organization ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- The `trace` field accepts arbitrary JSON and passes through to all configured destinations; certain keys (`trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id`) have special meaning for trace hierarchy ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- `parent_span_id` enables nesting OpenRouter traces under existing external tracing spans (e.g., OpenTelemetry) ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[concepts/input_output_logging]]
- [[entities/open_telemetry]]