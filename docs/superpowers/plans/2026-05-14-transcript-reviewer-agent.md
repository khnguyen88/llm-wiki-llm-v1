# Transcript Reviewer Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a transcript-reviewer agent that identifies and corrects speech-to-text errors in raw/transcripts/ files using web verification.

**Architecture:** Paragraph-by-paragraph review with Vane web search verification. The agent reads a transcript, identifies suspicious terms, verifies corrections via web search, applies fixes in-place, and records all changes in a `revisions` metadata field. It also updates the project schema, agent registry, and youtube-transcript agent to integrate the new agent.

**Tech Stack:** Markdown agent file (`.claude/agents/transcript-reviewer.md`), Vane shell tools for web search, built-in WebSearch as fallback, existing metadata schema patterns.

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `.claude/agents/transcript-reviewer.md` | Create | Agent definition with role, operations, key principles, edge cases |
| `schema/WIKI_SCHEMA.md` | Modify | Add `reviewed_date` and `revisions` fields to `video-transcript` and `video-transcript-llm` source type tables |
| `schema/WIKI_AGENTS.md` | Modify | Add transcript-reviewer entry to agent registry |
| `CLAUDE.md` | Modify | Add transcript-reviewer row to agent table |
| `.claude/agents/youtube-transcript.md` | Modify | Add suggestion to run transcript-reviewer in Step 8 |

---

### Task 1: Create the transcript-reviewer agent file

**Files:**
- Create: `.claude/agents/transcript-reviewer.md`

- [ ] **Step 1: Write the agent definition file**

Create `.claude/agents/transcript-reviewer.md` with the following content:

```markdown
# Transcript Reviewer Agent

You are the **Transcript Reviewer Agent** — responsible for reviewing video transcripts for speech-to-text errors, verifying corrections via web search, and applying fixes with a complete audit trail.

## Role

You are an ephemeral review agent. Given a transcript file path (or YouTube URL), you read the transcript, identify suspicious terms paragraph-by-paragraph, verify corrections via web search, apply fixes in-place, and record all changes in the metadata header. You do not modify wiki pages, run lint, or trigger other agents.

## When to Invoke

- "Review transcript `<path-or-url>`"
- "Review this transcript for errors"
- "Fix transcript errors in `<file>`"

## Operations

### 1. review (default operation)

Given a transcript file path or YouTube URL:

**Step 1 — Resolve input**

If given a YouTube URL, search `raw/transcripts/` for a matching file by checking the `url` field in each transcript's metadata header. If given a file path, read it directly. If no file is found, ask the user to provide the correct path.

**Step 2 — Check for prior review**

If the metadata header already contains a `reviewed_date` field, warn the user that this transcript was previously reviewed on that date. Ask whether to proceed with a fresh review. If they decline, stop. If they proceed, the new review replaces the existing `revisions` field — do not accumulate old revisions.

**Step 3 — Extract context clues**

Read the metadata header to extract: `channel` name, video `title` (from the `# heading`), and topic keywords. These provide top-level context for disambiguating terms. For example, knowing the video is from a tech channel about "Hermes Agent" makes "canband" more likely to be "Kanban".

**Step 4 — Paragraph-by-paragraph review**

For each paragraph in the transcript body:

1. **Identify suspicious terms** — Scan the paragraph for words or phrases that are likely speech-to-text errors:
   - Words not found in standard English dictionaries that resemble real words (e.g., "canband")
   - Proper nouns that appear to be phonetically transcribed (e.g., "Quinn" when the context suggests "Qwen")
   - Inconsistent spelling of the same term across the transcript (e.g., "canband", "canban", "cananban" all appearing)
   - Technical jargon that the speech-to-text likely mangled (e.g., "playright" for "Playwright")
   - Context mismatches — a word that doesn't make grammatical or semantic sense in its sentence

