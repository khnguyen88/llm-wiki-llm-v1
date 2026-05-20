---
title: "Deployment Patterns"
summary: "Four production deployment patterns for hosting the Agent SDK: ephemeral, long-running, hybrid, and single-container"
type: concept
sources:
  - raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md
tags:
  - deployment
  - hosting
  - agent-sdk
  - architecture
  - containers
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Deployment Patterns

Four production deployment patterns for hosting the Agent SDK in container environments, each suited to different workload characteristics and interaction models. ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

## Key Points

- **Ephemeral sessions** create a new container per task and destroy it on completion; best for one-off tasks where the user interacts during execution but the container is discarded after ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- **Long-running sessions** maintain persistent container instances, often running multiple Agent processes inside one container; best for proactive agents, content-serving agents, or high-frequency message processing ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- **Hybrid sessions** use ephemeral containers hydrated with history and state from a database or SDK session resumption; best for intermittent interactions that resume where they left off ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- **Single containers** run multiple Agent SDK processes in one global container; best for agents that must collaborate closely, but least popular because agents risk overwriting each other's work ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

## Details

Each pattern addresses a different ownership and lifecycle model. Ephemeral sessions are the simplest: spin up, execute, tear down. They suit tasks like bug investigation, invoice processing, translation, and media processing where the work has a clear beginning and end. ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

Long-running sessions trade simplicity for persistence. An email agent that monitors incoming mail, a site builder that hosts per-user websites with live editing, or a high-frequency chatbot on Slack all require the agent to remain active and responsive over extended periods. Multiple Agent processes may run inside the same container to handle concurrent demand. ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

Hybrid sessions combine the cost efficiency of ephemeral containers with the continuity of long-running ones. State is persisted externally (database or SDK session resumption) and loaded when the user returns. Examples include project managers with intermittent check-ins, deep research tasks that span hours, and customer support agents that load ticket history across multiple interactions. ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

Single containers are the least popular pattern because coordinating multiple agents in the same filesystem requires preventing them from overwriting each other's work. The primary use case is simulations where agents must interact directly with each other, such as in video game environments. ^[001a-raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

## Related

- [[004-wiki/entities/agent_sdk]]
- [[004-wiki/concepts/sandbox_hosting]]
- [[004-wiki/concepts/agent_loop]]
- [[004-wiki/concepts/cost_tracking]]