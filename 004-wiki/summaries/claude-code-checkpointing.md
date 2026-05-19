---
title: "Claude Code Checkpointing"
summary: "Claude Code automatically tracks file edits per user prompt, enabling rewind to prior code/conversation states and targeted context summarization via the Esc+Esc or /rewind menu"
type: summary
sources:
  - raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md
tags:
  - claude-code
  - checkpointing
  - undo
  - session-management
  - context-window
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Checkpointing

## Key Points

- Every user prompt creates a new checkpoint; checkpoints persist across sessions and are automatically cleaned up after 30 days (configurable) ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- The rewind menu (Esc+Esc or `/rewind`) displays a scrollable list of session prompts and offers five actions: Restore code and conversation, Restore conversation, Restore code, Summarize from here, and Never mind ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- "Restore code and conversation" reverts both files and conversation to the selected point; "Restore conversation" rewinds conversation while keeping current code; "Restore code" reverts files while keeping conversation ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- "Summarize from here" compresses messages from the selected point forward into an AI-generated summary, keeping earlier context intact and preserving original messages in the session transcript for reference ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- After restoring or summarizing, the original prompt is restored to the input field for re-sending or editing ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- Summarize is similar to `/compact` but targeted: it compresses only the latter portion of conversation rather than the whole history ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- Checkpoints only track changes made by Claude's file editing tools; Bash commands (rm, mv, cp) and external file modifications are not tracked ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]

## Quotes

- "Think of checkpoints as 'local undo' and Git as 'permanent history'" ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]

## Notes

- Common use cases: exploring alternative implementations, recovering from mistakes, iterating on feature variations, freeing context window space by summarizing verbose debugging sessions ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- External changes to files outside the current session are not tracked, unless they happen to modify the same files that the current session is editing ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- For branching off while preserving the original session intact (instead of summarizing), use fork: `claude --continue --fork-session` ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]

## Related

- [[concepts/file_checkpointing]]
- [[concepts/sessions]]
- [[concepts/context_window]]
- [[entities/claude_code]]