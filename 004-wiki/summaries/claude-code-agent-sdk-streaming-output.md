---
title: "Claude Code Agent Sdk Streaming Output"
summary: "Enabling real-time incremental responses from the Agent SDK via StreamEvent messages for text and tool call streaming"
type: summary
sources:
  - raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md
tags:
  - agent-sdk
  - streaming
  - real-time
  - output
  - api
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Streaming Output

## Key Points

- Setting `include_partial_messages` (Python) or `includePartialMessages` (TypeScript) to `true` enables streaming, causing the SDK to yield `StreamEvent` messages containing raw API events alongside the usual `AssistantMessage` and `ResultMessage` ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- StreamEvent messages contain raw Claude API streaming events in an `event` field; consumers must check `event.type` to distinguish event kinds and extract data from nested `delta` fields ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- Text streaming uses `content_block_delta` events where `delta.type` is `text_delta`; tool call streaming tracks `content_block_start` (tool begins), `content_block_delta` with `input_json_delta` (input chunks), and `content_block_stop` (tool call complete) ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- When extended thinking is enabled (`max_thinking_tokens` / `maxThinkingTokens`), StreamEvent messages are not emitted; only complete messages after each turn are received ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- Structured output JSON appears only in the final `ResultMessage.structured_output`, not as streaming deltas ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- A typical streaming UI pattern uses an `in_tool` flag to suppress text output while a tool is executing and show a status indicator like `[Using Read...]` instead ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- Without partial messages enabled, only `SystemMessage`, `AssistantMessage`, `ResultMessage`, and `SDKCompactBoundaryMessage` / `SystemMessage` with `compact_boundary` subtype are received ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]

## Notes

- The streaming output feature covers receiving tokens in real-time; for input modes (how messages are sent to agents), see the streaming vs single-mode documentation ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]
- StreamEvent is named `StreamEvent` in Python (imported from `claude_agent_sdk.types`) and `SDKPartialAssistantMessage` with `type: 'stream_event'` in TypeScript ^[raw/document/claude code/claude-code-022-agent-sdk-streaming-output-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/streaming_output]]
- [[concepts/agent_loop]]
- [[concepts/sessions]]