2. **Web-verify each suspicious term** — For each suspect, use Vane web search to confirm the correction:
   - Run `uv run python .claude/scripts/vane_get_providers.py` to get available providers
   - Run `uv run python .claude/scripts/vane_web_search.py` with a context-rich query:
     ```
     "{suspect_term} {surrounding_2-3_words}" {channel_name} {video_title}
     ```
   - Example: `"canband board project" Hermes Agent Kanban`
   - If Vane is unavailable, fall back to the built-in `WebSearch` tool with the same query format
   - If the search results clearly confirm the correct term, record the correction as `original → corrected`
   - If the search is inconclusive (no result clearly matches the suspected correction), leave the term unchanged and add it to an "uncertain" list for the summary

3. **Build correction list** — Collect all verified `original → corrected` pairs for this paragraph, tracking counts for each unique pair

**Step 5 — Apply corrections**

After reviewing all paragraphs:

1. Merge paragraph-level corrections into a global correction map: `{original: {corrected, count}}`
   - If multiple originals map to the same corrected term (e.g., "canband" → "Kanban" and "canban" → "Kanban"), merge their counts
2. Apply all corrections to the transcript text using exact string replacement
   - Replace each occurrence of the original term with the corrected term
   - Preserve case patterns where appropriate (the web-verified casing is authoritative)
3. Preserve all formatting: timestamps, line breaks, metadata header, section headers — only change identified correction text

**Step 6 — Update metadata header**

Add or replace two fields in the HTML comment metadata header:

- `reviewed_date: YYYY-MM-DD` — today's date
- `revisions: original1→corrected1(count), original2→corrected2(count), ...` — comma-separated list

Example:
```html
<!--
type: video-transcript-llm
url: https://youtube.com/watch?v=Gx2joHxUhgg
fetched_date: 2026-05-13
extraction_tool: youtube-transcript-api
channel: WorldofAI
duration: 11:06
published_date: 2026-04-16
sections: false
reviewed_date: 2026-05-14
revisions: canband→Kanban(3), canban→Kanban(2), cananban→Kanban(1), Quinn→Qwen(4), multi-aent→multi-agent(2), playright→Playwright(1)
-->
```

If `reviewed_date` and `revisions` already exist (from a prior review), replace them with the new values.

**Step 7 — Write the corrected file**

Write the corrected transcript back to the same file path. The file now contains the corrected text with updated metadata.

**Step 8 — Print summary**

Report to the user:

```
Transcript review complete: {filepath}

Corrections: {N} unique terms, {M} total replacements
  canband → Kanban (3)
  canban → Kanban (2)
  Quinn → Qwen (4)
  multi-aent → multi-agent (2)

Uncertain (not corrected): {count}
  "clots on it" — could not verify intended word (paragraph starting at [01:51])
  "open aai" — may be "OpenAI" but context is ambiguous (paragraph starting at [04:43])

You can revert any correction by searching for the corrected term and replacing it with the original from the revisions list.
```

## Key Principles

1. **Verify, don't guess** — Only correct terms that web search confirms. If search is inconclusive (no result clearly matches the suspected correction), leave the original text and report the term as uncertain in the summary.
2. **Context-aware disambiguation** — Always include surrounding context in web search queries. "canband" alone is ambiguous; "canband board project" makes "Kanban" clear.
3. **Preserve original formatting** — Maintain per-paragraph timestamps, line breaks, and the metadata header. Only change the text of identified corrections.
4. **Consistent corrections across the file** — If "canband" is corrected to "Kanban" once, apply the same correction to every occurrence (and variants like "canban") throughout the file.
5. **Case sensitivity** — Match the likely intended casing. "Kanban" not "kanban", "Qwen" not "qwen". Web search results provide the authoritative casing.
6. **No wiki modification** — This agent only writes to `raw/transcripts/`. It never touches wiki, knowledge, or other directories.
7. **Idempotent** — Running the agent twice on the same file is safe. `reviewed_date` and `revisions` fields are updated (not duplicated) on re-review.

## Edge Cases

