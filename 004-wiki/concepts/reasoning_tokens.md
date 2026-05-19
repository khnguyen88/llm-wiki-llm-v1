---
title: "Reasoning Tokens"
summary: "Output tokens that expose a model's internal reasoning steps, controllable through OpenRouter's unified reasoning parameter with effort levels, max_tokens allocation, and exclusion options"
type: concept
sources:
  - raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md
tags:
  - reasoning-tokens
  - openrouter
  - effort-levels
  - api
  - llm
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Reasoning Tokens

Reasoning tokens (also called thinking tokens) are output tokens that provide a transparent look into the reasoning steps taken by a model. They are included in responses by default if the model decides to output them, appear in the `reasoning` field of each message, and are charged as output tokens. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

## Key Points

- Reasoning tokens are output tokens that expose model reasoning steps; they appear in the `reasoning` field of each message and are charged as output tokens ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- Some reasoning models (e.g., OpenAI o-series) do not return their reasoning tokens in the response ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- OpenRouter normalizes different provider-specific reasoning APIs into a unified `reasoning` parameter with `effort`, `max_tokens`, `exclude`, and `enabled` fields ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- Five effort levels control the proportion of tokens allocated to reasoning: `xhigh` (~95%), `high` (~80%), `medium` (~50%), `low` (~20%), `minimal` (~10%), and `none` (disables reasoning) ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- `max_tokens` directly specifies a token budget for reasoning; for models supporting only effort levels, the value is converted to an effort level using the allocation percentages ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]
- The `exclude` flag (`true`/`false`) lets models reason internally without including reasoning tokens in the response ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

## Details

### Controlling Reasoning Tokens

The `reasoning` config object consolidates settings for controlling reasoning strength across different models. It supports four fields:

- **`effort`**: OpenAI-style qualitative level (`xhigh`, `high`, `medium`, `low`, `minimal`, `none`). Supported by OpenAI reasoning models (o1, o3, GPT-5 series) and Grok models.
- **`max_tokens`**: Anthropic-style direct token budget. Supported by Gemini thinking models, Anthropic reasoning models (via `reasoning.max_tokens`), and some Alibaba Qwen thinking models (mapped to `thinking_budget`).
- **`exclude`**: Boolean (default `false`). When `true`, the model reasons internally but does not return reasoning tokens in the response.
- **`enabled`**: Boolean. Enables reasoning at medium effort with no exclusions. Inferred from `effort` or `max_tokens` if those are set.

When `effort` is specified on a model that only supports `max_tokens`, the budget is calculated using the effort allocation percentages. Conversely, when `max_tokens` is specified on an effort-only model, the appropriate effort level is determined from the same percentages. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

### Provider-Specific Implementations

**Anthropic**: Supports `reasoning.max_tokens` with a minimum of 1,024 and maximum of 128,000 tokens. The `budget_tokens` formula is: `budget_tokens = max(min(max_tokens * effort_ratio, 128000), 1024)`. The effort ratios are: xhigh=0.95, high=0.8, medium=0.5, low=0.2, minimal=0.1. `max_tokens` must be strictly higher than the reasoning budget to leave tokens for the final response. The `:thinking` variant is no longer supported; use the `reasoning` parameter instead. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

**Google Gemini 3**: Uses `thinkingLevel` (not `thinkingBudget`). OpenRouter maps `reasoning.effort` directly to Google's `thinkingLevel` values, with `xhigh` mapped down to `high`. When `reasoning.max_tokens` is specified, OpenRouter passes it as `thinkingBudget`, but Gemini 3 internally maps the budget to a `thinkingLevel`, so precise token control is not available. Actual token consumption is determined by Google's internal implementation. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

**OpenAI / Grok**: Use `reasoning.effort` directly. If a model does not support a specific effort level, OpenRouter maps the requested effort to the nearest supported level. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

**Alibaba Qwen**: Some Qwen thinking models map `reasoning.max_tokens` to `thinking_budget`; support varies by model. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

### Preserving Reasoning Across Turns

Reasoning context can be preserved across multi-turn conversations by passing it back in assistant messages via:

1. **`message.reasoning`** (string): Plaintext reasoning passed as a string field.
2. **`message.reasoning_details`** (array): Full structured reasoning details block, needed for models that return special reasoning types (encrypted, summarized).

`reasoning_content` is an alias for `reasoning` and functions identically. Preserving reasoning is especially important for tool calling: when a model invokes a tool, it pauses its response to await external information. Returning the original reasoning blocks with tool results ensures reasoning continuity and context maintenance. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

Preserving reasoning is supported by: OpenAI reasoning models (o1, o3, GPT-5+), Anthropic reasoning models (Claude 3.7+), Gemini Reasoning models, xAI reasoning models, and open source models including Qwen 3.5+, MiniMax M2+, MoonShot Kimi K2+, NVIDIA Nemotron 3 Nano+, Prime Intellect INTELLECT-3, Xiaomi MiMo-V2-Flash+, and Z.ai GLM 4.5+. Standard interleaved thinking only; Z.ai preserved thinking is not supported. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

### Legacy Parameters

`include_reasoning: true` is equivalent to `reasoning: {}`, and `include_reasoning: false` is equivalent to `reasoning: { exclude: true }`. The `reasoning` parameter is recommended for future compatibility. ^[raw/document/openrouter/openrouter-072-guides-best-practices-reasoning-tokens-2026-04-29.md]

## Related

- [[concepts/reasoning_details]]
- [[concepts/extended_thinking]]
- [[concepts/tool_calling]]
- [[entities/openrouter]]
- [[entities/openai]]
- [[entities/google_gemini]]
- [[entities/deepseek]]
- [[entities/grok]]
- [[entities/qwen]]
- [[summaries/openrouter-guides-best-practices-reasoning-tokens]]