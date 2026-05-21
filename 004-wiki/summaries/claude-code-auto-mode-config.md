---
title: "Claude Code Auto Mode Config"
summary: "Configuration reference for Claude Code's auto mode classifier, which routes tool calls through trust-based rules to eliminate permission prompts for routine internal operations"
type: summary
sources:
  - raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md
tags:
  - claude-code
  - auto-mode
  - permissions
  - configuration
  - classifier
  - security
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Auto Mode Config

## Key Points

- Auto mode eliminates permission prompts by routing each tool call through a classifier that blocks irreversible, destructive, or external actions ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- The classifier reads `autoMode` from four scopes: user settings (`~/.claude/settings.json`), local project settings (`.claude/settings.local.json`), managed settings, and inline JSON via `--settings` flag or Agent SDK ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- The classifier does not read `autoMode` from shared project settings (`.claude/settings.json`), preventing a checked-in repo from injecting its own allow rules ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- `autoMode.environment` defines trusted infrastructure as natural-language prose entries; the literal string `"$defaults"` splices in built-in defaults so custom entries can go before or after them ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- The classifier evaluates rules in three tiers: `soft_deny` blocks first, `allow` overrides matching blocks as exceptions, and explicit user intent overrides both ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- Omitting `"$defaults"` from any `autoMode` section replaces the entire default list for that section, discarding all built-in rules ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- CLI subcommands `claude auto-mode defaults`, `claude auto-mode config`, and `claude auto-mode critique` inspect and validate the effective configuration ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]

## Quotes

- "Entries are prose, not regex or tool patterns. The classifier reads them as natural-language rules. Write them the way you would describe your infrastructure to a new engineer." ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- "General requests don't count as explicit intent. Asking Claude to 'clean up the repo' does not authorize force-pushing, but asking Claude to 'force-push this branch' does." ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]

## Notes

- The classifier is a second gate that runs after the permissions system; for actions that must never run regardless of user intent, use `permissions.deny` in managed settings ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- Denied actions appear in `/permissions` under the Recently denied tab; pressing `r` marks for retry ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- The `PermissionDenied` hook enables programmatic reaction to denials ^[001a-raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]

## Related

- [[004-wiki/concepts/auto-mode]]
- [[004-wiki/entities/claude-code]]
- [[004-wiki/concepts/permissions]]
- [[004-wiki/concepts/managed-settings]]
- [[004-wiki/concepts/setting-sources]]
- [[004-wiki/concepts/hooks]]