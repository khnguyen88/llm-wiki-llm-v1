---
title: "OpenRouter Body Builder Router"
summary: "OpenRouter's Body Builder router transforms natural language prompts into structured API request bodies for running the same task across multiple models in parallel"
type: summary
sources:
  - raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md
tags:
  - openrouter
  - body-builder
  - routing
  - parallel-execution
  - model-benchmarking
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Body Builder Router

## Key Points

- Body Builder (`openrouter/bodybuilder`) uses AI to transform natural language prompts into valid OpenRouter API request bodies, enabling the same task to be run across multiple models in parallel ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Free to use — no charge for generating request bodies; standard model pricing applies only when executing the generated requests ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Returns a JSON object containing an array of OpenRouter-compatible request bodies, one per model, each with its own `model` and `messages` fields ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Understands model aliases and common names (e.g., "Claude Sonnet" maps to `anthropic/claude-sonnet-4.5`, "GPT-5" maps to `openai/gpt-5.1`) and selects latest model versions by default ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Requires `messages` format input; generated requests use minimal required fields by default; system messages in input are preserved and forwarded ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Primary use cases include model benchmarking, redundancy and reliability (multi-provider verification), A/B testing across models, and exploration of model capabilities ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]

## Quotes

- "Body Builder uses AI to understand your intent and generate valid OpenRouter API request bodies." ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md:8]

## Notes

- Model slugs in the source examples are current as of December 4, 2025 and may change as new versions are released; check the OpenRouter models page for the latest available slugs.

## Related

- [[entities/openrouter]]
- [[concepts/body_builder]]
- [[concepts/auto_router]]
- [[concepts/model_fallback]]
- [[concepts/structured_output]]