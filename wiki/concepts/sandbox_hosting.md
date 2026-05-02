---
title: "Sandbox Hosting"
summary: "The practice of running the Agent SDK inside container-based sandboxed environments for security isolation, resource limits, and controlled execution"
type: concept
sources:
  - raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
tags:
  - sandboxing
  - hosting
  - containers
  - agent-sdk
  - security
  - isolation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Sandbox Hosting

Running the Agent SDK inside a sandboxed container environment for security isolation, resource limits, and controlled execution. Because the Agent SDK executes commands in a persistent shell and manages file operations, container-based sandboxing provides process isolation, resource limits, network control, and ephemeral filesystems. ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

## Key Points

- The Agent SDK should run inside a sandboxed container environment for process isolation, resource limits, network control, and ephemeral filesystems ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- The SDK supports programmatic sandbox configuration for command execution via sandbox settings ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Six third-party sandbox providers are available: Modal, Cloudflare, Daytona, E2B, Fly.io, and Vercel ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Self-hosted sandbox options include Docker, gVisor, and Firecracker ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Each SDK instance requires recommended resources of 1GiB RAM, 5GiB disk, and 1 CPU; network access requires outbound HTTPS to `api.anthropic.com` plus optional MCP server connectivity ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]
- Four isolation technologies with increasing strength: sandbox-runtime (good, very low overhead, low complexity), Docker containers (setup-dependent, low overhead, medium complexity), gVisor (excellent, medium/high overhead, medium complexity), VMs like Firecracker (excellent, high overhead, medium/high complexity) ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- With `--network none` in Docker, the agent has no network interfaces and can only communicate through a mounted Unix socket connected to a proxy on the host ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Filesystem controls include read-only code mounting (`-v /path:/workspace:ro`), tmpfs for ephemeral writable locations (cleared on container stop), and overlay filesystems for review-before-apply workflows ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Details

Unlike stateless LLM API calls, the Agent SDK operates as a long-running process that executes commands, manages file operations, and handles tool execution with context from previous interactions. This stateful architecture makes sandboxing essential for production deployments: without isolation, a compromised or misbehaving agent could affect the host system.

Both SDK packages (Python `claude_agent_sdk` and TypeScript `@anthropic-ai/claude-code`) bundle a native Claude Code binary for the host platform, so no separate Claude Code or Node.js installation is needed for the spawned CLI. Runtime dependencies are Python 3.10+ for the Python SDK or Node.js 18+ for the TypeScript SDK. ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

Communication with sandboxed instances works by exposing ports; applications can expose HTTP/WebSocket endpoints for external clients while the SDK runs internally within the container. Idle container timeout behavior is provider-dependent, and the source recommends tuning based on expected user response frequency. ^[raw/document/claude code/claude-code-008-agent-sdk-hosting-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/deployment_patterns]]
- [[concepts/cost_tracking]]
- [[concepts/agent_loop]]
- [[concepts/secure_deployment]]
- [[concepts/proxy_pattern]]
- [[entities/sandbox_runtime]]
- [[entities/gvisor]]
- [[entities/firecracker]]
- [[entities/docker]]