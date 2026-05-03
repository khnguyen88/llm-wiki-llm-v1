---
title: "PostHog"
summary: "An open-source product analytics platform with LLM analytics capabilities, available as a Broadcast destination on OpenRouter"
type: entity
sources:
  - raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md
tags:
  - analytics
  - open-source
  - llm-analytics
  - broadcast-destination
  - posthog
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# PostHog

An open-source product analytics platform that helps understand user behavior, with LLM analytics capabilities for tracking and analyzing AI application usage. ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]

## Key Facts

- Available as a Broadcast destination on [[entities/openrouter|OpenRouter]] for sending LLM request/response trace data ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Configuration requires a project API key (prefix `phc_...`) obtained from PostHog Project Settings ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Default endpoint is `https://us.i.posthog.com`; EU region uses `https://eu.i.posthog.com` ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Three standard `trace` metadata keys map to PostHog event properties: `trace_id`, `trace_name`, `generation_name` ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- The `user` request field maps to PostHog's `$ai_user` property for user-level LLM analytics ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- The `session_id` request field maps to PostHog's `$ai_session_id` property for session grouping ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Custom metadata keys from the `trace` field are included as properties on the LLM analytics event ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- PostHog's LLM analytics dashboard automatically tracks token usage, costs, and model performance ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- When [[concepts/data_privacy|Privacy Mode]] is enabled, the `$ai_input` and `$ai_output_choices` properties are excluded from events; all other analytics data is still sent normally ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[concepts/analytics]]
- [[summaries/openrouter-guides-features-broadcast-posthog]]