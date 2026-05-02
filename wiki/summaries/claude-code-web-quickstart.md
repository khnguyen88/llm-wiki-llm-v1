---
title: "Claude Code Web Quickstart"
summary: "Setup guide for Claude Code on the web: connecting GitHub, creating cloud environments, starting tasks, pre-filling sessions, and reviewing changes"
type: summary
sources:
  - raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md
tags:
  - claude-code
  - web
  - quickstart
  - github
  - cloud
  - sessions
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Web Quickstart

## Key Points

- Claude Code on the web runs on Anthropic-managed cloud VMs; sessions persist across devices and continue running after the browser tab is closed ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Setup requires connecting a GitHub account via the Claude GitHub App or `/web-setup` from the CLI, then creating a cloud environment with network access, environment variables, and an optional setup script ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Each web session follows: clone and prepare → configure network → work → push branch; the session stays live after pushing so PR creation and further edits happen within the same conversation ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Cloud sessions offer only Auto accept edits and Plan permission modes; Ask, Auto, and Bypass are not available ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Web sessions are best suited for parallel tasks, repos not available locally, well-defined tasks that need minimal steering, and code exploration without a local checkout ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Sessions can be pre-filled via URL parameters (`prompt`, `prompt_url`, `repositories`, `environment`) to build integrations like issue-tracker buttons ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Review workflow uses a diff view with inline comments; comments queue until the next message, then bundle with it so Claude sees the file and line context ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]

## Quotes

- "Claude clones the repositories, runs your setup script if configured, and starts working. Each task gets its own session and its own branch, so you don't need to wait for one to finish before starting another." ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- "The session doesn't close when the branch is pushed. PR creation and further edits all happen within the same conversation." ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- "Closing the tab or navigating away doesn't stop the session. It continues running in the background until Claude finishes the current task, then idles." ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]

## Notes

- The comparison table in the source shows how web, Remote Control, Terminal CLI, and Desktop app differ on execution location, chat interface, local config availability, GitHub requirement, persistence, permission modes, and network access
- Organizations with Zero Data Retention enabled cannot use `/web-setup` or other cloud session features
- `/web-setup` requires CLI v2.1.80+ and claude.ai subscription authentication; API key or third-party provider auth is not supported

## Related

- [[entities/claude_code_web]]
- [[entities/github]]
- [[concepts/cloud_environment]]
- [[concepts/network_access]]
- [[concepts/permissions]]
- [[concepts/session_prefill]]
- [[concepts/sessions]]
- [[concepts/parallel_sessions]]
- [[concepts/teleport]]