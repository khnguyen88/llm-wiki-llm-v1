---
title: "Claude Code VS Code"
summary: "VS Code extension providing a native graphical interface for Claude Code with inline diffs, @-mentions, plan review, checkpoints, plugin management, and built-in IDE MCP server"
type: summary
sources:
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
tags:
  - claude-code
  - vs-code
  - ide
  - extension
  - mcp
  - checkpoints
  - plugins
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code VS Code

## Key Points

- The VS Code extension provides a native graphical interface for Claude Code, including inline diff review, @-mentions with line ranges, plan review, conversation history, and multiple tabs ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Requires VS Code 1.98.0+ and an Anthropic account; includes the CLI which is accessible from the integrated terminal ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The prompt box supports permission modes, a command menu (`/`), context indicator, extended thinking toggle, and multi-line input (`Shift+Enter`) ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- @-mentions reference files and folders with fuzzy matching; `Option+K`/`Alt+K` inserts an @-mention with the current selection's file path and line numbers ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The extension runs a built-in IDE MCP server that exposes `mcp__ide__getDiagnostics` and `mcp__ide__executeCode` tools; the server binds to `127.0.0.1` with per-activation random auth tokens ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Checkpoints in the extension offer three rewind options: fork conversation, rewind code, or fork conversation and rewind code ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Remote sessions from Claude Code on the Web can be resumed locally in VS Code via the Session history Remote tab; only web sessions started with a GitHub repository appear ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Quotes

- "The VS Code extension provides a native graphical interface for Claude Code, integrated directly into your IDE." ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md:1]
- "When Claude wants to edit a file, it shows a side-by-side comparison of the original and proposed changes, then asks for permission." ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md:1]
- "Jupyter execution always asks first. mcp__ide__executeCode can't run anything silently." ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md:1]

## Notes

- The extension registers a URI handler at `vscode://anthropic.claude-code/open` with optional `prompt` and `session` query parameters for integration with external tooling
- Plugin management in the extension uses the same CLI commands under the hood; configurations are shared between extension and CLI
- The CLI offers features not available in the extension: all commands/skills, MCP server config, `!` bash shortcut, and tab completion

## Related

- [[entities/vs_code_extension]]
- [[entities/claude_code]]
- [[concepts/ide_mcp_server]]
- [[concepts/file_checkpointing]]
- [[concepts/plugins]]
- [[concepts/mcp]]
- [[concepts/sessions]]
- [[concepts/permissions]]
- [[concepts/worktrees]]
- [[entities/chrome_extension]]
- [[concepts/browser_automation]]