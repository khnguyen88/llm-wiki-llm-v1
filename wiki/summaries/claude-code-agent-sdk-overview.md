---
title: "Claude Code Agent Sdk Overview"
summary: "Overview of the Claude Agent SDK for building production AI agents with built-in tools, hooks, subagents, MCP, permissions, and sessions"
type: summary
sources:
  - raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md
tags:
  - agent-sdk
  - claude-code
  - overview
  - tools
  - hooks
  - subagents
  - mcp
  - permissions
  - sessions
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Overview

The Claude Agent SDK embeds Claude Code's tools, agent loop, and context management as a programmable library available in Python and TypeScript, enabling developers to build AI agents that autonomously read files, run commands, search the web, and edit code. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Key Points

- The SDK provides the same tools, agent loop, and context management that power Claude Code, programmable via Python (`claude_agent_sdk`) and TypeScript (`@anthropic-ai/claude-agent-sdk`) ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Built-in tools (Read, Write, Edit, Bash, Monitor, Glob, Grep, WebSearch, WebFetch, AskUserQuestion) enable agents to work immediately without custom tool implementation ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Hooks run custom code at lifecycle points (PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd, UserPromptSubmit) to validate, log, block, or transform agent behavior ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Subagents are specialized agents defined via AgentDefinition with custom instructions and tool sets; the Agent tool must be included in allowedTools ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- MCP servers connect the agent to external systems like databases, browsers, and APIs via the mcpServers option ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Permissions control tool access through allowed_tools (pre-approves specific tools) and permission_mode (sets approval behavior) ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Sessions maintain context across exchanges; session_id from SystemMessage init enables resume and fork operations ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Authentication supports API key (ANTHROPIC_API_KEY), Amazon Bedrock (CLAUDE_CODE_USE_BEDROCK=1), Google Vertex AI (CLAUDE_CODE_USE_VERTEX=1), and Microsoft Azure (CLAUDE_CODE_USE_FOUNDRY=1) ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Opus 4.7 (`claude-opus-4-7`) requires Agent SDK v0.2.111 or later ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Quotes

> Build AI agents that autonomously read files, run commands, search the web, edit code, and more. The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

> A common path is to prototype with the Agent SDK locally, then move to Managed Agents for production. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Notes

- The source is an overview page that summarizes SDK capabilities at a high level; dedicated pages exist for each topic (hooks, MCP, custom tools, sessions, etc.) with deeper detail
- Branding guidelines for partners: "Claude Agent" is preferred; "Claude Code" or "Claude Code Agent" are not permitted in partner products ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Use of the Agent SDK is governed by Anthropic's Commercial Terms of Service ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[entities/managed_agents]]
- [[entities/client_sdk]]
- [[concepts/agent_loop]]
- [[concepts/hooks]]
- [[concepts/mcp]]
- [[concepts/permissions]]
- [[concepts/sessions]]
- [[concepts/subagents]]
- [[concepts/setting_sources]]
- [[concepts/skills]]
- [[concepts/custom_tools]]
- [[concepts/cost_tracking]]
- [[concepts/file_checkpointing]]
- [[concepts/observability]]
- [[concepts/deployment_patterns]]