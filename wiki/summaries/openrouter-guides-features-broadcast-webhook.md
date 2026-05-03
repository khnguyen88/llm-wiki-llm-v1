---
title: "Openrouter Guides Features Broadcast Webhook"
summary: "OpenRouter Broadcast webhook destination sends OTLP-formatted traces to any HTTP endpoint, with custom headers, configurable HTTP method, and custom metadata support"
type: summary
sources:
  - raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - webhook
  - otlp
  - observability
  - custom-metadata
  - privacy-mode
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Webhook

## Key Points

- Webhook is a Broadcast destination that sends traces to any HTTP endpoint accepting JSON payloads via POST or PUT ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Traces are sent in OpenTelemetry Protocol (OTLP) JSON format, making them compatible with any OTLP-aware system ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Configuration requires a URL, optional HTTP method (POST default or PUT), and optional custom headers as a JSON object for authentication ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- The Test Connection sends an empty OTLP payload with an `X-Test-Connection: true` header; configuration only saves if the test passes (2xx or 400 status accepted) ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Custom metadata from the `trace` field maps to `trace.metadata.*` span attributes; five standard keys (`trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id`) map to dedicated OTLP fields ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Privacy Mode excludes prompt and completion content while preserving token usage, costs, timing, model information, and custom metadata ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Use cases include custom analytics pipelines, internal monitoring tools, event-driven architectures, compliance logging, and development/testing ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

## Quotes

- "Webhook allows you to send traces to any HTTP endpoint that can receive JSON payloads." ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md:3]
- "For production use, ensure your webhook endpoint is highly available and can handle the expected volume of traces. Consider implementing retry logic on your end for any failed deliveries." ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md:73-74]

## Notes

- The `user` field maps to `user.id` and `session_id` maps to `session.id` in span attributes, consistent with other Broadcast destinations
- Multimodal content is stripped from request and response content in traces
- The endpoint must be publicly accessible from the internet

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/webhook]]
- [[entities/open_telemetry]]
- [[concepts/data_privacy]]