---
title: "Claude Code Admin Setup"
summary: "Decision map for deploying Claude Code organizationally, covering API providers, managed settings delivery, policy enforcement, usage monitoring, and data handling"
type: summary
sources:
  - raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md
tags:
  - claude-code
  - admin
  - deployment
  - managed-settings
  - compliance
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Admin Setup

## Key Points

- Claude Code enforces organization policy through managed settings that take precedence over local developer configuration; settings can be delivered via server-managed (highest), plist/registry, file-based, or Windows user registry (lowest) mechanisms ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Five API providers available: Claude for Teams/Enterprise (default, per-seat), Claude Console (API-first, pay-as-you-go), Amazon Bedrock (AWS compliance), Google Vertex AI (GCP compliance), Microsoft Foundry (Azure compliance) ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Array settings such as `permissions.allow` and `permissions.deny` merge entries from all sources — developers can extend managed lists but cannot remove from them ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Permission rules and sandboxing address different threat layers: denying WebFetch blocks Claude's fetch tool, but `curl` and `wget` through Bash remain accessible unless OS-level sandboxing closes that gap ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Usage monitoring via OpenTelemetry works with all providers; analytics dashboard and cost tracking are Anthropic-only ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- On Team, Enterprise, Claude API, and cloud provider plans, Anthropic does not train models on code or prompts; Zero Data Retention (nothing stored after request completion) is available on Claude for Enterprise ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Verification: `/status` inside Claude Code shows "Enterprise managed settings" followed by the source indicator — `(remote)`, `(plist)`, `(HKLM)`, `(HKCU)`, or `(file)` ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]

## Notes

- The source is a decision map aimed at administrators, structured as five sequential decisions: provider, settings delivery, enforcement scope, usage visibility, and data handling
- WSL reads only the Linux file path `/etc/claude-code/managed-settings.json` by default; set `wslInheritsWindowsSettings: true` in Windows admin-only sources to extend Windows registry and Program Files policy to WSL on the same machine ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Cloud providers expose spend through their native billing tools (AWS Cost Explorer, GCP Billing, Azure Cost Management) rather than Anthropic's dashboard ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/managed_settings]]