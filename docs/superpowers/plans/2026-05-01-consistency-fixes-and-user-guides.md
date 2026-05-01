# Consistency Fixes + User/Owner Guides Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix consistency issues across docs/schemas/agents/wiki/code, clean up stray files, and create README-USER-GUIDE.md and README-OWNER-GUIDE.md.

**Architecture:** Fix documentation mismatches first (AGENTS.md, WIKI_SCHEMA.md, WIKI_WORKFLOWS.md, wiki-linter.md, knowledge-compiler.md, README.md, CLAUDE.md, settings.json), then fix wiki frontmatter, then clean up stray files, then write the two guide documents.

**Tech Stack:** Markdown (all docs/wiki files), Git

---

## File Changes Map

**Modified files:**
- `.claude/settings.json` — Hook commands: `python` → `uv run python`
- `CLAUDE.md` — Add WIKI_AGENTS.md to On-Demand Details
- `AGENTS.md` — 10 fixes (duplicate entry, Python version, context-loader, Windows flags, tools_scripts, sources-manifest comment, frontmatter dates, frontmatter fields, sync-check docs, lint count 12→8)
- `README.md` — Add tools_scripts/, fix sources-manifest comment
- `schema/WIKI_SCHEMA.md` — Fix `[[Page Name]]` → `[[path/to/article]]`
- `schema/WIKI_WORKFLOWS.md` — Update lint check count 12→8, remove 4 unimplemented checks
- `.claude/agents/wiki-linter.md` — Update check count 12→8, remove 4 unimplemented checks
- `.claude/agents/knowledge-compiler.md` — Add summary/type/tags to frontmatter required fields
- `wiki/index.md` — Add summary field, change date→created/updated
- `wiki/sources-manifest.md` — Add missing frontmatter fields
- `.gitignore` — Add .agents/, compound-knowledge.md, _useful_tools.md

**Created files:**
- `README-USER-GUIDE.md` — New user/adopter guide
- `README-OWNER-GUIDE.md` — Owner/internal reference guide

**Deleted:**
- `.agents/` directory (empty, broken symlink)

---

### Task 1: Fix AGENTS.md (10 changes)

**Files:**
- Modify: `AGENTS.md`

- [ ] **Step 1: Remove duplicate wiki-repair.md entry**

In the `.claude/agents/` listing (around line 335), there are two `wiki-repair.md` entries. Remove the duplicate on line 335.

Find:
```
|       |-- wiki-repair.md
|       |-- wiki-repair.md
```
Replace with:
```
|       |-- wiki-repair.md
```

- [ ] **Step 2: Fix Python version**

On line 583, change `Python 3.12+` to `Python >=3.11`.

- [ ] **Step 3: Add context-loader.md to agents listing**

