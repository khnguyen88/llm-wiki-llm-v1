---
title: "Fan-Out"
summary: "A pattern for distributing work across many parallel Claude invocations by generating a task list, writing a script loop, and refining the prompt before scaling"
type: concept
sources:
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
tags:
  - claude-code
  - automation
  - scaling
  - batch
  - migration
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Fan-Out

A pattern for distributing large-scale work across many parallel Claude invocations. Generate a task list, write a script to loop through it calling `claude -p` for each item, refine the prompt on the first few files, then run at scale. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Key Points

- Three-step process: (1) generate a task list of files to process, (2) write a script that loops through the list calling `claude -p` for each, (3) test on a few files, refine the prompt, then run on the full set ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Use `--allowedTools` to restrict what Claude can do during unattended batch operations ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Can be integrated into existing data and processing pipelines by piping `claude -p` output into other commands ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Refine the prompt based on what goes wrong with the first 2-3 files before running the full set ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Details

The fan-out pattern is useful for large migrations, bulk analysis, or any task that can be decomposed into independent units of work. The key insight is to validate the prompt on a small sample before committing to the full run, since a bad prompt applied to thousands of files wastes both time and tokens. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

The `--allowedTools` flag is critical for safety: it restricts Claude's capabilities to only the tools specified, preventing unintended side effects during batch operations. For example, a migration script might allow only `Edit` and `Bash(git commit *)` to prevent Claude from making broader changes. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/non_interactive_mode]]
- [[concepts/parallel_sessions]]
- [[concepts/permissions]]