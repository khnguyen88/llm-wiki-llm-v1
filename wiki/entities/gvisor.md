---
title: "gVisor"
summary: "Google's container isolation runtime that intercepts system calls in userspace to provide kernel-level isolation without a full VM"
type: entity
sources:
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
tags:
  - security
  - containers
  - isolation
  - google
  - syscall
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# gVisor

A container runtime developed by Google that intercepts system calls in userspace before they reach the host kernel, implementing its own compatibility layer that handles most syscalls without involving the real kernel. This reduces the attack surface compared to standard containers, which share the host kernel directly. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Key Facts

- Installed as the `runsc` runtime and configured in `/etc/docker/daemon.json` to enable `docker run --runtime=runsc` ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Standard containers route syscalls directly to the host kernel; gVisor intercepts them in userspace, so malicious code must first exploit gVisor's compatibility layer before reaching the host kernel ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Isolation strength rated "excellent" (with correct setup), with medium/high performance overhead and medium complexity ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- CPU-bound computation has ~0% overhead (no syscall interception needed); simple syscalls are ~2x slower; file I/O intensive workloads can be 10-200x slower for heavy open/close patterns ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Recommended for multi-tenant environments or when processing untrusted content where the additional isolation is worth the overhead ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Related

- [[entities/docker]]
- [[entities/sandbox_runtime]]
- [[entities/firecracker]]
- [[concepts/sandbox_hosting]]
- [[concepts/secure_deployment]]