---
title: "Claude Code Skills"
summary: "Skills extend Claude Code's capabilities with on-demand markdown instructions, configurable via frontmatter, supporting automatic invocation, subagent execution, and dynamic context injection"
type: summary
sources:
  - raw/document/claude code/claude-code-103-skills-2026-04-29.md
tags:
  - skills
  - claude-code
  - extensibility
  - slash-commands
  - frontmatter
  - subagents
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Skills

Skills extend what Claude Code can do by providing markdown-based instructions that load on demand rather than consuming context every session. A skill is a directory containing a `SKILL.md` file with YAML frontmatter and markdown instructions. The directory name becomes the `/slash-command`, and frontmatter controls when and how Claude invokes it. Custom commands have been merged into skills; both `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` create `/deploy` and work the same way, though skills add optional features like supporting files and frontmatter. Skills follow the Agent Skills open standard (agentskills.io), which works across multiple AI tools. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Skill Locations and Precedence

| Location | Path | Scope |
|---|---|---|
| Enterprise | See managed settings | All users in organization |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All user's projects |
| Project | `.claude/skills/<name>/SKILL.md` | Current project only |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin is enabled |

When skills share the same name across levels, enterprise overrides personal, and personal overrides project. Plugin skills use a `plugin-name:skill-name` namespace, so they cannot conflict with other levels. If a skill and a legacy command share the same name, the skill takes precedence. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

Claude Code watches skill directories for file changes; additions, edits, and removals take effect within the current session without restarting. Creating a new top-level skills directory that did not exist at session start requires a restart. Skills are automatically discovered from nested `.claude/skills/` directories when working in subdirectories, supporting monorepo setups. The `--add-dir` flag loads skills from `.claude/skills/` within added directories, but not other `.claude/` configuration. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Frontmatter Configuration

Skills support extensive YAML frontmatter for controlling behavior, invocation, and execution context. All fields are optional; only `description` is recommended.

| Field | Purpose |
|---|---|
| `name` | Display name; defaults to directory name. Lowercase, hyphens, max 64 chars |
| `description` | What the skill does and when to use it. Truncated at 1,536 chars in the skill listing |
| `when_to_use` | Additional trigger context; appended to `description` and counts toward the 1,536-char cap |
| `argument-hint` | Hint shown during autocomplete (e.g., `[issue-number]`) |
| `arguments` | Named positional arguments for `$name` substitution |
| `disable-model-invocation` | Set `true` to prevent Claude from auto-loading; user must invoke with `/name` |
| `user-invocable` | Set `false` to hide from `/` menu; background knowledge only |
| `allowed-tools` | Tools Claude can use without approval while skill is active |
| `model` | Model override for the current turn; accepts same values as `/model` or `inherit` |
| `effort` | Effort level override (`low`, `medium`, `high`, `xhigh`, `max`) |
| `context` | Set to `fork` to run in isolated subagent context |
| `agent` | Subagent type when `context: fork` (e.g., `Explore`, `Plan`, `general-purpose`, or custom) |
| `hooks` | Hooks scoped to this skill's lifecycle |
| `paths` | Glob patterns limiting when the skill activates |
| `shell` | Shell for `!`command`` blocks (`bash` default or `powershell`) |

^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Invocation Control

Two frontmatter fields control who can invoke a skill and how descriptions load into context:

| Frontmatter | User can invoke | Claude can invoke | When loaded into context |
|---|---|---|---|
| (default) | Yes | Yes | Description always in context; full content loads when invoked |
| `disable-model-invocation: true` | Yes | No | Description not in context; full content loads on user invocation |
| `user-invocable: false` | No | Yes | Description always in context; full content loads when invoked |

^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

Skill access can be restricted via permission rules: deny `Skill` entirely in `/permissions`, allow specific skills with `Skill(name)`, or deny with `Skill(name *)`. The `user-invocable` field only controls menu visibility, not programmatic access; use `disable-model-invocation: true` to block Claude from invoking. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## String Substitutions

