---
title: "Langfuse"
summary: "An open-source LLM engineering platform for tracing, evaluating, and debugging LLM applications"
type: entity
sources:
  - raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md
tags:
  - langfuse
  - observability
  - tracing
  - llm-engineering
  - open-source
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Langfuse

An open-source LLM engineering platform for tracing, evaluating, and debugging LLM applications. ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]

## Key Facts

- Provides tracing, evaluation, and debugging capabilities for LLM applications ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Available as a [[004-wiki/concepts/broadcast|Broadcast]] destination in [[004-wiki/entities/openrouter|OpenRouter]], configured in Settings > Observability ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Authentication uses a key pair (Secret Key and Public Key) created in Langfuse project Settings > API Keys ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Default Base URL is `https://us.cloud.langfuse.com`; configurable for other regions or self-hosted deployments ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Supports hierarchical trace structures with traces containing spans containing generations, controlled via the `trace` metadata field ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Maps five standard `trace` keys to Langfuse concepts: `trace_id` → Trace ID, `trace_name` → Trace Name, `span_name` → Span Name, `generation_name` → Generation Name, `parent_span_id` → Parent Observation ID ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Maps `user` request field to Langfuse User ID and `session_id` to Langfuse Session ID ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]
- Additional `trace` keys beyond the five standard ones are passed as trace metadata for filtering and analysis ^[001a-raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/data-privacy]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/summaries/openrouter-guides-features-broadcast-langfuse]]