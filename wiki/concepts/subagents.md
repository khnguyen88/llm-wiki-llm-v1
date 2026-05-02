---
title: "Subagents"
summary: "Specialized agents spawned by a main agent to handle focused subtasks, defined with custom instructions and tool sets, reporting results back to the parent"
type: concept
sources:
  - raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md
  - raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md
  - raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md
  - raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md
  - raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
tags:
  - agent-sdk
  - subagents
  - delegation
  - agent-architecture
  - agent-teams
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Subagents

Specialized agents spawned by a main agent to handle focused subtasks. The main agent delegates work, and subagents report back with results. Subagents are defined with custom instructions and restricted tool sets via AgentDefinition. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Key Points

- Subagents are specialized agents defined via `AgentDefinition` with `description`, `prompt`, and `tools` fields ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- The `Agent` tool must be included in `allowed_tools` for the main agent to delegate to subagents ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Messages from subagents include a `parent_tool_use_id` field to track which messages belong to which subagent execution ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Subagents enable a delegation pattern where a main agent distributes focused work to specialized agents ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- When the parent uses `bypassPermissions`, `acceptEdits`, or `auto`, all subagents inherit that permission mode and it cannot be overridden per subagent ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Unlike Skills (which must be created as filesystem artifacts), subagents can be defined programmatically via `AgentDefinition` ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Three creation methods: programmatic `agents` parameter (recommended), filesystem-based `.claude/agents/` markdown definitions, and built-in `general-purpose` subagent available without any definition ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagents run in isolated fresh conversations with no parent history; the only channel from parent to subagent is the Agent tool's prompt string ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagents cannot spawn their own subagents — do not include `Agent` in a subagent's `tools` array ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Multiple subagents can run concurrently for parallelization of complex workflows ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagents receive their own system prompt, project CLAUDE.md (via `settingSources`), and tool definitions; they do not receive the parent's conversation history, skills (unless listed in `AgentDefinition.skills`), or parent system prompt ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- `AgentDefinition` supports `description`, `prompt`, `tools`, `disallowedTools`, `model`, `skills`, `memory`, `mcpServers`, `maxTurns`, `background`, `effort`, and `permissionMode` fields ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Programmatic agent definitions take precedence over filesystem-based agents with the same name ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagent invocation is detected via `tool_use` blocks where `name` is `"Agent"` or `"Task"` (legacy, renamed in v2.1.63); messages within a subagent context include `parent_tool_use_id` ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagents can be resumed by capturing `session_id` from the first query and `agentId` from message content, then passing `resume: sessionId` in a subsequent query ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- On Windows, subagents with prompts exceeding 8191 characters may fail due to command line length limits ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]
- Subagent definitions can be reused as agent team teammates; when used as teammates, the definition's `tools` allowlist and `model` are honored, and the definition body is appended to the teammate's system prompt rather than replacing it ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Using subagents for investigation keeps the main context clean: the subagent explores the codebase, reads relevant files, and reports back with findings without cluttering the main conversation ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Subagents can also be used for verification after implementation: "use a subagent to review this code for edge cases" produces more objective review because the reviewing context hasn't seen the implementation ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Comparison with Agent Teams

| | Subagents | Agent Teams |
|---|---|---|
| **Context** | Own context window; results return to the caller | Own context window; fully independent |
| **Communication** | Report results back to the main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Shared task list with self-coordination |
| **Best for** | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| **Token cost** | Lower: results summarized back to main context | Higher: each teammate is a separate Claude instance |

^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

Use subagents for quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own. ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

## Details

Each subagent is defined with its own instructions and tool set via AgentDefinition, allowing it to focus on a specific domain such as code review, research, or testing. The main agent includes `"Agent"` in its `allowed_tools` to invoke subagents. The `parent_tool_use_id` field on subagent messages enables the calling application to correlate which messages belong to which subagent execution, essential for logging, monitoring, and result aggregation when multiple subagents run. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

Subagents may have different system prompts and less constrained behavior than the main agent, so inheriting `bypassPermissions` grants them full autonomous system access without any approval prompts. This inheritance is mandatory — the inherited mode cannot be overridden on a per-subagent basis. ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]

Context isolation is a primary benefit: each subagent runs in its own fresh conversation, so intermediate tool calls and results stay inside the subagent. Only the final message returns to the parent, keeping the main conversation window clean. Since the only channel from parent to subagent is the Agent tool's prompt string, any file paths, error messages, or decisions the subagent needs must be included directly in that prompt. ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]

Subagent transcripts persist independently of the main conversation. When the main conversation compacts, subagent transcripts are unaffected and stored in separate files. Transcripts are cleaned up based on the `cleanupPeriodDays` setting (default 30 days). A subagent can be resumed by capturing `session_id` from the first query's result message and extracting `agentId` from message content, then passing `resume: sessionId` in a subsequent query. The same agent definition must be passed in the `agents` parameter for both queries when resuming custom agents. ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]

Common tool combinations for subagents include read-only analysis (Read, Grep, Glob), test execution (Bash, Read, Grep), code modification (Read, Edit, Write, Grep, Glob), and full access (omit `tools` field to inherit all parent tools). ^[raw/document/claude code/claude-code-025-agent-sdk-subagents-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/custom_tools]]
- [[concepts/permissions]]
- [[concepts/sessions]]
- [[concepts/skills]]
- [[concepts/setting_sources]]
- [[summaries/claude-code-agent-sdk-subagents]]
- [[concepts/agent_teams]]
- [[concepts/failure_patterns]]
- [[summaries/claude-code-best-practices]]