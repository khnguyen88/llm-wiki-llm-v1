---
title: "Claude Code Agent Sdk Subagents"
summary: "Subagents in the Agent SDK are separate agent instances spawned for focused subtasks, offering context isolation, parallelization, and specialized instructions via programmatic AgentDefinition or filesystem-based definitions"
type: summary
sources:
  - raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md
tags:
  - agent-sdk
  - subagents
  - delegation
  - context-isolation
  - parallelization
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Subagents

## Key Points

- Subagents are separate agent instances that run in isolated contexts, returning only their final message to the parent ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Three creation methods: programmatic `agents` parameter (recommended), filesystem-based `.claude/agents/` definitions, and built-in `general-purpose` subagent available when `Agent` is in `allowedTools` ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagents cannot spawn their own subagents — do not include `Agent` in a subagent's `tools` array ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Multiple subagents can run concurrently for parallelization, dramatically speeding up complex workflows ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagents receive their own system prompt, project CLAUDE.md, and tool definitions, but do not receive the parent's conversation history, skills (unless listed in `AgentDefinition.skills`), or parent system prompt ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagent invocation is detected via `tool_use` blocks where `name` is `"Agent"` or `"Task"` (legacy); messages within a subagent context include a `parent_tool_use_id` field ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagents can be resumed using `session_id` and `agentId` extracted from the first query; transcripts persist independently of the main conversation and are cleaned up based on `cleanupPeriodDays` (default 30 days) ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]

## Quotes

- "Subagents are separate agent instances that your main agent can spawn to handle focused subtasks. Use subagents to isolate context for focused subtasks, run multiple analyses in parallel, and apply specialized instructions without bloating the main agent's prompt." ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- "The only channel from parent to subagent is the Agent tool's prompt string, so include any file paths, error messages, or decisions the subagent needs directly in that prompt." ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- "Programmatically defined agents take precedence over filesystem-based agents with the same name." ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]

## Notes

- On Windows, subagents with very long prompts may fail due to command line length limits (8191 chars); use filesystem-based agents for complex instructions instead ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Filesystem-based agents in `.claude/agents/` are loaded at startup only; creating a new agent file while Claude Code is running requires a session restart ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- The tool name was renamed from `"Task"` to `"Agent"` in Claude Code v2.1.63; current SDK releases emit `"Agent"` in `tool_use` blocks but still use `"Task"` in `system:init` tools list and `result.permission_denials[].tool_name` ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/subagents]]
- [[concepts/agent_loop]]
- [[concepts/skills]]
- [[concepts/custom_tools]]
- [[concepts/permissions]]
- [[concepts/sessions]]