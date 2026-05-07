# Web Search & AI Research Agents Design

**Date**: 2026-05-06
**Status**: Approved

## Overview

Add two new agents to the wiki project:

- **web-search** — Ephemeral web search using the Vane API. Returns results to the caller without saving files.
- **ai-research** — Persistent deep research that saves results to `ai-research/web/`, lints, and runs sync-check.

Also update **wiki-query** to suggest web-search or ai-research when the KB has gaps, and update all supporting project files for consistency.

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Architecture | Two separate agents (Approach A) | Clean separation of concerns; each agent does one job; independently invokable |
| web-search depth | Shallow by default, optional deep | Quick lookups are common; deep dive only when needed |
| ai-research depth | Always deep | Persistent research should be thorough |
| Update strategy | Prune then replace | Clean, no contradictions, no stale content; latest research replaces previous |
| wiki-query delegation | Ask first, then invoke | User controls when external searches happen |
| File location | Always `ai-research/web/` | Simple, consistent, matches vane `--save` behavior and existing schema |
| File naming | `{slug}-{YYYY-MM-DD}.md` | Follows existing schema convention; slug derived from query |

## Agent 1: web-search

**File**: `.claude/agents/web-search.md`

**Role**: You are the **Web Search Agent** — responsible for performing web searches using the Vane API and returning synthesized results to the caller.

### Operations

1. **Get providers** — Run `vane_get_providers` to fetch available provider IDs and model keys. Select the best available chat model (prefer `gemma4:31b-cloud`) and embedding model (prefer `mixedbread-ai/mxbai-embed-large-v1` from Transformers provider).

2. **Search** (shallow, default) — Run `vane_web_search` with the user's query. Present the full output verbatim — schema header, message body, and Sources section. No summarization, no reformatting.

3. **Deep search** (optional) — After vane returns results, identify the top 3-5 source URLs with the most relevant content. Use crawl4ai MCP tool to fetch full page content from each. Present the vane synthesis first, then append `## Deep Dive` sections with the crawled content for each URL.

### Key Principles

- Never save files — this agent is ephemeral, it returns results to the caller
- Always present vane output verbatim per the tool description
- The caller (wiki-query, ai-research, or the user) decides what to do with the results
- No file I/O, no persistence, no side effects

## Agent 2: ai-research

**File**: `.claude/agents/ai-research.md`

**Role**: You are the **AI Research Agent** — responsible for performing deep web research and persisting results as wiki source files in `ai-research/web/`.

### Operations

1. **Check existing** — Check if `ai-research/web/` already has a file for this topic (match by slug). If found, prune it — delete the old file before starting fresh.

2. **Deep search** — Execute the deep search: get providers → run `vane_web_search` → crawl top 3-5 source URLs via crawl4ai. Always deep, never shallow.

3. **Save to ai-research** — Write the result to `ai-research/web/{slug}-{YYYY-MM-DD}.md` using the `--save` flag on `vane_web_search` (which creates the file with HTML comment metadata header + message body + Sources section). Then:
   - **Add YAML frontmatter** at the very top of the file (before the HTML comment header). The file will have both: YAML frontmatter (wiki page metadata) and HTML comment metadata header (provenance metadata per WIKI_SCHEMA.md).
   - **Append deep-dive content** from crawl4ai after the Sources section.

   The YAML frontmatter should be:

   ```yaml
   ---
   title: "<Human-readable title from query or summarized version>"
   summary: "<1-2 sentence summary of what was researched>"
   type: ai-research-multi
   sources:
     - ai-research/web/{filename}
   tags: [<relevant tags>]
   created: "<ISO 8601 timestamp>"
   updated: "<ISO 8601 timestamp>"
   ---
   ```

4. **Lint** — Run `uv run python scripts/lint.py` to validate the saved file.

5. **Sync-check** — Invoke the sync-check agent to verify cross-file consistency after changes.

### Title Naming

- Use the user's query as the title if it's under ~80 characters
- If longer, summarize to a concise descriptive title
- The slug (for filename) is derived by the existing `slugify()` in `vane_web_search.py`

### Prune-and-Replace Rule

