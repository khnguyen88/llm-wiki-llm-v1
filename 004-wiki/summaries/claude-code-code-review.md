---
title: "Claude Code Code Review"
summary: "Automated PR review feature that uses multi-agent analysis to find logic errors, security vulnerabilities, and regressions, posting findings as inline GitHub comments with severity levels"
type: summary
sources:
  - raw/document/claude code/claude-code-046-code-review-2026-04-29.md
tags:
  - claude-code
  - code-review
  - github
  - ci-cd
  - automation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Code Review

## Key Points

- Code Review uses a fleet of specialized agents that analyze PR diffs in parallel on Anthropic infrastructure, followed by a verification step that filters false positives before posting findings ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Findings are posted as inline GitHub comments with three severity levels: Important (bugs that should be fixed before merging), Nit (minor issues worth fixing but not blocking), and Pre-existing (bugs not introduced by the PR) ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Reviews can be triggered automatically (on PR creation, on every push, or manual via `@claude review` / `@claude review once` comments); `@claude review` also subscribes the PR to future push-triggered reviews ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- REVIEW.md at the repository root is injected as highest-priority instruction into every review agent, allowing customization of severity definitions, nit caps, skip rules, repo-specific checks, verification bars, re-review convergence, and summary shape ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- CLAUDE.md violations introduced by a PR are flagged as nit-level findings; bidirectional checking also flags when code changes make CLAUDE.md statements outdated ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Reviews average $15-25 per review and complete in about 20 minutes; costs scale with PR size, codebase complexity, and the number of issues requiring verification ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- The check run always completes with a neutral conclusion so it never blocks merging through branch protection rules; a machine-readable severity summary is available for custom CI gating ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

## Quotes

- "A fleet of specialized agents examine the code changes in the context of your full codebase, looking for logic errors, security vulnerabilities, broken edge cases, and subtle regressions." ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- "Length has a cost: a long REVIEW.md dilutes the rules that matter most. Keep it to instructions that change review behavior, and leave general project context in CLAUDE.md." ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

## Notes

- Code Review is in research preview, available for Team and Enterprise subscriptions; not available for organizations with Zero Data Retention enabled
- The GitHub App requests Contents, Issues, and Pull Requests permissions (read/write); Code Review only uses Contents read and Pull Requests write
- Admin setup requires admin access to the Claude organization and permission to install GitHub Apps in the GitHub organization

## Related

- [[concepts/code_review]]
- [[entities/claude_code]]
- [[entities/github]]
- [[concepts/claude_directory]]
- [[concepts/verification]]