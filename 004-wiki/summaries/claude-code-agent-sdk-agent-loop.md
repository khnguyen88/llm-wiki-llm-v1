---
title: "Claude Code Agent Sdk Agent Loop"
summary: "Explains how the Agent SDK's execution loop works: message lifecycle, tool execution, context window management, permission modes, and hooks"
type: summary
sources:
  - raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md
tags:
  - claude-code
  - agent-sdk
  - agent-loop
  - context-window
  - hooks
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Agent Loop

## Key Points

- The Agent SDK embeds Claude Code's autonomous agent loop in external applications; the SDK is a standalone package that does not require the Claude Code CLI ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Every agent session follows a five-step cycle: receive prompt, evaluate/respond, execute tools, repeat, and return result ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- A turn is one round trip of Claude producing output with tool calls, the SDK executing those tools, and results feeding back automatically; turns continue until Claude produces output with no tool calls ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- The SDK yields five message types: SystemMessage, AssistantMessage, UserMessage, StreamEvent, and ResultMessage ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Context accumulates across turns and does not reset; when it approaches the window limit, the SDK automatically compacts older history into summaries ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Read-only tools (Read, Glob, Grep, read-only MCP tools) can execute in parallel; state-modifying tools (Edit, Write, Bash) run sequentially ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Six permission modes control tool approval: default, acceptEdits, plan, dontAsk, auto (TypeScript only), and bypassPermissions ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

## Quotes

- "The Agent SDK lets you embed Claude Code's autonomous agent loop in your own applications. The SDK is a standalone package that gives you programmatic control over tools, permissions, cost limits, and output." ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- "Content that stays the same across turns (system prompt, tool definitions, CLAUDE.md) is automatically prompt cached, which reduces cost and latency for repeated prefixes." ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- "Each subagent starts with a fresh conversation (no prior message history, though it does load its own system prompt and project-level context like CLAUDE.md). It does not see the parent's turns, and only its final response returns to the parent as a tool result." ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

## Notes

- The source provides a comprehensive reference for the Agent SDK's loop architecture, covering message types, tool execution semantics, permission controls, effort levels, context management, and hook lifecycle
- ResultMessage subtypes distinguish success from various error conditions (max turns, max budget, execution error, structured output retries)
- The effort parameter (low/medium/high/xhigh/max) trades latency and token cost for reasoning depth and is independent of extended thinking

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/agent_loop]]
- [[concepts/context_window]]
- [[concepts/hooks]]