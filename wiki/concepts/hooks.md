---
title: "Hooks"
summary: "Callbacks that fire at specific points in the agent loop lifecycle, enabling interception, modification, or blocking of tool calls and other agent actions"
type: concept
sources:
  - raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md
  - raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md
  - raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md
  - raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md
  - raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md
  - raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md
  - raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md
  - raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md
tags:
  - hooks
  - claude-code
  - agent-sdk
  - lifecycle
  - extensibility
  - callbacks
  - permissions
  - agent-teams
  - cloud-sessions
  - terminal-config
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Hooks

Callbacks that fire at specific points in the agent loop lifecycle, allowing developers to intercept, modify, or block agent actions. Hooks run in the application process, not inside the agent's context window, so they do not consume context tokens. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

## Key Points

- Hooks run outside the agent's context window and do not consume context tokens ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- A `PreToolUse` hook that rejects a tool call short-circuits the loop: the tool does not execute, and Claude receives the rejection message as the tool result ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Six primary hook types: PreToolUse (before execution), PostToolUse (after return), UserPromptSubmit (when a prompt is sent), Stop (when agent finishes), SubagentStart/SubagentStop (when subagent spawns/completes), and PreCompact (before context compaction) ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Both Python and TypeScript SDKs support all primary hook events; the TypeScript SDK includes additional observability events not yet available in Python ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- The SDK supports two hook types that run side by side: filesystem hooks (shell commands defined in `settings.json`, loaded via `settingSources`) and programmatic hooks (callback functions passed to `query()`) ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Filesystem hooks support five types: `"command"` (shell scripts), `"http"` (POST to an endpoint), `"mcp_tool"` (call an MCP server tool), `"prompt"` (LLM evaluates a prompt), and `"agent"` (spawns a verifier agent); they fire in both the main agent and any subagents it spawns ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Programmatic hooks are scoped to the main session only and run in the application process; returning `{}` allows the tool to proceed, while `{"decision": "block", "reason": "..."}` prevents execution ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- The TypeScript SDK supports additional hook events beyond Python: `SessionStart`, `SessionEnd`, `TeammateIdle`, and `TaskCompleted` ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- 18 total hook events are available across both SDKs: PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch (TS only), UserPromptSubmit, Stop, SubagentStart, SubagentStop, PreCompact, PermissionRequest, Notification, SessionStart (TS only), SessionEnd (TS only), Setup (TS only), TeammateIdle (TS only), TaskCompleted (TS only), ConfigChange (TS only), WorktreeCreate (TS only), and WorktreeRemove (TS only) ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Hooks are configured in the `hooks` field of `ClaudeAgentOptions` (Python) or `options` (TypeScript), keyed by event name with arrays of `HookMatcher` objects containing an optional regex `matcher`, a required `hooks` array of callbacks, and an optional `timeout` (default 60 seconds) ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Every callback receives three arguments: typed input data (with `session_id`, `cwd`, `hook_event_name`, plus event-specific fields), a tool use ID for correlating Pre/Post events, and a context object; in TypeScript, the context contains an `AbortSignal` for cancellation ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Callbacks return output objects with top-level fields (`systemMessage` to inject context visible to the model, `continue`/`continue_` to control agent continuation) and `hookSpecificOutput` with event-specific fields: `permissionDecision` (`"allow"`, `"deny"`, `"ask"`, or `"defer"` in TypeScript only), `permissionDecisionReason`, and `updatedInput` ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Permission decision priority: deny > defer > ask > allow; if any hook returns deny, the operation is blocked regardless of other hooks ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Async output (`{"async": true}` / `{"async_": True}` in Python) tells the agent to proceed without waiting for the hook to finish; used only for side effects like logging, metrics, or notifications ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Matchers filter by tool name only (not file paths or arguments); to filter by file path, check `tool_input.file_path` inside the callback ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- Hook execution produces `claude_code.hook` spans in OpenTelemetry traces when enhanced telemetry beta is enabled; requires `ENABLE_BETA_TRACING_DETAILED=1` and `BETA_TRACING_ENDPOINT` in addition to standard tracing variables ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Agent team hooks enforce quality gates: `TeammateIdle` fires when a teammate is about to go idle (exit code 2 sends feedback and keeps the teammate working), `TaskCreated` fires when a task is being created (exit code 2 prevents creation), `TaskCompleted` fires when a task is marked complete (exit code 2 prevents completion) ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Hooks are the first step in the permission evaluation flow: they run before deny rules, permission modes, and allow rules, and can allow, deny, or continue to the next step ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- The `PermissionDenied` hook fires when auto mode denies a tool call, enabling programmatic reaction to denials (e.g., logging, alerting, or auto-remediation) ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- Hooks are deterministic and guarantee the action happens, unlike CLAUDE.md instructions which are advisory; if a rule in CLAUDE.md keeps being ignored, convert it to a hook ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Claude can write hooks: try prompts like "Write a hook that runs eslint after every file edit" or "Write a hook that blocks writes to the migrations folder" ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Run `/hooks` to browse configured hooks ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- In cloud sessions, SessionStart hooks defined in the repo's `.claude/settings.json` run on every session including resumes; user-level hooks from `~/.claude/settings.json` do not carry over ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Cloud-only hook logic can use the `CLAUDE_CODE_REMOTE` environment variable (set to `true` in cloud sessions) to skip execution in local environments ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Cloud session hooks that install packages require network access to reach registries; they fail under "None" network access and some package managers (notably Bun) have known proxy compatibility issues ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Setup scripts differ from SessionStart hooks: setup scripts are attached to the cloud environment (run before Claude launches, benefit from caching), while SessionStart hooks are attached to the repository (run after Claude launches, on every session including resumes) ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- The Notification hook event fires when Claude needs user attention; matcher values filter by event type: `permission_prompt` (tool approval needed), `idle_prompt` (Claude done, waiting for input), `auth_success` (authentication completes), `elicitation_dialog` (MCP server opens form), `elicitation_complete` (MCP form submitted/dismissed), `elicitation_response` (MCP response sent) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Platform-specific Notification hook commands: macOS uses `osascript -e 'display notification'`, Linux uses `notify-send`, Windows uses `powershell.exe` with `System.Windows.Forms.MessageBox` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- `SubagentStart` and `SubagentStop` are hook events in `settings.json` that respond to subagent lifecycle in the main session; both support matchers to target specific agent types by name ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Subagent frontmatter can define hooks that run only while that specific subagent is active and are cleaned up when it finishes; `Stop` hooks in frontmatter are automatically converted to `SubagentStop` events at runtime ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Frontmatter hooks fire both when the agent is spawned as a subagent through the Agent tool and when the agent runs as the main session via `--agent` or the `agent` setting; in the main-session case they run alongside any hooks defined in `settings.json` ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- `PreToolUse` hooks in subagent frontmatter can validate operations before they execute, enabling patterns like read-only database enforcement where the hook script reads JSON from stdin, extracts the command, and exits with code 2 to block disallowed operations ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- In terminals without native desktop notification support (Warp, Apple Terminal, and others), a Notification hook can play a sound or run a custom command when Claude finishes a task or pauses for permission; hooks run alongside the native desktop notification rather than replacing it ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Notification hooks are configured in `settings.json` under the `hooks` key with `Notification` event type and a `command` hook type; example: `{"hooks": {"Notification": [{"hooks": [{"type": "command", "command": "afplay /System/Library/Sounds/Glass.aiff"}]}]}}` plays a macOS system sound ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Desktop notifications reach the OS natively in Ghostty and Kitty without setup; iTerm2 requires enabling "Notification Center Alerts" and "Send escape sequence-generated alerts" in Settings → Profiles → Terminal; notifications also reach local machines over SSH ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Details

