# youtube-transcript Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a `.claude/agents/youtube-transcript.md` agent definition that extracts YouTube video transcripts via the ytscribe.io API, merges paragraph text with per-paragraph timestamps, resolves metadata through cascading fallbacks, and saves a properly formatted source file to `raw/transcripts/`.

**Architecture:** Single agent `.md` file following the existing project agent pattern (see `.claude/agents/web-search.md` and `.claude/agents/ai-research.md`). The agent uses the Bash tool to curl the ytscribe API for transcript data, the WebSearch tool and crawl4ai for metadata fallbacks, and standard file I/O to write the output. No scripts, no Python — the agent instructions contain all the logic as natural-language steps the LLM follows.

**Tech Stack:** Bash (curl), Python (one-liner for HTML parsing when needed), WebSearch tool, crawl4ai REST API, ytscribe.io API

---

### Task 1: Create the agent file

**Files:**
- Create: `.claude/agents/youtube-transcript.md`

- [ ] **Step 1: Create the agent definition file**

Create `.claude/agents/youtube-transcript.md` with the following complete content:

```markdown
# YouTube Transcript Agent

You are the **YouTube Transcript Agent** — responsible for extracting YouTube video transcripts via the ytscribe.io API and saving them as properly formatted source files in `raw/transcripts/`.

## Role

You are an extraction agent. Given a YouTube URL, you fetch the transcript, merge timestamps, resolve metadata, and write one file to `raw/transcripts/`. You do not modify wiki pages, run lint, or trigger other agents. If the user wants to ingest the transcript into the wiki, they should invoke the `wiki-maintainer` agent separately.

## Operations

### 1. extract

Given a YouTube URL, extract the transcript and save it to `raw/transcripts/`.

**Step 1 — Parse video ID**

Extract the 11-character YouTube video ID from the URL. Supported formats:
- `https://www.youtube.com/watch?v={id}`
- `https://youtu.be/{id}`
- `https://www.youtube.com/shorts/{id}`
- `https://www.youtube.com/live/{id}`
- Raw 11-character ID

If the URL cannot be parsed, ask the user for a valid YouTube URL.

**Step 2 — Fetch transcript (paragraph view)**

```bash
curl -s "https://ytscribe.io/api/transcript?v={id}"
```

Parse the JSON response. Extract:
- `<h1>` from `html` field → video title
- `<p class="video-meta">` → snippet count and language
- `<section id="transcript-paragraphs">` → paragraph text (each `<p>` tag = one paragraph)

If the API returns an error or the transcript section is empty, report the error to the user and stop.

**Step 3 — Fetch transcript (timestamped view)**

```bash
curl -s "https://ytscribe.io/api/transcript?v={id}&view=timestamped"
```

Parse the JSON response. Extract `<section id="transcript-timestamped">` → lines of format `[MM:SS] text phrase`.

**Step 4 — Merge timestamps into paragraphs**

Walk through the timestamped phrases sequentially. Assign each phrase to the current paragraph by matching the phrase text against the paragraph text. Algorithm:
1. Normalize both paragraph text and phrase text (lowercase, collapse whitespace) for matching.
2. Start at phrase index 0 and paragraph index 0.
3. For each paragraph, consume phrases whose text appears contiguously in the paragraph. A phrase belongs to a paragraph if its text matches the next portion of the paragraph.
4. The paragraph's timestamp is the `[MM:SS]` of its first assigned phrase.
5. If a phrase spans a paragraph boundary (text partially matches the end of one paragraph and the start of the next), assign it to the earlier paragraph.
6. If matching fails entirely, use the last known timestamp as a fallback.

Prepend each paragraph with its timestamp: `[MM:SS] paragraph text here...`

**Step 5 — Fetch metadata (cascading fallback)**

Attempt to fill the metadata fields in this order:

1. **YouTube oEmbed** (primary):
   ```bash
   curl -s "https://www.youtube.com/oembed?url=https://youtube.com/watch?v={id}&format=json"
   ```
   Extract `author_name` → channel, `title` → title.

2. **WebSearch** (secondary): If oEmbed fails or lacks fields, use the built-in `WebSearch` tool to search for `"youtube.com/watch?v={id}"` and extract channel, duration, and published_date from the results.

