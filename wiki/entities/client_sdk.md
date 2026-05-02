---
title: "Anthropic Client SDK"
summary: "Anthropic's direct API access SDK where developers send prompts and implement tool execution loops themselves"
type: entity
sources:
  - raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md
tags:
  - anthropic
  - client-sdk
  - api
  - development-tools
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Anthropic Client SDK

Anthropic's direct API access SDK where developers send prompts and implement tool execution themselves. Unlike the Agent SDK, the Client SDK does not handle tool execution autonomously; developers must implement the tool loop. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Key Facts

- Provides direct API access: developers send prompts and receive responses, but must implement tool execution themselves ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Developers implement the tool loop manually: check for `tool_use` stop reasons, execute the tool, feed results back, and repeat ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- The Agent SDK differs by handling tool execution autonomously within the built-in agent loop ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Suitable for use cases requiring fine-grained control over each API request and response cycle ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/managed_agents]]
- [[concepts/agent_loop]]
- [[concepts/custom_tools]]