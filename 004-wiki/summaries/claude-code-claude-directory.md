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

- The `.claude` directory at project level and `~/.claude` at global level store all Claude Code configuration: instructions, settings, skills, subagents, and memory ^[001a-raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Project-scope files live under `.claude/` (or at the project root for `CLAUDE.md`, `.mcp.json`, `.worktreeinclude`); global-scope files live under `~/.claude/` and apply across all projects ^[001a-raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- On Windows, `~/.claude` resolves to `%USERPROFILE%\.claude`; setting `CLAUDE_CONFIG_DIR` overrides all `~/.claude` paths ^[001a-raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Settings precedence from highest to lowest: managed settings, CLI flags, environment variables, then `settings.json` ^[001a-raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE.local.md` (project root, gitignored) holds private preferences alongside `CLAUDE.md`; `settings.local.json` (project only, auto-gitignored) holds personal overrides ^[001a-raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Application data (transcripts, tool results, file snapshots, caches) is stored in `~/.claude/` and auto-cleaned after `cleanupPeriodDays` (default 30); transcripts are plaintext and not encrypted at rest ^[001a-raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Several paths persist indefinitely until manually deleted: `history.jsonl` (prompt history), `stats-cache.json` (usage stats), and legacy `todos/` directory ^[001a-raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Notes

- The source document is primarily a file reference table; the substantive conceptual content is extracted into [[004-wiki/concepts/claude_directory]] and [[004-wiki/concepts/application_data]].

## Related

- [[004-wiki/concepts/claude_directory]]
- [[004-wiki/concepts/application_data]]
- [[004-wiki/concepts/setting_sources]]
- [[004-wiki/concepts/managed_settings]]
- [[004-wiki/concepts/sessions]]
- [[004-wiki/concepts/skills]]
- [[004-wiki/concepts/subagents]]
- [[004-wiki/concepts/hooks]]
- [[004-wiki/concepts/permissions]]
- [[004-wiki/concepts/output_styles]]
- [[004-wiki/concepts/file_checkpointing]]
- [[004-wiki/entities/claude_code]]