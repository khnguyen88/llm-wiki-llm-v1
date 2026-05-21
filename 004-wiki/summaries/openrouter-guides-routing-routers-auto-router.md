---
title: "Openrouter Guides Routing Routers Auto Router"
summary: "OpenRouter's Auto Router (openrouter/auto) uses NotDiamond to analyze prompts and automatically select the optimal model, with configurable allowed-model filters via the plugins parameter"
type: summary
sources:
  - raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md
tags:
  - openrouter
  - auto-router
  - model-selection
  - notdiamond
  - routing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Routing Routers Auto Router

## Key Points

- The Auto Router (`openrouter/auto`) automatically selects the best model for a prompt by analyzing prompt complexity, task type, and model capabilities, powered by NotDiamond ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Usage requires setting `model` to `openrouter/auto` in the chat completions request; the response includes a `model` field showing which model was selected ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Routing process: prompt analysis by NotDiamond, optimal model selection, request forwarding, and response tracking with model metadata ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Allowed models can be restricted via the `plugins` parameter with wildcard patterns (e.g., `anthropic/*`, `openai/gpt-5*`, `*/claude-*`); configurable per-request or as defaults in Plugin Settings ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- No additional fee for using the Auto Router; users pay the standard rate for whichever model is selected ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Requires `messages` format (not `prompt`); streaming is supported; all standard OpenRouter features work with the selected model ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Supported model pool includes Claude Sonnet 4.5, Claude Opus 4.5, GPT-5.1, Gemini 3.1 Pro, DeepSeek 3.2, and other top-performing models; model slugs change as new versions are released ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]

## Quotes

- "Instead of manually choosing a model, let the Auto Router analyze your prompt and select the optimal model from a curated set of high-quality options." ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- "You pay the standard rate for whichever model is selected. There is no additional fee for using the Auto Router." ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- "When no patterns are configured, the Auto Router uses all supported models." ^[001a-raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]

## Notes

- The Auto Router complements [[004-wiki/concepts/model-fallback]] (which handles failures) and [[004-wiki/concepts/provider-routing]] (which selects providers for a given model) by addressing a different problem: choosing *which model* to use in the first place.
- Use cases include general-purpose applications with unpredictable prompt types, cost optimization for simpler tasks, quality optimization for complex prompts, and experimentation to discover best-performing models.

## Related

- [[004-wiki/concepts/auto-router]]
- [[004-wiki/entities/openrouter]]
- [[004-wiki/entities/notdiamond]]
- [[004-wiki/concepts/model-fallback]]
- [[004-wiki/concepts/provider-routing]]
- [[004-wiki/concepts/auto-exacto]]