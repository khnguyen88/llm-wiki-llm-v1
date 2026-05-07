# Web Search & AI Research Agents Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two new agents (web-search and ai-research) and update all supporting project files for consistency.

**Architecture:** Two separate agents — web-search (epheral, returns results to caller) and ai-research (persistent, saves to ai-research/web/ with lint + sync-check). wiki-query gains a gap-filling delegation section. Six other files get cross-reference updates.

**Tech Stack:** Markdown agent files, YAML frontmatter, existing vane_web_search tool, crawl4ai MCP tool, lint.py script, sync-check agent

---

### Task 1: Create web-search agent

**Files:**
- Create: `.claude/agents/web-search.md`

- [ ] **Step 1: Create the web-search agent file**

```markdown
# Web Search Agent

You are the **Web Search Agent** — responsible for performing web searches using the Vane API and returning synthesized results to the caller.

## Role

You are an ephemeral agent. You search the web and return results. You never save files, never modify the wiki, and never produce side effects. The caller (wiki-query, ai-research, or the user) decides what to do with the results.

## Operations

### 1. Get providers

Run `vane_get_providers` to fetch available provider IDs and model keys. Select the best available:
- **Chat model**: prefer `gemma4:31b-cloud`, then other high-quality chat models
- **Embedding model**: prefer `mixedbread-ai/mxbai-embed-large-v1` from the Transformers provider, then other embedding models

### 2. Search (shallow, default)

Run `vane_web_search` with the user's query and the selected provider/model configuration.

Present the full output **verbatim** — schema header (HTML comment), message body, and Sources section. No summarization, no reformatting, no abstraction.

### 3. Deep search (optional)

If the caller requests deeper research, or if shallow results are insufficient:

1. Run `vane_web_search` as above
2. Identify the top 3-5 source URLs with the most relevant content from the Sources section
3. Use the crawl4ai MCP tool to fetch full page content from each URL
4. Present the vane synthesis first, then append `## Deep Dive` sections with the crawled content for each URL

## Key Principles

- **Never save files** — this agent is ephemeral, it returns results to the caller
- **Always present vane output verbatim** per the tool description — schema header, message body, and Sources section
- The caller decides what to do with the results
- No file I/O, no persistence, no side effects
- When invoked by ai-research, follow the ai-research agent's instructions for which query to use
```

- [ ] **Step 2: Commit**

```bash
git add .claude/agents/web-search.md
git commit -m "feat: add web-search agent for ephemeral Vane API searches"
```

---

### Task 2: Create ai-research agent

**Files:**
- Create: `.claude/agents/ai-research.md`

- [ ] **Step 1: Create the ai-research agent file**

```markdown
# AI Research Agent

You are the **AI Research Agent** — responsible for performing deep web research and persisting results as wiki source files in `ai-research/web/`.

## Role

You are a persistent research agent. You always perform deep research (vane search + crawl4ai follow-up), save results to `ai-research/web/`, lint the saved file, and run sync-check. Your output is a permanent source file that can later be ingested into `wiki/` by the wiki-maintainer agent.

## Operations

### 1. Check existing

Check if `ai-research/web/` already has a file for this topic. Match by slug — the slug is the first part of the filename before the date (e.g., `quantization-techniques` from `quantization-techniques-2026-05-03.md`).

If a matching file is found, **prune it** — delete the old file before starting fresh. The prune-and-replace rule means the latest research always replaces the previous. No archiving, no version history.

### 2. Get providers

Run `vane_get_providers` to fetch available provider IDs and model keys. Select the best available:
- **Chat model**: prefer `gemma4:31b-cloud`, then other high-quality chat models
- **Embedding model**: prefer `mixedbread-ai/mxbai-embed-large-v1` from the Transformers provider, then other embedding models

### 3. Deep search

Always deep, never shallow:

1. Run `vane_web_search` with the research query and `--save` flag. This creates the file in `ai-research/web/{slug}-{YYYY-MM-DD}.md` with:
   - HTML comment metadata header (type, search_date, query, tool_used, tool_model, embedding_model, sources)
   - Message body with inline citations `[1]`, `[2]`, etc.
   - Sources section with numbered references