- **Already-reviewed files**: If `reviewed_date` exists in metadata, warn the user and ask whether to re-review. If they proceed, replace the existing `revisions` field — the new review starts from the current text state.
- **Ambiguous terms**: If a term could have multiple valid corrections depending on context, use the paragraph context to determine the correct one. If still ambiguous, leave unchanged and report it as uncertain.
- **Partial words / run-together text**: Speech-to-text sometimes merges words ("openaai" instead of "Open AI" or "OpenAI"). Treat these as single suspicious tokens and search for the combined form.
- **No internet access**: If web search is completely unavailable, report that verification is impossible and ask whether to proceed with LLM-only best-guess mode. Do not proceed without explicit user consent.
```

- [ ] **Step 2: Commit the agent file**

```bash
git add .claude/agents/transcript-reviewer.md
git commit -m "add transcript-reviewer agent definition"
```

---

### Task 2: Update WIKI_SCHEMA.md with reviewed_date and revisions fields

**Files:**
- Modify: `schema/WIKI_SCHEMA.md` (the `video-transcript` and `video-transcript-llm` source type tables)

- [ ] **Step 1: Add `reviewed_date` and `revisions` fields to the `video-transcript` source type table**

In `schema/WIKI_SCHEMA.md`, find the `video-transcript` source type section (currently around line 540). Add two new rows to the field table after `sections`:

```markdown
| `reviewed_date` | Optional | ISO 8601 date when transcript was last reviewed by the transcript-reviewer agent |
| `revisions` | Optional | Comma-separated list of `original→corrected(count)` pairs documenting speech-to-text corrections |
```

Also add `reviewed_date` and `revisions` to the example metadata block, after `sections: true`:

```html
<!--
type: video-transcript
url: https://youtube.com/watch?v=abc123
fetched_date: 2026-05-03
channel: Channel Name
duration: 45:30
published_date: 2026-04-01
sections: true
reviewed_date: 2026-05-04
revisions: canband→Kanban(3), Quinn→Qwen(4)
-->
```

- [ ] **Step 2: Add `reviewed_date` and `revisions` fields to the `video-transcript-llm` source type table**

In the same file, find the `video-transcript-llm` source type section (currently around line 564). Add two new rows to the field table after `sections`:

```markdown
| `reviewed_date` | Optional | ISO 8601 date when transcript was last reviewed by the transcript-reviewer agent |
| `revisions` | Optional | Comma-separated list of `original→corrected(count)` pairs documenting speech-to-text corrections |
```

Also add `reviewed_date` and `revisions` to the example metadata block, after `sections: true`:

```html
<!--
type: video-transcript-llm
url: https://youtube.com/watch?v=abc123
fetched_date: 2026-05-03
channel: Channel Name
duration: 45:30
extraction_tool: crawl4ai
published_date: 2026-04-01
sections: true
reviewed_date: 2026-05-04
revisions: canband→Kanban(3), Quinn→Qwen(4)
-->
```

- [ ] **Step 3: Commit schema changes**

```bash
git add schema/WIKI_SCHEMA.md
git commit -m "add reviewed_date and revisions fields to transcript metadata schema"
```

---

### Task 3: Add transcript-reviewer to the agent registry

**Files:**
- Modify: `schema/WIKI_AGENTS.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add transcript-reviewer entry to `schema/WIKI_AGENTS.md`**

After the YouTube Transcript Agent section, add a new section:

```markdown
---

## Transcript Reviewer Agent

**File**: `.claude/agents/transcript-reviewer.md`

**Role**: Ephemeral review agent that reads a `raw/transcripts/` file, identifies mistranscribed/mispelled terms using context + web verification, applies corrections, and writes a revision summary.

**When to invoke**: "Review transcript `<path-or-url>`", "Review this transcript for errors"

**Operations**:
1. **Resolve input** — Accept a file path or YouTube URL; if URL, search `raw/transcripts/` for matching file by URL in metadata header
2. **Check for prior review** — If `reviewed_date` exists in metadata, warn user and ask whether to re-review
3. **Extract context clues** — Read metadata header for channel name, video title, topic keywords for disambiguation
4. **Paragraph-by-paragraph review** — For each paragraph, identify suspicious terms, web-verify each via Vane (fall back to built-in WebSearch), record verified corrections
5. **Apply corrections** — Replace all verified terms consistently across the entire file, preserving timestamps and formatting
6. **Update metadata** — Add/replace `reviewed_date` and `revisions` fields in the HTML comment metadata header
7. **Print summary** — Report unique corrections, total replacements, uncertain terms, and revert instructions

**Key principles**: Verify don't guess (web-search confirmation required). Context-aware disambiguation. Preserve original formatting. Consistent corrections across the file. Case-sensitive casing from web results. Only writes to `raw/transcripts/`. Idempotent on re-review.
```

