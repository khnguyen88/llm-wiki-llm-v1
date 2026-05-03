---
title: "Openrouter Guides Features Broadcast Newrelic"
summary: "How to configure OpenRouter Broadcast to send LLM traces to New Relic via OTLP, including license key setup, custom metadata mapping, and Privacy Mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md
tags:
  - openrouter
  - newrelic
  - broadcast
  - otlp
  - observability
  - tracing
  - privacy
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Newrelic

## Key Points

- New Relic is a full-stack observability platform that receives OpenRouter Broadcast traces via the OTLP protocol ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Setup requires a New Relic Ingest License Key and region selection (`us` or `eu`), configured in OpenRouter Settings > Observability after enabling Broadcast ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Five standard `trace` metadata keys map to New Relic fields: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- Custom metadata keys from the `trace` field are included as span attributes under the `trace.metadata.*` namespace; `user` maps to `user.id` and `session_id` maps to `session.id` ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- GenAI semantic conventions (`gen_ai.*` attributes) are used for model, token, and cost data ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]
- When Privacy Mode is enabled, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

## Quotes

- "New Relic receives traces via the OTLP protocol. Custom metadata from the `trace` field is sent as span attributes." ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md:73-74]

- "The configuration only saves if the test passes." ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md:36]

## Notes

- New Relic traces can be viewed in the distributed tracing view, where users can filter by custom attributes using NRQL queries, view metadata in the span attributes panel, and create alerts and dashboards based on metadata fields ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

## Related

- [[entities/new_relic]]
- [[entities/openrouter]]
- [[entities/open_telemetry]]
- [[concepts/broadcast]]
- [[concepts/data_privacy]]
- [[concepts/observability]]