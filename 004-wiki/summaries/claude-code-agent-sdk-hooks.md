---
title: "Claude Code Agent Sdk Hooks"
summary: "Detailed reference for Agent SDK hooks: callback functions that intercept agent events at key execution points to block, modify, log, or redirect tool calls and other agent actions"
type: summary
sources:
  - raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md
tags:
  - hooks
  - agent-sdk
  - claude-code
  - callbacks
  - permissions
  - lifecycle
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Hooks

## Key Points

- Hooks are callback functions registered to agent events (PreToolUse, PostToolUse, Stop, etc.) that can block dangerous operations, log tool calls, transform inputs/outputs, require human approval, or track session lifecycle ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- 18 hook events are available: PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch, UserPromptSubmit, Stop, SubagentStart, SubagentStop, PreCompact, PermissionRequest, Notification, SessionStart, SessionEnd, Setup, TeammateIdle, TaskCompleted, ConfigChange, WorktreeCreate, WorktreeRemove — Python supports 11, TypeScript supports all 18 ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Hooks are configured via the `hooks` field in `ClaudeAgentOptions` (Python) or `options` (TypeScript), organized as a dictionary keyed by event name with arrays of `HookMatcher` objects containing an optional regex `matcher`, a required `hooks` array of callbacks, and an optional `timeout` (default 60s) ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Every hook callback receives three arguments: typed input data (with `session_id`, `cwd`, `hook_event_name`, plus event-specific fields), a tool use ID for correlating PreToolUse/PostToolUse events, and a context object (TypeScript: `AbortSignal` for cancellation; Python: reserved for future use) ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Callbacks return output objects with top-level fields (`systemMessage` to inject context, `continue`/`continue_` to control agent continuation) and a `hookSpecificOutput` object with event-type-specific fields like `permissionDecision` (`"allow"`, `"deny"`, `"ask"`, or `"defer"` in TypeScript only), `permissionDecisionReason`, and `updatedInput` ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Permission decision priority: deny > defer > ask > allow — if any hook returns deny, the operation is blocked regardless of other hooks ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Async output (`{"async": true}` / `{"async_": True}` in Python) tells the agent to proceed immediately without waiting for the hook to finish; used only for side effects like logging or webhooks ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]

## Quotes

- "Hooks run your code in response to agent events, like a tool being called, a session starting, or execution stopping." ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- "When multiple hooks or permission rules apply, deny takes priority over defer, which takes priority over ask, which takes priority over allow." ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- "Keep each hook focused on a single responsibility and chain multiple hooks for complex logic." ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- "Async outputs cannot block, modify, or inject context into the operation since the agent has already moved on. Use them only for side effects like logging, metrics, or notifications." ^[001a-raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]

## Notes

- Matchers filter by tool name only, not by file paths or other arguments — to filter by file path, check `tool_input.file_path` inside the callback
- MCP tools use the naming pattern `mcp__<server>__<action>`; match with regex `^mcp__` to target all MCP tools
- `SessionStart` and `SessionEnd` are TypeScript-only as SDK callbacks; in Python, they are only available as shell command hooks loaded via `setting_sources`
- The `updatedInput` field in `hookSpecificOutput` requires `permissionDecision: 'allow'` to take effect; always return a new object rather than mutating the original `tool_input`
- A `UserPromptSubmit` hook that spawns subagents can create infinite loops; guard against this by checking for subagent indicators in the hook input

## Related

- [[004-wiki/concepts/hooks]]
- [[004-wiki/concepts/agent_loop]]
- [[004-wiki/concepts/custom_tools]]
- [[004-wiki/concepts/setting_sources]]
- [[004-wiki/concepts/file_checkpointing]]
- [[004-wiki/entities/agent_sdk]]
- [[004-wiki/entities/claude_code]]