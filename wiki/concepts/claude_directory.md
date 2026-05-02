---
title: "Claude Directory"
summary: "The .claude directory structure where Claude Code reads configuration files including CLAUDE.md, settings.json, hooks, skills, subagents, rules, and auto memory"
type: concept
sources:
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
  - raw/document/claude code/claude-code-046-code-review-2026-04-29.md
tags:
  - claude-code
  - configuration
  - directory-structure
  - settings
  - scopes
  - code-review
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Directory

The `.claude` directory is where Claude Code reads project-level configuration, and `~/.claude` holds global configuration that applies across all projects. Project files should be committed to git for team sharing; global files are personal. On Windows, `~/.claude` resolves to `%USERPROFILE%\.claude`. If `CLAUDE_CONFIG_DIR` is set, every `~/.claude` path lives under that directory instead. ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Key Points

- Project-scope files live under `.claude/` (or at the project root for `CLAUDE.md`, `.mcp.json`, `.worktreeinclude`); global-scope files live under `~/.claude/` and apply across all projects ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Most users only need to edit `CLAUDE.md` and `settings.json`; the rest of the directory structure is optional and added as needed ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE.md` provides project context and conventions; loaded every session at project or global scope ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE.local.md` (project root, gitignored) holds private developer preferences alongside `CLAUDE.md` ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `settings.json` holds permissions, hooks, environment variables, and model defaults at project or global scope ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `settings.local.json` (project only, auto-gitignored) holds personal overrides that should not be committed ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Settings precedence from highest to lowest: managed settings, CLI flags, environment variables, then `settings.json` ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- REVIEW.md at the repository root is a review-only instruction file injected directly into every Code Review agent as highest priority; `@` import syntax is not expanded in REVIEW.md, so rules must be written directly in the file ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- In Code Review, CLAUDE.md violations newly introduced by a PR are flagged as nit-level findings; bidirectionally, if a PR changes code in a way that makes a CLAUDE.md statement outdated, Claude flags that the docs need updating ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

## Details

### File Reference

Each file in the `.claude` directory has a defined scope and commit behavior:

| File | Scope | Commit | Purpose |
|------|-------|--------|---------|
| `CLAUDE.md` | Project and global | Yes | Instructions loaded every session |
| `rules/*.md` | Project and global | Yes | Topic-scoped instructions, optionally path-gated |
| `settings.json` | Project and global | Yes | Permissions, hooks, env vars, model defaults |
| `settings.local.json` | Project only | No | Personal overrides, auto-gitignored |
| `.mcp.json` | Project only | Yes | Team-shared MCP servers |
| `.worktreeinclude` | Project only | Yes | Gitignored files to copy into worktrees |
| `skills/<name>/SKILL.md` | Project and global | Yes | Reusable prompts invoked with `/name` or auto-invoked |
| `commands/*.md` | Project and global | Yes | Single-file prompts; same mechanism as skills |
| `output-styles/*.md` | Project and global | Yes | Custom system-prompt sections |
| `agents/*.md` | Project and global | Yes | Subagent definitions with own prompt and tools |
| `agent-memory/<name>/` | Project and global | Yes | Persistent memory for subagents |
| `REVIEW.md` | Project only | Yes | Review-only instructions, highest priority in Code Review agents |
| `~/.claude.json` | Global only | No | App state, OAuth, UI toggles, personal MCP servers |
| `projects/<project>/memory/` | Global only | No | Auto memory: Claude's notes across sessions |
| `keybindings.json` | Global only | No | Custom keyboard shortcuts |
| `themes/*.json` | Global only | No | Custom color themes |

^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

### Files Not in the Explorer

Several related files live outside the directory explorer: `managed-settings.json` at system level (enterprise-enforced, cannot be overridden), `CLAUDE.local.md` at project root (private preferences, gitignored), and installed plugins under `~/.claude/plugins` (managed by `claude plugin` commands, with orphaned versions deleted after 7 days). ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

### Choosing the Right File

Different customization types belong in different files: project context and conventions go in `CLAUDE.md`; tool call allow/block rules go in `settings.json` permissions or hooks; pre/post-tool scripts go in `settings.json` hooks; session environment variables go in `settings.json` env; personal overrides not for git go in `settings.local.json`; reusable slash-command prompts go in `skills/<name>/SKILL.md`; specialized subagents go in `agents/*.md`; external tools over MCP go in `.mcp.json`; and response formatting goes in `output-styles/*.md`. ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Related

- [[concepts/application_data]]
- [[concepts/setting_sources]]
- [[concepts/managed_settings]]
- [[concepts/skills]]
- [[concepts/subagents]]
- [[concepts/hooks]]
- [[concepts/permissions]]
- [[concepts/output_styles]]
- [[concepts/file_checkpointing]]
- [[concepts/code_review]]
- [[entities/claude_code]]