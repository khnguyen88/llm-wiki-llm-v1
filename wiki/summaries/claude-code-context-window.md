---
title: "Claude Code Context Window"
summary: "Details what loads into the context window, how compaction preserves or discards each mechanism, and how to inspect context usage"
type: summary
sources:
  - raw/document/claude code/claude-code-051-context-window-2026-04-29.md
tags:
  - context-window
  - compaction
  - claude-code
  - token-management
  - skills
  - hooks
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Context Window

## Key Points

- Before any user input, the context window is pre-filled with CLAUDE.md, auto memory, MCP tool names, skill descriptions, output style, and `--append-system-prompt` text — all entering the system prompt the same way ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- As work proceeds, each file read adds tokens to context, path-scoped rules load automatically alongside matching files, and PostToolUse hooks fire after each edit ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Subagents handle research in separate context windows; only the summary and a small metadata trailer return to the parent session ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Compaction (`/compact`) replaces conversation history with a structured summary; system prompt, project-root CLAUDE.md, and auto memory are re-injected from disk, but path-scoped rules and nested CLAUDE.md files are lost until their trigger files are read again ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Invoked skill bodies are re-injected after compaction, capped at 5,000 tokens per skill and 25,000 tokens total; the oldest invoked skills are dropped first when the total budget is exceeded, and truncation preserves the start of each file ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Hooks are unaffected by compaction because they execute as code outside the context window, not as context content ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Rules that must persist across compaction should drop the `paths:` frontmatter or be moved to the project-root CLAUDE.md ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

## Quotes

- "Path-scoped rules and nested CLAUDE.md files load into message history when their trigger file is read, so compaction summarizes them away with everything else." ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- "Truncation keeps the start of the file, so put the most important instructions near the top of SKILL.md." ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

## Notes

- Run `/context` for a live breakdown of context usage by category with optimization suggestions ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Run `/memory` to check which CLAUDE.md and auto memory files loaded at startup ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/context_window]]
- [[concepts/compaction]]
- [[concepts/skills]]
- [[concepts/hooks]]
- [[concepts/subagents]]
- [[concepts/system_prompt]]
- [[concepts/output_styles]]
- [[concepts/prompt_caching]]