---
title: "Claude Code Analytics"
summary: "Analytics dashboards for tracking team usage, contribution metrics, and engineering velocity impact of Claude Code across Teams/Enterprise and API plans"
type: summary
sources:
  - raw/document/claude code/claude-code-033-analytics-2026-04-29.md
tags:
  - claude-code
  - analytics
  - contribution-metrics
  - pr-attribution
  - github
  - enterprise
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Analytics

## Key Points

- Claude Code provides two analytics dashboards: Teams/Enterprise at `claude.ai/analytics/claude-code` and API customers at `platform.claude.com/claude-code` ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Teams/Enterprise dashboard includes usage metrics, contribution metrics with GitHub integration, a leaderboard, and CSV data export; API dashboard shows usage, spend, and team insights only ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Contribution metrics require installing the Claude GitHub app and enabling analytics at `claude.ai/admin-settings/claude-code`; they are not available for Zero Data Retention organizations or API customers ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Contribution metrics are deliberately conservative underestimates: only lines and PRs with high confidence in Claude Code involvement are counted ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- PR attribution matches Claude Code session activity against merged PR diffs within a 21-day-before to 2-day-after window, with line normalization and multiple matching strategies ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Auto-generated files (lock files, build artifacts, minified files, test fixtures, lines over 1,000 characters) are excluded from attribution analysis ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Merged PRs containing Claude Code-assisted lines are labeled `claude-code-assisted` in GitHub, enabling programmatic queries ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Quotes

- "These metrics are deliberately conservative and represent an underestimate of Claude Code's actual impact. Only lines and PRs where there is high confidence in Claude Code's involvement are counted." ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- "Code substantially rewritten by developers, with more than 20% difference, is not attributed to Claude Code" ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Notes

- Data typically appears within 24 hours after enabling contribution metrics, with daily updates ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- The algorithm does not consider the PR source or destination branch when performing attribution ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- "Effective lines" for lines-of-code counting exclude empty lines, lines with only brackets/trivial punctuation, and lines with 3 or fewer characters after normalization ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Spend figures in the Console dashboard are estimates for analytics purposes; actual costs are on the billing page ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/github]]
- [[concepts/analytics]]
- [[concepts/pr_attribution]]
- [[concepts/observability]]
- [[concepts/cost_tracking]]