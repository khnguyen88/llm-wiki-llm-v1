---
title: "Skills"
summary: "Markdown files that give Agent SDK agents specialized knowledge and invocable workflows, loaded on demand rather than at every session start"
type: concept
sources:
  - raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md
  - raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md
  - raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md
  - raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-051-context-window-2026-04-29.md
tags:
  - agent-sdk
  - claude-code
  - skills
  - extensibility
  - on-demand
  - compaction
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Skills

Skills are markdown files that give agents specialized knowledge and invocable workflows. Unlike CLAUDE.md (which loads every session), skills load on demand: the agent receives skill descriptions at startup and loads the full content only when relevant. ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

## Key Points

- Skills are discovered from the filesystem through [[concepts/setting_sources|settingSources]]; with default options, user and project skills load automatically ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- The `Skill` tool is enabled by default when `allowedTools` is not specified; when using an allowlist, `"Skill"` must be included explicitly ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Skills must be created as filesystem artifacts at `.claude/skills/<name>/SKILL.md`; there is no programmatic API for registering skills ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Skills serve two purposes: providing reference material the agent loads when relevant, and defining reusable workflows (deploy, review, release) ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Plugin skills are automatically namespaced with the plugin name as `plugin-name:skill-name` when invoked as slash commands to prevent naming conflicts between plugins ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugin skills require a `SKILL.md` file in their own subdirectory under `skills/` (e.g., `skills/my-skill/SKILL.md`) ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- The `allowed-tools` frontmatter field in SKILL.md does not apply when using Skills through the SDK; tool access is controlled via the main `allowedTools` option instead ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Unlike subagents (which can be defined programmatically), Skills must be created as filesystem artifacts; the SDK does not provide a programmatic API for registering Skills ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Three skill location types in the SDK: project skills (`.claude/skills/`, shared via git when `"project"` in settingSources), user skills (`~/.claude/skills/`, personal when `"user"` in settingSources), and plugin skills (bundled with installed plugins) ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Skills are model-invoked: Claude autonomously chooses when to use them based on context, rather than requiring explicit user invocation ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Without a `canUseTool` callback, any tool not in the `allowedTools` list is denied; this is how tool access for Skills is controlled in SDK applications ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Skills supersede the legacy `.claude/commands/` slash command format; the recommended `.claude/skills/<name>/SKILL.md` format supports both slash-command invocation (`/name`) and autonomous invocation by Claude ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- Use `disable-model-invocation: true` in SKILL.md frontmatter for workflows with side effects that should only be triggered manually by the user ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Skills are preferred over CLAUDE.md for domain knowledge or workflows that are only relevant sometimes; Claude loads skills on demand without bloating every conversation ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Create a skill by adding a directory with a `SKILL.md` to `.claude/skills/`; invoke directly with `/skill-name` ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- After compaction, invoked skill bodies are re-injected, but capped at 5,000 tokens per skill and 25,000 tokens total; when the total budget is exceeded, the oldest invoked skills are dropped first ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Truncation of skill bodies after compaction preserves the start of the file, so important instructions should be placed near the top of `SKILL.md` ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Legacy `.claude/commands/` custom slash commands are still supported by the CLI and support frontmatter (`description`, `allowed-tools`, `model`, `argument-hint`), dynamic arguments, bash execution, and file references ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]

## Details

Skills differ from CLAUDE.md instructions in their loading behavior. CLAUDE.md files are loaded into every session, consuming context window space regardless of relevance. Skills are advertised by description at startup and their full content is fetched only when the agent determines they are relevant to the current task. This on-demand loading makes skills more context-efficient for specialized knowledge that is not needed in every session. ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

In the SDK, Skills differ from subagents in a key architectural way: subagents can be defined programmatically via `AgentDefinition`, but Skills must be created as filesystem artifacts (`SKILL.md` files). The SDK does not provide a programmatic API for registering Skills. This means Skills require filesystem access and proper `settingSources` configuration to be discoverable, whereas subagents can be instantiated purely in code. ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]

A notable SDK-specific constraint is that the `allowed-tools` frontmatter field in SKILL.md is only supported when using Claude Code CLI directly. When using Skills through the SDK, tool access is controlled entirely through the main `allowedTools` option in the query configuration. Without a `canUseTool` callback, any tool not in the `allowedTools` list is denied, so SDK applications must pre-approve the specific tools their Skills need. ^[raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/setting_sources]]
- [[concepts/agent_loop]]
- [[concepts/plugins]]
- [[concepts/subagents]]
- [[concepts/context_window]]
- [[summaries/claude-code-best-practices]]