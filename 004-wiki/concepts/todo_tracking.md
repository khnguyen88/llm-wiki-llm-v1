---
title: "Todo Tracking"
summary: "Built-in task management in the Agent SDK using the TodoWrite tool to track progress through pending, in_progress, and completed states"
type: concept
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

# Todo Tracking

Built-in task management in the Agent SDK that uses the TodoWrite tool to track and display progress for complex workflows. ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]

## Key Points

- Todos follow a three-state lifecycle: `pending` (identified), `in_progress` (actively being worked on), and `completed` (finished successfully); groups of completed todos are removed ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]
- The SDK automatically creates todos for complex multi-step tasks requiring 3+ actions, user-provided task lists, non-trivial operations benefiting from progress tracking, and explicit requests for todo organization ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]
- Todo updates surface in the message stream as `tool_use` blocks where `block.name === "TodoWrite"`; the `block.input.todos` array contains each todo's `status`, `content`, and `activeForm` ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]
- The `activeForm` field on each todo provides a present-continuous description (e.g., "Running tests") displayed when the todo is `in_progress`, while `content` is the imperative description (e.g., "Run tests") shown for other states ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]

## Details

Todo tracking in the Agent SDK operates through the built-in `TodoWrite` tool. When the agent identifies a multi-step task, it invokes `TodoWrite` to create a structured task list. As work progresses, subsequent `TodoWrite` calls update individual todo statuses. Applications consuming the message stream can detect these updates by filtering for `tool_use` blocks with `name === "TodoWrite"` and reading the `input.todos` array.

The source document demonstrates a `TodoTracker` class pattern: iterate over the `query()` message stream, extract `TodoWrite` tool calls from assistant messages, and render a progress display showing completed/total count and current tasks. This pattern enables real-time progress UI in applications built on the Agent SDK. ^[raw/document/claude code/claude-code-026-agent-sdk-todo-tracking-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/streaming_output]]
- [[concepts/custom_tools]]