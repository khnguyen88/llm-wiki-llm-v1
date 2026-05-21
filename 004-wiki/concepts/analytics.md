---
title: "Analytics"
summary: "Claude Code's dashboard system for tracking team usage, contribution metrics, and engineering velocity across Teams/Enterprise and API plans"
type: concept
sources:
  - raw/document/claude code/claude-code-033-analytics-2026-04-29.md
  - raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md
tags:
  - analytics
  - claude-code
  - usage-tracking
  - metrics
  - enterprise
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Analytics

Claude Code provides analytics dashboards that let organizations understand developer usage patterns, track contribution metrics, and measure engineering velocity impact. ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Key Points

- Two dashboards exist: Teams/Enterprise at `claude.ai/analytics/claude-code` and API customers at `platform.claude.com/claude-code` ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Teams/Enterprise dashboard includes usage metrics (lines accepted, suggestion accept rate, daily active users, sessions), contribution metrics with GitHub integration, a leaderboard, and CSV data export ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- API dashboard shows lines of code accepted, suggestion accept rate, activity (daily active users/sessions), spend (daily API costs), and per-user team insights ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Usage and adoption data is available for all Teams/Enterprise accounts; contribution metrics require GitHub integration setup ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- The leaderboard shows the top 10 users ranked by contribution volume, with an export option for all users as CSV ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Details

Usage metrics track session-level activity: lines of code accepted (excluding rejected suggestions and not tracking subsequent deletions), suggestion accept rate (percentage of Edit, Write, and NotebookEdit tool usage accepted), daily active users, and sessions. ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

The dashboard includes several charts: Adoption (daily active users and sessions), PRs per user (merged PRs per day divided by daily active users), Pull requests breakdown (PRs with vs. without Claude Code, toggleable to lines-of-code view), and the Leaderboard. ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

Contribution metrics are in public beta and only cover users within the claude.ai organization. Usage through the Claude Console API or third-party integrations is not included. They are not available for organizations with Zero Data Retention enabled. ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

Under ZDR, the analytics dashboard shows usage metrics only; Claude Code Analytics does not store prompts or model responses but collects productivity metadata such as account emails and usage statistics. ^[001a-raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]

For API customers, the team insights table shows per-user metrics: members (authenticated users, displayed by key identifier for API key users or email for OAuth users), spend this month, and lines this month. ^[001a-raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Related

- [[004-wiki/entities/claude-code]]
- [[004-wiki/entities/github]]
- [[004-wiki/concepts/pr-attribution]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/concepts/cost-tracking]]
- [[004-wiki/concepts/zero-data-retention]]