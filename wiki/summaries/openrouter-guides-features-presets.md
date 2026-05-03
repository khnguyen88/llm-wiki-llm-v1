---
title: "Openrouter Guides Features Presets"
summary: "OpenRouter presets are named configurations that separate LLM settings from application code, managing provider routing, model selection, system prompts, and generation parameters via a slug-based API reference"
type: summary
sources:
  - raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md
tags:
  - openrouter
  - presets
  - configuration
  - provider-routing
  - llm-gateway
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Presets

## Key Points

- Presets are named configurations that encapsulate LLM settings (provider routing, model selection, system prompts, generation parameters, provider inclusion/exclusion rules) separate from application code ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Three API reference methods: direct model reference (`@preset/slug`), preset field (`"preset": "slug"`), and combined model-and-preset (`"model": "provider/model@preset/slug"`) ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Presets enable rapid iteration by allowing LLM configuration changes (model versions, prompts, parameters, provider preferences) without code deployment ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Organization account members can access all organization presets, enabling team-wide sharing of best practices ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Presets maintain version history for rollback, but API requests always use the latest version ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Request-level parameters are shallow-merged with preset-configured options, allowing per-request overrides ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]

## Quotes

- "Presets allow you to separate your LLM configuration from your code." ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md:9]
- "If you provide parameters in the request, they will be shallow-merged with the options configured in the preset." ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md:63]

## Notes

- Presets are created and managed through the OpenRouter web application at `/settings/presets` ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/presets]]
- [[concepts/provider_routing]]
- [[concepts/system_prompt]]
- [[concepts/workspaces]]