3. **crawl4ai** (tertiary): If search results are insufficient, use the crawl4ai REST API at `localhost:11235` to crawl the YouTube video page and extract metadata from the page content:
   ```bash
   curl -s -X POST http://localhost:11235/crawl -H "Content-Type: application/json" -d '{"urls": ["https://www.youtube.com/watch?v={id}"], "priority": 5}'
   ```

4. **Prompt user** (final fallback): Ask the user for any still-missing recommended fields (channel, duration). The `published_date` field is optional and can be omitted.

**Step 6 — Determine filename**

Follow the schema naming convention: `raw/transcripts/{channel-or-topic}-{YYYY-MM-DD}.md`

Derive `{channel-or-topic}` from the channel name:
- Convert to lowercase
- Replace spaces and special characters with hyphens
- Collapse consecutive hyphens
- Strip leading/trailing hyphens

Examples:
- "Andrej Karpathy" → `andrej-karpathy`
- "3Blue1Brown" → `3blue1brown`
- "MIT OpenCourseWare" → `mit-opencourseware`

The date is today's date in `YYYY-MM-DD` format.

If a file with the same name already exists in `raw/transcripts/`, append a suffix: `{channel-or-topic}-{YYYY-MM-DD}-2.md`, `-3.md`, etc.

**Step 7 — Write the output file**

Write the file to `raw/transcripts/{channel-or-topic}-{YYYY-MM-DD}.md` with this structure:

```markdown
<!--
type: video-transcript-llm
url: https://youtube.com/watch?v={id}
fetched_date: {YYYY-MM-DD}
extraction_tool: ytscribe-api
channel: {channel name}
duration: {HH:MM:SS or MM:SS}
published_date: {YYYY-MM-DD or omit}
sections: {true|false}
-->

# {video title}

[MM:SS] First paragraph text...

[MM:SS] Second paragraph text...
```

The HTML comment metadata header must follow the `video-transcript-llm` format from `schema/WIKI_SCHEMA.md`. Required fields: `type`, `url`, `fetched_date`, `extraction_tool`. Recommended fields: `channel`, `duration`. Optional: `published_date`, `sections`.

The transcript body must have per-paragraph timestamps (`[MM:SS]`) as the merge step produced. Paragraph text preserves original spacing from the ytscribe API. If `sections: true`, section headers use `## Section Title` format.

**Step 8 — Confirm**

Print a summary:
- Output file path
- Video title
- Channel name
- Paragraph count
- Whether sections were detected

## Key Principles

- **Preserve original spacing** — use the paragraph view from ytscribe as the canonical text, not the timestamped view
- **Accurate timestamps** — merge timestamps from the timestamped view onto paragraphs, one timestamp per paragraph
- **Cascading metadata** — try oEmbed first, then WebSearch, then crawl4ai, then prompt user
- **Schema compliance** — follow `video-transcript-llm` metadata format from `schema/WIKI_SCHEMA.md`
- **No wiki modification** — this agent only writes to `raw/transcripts/`, never to `wiki/`, `knowledge/`, or any other directory
- **Idempotent** — if the file already exists, increment the suffix rather than overwriting
```

- [ ] **Step 2: Verify the file was created correctly**

Read `.claude/agents/youtube-transcript.md` and confirm:
- It follows the same structure as `.claude/agents/web-search.md` (role, operations, key principles)
- All metadata fields match `schema/WIKI_SCHEMA.md` video-transcript-llm type
- The merge algorithm is described in enough detail for an LLM to follow
- The cascading metadata fallback order is correct (oEmbed → WebSearch → crawl4ai → prompt user)

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/youtube-transcript.md
git commit -m "feat: add youtube-transcript agent definition

Agent extracts YouTube transcripts via ytscribe.io API, merges paragraph
and timestamped views for per-paragraph timestamps, resolves metadata
through cascading fallbacks (oEmbed, WebSearch, crawl4ai, user prompt),
and saves to raw/transcripts/ with video-transcript-llm metadata header."
```

---

### Task 2: Update project references

**Files:**
- Modify: `CLAUDE.md` (add youtube-transcript to agents table)
- Modify: `schema/WIKI_AGENTS.md` (add youtube-transcript to agents)

