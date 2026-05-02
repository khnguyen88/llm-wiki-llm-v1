---
title: "Claude Code Agent Sdk Todo Tracking"
summary: "Built-in todo functionality in the Agent SDK for tracking task progress through pending, in_progress, and completed states via the TodoWrite tool"
type: summary
sources:
  - raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md
tags:
  - agent-sdk
  - todo-tracking
  - progress
  - task-management
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Todo Tracking

## Key Points

- The Agent SDK includes built-in todo functionality for managing tasks and displaying progress to users ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]
- Todos follow a lifecycle: created as `pending`, activated to `in_progress`, marked `completed` on success, and removed when all tasks in a group finish ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]
- The SDK automatically creates todos for complex multi-step tasks (3+ actions), user-provided task lists, non-trivial operations, and explicit user requests ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]
- Todo updates are reflected in the message stream as `tool_use` blocks with `name: "TodoWrite"`; each block contains an `input.todos` array with `status`, `content`, and `activeForm` fields ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]
- Each todo item has three fields: `status` (pending/in_progress/completed), `content` (task description), and `activeForm` (present-continuous description shown when in_progress) ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]

## Notes

- The source document provides TypeScript code examples for monitoring todo changes and building a real-time progress display. The Python SDK offers equivalent functionality.

## Related

- [[entities/agent_sdk]]
- [[concepts/todo_tracking]]
- [[concepts/agent_loop]]
- [[concepts/streaming_output]]