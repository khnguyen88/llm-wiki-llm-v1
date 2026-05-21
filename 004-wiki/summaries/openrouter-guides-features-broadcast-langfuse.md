---
title: "OpenRouter Guides Features Broadcast Langfuse"
summary: "How to configure OpenRouter Broadcast to send LLM traces to Langfuse, including API key setup, custom metadata mapping, and Privacy Mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md
tags:
  - openrouter
  - langfuse
  - broadcast
  - observability
  - tracing
  - privacy
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Guides Features Broadcast Langfuse

## Key Points

- Langfuse is an open-source LLM engineering platform for tracing, evaluating, and debugging LLM applications ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Setup requires five steps: create a Langfuse API key pair (Secret + Public Key), enable Broadcast in OpenRouter Settings > Observability, configure the Langfuse destination with keys and optional Base URL, test the connection, then send a test trace ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- The configuration only saves if the Test Connection check passes ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- The `trace` field in API requests supports five standard metadata keys: `trace_id`, `trace_name`, `span_name`, `generation_name`, and `parent_span_id` ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Additional request-level fields map to Langfuse concepts: `user` → User ID for user-level analytics, `session_id` → Session ID for grouping conversations ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Any additional keys in the `trace` object beyond the five standard keys are passed as trace metadata for filtering and analysis in Langfuse ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Privacy Mode excludes prompt and completion content from traces while preserving token usage, costs, timing, model information, and custom metadata ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]

## Notes

- The default Langfuse Base URL is `https://us.cloud.langfuse.com`; this should be changed for other regions or self-hosted instances ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- The `trace` field enables hierarchical trace structures in Langfuse, e.g., a trace containing spans containing generations ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]

## Related

- [[004-wiki/entities/langfuse]]
- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/data-privacy]]
- [[004-wiki/concepts/observability]]