---
title: "Free Models Router"
summary: "An OpenRouter router that automatically selects a free model at random from available free models, filtering by request capabilities like vision, tool calling, and structured outputs"
type: concept
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

# Free Models Router

An [[entities/openrouter|OpenRouter]] router (`openrouter/free`) that automatically selects a free model at random from the pool of currently available free models, filtering for models that support the capabilities required by the request (vision, tool calling, structured outputs). ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]

## Key Points

- Activated by setting `model` to `openrouter/free` in the chat completions request ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- Routing process: (1) request analysis for required capabilities, (2) filtering free models that support those capabilities, (3) random selection from the filtered pool, (4) forwarding the request, (5) returning the response with model metadata ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- Completely free — no charge for using the router itself or for requests routed to free models ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- Response includes the `model` field identifying which free model was actually used (e.g., `upstage/solar-pro-3:free`) ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]
- To use a specific free model instead of random selection, append the `:free` variant suffix to a model ID (e.g., `meta-llama/llama-3.2-3b-instruct:free`) ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]

## Details

The Free Models Router is intended for learning, experimentation, prototyping, and low-volume use cases where zero-cost inference is more important than choosing a specific model. It differs from the [[concepts/auto_router]] in that it selects randomly from free models rather than optimizing model choice based on prompt analysis. ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]

### Limitations

Free models may have lower rate limits, variable availability, and higher latency during peak usage compared to paid models. The router does not allow control over which specific model is selected; if a specific free model is needed, the [[concepts/model_variants|`:free` variant]] suffix should be used instead. ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]

### Available Free Models

Free model availability changes frequently. The current list is available on the [OpenRouter models page](https://openrouter.ai/models?pricing=free). Examples include DeepSeek R1, Meta Llama models, and Alibaba Qwen models. ^[raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/auto_router]]
- [[concepts/model_variants]]
- [[concepts/rate_limiting]]
- [[summaries/openrouter-guides-routing-routers-free-models-router]]