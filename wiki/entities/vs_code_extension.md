---
title: "VS Code Extension"
summary: "Official VS Code extension providing a native graphical interface for Claude Code with inline diff review, @-mentions, plan review, checkpoints, plugin management, and a built-in IDE MCP server"
type: entity
sources:
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
tags:
  - claude-code
  - vs-code
  - ide
  - extension
  - microsoft
  - editor
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# VS Code Extension

The official Visual Studio Code extension for Claude Code, providing a native graphical interface integrated directly into the IDE. The extension is the recommended way to use Claude Code in VS Code and includes the CLI for access from the integrated terminal. ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Key Facts

- Requires VS Code 1.98.0 or higher; also available for Cursor ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Installed via the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`) searching for "Claude Code", or directly from the VS Code Marketplace ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Spark icon in the Editor Toolbar (top-right, requires a file open), Activity Bar (left sidebar), and Status Bar (bottom-right, works without a file open) all open the Claude Code panel ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Authentication requires an Anthropic account; if `ANTHROPIC_API_KEY` is set but VS Code doesn't inherit it, launch VS Code from a terminal with `code .` or sign in with a Claude account instead ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The prompt box supports permission modes (default, plan, auto-accept), a `/` command menu, context indicator, extended thinking toggle, and multi-line input with `Shift+Enter` ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- @-mentions reference files (`@auth` fuzzy matches), folders (trailing slash), and terminal output (`@terminal:name`); `Option+K`/`Alt+K` inserts an @-mention with file path and line range for the current selection ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The panel can be dragged to the secondary sidebar, primary sidebar, or editor area; Claude remembers the preferred location ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Multiple conversations can run simultaneously in separate tabs or windows; a colored dot on the spark icon indicates status (blue = permission pending, orange = finished while hidden) ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Session history supports searching by keyword and browsing by time (Today, Yesterday, Last 7 days, etc.); remote sessions from Claude Code on the Web appear in a separate Remote tab ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Resuming remote sessions requires signing in with Claude.ai Subscription (not Anthropic Console); only web sessions started with a GitHub repository appear in the Remote tab ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Plugin management via `/plugins` opens a graphical dialog with installed/available tabs, search filtering, and three installation scopes (user, project, local) ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Plugin marketplaces can be added via GitHub repo, URL, or local path; changes prompt a restart ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- `@browser` references the Chrome extension for browser automation; requires Chrome extension v1.0.36+ ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Registers a URI handler at `vscode://anthropic.claude-code/open` with optional `prompt` (URL-encoded, pre-filled but not submitted) and `session` (resume by ID) parameters ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Terminal mode replaces the graphical panel with the CLI interface; toggled via the `useTerminal` setting or `Cmd+,` / `Ctrl+,` → Extensions → Claude Code ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- `Cmd+Esc` / `Ctrl+Esc` toggles focus between editor and Claude; `Cmd+Shift+Esc` / `Ctrl+Shift+Esc` opens a new conversation tab ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- `Option+K` / `Alt+K` inserts an @-mention reference for the current file and selection ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The extension and CLI share conversation history; `claude --resume` in the terminal opens an interactive picker to continue an extension conversation ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- CLI-only features not available in the extension: all commands/skills, MCP server configuration, `!` bash shortcut, and tab completion ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Checkpoints in the extension offer three rewind options when hovering over a message: fork conversation, rewind code to that point, or both ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- `@terminal:name` references terminal output by the terminal's title ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Background process visibility is limited in the extension compared to the CLI; for better visibility, have Claude output the command to run it manually in the integrated terminal ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- MCP servers are added via `claude mcp add` in the integrated terminal and managed with `/mcp` in the chat panel ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Security note: with auto-edit permissions enabled, Claude can modify VS Code configuration files (settings.json, tasks.json) that VS Code may execute automatically; use manual approval mode or VS Code Restricted Mode for untrusted workspaces ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Extension Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `useTerminal` | `false` | Launch Claude in terminal mode instead of graphical panel |
| `initialPermissionMode` | `default` | Controls approval prompts: `default`, `plan`, `acceptEdits`, or `bypassPermissions` |
| `preferredLocation` | `panel` | Where Claude opens: `sidebar` or `panel` |
| `autosave` | `true` | Auto-save files before Claude reads or writes them |
| `useCtrlEnterToSend` | `false` | Use Ctrl/Cmd+Enter instead of Enter to send prompts |
| `enableNewConversationShortcut` | `false` | Enable Cmd/Ctrl+N to start a new conversation |
| `hideOnboarding` | `false` | Hide the onboarding checklist |
| `respectGitIgnore` | `true` | Exclude .gitignore patterns from file searches |
| `usePythonEnvironment` | `true` | Activate workspace Python environment (requires Python extension) |
| `environmentVariables` | `[]` | Set environment variables for the Claude process |
| `disableLoginPrompt` | `false` | Skip authentication prompts (for third-party provider setups) |
| `allowDangerouslySkipPermissions` | `false` | Adds Auto mode and Bypass permissions to the mode selector |
| `claudeProcessWrapper` | - | Executable path used to launch the Claude process |

^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Third-Party Providers

To use Amazon Bedrock, Google Vertex AI, or Microsoft Foundry instead of the direct Anthropic API: (1) enable `disableLoginPrompt` in VS Code settings, (2) configure the provider in `~/.claude/settings.json`. Settings in `settings.json` are shared between the extension and CLI. ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Troubleshooting

- **Extension won't install**: ensure VS Code 1.98.0+, check extension permissions, try the VS Code Marketplace directly
- **Spark icon not visible**: open a file (icon only appears with a file open), check VS Code version, restart with "Developer: Reload Window", disable conflicting AI extensions (Cline, Continue), check workspace trust (extension doesn't work in Restricted Mode); alternatively click "Claude Code" in the Status Bar or use the Command Palette
- **Claude never responds**: check internet connection, start a new conversation, try the CLI for detailed error messages, file an issue on GitHub
- Uninstall removes the extension; to also remove all data: `rm -rf ~/.vscode/globalStorage/anthropic.claude-code`

^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Related

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
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[concepts/authentication]]