---
title: "Firecracker"
summary: "AWS's lightweight microVM technology providing hardware-level isolation with sub-125ms boot times and minimal memory overhead"
type: entity
sources:
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
tags:
  - security
  - virtualization
  - isolation
  - aws
  - microvm
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Firecracker

A lightweight microVM technology from AWS designed for secure, fast container-like isolation at the hardware level. Each VM runs its own kernel, creating a strong boundary where a vulnerability in the guest kernel does not directly compromise the host. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Key Facts

- Boots VMs in under 125ms with less than 5 MiB memory overhead ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Strips unnecessary device emulation to reduce attack surface compared to traditional VMs ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Agent VMs communicate through `vsock` (virtual sockets) rather than network interfaces; all traffic routes through vsock to a proxy on the host ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Isolation strength rated "excellent" (with correct setup), with high performance overhead and medium/high complexity ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- VMs are not automatically more secure than alternatives like [[entities/gvisor]]; security depends heavily on the hypervisor and device emulation code ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Related

- [[entities/gvisor]]
- [[entities/docker]]
- [[entities/sandbox_runtime]]
- [[concepts/sandbox_hosting]]
- [[concepts/secure_deployment]]