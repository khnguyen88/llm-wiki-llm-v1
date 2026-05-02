# Design: Rich Summary Format for Wiki Maintainer

**Date:** 2026-05-01
**Status:** Draft
**Problem:** Current wiki summaries are flat bullet lists with per-bullet citations; old summaries had rich sections, tables, and narrative flow.

## Root Cause

Three factors caused the regression from rich to flat summaries:

1. **Rigid schema template** — `WIKI_SCHEMA.md` Summary Page template only defines `## Key Points`, `## Quotes`, `## Notes`. This constrains the agent into producing flat bullet lists instead of rich sections with tables and custom headings.

2. **Per-bullet citations** — The requirement to add `^[raw/articles/source.md]` on every key point turns narrative paragraphs into citation-stuffed bullet lists. The old summaries used no inline citations and were far more readable.

3. **Frontmatter `summary` field absorbed the narrative** — What used to be a rich opening section is now a one-line YAML field, so the body starts with "Key Points" instead of a narrative introduction.

## Solution: Flexible Template with Section-Level Citations

### Summary Page Template (WIKI_SCHEMA.md)

Replace the current rigid template:

```markdown
<!-- OLD -->
## Key Points
- Point 1^[raw/articles/source.md]
- Point 2

## Quotes
> "Important quote"^[raw/articles/source.md:45]

## Notes
Additional remarks.
```

With the new flexible template:

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

### Style Guide Addition (WIKI_SCHEMA.md)

Add a "Style Guide for Summaries" section after the Summary Page template:

- Use section headings drawn from the source's structure (e.g., "Anatomy of an LLM Name", "Decision Guide")
- Use tables for any comparative, tiered, or structured data from the source
- Write narrative paragraphs for the Summary section and transitions between sections
- Cite at section level — place `^[source.md]` at the end of a section or on the first claim, not on every bullet point
- The `summary` frontmatter field is a one-line abstract; the `## Summary` body section is a narrative overview (2-4 sentences)
- When a source has distinct topics, create subsections rather than flattening into a bullet list
- Preserve the author's original structure when it provides clarity (e.g., decision frameworks, comparison matrices)

### Agent Changes (wiki-maintainer.md)

Step 3 currently says:
> "Write summary: wiki/summaries/[source-name].md — link to processed/ segments if applicable. Include summary in frontmatter. Use claim citations ^[source.md] for paragraph-level provenance."

Change to:
> "Write summary: wiki/summaries/[source-name].md — use rich section headings and tables appropriate to the source content. Include a narrative Summary section, custom sections with tables where applicable, section-level citations, and a Key Quotes section. See WIKI_SCHEMA.md → Summary Pages for the full template."

### Workflow Changes (WIKI_WORKFLOWS.md)

Step 2 (Extract key information) — add:
> "Identify structured data suitable for tables (comparisons, tiers, risk matrices, decision guides)"

Step 3 (Write summary page) — update to match the new agent wording, emphasizing:
- Rich section headings over flat bullet lists
- Tables for structured/comparative data
- Narrative Summary section
- Section-level citations

### No Changes Needed

- `CLAUDE.md` — already references the schema for format details
- `WIKI_AGENTS.md` — already defers to WIKI_WORKFLOWS.md for workflow details

## Example: Before vs After

### Before (current, flat)

```markdown
## Key Points
- LLM names encode a soft grammar of family, version, size, alignment stage, and runtime tags^[raw/articles/source.md]
- Parameter size tags signal memory, latency, and quality trade-offs^[raw/articles/source.md]
- Alignment tags (base/instruct/chat) are the strongest first filter^[raw/articles/source.md]

## Quotes
> "Learn to read model names quickly, but never ship based on the name alone."^[raw/articles/source.md]

## Notes
- Source includes a Python parser for extracting tags

## Related
- [[concepts/model_naming]]
```

### After (proposed, rich)

```markdown
## Summary
LLM model names encode practical deployment metadata — family, size, training stage, context window, format, and quantization — enabling fast model selection triage but not replacing benchmarking.^[raw/articles/source.md]

## Anatomy of an LLM Name
Typical pattern: `<family>-<version>-<size>-<alignment>-<context>-<format>-<quant>`

| Component | Example | Meaning |
|-----------|---------|---------|
| Family | Llama, Mistral, Qwen | Architectural lineage |
| Size | 8B, 70B | Parameter count |
| Alignment | Instruct, Chat, Base | Training variant |

## Naming Ambiguity Risks
| Ambiguity | Consequence | Mitigation |
|-----------|-------------|------------|
| Instruct quality varies | Wrong expectations | Benchmark on task set |
| Missing context tag | Truncation surprises | Verify model card |

## Key Quotes
> "Learn to read model names quickly, but never ship based on the name alone."^[raw/articles/source.md]

## Related
- [[concepts/model_naming]]
```

## Files to Modify

1. `schema/WIKI_SCHEMA.md` — Replace Summary Page template, add Style Guide section
2. `.claude/agents/wiki-maintainer.md` — Update step 3 wording
3. `schema/WIKI_WORKFLOWS.md` — Update steps 2 and 3