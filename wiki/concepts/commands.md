---
title: "Commands"
summary: "Slash commands that control Claude Code from inside a session, providing quick access to model switching, session management, code review, permissions, and workflow automation"
type: concept
sources:
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
  - raw/document/claude code/claude-code-051-context-window-2026-04-29.md
  - raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md
  - raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
  - raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md
  - raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
  - raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md
tags:
  - claude-code
  - commands
  - cli
  - sessions
  - skills
  - context-management
  - voice
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.95
provenance: extracted
---

# Commands

Slash commands control Claude Code from inside a session, providing quick access to model switching, session management, code review, permissions, and workflow automation. Type `/` to see every available command, or `/` followed by letters to filter. ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Key Points

- Two command categories: built-in commands (coded into the CLI) and bundled skills (prompt-based, using the same mechanism as user-written skills) ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Availability varies by platform, plan, and environment; some commands are only visible under specific conditions (e.g., /setup-bedrock requires CLAUDE_CODE_USE_BEDROCK=1, /desktop is macOS/Windows only) ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Required arguments are denoted `<arg>` and optional arguments `[arg]` ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- MCP servers expose prompts as commands in the format `/mcp__<server>__<prompt>`, dynamically discovered from connected servers ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Custom commands are created through [[concepts/skills|skills]] at `.claude/skills/<name>/SKILL.md` ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Details

Built-in commands implement their behavior directly in the CLI codebase. They cover core functionality including session management (/compact, /clear, /resume, /branch), model configuration (/model, /effort, /fast), code review (/review, /ultrareview, /security-review), permissions (/permissions, /sandbox), observability (/context, /diff, /doctor, /usage), and cloud/web integration (/desktop, /teleport, /remote-control, /web-setup). Several commands have aliases: /branch (/fork), /clear (/reset, /new), /config (/settings), /resume (/continue), /remote-control (/rc), /desktop (/app). ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

The `/context` command shows a live breakdown of context usage by category with optimization suggestions, helping identify which components consume the most tokens. ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md] The `/memory` command shows which CLAUDE.md and auto memory files loaded at startup. ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

The `/doctor` command runs an automated health check covering installation, settings validity, MCP server configuration, and context usage; `claude doctor` provides the same check from the shell when the CLI cannot start. ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md] The `/heapdump` command writes a JavaScript heap snapshot and memory breakdown to `~/Desktop` (or the home directory on Linux without a Desktop folder); the breakdown shows resident set size, JS heap, array buffers, and unaccounted native memory. The `.heapsnapshot` file can be opened in Chrome DevTools under Memory → Load to inspect retainers. ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

The `/voice` command toggles voice dictation on or off, with optional mode arguments: `/voice hold` (push-to-talk), `/voice tap` (toggle recording), `/voice off` (disable). The first enable runs a microphone check; on macOS, this triggers the system microphone permission prompt. Voice dictation persists across sessions and can also be configured directly in the user settings `voice` block with `enabled` (boolean), `mode` (`"hold"` or `"tap"`), and `autoSubmit` (boolean, hold mode only). ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

Bundled skills are invoked the same way as built-in commands but execute by passing a prompt to Claude. They include /batch (large-scale change orchestration via git worktrees), /claude-api (API reference and migration), /debug (logging and troubleshooting), /fewer-permission-prompts (allowlist generation), /loop (repeated execution; self-paces when the interval is omitted), and /simplify (code quality review). ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md] ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

The `/effort` command provides an interactive slider for setting the effort level; `xhigh` is the recommended setting for most coding work. ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md] The `/usage` command shows what is driving rate limits. ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md] The `/powerup` command (v2.1.90) provides interactive lessons that teach Claude Code features through animated demos inside the terminal. ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md] ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md] The `/team-onboarding` command packages a user's setup into a replayable guide for onboarding new team members. ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md] Transcript search is accessible by pressing `/` in the session picker, allowing users to search through past session transcripts. ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

The `/autofix-pr` command (Week 15) infers the open PR for the current branch and enables auto-fix on Claude Code on the web in one step. ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md] `/release-notes` is now an interactive version picker. ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md] `/agents` has a tabbed layout with a Running tab showing live subagents (with a `● N running` count) plus Run agent and View running instance actions in the Library tab. ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]

Focus view (press `Ctrl+O` in flicker-free mode) collapses the display to the last prompt, a one-line tool summary with diffstats, and Claude's final response. ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]

Default effort level is now `high` for API-key, Bedrock, Vertex, Foundry, Team, and Enterprise users. ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]

Week 16 (v2.1.105-113) added: `/effort` interactive arrow-key slider when called without arguments; `xhigh` effort level as the new default for Opus 4.7; `/usage` breakdown showing percentage contributions from parallel sessions, subagents, cache misses, and long context, with day (`d`) and week (`w`) toggle; `/recap` for on-demand session recap (configurable via `/config`); `/tui` command and `tui` setting for switching between classic and flicker-free rendering; `/focus` command replacing `Ctrl+O` for focus view; `/undo` as alias for `/rewind`; `/proactive` as alias for `/loop`; `/fewer-permission-prompts` scans transcripts for common read-only Bash and MCP calls and proposes an allowlist; built-in commands (`/init`, `/review`, `/security-review`) discoverable and runnable via the Skill tool ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

Week 17 (v2.1.114-119) merged `/cost` and `/stats` into `/usage`; the old names still work as typing shortcuts that open the relevant tab. ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md] `/config` changes (theme, editor mode, verbose, and similar) now persist to `~/.claude/settings.json` and follow the same project/local/policy precedence as other settings. ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/skills]]
- [[concepts/sessions]]
- [[concepts/context_window]]
- [[concepts/subagents]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/mcp]]
- [[concepts/code_review]]
- [[concepts/auto_fix]]
- [[concepts/cost_tracking]]
- [[concepts/file_checkpointing]]
- [[concepts/plugins]]
- [[entities/claude_code_web]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/github]]
- [[entities/managed_agents]]
- [[concepts/troubleshooting]]
- [[concepts/voice_dictation]]
- [[summaries/claude-code-whats-new-2026-w16]]
- [[summaries/claude-code-whats-new-2026-w17]]