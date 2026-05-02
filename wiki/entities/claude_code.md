---
title: "Claude Code"
summary: "Anthropic's CLI tool for deploying and managing Claude in organizational environments, with managed policy enforcement, multiple API provider support, and configurable security controls"
type: entity
sources:
  - raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md
  - raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md
  - raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md
  - raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md
  - raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md
  - raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md
  - raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md
  - raw/document/claude code/claude-code-033-analytics-2026-04-29.md
  - raw/document/claude code/claude-code-034-authentication-2026-04-29.md
  - raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md
  - raw/document/claude code/claude-code-037-champion-kit-2026-04-29.md
  - raw/document/claude code/claude-code-039-channels-2026-04-29.md
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
  - raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md
  - raw/document/claude code/claude-code-042-chrome-2026-04-29.md
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
  - raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md
  - raw/document/claude code/claude-code-046-code-review-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-049-communications-kit-2026-04-29.md
  - raw/document/claude code/claude-code-050-computer-use-2026-04-29.md
  - raw/document/claude code/claude-code-051-context-window-2026-04-29.md
tags:
  - claude-code
  - anthropic
  - cli
  - dev-tools
  - enterprise
  - agent-sdk
  - skills
  - settings
  - observability
  - agent-teams
  - analytics
  - authentication
  - channels
  - checkpointing
  - chrome
  - browser-automation
  - cloud-sessions
  - remote
  - teleport
  - auto-fix
  - cli-flags
  - code-review
  - commands
  - context-window
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Claude Code

Anthropic's command-line tool for interacting with Claude, designed for organizational deployment with managed policy enforcement, multiple API provider support, and configurable security controls. ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md] The Agent SDK extends Claude Code's capabilities by embedding its autonomous agent loop in external applications as a standalone package. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

## Key Facts

