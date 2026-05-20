---
title: "Ramp"
summary: "A finance automation platform for managing business expenses, tracking spending, and optimizing costs, with AI usage tracking via OpenRouter"
type: entity
sources:
  - raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md
tags:
  - ramp
  - finance-automation
  - expense-management
  - cost-tracking
  - openrouter
  - broadcast
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Ramp

A finance automation platform that helps businesses manage expenses, track spending, and optimize costs. With Ramp's AI usage tracking, organizations can monitor and control LLM spending through [[004-wiki/entities/openrouter|OpenRouter]]. ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]

## Key Facts

- API key is generated in Ramp's integration settings (Settings > Integrations > OpenRouter > Connect > Generate API Key) ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Default API base URL is `https://api.ramp.com/developer/v1/ai-usage/openrouter`; only change if directed by Ramp ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Receives LLM trace data from OpenRouter via the [[004-wiki/entities/open_telemetry|OpenTelemetry Protocol (OTLP)]], including token usage, cost information, timing metrics, model information, and request/response content ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Supports optional custom HTTP headers passed as a JSON object in the Broadcast configuration ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- AI spend dashboard displays usage data received from OpenRouter traces ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Five standard `trace` metadata keys map to OTLP span attributes: `trace_id` (Trace ID), `trace_name` (Span Name), `span_name` (Span Name), `generation_name` (Span Name), `parent_span_id` (Parent Span ID) ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- The `user` and `session_id` request fields map to `user.id` and `session.id` span attributes respectively; custom `trace` keys appear under `trace.metadata.*` namespace ^[001a-raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/cost_tracking]]
- [[004-wiki/entities/open_telemetry]]