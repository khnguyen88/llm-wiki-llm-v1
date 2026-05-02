---
title: "Rate Limiting"
summary: "Per-user TPM and RPM recommendations for Claude Code team deployments, scaling inversely with team size to account for concurrency patterns"
type: concept
sources:
  - raw/document/claude code/claude-code-052-costs-2026-04-29.md
  - raw/document/claude code/claude-code-105-statusline-2026-04-29.md
tags:
  - rate-limiting
  - claude-code
  - team-management
  - deployment
  - cost-management
  - statusline
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Rate Limiting

Per-user Token Per Minute (TPM) and Request Per Minute (RPM) recommendations for Claude Code team deployments. Rate limits apply at the organization level, not per individual user, meaning individual users can temporarily consume more than their calculated share when others are not actively using the service. ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Key Points

- Rate limits apply at the organization level, not per individual user; individuals can temporarily exceed their calculated share when others are inactive ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- TPM per user decreases as team size grows because fewer users tend to use Claude Code concurrently in larger organizations ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- For organizations with custom rate limits, Claude Code traffic in the workspace counts toward the organization's overall API rate limits; a workspace rate limit can cap Claude Code's share and protect other production workloads ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Scenarios with unusually high concurrent usage (such as live training sessions with large groups) may need higher TPM allocations per user ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- The statusline exposes Claude.ai subscription rate limit usage via `rate_limits.five_hour.used_percentage` and `rate_limits.seven_day.used_percentage` (0-100), with `resets_at` Unix epoch timestamps; this field only appears for Pro/Max subscribers after the first API response, and each window may be independently absent ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

## Details

Recommended per-user TPM and RPM allocations based on organization size:

| Team size | TPM per user | RPM per user |
|---|---|---|
| 1-5 users | 200k-300k | 5-7 |
| 5-20 users | 100k-150k | 2.5-3.5 |
| 20-50 users | 50k-75k | 1.25-1.75 |
| 50-100 users | 25k-35k | 0.62-0.87 |
| 100-500 users | 15k-20k | 0.37-0.47 |
| 500+ users | 10k-15k | 0.25-0.35 |

^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

For example, a 200-user organization might request 20k TPM per user, or 4 million total TPM (200 x 20,000). The workspace rate limit can be configured on the workspace's Limits page in the [[entities/claude_console|Claude Console]]. ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Related

- [[entities/claude_console]]
- [[concepts/cost_tracking]]
- [[concepts/token_optimization]]
- [[concepts/statusline]]
- [[summaries/claude-code-costs]]