Hooks enable several key patterns in the agent loop. PreToolUse hooks can validate inputs and block dangerous commands before they execute. PostToolUse hooks can audit outputs and trigger side effects after a tool returns. UserPromptSubmit hooks can inject additional context into prompts. Stop hooks can validate results and save session state. PreCompact hooks can archive the full transcript before summarization occurs. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

The PreCompact hook is particularly important for context management. When the agent loop approaches the context window limit, automatic compaction summarizes older history. A PreCompact hook receives a `trigger` field (`manual` or `auto`) and can, for example, archive the full conversation transcript before compaction discards the details. This hook fires before the compactor runs, giving the developer a chance to preserve information that the summary might lose. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

Hooks execute in the order they appear in the matcher array, and each hook should be focused on a single responsibility. Multiple matchers can be chained for complex logic — for example, a rate limiter, then authorization, then input sanitization, then audit logging. ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md] The `matcher` field is a regex string matched against a value that depends on the hook event type: for tool-based hooks, it matches the tool name; for other hooks, it matches the event-specific field. Hooks without a matcher run for every occurrence of that event type. ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]

When using `updatedInput` to modify a tool call, the callback must also return `permissionDecision: 'allow'` for the modification to take effect. The original `tool_input` should never be mutated directly; instead, return a new object. The `systemMessage` top-level output field injects context into the conversation that the model sees, but it may not appear in all SDK output modes. ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]

A `UserPromptSubmit` hook that spawns subagents can create infinite loops if those subagents trigger the same hook. Prevent this by checking for a subagent indicator in the hook input before spawning, using a shared variable or session state to track recursion, or scoping hooks to only run for the top-level agent session. ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/agent_loop]]
- [[concepts/context_window]]
- [[concepts/setting_sources]]
- [[concepts/skills]]
- [[concepts/observability]]
- [[concepts/agent_teams]]
- [[concepts/auto_mode]]
- [[concepts/cloud_environment]]
- [[summaries/claude-code-common-workflows]]
- [[summaries/claude-code-best-practices]]
- [[concepts/subagents]]
- [[summaries/claude-code-sub-agents]]
- [[concepts/terminal_config]]
- [[summaries/claude-code-terminal-config]]