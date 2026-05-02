---
title: "Streaming Input"
summary: "The Agent SDK's default input mode using async generators to feed messages into a persistent agent session, supporting images, queued messages, hooks, and multi-turn context"
type: concept
sources:
  - raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md
tags:
  - agent-sdk
  - streaming
  - input
  - sessions
  - api
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Streaming Input

The Agent SDK's default and recommended input mode, where an async generator function yields user messages into a persistent agent session. Unlike single message input, streaming input enables full agent capabilities including image attachments, message queueing, real-time interruption, hook integration, and natural multi-turn conversations. ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]

## Key Points

- Streaming input is the default and recommended mode; the agent operates as a long-lived process handling user input, interruptions, permission requests, and session management ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Messages are yielded from an async generator function with `type: "user"` and a `message` object containing `role: "user"` and `content` (which can be a string or a content array with text and image blocks) ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Supports image attachments via content blocks with `type: "image"` and base64-encoded source data ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Supports queued messages that process sequentially, with the ability to interrupt the agent between messages ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]
- Provides full access to all tools, custom MCP servers, hooks, and real-time feedback as responses are generated ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]

## Details

In streaming input mode, the `prompt` parameter of `query()` accepts an async generator rather than a plain string. The generator yields message objects as they become available — for example, a user's first question followed by a follow-up with an image after a delay. Each yielded message has `type: "user"` with a nested `message` object containing the `role` and `content`. Content can be a simple text string or a structured array with text and image blocks, where image blocks include base64-encoded source data. ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]

This mode contrasts with single message input, which passes a plain string as the `prompt` and is suited for one-shot queries in stateless environments. Single message mode lacks support for image attachments, dynamic message queueing, real-time interruption, hook integration, and natural multi-turn conversations. ^[raw/document/claude code/claude-code-023-agent-sdk-streaming-vs-single-mode-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/streaming_output]]
- [[concepts/sessions]]
- [[concepts/hooks]]
- [[concepts/agent_loop]]