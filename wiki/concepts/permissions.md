---
title: "Permissions"
summary: "Mechanism that controls which tools an agent can use through a five-step evaluation flow, six permission modes, and declarative allow/deny rules; in the CLI, specific tools require explicit permission while others operate freely"
type: concept
sources:
  - raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md
  - raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md
  - raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
  - raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md
  - raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
  - raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md
  - raw/document/claude code/claude-code-050-computer-use-2026-04-29.md
  - raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md
  - raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md
tags:
  - agent-sdk
  - permissions
  - security
  - access-control
  - permission-modes
  - agent-teams
  - cli
  - subagents
  - tools
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
provenance: merged
---

# Permissions

Permissions in the Agent SDK control which tools an agent can use and how tool approvals are handled. They operate through a five-step evaluation flow that combines hooks, deny rules, permission modes, allow rules, and the `canUseTool` callback. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md] ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]

## Key Points

- Permission evaluation follows a strict order: (1) hooks, (2) deny rules, (3) permission mode, (4) allow rules, (5) `canUseTool` callback ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Deny rules (`disallowed_tools` and `settings.json` deny rules) are checked before permission mode and can block tools even in `bypassPermissions` mode ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Six permission modes: `default` (no auto-approvals), `dontAsk` (deny unmatched tools), `acceptEdits` (auto-approve file ops), `bypassPermissions` (approve everything), `plan` (no tool execution), and `auto` (TypeScript only, model-classified) ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- `allowed_tools` pre-approves specific tools but does not constrain `bypassPermissions`; unlisted tools fall through to the mode check where `bypassPermissions` approves them ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md] ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Permission mode can be set at query time and changed dynamically mid-session via `set_permission_mode()` / `setPermissionMode()` ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- When a parent uses `bypassPermissions`, `acceptEdits`, or `auto`, all subagents inherit that mode and it cannot be overridden per subagent ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Allow, deny, and ask rules can be declared in `.claude/settings.json`, loaded when the `project` setting source is enabled ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Tool combinations define capability tiers: `Read`, `Glob`, `Grep` for read-only analysis; adding `Edit` enables code modification; adding `Bash` enables full automation including running tests and executing commands ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- Bash commands are parsed into an AST and matched against permission rules before execution; commands that cannot be parsed cleanly require explicit approval ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Constructs like `eval` always require approval regardless of allow rules; the command parsing is a permission gate, not a sandbox, and does not infer whether a command is dangerous from its target path or effects ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- Organizations can set permission policies that apply across all users; glob patterns enable rules like "allow all npm commands" or "block any command with sudo" ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- In agent teams, all teammates start with the lead's permission settings; if the lead runs with `--dangerously-skip-permissions`, all teammates do too; individual teammate modes can be changed after spawning but per-teammate modes cannot be set at spawn time ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- The auto mode classifier is a second gate that runs after the permissions system; `permissions.deny` in managed settings blocks actions before the classifier is consulted and cannot be overridden by classifier rules ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- In auto mode, the classifier reads `autoMode` from user settings, local project settings, managed settings, and inline JSON — but not from shared project `.claude/settings.json`, preventing checked-in repos from injecting allow rules ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- Permission relay (v2.1.81+) forwards tool approval prompts to a remote channel so users can approve or deny tool use from another device; it covers tool-use approvals (Bash, Write, Edit) but not project trust or MCP server consent dialogs ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- CLI permission flags: `--permission-mode` sets the initial mode (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`), overriding `defaultMode` from settings; `--allowedTools` pre-approves tools without prompting (supports glob patterns like `"Bash(git log *)"`); `--disallowedTools` removes tools from the model's context entirely ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--dangerously-skip-permissions` is equivalent to `--permission-mode bypassPermissions`; `--allow-dangerously-skip-permissions` adds `bypassPermissions` to the Shift+Tab mode cycle without starting in it, allowing a session to begin in a different mode like `plan` and switch to `bypassPermissions` later ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--permission-prompt-tool` specifies an MCP tool to handle permission prompts in non-interactive mode ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Computer use uses per-session app approval: the first time Claude needs a specific app, a prompt shows which apps it wants to control, any extra permissions (e.g., clipboard access), and how many other apps will be hidden; approval lasts for the current session only ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Apps with broad access show sentinel warnings in the approval prompt: Terminal, iTerm, VS Code, and other terminals/IDEs warn "equivalent to shell access"; Finder warns "can read or write any file"; System Settings warns "can change system settings" ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Claude's level of control varies by app category in computer use: browsers and trading platforms are view-only, terminals and IDEs are click-only, and everything else gets full control ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Subagent `permissionMode` field controls how the subagent handles permission prompts: `default` (standard prompts), `acceptEdits` (auto-accept file edits for working directory paths), `auto` (background classifier), `dontAsk` (auto-deny prompts, explicitly allowed tools still work), `bypassPermissions` (skip all prompts), `plan` (read-only) ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- In subagents, `bypassPermissions` still prompts for writes to `.git`, `.claude`, `.vscode`, `.idea`, and `.husky` directories (except `.claude/commands`, `.claude/agents`, and `.claude/skills`) ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- `Agent(subagent-name)` syntax in `permissions.deny` settings prevents Claude from using specific subagents by name; works for both built-in and custom subagents ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- In the CLI, tools requiring explicit permission are: Bash, Edit, ExitPlanMode, Monitor, NotebookEdit, PowerShell, Skill, WebFetch, WebSearch, and Write; all other built-in tools operate without prompting; to disable a tool entirely, add its name to the `deny` array in permission settings ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Details

Permissions serve as the safety boundary for agent actions. The evaluation flow processes each tool request in sequence: hooks run first and can allow, deny, or pass; deny rules block matching tools unconditionally; the permission mode applies global behavior (e.g., `acceptEdits` approves file operations, `bypassPermissions` approves everything that reaches this step); allow rules pre-approve specific tools; and finally `canUseTool` handles anything not resolved by the earlier steps. In `dontAsk` mode, the `canUseTool` callback is skipped and the tool is denied instead. ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]

The `acceptEdits` mode auto-approves file edits (Edit, Write tools) and filesystem commands (`mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`) but only for paths inside the working directory or `additionalDirectories`. Other tools like Bash commands that aren't filesystem operations still require normal permissions. The `bypassPermissions` mode approves all tools without prompts, but hooks and deny rules evaluated earlier in the flow can still block operations. The `plan` mode prevents all tool execution entirely, allowing Claude only to analyze and create plans; it may still use `AskUserQuestion` to clarify requirements. ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]

A common pattern is creating a locked-down agent by pairing `allowedTools` with `permissionMode: "dontAsk"` — listed tools are approved, and anything else is denied outright instead of prompting. For a read-only agent, restrict `allowed_tools` to `Read`, `Glob`, and `Grep`. `allowed_tools` only pre-approves the tools listed; unlisted tools are not matched by any allow rule and fall through to the permission mode. This means `allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"` still approves every tool; use `disallowed_tools` to block specific tools in that scenario. ^[raw/document/claude code/claude-code-013-agent-sdk-overview-2026-04-29.md] ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/hooks]]
- [[concepts/custom_tools]]
- [[concepts/subagents]]
- [[concepts/setting_sources]]
- [[concepts/secure_deployment]]
- [[concepts/agent_teams]]
- [[concepts/auto_mode]]
- [[concepts/channels]]
- [[concepts/computer_use]]
- [[summaries/claude-code-tools-reference]]
- [[summaries/claude-code-cli-reference]]
- [[summaries/claude-code-sub-agents]]