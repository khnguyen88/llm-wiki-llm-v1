# Wiki Workflows - External Knowledge Base

This file defines the three core operations: Ingest, Query, and Lint for the external knowledge base.

---

## 1. Ingest Workflow

**Purpose**: Process a new source document into the wiki.

**Trigger**: Human adds file to `raw/` and prompts "Process this source"

**Steps**:

1. **Read source document**
   - Load the file from `raw/` directory
   - If it's an image, note its presence for reference

2. **Extract key information**
   - Identify entities (people, places, things, organizations)
   - Identify concepts (ideas, techniques, theories, methods)
   - Extract key claims, facts, and quotes

3. **Write summary page**
   - Create `wiki/summaries/[source-title].md`
   - Include key points, quotes, and notes
   - Add YAML frontmatter with source path

4. **Create/update entity pages**
   - For each identified entity, create or update `wiki/entities/[entity].md`
   - Add facts, relations to other entities
   - Update existing entity if topic expands

5. **Create/update concept pages**
   - For each identified concept, create or update `wiki/concepts/[concept].md`
   - Explain the concept, link to related entities
   - Update existing concept if new information emerges

6. **Update index**
   - Add entries for new pages in `wiki/index.md`
   - Organize by category (entities, concepts, summaries, qanda)

7. **Update log**
   - Append entry to `wiki/log.md`
   - Format: `## [YYYY-MM-DD] ingest | Source Title`

8. **Update cross-references**
   - Add backlinks to related pages
   - Ensure bidirectional linking where appropriate
   - Check for connections between concepts

9. **Update synthesis.md** (if relevant)
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

1. **Broken links**
   - Find `[[wikilinks]]` pointing to non-existent articles
   - Report with severity: error

2. **Orphan pages**
   - Find pages with zero inbound links from other articles
   - Report with severity: warning (may be intentional)

3. **Orphan sources**
   - Find raw sources not yet compiled to wiki
   - Report with severity: suggestion

4. **Stale articles**
   - Find articles whose source has changed since compilation
   - Report with severity: warning

5. **Contradictions**
   - Compare claims across pages for conflicts
   - Requires LLM judgment
   - Report with severity: error

6. **Missing backlinks**
   - Find A links to B but B doesn't link back to A
   - Report with severity: suggestion

7. **Sparse articles**
   - Find articles under 200 words
   - Likely incomplete
   - Report with severity: suggestion

**Output**: Report of issues found with severity levels (error, warning, suggestion)

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
