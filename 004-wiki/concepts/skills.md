---
title: "Skills"
summary: "Markdown files that give agents specialized knowledge and invocable workflows, loaded on demand rather than at every session start, following the Agent Skills open standard with configurable frontmatter for invocation control, subagent execution, and dynamic context"
type: concept
sources:
  - raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md
  - raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md
  - raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md
  - raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-051-context-window-2026-04-29.md
  - raw/document/claude code/claude-code-103-skills-2026-04-29.md
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
tags:
  - agent-sdk
  - claude-code
  - skills
  - extensibility
  - on-demand
  - compaction
  - frontmatter
  - slash-commands
  - agent-skills-standard
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Skills

Skills are markdown files that give agents specialized knowledge and invocable workflows. Unlike CLAUDE.md (which loads every session), skills load on demand: the agent receives skill descriptions at startup and loads the full content only when relevant. Skills follow the Agent Skills open standard (agentskills.io), which works across multiple AI tools; Claude Code extends it with invocation control, subagent execution, and dynamic context injection. ^[001a-raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md] ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Key Points

- Custom commands have been merged into skills; both `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` create `/deploy` and work the same way, though skills add optional features like supporting files and frontmatter ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Skills follow the Agent Skills open standard (agentskills.io); Claude Code extends it with invocation control, subagent execution, and dynamic context injection ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Bundled skills (/simplify, /batch, /debug, /loop, /claude-api) are prompt-based rather than fixed-logic, giving Claude a playbook to orchestrate work ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Skill locations follow a precedence hierarchy: enterprise overrides personal, personal overrides project; plugin skills use `plugin-name:skill-name` namespace to avoid conflicts ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Claude Code watches skill directories for file changes; edits take effect within the session without restarting, though creating a new top-level skills directory requires a restart ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Skills are automatically discovered from nested `.claude/skills/` directories when working in subdirectories (monorepo support), and from `.claude/skills/` within `--add-dir` directories ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- The `user-invocable: false` frontmatter hides a skill from the `/` menu but does not block programmatic Skill tool access; `disable-model-invocation: true` is required to block Claude from invoking ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Skills support string substitutions: `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N` for positional access, `$name` for named arguments, and `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}` for dynamic values ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- The `` !`command` `` syntax (dynamic context injection) runs shell commands before skill content is sent to Claude, replacing placeholders with actual output; disabled with `"disableSkillShellExecution": true` in settings ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Setting `context: fork` runs a skill in an isolated subagent where the SKILL.md content becomes the task prompt, with the `agent` field selecting the subagent type ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Each skill's combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing; the total description context budget scales at 1% of the context window with an 8,000-character fallback, adjustable via `SLASH_COMMAND_TOOL_CHAR_BUDGET` ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Skills are discovered from the filesystem through [[004-wiki/concepts/setting-sources|settingSources]]; with default options, user and project skills load automatically ^[001a-raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- The `Skill` tool is enabled by default when `allowedTools` is not specified; when using an allowlist, `"Skill"` must be included explicitly ^[001a-raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Skills must be created as filesystem artifacts at `.claude/skills/<name>/SKILL.md`; there is no programmatic API for registering skills ^[001a-raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Skills serve two purposes: providing reference material the agent loads when relevant, and defining reusable workflows (deploy, review, release) ^[001a-raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- Plugin skills are automatically namespaced with the plugin name as `plugin-name:skill-name` when invoked as slash commands to prevent naming conflicts between plugins ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugin skills require a `SKILL.md` file in their own subdirectory under `skills/` (e.g., `skills/my-skill/SKILL.md`) ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- The `allowed-tools` frontmatter field in SKILL.md does not apply when using Skills through the SDK; tool access is controlled via the main `allowedTools` option instead ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Unlike subagents (which can be defined programmatically), Skills must be created as filesystem artifacts; the SDK does not provide a programmatic API for registering Skills ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Three skill location types in the SDK: project skills (`.claude/skills/`, shared via git when `"project"` in settingSources), user skills (`~/.claude/skills/`, personal when `"user"` in settingSources), and plugin skills (bundled with installed plugins) ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Skills are model-invoked: Claude autonomously chooses when to use them based on context, rather than requiring explicit user invocation ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Without a `canUseTool` callback, any tool not in the `allowedTools` list is denied; this is how tool access for Skills is controlled in SDK applications ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Skills supersede the legacy `.claude/commands/` slash command format; the recommended `.claude/skills/<name>/SKILL.md` format supports both slash-command invocation (`/name`) and autonomous invocation by Claude ^[001a-raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- Use `disable-model-invocation: true` in SKILL.md frontmatter for workflows with side effects that should only be triggered manually by the user ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Skills are preferred over CLAUDE.md for domain knowledge or workflows that are only relevant sometimes; Claude loads skills on demand without bloating every conversation ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Create a skill by adding a directory with a `SKILL.md` to `.claude/skills/`; invoke directly with `/skill-name` ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- After compaction, invoked skill bodies are re-injected, but capped at 5,000 tokens per skill and 25,000 tokens total; when the total budget is exceeded, the oldest invoked skills are dropped first ^[001a-raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Claude can discover and run built-in commands (such as `/init`, `/review`, and `/security-review`) via the Skill tool ^[001a-raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Truncation of skill bodies after compaction preserves the start of the file, so important instructions should be placed near the top of `SKILL.md` ^[001a-raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Legacy `.claude/commands/` custom slash commands are still supported by the CLI and support frontmatter (`description`, `allowed-tools`, `model`, `argument-hint`), dynamic arguments, bash execution, and file references ^[001a-raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]

