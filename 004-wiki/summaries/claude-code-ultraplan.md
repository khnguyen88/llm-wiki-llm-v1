---
title: "Claude Code Ultraplan"
summary: "Ultraplan delegates planning tasks from the CLI to a cloud-based Claude Code on the web session for richer review, inline comments, and flexible execution either remotely or locally"
type: summary
sources:
  - raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md
tags:
  - claude-code
  - planning
  - cloud
  - web
  - workflows
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Ultraplan

## Key Points

- Ultraplan is a research preview (requires v2.1.91+) that hands a planning task from the local CLI to a [[004-wiki/entities/claude_code_web|Claude Code on the web]] session running in [[004-wiki/concepts/plan_mode|plan mode]], freeing the terminal for other work ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- Launch from the CLI via `/ultraplan <prompt>`, the keyword `ultraplan` in a normal prompt, or by choosing "No, refine with Ultraplan" when declining a local plan approval ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- Ultraplan requires a Claude Code on the web account and a GitHub repository; it is not available with Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry authentication ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- The cloud session runs in the account's default [[004-wiki/concepts/cloud_environment|cloud environment]], creating one automatically if none exists ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- If [[004-wiki/concepts/remote_control|Remote Control]] is active, it disconnects when ultraplan starts because both features occupy the claude.ai/code interface ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- Review in the browser supports inline comments (highlight any passage), emoji reactions, and an outline sidebar for navigation; iterate as many times as needed before executing ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- Two execution paths: approve and run on the web (opens a PR from the cloud session), or teleport back to the terminal (choose implement here, start new session, or cancel and save plan to a file) ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]

## Quotes

- "Ultraplan hands a planning task from your local CLI to a Claude Code on the web session running in plan mode." ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- "This is useful when you want a richer review surface than the terminal offers." ^[001a-raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]

## Notes

- The `/ultraplan` command and keyword paths show a confirmation dialog before launching; the local-plan-refinement path skips it since that selection already serves as confirmation.
- The CLI displays three status indicators during ultraplan: `◇ ultraplan` (drafting), `◇ ultraplan needs your input` (clarifying question), `◆ ultraplan ready` (plan ready for review).
- `/tasks` provides a detail view with the session link, agent activity, and a "Stop ultraplan" action that archives the cloud session without saving anything to the terminal.

## Related

- [[004-wiki/concepts/ultraplan]]
- [[004-wiki/entities/claude_code_web]]
- [[004-wiki/entities/claude_code]]
- [[004-wiki/concepts/plan_mode]]
- [[004-wiki/concepts/teleport]]
- [[004-wiki/concepts/cloud_environment]]
- [[004-wiki/concepts/sessions]]