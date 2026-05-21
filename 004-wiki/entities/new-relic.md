---
title: "New Relic"
summary: "A full-stack observability platform for monitoring applications, infrastructure, and digital experiences; available as an OpenRouter Broadcast destination receiving traces via OTLP"
type: entity
sources:
  - raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md
tags:
  - newrelic
  - observability
  - monitoring
  - tracing
  - otlp
  - broadcast
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# New Relic

A full-stack observability platform for monitoring applications, infrastructure, and digital experiences. It is available as a [[004-wiki/concepts/broadcast|Broadcast]] destination on [[004-wiki/entities/openrouter|OpenRouter]], receiving LLM traces via the [[004-wiki/entities/open-telemetry|OpenTelemetry]] OTLP protocol. ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

## Key Facts

- Receives OpenRouter Broadcast traces via the OTLP protocol, with custom metadata from the `trace` field sent as span attributes ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Configuration requires a New Relic Ingest License Key (created under API Keys in account settings) and a region selection (`us` or `eu`) ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Setup is done in OpenRouter Settings > Observability by enabling Broadcast, then clicking the edit icon next to New Relic to enter credentials ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Five standard `trace` metadata keys map to New Relic fields: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Custom metadata keys from the `trace` field are included as span attributes under the `trace.metadata.*` namespace ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- The `user` request field maps to `user.id` and `session_id` maps to `session.id` in span attributes ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- GenAI semantic conventions (`gen_ai.*` attributes) are used for model, token, and cost data ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Distributed tracing view supports filtering traces by custom attributes using NRQL queries, viewing custom metadata in the span attributes panel, and creating alerts and dashboards based on metadata fields ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- When [[004-wiki/concepts/data-privacy|Privacy Mode]] is enabled for the New Relic destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally ^[001a-raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/entities/open-telemetry]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/data-privacy]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/summaries/openrouter-guides-features-broadcast-newrelic]]