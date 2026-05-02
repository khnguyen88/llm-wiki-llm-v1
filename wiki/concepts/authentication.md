---
title: "Authentication"
summary: "Mechanism by which Claude Code verifies user identity and authorizes API access, supporting six credential sources with defined precedence"
type: concept
sources:
  - raw/document/claude code/claude-code-034-authentication-2026-04-29.md
tags:
  - claude-code
  - authentication
  - credentials
  - security
  - enterprise
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Authentication

Authentication in Claude Code verifies user identity and authorizes API access through multiple credential sources with a strict precedence order. Individual users authenticate via browser login with a Claude.ai account, while teams and organizations can use Claude Console, cloud provider credentials, or long-lived OAuth tokens. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Key Points

- Six credential sources in precedence order: (1) cloud provider credentials when `CLAUDE_CODE_USE_BEDROCK`/`CLAUDE_CODE_USE_VERTEX`/`CLAUDE_CODE_USE_FOUNDRY` is set, (2) `ANTHROPIC_AUTH_TOKEN` as bearer header, (3) `ANTHROPIC_API_KEY` as `X-Api-Key` header, (4) `apiKeyHelper` script output, (5) `CLAUDE_CODE_OAUTH_TOKEN`, (6) subscription OAuth from `/login` ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- First-launch authentication opens a browser for OAuth login; press `c` to copy the login URL if the browser doesn't open automatically ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `ANTHROPIC_API_KEY` is prompted once for approval in interactive mode (choice remembered); use the "Use custom API key" toggle in `/config` to change later; in non-interactive mode (`-p`), the key is always used ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `claude setup-token` generates a one-year OAuth token for non-interactive environments (CI, scripts); token is scoped to inference only and cannot establish Remote Control sessions ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` apply only to terminal CLI sessions; Claude Desktop and remote sessions use OAuth exclusively and do not call `apiKeyHelper` or read API key environment variables ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Details

### Credential Storage

On macOS, credentials are stored in the encrypted macOS Keychain. On Linux, credentials are stored in `~/.claude/.credentials.json` with file mode 0600. On Windows, the same file inherits the access controls of the user profile directory. The `CLAUDE_CONFIG_DIR` environment variable overrides the default storage location. Supported authentication types include Claude.ai credentials, Claude API credentials, Azure Auth, Bedrock Auth, and Vertex Auth. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

### Dynamic Credentials

The `apiKeyHelper` setting allows running a shell script that returns an API key, enabling integration with vaults or credential rotation systems. By default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. The refresh interval can be customized via `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`. If the helper takes longer than 10 seconds, Claude Code displays a warning in the prompt bar showing elapsed time. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

### Precedence Pitfalls

When an active Claude subscription exists alongside `ANTHROPIC_API_KEY`, the API key takes precedence once approved. This can cause authentication failures if the key belongs to a disabled or expired organization. Running `unset ANTHROPIC_API_KEY` falls back to the subscription. Claude Code on the Web always uses subscription credentials; `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` in the sandbox environment do not override them. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

### Team Authentication Options

Teams and organizations can configure Claude Code access through: Claude for Teams or Enterprise (recommended for most teams, provides web + Code with centralized billing), Claude Console (API-based billing, supports SSO), or cloud providers (Amazon Bedrock, Google Vertex AI, Microsoft Foundry). Cloud provider authentication requires setting environment variables before running `claude` and does not require browser login. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/claude_console]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[concepts/managed_settings]]
- [[concepts/permissions]]
- [[concepts/secure_deployment]]
- [[concepts/sessions]]