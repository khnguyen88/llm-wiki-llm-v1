---
title: "Openrouter Guides Features Broadcast Opik"
summary: "Guide for configuring Comet Opik as a Broadcast destination in OpenRouter, including setup steps, custom metadata mapping, and Privacy Mode behavior"
type: summary
sources:
  - raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - opik
  - observability
  - tracing
  - comet
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Opik

## Key Points

- Comet Opik is an open-source platform for evaluating, testing, and monitoring LLM applications, available as a Broadcast destination on OpenRouter ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Setup requires four steps: obtain Opik API credentials (workspace, project, API key from Settings > API Keys), enable Broadcast in OpenRouter Observability settings, configure the Comet Opik destination with API key, workspace, and project name, then test and save ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Four metadata keys map from the `trace` field to Opik: `trace_id` → trace metadata (`openrouter_trace_id`), `trace_name` → Trace Name, `span_name` → Span Name, `generation_name` → Span Name ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Custom metadata keys from the `trace` field are included in both trace and span metadata objects; cost information (input, output, total) is automatically added to span metadata ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Opik uses UUIDv7 format for trace and span IDs internally; original OpenRouter IDs are stored in metadata as `openrouter_trace_id` and `openrouter_observation_id` ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- When Privacy Mode is enabled for the Opik destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

## Notes

- The Comet API key prefix is `opik_...` ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- The `user` field maps to user identification in trace metadata ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]
- Model parameters and finish reasons are included in span metadata when available ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

## Related

- [[entities/comet_opik]]
- [[concepts/broadcast]]
- [[entities/openrouter]]
- [[concepts/data_privacy]]