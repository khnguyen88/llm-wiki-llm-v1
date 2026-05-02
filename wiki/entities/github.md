---
title: "GitHub"
summary: "Code hosting platform integrated with Claude Code analytics for contribution metrics and PR attribution"
type: entity
sources:
  - raw/document/claude code/claude-code-033-analytics-2026-04-29.md
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
  - raw/document/claude code/claude-code-046-code-review-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
tags:
  - github
  - claude-code
  - analytics
  - integration
  - cloud-sessions
  - authentication
  - code-review
  - commands
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# GitHub

Code hosting platform that integrates with Claude Code analytics to provide contribution metrics and PR attribution for Teams and Enterprise plans. ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md] In cloud sessions, GitHub authentication uses either a GitHub App (per-repo scoping, required for auto-fix) or `/web-setup` (syncs local `gh` CLI token). ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Key Facts

- The Claude GitHub app must be installed by a GitHub admin at `github.com/apps/claude` to enable contribution metrics ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Contribution metrics support both GitHub Cloud and GitHub Enterprise Server ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Merged PRs containing Claude Code-assisted lines are labeled `claude-code-assisted` in GitHub ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- The `claude-code-assisted` label enables programmatic querying of Claude Code-attributed PRs via GitHub search ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Cloud sessions authenticate via the Claude GitHub App (per-repo scoping) or `/web-setup` (syncs local `gh` CLI token); the App is required for auto-fix PR functionality ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- A dedicated GitHub proxy handles all git operations in cloud sessions: it manages authentication with scoped credentials, restricts git push to the current working branch, and enables cloning, fetching, and PR operations while maintaining security boundaries ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Cloud sessions include built-in GitHub tools for reading issues, listing PRs, fetching diffs, and posting comments without setup; these tools authenticate through the GitHub proxy, so the user's token never enters the container ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Code Review requires installing the Claude GitHub App with Contents (read/write), Issues (read/write), and Pull Requests (read/write) permissions; the app uses Contents read and Pull Requests write for review functionality ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Code Review findings appear as inline PR comments, as annotations on the Files changed tab, and in the check run Details severity table; the check run always completes with a neutral conclusion so it never blocks merging through branch protection rules ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Manual review triggers use `@claude review` or `@claude review once` as top-level PR comments; require owner, member, or collaborator access; `@claude review` also subscribes the PR to future push-triggered reviews ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- `/install-github-app` sets up the Claude GitHub Actions app for a repository, walking through repo selection and integration configuration ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/analytics]]
- [[concepts/pr_attribution]]
- [[concepts/network_access]]
- [[concepts/auto_fix]]
- [[concepts/code_review]]
- [[concepts/commands]]