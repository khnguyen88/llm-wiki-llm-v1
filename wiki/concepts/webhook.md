---
title: "Webhook"
summary: "An OpenRouter Broadcast destination that sends OTLP-formatted traces to any HTTP endpoint accepting JSON payloads"
type: concept
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

# Webhook

An [[entities/openrouter|OpenRouter]] [[concepts/broadcast|Broadcast]] destination that sends LLM request/response traces to any HTTP endpoint capable of receiving JSON payloads. Traces are delivered in [[entities/open_telemetry|OpenTelemetry Protocol (OTLP)]] JSON format, enabling integration with any OTLP-aware system or custom observability pipeline. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

## Key Points

- The webhook endpoint must accept `application/json`, return a 2xx status code on success, and be publicly accessible from the internet ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Configuration requires a URL, an optional HTTP method (`POST` default or `PUT`), and optional custom headers as a JSON object for authentication ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Test Connection sends an empty OTLP payload with `X-Test-Connection: true` header; a 2xx or 400 status code is accepted for the test to pass; configuration only saves on success ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Custom metadata from the `trace` field maps to `trace.metadata.*` span attributes in the OTLP JSON payload ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]
- Privacy Mode excludes prompt and completion content from traces while preserving all other data ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

## Details

### Setup

Setup requires enabling Broadcast in Settings > Observability, then configuring the Webhook destination with a URL (e.g., `https://api.example.com/traces`), optional HTTP method, and optional authentication headers. After configuration, clicking Test Connection verifies the setup — OpenRouter sends an empty OTLP payload to the endpoint and checks for a 2xx (or 400) response. The configuration only saves if the test passes. A final verification step sends a real API request through OpenRouter to confirm the webhook endpoint receives trace data. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

### Payload Format

Traces are sent in OTLP JSON format. Each payload contains a `resourceSpans` array with span data including trace and span IDs, timestamps and duration, model and provider information, token usage and cost, and request/response content (with multimodal content stripped). The `service.name` resource attribute is set to `"openrouter"`. GenAI semantic conventions (`gen_ai.request.model`, `gen_ai.usage.prompt_tokens`, `gen_ai.usage.completion_tokens`) are used for model and token attributes. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

### Custom Metadata

The `trace` field in API requests supports five standard metadata keys that map to dedicated OTLP fields:

| Key               | OTLP Mapping   | Description                                      |
| ----------------- | -------------- | ------------------------------------------------ |
| `trace_id`        | `traceId`      | Group multiple requests into a single trace      |
| `trace_name`      | Span `name`    | Custom name for the root span                    |
| `span_name`       | Span `name`    | Name for intermediate spans in the hierarchy     |
| `generation_name` | Span `name`    | Name for the LLM generation span                 |
| `parent_span_id`  | `parentSpanId` | Link to an existing span in your trace hierarchy |

Arbitrary metadata keys appear as span attributes under the `trace.metadata.*` namespace. The `user` field maps to `user.id` and `session_id` maps to `session.id` in span attributes. All standard GenAI semantic conventions (`gen_ai.*`) are included for model, token, and cost data. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

### Privacy Mode

When Privacy Mode is enabled for the Webhook destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

### Use Cases

The Webhook destination suits custom analytics pipelines (data warehouse or analytics system integration), internal monitoring tools (proprietary observability platforms), event-driven architectures (triggering workflows based on LLM usage), compliance logging (storing traces in systems meeting regulatory requirements), and development/testing (using services like webhook.site to inspect payloads). For production use, the webhook endpoint should be highly available with retry logic for failed deliveries. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/open_telemetry]]
- [[concepts/data_privacy]]
- [[summaries/openrouter-guides-features-broadcast-webhook]]