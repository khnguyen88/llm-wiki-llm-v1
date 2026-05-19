---
title: "sandbox-runtime"
summary: "Anthropic's lightweight sandbox package that enforces filesystem and network restrictions at the OS level for Claude Code and Agent SDK"
type: entity
sources:
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
tags:
  - sandboxing
  - security
  - agent-sdk
  - npm
  - isolation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# sandbox-runtime

An npm package (`@anthropic-ai/sandbox-runtime`) from Anthropic that provides lightweight OS-level isolation for Claude Code and Agent SDK without requiring Docker, container images, or networking setup. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Key Facts

- Installed via `npm install @anthropic-ai/sandbox-runtime` ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Uses OS primitives for filesystem restrictions: `bubblewrap` on Linux and `sandbox-exec` on macOS ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Network isolation removes the network namespace (Linux) or uses Seatbelt profiles (macOS) to route traffic through a built-in proxy ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Configuration is JSON-based with allowlists for domains and filesystem paths ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Isolation strength is rated "good" with very low performance overhead and low complexity ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Sandbox processes share the host kernel; a kernel vulnerability could theoretically enable escape, so kernel-level isolation requires [[entities/gvisor]] or a VM ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- The built-in proxy does not terminate or inspect encrypted traffic; domain fronting could potentially bypass the allowlist ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/gvisor]]
- [[entities/firecracker]]
- [[concepts/sandbox_hosting]]
- [[concepts/proxy_pattern]]
- [[concepts/secure_deployment]]