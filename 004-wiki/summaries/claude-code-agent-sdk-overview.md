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

The Claude Agent SDK embeds Claude Code's tools, agent loop, and context management as a programmable library available in Python and TypeScript, enabling developers to build AI agents that autonomously read files, run commands, search the web, and edit code. ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Key Points

- The SDK provides the same tools, agent loop, and context management that power Claude Code, programmable via Python (`claude_agent_sdk`) and TypeScript (`@anthropic-ai/claude-agent-sdk`) ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Built-in tools (Read, Write, Edit, Bash, Monitor, Glob, Grep, WebSearch, WebFetch, AskUserQuestion) enable agents to work immediately without custom tool implementation ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Hooks run custom code at lifecycle points (PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd, UserPromptSubmit) to validate, log, block, or transform agent behavior ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Subagents are specialized agents defined via AgentDefinition with custom instructions and tool sets; the Agent tool must be included in allowedTools ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- MCP servers connect the agent to external systems like databases, browsers, and APIs via the mcpServers option ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Permissions control tool access through allowed_tools (pre-approves specific tools) and permission_mode (sets approval behavior) ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Sessions maintain context across exchanges; session_id from SystemMessage init enables resume and fork operations ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Authentication supports API key (ANTHROPIC_API_KEY), Amazon Bedrock (CLAUDE_CODE_USE_BEDROCK=1), Google Vertex AI (CLAUDE_CODE_USE_VERTEX=1), and Microsoft Azure (CLAUDE_CODE_USE_FOUNDRY=1) ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Opus 4.7 (`claude-opus-4-7`) requires Agent SDK v0.2.111 or later ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Quotes

> Build AI agents that autonomously read files, run commands, search the web, edit code, and more. The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript. ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

> A common path is to prototype with the Agent SDK locally, then move to Managed Agents for production. ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Notes

- The source is an overview page that summarizes SDK capabilities at a high level; dedicated pages exist for each topic (hooks, MCP, custom tools, sessions, etc.) with deeper detail
- Branding guidelines for partners: "Claude Agent" is preferred; "Claude Code" or "Claude Code Agent" are not permitted in partner products ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Use of the Agent SDK is governed by Anthropic's Commercial Terms of Service ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Related

- [[004-wiki/entities/agent-sdk]]
- [[004-wiki/entities/claude-code]]
- [[004-wiki/entities/managed-agents]]
- [[004-wiki/entities/client-sdk]]
- [[004-wiki/concepts/agent-loop]]
- [[004-wiki/concepts/hooks]]
- [[004-wiki/concepts/mcp]]
- [[004-wiki/concepts/permissions]]
- [[004-wiki/concepts/sessions]]
- [[004-wiki/concepts/subagents]]
- [[004-wiki/concepts/setting-sources]]
- [[004-wiki/concepts/skills]]
- [[004-wiki/concepts/custom-tools]]
- [[004-wiki/concepts/cost-tracking]]
- [[004-wiki/concepts/file-checkpointing]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/concepts/deployment-patterns]]