---
title: "Network Access"
summary: "Outbound connection controls for Claude Code on the Web cloud environments, with four access levels, a GitHub proxy, and a security proxy filtering all traffic"
type: concept
sources:
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
tags:
  - claude-code
  - cloud
  - networking
  - security
  - proxy
  - firewall
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Network Access

Network access controls outbound connections from Claude Code on the Web cloud environments. Each environment specifies one access level, extendable with custom allowed domains. The default level is Trusted. ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Key Points

- Four access levels: None (no outbound), Trusted (allowlisted domains only, the default), Full (any domain), Custom (user-defined allowlist, optionally including the Trusted defaults) ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- GitHub operations use a separate proxy that is independent of the network access level setting; inside the sandbox, git authenticates via a scoped credential that the proxy translates to the user's actual token ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- All outbound traffic passes through an HTTP/HTTPS security proxy providing protection against malicious requests, rate limiting, and content filtering ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- The Trusted allowlist covers Anthropic services, version control (GitHub, GitLab, Bitbucket), container registries (Docker Hub, GCR, GHCR, MCR, ECR), cloud platforms (GCP, Azure, AWS, Oracle), package managers (npm, PyPI, RubyGems, crates.io, Go, Maven, Packagist, NuGet, pub.dev, hex.pm, CPAN, CocoaPods, Hackage, Swift), Linux distributions, development tools, monitoring services, and MCP domains ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Custom domains support wildcard subdomain matching with `*.` prefix (e.g., `*.internal.example.com`) ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Some package managers (notably Bun) have known proxy compatibility issues when operating behind the security proxy ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Details

The GitHub proxy provides security boundaries for git operations: it manages authentication by translating scoped credentials inside the sandbox to the user's actual GitHub token, restricts git push operations to the current working branch, and enables cloning, fetching, and PR operations while maintaining isolation. The security proxy applies to all other outbound traffic and is designed for abuse prevention as well as security filtering.

Environments with None network access cannot run setup scripts that install packages, since no outbound connections are permitted. The Trusted level covers most common development workflows. The Full level should be used cautiously as it allows connections to any domain. Custom allows organizations to define their own allowlists, with an option to include the default Trusted domains alongside custom entries.

## Related

- [[entities/claude_code_web]]
- [[concepts/cloud_environment]]
- [[entities/github]]