## Details

Skills differ from CLAUDE.md instructions in their loading behavior. CLAUDE.md files are loaded into every session, consuming context window space regardless of relevance. Skills are advertised by description at startup and their full content is fetched only when the agent determines they are relevant to the current task. This on-demand loading makes skills more context-efficient for specialized knowledge that is not needed in every session. ^[001a-raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]

In the SDK, Skills differ from subagents in a key architectural way: subagents can be defined programmatically via `AgentDefinition`, but Skills must be created as filesystem artifacts (`SKILL.md` files). The SDK does not provide a programmatic API for registering Skills. This means Skills require filesystem access and proper `settingSources` configuration to be discoverable, whereas subagents can be instantiated purely in code. ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]

A notable SDK-specific constraint is that the `allowed-tools` frontmatter field in SKILL.md is only supported when using Claude Code CLI directly. When using Skills through the SDK, tool access is controlled entirely through the main `allowedTools` option in the query configuration. Without a `canUseTool` callback, any tool not in the `allowedTools` list is denied, so SDK applications must pre-approve the specific tools their Skills need. ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]

### Invocation Control

Two frontmatter fields control who can invoke a skill and how descriptions load into context:

| Frontmatter | User can invoke | Claude can invoke | When loaded into context |
|---|---|---|---|
| (default) | Yes | Yes | Description always in context; full content loads when invoked |
| `disable-model-invocation: true` | Yes | No | Description not in context; full content loads on user invocation |
| `user-invocable: false` | No | Yes | Description always in context; full content loads when invoked |

^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]

In a regular session, skill descriptions are loaded into context so Claude knows what is available, but full content only loads when invoked. Subagents with preloaded skills work differently: the full skill content is injected at startup. ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]

### String Substitutions

Skills support string substitution for dynamic values in their content:

| Variable | Description |
|---|---|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` | Access argument by 0-based index |
| `$N` | Shorthand for `$ARGUMENTS[N]` |
| `$name` | Named argument declared in `arguments` frontmatter |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_EFFORT}` | Current effort level |
| `${CLAUDE_SKILL_DIR}` | Directory containing the skill's SKILL.md |

If `$ARGUMENTS` is not present in the content, arguments are appended as `ARGUMENTS: <value>`. Indexed arguments use shell-style quoting. ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]

### Dynamic Context Injection

The `` !`command` `` syntax runs shell commands before skill content is sent to Claude. The command output replaces the placeholder, so Claude receives actual data, not the command itself. This is preprocessing, not something Claude executes. For multi-line commands, use a fenced code block opened with `` ```! ``. To disable this behavior for user/project/plugin/additional-directory sources, set `"disableSkillShellExecution": true` in settings; bundled and managed skills are not affected. Including the word "ultrathink" in skill content enables extended thinking for that invocation. ^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]

### Subagent Execution

Setting `context: fork` in frontmatter runs a skill in an isolated subagent context where the skill content becomes the task prompt. The subagent has no access to conversation history. The `agent` field selects the subagent type (`Explore`, `Plan`, `general-purpose`, or custom agents from `.claude/agents/`). This contrasts with the inverse pattern (subagents with `skills` field), where the subagent's markdown body is the system prompt and Claude's delegation message is the task:

| Approach | System prompt | Task | Also loads |
|---|---|---|---|
| Skill with `context: fork` | From agent type | SKILL.md content | CLAUDE.md |
| Subagent with `skills` field | Subagent's markdown body | Claude's delegation message | Preloaded skills + CLAUDE.md |

^[001a-raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Related

- [[004-wiki/entities/agent-sdk]]
- [[004-wiki/entities/claude-code]]
- [[004-wiki/concepts/setting-sources]]
- [[004-wiki/concepts/agent-loop]]
- [[004-wiki/concepts/plugins]]
- [[004-wiki/concepts/subagents]]
- [[004-wiki/concepts/context-window]]
- [[004-wiki/concepts/permissions]]
- [[004-wiki/concepts/extended-thinking]]
- [[004-wiki/concepts/commands]]
- [[004-wiki/summaries/claude-code-best-practices]]
- [[004-wiki/summaries/claude-code-skills]]