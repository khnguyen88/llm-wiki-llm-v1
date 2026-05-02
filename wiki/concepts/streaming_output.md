---
title: "Streaming Output"
summary: "Real-time incremental delivery of text and tool-call responses from the Agent SDK via StreamEvent messages instead of waiting for complete responses"
type: concept
sources:
  - raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md
tags:
  - streaming
  - agent-sdk
  - real-time
  - api
  - output
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Streaming Output

Real-time incremental delivery of LLM responses through the Agent SDK, where tokens and tool-call data arrive as they are generated rather than waiting for the complete response. Streaming is opt-in via the `include_partial_messages` (Python) or `includePartialMessages` (TypeScript) option. ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]

## Key Points

- Streaming is disabled by default; enabling it adds `StreamEvent` messages to the async iterator alongside the standard `AssistantMessage` and `ResultMessage` types ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- Each `StreamEvent` contains a raw Claude API streaming event in its `event` field; consumers must check `event["type"]` to route events and extract data from nested `delta` dictionaries ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- Text deltas arrive as `content_block_delta` events with `delta.type == "text_delta"`; tool input deltas arrive as `content_block_delta` events with `delta.type == "input_json_delta"` and must be manually accumulated ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- The `StreamEvent` dataclass (Python) has fields: `uuid` (unique event ID), `session_id`, `event` (raw API event dict), and `parent_tool_use_id` (set when the event originates from a subagent) ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- Extended thinking (enabled by setting `max_thinking_tokens` / `maxThinkingTokens`) is incompatible with streaming — no `StreamEvent` messages are emitted when thinking is active ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- Structured output JSON is available only in the final `ResultMessage.structured_output` field, not as streaming deltas ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]

## Details

When partial messages are enabled, the message flow follows a predictable sequence: `message_start`, then alternating blocks of `content_block_start` / `content_block_delta` / `content_block_stop` for text and tool-use content, followed by `message_delta` and `message_stop`, then the complete `AssistantMessage`. This repeats for each turn until the final `ResultMessage`. ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]

A common UI pattern for streaming combines text and tool-call handling using an `in_tool` flag. When a `content_block_start` event arrives with `content_block.type == "tool_use"`, the flag is set and a status indicator like `[Using Read...]` is displayed. Text deltas are suppressed while the flag is true. When `content_block_stop` fires, the flag clears and a "done" message appears. This prevents interleaved text and tool-status output from creating a confusing display. ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]

Without partial messages enabled, the async iterator yields only `SystemMessage`, `AssistantMessage`, `ResultMessage`, and a compact boundary message (`SDKCompactBoundaryMessage` in TypeScript, `SystemMessage` with `subtype "compact_boundary"` in Python). All incremental data is absent — the consumer receives only completed messages after each turn. ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/sessions]]
- [[concepts/subagents]]
- [[concepts/structured_output]]