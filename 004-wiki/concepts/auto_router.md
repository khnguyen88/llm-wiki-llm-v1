---
title: "Auto Router"
summary: "OpenRouter's automatic model selection feature that analyzes prompts and routes them to the optimal model, powered by NotDiamond"
type: concept
sources:
  - raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md
  - raw/document/openrouter/openrouter-028-guides-routing-routers-free-models-router-2026-04-29.md
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

# Auto Router

An automatic model selection feature on [[entities/openrouter|OpenRouter]] that analyzes prompts and routes them to the optimal model from a curated pool, powered by [[entities/notdiamond|NotDiamond]]. Instead of manually specifying a model, developers set `model` to `openrouter/auto` and the router selects the best model based on prompt complexity, task type, and model capabilities. ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]

## Key Points

- Activated by setting `model` to `openrouter/auto` in the chat completions request; the response's `model` field identifies which model was selected ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Routing process: (1) prompt analysis by NotDiamond, (2) optimal model selection, (3) request forwarding, (4) response tracking with model metadata ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Allowed models can be restricted via the `plugins` parameter with an object containing `id: "auto-router"` and an `allowed_models` array of wildcard patterns ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- No additional fee; users pay the standard rate for whichever model is selected ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]
- Requires `messages` format (not `prompt`); streaming and all standard OpenRouter features (tool calling, etc.) work with the selected model ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]

## Details

### Allowed Models Configuration

The `plugins` parameter restricts which models the Auto Router can select from. Patterns support wildcards:

| Pattern | Matches |
|---|---|
| `anthropic/*` | All Anthropic models |
| `openai/gpt-5*` | All GPT-5 variants |
| `google/*` | All Google models |
| `openai/gpt-5.1` | Exact match only |
| `*/claude-*` | Any provider with claude in model name |

^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]

Configuration can be done per-request via the `plugins` parameter in the API call, or as defaults in the Plugin Settings UI at Settings > Plugins > Auto Router. Per-request settings override defaults. When no patterns are configured, the Auto Router uses all supported models. ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]

### Distinction from Other Routing Features

The Auto Router solves the model *selection* problem (which model to use), which is distinct from [[concepts/model_fallback]] (which handles model *failure*) and [[concepts/provider_routing]] (which selects the best *provider* for a given model). [[concepts/auto_exacto]] optimizes provider ordering for tool-calling quality, while the Auto Router chooses the model itself. ^[raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/notdiamond]]
- [[concepts/model_fallback]]
- [[concepts/provider_routing]]
- [[concepts/auto_exacto]]
- [[concepts/llm_gateway]]
- [[concepts/free_models_router]]
- [[summaries/openrouter-guides-routing-routers-auto-router]]
- [[summaries/openrouter-guides-routing-routers-free-models-router]]