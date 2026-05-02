---
title: "Auto Mode"
summary: "Permission mode in Claude Code that eliminates prompts by routing tool calls through a classifier that blocks destructive actions and enforces trust boundaries defined by environment, soft_deny, and allow rules"
type: concept
sources:
  - raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
  - raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md
tags:
  - claude-code
  - auto-mode
  - permissions
  - classifier
  - security
  - trust-boundaries
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Auto Mode

Auto mode lets Claude Code run without permission prompts by routing each tool call through a classifier that blocks anything irreversible, destructive, or aimed outside the environment. The classifier uses trust rules defined in the `autoMode` settings block to distinguish routine internal operations from potentially harmful actions. Auto mode is the middle ground between approving everything and `--dangerously-skip-permissions`: safe actions run without interruption while risky ones get blocked. ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md] ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

## Key Points

- The classifier is a second gate that runs after the permissions system; `permissions.deny` in managed settings blocks actions before the classifier is consulted and cannot be overridden ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- `autoMode.environment` defines trusted infrastructure as natural-language prose entries covering organization, source control, cloud buckets, internal domains, and key services ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- Rule evaluation follows three tiers: `soft_deny` blocks first, `allow` overrides matching blocks as exceptions, and explicit user intent overrides both ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- The classifier reads `autoMode` from user settings, local project settings, managed settings, and inline JSON — but not from shared project `.claude/settings.json`, preventing repos from injecting their own allow rules ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- Entries from each scope are combined additively: developers can extend `environment`, `allow`, and `soft_deny` but cannot remove entries that managed settings provide; a developer-added `allow` entry can override an organization `soft_deny` entry ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- For non-interactive runs with the `-p` flag, auto mode aborts if the classifier repeatedly blocks actions, since there is no user to fall back to ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Cycle to auto mode with `Shift+Tab`, or set it as the default via `"permissions": {"defaultMode": "auto"}` in `.claude/settings.json` ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Details

Out of the box, the classifier trusts only the working directory and the current repo's configured remotes. Actions like pushing to a company source-control org or writing to a team cloud bucket are blocked until added to `autoMode.environment`. The literal string `"$defaults"` in any `autoMode` array splices built-in defaults at that position, allowing custom entries to precede or follow them. Omitting `"$defaults"` replaces the entire default list for that section. ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]

The classifier reads environment entries as natural-language rules, not regex or tool patterns. A thorough `environment` section covers organization identity, source control hosts, cloud providers and trusted buckets, internal domains, key services, and additional compliance context. The recommended rollout starts with defaults plus source control org and key services, then adds trusted domains and cloud buckets as blocks arise. ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]

Explicit user intent overrides both `soft_deny` and `allow` rules, but general requests do not count. Asking Claude to "clean up the repo" does not authorize force-pushing, while asking to "force-push this branch" does. When auto mode denies a tool call, the denial is recorded in `/permissions` under the Recently denied tab, and pressing `r` marks the action for retry. The `PermissionDenied` hook enables programmatic reaction to denials. Three CLI subcommands support inspection: `claude auto-mode defaults` prints built-in rules, `claude auto-mode config` prints the effective merged config, and `claude auto-mode critique` provides AI feedback on custom rules. ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/permissions]]
- [[concepts/managed_settings]]
- [[concepts/setting_sources]]
- [[concepts/hooks]]
- [[concepts/non_interactive_mode]]
- [[summaries/claude-code-best-practices]]