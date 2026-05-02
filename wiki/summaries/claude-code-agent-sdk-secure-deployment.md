---
title: "Claude Code Agent Sdk Secure Deployment"
summary: "Guide to securing Claude Code and Agent SDK deployments through isolation technologies, credential management with the proxy pattern, and filesystem controls"
type: summary
sources:
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
tags:
  - security
  - deployment
  - agent-sdk
  - sandboxing
  - credential-management
  - isolation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Secure Deployment

## Key Points

- The primary threat for agent deployments is prompt injection, where instructions embedded in processed content cause unintended actions; model error is also a risk ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Built-in security features include a permissions system with glob-based rules, AST-based command parsing for bash, web search summarization to reduce injection risk, and sandbox mode for filesystem/network restrictions ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Three security principles guide hardening: security boundaries (separating components by trust level), least privilege (restricting to minimum required capabilities), and defense in depth (layering multiple controls) ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Four isolation technologies are available with increasing strength: sandbox-runtime (good, very low overhead), Docker containers (setup-dependent, low overhead), gVisor (excellent, medium/high overhead), and VMs like Firecracker (excellent, high overhead) ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- The proxy pattern is the recommended credential management approach: run a proxy outside the agent's security boundary that injects credentials into requests, so the agent never sees them ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `ANTHROPIC_BASE_URL` routes sampling requests to a proxy in plaintext for inspection; `HTTP_PROXY`/`HTTPS_PROXY` routes all HTTP traffic but creates opaque TLS tunnels for HTTPS without TLS termination ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Filesystem controls include read-only code mounting, tmpfs for ephemeral writable locations, and overlay filesystems for review-before-apply workflows ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Quotes

- "Unlike traditional software that follows predetermined code paths, these tools generate their actions dynamically based on context and goals. This flexibility is what makes them useful, but it also means their behavior can be influenced by the content they process." ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- "Securing an agent deployment doesn't require exotic infrastructure. The same principles that apply to running any semi-trusted code apply here: isolation, least privilege, and defense in depth." ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- "Commands that cannot be parsed cleanly, or that do not match an allow rule, require explicit approval. A small set of constructs such as `eval` always require approval regardless of allow rules." ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Notes

- The source emphasizes that not every deployment needs maximum security; a developer laptop has different requirements than a multi-tenant production environment processing customer data
- Cloud deployments combine isolation technologies with cloud-native controls: private subnets, firewall rules, proxy-based credential injection, minimal IAM permissions, and traffic logging
- Not all programs respect `HTTP_PROXY`/`HTTPS_PROXY`; Node.js `fetch()` ignores them by default (set `NODE_USE_ENV_PROXY=1` in Node 24+), and `proxychains` or iptables redirects may be needed for comprehensive coverage

## Related

- [[entities/agent_sdk]]
- [[entities/sandbox_runtime]]
- [[entities/gvisor]]
- [[entities/firecracker]]
- [[entities/docker]]
- [[concepts/sandbox_hosting]]
- [[concepts/deployment_patterns]]
- [[concepts/permissions]]
- [[concepts/proxy_pattern]]
- [[concepts/secure_deployment]]