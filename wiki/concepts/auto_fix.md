---
title: "Auto-Fix"
summary: "Feature that watches pull requests for CI failures and review comments, automatically pushing fixes when confident and requesting guidance for ambiguous situations"
type: concept
sources:
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
tags:
  - claude-code
  - cloud
  - ci
  - pr
  - automation
  - github
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Auto-Fix

Auto-fix enables Claude to monitor a pull request and automatically respond to CI failures and review comments. It requires the Claude GitHub App to be installed on the repository. ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Key Points

- Auto-fix requires the Claude GitHub App (not `/web-setup` authentication) because it uses the App to receive PR webhooks ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Can be activated from four entry points: the web UI CI status bar's "Auto-fix" button, the CLI `/autofix-pr` command, the Claude mobile app, or by pasting a PR URL into a session ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Claude classifies PR events into three categories: clear fixes (pushed automatically), ambiguous requests (asks for guidance), and duplicate or no-action events (noted and skipped) ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Claude may reply to review comment threads on GitHub using the user's account; each reply is labeled as coming from Claude Code so reviewers know it was written by the agent ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Repositories with comment-triggered automation (e.g., Atlantis, Terraform Cloud, custom GitHub Actions on `issue_comment`) should review their automation before enabling auto-fix, since Claude can post comments that trigger those workflows ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Details

When auto-fix is active, Claude subscribes to GitHub events for the PR, including new review comments and CI check failures. For each event, Claude investigates and decides how to proceed. Clear fixes that don't conflict with earlier instructions are pushed directly with an explanation in the session. Ambiguous or architecturally significant reviewer comments prompt Claude to ask for guidance before acting. Duplicate or no-action events are noted and skipped.

The `/autofix-pr` CLI command detects the open PR for the current branch using `gh`, spawns a web session, and enables auto-fix in one step. From the web interface, the CI status bar provides an "Auto-fix" toggle. From the mobile app, natural language instructions like "watch this PR and fix any CI failures" activate the feature.

## Related

- [[entities/claude_code_web]]
- [[entities/github]]
- [[concepts/sessions]]