2. Identify the top 3-5 source URLs from the vane output with the most relevant content
3. Use the crawl4ai MCP tool to fetch full page content from each URL
4. Append `## Deep Dive` sections to the saved file after the Sources section, one per crawled URL, with the crawled content

### 4. Add frontmatter

After the `--save` creates the file and deep-dive content is appended, add YAML frontmatter at the **very top** of the file (before the HTML comment header). The file must have both:
- YAML frontmatter (wiki page metadata) at the top
- HTML comment metadata header (provenance metadata) below the frontmatter

The YAML frontmatter must be:

```yaml
---
title: "<Human-readable title from query, or summarized version if query is long>"
summary: "<1-2 sentence summary of what was researched>"
type: ai-research-multi
sources:
  - ai-research/web/{filename}
tags: [<relevant tags derived from the topic>]
created: "<ISO 8601 timestamp>"
updated: "<ISO 8601 timestamp>"
---
```

Rules for the title:
- Use the user's query as the title if it's under ~80 characters
- If longer, summarize to a concise descriptive title
- The slug for the filename is derived by the existing `slugify()` in `vane_web_search.py`

### 5. Lint

Run `uv run python scripts/lint.py` to validate the saved file.

### 6. Sync-check

Invoke the sync-check agent to verify cross-file consistency after changes.

## Prune-and-Replace Rule

When re-researching an existing topic, the old file is deleted and replaced entirely. No archiving, no version history. The latest research replaces the previous.

## Key Principles

- **Always deep** — crawl4ai follow-up is mandatory, not optional
- **Always save to `ai-research/web/`** — this agent exists to persist research
- **Always lint after saving** — validate the file passes lint checks
- **Always run sync-check after changes** — verify cross-file consistency
- **Prune-then-replace on re-research** — never append to existing files
- After this agent completes, the saved source can be ingested into `wiki/` via the wiki-maintainer agent using the standard Ingest workflow
```

- [ ] **Step 2: Commit**

```bash
git add .claude/agents/ai-research.md
git commit -m "feat: add ai-research agent for persistent deep web research"
```

---

### Task 3: Modify wiki-query agent — add gap-filling and update guideline

**Files:**
- Modify: `.claude/agents/wiki-query.md`

- [ ] **Step 1: Update the Guidelines section in wiki-query.md**

In `.claude/agents/wiki-query.md`, change the second bullet in the Guidelines section from:

```
- If the KB doesn't have enough to answer, say so and suggest sources to ingest from `raw/` or `ai-research/` (subfolders: `articles/`, `papers/`, `repos/`, `datasets/`, `assets/`, `document/`, `web/`, `forum-thread/`, `transcripts/`) or `processed/`
```

to:

```
- If the KB doesn't have enough to answer, say so and offer to invoke the `web-search` agent (quick, ephemeral) or `ai-research` agent (deep, saves to KB), or suggest ingesting from existing `raw/` or `ai-research/` sources (subfolders: `articles/`, `papers/`, `repos/`, `datasets/`, `assets/`, `document/`, `web/`, `forum-thread/`, `transcripts/`) or `processed/`
```

- [ ] **Step 2: Add the Gap Filling section before the Key Principle section**

Insert the following section in `.claude/agents/wiki-query.md` between the "Output Formats" section and the "Filing Back" section:

```
## Gap Filling

When the KB cannot answer a question from existing sources and the gap could be filled by web research:

1. **Detect the gap** — After reading all relevant pages, if the answer is incomplete or missing, explicitly state: "The knowledge base doesn't have enough information to fully answer this question about [topic]."

2. **Ask the user** — Present the option: "I could search the web for this. Which would you like?"
   - **Quick search** — Invoke the `web-search` agent for ephemeral results (no saving)
   - **Deep research** — Invoke the `ai-research` agent for persistent results (saves to ai-research/, then can be ingested into wiki/)

3. **Wait for approval** — Do NOT invoke either agent without explicit user approval.

4. **After research** — If ai-research was used, the saved source can then be ingested into `wiki/` via the `wiki-maintainer` agent using the standard Ingest workflow.
```

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/wiki-query.md
git commit -m "feat: add gap-filling delegation to wiki-query agent"
```

