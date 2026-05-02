# Wiki Workflows - External Knowledge Base

This file defines the four core operations: Ingest, Query, Lint, and Research for the external knowledge base.

---

## 1. Ingest Workflow

**Purpose**: Process a new source document into the wiki.

**Trigger**: Human adds file to `raw/` or `ai-research/` (any subfolder: `articles/`, `papers/`, `repos/`, `datasets/`, `assets/`, `document/`, `web/`, `forum-thread/`, `transcripts/`) and prompts "Process this source"

**Steps**:

0. **Check source size** (pre-processing)
   - If the file is a PDF, binary document, or exceeds ~3,000 words: invoke the document-processor agent to segment it into `processed/`
   - Small markdown files go directly to step 1

1. **Read source document**
   - Load the file from `raw/` or `ai-research/` (small files) or `processed/` (segmented documents)

2. **Extract key information**
   - Identify entities (people, places, things, organizations)
   - Identify concepts (ideas, techniques, theories, methods)
   - Extract key claims, facts, and quotes
   - Identify structured data suitable for tables (comparisons, tiers, risk matrices, decision guides, parameter lists)
   - Assign `confidence` (0.0–1.0) and `provenance` (extracted|merged|inferred|ambiguous) to extracted content

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

4. **Create/update entity pages**
   - For each identified entity, create or update `wiki/entities/[entity].md`
   - Add facts, relations to other entities
   - Include `summary` in frontmatter (one-line description)
   - Set `created`/`updated` timestamps (ISO 8601)
   - When updating existing entities: set `provenance: merged` if combining multiple sources
   - Update existing entity if topic expands

5. **Create/update concept pages**
   - For each identified concept, create or update `wiki/concepts/[concept].md`
   - Explain the concept, link to related entities
   - Include `summary` in frontmatter (one-line description)
   - Set `created`/`updated` timestamps (ISO 8601)
   - When updating existing concepts: set `provenance: merged`, reconcile `confidence` (take minimum across sources)
   - Use claim citations `^[source.md:line-range]` for specific extracted claims
   - Update existing concept if new information emerges

6. **Update index**
   - Add entries for new pages in `wiki/index.md`
   - Organize by category (entities, concepts, summaries, qanda)

7. **Update sources manifest**
   - Add row to `wiki/sources-manifest.md` table
   - Columns: source path, status (`ingested`), wiki page link, date

8. **Update log**
   - Append entry to `wiki/log.md`
   - Format: `## [YYYY-MM-DD] ingest | Source Title`

9. **Update cross-references**
   - Add backlinks to related pages
   - Ensure bidirectional linking where appropriate
   - Check for connections between concepts

10. **Update synthesis.md** (if relevant)
   - Add key takeaways to overarching summary
   - Note how new source changes or confirms existing understanding

**Output**: 5-15 wiki pages updated/created per source

---

## 2. Query Workflow

**Purpose**: Answer questions using the wiki as a knowledge base.

**Trigger**: Human asks a question

**Steps**:

1. **Read index**
   - Load `wiki/index.md` to find relevant pages

2. **Drill into relevant pages**
   - Read summary pages first for context
   - Read entity/concept pages for details
   - Follow links to discover related information

3. **Synthesize answer**
   - Combine information from multiple pages
   - Attribute claims to sources where appropriate
   - Identify any contradictions or gaps
   - Provide citations with `[[wikilinks]]`

4. **Format output**
   - **Markdown page** - For detailed answers
   - **Comparison table** - For comparing items
   - **Slide deck (Marp)** - For presentations
   - **Chart** - For data visualization

5. **Optionally file back**
   - If the answer is valuable, create a new wiki page
   - Add to index and update log
   - This makes future queries more efficient (compounding knowledge)

**Output**: Answer in appropriate format, optionally added to wiki

---

## 3. Lint Workflow

**Purpose**: Health check and maintenance of the wiki.

**Trigger**: Human prompts "Run a health check" or "Lint the wiki"

**Checks**:

### Structural Checks (no LLM judgment needed)

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

8. **Missing summary** (suggestion)
   - Find pages with empty or missing `summary` in frontmatter

9. **Duplicate concept** (error)
   - Find multiple pages with the same title (case-insensitive comparison)

10. **Malformed citation** (error)
    - Find `^[...]` claim citation markers with invalid syntax: non-numeric line ranges, reversed ranges, line 0, or paths not starting with `raw/`, `ai-research/`, or `processed/`

11. **Broken citation** (error)
    - Find `^[source.md]` references pointing to nonexistent source files
    - Find claim citations with line ranges exceeding source file length

### LLM Judgment Check

12. **Contradictions** (error, requires LLM judgment)
    - Compare claims across pages for conflicts
    - When found, add `contradictedBy` to frontmatter of affected pages

**Output**: Report of issues found with severity levels (error, warning, suggestion)

---

## 3b. Repair Workflow

**Purpose**: Act on lint findings to fix structural issues in the wiki.

**Trigger**: Human prompts "Fix broken links", "Resolve orphans", "Repair lint errors"

**Agent**: wiki-repair (see `.claude/agents/wiki-repair.md`)

**Operations**: fix-broken-links, add-backlinks, resolve-orphans, prune-stubs, merge-duplicates, validate-sources, fix-naming

**Boundary**: The repair agent fixes structural defects in existing pages. It does NOT create new content from sources (that is wiki-maintainer's job during ingest). It does NOT run lint checks (that is wiki-linter's job).

**Output**: Changes to wiki files, updated lint score, log entry in `wiki/log.md`

---

## 4. Research Workflow

**Purpose**: Fill knowledge gaps by discovering and saving web sources.

**Trigger**: Human asks to research a topic, or a query reveals gaps the wiki cannot answer from existing sources.

**Steps**:

1. **Search the web** for relevant, high-quality sources on the topic
2. **Save each source as a separate file** in `ai-research/` (one source, one file)
   - Include frontmatter: `url`, `fetched` date, `summary`
   - Save the FULL cleaned content, not a summary
   - Use lowercase hyphenated file names (e.g., `ai-research/web/topic-source-name.md`)
   - Do NOT overwrite existing files — always create new files
3. **Ingest saved sources** into `wiki/` using the standard Ingest workflow
   - A single wiki article can cite multiple `ai-research/` files in its frontmatter `sources:` field
   - The wiki article is where summarization happens, not `ai-research/`
4. **Log the operation** in `wiki/log.md`:
   - Format: `## [YYYY-MM-DD] research | Topic Name | ai-research/path/to/source.md`

**Output**: New source files in `ai-research/`, new/updated wiki pages, updated index and manifest

---

## End-of-Day Compilation

**Automatic Trigger**: If it's past 6 PM local time and today's log has changed

**What happens**:
1. Read all new entries in `wiki/log.md` since last compilation
2. Process each entry through the Ingest workflow
3. Update `synthesis.md` with new understanding
4. Run structural lint checks
5. Report compilation results to `wiki/log.md`

This means the wiki auto-compiles without needing cron jobs or manual triggers.
