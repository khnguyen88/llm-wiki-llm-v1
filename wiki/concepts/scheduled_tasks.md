---
title: "Scheduled Tasks"
summary: "Four approaches for running Claude Code tasks on a schedule or recurring basis: Routines, desktop scheduled tasks, GitHub Actions, and the /loop CLI command; session-scoped cron tools (CronCreate, CronDelete, CronList) manage in-session scheduling"
type: concept
sources:
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md
tags:
  - claude-code
  - scheduling
  - automation
  - routines
  - github-actions
  - cron
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Scheduled Tasks

Running Claude Code tasks automatically on a recurring basis or at specific times. Four approaches exist, each suited to different deployment contexts and access requirements. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Key Points

- **Routines** run on Anthropic-managed infrastructure and can operate even when your computer is off; they also support API call and GitHub event triggers in addition to schedules; configure at claude.ai/code/routines ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- **Desktop scheduled tasks** run on your local machine via the Claude Code desktop app, providing direct access to local files, tools, and uncommitted changes ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- **GitHub Actions** run in your CI pipeline, suited for tasks tied to repo events (opened PRs) or cron schedules alongside workflow config ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- **`/loop`** is an in-session CLI command for quick polling while a session is open; tasks stop when you start a new conversation, but `--resume` and `--continue` can restore unexpired ones ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

- **CronCreate**, **CronDelete**, and **CronList** are session-scoped tools for managing scheduled prompts within a running session; CronCreate schedules a recurring or one-shot prompt, CronDelete cancels a scheduled task by ID, and CronList lists all scheduled tasks in the session ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- Cron tasks are session-scoped and are restored on `--resume` or `--continue` if they have not expired ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]
- When writing prompts for scheduled tasks, be explicit about what success looks like and what to do with results, since the task runs autonomously and cannot ask clarifying questions ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Details

| Option | Where it runs | Best for |
|--------|---------------|----------|
| Routines | Anthropic-managed infrastructure | Tasks that should run even when your computer is off; can also trigger on API calls or GitHub events |
| Desktop scheduled tasks | Your machine via the desktop app | Tasks needing direct access to local files, tools, or uncommitted changes |
| GitHub Actions | Your CI pipeline | Tasks tied to repo events like opened PRs, or cron schedules that should live alongside workflow config |
| `/loop` | Current CLI session | Quick polling while a session is open; tasks stop when you start a new conversation |

^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

Scheduled task prompts should define success criteria explicitly and specify what to do with results, since the task cannot ask for clarification mid-execution. For example: "Review open PRs labeled `needs-review`, leave inline comments on any issues, and post a summary in the `#eng-reviews` Slack channel." ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/non_interactive_mode]]
- [[concepts/auto_mode]]
- [[entities/github]]
- [[concepts/cloud_environment]]
- [[summaries/claude-code-common-workflows]]