---
title: "Openrouter Guides Features Broadcast Weave"
summary: "Configuration guide for sending OpenRouter Broadcast traces to W&B Weave for LLM observability, including custom metadata mapping and privacy controls"
type: summary
sources:
  - raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - wandb-weave
  - observability
  - tracing
  - privacy
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Weave

## Key Points

- [[entities/wandb_weave|W&B Weave]] is an observability platform for tracking and evaluating LLM applications, available as a [[concepts/broadcast|Broadcast]] destination on OpenRouter ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Setup requires a W&B API key (from User Settings), enabling Broadcast in OpenRouter Settings > Observability, and configuring Weave with API Key, Entity, Project, and optional Base URL (default `https://trace.wandb.ai`) ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Three custom metadata keys are supported: `trace_id` maps to the `openrouter_trace_id` attribute, `trace_name` and `generation_name` both map to `op_name` ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Weave organizes trace data into Attributes (metadata like user IDs, trace identifiers), Inputs (request data, messages, model parameters), and Summary (token usage, costs, timing) ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- The `user` request field maps to `user_id` in attributes; `session_id` maps to `session_id` in attributes; custom `trace` keys merge into the call's attributes ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Model parameters (`temperature`, `max_tokens`, `top_p`) are included in inputs for easy filtering ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Privacy Mode excludes prompt and completion content from traces while sending all other data (token usage, costs, timing, model info, custom metadata) normally ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

## Notes

- The configuration only saves if the Test Connection check passes, consistent with other Broadcast destinations ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

## Related

- [[entities/wandb_weave]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[concepts/data_privacy]]