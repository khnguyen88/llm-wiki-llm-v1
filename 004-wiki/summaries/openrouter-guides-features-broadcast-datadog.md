---
title: "Openrouter Guides Features Broadcast Datadog"
summary: "How to configure Datadog LLM Observability as a Broadcast destination in OpenRouter, including setup steps, custom metadata mapping, and Privacy Mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md
tags:
  - openrouter
  - datadog
  - broadcast
  - observability
  - llm-observability
  - tracing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Datadog

## Key Points

- Datadog LLM Observability integrates with OpenRouter Broadcast to investigate root causes, monitor operational performance, and evaluate LLM application quality, privacy, and safety ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Setup requires creating a Datadog API key (Organization Settings > API Keys), enabling Broadcast in OpenRouter (Settings > Observability), and configuring the Datadog destination with the API key, ML App name, and optional URL override ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Four metadata keys from the `trace` field map to Datadog: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Datadog automatically adds two tags: `service:{ml_app}` (from the configured ML App name) and `user_id:{user}` (from the request `user` field); additional `trace` keys are passed to the span's `meta` object ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- The default Datadog API URL is `https://api.us5.datadoghq.com`; this should be changed for non-US5 regions ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- When [[concepts/data_privacy|Privacy Mode]] is enabled for the Datadog destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

## Notes

- The `trace_id` metadata key groups multiple OpenRouter requests into a single Datadog trace, enabling correlation of multi-step LLM workflows ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

## Related

- [[entities/datadog]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[concepts/data_privacy]]