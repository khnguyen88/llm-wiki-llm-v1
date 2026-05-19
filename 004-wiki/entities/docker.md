---
title: "Docker"
summary: "Container platform providing isolation through Linux namespaces, used for sandboxing Claude Code and Agent SDK deployments with hardened security configurations"
type: entity
sources:
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
tags:
  - containers
  - security
  - deployment
  - isolation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Docker

A container platform providing isolation through Linux namespaces, where each container has its own view of the filesystem, process tree, and network stack while sharing the host kernel. Used for sandboxing Claude Code and Agent SDK deployments. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Key Facts

- Containers share the host kernel; a kernel vulnerability could allow container escape ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Isolation strength is "setup dependent" with low performance overhead and medium complexity ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `--cap-drop ALL` removes Linux capabilities like `NET_ADMIN` and `SYS_ADMIN` that could enable privilege escalation ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `--security-opt no-new-privileges` prevents processes from gaining privileges through setuid binaries ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `--security-opt seccomp=...` restricts available syscalls; Docker's default blocks ~44 syscalls, custom profiles can block more ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `--network none` removes all network interfaces; the agent communicates only through a mounted Unix socket connected to a host proxy ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `--read-only` makes the root filesystem immutable; `--tmpfs` mounts provide ephemeral writable directories ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `--userns-remap` maps container root to an unprivileged host user, limiting damage from container escape; `--ipc private` isolates inter-process communication ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Avoid mounting sensitive host directories like `~/.ssh`, `~/.aws`, or `~/.config` even as read-only ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Docker and Docker Compose are pre-installed in Claude Code on the Web cloud sessions for running containerized services; ask Claude to run `docker compose up` to start project services ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Pulled Docker images are saved in the cached environment, so each new session has them on disk; the cache stores files only, not running processes, so containers must be started each session ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Related

- [[entities/gvisor]]
- [[entities/sandbox_runtime]]
- [[entities/firecracker]]
- [[concepts/sandbox_hosting]]
- [[concepts/deployment_patterns]]
- [[concepts/secure_deployment]]
- [[concepts/cloud_environment]]