---
title: Request Transformers
type: concept
date: 2026-04-22
sources:
  - raw/repos/claude-code-router/docs/docs/server/config/transformers.md
  - raw/repos/claude-code-router/README.md
tags:
  - llm
  - api
  - proxy
  - claude-code
---

# Request Transformers

Plugins that convert LLM requests and responses between the unified internal format (Anthropic API) and provider-specific formats. Central to [[claude-code-router]]'s ability to support multiple providers.

## Data Flow

Incoming Anthropic request -> `transformRequestOut` -> `UnifiedChatRequest` -> `transformRequestIn` (optional) -> Provider API -> `transformResponseIn` (optional) -> `transformResponseOut` (optional) -> outgoing Anthropic response.

## Transformer Interface

TypeScript `Transformer` interface with methods: `transformRequestIn`, `transformRequestOut`, `transformResponseIn`, `transformResponseOut`, `auth`, `endPoint`, `name`, `logger`. Key types: `UnifiedChatRequest` (includes reasoning with effort levels none/low/medium/high), `UnifiedMessage` (supports tool_calls, thinking content).

## Built-in Transformers

| Transformer | Purpose |
|-------------|---------|
| anthropic | Pass-through (preserves original request/response) |
| deepseek | Adapts for DeepSeek API |
| gemini | Adapts for Gemini API |
| openrouter | Adapts for OpenRouter (supports provider routing parameter) |
| groq | Adapts for Groq API |
| maxtoken | Sets specific `max_tokens` value |
| tooluse | Optimizes tool usage via `tool_choice` |
| reasoning | Processes `reasoning_content` field |
| sampling | Handles temperature, top_p, top_k, repetition_penalty |
| enhancetool | Error tolerance layer for tool call parameters |
| cleancache | Clears `cache_control` from requests |
| vertex-gemini | Gemini API via Vertex authentication |

## Application Levels

- **Provider-level**: Applied to all models under a provider
- **Model-specific**: Applied only to a named model
- **Global**: Via the `transformers` array in config.json for custom transformers

## Custom Transformers

JavaScript modules loaded via the `transformers` field. Can implement any combination of the Transformer interface methods. Supports options passing via nested arrays.

## Related

- [[claude-code-router]] — the tool using transformers
- [[model_routing]] — routing decisions that work with transformers