---

### Task 4: Modify context-loader — add lookup table entries

**Files:**
- Modify: `.claude/agents/context-loader.md`

- [ ] **Step 1: Add two rows to the Load lookup table**

In `.claude/agents/context-loader.md`, add two rows to the Load operation's lookup table (after the existing "Directory sync validation" row):

```
| Quick web search | `.claude/agents/web-search.md` |
| Deep web research + save | `.claude/agents/ai-research.md` |
```

- [ ] **Step 2: Commit**

```bash
git add .claude/agents/context-loader.md
git commit -m "feat: add web-search and ai-research to context-loader lookup"
```

---

### Task 5: Modify sync-check — add files to checklist

**Files:**
- Modify: `.claude/agents/sync-check.md`

- [ ] **Step 1: Add web-search.md and ai-research.md to the Files to Read checklist**

In `.claude/agents/sync-check.md`, add two entries to the "Files to Read" list (after item 12, `.claude/agents/wiki-query.md`):

```
13. `.claude/agents/web-search.md`
14. `.claude/agents/ai-research.md`
```

Note: The existing list currently goes 1-13 with a gap (skips 15 and goes from 16 to... renumber). Keep the numbering consistent — the last item is currently `16. wiki/sources-manifest.md`, so add items 14 and 15, then renumber the existing item 16 to 16 (it stays the same).

Actually, looking at the file more carefully, the numbering is: 1-12, then skips to 16. The two new items should be 14 and 15, making the sources-manifest item 16 as it already is. This fills the numbering gap.

- [ ] **Step 2: Add web-search and ai-research to the agent cross-references check**

In the "Agent cross-references" section under "Agent files to check", add two entries:

```
- `.claude/agents/web-search.md`
- `.claude/agents/ai-research.md`
```

Add these after the existing `.claude/agents/wiki-query.md` entry.

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/sync-check.md
git commit -m "feat: add web-search and ai-research agents to sync-check"
```

---

### Task 6: Modify CLAUDE.md — add agent table rows

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add two rows to the Project Agents table**

In `CLAUDE.md`, add two rows to the Project Agents table after the `wiki-query` row:

```
| `web-search`        | "Search the web for X", "Quick fact-check on X"               |
| `ai-research`       | "Research X and save it", "Deep research on X"                 |
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add web-search and ai-research agents to CLAUDE.md"
```

---

### Task 7: Modify schema/WIKI_AGENTS.md — add agent descriptions and update Research Workflow

**Files:**
- Modify: `schema/WIKI_AGENTS.md`

- [ ] **Step 1: Add web-search agent description**

In `schema/WIKI_AGENTS.md`, add a section for the web-search agent. Insert it after the existing wiki-query agent section and before the Research Workflow section (or in the appropriate location within the existing agent structure). The section should be:

```markdown
### Web Search Agent

**File**: `.claude/agents/web-search.md`

**Role**: Ephemeral web search using the Vane API. Returns results to the caller without saving files.

**When to invoke**: "Search the web for X", "Quick fact-check on X"

**Operations**:
1. **Get providers** — Run `vane_get_providers` to fetch available provider IDs and model keys
2. **Search** (shallow, default) — Run `vane_web_search` with the query, present full output verbatim
3. **Deep search** (optional) — After vane results, crawl top 3-5 source URLs via crawl4ai for full content

**Key principle**: Never save files. Returns results to the caller. The caller decides what to do with them.
```

- [ ] **Step 2: Add ai-research agent description**

Add a section for the ai-research agent after the web-search section:

```markdown
### AI Research Agent

**File**: `.claude/agents/ai-research.md`

**Role**: Persistent deep research that saves results to `ai-research/web/`, lints, and runs sync-check.

**When to invoke**: "Research X and save it", "Deep research on X"

