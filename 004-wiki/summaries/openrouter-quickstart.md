---
title: "Openrouter Quickstart"
summary: "OpenRouter provides a unified API for hundreds of AI models through a single endpoint, with three integration methods: direct API, Client SDKs, and Agent SDK"
type: summary
sources:
  - raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md
tags:
  - openrouter
  - api
  - sdk
  - agent-sdk
  - quickstart
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Quickstart

## Key Points

- OpenRouter provides a unified API that gives access to hundreds of AI models through a single endpoint (`/api/v1/chat/completions`), automatically handling fallbacks and selecting cost-effective options ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]
- Three integration approaches: direct API (standard HTTP requests), Client SDKs (type-safe wrappers in TypeScript and Python), and Agent SDK (higher-level agent primitives with tool execution and state management) ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]
- The OpenRouter API is compatible with the OpenAI SDK as a drop-in replacement via `baseURL` configuration ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]
- Optional headers `HTTP-Referer` and `X-OpenRouter-Title` enable app attribution for rankings on OpenRouter's public leaderboards ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]
- Client SDK (`@openrouter/sdk` for TypeScript, `openrouter` for Python) provides full type safety with auto-generated types from the OpenAPI spec and zero boilerplate ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]
- Agent SDK (`@openrouter/agent`) provides the `callModel` function that handles multi-turn conversation loops, tool execution, and state management in a single invocation ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]
- An interactive Request Builder at `/request-builder` generates OpenRouter API requests in various languages ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]

## Quotes

- "OpenRouter provides a unified API that gives you access to hundreds of AI models through a single endpoint, while automatically handling fallbacks and selecting the most cost-effective options." ^[raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md]

## Notes

- The source recommends using OpenRouter SDKs (`@openrouter/sdk`, `openrouter`) by default; the OpenAI SDK integration should only be used when explicitly requested
- The Client SDK is described as intentionally lean — a thin layer over the REST API
- The Agent SDK's `callModel` sends the prompt, receives tool calls, executes tools, feeds results back, and returns the final response in one call

## Related

- [[entities/openrouter]]
- [[concepts/llm_gateway]]
- [[concepts/streaming_output]]
- [[entities/agent_sdk]]