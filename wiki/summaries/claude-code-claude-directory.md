---
title: "Claude Code Claude Directory"
summary: "Reference guide for the .claude directory structure, covering configuration files, scopes, settings precedence, application data lifecycle, and plaintext storage security"
type: summary
sources:
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
tags:
  - claude-code
  - configuration
  - settings
  - directory-structure
  - application-data
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Claude Directory

## Key Points

- The `.claude` directory at project level and `~/.claude` at global level store all Claude Code configuration: instructions, settings, skills, subagents, and memory ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Project-scope files live under `.claude/` (or at the project root for `CLAUDE.md`, `.mcp.json`, `.worktreeinclude`); global-scope files live under `~/.claude/` and apply across all projects ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- On Windows, `~/.claude` resolves to `%USERPROFILE%\.claude`; setting `CLAUDE_CONFIG_DIR` overrides all `~/.claude` paths ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Settings precedence from highest to lowest: managed settings, CLI flags, environment variables, then `settings.json` ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE.local.md` (project root, gitignored) holds private preferences alongside `CLAUDE.md`; `settings.local.json` (project only, auto-gitignored) holds personal overrides ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Application data (transcripts, tool results, file snapshots, caches) is stored in `~/.claude/` and auto-cleaned after `cleanupPeriodDays` (default 30); transcripts are plaintext and not encrypted at rest ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Several paths persist indefinitely until manually deleted: `history.jsonl` (prompt history), `stats-cache.json` (usage stats), and legacy `todos/` directory ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Notes

- The source document is primarily a file reference table; the substantive conceptual content is extracted into [[concepts/claude_directory]] and [[concepts/application_data]].

## Related

- [[concepts/claude_directory]]
- [[concepts/application_data]]
- [[concepts/setting_sources]]
- [[concepts/managed_settings]]
- [[concepts/sessions]]
- [[concepts/skills]]
- [[concepts/subagents]]
- [[concepts/hooks]]
- [[concepts/permissions]]
- [[concepts/output_styles]]
- [[concepts/file_checkpointing]]
- [[entities/claude_code]]