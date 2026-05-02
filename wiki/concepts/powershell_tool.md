---
title: "PowerShell Tool"
summary: "Native PowerShell command execution tool in Claude Code that runs commands in PowerShell instead of routing through Git Bash on Windows, with progressive rollout and opt-in availability on other platforms"
type: concept
sources:
  - raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md
tags:
  - claude-code
  - powershell
  - windows
  - shell
  - tools
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# PowerShell Tool

A built-in tool that executes PowerShell commands natively, providing native Windows command execution instead of routing through Git Bash. On Windows, this means commands run in PowerShell directly. On Linux, macOS, and WSL, the tool is opt-in and requires PowerShell 7+. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Key Points

- On Windows without Git Bash, the tool is enabled automatically; on Windows with Git Bash, it is rolling out progressively; on Linux, macOS, and WSL, set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` to opt in ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- On Windows, Claude Code auto-detects `pwsh.exe` (PowerShell 7+) with fallback to `powershell.exe` (PowerShell 5.1); on Linux/macOS/WSL, PowerShell 7+ must be installed and on PATH ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- Three settings control PowerShell usage: `"defaultShell": "powershell"` in settings.json for interactive commands, `"shell": "powershell"` on individual command hooks, and `shell: powershell` in skill frontmatter for `!`command`` blocks ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The same working-directory reset behavior as Bash applies, including `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` to disable directory carry-over ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- Preview limitations: PowerShell profiles are not loaded, and sandboxing is not supported on Windows ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- On Windows, set `CLAUDE_CODE_USE_POWERSHELL_TOOL=0` to opt out of the progressive rollout ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Details

The PowerShell tool addresses the need for native Windows command execution in Claude Code. Before this tool, all shell commands on Windows were routed through Git Bash, which could cause issues with Windows-specific commands, paths, and PowerShell-specific syntax. The tool uses PowerShell 5.1 syntax by default (Windows PowerShell 5.1 edition), with specific behavioral differences documented for pipeline chaining, null-coalescing, and other operators that differ from Bash.

Shell selection for PowerShell extends beyond the tool itself. Three independent settings control where PowerShell is used: `defaultShell` in settings.json routes interactive `!` commands through PowerShell when the tool is enabled; `shell` on individual command hooks runs that hook in PowerShell regardless of the tool being enabled (hooks spawn PowerShell directly); and `shell: powershell` in skill frontmatter runs `!`command`` blocks in PowerShell, also requiring the tool to be enabled. These settings allow granular control over when PowerShell is used across different execution contexts. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/skills]]
- [[concepts/terminal_config]]
- [[summaries/claude-code-tools-reference]]