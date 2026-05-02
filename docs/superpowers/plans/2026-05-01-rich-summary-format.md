# Rich Summary Format Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the rigid Key Points/Quotes/Notes summary template with a flexible template that produces rich, human-readable wiki summaries with custom sections, tables, and section-level citations.

**Architecture:** Three documentation-only changes — update the schema template, the agent instructions, and the workflow steps to consistently encourage rich summary output. No code changes.

**Tech Stack:** Markdown documentation files only

---

### Task 1: Update Summary Page Template in WIKI_SCHEMA.md

**Files:**
- Modify: `schema/WIKI_SCHEMA.md` (lines 198-224: Summary Pages section, and after line 224: add Style Guide)

- [ ] **Step 1: Replace the Summary Pages template**

In `schema/WIKI_SCHEMA.md`, find the `### Summary Pages` section (starting at line 198). Replace the entire code block inside it (lines 200-224) with the new template:

```markdown
### Summary Pages

```markdown
---
title: Source Title
summary: One-line summary of this source document
type: summary
sources:
  - raw/document/path/to/source.md or raw/web/path/to/source.md or ai-research/web/path/to/source.md
tags:
  - topic1
created: "2026-04-05T12:00:00Z"
updated: "2026-04-05T12:00:00Z"
---

# Source Title

## Summary
2-4 sentence narrative overview of the source's argument and significance.^[raw/articles/source.md]

## [Custom Section Headings]
Use section headings drawn from the source's structure. When the source
compares items, creates a taxonomy, or presents data — use tables.

Cite sources at the section level (end of section) rather than per-bullet.
Use tables whenever the source contains structured or comparative data.

## Key Quotes
> "Important quote"^[raw/articles/source.md:45]

## Related
- [[concepts/topic]]
- [[entities/name]]
```
```

- [ ] **Step 2: Add Style Guide section after Summary Pages**

Immediately after the closing triple-backtick of the Summary Pages template (after the `### Q&A Pages` heading line is found), insert a new section. Find the line `### Q&A Pages` and insert the following block *before* it:

```markdown
### Style Guide for Summaries

Summaries should be rich, encyclopedia-style articles — not flat bullet lists. Follow these guidelines:

- **Use section headings drawn from the source's structure** (e.g., "Anatomy of an LLM Name", "Decision Guide", "Why Naming Conventions Exist") rather than generic headings like "Key Points"
- **Use tables** for any comparative, tiered, or structured data from the source (comparison matrices, tier lists, risk/consequence/mitigation tables, parameter tables)
- **Write narrative paragraphs** for the `## Summary` section and for transitions between sections — not bullet lists
- **Cite at section level** — place `^[source.md]` at the end of a section or on the first claim in a section, not on every bullet point
- **The `summary` frontmatter field** is a one-line abstract; the `## Summary` body section is a narrative overview (2-4 sentences)
- **When a source has distinct topics**, create subsections rather than flattening into a uniform bullet list
- **Preserve the author's original structure** when it provides clarity (e.g., decision frameworks, comparison matrices, step-by-step guides)
- **`## Key Quotes`** collects the most important direct quotes from the source (2-5 quotes maximum)
- **`## Related`** links to wiki concepts and entities with `[[wikilinks]]`