| Variable | Description |
|---|---|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` | Access argument by 0-based index |
| `$N` | Shorthand for `$ARGUMENTS[N]` |
| `$name` | Named argument declared in `arguments` frontmatter |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_EFFORT}` | Current effort level |
| `${CLAUDE_SKILL_DIR}` | Directory containing the skill's `SKILL.md` |

If `$ARGUMENTS` is not present in the skill content, arguments are appended as `ARGUMENTS: <value>`. Indexed arguments use shell-style quoting: `/my-skill "hello world" second` makes `$0` expand to `hello world` and `$1` to `second`. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Dynamic Context Injection

The `` !`command` `` syntax runs shell commands before skill content is sent to Claude, replacing the placeholder with actual output. This is preprocessing, not something Claude executes. For multi-line commands, use a fenced code block opened with `` ```! ``. To disable shell execution for user/project/plugin/additional-directory sources, set `"disableSkillShellExecution": true` in settings; bundled and managed skills are not affected. Including the word "ultrathink" in skill content enables extended thinking for that invocation. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Subagent Execution

Setting `context: fork` runs a skill in an isolated subagent. The skill content becomes the task prompt, and the subagent has no access to conversation history. The `agent` field selects the subagent type. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

| Approach | System prompt | Task | Also loads |
|---|---|---|---|
| Skill with `context: fork` | From agent type | SKILL.md content | CLAUDE.md |
| Subagent with `skills` field | Subagent's markdown body | Claude's delegation message | Preloaded skills + CLAUDE.md |

^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Skill Content Lifecycle and Compaction

When invoked, the rendered `SKILL.md` content enters the conversation as a single message and stays for the rest of the session. Claude Code does not re-read the skill file on later turns. During auto-compaction, invoked skills are re-attached after the summary: the first 5,000 tokens of each skill, with a combined budget of 25,000 tokens, filled starting from the most recently invoked skill. Older skills can be dropped entirely after compaction. If a skill seems to stop influencing behavior after the first response, strengthening the `description` and instructions or re-invoking after compaction can help. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Supporting Files

Skills can include multiple files in their directory: templates, examples, scripts, and reference documentation. Reference supporting files from `SKILL.md` so Claude knows what each file contains and when to load it. Keep `SKILL.md` under 500 lines and move detailed reference material to separate files. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Bundled Skills

Claude Code includes bundled skills available in every session: `/simplify`, `/batch`, `/debug`, `/loop`, and `/claude-api`. Unlike most built-in commands (which execute fixed logic), bundled skills are prompt-based: they give Claude a detailed playbook and let it orchestrate work using its tools. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Key Quotes

> "Unlike CLAUDE.md content, a skill's body loads only when it's used, so long reference material costs almost nothing until you need it." ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

> "Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way." ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

> "Keep SKILL.md under 500 lines. Move detailed reference material to separate files." ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

> "Skill descriptions are loaded into context so Claude knows what's available, but if you have many skills, descriptions are shortened to fit the character budget, which can strip the keywords Claude needs to match your request." ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Notes

- Skills can generate visual output by bundling scripts that produce interactive HTML files (e.g., codebase visualizers, dependency graphs, test coverage reports). ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Skills can be shared at project scope (commit `.claude/skills/`), as plugins (with a `skills/` directory), or organization-wide via managed settings. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- The description context budget scales at 1% of the context window with an 8,000-character fallback, adjustable via `SLASH_COMMAND_TOOL_CHAR_BUDGET`. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]
- Troubleshooting: if a skill doesn't trigger, check that the description includes keywords users would say; if it triggers too often, make the description more specific or add `disable-model-invocation: true`. ^[raw/document/claude code/claude-code-103-skills-2026-04-29.md]

## Related

- [[concepts/skills]]
- [[entities/claude_code]]
- [[concepts/subagents]]
- [[concepts/plugins]]
- [[concepts/managed_settings]]
- [[concepts/context_window]]
- [[concepts/commands]]
- [[concepts/extended_thinking]]
- [[concepts/permissions]]