---
title: "Claude Code Authentication"
summary: "Authentication methods and credential management for Claude Code, covering individual login, team authentication via Console or cloud providers, credential storage, precedence rules, and long-lived tokens"
type: summary
sources:
  - raw/document/claude code/claude-code-034-authentication-2026-04-29.md
tags:
  - claude-code
  - authentication
  - credentials
  - enterprise
  - cloud-providers
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Authentication

## Key Points

- Claude Code supports multiple authentication methods: Claude.ai account login (Pro/Max/Teams/Enterprise), Claude Console credentials, and cloud provider authentication (Amazon Bedrock, Google Vertex AI, Microsoft Foundry) ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Credentials are stored in macOS Keychain (macOS) or `~/.claude/.credentials.json` (Linux/Windows), with the file written with mode 0600 on Linux and inheriting user profile ACLs on Windows ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Authentication precedence order: cloud provider credentials (when env vars set) > `ANTHROPIC_AUTH_TOKEN` > `ANTHROPIC_API_KEY` > `apiKeyHelper` script > `CLAUDE_CODE_OAUTH_TOKEN` > subscription OAuth from `/login` ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `apiKeyHelper` setting runs a shell script that returns an API key, refreshing by default after 5 minutes or on HTTP 401; customizable via `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `claude setup-token` generates a one-year OAuth token for CI pipelines; set as `CLAUDE_CODE_OAUTH_TOKEN` environment variable ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` apply only to terminal CLI sessions; Claude Desktop and remote sessions use OAuth exclusively ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Claude Console supports two user roles: Claude Code role (API keys only) and Developer role (any API key type) ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Notes

- The authentication precedence can cause unexpected failures: an active Claude subscription with `ANTHROPIC_API_KEY` set will use the API key once approved, which fails if the key belongs to a disabled or expired organization. Run `unset ANTHROPIC_API_KEY` to fall back to subscription.
- `claude setup-token` tokens are scoped to inference only and cannot establish Remote Control sessions; bare mode does not read `CLAUDE_CODE_OAUTH_TOKEN`.
- Claude Code on the Web always uses subscription credentials; `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` in the sandbox do not override them.

## Related

- [[entities/claude_code]]
- [[entities/claude_console]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[concepts/authentication]]
- [[concepts/managed_settings]]
- [[concepts/permissions]]