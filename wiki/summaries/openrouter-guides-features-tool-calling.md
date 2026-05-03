---
title: "OpenRouter Tool & Function Calling"
summary: "OpenRouter standardizes the tool calling interface across models and providers, supporting a three-step request pattern, interleaved thinking between calls, and agentic loops for multi-step tool use"
type: summary
sources:
  - raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md
tags:
  - openrouter
  - tool-calling
  - function-calling
  - agentic-loop
  - interleaved-thinking
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Tool & Function Calling

## Key Points

- Tool calls (function calls) let an LLM suggest external tool invocations; the client executes the tool locally and returns results to the LLM, which then formats a final answer ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- OpenRouter standardizes the tool calling interface across models and providers, enabling the same tool definitions to work with any supported model ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- Models supporting tool calling can be filtered at `openrouter.ai/models?supported_parameters=tools` ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- The tool calling flow has three steps: (1) send inference request with tool definitions, (2) execute requested tool locally, (3) send follow-up request with tool results appended to the message history ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- The `tools` parameter must be included in every request (both initial and follow-up) so the router can validate the tool schema on each call ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- Interleaved thinking allows models to reason between tool calls, enabling multi-step decision-making with reasoning steps in between ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- The `tool_choice` parameter controls tool usage: `"auto"` (model decides), `"none"` (disabled), or a specific function object to force a particular tool ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- `parallel_tool_calls` (default `true`) controls whether multiple tools can be called simultaneously; set to `false` for sequential-only invocation ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Quotes

> "Tool calls (also known as function calls) give an LLM access to external tools. The LLM does not call the tools directly. Instead, it suggests the tool to call. The user then calls the tool separately and provides the results back to the LLM." ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

> "The tools parameter must be included in every request (Steps 1 and 3) so the router can validate the tool schema on each call." ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Notes

- The source provides complete code examples in TypeScript SDK, Python (OpenAI SDK), and TypeScript (fetch) for tool calling workflows
- Agentic loop pattern shown with a `maxIterations` cap (default 10) to prevent infinite tool-calling cycles

## Related

- [[entities/openrouter]]
- [[concepts/tool_calling]]
- [[concepts/interleaved_thinking]]
- [[concepts/agent_loop]]
- [[concepts/streaming_output]]