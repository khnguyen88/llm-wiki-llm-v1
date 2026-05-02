---
title: "Claude Code Agent Sdk Streaming Vs Single Mode"
summary: "The Agent SDK supports two input modes: streaming input (default, recommended) for persistent interactive sessions, and single message input for simpler one-shot queries with limited capabilities"
type: summary
sources:
  - raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md
tags:
  - agent-sdk
  - streaming
  - input-modes
  - sessions
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Streaming Vs Single Mode

## Key Points

- The Agent SDK provides two input modes: streaming input mode (default and recommended) and single message input mode ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Streaming input mode operates as a long-lived process that accepts user input, handles interruptions, surfaces permission requests, and manages sessions ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Streaming input supports image attachments, queued messages, full tool integration, hooks, real-time feedback, and context persistence across multiple turns ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Single message input is designed for one-shot queries in stateless environments such as lambda functions ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Single message input does not support image attachments, dynamic message queueing, real-time interruption, hook integration, or natural multi-turn conversations ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Streaming input uses an async generator (`generateMessages()`) that yields user messages with `type: "user"` containing `role: "user"` and `content` ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Single message input uses a plain string `prompt` and supports `continue: true` to resume a previous session's context ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]

## Notes

- The streaming input example demonstrates yielding multiple messages from an async generator, including a follow-up message with an image attachment after a delay ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Single message continuation uses `options: { continue: true }` to maintain conversation state without manually passing session IDs ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/streaming_input]]
- [[concepts/streaming_output]]
- [[concepts/sessions]]
- [[concepts/hooks]]