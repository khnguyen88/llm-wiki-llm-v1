---
title: "Ultraplan"
summary: "A Claude Code feature that delegates planning tasks from the CLI to a cloud-based web session for collaborative review and flexible execution"
type: concept
sources:
  - raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
tags:
  - claude-code
  - planning
  - cloud
  - web
  - workflows
  - early-preview
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Ultraplan

Ultraplan delegates a planning task from the local CLI to a [[entities/claude_code_web|Claude Code on the web]] session running in [[concepts/plan_mode|plan mode]]. Claude drafts the plan in the cloud while the terminal stays free for other work. When the plan is ready, the user reviews it in the browser and chooses where to execute it. Ultraplan entered early preview in Week 15 (v2.1.92-101, April 6-10, 2026). ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md] ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

## Key Points

- Three ways to launch from the CLI: `/ultraplan <prompt>` command, the keyword `ultraplan` in a normal prompt, or choosing "No, refine with Ultraplan" when declining a local plan approval ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- Requires Claude Code v2.1.91+, a Claude Code on the web account, and a GitHub repository; not available with Bedrock, Vertex AI, or Microsoft Foundry authentication ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- The cloud session runs in the account's default [[concepts/cloud_environment|cloud environment]], creating one automatically if none exists ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- [[concepts/remote_control|Remote Control]] disconnects when ultraplan starts because both features use the claude.ai/code interface simultaneously ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- Browser review supports inline comments (highlight any passage), emoji reactions, and an outline sidebar; users can iterate on the plan before choosing execution ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]

## Details

The CLI shows three status indicators while ultraplan runs: `◇ ultraplan` (Claude is researching and drafting), `◇ ultraplan needs your input` (clarifying question available in the web session), and `◆ ultraplan ready` (plan ready for review). Running `/tasks` and selecting the ultraplan entry opens a detail view with the session link, agent activity, and a "Stop ultraplan" action that archives the cloud session. ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]

When the plan is approved, two execution paths are available. **Execute on the web** has Claude implement the plan in the same cloud session; after completion the user reviews the diff and creates a pull request from the web interface. **Teleport back to terminal** sends the plan to the waiting CLI session with three options: "Implement here" (inject the plan into the current conversation), "Start new session" (begin fresh with only the plan as context, printing a `claude --resume` command to return to the previous conversation later), or "Cancel" (save the plan to a file without executing). The web session is archived when teleporting back so it does not continue working in parallel. ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]

The command and keyword launch paths show a confirmation dialog before proceeding; the local-plan-refinement path skips this dialog because the user's selection to refine with ultraplan already serves as confirmation. ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]

## Related

- [[entities/claude_code_web]]
- [[entities/claude_code]]
- [[concepts/plan_mode]]
- [[concepts/teleport]]
- [[concepts/cloud_environment]]
- [[concepts/sessions]]
- [[summaries/claude-code-ultraplan]]