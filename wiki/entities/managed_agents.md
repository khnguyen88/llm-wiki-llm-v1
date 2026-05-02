---
title: "Managed Agents"
summary: "Anthropic's hosted REST API service that runs AI agents in managed sandboxes, handling infrastructure, session state, and tool execution"
type: entity
sources:
  - raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
tags:
  - anthropic
  - managed-agents
  - hosting
  - rest-api
  - sandbox
  - commands
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Managed Agents

A hosted REST API service from Anthropic that runs AI agents in managed sandboxes. Anthropic operates the agent infrastructure and sandbox, while applications send events and stream results. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Key Facts

- Runs on Anthropic-managed infrastructure as a REST API, contrasted with the Agent SDK which runs inside the developer's own process ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Each session gets a managed sandbox; the agent works on files within that sandbox ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Session state is stored in an Anthropic-hosted event log, rather than JSONL on the developer's filesystem ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Custom tools work by Claude triggering the tool and the application executing it and returning results, rather than in-process functions ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Best for production agents without operating sandbox or session infrastructure, and for long-running asynchronous sessions ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- A common path is to prototype with the Agent SDK locally, then move to Managed Agents for production ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- `/claude-api managed-agents-onboard` provides an interactive walkthrough that creates a new Managed Agent from scratch ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/client_sdk]]
- [[concepts/sandbox_hosting]]
- [[concepts/deployment_patterns]]
- [[concepts/agent_loop]]
- [[concepts/commands]]