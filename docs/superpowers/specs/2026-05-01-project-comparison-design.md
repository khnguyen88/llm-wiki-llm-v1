# Design: Project Comparison & Origin Tracing Document

**Date**: 2026-05-01
**Status**: Draft

## Goal

Create `README-PROJECT-COMPARISON.md` at the project root that traces the origin of every major feature in this project back to its source(s), documents what was modified or omitted from each source, and highlights the project's own original contributions.

## Sources

| # | Source | Type | Key Contribution |
|---|--------|------|-------------------|
| 1 | Karpathy's LLM Wiki Gist | Gist/blog post | Foundational raw→wiki pipeline concept |
| 2 | Cole Medin's claude-memory-compiler | GitHub repo | daily→knowledge pipeline, hooks, flush system |
| 3 | Atomic Memory's llm-wiki-compiler | GitHub repo | Enhanced frontmatter, citations, lint rules |
| 4 | Josh Pocock's karpathy-obsidian-vault | GitHub repo | ai-research convention, Obsidian integration |

## Research Method

1. Clone all 3 GitHub repos into a temp directory
2. Fetch Karpathy's gist via WebFetch
3. Compare each source against the current project structure, schemas, hooks, scripts, tools, agents, lint system, and frontmatter
4. Delete temp repos after research
5. Synthesize findings into the comparison document

## Document Structure

### Part 1: Feature Matrix

Table with rows for each feature category and columns for each source + "This Project":

| Feature Category | Karpathy Gist | Cole Medin | Atomic Memory | Josh Pocock | This Project |
|---|---|---|---|---|---|
| Directory structure | ... | ... | ... | ... | ... |
| Schema concepts | ... | ... | ... | ... | ... |
| Hooks | ... | ... | ... | ... | ... |
| Scripts | ... | ... | ... | ... | ... |
| Tools | ... | ... | ... | ... | ... |
| Agents | ... | ... | ... | ... | ... |
| Lint system | ... | ... | ... | ... | ... |
| Frontmatter | ... | ... | ... | ... | ... |

### Part 2: Source Narratives

One subsection per source with:
- **Core concept adopted** — what was taken and how
- **What was modified** — how it was adapted
- **What was omitted** — what the source had that was dropped

### Part 3: Original Contributions

Features/concepts that none of the 4 sources had — purely this project's own additions:
- Dual KB architecture (external wiki + internal knowledge)
- 9 specialized agents
- Agent SDK-based batch scripts
- Sync-check agent
- Context-loader agent
- etc.

### Part 4: Key Modifications

Where this project significantly diverged from any source's approach:
- E.g., Cole Medin uses headless Claude CLI; this project uses Python Agent SDK
- E.g., Atomic Memory has a different lint set; this project expanded to 12+1 checks
- E.g., Josh Pocock uses raw Obsidian; this project has structured frontmatter and schemas

## Depth Level

Architectural & feature mapping — concept-level comparison, not line-by-line code diffs.

## Output

- File: `README-PROJECT-COMPARISON.md` at project root
- No git commit — user reviews and commits manually
- Temp repos deleted after research phase

## Scope Boundaries

- This is a documentation-only task — no code changes
- The comparison is for understanding lineage, not for judging source quality
- The document will help inform future template finalization work on a separate branch