When re-researching an existing topic, the old file is deleted and replaced entirely. No archiving, no version history. The latest research replaces the previous.

### Key Principles

- Always deep — crawl4ai follow-up is mandatory, not optional
- Always save to `ai-research/web/` — this agent exists to persist research
- Always lint after saving
- Always run sync-check after changes
- Prune-then-replace on re-research, never append

## Agent 3: wiki-query Changes

**File**: `.claude/agents/wiki-query.md` (modify existing)

### New Section: Gap Filling

When wiki-query cannot answer a question from the existing KB and the gap could be filled by web research:

1. **Detect the gap** — After reading all relevant pages, if the answer is incomplete or missing, explicitly state: "The knowledge base doesn't have enough information to fully answer this question about [topic]."

2. **Ask the user** — Present the option: "I could search the web for this. Which would you like?"
   - **Quick search** — Invoke the `web-search` agent for ephemeral results (no saving)
   - **Deep research** — Invoke the `ai-research` agent for persistent results (saves to ai-research/, then can be ingested into wiki/)

3. **Wait for approval** — Do NOT invoke either agent without explicit user approval.

4. **After research** — If ai-research was used, the saved source can then be ingested into wiki/ via the `wiki-maintainer` agent using the standard Ingest workflow.

### Guideline Update

Change the existing guideline from:

> If the KB doesn't have enough to answer, say so and suggest sources to ingest from `raw/` or `ai-research/`

To:

> If the KB doesn't have enough to answer, say so and offer to invoke the `web-search` agent (quick, ephemeral) or `ai-research` agent (deep, saves to KB), or suggest ingesting from existing `raw/` or `ai-research/` sources

## Supporting File Updates

### CLAUDE.md

Add two rows to the Project Agents table:

| Agent | When to invoke |
|-------|---------------|
| `web-search` | "Search the web for X", "Quick fact-check on X" |
| `ai-research` | "Research X and save it", "Deep research on X" |

### schema/WIKI_AGENTS.md

Add two entries describing the new agent roles (web-search as ephemeral search layer, ai-research as persistent deep research layer). Update the Research Workflow section to reference both agents as named operations.

### schema/WIKI_WORKFLOWS.md

Add two new workflow definitions:

**Search Workflow** (3-4 steps):
1. Get providers via `vane_get_providers`
2. Run vane search with `vane_web_search`
3. (Optional) Deep-dive via crawl4ai on top source URLs
4. Return results to caller

**Deep Research Workflow** (5-6 steps):
1. Check existing files in `ai-research/web/` for the same topic
2. Deep search via vane + crawl4ai
3. Save to `ai-research/web/{slug}-{YYYY-MM-DD}.md` with frontmatter
4. Lint via `uv run python scripts/lint.py`
5. Sync-check via sync-check agent

### schema/WIKI_SCHEMA.md

No changes needed. The `ai-research-multi` source type, file naming convention, slugify behavior, and frontmatter format already exist in the schema.

### AGENTS.md

Add web-search and ai-research to the Core Operations section and the Full Project Structure agent list.

### .claude/agents/context-loader.md

Add two rows to the lookup table:

| Need | Load from |
|------|-----------|
| Quick web search | `.claude/agents/web-search.md` |
| Deep web research + save | `.claude/agents/ai-research.md` |

### .claude/agents/sync-check.md

Add `web-search.md` and `ai-research.md` to the Files to Read checklist.

### Scripts

No changes needed. `vane_web_search.py` already has `--save` support. `lint.py`, `compile.py`, and other scripts don't need modifications.

## Files to Create

1. `.claude/agents/web-search.md` — New agent file
2. `.claude/agents/ai-research.md` — New agent file

## Files to Modify

1. `.claude/agents/wiki-query.md` — Add gap-filling section, update guideline
2. `.claude/agents/context-loader.md` — Add lookup table entries
3. `.claude/agents/sync-check.md` — Add files to checklist
4. `CLAUDE.md` — Add agent table rows
5. `schema/WIKI_AGENTS.md` — Add agent descriptions, update Research Workflow
6. `schema/WIKI_WORKFLOWS.md` — Add Search and Deep Research workflows
7. `AGENTS.md` — Add agents to operations and project structure