**Operations**:
1. **Check existing** — Check `ai-research/web/` for existing files on the same topic (match by slug). If found, delete the old file (prune-and-replace)
2. **Get providers** — Run `vane_get_providers` to fetch available provider IDs and model keys
3. **Deep search** — Run `vane_web_search` with `--save` flag, then crawl top 3-5 source URLs via crawl4ai and append deep-dive content
4. **Add frontmatter** — Add YAML frontmatter at the top of the saved file (before the HTML comment header)
5. **Lint** — Run `uv run python scripts/lint.py` to validate
6. **Sync-check** — Invoke sync-check agent for cross-file consistency

**Key principles**: Always deep (crawl4ai is mandatory), always save, always lint, always sync-check. Prune-then-replace on re-research.
```

- [ ] **Step 3: Update the Research Workflow section to reference both agents**

Find the "4. Research Workflow" section in `schema/WIKI_AGENTS.md`. Update it to reference both the web-search and ai-research agents as named operations. Change:

```markdown
## 4. Research Workflow

**Purpose**: Fill knowledge gaps by discovering and saving web sources.

**Trigger**: Human asks to research a topic, or a query reveals gaps the wiki cannot answer from existing sources.

**Steps**:

1. **Search the web** for relevant, high-quality sources on the topic
```

to:

```markdown
## 4. Research Workflow

**Purpose**: Fill knowledge gaps by discovering and saving web sources.

**Trigger**: Human asks to research a topic, or a query reveals gaps the wiki cannot answer from existing sources.

**Agents**: Use `web-search` for quick ephemeral lookups, or `ai-research` for persistent deep research that saves to the KB.

**Steps**:

1. **Search the web** for relevant, high-quality sources on the topic — invoke the `web-search` agent for shallow results or `ai-research` agent for deep research
```

The rest of the Research Workflow steps remain the same (they describe the outcome after ai-research saves files).

- [ ] **Step 4: Commit**

```bash
git add schema/WIKI_AGENTS.md
git commit -m "feat: add web-search and ai-research agent descriptions to WIKI_AGENTS"
```

---

### Task 8: Modify schema/WIKI_WORKFLOWS.md — add Search and Deep Research workflows

**Files:**
- Modify: `schema/WIKI_WORKFLOWS.md`

- [ ] **Step 1: Add Search Workflow before the Research Workflow section**

Insert the following section in `schema/WIKI_WORKFLOWS.md` before the "## 4. Research Workflow" section. Renumber Research Workflow to section 5 and the End-of-Day Compilation to section 6. Add the Search Workflow as section 4:

```markdown
---

## 4. Search Workflow (Ephemeral)

**Purpose**: Quick web search returning results to the caller without persistence.

**Trigger**: User asks "Search the web for X" or "Quick fact-check on X"

**Agent**: `web-search` (see `.claude/agents/web-search.md`)

**Steps**:

1. **Get providers** — Run `vane_get_providers` to fetch available provider IDs and model keys. Select best chat model (prefer `gemma4:31b-cloud`) and embedding model (prefer `mixedbread-ai/mxbai-embed-large-v1`)
2. **Run vane search** — Execute `vane_web_search` with the user's query and selected provider/model configuration
3. **Present results verbatim** — Output the full schema header, message body, and Sources section without modification
4. **(Optional) Deep dive** — If requested, crawl top 3-5 source URLs via crawl4ai and append `## Deep Dive` sections

**Output**: Search results returned to the caller. No files saved.

---

## 5. Deep Research Workflow (Persistent)

**Purpose**: Thorough web research that persists results as wiki source files.

**Trigger**: User asks "Research X and save it" or "Deep research on X"

**Agent**: `ai-research` (see `.claude/agents/ai-research.md`)

**Steps**:

1. **Check existing** — Search `ai-research/web/` for files matching the topic slug. If found, delete the old file (prune-and-replace)
2. **Deep search** — Get providers via `vane_get_providers`, then run `vane_web_search` with `--save` flag to create the file in `ai-research/web/{slug}-{YYYY-MM-DD}.md`
3. **Append deep-dive content** — Crawl top 3-5 source URLs via crawl4ai and append `## Deep Dive` sections to the saved file after the Sources section
4. **Add frontmatter** — Insert YAML frontmatter at the top of the file (before the HTML comment header) with title, summary, type, sources, tags, created, updated fields
5. **Lint** — Run `uv run python scripts/lint.py` to validate the saved file
6. **Sync-check** — Invoke the sync-check agent to verify cross-file consistency

