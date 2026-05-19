---
title: "Agent Loop"
summary: "The iterative execution cycle in which an LLM agent receives a prompt, decides on actions, calls tools, processes results, and repeats until the task is complete"
type: concept
sources:
  - raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md
  - raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md
  - raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md
  - raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md
  - raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md
tags:
  - agent-loop
  - claude-code
  - agent-sdk
  - architecture
  - openrouter
  - tool-calling
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Agent Loop

The iterative execution cycle that powers autonomous LLM agents: the model receives a prompt, evaluates the current state, calls tools to take action, receives the results, and repeats until it produces a response with no tool calls. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

## Key Points

- Every agent session follows five steps: (1) receive prompt, (2) evaluate and respond with text or tool calls, (3) execute requested tools and collect results, (4) repeat steps 2-3, (5) return the final text result ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- A turn is one round trip: Claude produces output with tool calls, the SDK executes those tools, and results feed back automatically without yielding control to the caller's code ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- The loop ends when Claude produces a response with no tool calls; the SDK then yields a ResultMessage with final text, token usage, cost, and session ID ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Five message types cover the full lifecycle: SystemMessage (session events), AssistantMessage (Claude's responses), UserMessage (tool results and user inputs), StreamEvent (partial streaming), and ResultMessage (final outcome) ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- The loop can be capped with `max_turns`/`maxTurns` (tool-use round trips) and `max_budget_usd`/`maxBudgetUsd` (spend threshold); hitting either limit returns a ResultMessage with an error subtype ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- The effort parameter (low, medium, high, xhigh, max) controls reasoning depth per turn, trading latency and token cost for thoroughness ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- The SDK handles the orchestration (tool execution, context management, retries) automatically; consumers iterate over the async stream and filter for human-readable output ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]

## Details

The agent loop is the core architectural pattern behind Claude Code's autonomous behavior. Rather than a single request-response cycle, the loop allows the model to iteratively call tools, observe their outputs, and adjust its approach. A simple query ("what files are here?") might take one or two turns, while a complex task ("refactor the auth module and update the tests") can chain dozens of tool calls across many turns. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

Tool execution follows specific concurrency rules. Read-only tools (Read, Glob, Grep, and MCP tools marked read-only) can execute in parallel within a single turn. Tools that modify state (Edit, Write, Bash) run sequentially to avoid conflicts. Custom tools default to sequential execution but can be marked as read-only via `readOnly` (TypeScript) or `readOnlyHint` (Python) annotations to enable parallel execution. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

The ResultMessage `subtype` field distinguishes termination states: `success` (task completed), `error_max_turns` (hit turn limit), `error_max_budget_usd` (hit budget limit), `error_during_execution` (API failure or cancellation), and `error_max_structured_output_retries` (validation failures). The `result` field containing the final text output is only present on the `success` subtype. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

OpenRouter implements an agentic loop pattern for tool calling: the loop repeatedly calls the LLM, checks if the response contains `tool_calls`, executes the requested tools locally, appends `tool` role messages with results, and continues until the model responds without tool calls or a maximum iteration count is reached. A `maxIterations` cap (commonly 10) prevents infinite loops. The `tools` parameter must be included in every request so the router can validate the tool schema on each call. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/context_window]]
- [[concepts/hooks]]
- [[concepts/cost_tracking]]
- [[concepts/file_checkpointing]]
- [[concepts/streaming_output]]
- [[entities/openrouter]]
- [[concepts/tool_calling]]