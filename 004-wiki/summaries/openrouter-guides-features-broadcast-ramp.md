---
title: "Openrouter Guides Features Broadcast Ramp"
summary: "Setup guide for sending OpenRouter LLM usage traces to Ramp for AI spend monitoring and expense management"
type: summary
sources:
  - raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md
tags:
  - openrouter
  - ramp
  - broadcast
  - observability
  - cost-tracking
  - otlp
  - finance-automation
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Ramp

## Key Points

- Ramp is a finance automation platform that monitors and controls LLM spending through OpenRouter's [[concepts/broadcast|Broadcast]] feature ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Setup requires a Ramp API key (generated in Settings > Integrations), enabling Broadcast in OpenRouter (Settings > Observability), and configuring the Ramp destination with the API key and optional Base URL/Headers ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Traces are sent via the OpenTelemetry Protocol (OTLP), including token usage, cost, timing, model information, and request/response content ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Five standard `trace` metadata keys map to OTLP span attributes: `trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id` ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- The `user` field maps to `user.id` and `session_id` maps to `session.id` in span attributes; custom `trace` keys appear under `trace.metadata.*` namespace ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Privacy Mode excludes prompt and completion content from traces while preserving token usage, costs, timing, model information, and custom metadata ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]

## Quotes

- "Ramp is a finance automation platform that helps businesses manage expenses, track spending, and optimize costs." ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md:8]

## Notes

- The default Ramp Base URL is `https://api.ramp.com/developer/v1/ai-usage/openrouter` and should only be changed if directed by Ramp ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]
- Standard GenAI semantic conventions (`gen_ai.*`) are used for model, token usage, and cost attributes in the OTLP payload ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]

## Related

- [[entities/ramp]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/open_telemetry]]
- [[concepts/cost_tracking]]
- [[concepts/data_privacy]]