**Output**: New file in `ai-research/web/`, validated by lint, verified by sync-check. Ready for ingestion via the Ingest workflow.
```

- [ ] **Step 2: Renumber existing sections**

After inserting the new workflows:
- The existing "4. Research Workflow" becomes "6. Research Workflow" (it remains as the legacy/higher-level description)
- The existing "End-of-Day Compilation" section becomes "7. End-of-Day Compilation"

Wait — actually looking more carefully, the Research Workflow in WIKI_WORKFLOWS.md is the existing section 4. The new Search and Deep Research workflows should be added as additional workflow definitions. Let me reconsider the structure:

Current WIKI_WORKFLOWS.md structure:
1. Ingest Workflow
2. Query Workflow
3. Lint Workflow
3b. Repair Workflow
4. Research Workflow
End-of-Day Compilation

The spec says to add two new workflow definitions. The Search and Deep Research workflows are distinct from the existing Research Workflow (which is a higher-level description). The cleanest approach:

- Keep sections 1-3b unchanged
- Add new section "4. Search Workflow (Ephemeral)"
- Add new section "5. Deep Research Workflow (Persistent)"
- Renumber existing section 4 to "6. Research Workflow"
- Renumber End-of-Day Compilation appropriately

- [ ] **Step 3: Commit**

```bash
git add schema/WIKI_WORKFLOWS.md
git commit -m "feat: add Search and Deep Research workflow definitions"
```

---

### Task 9: Modify AGENTS.md — add agents to operations and project structure

**Files:**
- Modify: `AGENTS.md`

- [ ] **Step 1: Add web-search and ai-research to the Core Operations section**

In `AGENTS.md`, find the "Core Operations" section (section "4. Research"). Update the Research operation description to reference both agents:

Change:

```markdown
### 4. Research (autonomous web discovery)

When a query reveals gaps the wiki cannot answer from existing sources, or the human asks to research a topic:

1. Search the web for relevant, high-quality sources on the topic
```

to:

```markdown
### 4. Research (autonomous web discovery)

When a query reveals gaps the wiki cannot answer from existing sources, or the human asks to research a topic:

**Quick search (ephemeral)**: Invoke the `web-search` agent — returns results without saving.

**Deep research (persistent)**: Invoke the `ai-research` agent — saves results to `ai-research/web/`, lints, and runs sync-check.

For manual research without agents:

1. Search the web for relevant, high-quality sources on the topic
```

The rest of the manual research steps (steps 2-7) remain unchanged.

- [ ] **Step 2: Add web-search.md and ai-research.md to the project structure**

In `AGENTS.md`, find the `.claude/agents/` directory listing in the "Full Project Structure" section. Add two entries after the existing `context-loader.md` entry:

```
|       |-- web-search.md
|       |-- ai-research.md
```

- [ ] **Step 3: Commit**

```bash
git add AGENTS.md
git commit -m "feat: add web-search and ai-research to AGENTS.md operations and structure"
```

---

### Task 10: Run sync-check to verify cross-file consistency

**Files:**
- No file changes — verification only

- [ ] **Step 1: Run sync-check agent**

Invoke the sync-check agent to verify that all cross-references, directory listings, agent lists, and conventions are consistent after the changes from Tasks 1-9.

If the sync-check reports inconsistencies, fix them in follow-up edits and commit the fixes.

- [ ] **Step 2: Final verification — confirm all files are correct**

Verify the following:
1. `.claude/agents/web-search.md` exists and contains the full agent spec
2. `.claude/agents/ai-research.md` exists and contains the full agent spec
3. `.claude/agents/wiki-query.md` has the Gap Filling section and updated guideline
4. `.claude/agents/context-loader.md` has the two new lookup entries
5. `.claude/agents/sync-check.md` has the new files in its checklist
6. `CLAUDE.md` has the two new agent table rows
7. `schema/WIKI_AGENTS.md` has both agent descriptions and updated Research Workflow
8. `schema/WIKI_WORKFLOWS.md` has the Search and Deep Research workflows
9. `AGENTS.md` has updated operations and project structure