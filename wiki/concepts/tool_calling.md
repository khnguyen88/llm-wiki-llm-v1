---
title: "Tool Calling"
summary: "A pattern where an LLM suggests external tool invocations with arguments, the client executes the tool locally, and results are fed back to the LLM for a final response"
type: concept
sources:
  - raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md
  - raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md
tags:
  - tool-calling
  - function-calling
  - llm
  - api
  - agentic
  - server-tools
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Tool Calling

Tool calling (also known as function calling) is a pattern where an LLM is given descriptions of external tools and suggests which tool to invoke along with arguments, but does not execute the tool directly. The client executes the tool locally and returns the results to the LLM, which then formats a final response. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Key Points

- The LLM suggests tool invocations but never calls tools directly; the client is responsible for execution and returning results ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- The three-step flow: (1) send inference request with `tools` definitions, (2) execute requested tool(s) locally using `tool_calls` from the assistant response, (3) send follow-up request with `tool` role messages containing results appended to the message history ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- The `tools` array must be included in every request (both initial and follow-up) so the router can validate the tool schema on each call ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- Each tool definition includes a `name`, `description`, and `parameters` JSON Schema; the `type` field is always `"function"` ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- The assistant response includes `tool_calls` with a unique `id`, function `name`, and JSON-encoded `arguments`; the client must return results using a `tool` role message with the matching `tool_call_id` ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Details

Tool definitions follow the OpenAI function calling format. Each tool is described as an object with `type: "function"` and a `function` property containing `name`, `description`, and `parameters` (a JSON Schema object). The model uses these descriptions to decide whether and how to call each tool. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

The `tool_choice` parameter controls tool usage behavior: `"auto"` lets the model decide whether to use tools (default), `"none"` disables tool usage entirely, and specifying a function object forces the model to call that particular tool. When `parallel_tool_calls` is `true` (default), the model may request multiple tool invocations in a single response; setting it to `false` restricts the model to one tool call at a time. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

When streaming, tool call deltas arrive incrementally via `delta.tool_calls` in SSE chunks, with `finish_reason: "tool_calls"` signaling that all tool calls are complete. The client must accumulate partial tool call data across streaming chunks before executing the tools. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

Best practices for tool definitions include using clear, descriptive function names that indicate purpose, providing comprehensive descriptions explaining when and how to use each tool, and designing multi-tool workflows where tools naturally chain together (e.g., search → get details → check inventory). ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

On OpenRouter, user-defined tools (described above) are distinct from **server tools**, which use the `openrouter:*` type prefix and are executed by OpenRouter server-side rather than by the client. Server tools and user-defined tools can coexist in the same `tools` array — the model decides when to call either type, but only user-defined tools require client-side execution. ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/interleaved_thinking]]
- [[concepts/agent_loop]]
- [[concepts/streaming_output]]
- [[concepts/structured_output]]
- [[concepts/server_tools]]