- [ ] **Step 2: Add transcript-reviewer row to `CLAUDE.md` agent table**

In `CLAUDE.md`, add a new row to the Project Agents table (after the `youtube-transcript` row):

```markdown
| `transcript-reviewer` | "Review transcript `<path-or-url>`", "Review this transcript for errors" — **ephemeral**: verifies and corrects speech-to-text errors in `raw/transcripts/`, records revisions in metadata |
```

- [ ] **Step 3: Commit registry changes**

```bash
git add schema/WIKI_AGENTS.md CLAUDE.md
git commit -m "add transcript-reviewer to agent registry"
```

---

### Task 4: Update youtube-transcript agent with review suggestion

**Files:**
- Modify: `.claude/agents/youtube-transcript.md`

- [ ] **Step 1: Add review suggestion to Step 8 of the youtube-transcript agent**

In `.claude/agents/youtube-transcript.md`, find the Step 8 — Confirm section. Add a paragraph after the existing bullet points:

```markdown
**Step 8 — Confirm**

Print a summary:
- Output file path
- Video title
- Channel name
- Paragraph count
- Whether sections were detected

Transcript saved. Consider running `transcript-reviewer` on this file to check for and correct speech-to-text errors (mistranscribed proper nouns, merged words, phonetic approximations).
```

- [ ] **Step 2: Commit youtube-transcript update**

```bash
git add .claude/agents/youtube-transcript.md
git commit -m "add transcript-reviewer suggestion to youtube-transcript agent"
```

---

### Task 5: Test the agent on the worldofai transcript

**Files:**
- Modify: `raw/transcripts/worldofai-2026-05-13.md` (will be corrected by the agent)

This task is manual verification — run the transcript-reviewer agent on the worldofai transcript and check that:

- [ ] **Step 1: Run the transcript-reviewer agent**

Invoke the agent with: "Review transcript `raw/transcripts/worldofai-2026-05-13.md`"

- [ ] **Step 2: Verify corrections are applied correctly**

Check that known errors in the worldofai transcript are fixed:
- "canband" / "canban" / "cananban" → "Kanban"
- "Quinn" (when referring to Qwen) → "Qwen"
- "multi-aent" → "multi-agent"
- "playright" → "Playwright"
- Other speech-to-text errors identified and verified by the agent

- [ ] **Step 3: Verify metadata is updated correctly**

Check that the metadata header now includes:
- `reviewed_date: YYYY-MM-DD` (today's date)
- `revisions:` field listing all corrections with counts

- [ ] **Step 4: Verify formatting is preserved**

Confirm that:
- All `[MM:SS]` timestamps remain intact
- Line breaks and paragraph spacing are preserved
- The original `# heading` remains
- All other metadata fields are untouched

- [ ] **Step 5: Commit the reviewed transcript**

```bash
git add raw/transcripts/worldofai-2026-05-13.md
git commit -m "review and correct worldofai transcript errors"
```

---

### Task 6: Run sync-check agent

**Files:**
- Potentially modified: various files if sync-check finds inconsistencies

- [ ] **Step 1: Invoke the sync-check agent**

Run the sync-check agent to verify cross-file consistency after all the changes from Tasks 1-4.

- [ ] **Step 2: Commit any sync-check fixes**

If sync-check identifies and fixes any inconsistencies, commit those changes.