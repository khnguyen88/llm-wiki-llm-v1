---
title: "Openrouter Guides Features Broadcast Posthog"
summary: "OpenRouter Broadcast integration with PostHog for LLM analytics, covering setup, custom metadata mapping, and privacy mode"
type: summary
sources:
  - raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - posthog
  - llm-analytics
  - observability
  - privacy-mode
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Posthog

## Key Points

- PostHog is an open-source product analytics platform with LLM analytics capabilities, available as a Broadcast destination on OpenRouter ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Setup requires a PostHog project API key (prefix `phc_...`), enabling Broadcast in OpenRouter's Observability settings, and configuring the PostHog destination with optional endpoint override (default `https://us.i.posthog.com`, EU: `https://eu.i.posthog.com`) ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Three standard `trace` metadata keys map to PostHog event properties: `trace_id`, `trace_name`, and `generation_name` ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- The `user` field maps to PostHog's `$ai_user` property and `session_id` maps to `$ai_session_id` for user-level and session-level LLM analytics ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Custom metadata keys from the `trace` field are included as properties on the LLM analytics event ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- Privacy Mode excludes `$ai_input` and `$ai_output_choices` properties from events while preserving token usage, costs, model information, and custom metadata ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]

## Quotes

- "PostHog receives LLM analytics events with custom metadata included as event properties. Use the `trace` field to attach additional context to your analytics data." ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- "The configuration only saves if the test passes." ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]

## Notes

- PostHog's LLM analytics dashboard automatically tracks token usage, costs, and model performance ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]
- The PostHog integration uses a simpler metadata mapping than other Broadcast destinations (only 3 standard trace keys vs. the typical 5), with no `span_name` or `parent_span_id` mapping mentioned

## Related

- [[entities/posthog]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/observability]]
- [[concepts/analytics]]
- [[summaries/openrouter-guides-features-broadcast-overview]]