---
title: "Datadog"
summary: "A monitoring and observability platform that provides LLM Observability as a Broadcast destination for OpenRouter"
type: entity
sources:
  - raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md
tags:
  - datadog
  - observability
  - monitoring
  - openrouter
  - broadcast
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Datadog

A monitoring and observability platform providing LLM Observability capabilities, available as a [[004-wiki/concepts/broadcast|Broadcast]] destination in OpenRouter for investigating root causes, monitoring operational performance, and evaluating LLM application quality, privacy, and safety. ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

## Key Facts

- Datadog LLM Observability integrates with OpenRouter Broadcast to send trace data for LLM requests ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Configuration in OpenRouter requires an API key (from Datadog Organization Settings > API Keys), an ML App name, and an optional URL (default `https://api.us5.datadoghq.com`) ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Four `trace` metadata keys map to Datadog fields: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Two tags are automatically added: `service:{ml_app}` and `user_id:{user}`; additional `trace` keys are passed to the span's `meta` object ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- The default Datadog API URL (`https://api.us5.datadoghq.com`) should be overridden for non-US5 regions ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]
- When [[004-wiki/concepts/data-privacy|Privacy Mode]] is enabled, prompt and completion content is excluded from traces while token usage, costs, timing, model information, and custom metadata are still sent ^[001a-raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/concepts/data-privacy]]