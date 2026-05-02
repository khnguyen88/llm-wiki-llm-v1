---
title: "File Checkpointing"
summary: "A mechanism in the Agent SDK that tracks file modifications through Write/Edit/NotebookEdit tools and enables rewinding files to any previous state using checkpoint UUIDs"
type: concept
sources:
  - raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
tags:
  - claude-code
  - agent-sdk
  - checkpointing
  - file-operations
  - undo
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# File Checkpointing

A mechanism in the Agent SDK that creates backups of files before they are modified through the Write, Edit, and NotebookEdit tools, allowing agents to rewind files to any previous state during or after a session. Each user message in the response stream carries a UUID that serves as a checkpoint identifier. ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]

## Key Points

- Only changes made through Write, Edit, and NotebookEdit are tracked; Bash commands (e.g., `echo >`, `sed -i`) are not captured ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Enabling checkpointing requires setting `enable_file_checkpointing=True` and `extra_args={"replay-user-messages": None}` (Python) or `enableFileCheckpointing: true` and `extraArgs: { 'replay-user-messages': null }` (TypeScript) ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Checkpoint UUIDs are carried by UserMessage objects in the response stream; the first UUID restores all files to their original state ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Rewinding restores files on disk only; conversation history and context remain intact after calling `rewind_files()` / `rewindFiles()` ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Checkpoints are session-scoped: they cannot span sessions, and directory create/move/delete operations are not undone by rewinding ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Every action Claude makes creates a checkpoint automatically; double-tap Escape or run `/rewind` to open the rewind menu ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Rewind can restore conversation only, code only, or both; "Summarize from here" condenses messages from the selected point forward while keeping earlier context intact ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Checkpoints persist across sessions, so you can close your terminal and still rewind later; checkpoints are automatically cleaned up after 30 days (configurable) ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md] ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- Checkpoints only track changes made by Claude's file editing tools, not external processes or Bash commands (e.g., rm, mv, cp); think of checkpoints as "local undo" and Git as "permanent history" ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md] ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- After restoring or summarizing via the rewind menu, the original prompt from the selected message is restored to the input field for re-sending or editing ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- "Summarize from here" compresses messages from the selected point forward into a compact AI-generated summary while keeping earlier context intact; original messages are preserved in the session transcript for reference ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- External file changes outside the current session are not tracked, unless they modify the same files as the current session ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- Pre-edit file snapshots are stored at `~/.claude/file-history/<session>/` and auto-cleaned on startup after `cleanupPeriodDays` (default 30 days) ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- In the VS Code extension, hovering over any message reveals a rewind button with three options: "Fork conversation from here" (new branch, keep code changes), "Rewind code to here" (revert files, keep full conversation), and "Fork conversation and rewind code" (new branch and revert files) ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Details

The checkpoint system tracks three categories of file state: files created during the session (deleted on rewind), files modified during the session (restored to original content on rewind), and the original content of modified files. When a rewind is triggered, created files are deleted and modified files are restored to their content at the checkpoint point. ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]

Two primary patterns exist for using checkpoints. The "checkpoint before risky operations" pattern keeps only the most recent UUID, updating it before each agent turn, and rewinds immediately if something goes wrong during the stream. The "multiple restore points" pattern stores all user message UUIDs in an array with metadata, enabling selective rollback to any intermediate state after the session completes. ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]

Rewinding after a stream completes requires resuming the session with an empty prompt (`query("")`) and then calling `rewind_files()` within the new response stream. Calling `rewindFiles()` after the stream has closed causes a "ProcessTransport is not ready for writing" error. The CLI also supports rewinding via `claude -p --resume <session-id> --rewind-files <checkpoint-uuid>`. ^[raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/agent_loop]]
- [[concepts/custom_tools]]
- [[concepts/cost_tracking]]
- [[summaries/claude-code-best-practices]]
- [[concepts/application_data]]
- [[entities/vs_code_extension]]