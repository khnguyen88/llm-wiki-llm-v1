---
title: "Setting Sources"
summary: "Configuration mechanism in the Agent SDK that controls which filesystem-based settings (project, user, local) are loaded into an SDK agent session"
type: concept
sources:
  - raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md
  - raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md
  - raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md
  - raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md
  - raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md
  - raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
tags:
  - agent-sdk
  - claude-code
  - settings
  - configuration
  - isolation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Setting Sources

The `settingSources` option (`setting_sources` in Python, `settingSources` in TypeScript) controls which filesystem-based settings the Agent SDK loads into a session. It determines access to CLAUDE.md files, skills, hooks, permissions, and other project or user configuration. ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

## Key Points

- Three source types: `"project"` loads from `<cwd>/.claude/` and parent directories, `"user"` loads from `~/.claude/`, and `"local"` loads gitignored `CLAUDE.local.md` and `.claude/settings.local.json` ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Omitting `settingSources` defaults to `["user", "project", "local"]`; passing an empty array `[]` disables all filesystem-based settings ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Project source loads CLAUDE.md, `.claude/rules/*.md`, project skills, project hooks, and project `settings.json`; the search walks parent directories up to the filesystem root, stopping when a `.claude/` directory is found ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Three inputs are read regardless of `settingSources`: managed policy settings, `~/.claude.json` global config, and auto memory at `~/.claude/projects/<project>/memory/` ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Agent SDK v0.1.0 broke isolation by no longer loading settings by default; current releases have **reverted** this so that omitting `settingSources` once again loads `["user", "project", "local"]` matching the CLI ^[raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- Python SDK 0.1.59 and earlier treated an empty `setting_sources` list the same as omitting the option; upgrading the SDK is required before `setting_sources=[]` produces the intended isolated behavior ^[raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- CLAUDE.md loading is controlled by setting sources, not by the `claude_code` system prompt preset: `"project"` loads project-level CLAUDE.md and `"user"` loads `~/.claude/CLAUDE.md`; CLAUDE.md will not load if the corresponding source is omitted ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Output styles at `~/.claude/output-styles/` (user-level) and `.claude/output-styles/` (project-level) also load through setting sources; include `"user"` or `"project"` respectively to activate them ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- `.claude/settings.json` can declare allow, deny, and ask rules for permissions; these rules are read when the `project` setting source is enabled, which it is for default `query()` options ^[raw/document/claude code/claude-code-014-agent-sdk-permissions-2026-04-29.md]
- Skills are discovered through `settingSources`; if `"user"` or `"project"` is omitted, skills from `~/.claude/skills/` or `<cwd>/.claude/skills/` will not load — use the `plugins` option to load skills from a specific path instead ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- The auto mode classifier reads `autoMode` from four scopes: user settings (`~/.claude/settings.json`), local project settings (`.claude/settings.local.json`), managed settings, and inline JSON via `--settings` or Agent SDK — but deliberately excludes shared project `.claude/settings.json` to prevent repos from injecting their own allow rules ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- `settings.local.json` at project scope is auto-gitignored and holds personal overrides that should not be committed to git ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `.mcp.json` is project-scope only and holds team-shared MCP server configurations; it should be committed to git ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]
- `CLAUDE.local.md` at the project root holds private developer preferences and should be added to `.gitignore` ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Details

Setting sources provide the isolation boundary for SDK agents. Because managed policy settings, global config, and auto memory are always read regardless of `settingSources`, an SDK process can pick up host-level configuration and per-directory memory. For multi-tenant deployments, the recommended approach is to run each tenant in its own filesystem namespace and set `settingSources: []` combined with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in the `env` option. ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

The `cwd` option determines where the SDK searches for project settings. If neither `cwd` nor any of its parent directories contains a `.claude/` folder, project-level features will not load even when `settingSources` includes `"project"`. ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

To disable the always-read inputs: remove the managed settings file from the host, relocate `~/.claude.json` by setting `CLAUDE_CONFIG_DIR` in `env`, or disable auto memory by setting `autoMemoryEnabled: false` in settings or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env`. ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

Agent SDK v0.1.0 introduced a breaking change where settings sources were no longer loaded by default, motivated by CI/CD consistency, deployed application isolation, test reproducibility, and multi-tenant leak prevention. Current SDK releases have reverted this default for `query()`: omitting `settingSources` once again loads user, project, and local settings, matching the CLI. Pass `settingSources: []` (TypeScript) or `setting_sources=[]` (Python) to opt into the isolated behavior. Note that Python SDK 0.1.59 and earlier treated an empty list the same as omitting the option, so upgrading is required before `setting_sources=[]` functions as intended. ^[raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/managed_settings]]
- [[concepts/hooks]]
- [[concepts/skills]]
- [[concepts/system_prompt]]
- [[concepts/output_styles]]
- [[concepts/permissions]]
- [[concepts/auto_mode]]
- [[concepts/claude_directory]]