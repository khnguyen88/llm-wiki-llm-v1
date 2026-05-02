---
title: "Sessions"
summary: "Context persistence mechanism in the Agent SDK that maintains conversation history and agent state across multiple exchanges, enabling continue, resume, and fork operations"
type: concept
sources:
  - raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md
  - raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
  - raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-104-slack-2026-04-29.md
  - raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
  - raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
tags:
  - agent-sdk
  - sessions
  - state
  - context
  - cloud
  - cli
  - slack
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Sessions

Sessions maintain context across multiple exchanges in the Agent SDK. Claude remembers files read, analysis done, and conversation history. Sessions can be resumed later to continue with full context, or forked to explore different approaches. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

## Key Points

- Sessions preserve context across multiple exchanges, including files read, analysis performed, and conversation history ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]
- Sessions persist the **conversation**, not the filesystem; to snapshot and revert file changes, use file checkpointing ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- The session_id is available from the `session_id` field on `ResultMessage` (both SDKs) and from the SystemMessage init event (TypeScript: direct field; Python: nested in `data`) ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md] ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- **Continue** resumes the most recent session in the current directory with no ID tracking; **Resume** takes a specific session ID and is required for multi-user apps or returning to non-recent sessions ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- **Fork** creates a new session starting with a copy of the original's history; the fork gets its own session ID and the original stays unchanged ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- Python's `ClaudeSDKClient` handles session IDs automatically across calls; TypeScript uses `continue: true` on each subsequent `query()` call for the same effect ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- Session files are stored at `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` where `<encoded-cwd>` replaces non-alphanumeric characters with `-` ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- TypeScript supports `persistSession: false` for in-memory-only sessions; Python always persists to disk ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- `claude --continue` resumes the most recent conversation; `claude --resume` selects from recent sessions by name or ID ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Use `/rename` to give sessions descriptive names like "oauth-migration" or "debugging-memory-leak" for easy later retrieval ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Treat sessions like branches: different workstreams can have separate, persistent contexts ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- "Summarize from here" in the rewind menu compresses messages from a selected point forward into an AI-generated summary, freeing context window space while keeping earlier context intact; for preserving the original session intact while branching, use fork (`claude --continue --fork-session`) ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- Cloud sessions appear in the sidebar at claude.ai/code and support sharing (Team visibility for Enterprise/Team, Public for Max/Pro), archiving, and permanent deletion ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Cloud sessions support `/compact` and `/context` commands but not `/clear` (start a new session instead); auto-compaction runs at ~95% context capacity by default, adjustable via `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` environment variable ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Cloud sessions expose their ID via `CLAUDE_CODE_REMOTE_SESSION_ID` for linking artifacts (PR bodies, commit messages) back to the session transcript URL ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Session transcripts are stored at `~/.claude/projects/<project>/<session>.jsonl` containing every message, tool call, and tool result; large tool outputs spill to `~/.claude/projects/<project>/<session>/tool-results/` ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Session transcripts are auto-cleaned on startup after `cleanupPeriodDays` (default 30 days); transcripts are plaintext and not encrypted at rest ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE_CODE_SKIP_PROMPT_HISTORY` disables transcript and prompt history writing; `--no-session-persistence` (non-interactive) or `persistSession: false` (Agent SDK) also disables session persistence ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- CLI session management: `--continue` / `-c` resumes the most recent conversation in the current directory (includes sessions that added the directory via `/add-dir`); `--resume` / `-r` resumes by session ID or name, or shows an interactive picker; `--fork-session` creates a new session ID when resuming instead of reusing the original ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--name` / `-n` sets a display name for the session shown in `/resume` and the terminal title; sessions can be resumed by name with `--resume`; `/rename` changes the name mid-session ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--session-id` uses a specific UUID as the session ID; `--from-pr` resumes sessions linked to a specific pull request (accepts PR number, GitHub/GitLab/Bitbucket URL) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- When resuming an old, large session, `--resume`, `--continue`, and `/resume` offer to resume from a summary instead of loading the full transcript (not available on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- The `/resume` picker shows interactive sessions from the current worktree by default, with shortcuts: Ctrl+A widens to all projects, Ctrl+W widens to all worktrees of the current repo, Ctrl+B filters to the current git branch, Space previews session content, Ctrl+R renames, and `/` or any printable character enters search mode ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Pasting a GitHub, GitHub Enterprise, GitLab, or Bitbucket PR/MR URL into the picker search field finds the session that created that PR ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Selecting a session from another worktree of the same repository resumes it directly; selecting from an unrelated project copies a `cd` and resume command to clipboard ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Name sessions early with `/rename` for distinct tasks (e.g., "payment-integration") to make later retrieval easier ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Forked sessions (from `/branch`, `/rewind`, or `--fork-session`) are grouped under their root session in the picker ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Resuming by name resolves across the current repository and its worktrees; `claude --resume <name>` opens the picker with the name pre-filled on ambiguity, while `/resume <name>` from inside a session reports an error ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Sessions created by `claude -p` or SDK invocations do not appear in the picker but can be resumed by passing their session ID directly to `claude --resume <session-id>` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Slack-initiated sessions follow a distinct flow: @mention → intent detection → session creation on claude.ai/code → progress updates in Slack thread → completion summary with action buttons (View Session, Create PR, Change Repo) ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- If Claude Code becomes unresponsive and the terminal is closed, conversation history is not lost; `claude --resume` in the same directory picks up the session where it left off ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- In the VS Code extension, session history is accessed via the Session history button at the top of the panel, with search by keyword and browsing by time (Today, Yesterday, Last 7 days, etc.); hovering reveals rename and remove actions ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Remote sessions from Claude Code on the Web can be resumed locally in VS Code via the Session history Remote tab; requires signing in with Claude.ai Subscription (not Anthropic Console); only web sessions started with a GitHub repository appear, and changes are not synced back to claude.ai ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The VS Code extension and CLI share the same conversation history; continue an extension conversation in the CLI with `claude --resume` ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Web session lifecycle: (1) clone and prepare — repository is cloned to an Anthropic-managed VM and setup script runs if configured; (2) configure network — internet access is set based on the environment's access level; (3) work — Claude analyzes, makes changes, runs tests, checks work; (4) push branch — Claude pushes its branch to GitHub for review; the session stays live after the push so PR creation and further edits happen within the same conversation ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Web sessions persist across devices (laptop, phone); closing the browser tab does not stop the session — it continues running in the background until the task finishes, then idles ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Web sessions can be pre-filled via URL parameters (`prompt`, `prompt_url`, `repositories`, `environment`) to enable integrations like issue-tracker buttons that open Claude Code with context pre-loaded ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Session recap (introduced in Week 17, v2.1.114-119) shows what happened in a session while the terminal was unfocused, allowing users to quickly catch up without scrolling the full transcript ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

## Details

Without sessions, each `query()` call starts with no prior context. With session resumption, the agent retains the full conversation history and all state from previous interactions. The session_id is captured from the SystemMessage init event and passed to subsequent `query()` calls via the `resume` option. Forking creates a new branch from an existing session, allowing exploration of different approaches without losing the original context. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md]

Continue and resume both pick up an existing session and add to it, but differ in how they find that session. Continue finds the most recent session in the current directory — no ID tracking needed. Resume takes a specific session ID, which is required when multiple sessions exist (e.g., one per user) or when returning to a session that is not the most recent. Resume is useful for follow-ups on completed tasks, recovering from `error_max_turns` or `error_max_budget_usd` limits, and restoring conversations after a process restart. ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]

Forking branches the conversation history, not the filesystem. If a forked agent edits files, those changes are real and visible to any session working in the same directory. The fork receives its own session ID distinct from the original. To resume a session across machines, either move the `.jsonl` session file to the same path on the new host (the `cwd` must match) or capture results as application state and pass them into a fresh session prompt. A `SessionStore` adapter enables shared storage for serverless or CI environments. ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]

Both SDKs expose session utility functions for building custom session pickers, cleanup logic, or transcript viewers: `list_sessions`/`listSessions`, `get_session_messages`/`getSessionMessages`, `get_session_info`/`getSessionInfo`, `rename_session`/`renameSession`, and `tag_session`/`tagSession`. ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/context_window]]
- [[concepts/file_checkpointing]]
- [[concepts/parallel_sessions]]
- [[entities/claude_code_web]]
- [[concepts/cloud_environment]]
- [[concepts/teleport]]
- [[summaries/claude-code-best-practices]]
- [[concepts/application_data]]
- [[concepts/worktrees]]
- [[summaries/claude-code-common-workflows]]
- [[summaries/claude-code-cli-reference]]
- [[entities/slack]]
- [[concepts/routing_mode]]
- [[concepts/troubleshooting]]
- [[entities/vs_code_extension]]
- [[concepts/session_prefill]]
- [[concepts/session_recap]]
- [[summaries/claude-code-web-quickstart]]