```

- [ ] **Step 3: Commit**

```bash
git add schema/WIKI_SCHEMA.md
git commit -m "schema: replace rigid summary template with flexible rich-content template and add style guide"
```

---

### Task 2: Update wiki-maintainer Agent Step 3

**Files:**
- Modify: `.claude/agents/wiki-maintainer.md` (line 20: step 3 of Ingest operation)

- [ ] **Step 1: Replace step 3 wording**

In `.claude/agents/wiki-maintainer.md`, find line 20:

```
3. Write summary: `wiki/summaries/[source-name].md` — link to `processed/` segments if applicable. Include `summary` in frontmatter. Use claim citations `^[source.md]` for paragraph-level provenance.
```

Replace with:

```
3. Write summary: `wiki/summaries/[source-name].md` — use rich section headings and tables appropriate to the source content. Include a narrative `## Summary` section, custom sections with tables where applicable, section-level citations, and a `## Key Quotes` section. Link to `processed/` segments if applicable. See `schema/WIKI_SCHEMA.md` → Summary Pages for the full template and Style Guide.
```

- [ ] **Step 2: Commit**

```bash
git add .claude/agents/wiki-maintainer.md
git commit -m "agent: update wiki-maintainer step 3 to encourage rich summaries with custom sections and tables"
```

---

### Task 3: Update WIKI_WORKFLOWS.md Steps 2 and 3

**Files:**
- Modify: `schema/WIKI_WORKFLOWS.md` (lines 22-34: steps 2 and 3 of Ingest Workflow)

- [ ] **Step 1: Update step 2 to add structured data identification**

In `schema/WIKI_WORKFLOWS.md`, find step 2 (lines 22-26):

```
2. **Extract key information**
   - Identify entities (people, places, things, organizations)
   - Identify concepts (ideas, techniques, theories, methods)
   - Extract key claims, facts, and quotes
   - Assign `confidence` (0.0–1.0) and `provenance` (extracted|merged|inferred|ambiguous) to extracted content
```

Replace with:

```
2. **Extract key information**
   - Identify entities (people, places, things, organizations)
   - Identify concepts (ideas, techniques, theories, methods)
   - Extract key claims, facts, and quotes
   - Identify structured data suitable for tables (comparisons, tiers, risk matrices, decision guides, parameter lists)
   - Assign `confidence` (0.0–1.0) and `provenance` (extracted|merged|inferred|ambiguous) to extracted content
```

- [ ] **Step 2: Update step 3 to emphasize rich format**

In `schema/WIKI_WORKFLOWS.md`, find step 3 (lines 28-34):

```
3. **Write summary page**
   - Create `wiki/summaries/[source-title].md`
   - Include key points, quotes, and notes
   - Add YAML frontmatter with all required fields (title, summary, type, sources, tags, created, updated)
   - Add optional provenance fields (confidence, provenance, contradictedBy, orphaned) when applicable
   - Use claim citations `^[source.md]` for paragraph-level provenance
   - Link to `processed/` segments if the source was segmented
```

Replace with:

```
3. **Write summary page**
   - Create `wiki/summaries/[source-title].md`
   - Use rich section headings drawn from the source's structure (not generic "Key Points")
   - Use tables for structured or comparative data identified in step 2
   - Include a narrative `## Summary` section (2-4 sentences) as the opening body section
   - Add YAML frontmatter with all required fields (title, summary, type, sources, tags, created, updated)
   - Add optional provenance fields (confidence, provenance, contradictedBy, orphaned) when applicable
   - Cite at section level — place `^[source.md]` at end of section or on first claim, not on every bullet
   - Include a `## Key Quotes` section for the most important direct quotes (2-5 maximum)
   - Include a `## Related` section with `[[wikilinks]]` to concepts and entities
   - Link to `processed/` segments if the source was segmented
   - See `schema/WIKI_SCHEMA.md` → Style Guide for Summaries for full guidance
```

- [ ] **Step 3: Commit**

```bash
git add schema/WIKI_WORKFLOWS.md
git commit -m "workflow: update ingest steps 2-3 to identify tables and produce rich summaries"
```

---

### Task 4: Update WIKI_AGENTS.md to reference style guide

**Files:**
- Modify: `schema/WIKI_AGENTS.md`

- [ ] **Step 1: Add style guide reference**

In `schema/WIKI_AGENTS.md`, find the "File Conventions" section. After the "Linking" subsection, add a new subsection:

Find the line containing:
```
- **Claim citations**: `^[raw/articles/source.md]` or `^[raw/articles/source.md:42-58]` — see `schema/WIKI_SCHEMA.md` → Claim-Level Citations
```

After that line, add:

```

- **Summary style**: Use rich section headings and tables — see `schema/WIKI_SCHEMA.md` → Style Guide for Summaries
```

- [ ] **Step 2: Commit**

```bash
git add schema/WIKI_AGENTS.md
git commit -m "agent-schema: add summary style guide reference to WIKI_AGENTS.md"
```