- Connects to Claude through five API providers: Claude for Teams/Enterprise (per-seat, default), Claude Console (pay-as-you-go), Amazon Bedrock, Google Vertex AI, and Microsoft Foundry ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Enforces organization policy through managed settings that take precedence over local developer configuration ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- `/status` command displays active managed settings source: `(remote)`, `(plist)`, `(HKLM)`, `(HKCU)`, or `(file)` ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Managed controls include permissions, sandboxing, MCP server restrictions, plugin marketplace restrictions, hook restrictions, and version floors ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- SSO, SCIM provisioning, and seat assignment are configured at the Claude account level, not within Claude Code itself ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Common login fixes: `/logout` then `/login` to switch accounts; `claude update` if enterprise auth option is missing; restart terminal after updating ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- On Team, Enterprise, API, and cloud provider plans, Anthropic does not train models on user code or prompts ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- The Agent SDK embeds Claude Code's autonomous agent loop in external applications as a standalone package, providing programmatic control over tools, permissions, cost limits, and output without requiring the CLI ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- The agent loop follows a cycle of receiving prompts, evaluating and calling tools, executing tools, and repeating until a final text-only response is produced ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- CLAUDE.md files load from multiple levels (project root, parent directories, child directories loaded on demand, local gitignored, user) and are all additive with no hard precedence rule; conflicts depend on how Claude interprets them ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Skills are on-demand markdown artifacts at `.claude/skills/<name>/SKILL.md` that advertise descriptions at startup and load full content only when relevant ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- The Agent SDK provides 18 hook events for intercepting agent behavior; Python supports 11 (missing SessionStart, SessionEnd, PostToolBatch, Setup, TeammateIdle, TaskCompleted, ConfigChange, WorktreeCreate, WorktreeRemove), while TypeScript supports all 18 ^[raw/document/claude code/claude-code-007-agent-sdk-hooks-2026-04-29.md]
- The SDK was renamed from "Claude Code SDK" to "Claude Agent SDK" to reflect broader agent-building capabilities beyond coding tasks; Claude Code docs now focus on the CLI tool and automation features while Agent SDK docs moved to the API Guide ^[raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- The CLI has OpenTelemetry instrumentation built in: it records spans around each model request and tool execution, emits metrics for token and cost counters, and emits structured log events for prompts and tool results ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Agent teams (experimental, disabled by default) coordinate multiple Claude Code instances with a lead session managing teammates via shared task lists and inter-agent messaging; requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and v2.1.32+ ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Provides analytics dashboards for Teams/Enterprise at `claude.ai/analytics/claude-code` and for API customers at `platform.claude.com/claude-code`; includes usage metrics, contribution metrics with GitHub integration, leaderboard, and CSV export ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Contribution metrics require installing the Claude GitHub app and enabling analytics at `claude.ai/admin-settings/claude-code`; not available for Zero Data Retention organizations or API customers ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- PR attribution matches Claude Code session activity against merged PR diffs within a 21-day-before to 2-day-after window; attributed PRs are labeled `claude-code-assisted` in GitHub ^[raw/document/claude code/claude-code-033-analytics-2026-04-29.md]
- Supports six authentication credential sources in precedence order: cloud provider credentials (Bedrock/Vertex/Foundry env vars), `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_API_KEY`, `apiKeyHelper` script, `CLAUDE_CODE_OAUTH_TOKEN`, and subscription OAuth from `/login` ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Credentials are stored in macOS Keychain (macOS) or `~/.claude/.credentials.json` (Linux/Windows); `CLAUDE_CONFIG_DIR` overrides the default location ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `apiKeyHelper` setting runs a shell script to return an API key (for vault/rotation integration), refreshing after 5 minutes or HTTP 401 by default; `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` customizes the interval ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `claude setup-token` generates a one-year OAuth token for CI/non-interactive environments; scoped to inference only, cannot establish Remote Control sessions; bare mode does not read it ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Auto mode eliminates permission prompts by routing tool calls through a classifier that blocks destructive or external actions; configured via `autoMode` settings block with `environment`, `allow`, and `soft_deny` fields read as natural-language rules ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- The champion kit provides a structured playbook for engineers advocating Claude Code internally: share reusable techniques (not outcomes), answer questions with actual prompts, and grow adoption through lightweight recurring habits (~40 min/week) ^[raw/document/claude code/claude-code-037-champion-kit-2026-04-29.md]
- Channels (research preview, v2.1.80+) are MCP server plugins that push external events into a running session, enabling two-way chat bridges with Telegram, Discord, and iMessage; enabled per session via `--channels` flag and gated on Team/Enterprise by `channelsEnabled` managed setting ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channel servers use stdio transport and the `@modelcontextprotocol/sdk` package; they declare `capabilities.experimental['claude/channel']` to register as channels and can optionally declare `capabilities.experimental['claude/channel/permission']` (v2.1.81+) for permission relay ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Custom channels require `--dangerously-load-development-channels` during the research preview; the bypass is per-entry and does not extend to `--channels` entries; `channelsEnabled` organization policy still applies ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Checkpointing automatically tracks file edits per user prompt; the rewind menu (Esc+Esc or `/rewind`) offers restore (code, conversation, or both) and targeted summarization; checkpoints persist across sessions and auto-clean after 30 days (configurable) ^[raw/document/claude code/claude-code-041-checkpointing-2026-04-29.md]
- Chrome integration (beta) connects to the Claude in Chrome browser extension for browser automation from the CLI or VS Code; requires extension v1.0.36+, Claude Code v2.0.73+, and a direct Anthropic plan; supports Chrome and Edge only, not Brave/Arc/WSL ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Chrome capabilities include live debugging, design verification, web app testing, authenticated web app interaction (shares browser login state), data extraction, task automation, and session recording as GIFs; pauses for manual CAPTCHA/login handling ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Enable Chrome via `claude --chrome` flag or `/chrome` command; setting it as default increases context usage since browser tools are always loaded ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Claude Code on the Web runs tasks on Anthropic-managed cloud VMs at claude.ai/code with session persistence, environment caching, and GitHub integration; `--remote` creates cloud sessions, `--teleport` pulls them locally ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Cloud sessions support auto-fix for PRs (watches CI failures and review comments), session sharing (Team/Public visibility), and environment configuration (network access levels, setup scripts, environment variables) ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Configuration is organized in the `.claude` directory (project scope) and `~/.claude` (global scope): CLAUDE.md for instructions, settings.json for permissions/hooks/env, skills/ for reusable prompts, agents/ for subagent definitions, output-styles/ for response formatting, and .mcp.json for MCP servers ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- Session data (transcripts, tool results, file snapshots) is stored as plaintext under `~/.claude/` and auto-cleaned after `cleanupPeriodDays` (default 30); transcripts are not encrypted at rest and OS file permissions are the only protection ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE.local.md` at project root (gitignored) holds private preferences alongside CLAUDE.md; `settings.local.json` (auto-gitignored) holds personal overrides ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- CLI commands include `claude` (interactive session), `claude auth login/logout/status` (authentication), `claude update` / `claude install` (version management), `claude mcp` (MCP configuration), `claude agents` (list subagents), `claude plugin` (plugin management), and `claude remote-control` (Remote Control server) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `claude setup-token` generates a long-lived OAuth token for CI and scripts; it prints the token to the terminal without saving it and requires a Claude subscription ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `claude ultrareview [target]` runs ultrareview non-interactively; prints findings to stdout and exits 0 on success or 1 on failure; supports `--json` for raw payload and `--timeout <minutes>` to override the 30-minute default ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--add-dir` grants file access to additional working directories but most `.claude/` configuration is not discovered from these directories ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--effort` sets the effort level for the current session (`low`, `medium`, `high`, `xhigh`, `max`); session-scoped and does not persist to settings ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--model` sets the model for the session using an alias (`sonnet`, `opus`) or full model name ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--setting-sources` controls which setting sources load (`user`, `project`, `local`), comma-separated ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--worktree` / `-w` starts Claude in an isolated git worktree at `<repo>/.claude/worktrees/<name>`; `--tmux` creates a tmux session for the worktree (uses iTerm2 native panes when available) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Code Review (research preview, Team/Enterprise) uses a fleet of specialized agents to analyze PR diffs in parallel, with a verification step to filter false positives; findings are posted as inline GitHub comments tagged by severity (Important, Nit, Pre-existing) ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Code Review averages $15-25 per review, scales with PR size and complexity, and is billed separately through extra usage; a monthly spend cap can be configured at `claude.ai/admin-settings/usage` ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Code Review is configured per repository with three trigger modes: once after PR creation, after every push, or manual only; manual triggers use `@claude review` or `@claude review once` as top-level PR comments ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Provides 50+ slash commands (type `/` to list) for session management, model switching, code review, permissions, and workflow automation; commands are either built-in (coded into the CLI) or bundled skills (prompt-based) ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- `/autofix-pr [prompt]` spawns a Claude Code on the Web session that watches the current branch's PR and pushes fixes for CI failures and review comments; accepts an optional prompt for custom instructions ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- `/batch <instruction>` decomposes large-scale changes into 5-30 independent units, spawning one background agent per unit in an isolated git worktree ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Plan Mode (`--permission-mode plan` or Shift+Tab) restricts Claude to read-only analysis and planning; accept a plan to switch to execution mode ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Extended thinking is enabled by default with adaptive reasoning on supported models; configure via `/effort`, `CLAUDE_CODE_EFFORT_LEVEL`, `MAX_THINKING_TOKENS`, or the `ultrathink` prompt keyword ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Worktrees (`claude --worktree <name>`) create isolated working directories for parallel sessions; `.worktreeinclude` specifies which gitignored files to copy to new worktrees ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Use `@` in prompts to reference files (`@file.js` includes full content), directories (`@src/components` provides listing), or MCP resources (`@server:resource`) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Notification hooks fire on `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`, `elicitation_complete`, and `elicitation_response` events ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Four scheduling approaches: Routines (Anthropic-managed), Desktop scheduled tasks (local), GitHub Actions (CI), and `/loop` (in-session polling) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Use `claude -p` as a unix-style utility for linting, code review, and piped workflows; supports `--output-format text/json/stream-json` for programmatic consumption ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- The communications kit provides copy-ready rollout materials: launch announcements in email and Slack/Teams formats, an executive sponsor variant, a pilot group variant, a champion recruitment DM, a tips-and-tricks drip campaign, FAQ responses, and prompt templates ^[raw/document/claude code/claude-code-049-communications-kit-2026-04-29.md:90-96]
- Computer use (research preview, macOS CLI only) lets Claude control the screen by opening apps, clicking, typing, and taking screenshots; enabled as the built-in `computer-use` MCP server via `/mcp`, requires Pro/Max plan and v2.1.85+, not available in non-interactive mode or on Team/Enterprise plans ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- `/context` shows a live breakdown of context usage by category with optimization suggestions ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- `/memory` displays which CLAUDE.md and auto memory files loaded at startup ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

## Related

- [[concepts/managed_settings]]
- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/context_window]]
- [[concepts/hooks]]
- [[concepts/setting_sources]]
- [[concepts/skills]]
- [[entities/open_telemetry]]
- [[concepts/observability]]
- [[concepts/agent_teams]]
- [[concepts/analytics]]
- [[concepts/pr_attribution]]
- [[concepts/authentication]]
- [[concepts/auto_mode]]
- [[entities/claude_console]]
- [[concepts/champion_kit]]
- [[concepts/communications_kit]]
- [[concepts/channels]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[entities/github]]
- [[concepts/file_checkpointing]]
- [[entities/chrome_extension]]
- [[concepts/browser_automation]]
- [[entities/claude_code_web]]
- [[concepts/cloud_environment]]
- [[concepts/network_access]]
- [[concepts/teleport]]
- [[concepts/auto_fix]]
- [[concepts/claude_directory]]
- [[concepts/application_data]]
- [[concepts/code_review]]
- [[concepts/commands]]
- [[concepts/plan_mode]]
- [[concepts/extended_thinking]]
- [[concepts/worktrees]]
- [[concepts/scheduled_tasks]]
- [[concepts/computer_use]]
- [[summaries/claude-code-common-workflows]]