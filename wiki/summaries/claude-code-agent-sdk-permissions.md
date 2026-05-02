---
title: "Claude Code Agent Sdk Permissions"
summary: "How the Agent SDK evaluates and enforces tool permissions through a five-step flow: hooks, deny rules, permission mode, allow rules, and canUseTool callback"
type: summary
sources:
  - raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md
tags:
  - agent-sdk
  - permissions
  - access-control
  - security
  - permission-modes
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Permissions

## Key Points

- Permission evaluation follows a strict five-step order: hooks, deny rules, permission mode, allow rules, and `canUseTool` callback; deny rules and hooks can block tools even in `bypassPermissions` mode ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Six permission modes control tool approval: `default` (no auto-approvals), `dontAsk` (deny unmatched), `acceptEdits` (auto-approve file ops), `bypassPermissions` (approve everything), `plan` (no tool execution), and `auto` (TypeScript only, model-classified) ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- `allowed_tools` pre-approves specific tools but does not constrain `bypassPermissions`; `disallowed_tools` always blocks and overrides every mode including `bypassPermissions` ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Permission mode can be set at query time via `permission_mode` / `permissionMode` and changed dynamically mid-session via `set_permission_mode()` / `setPermissionMode()` ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- When a parent uses `bypassPermissions`, `acceptEdits`, or `auto`, all subagents inherit that mode and it cannot be overridden per subagent ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- `acceptEdits` auto-approves file edits and filesystem commands (`mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`) but only for paths inside the working directory or `additionalDirectories` ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Allow, deny, and ask rules can also be declared in `.claude/settings.json`, loaded when the `project` setting source is enabled ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]

## Quotes

- "`allowed_tools` does not constrain `bypassPermissions`. Every tool is approved, not just the ones you listed. Deny rules (`disallowed_tools`), explicit `ask` rules, and hooks are evaluated before the mode check and can still block a tool." ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]

## Notes

- The `auto` mode (TypeScript only) uses a model classifier for approval decisions and has separate availability requirements
- For a fully locked-down agent, pair `allowedTools` with `permissionMode: "dontAsk"` — listed tools are approved, everything else is denied outright
- `plan` mode allows Claude to use `AskUserQuestion` to clarify requirements before finalizing a plan

## Related

- [[entities/agent_sdk]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/subagents]]
- [[concepts/setting_sources]]