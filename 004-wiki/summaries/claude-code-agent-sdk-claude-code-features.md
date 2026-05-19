---
title: "Claude Code Agent Sdk Claude Code Features"
summary: "Documents how Agent SDK agents access Claude Code filesystem-based features—settingSources, project instructions, skills, and hooks—with configuration examples and feature comparison"
type: summary
sources:
  - raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md
tags:
  - agent-sdk
  - claude-code
  - settings
  - skills
  - hooks
  - configuration
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Claude Code Features

## Key Points

- The `settingSources` option (`setting_sources` in Python, `settingSources` in TypeScript) controls which filesystem-based settings the SDK loads: `"project"` from `<cwd>/.claude/`, `"user"` from `~/.claude/`, `"local"` for gitignored local settings ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Omitting `settingSources` defaults to `["user", "project", "local"]`; passing `settingSources: []` disables all filesystem settings ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Three inputs are read regardless of `settingSources`: managed policy settings, `~/.claude.json` global config, and auto memory at `~/.claude/projects/<project>/memory/` ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- CLAUDE.md files at different levels (project root, parent directories, child directories, local, user) are all additive with no hard precedence rule; conflicts depend on how Claude interprets them ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Skills load on demand (unlike CLAUDE.md which loads every session); the `Skill` tool must be explicitly included in `allowedTools` when using an allowlist ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- The SDK supports both filesystem hooks (defined in `settings.json`, loaded via `settingSources`) and programmatic hooks (callback functions passed to `query()`); they run side by side ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- For multi-tenant deployments, run each tenant in its own filesystem and set `settingSources: []` plus `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env` ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

## Notes

- The source provides a feature comparison table mapping common goals (conventions, on-demand reference, reusable workflows, subtasks, audit/block logic, external service access) to the appropriate Claude Code extension mechanism and its SDK surface

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/setting_sources]]
- [[concepts/skills]]
- [[concepts/hooks]]
- [[concepts/managed_settings]]
- [[concepts/agent_loop]]