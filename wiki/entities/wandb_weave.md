---
title: "W&B Weave"
summary: "An observability platform by Weights & Biases for tracking and evaluating LLM applications, available as an OpenRouter Broadcast destination"
type: entity
sources:
  - raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md
tags:
  - wandb-weave
  - observability
  - tracing
  - llm-evaluation
  - openrouter-broadcast
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# W&B Weave

An observability platform by Weights & Biases for tracking and evaluating LLM applications. Available as a [[concepts/broadcast|Broadcast]] destination on [[entities/openrouter|OpenRouter]]. ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

## Key Facts

- API keys are obtained from W&B User Settings at `wandb.ai/settings` ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- OpenRouter Broadcast configuration requires: API Key, Entity (W&B username or team name), Project name, and optional Base URL (default `https://trace.wandb.ai`) ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Three custom metadata keys are supported from the `trace` field: `trace_id` maps to the `openrouter_trace_id` attribute, `trace_name` maps to `op_name`, `generation_name` maps to `op_name` ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Trace data is organized into three categories: Attributes (metadata about the call — user IDs, organization IDs, trace identifiers, custom metadata), Inputs (actual request data including messages and model parameters like `temperature`, `max_tokens`, `top_p`), and Summary (token usage, costs, and timing metrics) ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- The `user` request field maps to `user_id` in attributes; `session_id` maps to `session_id` in attributes ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- Custom metadata keys from the `trace` field are merged into the call's attributes ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]
- When Privacy Mode is enabled for this destination, prompt and completion content is excluded from traces; all other data (token usage, costs, timing, model information, custom metadata) is still sent normally ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[concepts/data_privacy]]