---
title: "Teleport"
summary: "Mechanisms for moving Claude Code tasks between the web cloud and local terminal using --remote, --teleport, and local repository bundling"
type: concept
sources:
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
tags:
  - claude-code
  - cloud
  - remote
  - teleport
  - sessions
  - workflow
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Teleport

Teleport and remote are the two mechanisms for moving Claude Code tasks between the web cloud and a local terminal. `--remote` creates a new cloud session from the CLI; `--teleport` pulls a cloud session into a local terminal. Session handoff from CLI is one-way: sessions can be pulled from the cloud but not pushed from the terminal. ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Key Points

- `claude --remote "task description"` creates a new cloud session that clones the current directory's GitHub remote at the current branch; push local commits first since the VM clones from GitHub, not the local machine ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- `claude --teleport` opens an interactive session picker; `claude --teleport <session-id>` resumes a specific session directly; inside an existing CLI session, `/teleport` or `/tp` does the same without restarting ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- From `/tasks` in the CLI, pressing `t` teleports into a background session; from the web interface, "Open in CLI" copies a terminal command ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Teleport requires: clean git state (no uncommitted changes), running from the same repository (not a fork), the branch pushed to remote, and the same claude.ai account ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Teleport requires claude.ai subscription authentication; API key, Bedrock, Vertex AI, or Microsoft Foundry authentication is not supported; run `/login` to switch to claude.ai auth ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- `--remote` works with a single repository at a time and is distinct from `--remote-control` (which exposes a local CLI session for monitoring from the web) ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Repositories without GitHub can be bundled and uploaded using `CCR_FORCE_BUNDLE=1`; bundles include full history across all branches plus uncommitted changes to tracked files, limited to 100 MB ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Details

Multiple `--remote` commands create independent cloud sessions that run in parallel, enabling concurrent task execution. Use `/tasks` in the CLI to monitor all sessions. The Desktop app provides a "Continue in" menu that can send a local session to the web (this capability does not exist in the CLI).

For complex tasks, a "plan locally, execute remotely" pattern is recommended: start Claude in plan mode (`claude --permission-mode plan`) locally to collaborate on the approach, commit and push the plan, then start a cloud session with `claude --remote "Execute the migration plan in docs/migration-plan.md"` for autonomous execution. The ultraplan feature provides a cloud-native alternative for drafting and reviewing plans in the web interface.

Bundled repositories that exceed 100 MB fall back to bundling only the current branch, then to a single squashed snapshot of the working tree. Bundled sessions cannot push results back to a remote unless GitHub authentication is also configured.

## Related

- [[entities/claude_code_web]]
- [[entities/claude_code]]
- [[concepts/sessions]]
- [[concepts/cloud_environment]]