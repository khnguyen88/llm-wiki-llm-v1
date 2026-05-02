---
title: "Claude Code Agent SDK Hosting"
summary: "Architecture, sandboxing requirements, and four production deployment patterns for hosting the Claude Agent SDK as a long-running stateful process"
type: summary
sources:
  - raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md
tags:
  - agent-sdk
  - hosting
  - deployment
  - sandboxing
  - containers
  - claude-code
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent SDK Hosting

## Key Points

- The Agent SDK differs from stateless LLM APIs by maintaining conversational state and executing commands in a persistent environment, requiring container-based sandboxing for security and isolation ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Each SDK instance requires Python 3.10+ or Node.js 18+, recommended 1GiB RAM / 5GiB disk / 1 CPU, and outbound HTTPS to `api.anthropic.com`; both SDK packages bundle a native Claude Code binary so no separate install is needed ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Four production deployment patterns are identified: ephemeral sessions (create/destroy per task), long-running sessions (persistent containers with multiple processes), hybrid sessions (ephemeral containers hydrated with state), and single containers (multiple processes in one container) ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Six sandbox providers are listed: Modal, Cloudflare, Daytona, E2B, Fly.io, and Vercel; self-hosted options include Docker, gVisor, and Firecracker ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Agent sessions do not time out, but `maxTurns` should be set to prevent Claude from looping indefinitely ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- The dominant hosting cost is tokens; container costs start at roughly 5 cents per hour ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

## Notes

- The source focuses on production deployment architecture; for security hardening details it defers to the Secure Deployment guide ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/sandbox_hosting]]
- [[concepts/deployment_patterns]]
- [[concepts/agent_loop]]
- [[concepts/cost_tracking]]