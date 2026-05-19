---
title: "Openrouter Guides Features Broadcast Braintrust"
summary: "Setup guide for configuring Braintrust as a Broadcast destination in OpenRouter, including custom metadata mapping, metrics, and Privacy Mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md
tags:
  - openrouter
  - braintrust
  - broadcast
  - observability
  - llm-evaluation
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Braintrust

## Key Points

- [[entities/braintrust|Braintrust]] is an end-to-end platform for evaluating, monitoring, and improving LLM applications, configurable as a [[concepts/broadcast|Broadcast]] destination in OpenRouter ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Setup requires a Braintrust API key (from Account Settings) and Project ID (from project settings), plus an optional Base URL defaulting to `https://api.braintrust.dev` ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Broadcast must be enabled in OpenRouter via Settings > Observability before configuring individual destinations ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Configuration only saves if the Test Connection check passes, ensuring credentials are valid before activation ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Custom metadata keys supported: `trace_id` (groups logs into traces), `trace_name` (display name), `span_name` (intermediate spans), `generation_name` (LLM span name) ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Braintrust receives detailed metrics per LLM call: token counts, cached token usage, reasoning tokens, cost information (input/output/total), and duration/timing ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Privacy Mode strips prompt and completion content from traces while preserving all other data (token usage, costs, timing, model info, custom metadata) ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]

## Notes

- The `user` field in API requests maps to Braintrust's `user_id` metadata; `session_id` maps to `session_id` metadata ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]
- Custom metadata keys beyond the standard four are included in the span's metadata object; tags are passed through for filtering in the Braintrust UI ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]

## Related

- [[entities/braintrust]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[summaries/openrouter-guides-features-broadcast-overview]]
- [[summaries/openrouter-guides-features-broadcast-arize]]