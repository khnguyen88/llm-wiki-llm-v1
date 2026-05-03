---
title: "Routines"
summary: "Templated cloud agents on Claude Code on the web that fire on a schedule, GitHub event, or API call, running without the user's machine being active"
type: concept
sources:
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
tags:
  - claude-code
  - cloud
  - automation
  - scheduling
  - github
  - routines
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Routines

Routines are templated cloud agents on [[entities/claude_code_web|Claude Code on the web]] that fire on a schedule, a GitHub event, or an API call, without requiring the user's machine to be running. They are defined once with a prompt, the repos they can touch, and the connectors they need. ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Key Points

- Routines are created on Claude Code on the web and run on Anthropic-managed infrastructure, not the user's local machine ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Three trigger types: scheduled (cron-style timing), GitHub events (with optional filters), and API calls via a tokened `/fire` endpoint ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- GitHub event triggers include `PR-opened` and `release-published`, with optional filters to scope which events actually fire the routine ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Each routine receives a unique tokened `/fire` endpoint that external systems can call to trigger execution ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Routines can be scaffolded from the terminal using `/schedule` (e.g., `/schedule daily PR review at 9am`) ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Details

Routines extend Claude Code on the web's cloud execution model to event-driven and scheduled automation. A routine definition specifies three components: the prompt (what the agent should do), the repositories it can access, and any connectors (MCP servers or other integrations) it needs. Once defined, the routine runs automatically whenever its trigger fires, without needing a user to initiate or monitor the session.

The trigger picker in the web UI covers GitHub events (with optional filters) and schedule-based timing. External systems can also trigger routines by calling the routine's unique `/fire` endpoint with an API token. This makes routines suitable for CI/CD integration, automated code review, and scheduled maintenance tasks. ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Related

- [[entities/claude_code_web]]
- [[entities/claude_code]]
- [[concepts/scheduled_tasks]]
- [[concepts/commands]]
- [[concepts/cloud_environment]]