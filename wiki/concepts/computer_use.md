---
title: "Computer Use"
summary: "A research preview feature that lets Claude Code control the user's screen on macOS — opening apps, clicking, typing, and taking screenshots — for GUI-only tasks that other tools cannot reach"
type: concept
sources:
  - raw/document/claude code/claude-code-050-computer-use-2026-04-29.md
tags:
  - claude-code
  - computer-use
  - gui
  - macos
  - mcp
  - permissions
  - accessibility
  - screen-control
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Computer Use

A feature that lets Claude Code control the user's screen on macOS by opening applications, clicking UI elements, typing, and taking screenshots. Computer use is the broadest and slowest interaction method; Claude tries more precise tools (MCP, Bash, Chrome) first and falls back to computer use only when nothing else can reach the target. ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

## Key Points

- Available as a built-in MCP server called `computer-use`, disabled by default and enabled per project via the `/mcp` menu ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Requires macOS, a Pro or Max plan, Claude Code v2.1.85+, and an interactive session; not available on Linux/Windows CLI, Team/Enterprise plans, or third-party providers (Bedrock, Vertex AI, Foundry) ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Needs two macOS permissions: Accessibility (click, type, scroll) and Screen Recording (see the screen) ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Per-session app approval with sentinel warnings for high-access apps: terminals and IDEs warn "equivalent to shell access," Finder warns "can read or write any file," System Settings warns "can change system settings" ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Holds a machine-wide lock so only one session can control the screen at a time; other visible apps are hidden while Claude works ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Press `Esc` anywhere to abort immediately; the key press is consumed so prompt injection cannot use it to dismiss dialogs ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Screenshots are downscaled automatically (e.g., 3456×2234 → ~1372×887) with no configurable target size; if text is too small after downscaling, increase the app's font size rather than changing display resolution ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

## Details

### Tool Precedence

Claude uses the most precise tool available for each task. If an MCP server exists for the service, Claude uses that. If the task is a shell command, Claude uses Bash. If the task is browser work and Chrome integration is set up, Claude uses that. Computer use is reserved for things nothing else can reach: native apps, simulators, and tools without an API. ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

### Safety Model

Computer use runs on the actual desktop with access to approved apps, unlike the sandboxed Bash tool. Built-in guardrails include per-app approval (only approved apps in the current session), sentinel warnings for high-access apps, terminal exclusion from screenshots (so on-screen prompts cannot feed back into the model), a global Esc key abort, and a machine-wide lock preventing concurrent sessions from controlling the screen. Claude also checks each action and flags potential prompt injection from on-screen content. ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

### Differences from Desktop App

The CLI and Desktop app share the same computer use engine but differ in several ways. The CLI supports macOS only, while Desktop supports macOS and Windows. In the CLI, computer use is enabled via `/mcp`; in Desktop, it is toggled in Settings > General. The CLI does not yet have a configurable denied apps list or auto-unhide toggle (always on). Desktop supports Dispatch integration for spawned sessions. ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

### Example Workflows

- **Validate a native build**: compile with `xcodebuild`, launch the app, interact with UI controls, and screenshot the result ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- **Reproduce a layout bug**: resize the window to trigger the bug, capture the broken state, then read the relevant stylesheets ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- **Test a simulator flow**: drive the iOS Simulator by tapping through onboarding screens without writing XCTest ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/mcp]]
- [[concepts/permissions]]
- [[concepts/browser_automation]]
- [[concepts/non_interactive_mode]]
- [[summaries/claude-code-computer-use]]