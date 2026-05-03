---
title: "Openrouter Guides Routing Routers Free Models Router"
summary: "OpenRouter's Free Models Router (openrouter/free) automatically selects a free model at random, filtering by request capabilities like vision and tool calling, for zero-cost inference"
type: summary
sources:
  - raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md
tags:
  - openrouter
  - free-models
  - model-routing
  - zero-cost
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Routing Routers Free Models Router

## Key Points

- The Free Models Router uses model ID `openrouter/free` and automatically selects a free model at random from available free models on [[entities/openrouter|OpenRouter]] ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- The router filters free models by required capabilities (vision, tool calling, structured outputs) before random selection ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- Completely free to use — no charge for the router or routed requests ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- Response includes a `model` field identifying which specific free model handled the request ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- For specific free model selection, append `:free` to a model ID (e.g., `meta-llama/llama-3.2-3b-instruct:free`) instead of using the router ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- Limitations include lower rate limits, variable availability, and higher latency compared to paid models ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- Intended for learning, experimentation, prototyping, and low-volume use cases ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]

## Quotes

> Instead of manually choosing a specific free model, let the Free Models Router handle model selection for you. This is ideal for experimentation, learning, and low-volume use cases where you want zero-cost inference without worrying about which specific model to use. ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md:12-14]

## Notes

- The source document includes code examples in TypeScript SDK, TypeScript fetch, Python, and cURL for using the Free Models Router
- A Chat Playground guide is referenced for trying the router without writing code

## Related

- [[entities/openrouter]]
- [[concepts/free_models_router]]
- [[concepts/auto_router]]
- [[concepts/model_variants]]
- [[concepts/rate_limiting]]