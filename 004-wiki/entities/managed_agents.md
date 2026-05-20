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

A hosted REST API service from Anthropic that runs AI agents in managed sandboxes. Anthropic operates the agent infrastructure and sandbox, while applications send events and stream results. ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Key Facts

- Runs on Anthropic-managed infrastructure as a REST API, contrasted with the Agent SDK which runs inside the developer's own process ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Each session gets a managed sandbox; the agent works on files within that sandbox ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Session state is stored in an Anthropic-hosted event log, rather than JSONL on the developer's filesystem ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Custom tools work by Claude triggering the tool and the application executing it and returning results, rather than in-process functions ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Best for production agents without operating sandbox or session infrastructure, and for long-running asynchronous sessions ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- A common path is to prototype with the Agent SDK locally, then move to Managed Agents for production ^[001a-raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- `/claude-api managed-agents-onboard` provides an interactive walkthrough that creates a new Managed Agent from scratch ^[001a-raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Related

- [[004-wiki/entities/agent_sdk]]
- [[004-wiki/entities/client_sdk]]
- [[004-wiki/concepts/sandbox_hosting]]
- [[004-wiki/concepts/deployment_patterns]]
- [[004-wiki/concepts/agent_loop]]
- [[004-wiki/concepts/commands]]