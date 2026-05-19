---
title: "Plan Mode"
summary: "A read-only permission mode that restricts Claude to analysis and planning without making file changes, used for safe code exploration and complex refactoring"
type: concept
sources:
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md
tags:
  - claude-code
  - permissions
  - planning
  - read-only
  - workflows
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Plan Mode

Plan Mode instructs Claude to create a plan by analyzing the codebase with read-only operations, preventing any file modifications. It is designed for exploring codebases, planning complex changes, or reviewing code safely. In Plan Mode, Claude uses `AskUserQuestion` to gather requirements and clarify goals before proposing a plan. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Key Points

- Plan Mode uses read-only operations only; Claude cannot modify files, only analyze and create plans ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Use Plan Mode for multi-step implementations, thorough code exploration, and interactive development where you want to iterate on direction before making changes ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Enter Plan Mode during a session by pressing Shift+Tab to cycle through permission modes (Normal → Auto-Accept → Plan) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Start a new session in Plan Mode with `claude --permission-mode plan` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Run headless queries in Plan Mode with `claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Press Ctrl+G to open the plan in a text editor for direct editing before Claude proceeds ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Accepting a plan automatically names the session from the plan content; the name appears on the prompt bar and in the session picker (existing `--name` or `/rename` names are not overwritten) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Configure Plan Mode as the default permission mode by setting `"defaultMode": "plan"` in `.claude/settings.json` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Details

Plan Mode acts as a safety boundary for code analysis. When active, Claude can read files, search the codebase, and ask clarifying questions, but cannot write, edit, or execute commands that modify the filesystem. This makes it ideal for situations where you want to understand the impact of a change before committing to it, or when reviewing unfamiliar code without risk of accidental modifications.

The Shift+Tab cycle goes through Normal Mode → Auto-Accept Mode (`⏵⏵ accept edits on`) → Plan Mode (`⏸ plan mode on`). When switching from Plan Mode back to Normal Mode, Claude can then execute the plan it created. The headless mode variant (`--permission-mode plan -p`) is useful for CI integration or automated analysis pipelines that should never modify code. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Related

- [[concepts/permissions]]
- [[concepts/non_interactive_mode]]
- [[concepts/sessions]]
- [[concepts/ultraplan]]
- [[entities/claude_code]]
- [[summaries/claude-code-common-workflows]]