In the `.claude/agents/` listing, add `context-loader.md` after `wiki-repair.md` (it's listed in the agent table but missing from the project tree).

- [ ] **Step 4: Fix Windows hook creation flags**

On line ~455-456, change:
```
- **Windows:** `CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS` flags
```
to:
```
- **Windows:** `CREATE_NO_WINDOW` flag (note: `DETACHED_PROCESS` breaks Agent SDK subprocess I/O)
```

- [ ] **Step 5: Add tools_scripts/ to project structure**

Add after the `hooks/` section in the project tree:
```
|-- tools_scripts/                    # Crawl scripts and utilities
|   |-- claude_en_urls.txt
|   |-- crawl_claude_docs.py
|   |-- crawl_openrouter_docs.py
|   |-- crawl4ai/
|   |   |-- basic.py
|   |-- rename_add_index.py
```

- [ ] **Step 6: Fix sources-manifest.md comment**

Change:
```
|   |-- sources-manifest.md          #   Source tracking (raw/processed → wiki status)
```
to:
```
|   |-- sources-manifest.md          #   Source tracking (raw/ai-research/processed → wiki status)
```

- [ ] **Step 7: Fix frontmatter examples to use ISO 8601 timestamps**

In the Concept Article example (around line 133), change:
```yaml
created: 2026-04-01
updated: 2026-04-03
```
to:
```yaml
created: "2026-04-01T12:00:00Z"
updated: "2026-04-03T12:00:00Z"
```

In the Connection Article example (around line 173), change:
```yaml
created: 2026-04-04
updated: 2026-04-04
```
to:
```yaml
created: "2026-04-04T12:00:00Z"
updated: "2026-04-04T12:00:00Z"
```

- [ ] **Step 8: Add summary, type, tags to required frontmatter for internal KB**

In the Conventions section (around line 314), change:
```
- **Frontmatter:** Every article must have YAML frontmatter with at minimum: title, sources, created, updated. Optional: confidence, provenance, contradictedBy, orphaned.
```
to:
```
- **Frontmatter:** Every article must have YAML frontmatter with at minimum: title, summary, type, sources, tags, created, updated. Optional: confidence, provenance, contradictedBy, orphaned.
```

- [ ] **Step 9: Document session-start.py sync-check injection**

In the `session-start.py` hook detail section (around line 433), after "Max context: 20,000 characters", add:
```
- Also injects a sync-check reminder instructing Claude to run the sync-check agent at session start
```

- [ ] **Step 10: Update lint check count from 12 to 8 and remove 4 unimplemented checks**

In the "3. Lint (Health Checks)" section (around line 264-279), change the intro from "Twelve checks" to "Eight checks" and remove checks 8-11 (Missing summary, Duplicate concept, Malformed citation, Broken citation). Keep check 12 (Contradictions) as check 8. The final list should be:

```
1. **Broken links** (error) — `[[wikilinks]]` pointing to non-existent articles
2. **Orphan pages** (warning) — Articles with zero inbound links from other articles. `orphaned: true` in frontmatter flags automatically.
3. **Orphan sources** (suggestion) — Daily logs not yet compiled, or raw/ai-research sources not yet ingested
4. **Stale articles** (warning) — Source daily log changed since article was last compiled
5. **Missing backlinks** (suggestion) — A links to B but B doesn't link back to A
6. **Sparse articles** (suggestion for <200 words, warning for <50 chars body) — Articles under 200 words (likely incomplete)
7. **Unsourced claims** (warning) — Statements not traceable to a source file
8. **Contradictions** (error, requires LLM judgment) — Conflicting claims across articles. Suggest adding `contradictedBy` to frontmatter.
```

Also update the "Script Details > lint.py" section. Change "Twelve checks:" to "Eight checks:" and replace the full check table with:

```
| Check | Type | Catches |
|-------|------|---------|
| Broken links | Structural | `[[wikilinks]]` to non-existent articles |
| Orphan pages | Structural | Articles with zero inbound links |
| Orphan sources | Structural | Daily logs not yet compiled, or raw/ai-research sources not yet ingested |
| Stale articles | Structural | Source logs changed since compilation |
| Missing backlinks | Structural | A links to B but B doesn't link back |
| Sparse articles | Structural | Under 200 words (suggestion), under 50 chars body (warning) |
| Unsourced claims | Structural | Statements not traceable to source file |
| Contradictions | LLM | Conflicting claims across articles |
```

Also update the `lint.py` description in the project tree from `#   12 health checks` to `#   8 health checks`.

- [ ] **Step 11: Commit AGENTS.md changes**

```bash
git add AGENTS.md
git commit -m "fix: 10 consistency fixes in AGENTS.md

- Remove duplicate wiki-repair.md entry
- Fix Python version 3.12+ → >=3.11
- Add context-loader.md to agents listing
- Fix Windows hook flags DETACHED_PROCESS → CREATE_NO_WINDOW
- Add tools_scripts/ to project structure
- Fix sources-manifest.md comment to include ai-research/
- Fix frontmatter examples to use ISO 8601 timestamps
- Add summary/type/tags to required frontmatter fields
- Document session-start.py sync-check injection
- Update lint check count 12→8, remove 4 unimplemented checks

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 2: Fix .claude/settings.json hook commands

**Files:**
- Modify: `.claude/settings.json`

- [ ] **Step 1: Change `python` to `uv run python` in all 3 hook commands**

In `.claude/settings.json`, change all three `"command"` values from `python hooks/...` to `uv run python hooks/...`:

```json
"command": "uv run python hooks/session-start.py"
"command": "uv run python hooks/pre-compact.py"
"command": "uv run python hooks/session-end.py"
```

- [ ] **Step 2: Commit settings.json**

```bash
git add .claude/settings.json
git commit -m "fix: use uv run python in hook commands

Hook commands now use 'uv run python' instead of bare 'python'
to ensure the project's virtual environment is used.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 3: Fix CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add schema/WIKI_AGENTS.md to On-Demand Details**

In the On-Demand Details section (around line 57-64), add a line for WIKI_AGENTS.md:

```
- **Workflows**: `schema/WIKI_WORKFLOWS.md`
- **File formats**: `schema/WIKI_SCHEMA.md`
- **Agent roles**: `schema/WIKI_AGENTS.md` and `.claude/agents/*.md`
- **Internal KB**: `AGENTS.md`
- **Scripts**: `scripts/*.py` (run via `uv run python scripts/<name>.py`)
- **Hooks**: `.claude/settings.json`
```

Note: WIKI_AGENTS.md is already listed in the Architecture table but was missing from On-Demand Details. Just adding it here makes it explicit.

- [ ] **Step 2: Commit CLAUDE.md**

```bash
git add CLAUDE.md
git commit -m "fix: add WIKI_AGENTS.md to On-Demand Details in CLAUDE.md

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 4: Fix schema files (WIKI_SCHEMA.md, WIKI_WORKFLOWS.md)

**Files:**
- Modify: `schema/WIKI_SCHEMA.md`
- Modify: `schema/WIKI_WORKFLOWS.md`

- [ ] **Step 1: Fix wikilink convention in WIKI_SCHEMA.md**

In `schema/WIKI_SCHEMA.md` around line 127, the Linking Conventions section shows:

```
- **Internal links**: `[[Page Name]]` or `[[entities/transformer_model|Transformer Model]]`
```

Change to:
```
- **Internal links**: `[[path/to/article]]` or `[[entities/transformer_model|Transformer Model]]`
```

This aligns with CLAUDE.md's convention of path-based wikilinks.

- [ ] **Step 2: Update lint check section in WIKI_WORKFLOWS.md**

In `schema/WIKI_WORKFLOWS.md`, the Lint Workflow section (checks 1-12) needs to be updated to match the 8-check list. Remove checks 8-11 (Missing summary, Duplicate concept, Malformed citation, Broken citation) and renumber Contradictions as check 8.

The updated check list should be:

```markdown
1. **Broken links** (error)
   - Find `[[wikilinks]]` pointing to non-existent articles

2. **Orphan pages** (warning)
   - Find pages with zero inbound links from other articles
   - Pages with `orphaned: true` in frontmatter are flagged automatically

3. **Orphan sources** (suggestion)
   - Find source documents in `raw/` or `ai-research/` (any subfolder) not yet processed, or `processed/` segments not yet ingested into wiki
   - Cross-check against `wiki/sources-manifest.md` for tracking

4. **Stale articles** (warning)
   - Find articles whose source has changed since compilation (compare hashes/timestamps)

5. **Missing backlinks** (suggestion)
   - Find A links to B but B doesn't link back to A

6. **Sparse articles** (suggestion for <200 words, warning for <50 chars body)
   - Find articles under 200 words (likely incomplete)
   - Flag body under 50 characters as a stronger warning (essentially empty)

7. **Unsourced claims** (warning)
   - Find statements in wiki articles not traceable to a `raw/` or `ai-research/` source file

8. **Contradictions** (error, requires LLM judgment)
   - Compare claims across pages for conflicts
   - When found, add `contradictedBy` to frontmatter of affected pages
```

- [ ] **Step 3: Commit schema fixes**

```bash
git add schema/WIKI_SCHEMA.md schema/WIKI_WORKFLOWS.md
git commit -m "fix: align wikilink convention and lint check count in schema files

- WIKI_SCHEMA.md: change [[Page Name]] to [[path/to/article]]
- WIKI_WORKFLOWS.md: reduce lint checks from 12 to 8, remove 4 unimplemented checks

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 5: Fix agent files (wiki-linter.md, knowledge-compiler.md)

**Files:**
- Modify: `.claude/agents/wiki-linter.md`
- Modify: `.claude/agents/knowledge-compiler.md`

- [ ] **Step 1: Update wiki-linter.md check count and remove unimplemented checks**

In `.claude/agents/wiki-linter.md`, update:
- The check count from 12 to 8
- Remove checks 8-11 (Missing summary, Duplicate concept, Malformed citation, Broken citation)
- Keep Contradictions as check 8
- Update the output format example to remove references to the 4 removed checks

The updated Structural Checks section:

```markdown
### Structural Checks (no LLM judgment needed)

1. **Broken links** (error) — `[[wikilinks]]` pointing to non-existent files
2. **Orphan pages** (warning) — Articles with zero inbound links from other articles. Pages with `orphaned: true` in frontmatter are flagged automatically.
3. **Orphan sources** (suggestion) — Source documents in `raw/` or `ai-research/` (any subfolder) not yet processed, or `processed/` segments not yet ingested into wiki. Cross-check against `wiki/sources-manifest.md` for tracking
4. **Stale articles** (warning) — Source changed since article was last compiled (compare hashes/timestamps)
5. **Missing backlinks** (suggestion) — A links to B but B doesn't link back to A
6. **Sparse articles** (suggestion for <200 words, warning for <50 chars body) — Articles under 200 words, likely incomplete. Body under 50 characters flagged as stronger warning (essentially empty).
7. **Unsourced claims** (warning) — Statements in wiki articles that do not trace back to a `raw/` or `ai-research/` source file, or claims that do not appear in the cited source.

### LLM Judgment Check

8. **Contradictions** (error) — Conflicting claims across articles. Requires reading multiple articles and reasoning about whether claims are truly incompatible. When found, suggest adding `contradictedBy` to frontmatter of affected pages.
```

- [ ] **Step 2: Update knowledge-compiler.md frontmatter required fields**

In `.claude/agents/knowledge-compiler.md` around line 90, change:
```
- **Frontmatter**: Every article must have YAML (title, sources, created, updated at minimum). Optional: confidence, provenance, contradictedBy, orphaned.
```
to:
```
- **Frontmatter**: Every article must have YAML (title, summary, type, sources, tags, created, updated at minimum). Optional: confidence, provenance, contradictedBy, orphaned.
```

- [ ] **Step 3: Commit agent file fixes**

```bash
git add .claude/agents/wiki-linter.md .claude/agents/knowledge-compiler.md
git commit -m "fix: update agent files for consistency

- wiki-linter.md: reduce check count 12→8, remove 4 unimplemented checks
- knowledge-compiler.md: add summary/type/tags to required frontmatter

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 6: Fix README.md

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Fix sources-manifest.md comment**

In the project structure tree, change:
```
│   ├── sources-manifest.md       #   Source tracking (raw/processed → wiki status)
```
to:
```
│   ├── sources-manifest.md       #   Source tracking (raw/ai-research/processed → wiki status)
```

- [ ] **Step 2: Add tools_scripts/ to project structure**

Add after the `reports/` entry in the project structure:
```
├── tools_scripts/                  # Crawl scripts and utilities
│   ├── claude_en_urls.txt
│   ├── crawl_claude_docs.py
│   ├── crawl_openrouter_docs.py
│   ├── crawl4ai/
│   │   └── basic.py
│   └── rename_add_index.py
```

- [ ] **Step 3: Commit README.md fixes**

```bash
git add README.md
git commit -m "fix: update sources-manifest comment and add tools_scripts/ to README

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 7: Fix wiki frontmatter (index.md, sources-manifest.md)

**Files:**
- Modify: `wiki/index.md`
- Modify: `wiki/sources-manifest.md`

- [ ] **Step 1: Fix wiki/index.md frontmatter**

Replace the current frontmatter:
```yaml
---
title: Wiki Index
type: index
date: 2026-04-22
sources: []
tags: [structural]
---
```
with:
```yaml
---
title: Wiki Index
summary: Master catalog of all wiki pages
type: index
sources: []
tags: [structural]
created: "2026-04-22T12:00:00Z"
updated: "2026-04-23T12:00:00Z"
---
```

- [ ] **Step 2: Fix wiki/sources-manifest.md frontmatter**

Replace the current frontmatter:
```yaml
---
title: Sources Manifest
type: manifest
date: 2026-04-22
---
```
with:
```yaml
---
title: Sources Manifest
summary: Tracks which source files have been ingested into the wiki
type: manifest
sources: []
tags: [structural]
created: "2026-04-22T12:00:00Z"
updated: "2026-04-23T12:00:00Z"
---
```

- [ ] **Step 3: Commit wiki frontmatter fixes**

```bash
git add wiki/index.md wiki/sources-manifest.md
git commit -m "fix: add missing frontmatter fields to wiki index and sources-manifest

- Add summary, created, updated fields
- Change date→created/updated with ISO 8601 timestamps

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 8: Superseded — synthesis.md update via wiki-maintainer subagent

> **Note:** The original task was to add `update_wiki_synthesis()` to `scripts/ingest_external.py`. This script no longer exists. Synthesis.md updates are now handled by the subagent-driven wiki-maintainer pattern, which updates `wiki/synthesis.md` as part of its 10-step ingest workflow (step 10). No code changes needed.

---

### Task 9: Clean up stray files

**Files:**
- Modify: `.gitignore`
- Delete: `.agents/` directory

- [ ] **Step 1: Add entries to .gitignore**

Add these lines to the end of `.gitignore`:

```
# Personal scratch files
.agents/
_useful_tools.md
compound-knowledge.md
```

- [ ] **Step 2: Delete .agents/ directory**

```bash
rm -rf .agents/
```

- [ ] **Step 3: Commit cleanup**

```bash
git add .gitignore
git commit -m "chore: gitignore stray files and remove empty .agents/ dir

- Add .agents/, _useful_tools.md, compound-knowledge.md to .gitignore
- Remove .agents/ directory (empty, broken symlink)

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 10: Create README-USER-GUIDE.md

**Files:**
- Create: `README-USER-GUIDE.md`

- [ ] **Step 1: Write README-USER-GUIDE.md**

Create `README-USER-GUIDE.md` with the following content. This is a guide for new users and potential adopters.

```markdown
# LLM Wiki — User Guide

A personal knowledge base that uses persistent wiki instead of RAG. Your AI conversations and web sources compile themselves into a searchable, compounding knowledge base.

## What is LLM Wiki?

Instead of rediscovering knowledge from scratch on every query (RAG), the LLM incrementally builds and maintains a **persistent wiki**. Every source you add and every question you ask makes the knowledge base richer. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read.

## Quick Start

### Prerequisites

- Python >=3.11
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Anthropic API key (or Claude Code credentials)

### Setup

```bash
git clone <your-repo-url>
cd llm-wiki-llm-v1
uv sync
```

### First Ingestion

```bash
# Add source documents to raw/ (any subfolder)
cp ~/my-article.md raw/articles/

# Ingest into the wiki (tell Claude Code)
# "Process raw/articles/my-article.md" or "Ingest my-article"
# The wiki-maintainer agent handles the full 10-step ingest workflow
```

## The Two Knowledge Bases

### External Knowledge Base (wiki/)

Web articles, papers, repos, and datasets compiled into a structured wiki.

```
raw/           → Human-curated sources (you add files here)
ai-research/   → LLM-discovered web sources (immutable once saved)
processed/     → Staging area for large files (LLM segments them)
wiki/          → Compiled knowledge (LLM owns this)
```

### Internal Knowledge Base (knowledge/)

Your Claude Code conversations compiled into searchable knowledge articles.

```
daily/         → Conversation logs (LLM-curated from your sessions)
knowledge/     → Compiled knowledge (LLM owns this)
```

**Ownership summary:**

| Directory | Who writes | Who curates | Can you edit? |
|-----------|-----------|-------------|--------------|
| `raw/` | You | You | Yes — add source files |
| `ai-research/` | LLM | You approve | No — immutable once saved |
| `processed/` | LLM | LLM | No — staging area |
| `wiki/` | LLM | LLM | No — let the LLM maintain it |
| `daily/` | LLM (via hooks) | LLM | No — immutable logs |
| `knowledge/` | LLM | LLM | No — let the LLM maintain it |

## Directory Map

### Wiki Content (what gets compiled)

```
raw/
├── articles/          # Web articles, blog posts
├── papers/            # Academic papers, PDFs
├── repos/             # Cloned Git repositories
├── datasets/          # Data files
├── assets/            # Images and attachments
├── document/          # Documents (papers, PDFs, datasets)
├── web/               # Web sources (articles, repos, tweets)
├── forum-thread/      # Forum discussions
└── transcripts/       # Conversation transcripts

ai-research/           # Same subfolder structure as raw/
                       # LLM discovers and saves web sources here

processed/             # Same subfolder structure as raw/
                       # Large raw files get segmented here before ingestion

wiki/
├── index.md           # Master catalog (THE retrieval mechanism)
├── sources-manifest.md # Which sources have been ingested
├── log.md             # Chronological operation log
├── synthesis.md       # Overarching thesis connecting all knowledge
├── concepts/          # Concept pages (snake_case)
├── entities/          # Entity pages (snake_case)
├── summaries/         # Source summaries (kebab-case)
└── qanda/             # Q&A articles (kebab-case)
```

### Project Infrastructure (how the system works)

```
daily/                 # Conversation logs (auto-generated by hooks)
knowledge/             # Compiled internal knowledge
├── index.md           # Master catalog for internal KB
├── log.md             # Build log
├── concepts/          # Concept articles
├── connections/       # Cross-cutting connections
└── qa/                # Filed Q&A answers

schema/                # Configuration for the external wiki
├── WIKI_AGENTS.md     # Wiki maintainer agent role
├── WIKI_SCHEMA.md     # File formats and conventions
└── WIKI_WORKFLOWS.md  # Ingest, Query, Lint, Research workflows

scripts/               # CLI tools (run via uv run python scripts/<name>.py)
├── compile.py         # Compile daily logs → knowledge articles
├── query.py           # Ask the knowledge base (index-guided, no RAG)
├── lint.py            # Health checks (8 structural + 1 LLM check)
├── flush.py            # Extract memories from conversations (background)
├── config.py           # Path constants and time helpers
└── utils.py            # Shared helpers

hooks/                 # Claude Code hooks (auto-activate in sessions)
├── session-start.py   # Injects knowledge base context into every session
├── session-end.py     # Captures conversation context before session ends
└── pre-compact.py      # Captures context before auto-compaction

.claude/
├── settings.json      # Hook configuration
├── mcp.json           # MCP server configuration (crawl4ai)
└── agents/            # 8 project-specific Claude Code agents
    ├── wiki-maintainer.md
    ├── document-processor.md
    ├── knowledge-compiler.md
    ├── wiki-linter.md
    ├── wiki-repair.md
    ├── wiki-query.md
    ├── sync-check.md
    ├── context-loader.md

tools_scripts/         # Crawling and utility scripts
├── claude_en_urls.txt
├── crawl_claude_docs.py
├── crawl_openrouter_docs.py
├── crawl4ai/
│   └── basic.py
└── rename_add_index.py

reports/               # Lint reports (gitignored, regenerated)
AGENTS.md              # Internal KB schema
CLAUDE.md              # Project instructions for Claude Code
pyproject.toml         # Dependencies (claude-agent-sdk, python-dotenv, tzdata)
```

## Core Commands

| Command | Purpose |
|---------|---------|
| `uv run python scripts/compile.py` | Compile new/changed daily logs into knowledge |
| `uv run python scripts/compile.py --all` | Force recompile all daily logs |
| `uv run python scripts/compile.py --dry-run` | Show what would be compiled |
| `uv run python scripts/query.py "question"` | Ask the knowledge base |
| `uv run python scripts/query.py "question" --file-back` | Ask and save answer as Q&A article |
| `uv run python scripts/lint.py` | Run all health checks |
| `uv run python scripts/lint.py --structural-only` | Run structural checks only (free, no API calls) |
| `uv run python scripts/lint.py --kb internal` | Lint internal KB only |
| `uv run python scripts/lint.py --kb external` | Lint external KB only |

## Using the Agents

Tell Claude Code:

| Agent | When to invoke |
|-------|---------------|
| `wiki-maintainer` | "Process this source", "Ingest X" |
| `document-processor` | Files >3,000 words or PDFs |
| `knowledge-compiler` | "Compile daily logs" |
| `wiki-linter` | "Lint the wiki", "Run health check" |
| `wiki-repair` | "Fix broken links", "Resolve orphans", "Repair lint errors" |
| `wiki-query` | Questions about compiled knowledge |
| `sync-check` | After structural changes to dirs/schemas/agents |
| `context-loader` | "Load rules for X", "Audit CLAUDE.md" |

## Obsidian Integration

The wiki works natively in Obsidian:

1. Install [Obsidian](https://obsidian.md/)
2. Open the project folder as a vault: "Open folder as vault"
3. Graph view, backlinks, Dataview queries, and Marp slides all work automatically

The `[[wikilinks]]` format, YAML frontmatter, and directory structure are designed for Obsidian compatibility.

## Crawling Docs

The project uses crawl4ai for web crawling (configured via MCP in `.claude/mcp.json`):

- **Primary**: Use the crawl4ai MCP tool (runs on `localhost:11235`)
- **Fallback**: If MCP is unavailable, use `WebFetch` or the scripts in `tools_scripts/`

Tell Claude Code: "Crawl [URL] and save it to ai-research/"

## Why No RAG?

At personal scale (50-500 articles), the LLM reading a structured `index.md` outperforms vector similarity. The LLM understands what you're really asking; cosine similarity just finds similar words. RAG becomes necessary at ~2,000+ articles when the index exceeds the context window.
```

- [ ] **Step 2: Commit README-USER-GUIDE.md**

```bash
git add README-USER-GUIDE.md
git commit -m "docs: add README-USER-GUIDE.md for new users and adopters

Covers quick start, two KB architecture, directory map with ownership,
core commands, agent dispatch, Obsidian integration, and crawling docs.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 11: Create README-OWNER-GUIDE.md

**Files:**
- Create: `README-OWNER-GUIDE.md`

- [ ] **Step 1: Write README-OWNER-GUIDE.md**

Create `README-OWNER-GUIDE.md` with the following content. This is a reference for the project owner — internals, maintenance, and known issues.

```markdown
# LLM Wiki — Owner Guide

Internal reference for how the system works, what to maintain, and what to watch out for.

## Architecture at a Glance

```
┌─────────────────────────────────────────────────────────┐
│                    External KB                           │
│                                                         │
│  raw/ ──► processed/ ──► wiki/                         │
│  (human)    (LLM stage)    (LLM compiled)               │
│  ai-research/ ──────────────┘                           │
│  (LLM found, immutable)                                 │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                    Internal KB                           │
│                                                         │
│  daily/ ──► knowledge/                                  │
│  (hooks capture)  (LLM compiled)                         │
│                                                         │
│  Schema: AGENTS.md                                      │
│  Schema: schema/WIKI_*.md                               │
└─────────────────────────────────────────────────────────┘
```

**Ownership rule:** You curate `raw/`. The LLM owns `wiki/`, `knowledge/`, `processed/`, and `daily/`. `ai-research/` is LLM-discovered but immutable once saved.

## Data Flow

### External Ingest (raw → wiki)

```
1. You add file to raw/ or ai-research/
2. If file >3000 words → document-processor segments to processed/
3. wiki-maintainer processes source
4. Creates/updates: summary, entities, concepts in wiki/
5. Updates: index.md, sources-manifest.md, log.md, synthesis.md
6. Lint + repair if batch ingesting
```

### Internal Compile (daily → knowledge)

```
1. session-end hook fires → flush.py extracts memories → daily/YYYY-MM-DD.md
2. compile.py reads daily log + existing knowledge articles
3. Creates/updates: concepts, connections in knowledge/
4. Updates: knowledge/index.md, knowledge/log.md
5. Auto-compilation triggers after 6 PM if daily log changed
```

## File Ownership Map

| Who edits | Directories/Files |
|-----------|------------------|
| **You** | `raw/` (add sources), `AGENTS.md` (schema), `CLAUDE.md` (project rules), `schema/WIKI_*.md` (config), `.claude/agents/*.md` (agent defs), `.claude/settings.json` (hooks), `pyproject.toml` (deps) |
| **LLM** | `wiki/` (compiled), `knowledge/` (compiled), `processed/` (staged), `daily/` (conversation logs), `scripts/state.json` (tracking) |
| **Hooks** | `daily/` (created by session-end), `scripts/flush-context-*` (temp) |
| **Gitignored** | `daily/`, `knowledge/`, `reports/`, `scripts/state.json`, `scripts/last-flush.json`, `.claude/settings.local.json`, `.obsidian/` |

## Scripts Reference

| Script | Purpose | Key CLI Flags | State Files |
|--------|---------|---------------|-------------|
| `compile.py` | Compile daily logs → knowledge articles | `--all`, `--file <path>`, `--dry-run` | `scripts/state.json` (hashes) |
| `query.py` | Index-guided KB query | `--file-back` (saves Q&A article) | `scripts/state.json` (query count) |
| `lint.py` | Health checks (8 structural + 1 LLM) | `--structural-only`, `--kb internal\|external\|both` | `scripts/state.json` (last lint), `reports/lint-*.md` |
| `flush.py` | Extract memories from conversations | (spawned by hooks, not manual) | `scripts/last-flush.json` (dedup) |
| `config.py` | Path constants and time helpers | (imported, not run directly) | — |
| `utils.py` | Shared helpers (slugify, frontmatter, etc.) | (imported, not run directly) | — |

## Hooks Reference

| Hook | When | What it does |
|------|------|--------------|
| `session-start.py` | Every Claude Code session start | Reads `knowledge/index.md` + recent daily log, injects as context. Also injects a sync-check reminder. |
| `session-end.py` | Session close | Reads transcript JSON, spawns `flush.py` as detached background process. Windows: `CREATE_NO_WINDOW` flag. |
| `pre-compact.py` | Before auto-compaction | Same architecture as session-end. Captures context before summarization discards it. Critical for long sessions. |

**Hook config location:** `.claude/settings.json` — commands use `uv run python hooks/<name>.py`

**Flush deduplication:** `scripts/last-flush.json` tracks `(session_id, timestamp)` to prevent double-processing. Skips if same session was flushed within 60 seconds.

**Auto-compilation:** If it's past 6 PM local time and today's daily log has changed since last compilation (hash comparison), `flush.py` spawns `compile.py` as another detached background process.

## Agent Dispatch Rules

| Trigger phrase | Agent | What it does |
|----------------|-------|--------------|
| "Process this source" | `wiki-maintainer` | 10-step ingest of a source into wiki/ |
| Files >3,000 words or PDFs | `document-processor` | Segment large files into processed/ |
| "Compile daily logs" | `knowledge-compiler` | Compile daily/ → knowledge/ |
| "Lint the wiki", "Run health check" | `wiki-linter` | 8 structural + 1 LLM checks |
| "Fix broken links", "Resolve orphans" | `wiki-repair` | 7 repair operations |
| Questions about compiled knowledge | `wiki-query` | 7-step query with optional file-back |
| After structural changes | `sync-check` | 7 categories of consistency checks |
| "Load rules for X", "Audit CLAUDE.md" | `context-loader` | On-demand rule loading, prompt health |

## Schema Cross-References

| File | Defines |
|------|---------|
| `AGENTS.md` | Internal KB schema: compiler analogy, article formats, operations, conventions, project structure, hook system, script details |
| `schema/WIKI_AGENTS.md` | External KB agent role, three-layer architecture, file conventions |
| `schema/WIKI_SCHEMA.md` | External KB file formats: frontmatter, naming, citations, page templates, index/log format |
| `schema/WIKI_WORKFLOWS.md` | External KB workflows: Ingest (10 steps), Query (5 steps), Lint (8+1 checks), Research |
| `CLAUDE.md` | Project instructions: architecture table, key directories, agent dispatch, core conventions, on-demand details |

## Known Issues & Design Decisions

- **Lint checks**: 8 structural + 1 LLM = 9 total. The 4 checks removed from docs (missing summary, duplicate concept, malformed citation, broken citation) are not implemented in lint.py. If you need them, add implementations before updating docs.
- **`daily/` and `knowledge/` are gitignored**: They're regenerated by hooks and scripts. If you lose the local copies, re-run compilation from a backup of daily logs.
- **`ai-research/` is currently empty**: The Research workflow has never been executed. All current wiki content comes from `raw/` sources.
- **`processed/` is currently empty**: No large files have been segmented yet.
- **`knowledge/qa/` is currently empty**: No Q&A articles have been filed back yet.
- **Windows hooks**: Use `CREATE_NO_WINDOW` flag, not `DETACHED_PROCESS`. The latter breaks Agent SDK subprocess I/O.
- **Wiki frontmatter**: All wiki pages require `title`, `summary`, `type`, `sources`, `tags`, `created`, `updated`. Optional: `confidence`, `provenance`, `contradictedBy`, `orphaned`.

## Maintenance Tasks

| Task | When | How |
|------|------|-----|
| Run sync-check | Every session start (automatic via hook) | The session-start hook injects a reminder |
| Run lint | After batch ingestion, or weekly | `uv run python scripts/lint.py --structural-only` |
| Run full lint | Monthly or before releases | `uv run python scripts/lint.py` |
| Reset state | If state.json gets corrupted | `rm scripts/state.json scripts/last-flush.json` |
| Compile daily logs | After 6 PM (automatic), or manually | `uv run python scripts/compile.py` |
| Review lint reports | After running lint | Check `reports/lint-YYYY-MM-DD.md` |
```

- [ ] **Step 2: Commit README-OWNER-GUIDE.md**

```bash
git add README-OWNER-GUIDE.md
git commit -m "docs: add README-OWNER-GUIDE.md for project internals and maintenance

Covers architecture, data flow, file ownership, scripts reference,
hooks reference, agent dispatch, schema cross-refs, known issues,
and maintenance tasks.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 12: Run sync-check to verify all fixes

**Files:** None (verification only)

- [ ] **Step 1: Run sync-check agent**

Invoke the sync-check agent to verify all the consistency fixes are correct and no new inconsistencies were introduced.

- [ ] **Step 2: Review sync-check results and fix any remaining issues**

If the sync-check finds new issues introduced by the fixes, address them immediately.

- [ ] **Step 3: Final commit if needed**

If any additional fixes were needed, commit them.

---

## Self-Review Checklist

After completing all tasks, verify:

- [ ] All spec items are addressed (15 doc fixes + 2 wiki fixes + 0 code fixes + 3 cleanup items + 2 guide files + 1 verification)
- [ ] No placeholder text in README-USER-GUIDE.md or README-OWNER-GUIDE.md
- [ ] All file paths in the plan match actual file paths on disk
- [ ] The lint check count is consistently 8 across all files (AGENTS.md, WIKI_WORKFLOWS.md, wiki-linter.md, knowledge-compiler.md, README.md, README-USER-GUIDE.md, README-OWNER-GUIDE.md)
- [ ] Hook commands use `uv run python` in all files (settings.json, AGENTS.md)
- [ ] Python version is consistently >=3.11 across all files (AGENTS.md, pyproject.toml, README-USER-GUIDE.md)
- [ ] Frontmatter conventions are consistent (title, summary, type, sources, tags, created, updated)
- [ ] Wikilink convention is consistently `[[path/to/article]]` across all files (CLAUDE.md, WIKI_SCHEMA.md, AGENTS.md)