---
title: "Application Data"
summary: "Data that Claude Code writes during sessions, including transcripts, tool results, file snapshots, caches, and logs, with automatic cleanup policies and plaintext storage considerations"
type: concept
sources:
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
tags:
  - claude-code
  - data-storage
  - cleanup
  - security
  - transcripts
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Application Data

Beyond configuration files, `~/.claude` holds data that Claude Code writes during sessions. These files are plaintext — anything that passes through a tool lands on disk, including file contents, command output, and pasted text. ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Key Points

- Session transcripts are stored at `projects/<project>/<session>.jsonl` and contain every message, tool call, and tool result ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Large tool outputs that exceed inline limits are spilled to `projects/<project>/<session>/tool-results/` ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Pre-edit file snapshots are stored in `file-history/<session>/` for checkpoint restore ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Auto-cleaned paths are deleted on startup once older than `cleanupPeriodDays` (default 30 days) ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Transcripts and history are not encrypted at rest; OS file permissions are the only protection ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE_CODE_SKIP_PROMPT_HISTORY` disables transcript and prompt history writing; `--no-session-persistence` (non-interactive) or `persistSession: false` (Agent SDK) achieve the same effect ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Details

### Auto-Cleaned Paths

The following paths under `~/.claude/` are automatically deleted on startup once they exceed `cleanupPeriodDays` (default 30):

| Path | Contents |
|------|----------|
| `projects/<project>/<session>.jsonl` | Full conversation transcript |
| `projects/<project>/<session>/tool-results/` | Large tool outputs spilled to separate files |
| `file-history/<session>/` | Pre-edit snapshots for checkpoint restore |
| `plans/` | Plan files from plan mode |
| `debug/` | Per-session debug logs (only written with `--debug` or `/debug`) |
| `paste-cache/`, `image-cache/` | Contents of large pastes and attached images |
| `session-env/` | Per-session environment metadata |
| `tasks/` | Per-session task lists written by task tools |
| `shell-snapshots/` | Captured shell environment for Bash tool (removed on clean exit) |
| `backups/` | Timestamped copies of `~/.claude.json` before config migrations |

^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

### Persisted Paths

The following paths are not covered by automatic cleanup and persist indefinitely until manually deleted:

| Path | Contents |
|------|----------|
| `history.jsonl` | Every prompt typed, with timestamp and project path; used for up-arrow recall |
| `stats-cache.json` | Aggregated token and cost counts shown by `/usage` |
| `todos/` | Legacy per-session task lists; no longer written by current versions |

^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

### Plaintext Storage and Security

Transcripts and history are stored as plaintext without encryption. If a tool reads a `.env` file or a command prints a credential, that value is written to `projects/<project>/<session>.jsonl`. To reduce exposure: lower `cleanupPeriodDays` to shorten transcript retention; set `CLAUDE_CODE_SKIP_PROMPT_HISTORY` to skip writing transcripts and prompt history; or use permission rules to deny reads of credential files. ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

### Clearing Local Data

Deleting any application-data path is safe for future sessions. The impact on past sessions varies: deleting `~/.claude/projects/` loses resume, continue, and rewind for past sessions; deleting `history.jsonl` loses up-arrow prompt recall; deleting `file-history/` loses checkpoint restore for past sessions; deleting `stats-cache.json` loses historical totals shown by `/usage`. The `debug/`, `plans/`, `paste-cache/`, `image-cache/`, `session-env/`, `tasks/`, `shell-snapshots/`, and `backups/` directories hold nothing user-facing. Do not delete `~/.claude.json`, `~/.claude/settings.json`, or `~/.claude/plugins/` — those hold auth, preferences, and installed plugins. ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Related

- [[concepts/claude_directory]]
- [[concepts/sessions]]
- [[concepts/file_checkpointing]]
- [[concepts/permissions]]
- [[entities/claude_code]]