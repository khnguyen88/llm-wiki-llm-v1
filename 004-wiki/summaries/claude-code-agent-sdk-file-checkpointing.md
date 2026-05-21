---
title: "Claude Code Agent Sdk File Checkpointing"
summary: "Agent SDK feature that tracks file modifications through Write/Edit/NotebookEdit tools and enables rewinding to any previous state via checkpoint UUIDs in the response stream"
type: summary
sources:
  - raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md
tags:
  - claude-code
  - agent-sdk
  - checkpointing
  - file-operations
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk File Checkpointing

## Key Points

- File checkpointing tracks modifications made through the Write, Edit, and NotebookEdit tools during an agent session, enabling rewind to any previous state ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Changes made through Bash commands (e.g., `echo > file.txt` or `sed -i`) are not captured by the checkpoint system ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Enabling checkpointing requires `enable_file_checkpointing=True` (Python) / `enableFileCheckpointing: true` (TypeScript) plus `extra_args={"replay-user-messages": None}` to receive checkpoint UUIDs in the stream ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Each UserMessage in the response stream carries a UUID that serves as a checkpoint; rewinding to the first one restores all files to their original state ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- File rewinding restores files on disk but does not rewind the conversation itself; history and context remain intact after calling `rewindFiles()` / `rewind_files()` ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- Checkpoints are session-scoped; creating, moving, or deleting directories is not undone by rewinding, and remote/network files are not tracked ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- After the stream completes, rewinding requires resuming the session with an empty prompt (`query("")`) before calling `rewind_files()`; otherwise a "ProcessTransport is not ready for writing" error occurs ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]

## Quotes

- "Only changes made through the Write, Edit, and NotebookEdit tools are tracked. Changes made through Bash commands (like `echo > file.txt` or `sed -i`) are not captured by the checkpoint system." ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]
- "File rewinding restores files on disk to a previous state. It does not rewind the conversation itself." ^[001a-raw/document/claude code/claude-code-006-agent-sdk-file-checkpointing-2026-04-29.md]

## Notes

- The source provides complete code examples in both Python and TypeScript for enabling checkpointing, capturing UUIDs, and rewinding files
- CLI rewind is also available: `claude -p --resume <session-id> --rewind-files <checkpoint-uuid>`
- Two common patterns are documented: checkpoint before risky operations (keeping only the latest UUID) and multiple restore points (storing all UUIDs in an array)
- The `permission_mode="acceptEdits"` setting is used in checkpointing examples to auto-approve file edits without prompting

## Related

- [[004-wiki/entities/agent-sdk]]
- [[004-wiki/entities/claude-code]]
- [[004-wiki/concepts/file-checkpointing]]
- [[004-wiki/concepts/agent-loop]]
- [[004-wiki/concepts/custom-tools]]