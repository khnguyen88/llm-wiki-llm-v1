---
title: "Claude Code Agent Sdk Typescript V2 Preview"
summary: "Preview of the simplified V2 TypeScript Agent SDK that replaces async generators with a session-based send/stream pattern for multi-turn conversations"
type: summary
sources:
  - raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md
tags:
  - agent-sdk
  - typescript
  - v2-preview
  - sessions
  - streaming
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Typescript V2 Preview

The V2 TypeScript Agent SDK is an unstable preview that simplifies multi-turn conversations by replacing async generators and yield coordination with a session-based `send()`/`stream()` pattern. ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]

## Key Points

- The V2 API surface reduces to three concepts: `createSession()`/`resumeSession()` to start or continue a conversation, `session.send()` to dispatch a message, and `session.stream()` to receive the response ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]
- `unstable_v2_prompt()` provides one-shot convenience for single-turn queries without maintaining a session; the result includes a `subtype` field where `"success"` indicates a valid response ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]
- The V2 interface is unstable; APIs may change before becoming stable, and some V1 features are not yet available including session forking (`forkSession` option) and some advanced streaming input patterns ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]
- Sessions support multi-turn conversations where `send()` can be called multiple times on the same session, and Claude retains context from previous turns ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]
- Session IDs for resumption are obtained from `msg.session_id` on streamed messages rather than from the result message alone ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]
- Resource cleanup uses TypeScript 5.2+ `await using` for automatic session disposal, or manual `session.close()` for older TypeScript versions ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]
- The V2 SDK is included in the existing `@anthropic-ai/claude-agent-sdk` npm package alongside V1 ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]

## Quotes

- "The V2 Claude Agent TypeScript SDK removes the need for async generators and yield coordination. This makes multi-turn conversations simpler, instead of managing generator state across turns, each turn is a separate send()/stream() cycle." ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md:6]

## Notes

- The `SDKSession` interface exposes `sessionId` (readonly), `send(message)`, `stream()` (returns AsyncGenerator), and `close()` ^[raw/document/claude code/claude-code-029-agent-sdk-typescript-v2-preview-2026-04-29.md]
- V2 function names are prefixed with `unstable_v2_` to signal their preview status
- All V2 examples use `claude-opus-4-7` as the model parameter

## Related

- [[entities/agent_sdk]]
- [[entities/client_sdk]]
- [[concepts/sessions]]
- [[concepts/streaming_output]]
- [[concepts/agent_loop]]
- [[concepts/subagents]]