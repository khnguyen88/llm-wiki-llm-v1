---
title: "Claude Code Agent Sdk Skills"
summary: "How Agent Skills work within the Agent SDK: filesystem-based discovery, settingSources dependency, tool access restrictions, and troubleshooting"
type: summary
sources:
  - raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md
tags:
  - agent-sdk
  - skills
  - setting-sources
  - allowed-tools
  - filesystem
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Skills

## Key Points

- Skills are filesystem artifacts created as `SKILL.md` files; there is no programmatic API for registering Skills in the SDK ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Skills are discovered through `settingSources`/`setting_sources`; including `"user"` or `"project"` enables skill discovery from `~/.claude/skills/` and `<cwd>/.claude/skills/` respectively ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- The `"Skill"` tool must be included in `allowedTools` to enable Skills ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- The `allowed-tools` frontmatter field in SKILL.md does not apply when using Skills through the SDK; tool access is controlled via the main `allowedTools` option instead ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Three skill location types: project skills (`.claude/skills/`, shared via git), user skills (`~/.claude/skills/`, personal across projects), and plugin skills ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Skill metadata is discovered at startup; full content is loaded only when Claude determines the skill is relevant ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- Unlike subagents (which can be defined programmatically), Skills must be created as filesystem artifacts ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]

## Quotes

- "The `allowed-tools` frontmatter field in SKILL.md is only supported when using Claude Code CLI directly. It does not apply when using Skills through the SDK." ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]

## Notes

- Troubleshooting common issues: Skills not found → check `settingSources` includes `"user"` or `"project"` and `cwd` points to a directory containing `.claude/skills/`; Skill not used → confirm `"Skill"` is in `allowedTools` and the skill description includes relevant keywords ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]
- The `plugins` option can load skills from a specific path when `settingSources` is set explicitly ^[001a-raw/document/claude code/claude-code-020-agent-sdk-skills-2026-04-29.md]

## Related

- [[004-wiki/entities/agent-sdk]]
- [[004-wiki/concepts/skills]]
- [[004-wiki/concepts/setting-sources]]
- [[004-wiki/concepts/subagents]]
- [[004-wiki/concepts/plugins]]
- [[004-wiki/concepts/permissions]]