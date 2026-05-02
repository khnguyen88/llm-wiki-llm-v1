---
title: "Secure Deployment"
summary: "Principles and techniques for securely deploying Claude Code and Agent SDK, including threat modeling, security boundaries, least privilege, and defense in depth"
type: concept
sources:
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
tags:
  - security
  - deployment
  - agent-sdk
  - threat-model
  - least-privilege
  - defense-in-depth
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Secure Deployment

The practice of deploying Claude Code and Agent SDK with appropriate security controls based on the threat model. Unlike traditional software that follows predetermined code paths, AI agents generate actions dynamically based on context, making their behavior influenced by content they process (prompt injection). The same principles that apply to running semi-trusted code apply here: isolation, least privilege, and defense in depth. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Key Points

- The primary threat is prompt injection: instructions embedded in files, webpages, or user input that cause the agent to take unintended actions; model error is also a risk ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Security boundaries separate components with different trust levels; sensitive resources like credentials should be placed outside the boundary containing the agent ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Least privilege restricts the agent to only required capabilities: filesystem (mount only needed directories, prefer read-only), network (restrict to specific endpoints via proxy), credentials (inject via proxy), system capabilities (drop Linux capabilities in containers) ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Defense in depth layers multiple controls: container isolation, network restrictions, filesystem controls, and request validation at a proxy ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Command parsing for permissions uses AST analysis before executing bash commands; commands that cannot be parsed cleanly require explicit approval, and constructs like `eval` always require approval regardless of allow rules ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Details

Not every deployment needs maximum security. A developer running Claude Code on a laptop has different requirements than a company processing customer data in a multi-tenant environment. The built-in security features (permissions system, command parsing, web search summarization, sandbox mode) address common concerns without additional infrastructure. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

For high-security deployments, isolation technologies provide increasing strength at increasing cost: sandbox-runtime (good isolation, very low overhead), [[entities/docker|Docker]] containers (setup-dependent, low overhead), [[entities/gvisor|gVisor]] (excellent, medium/high overhead), and [[entities/firecracker|Firecracker]] VMs (excellent, high overhead). In all configurations, Claude Code or the Agent SDK runs inside the isolation boundary, and security controls restrict what the agent can access from within. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

Cloud deployments combine isolation with cloud-native controls: private subnets with no internet gateway, cloud firewall rules blocking all egress except to the proxy, a proxy (e.g., Envoy with `credential_injector`) that validates requests and injects credentials, minimal IAM permissions, and traffic logging for audit. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

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