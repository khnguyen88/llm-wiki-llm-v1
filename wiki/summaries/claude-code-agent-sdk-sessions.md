---
title: "Claude Code Agent SDK Sessions"
summary: "How the Agent SDK persists conversation history via sessions, and the continue, resume, and fork operations for returning to prior runs"
type: summary
sources:
  - raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md
tags:
  - agent-sdk
  - sessions
  - context-persistence
  - python
  - typescript
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent SDK Sessions

## Key Points

- A session is the conversation history the SDK accumulates while an agent works — prompts, tool calls, tool results, and responses — written to disk automatically ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- Sessions persist the conversation, not the filesystem; use file checkpointing to snapshot and revert file changes ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- **Continue** resumes the most recent session in the current directory (no ID tracking); **Resume** takes a specific session ID (required for multi-user apps or returning to non-recent sessions) ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- **Fork** creates a new session starting with a copy of the original's history; the original stays unchanged ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- Python's `ClaudeSDKClient` and TypeScript's `continue: true` provide automatic session management without manual ID handling ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- Session IDs are captured from the `session_id` field on `ResultMessage` (both SDKs) or the `SystemMessage` init event (TypeScript direct field, Python nested in `data`) ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- Session files are stored under `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` where `<encoded-cwd>` replaces non-alphanumeric characters with `-` ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]

## Quotes

- "Sessions persist the **conversation**, not the filesystem." ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- "Forking branches the conversation history, not the filesystem. If a forked agent edits files, those changes are real and visible to any session working in the same directory." ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]

## Notes

- For cross-host resume, two options exist: move the session `.jsonl` file to the same path on the new host (cwd must match), or capture needed results as application state and pass them into a fresh session prompt — the latter is often more robust ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- TypeScript supports `persistSession: false` for in-memory-only sessions; Python always persists to disk ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]
- Both SDKs expose session utility functions: `listSessions`/`list_sessions`, `getSessionMessages`/`get_session_messages`, `getSessionInfo`/`get_session_info`, `renameSession`/`rename_session`, `tagSession`/`tag_session` ^[raw/document/claude code/claude-code-019-agent-sdk-sessions-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/sessions]]
- [[concepts/agent_loop]]
- [[concepts/file_checkpointing]]