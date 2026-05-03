---
title: "Presets"
summary: "Named LLM configurations that separate model settings from application code, allowing provider routing, model selection, and parameters to be updated without deployment"
type: concept
sources:
  - raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md
  - raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md
tags:
  - openrouter
  - configuration
  - provider-routing
  - api-design
  - response-caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Presets

Presets are named configurations that encapsulate all LLM settings needed for a specific use case, decoupling configuration from application code. ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]

## Key Points

- Each preset can manage provider routing preferences, model selection (including fallback arrays), system prompts, generation parameters (temperature, top_p, etc.), and provider inclusion/exclusion rules ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Three API reference patterns: `@preset/slug` as the model value, `"preset": "slug"` as a separate field, or `provider/model@preset/slug` combining model and preset in one string ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Enables configuration changes (model switching, prompt tuning, parameter adjustment, provider preference updates) without redeploying code ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Organization presets are accessible to all org members; version history is kept for rollback but API always uses the latest version ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]
- Request-level parameters shallow-merge over preset defaults, allowing per-request overrides ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]

## Details

Presets solve the separation-of-concerns problem in LLM-integrated applications. Instead of hardcoding model IDs, system prompts, and routing preferences in application code, developers define a named preset via the OpenRouter web interface and reference it by slug. This makes code more semantic (e.g., `"@preset/email-copywriter"` instead of `"openai/gpt-4"`) and allows non-code configuration changes. ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]

The three reference patterns serve different use cases. The direct model reference (`@preset/slug`) replaces the model field entirely and is the simplest form. The preset field pattern keeps an explicit model while layering preset settings on top. The combined syntax (`model@preset/slug`) specifies both in a single string. ^[raw/document/openrouter/openrouter-030-guides-features-presets-2026-04-29.md]

### Response caching configuration

Presets can enable response caching for all requests that reference them. Two fields control this: `cache_enabled` (boolean) enables caching, and `cache_ttl_seconds` (1–86400, default 300) sets the default TTL. When `cache_enabled` is set on a preset, caching is automatically applied to every request referencing that preset, with no `X-OpenRouter-Cache` header required. A preset with `cache_enabled: false` disables caching regardless of request headers. The `X-OpenRouter-Cache-TTL` header overrides the preset `cache_ttl_seconds`. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/provider_routing]]
- [[concepts/system_prompt]]
- [[concepts/workspaces]]
- [[concepts/response_caching]]