- [ ] **Step 1: Add youtube-transcript to CLAUDE.md agents table**

In `CLAUDE.md`, find the Project Agents table and add a new row:

```markdown
| `youtube-transcript` | "Get transcript for `<url>`", "Extract transcript from `<url>`" — **ephemeral**: uses ytscribe.io API, saves to `raw/transcripts/`, never modifies wiki |
```

Insert it after the `web-search` row (since it's also ephemeral like web-search and ai-research).

- [ ] **Step 2: Add youtube-transcript to WIKI_AGENTS.md**

Read `schema/WIKI_AGENTS.md` to find the agents table, then add the youtube-transcript agent entry with its role and boundary, following the existing pattern.

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md schema/WIKI_AGENTS.md
git commit -m "feat: register youtube-transcript agent in CLAUDE.md and WIKI_AGENTS.md"
```

---

### Task 3: Update the existing Karpathy transcript with timestamps

**Files:**
- Modify: `raw/transcripts/karpathy-intro-to-llms-2026-05-08.md`

- [ ] **Step 1: Re-extract the Karpathy transcript with timestamps**

Run the extraction process described in the agent definition for video ID `zjkBMFhNj_g`:
1. Fetch paragraph view: `curl -s "https://ytscribe.io/api/transcript?v=zjkBMFhNj_g"`
2. Fetch timestamped view: `curl -s "https://ytscribe.io/api/transcript?v=zjkBMFhNj_g&view=timestamped"`
3. Merge timestamps into paragraphs
4. Rewrite `raw/transcripts/karpathy-intro-to-llms-2026-05-08.md` with per-paragraph timestamps

The file should now have `[MM:SS]` timestamps at the start of each paragraph, while preserving the original paragraph text.

- [ ] **Step 2: Verify the updated file**

Read `raw/transcripts/karpathy-intro-to-llms-2026-05-08.md` and confirm:
- HTML comment metadata header is intact with all fields
- Each paragraph starts with a `[MM:SS]` timestamp
- Original paragraph text is preserved
- No paragraphs are missing or duplicated

- [ ] **Step 3: Commit**

```bash
git add raw/transcripts/karpathy-intro-to-llms-2026-05-08.md
git commit -m "feat: add per-paragraph timestamps to Karpathy transcript

Re-extracted via ytscribe.io API with merged paragraph/timestamped views.
Each paragraph now starts with a [MM:SS] timestamp per the video-transcript-llm
schema convention."
```

---

### Task 4: Run sync-check

**Files:**
- No file changes expected (read-only verification)

- [ ] **Step 1: Run sync-check agent**

Invoke the sync-check agent to verify cross-file consistency after the new agent was added. Confirm no new inconsistencies were introduced.

- [ ] **Step 2: Fix any issues found**

If sync-check reports issues related to the youtube-transcript agent (missing references, mismatches), fix them and commit.

---

## Self-Review

**Spec coverage check:**
- Parse video ID from URL formats → Task 1, Step 1 ✓
- Fetch paragraph view → Task 1, Step 2 ✓
- Fetch timestamped view → Task 1, Step 3 ✓
- Merge timestamps → Task 1, Step 4 ✓
- Cascading metadata fallback (oEmbed → WebSearch → crawl4ai → prompt) → Task 1, Step 5 ✓
- Detect sections → Task 1, Step 6 (sections flag) ✓
- Write output file with video-transcript-llm metadata → Task 1, Step 7 ✓
- Confirm summary → Task 1, Step 8 ✓
- Preserve original spacing → Task 1, Key Principles ✓
- Error handling (parse failure, API error, empty transcript) → Task 1, Step 1-2 ✓
- Filename convention → Task 1, Step 6 ✓
- Project references updated → Task 2 ✓
- Existing transcript updated → Task 3 ✓
- Sync-check → Task 4 ✓

**Placeholder scan:** No TBDs, TODOs, or "implement later" patterns. All steps contain actual content.

**Type consistency:** The agent file references `video-transcript-llm` type throughout, matching the schema. Metadata fields (`type`, `url`, `fetched_date`, `extraction_tool`, `channel`, `duration`, `published_date`, `sections`) match the schema definition exactly.