---
title: "PR Attribution"
summary: "Mechanism that matches Claude Code session activity against merged PR diffs to determine which code was written with Claude Code assistance"
type: concept
sources:
  - raw/document/claude code/claude-code-033-analytics-2026-04-29.md
tags:
  - pr-attribution
  - analytics
  - claude-code
  - github
  - contribution-metrics
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# PR Attribution

The process by which Claude Code determines which lines in a merged pull request were written with Claude Code assistance, by matching session activity against PR diffs. ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Key Points

- PRs are tagged as "with Claude Code" if they contain at least one line written during a Claude Code session, using conservative matching for high confidence ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- The attribution process extracts added lines from the PR diff, identifies matching Claude Code sessions within a time window, matches PR lines against Claude Code output using multiple strategies, and calculates metrics ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- The time window spans 21 days before to 2 days after the PR merge date ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Lines are normalized before comparison: whitespace trimming, multiple-space collapsing, quote standardization, and lowercase conversion ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Code substantially rewritten by developers (more than 20% difference) is not attributed to Claude Code ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Details

When a PR is merged, the system extracts added lines from the diff, identifies Claude Code sessions that edited matching files within the attribution time window, matches PR lines against Claude Code output, and calculates metrics for AI-assisted lines and total lines. Merged PRs containing Claude Code-assisted lines are labeled `claude-code-assisted` in GitHub. ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

Certain files are automatically excluded from analysis because they are auto-generated: lock files (package-lock.json, yarn.lock, Cargo.lock), generated code (Protobuf outputs, build artifacts, minified files), build directories (dist/, build/, node_modules/, target/), test fixtures (snapshots, cassettes, mock data), and lines over 1,000 characters. ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

The algorithm does not consider the PR source or destination branch when performing attribution. Sessions outside the 21-day window are not considered. ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/github]]
- [[concepts/analytics]]