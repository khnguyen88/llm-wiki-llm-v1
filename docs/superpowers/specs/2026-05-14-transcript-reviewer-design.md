# Transcript Reviewer Agent — Design Spec

**Date:** 2026-05-14
**Status:** Draft

## Problem

YouTube transcripts extracted by the `youtube-transcript` agent frequently contain speech-to-text errors — mistranscribed proper nouns (e.g., "canband" for "Kanban", "Quinn" for "Qwen"), merged words ("openaai" for "OpenAI"), and phonetic approximations of technical jargon. These errors propagate into the wiki when transcripts are ingested, degrading knowledge quality.

## Solution

Create a `transcript-reviewer` agent that reads a `raw/transcripts/` file, identifies suspicious terms paragraph-by-paragraph, verifies corrections via web search, applies fixes in-place, and records all changes in a `revisions` metadata field for auditability and reversibility.

## Agent Definition

**Name:** `transcript-reviewer`
**File:** `.claude/agents/transcript-reviewer.md`
**Role:** Ephemeral review agent — reads a transcript, identifies and verifies mistranscribed terms, applies corrections, writes revision summary.
**Scope:** Only `raw/transcripts/` files. Does not touch wiki, knowledge, or any other directory.
**When to invoke:** "Review transcript `<path-or-url>`", "Review this transcript for errors"

### Auto-suggestion (not auto-trigger)

The `youtube-transcript` agent's confirmation step (Step 8) should append a suggestion to its output:

> "Transcript saved. Run `transcript-reviewer` on this file to check for transcription errors."

This is a suggestion only — the user decides whether to run it.

## Operations

### `review` (default operation)

Given a transcript file path or YouTube URL:

**Step 1 — Resolve input**

If given a YouTube URL, search `raw/transcripts/` for a matching file (by URL in metadata header or by channel-date pattern). If given a path, read it directly. If no file found, ask the user.

**Step 2 — Extract context clues**

Read the metadata header to extract: channel name, video title, topic keywords. These provide top-level context for disambiguating terms (e.g., knowing it's a tech video makes "Quinn" more likely to be "Qwen").

**Step 3 — Paragraph-by-paragraph review**

For each paragraph in the transcript:

1. **Identify suspicious terms** — Look for:
   - Words not in standard dictionaries that resemble real words
   - Proper nouns that seem phonetically transcribed (e.g., "canband" → "Kanban")
   - Inconsistent spelling of the same term across the transcript
   - Technical jargon likely mangled by speech-to-text
   - Context mismatches (a word that doesn't make grammatical/semantic sense in its sentence)

2. **Web-verify** — For each suspicious term, search using Vane (`vane_web_search`) with a query that includes surrounding context:
   - Query format: `"{suspect_term} {surrounding_context}" {channel_name} {video_title}`
   - Example: `"canband board project" Hermes Agent Kanban`
   - Fall back to built-in `WebSearch` if Vane is unavailable
   - If search confirms the correct term, record the correction
   - If search is inconclusive, skip the term (don't guess)

3. **Record corrections** — Build a list of `original → corrected` pairs for the paragraph

**Step 4 — Apply corrections**

Write the corrected transcript back to the same file path. Each mistranscribed word is replaced with the verified correction. Maintain per-paragraph timestamps, line breaks, and the metadata header — only change the text of identified corrections.

**Step 5 — Update metadata header**

Add/replace `reviewed_date` and `revisions` fields in the HTML comment metadata header:

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
revisions: canband→Kanban(3), canban→Kanban(2), cananban→Kanban(1), Quinn→Qwen(4), multi-aent→multi-agent(2), playright→Playwright(1), clots on it→Claude(1), open aai→OpenAI(2)
-->
```

The `revisions` field format: `original→corrected(count)`, comma-separated. Count = number of occurrences replaced. This gives the user a complete audit trail — they can search-and-replace any correction back to the original if they disagree.

**Step 6 — Print summary**

Report to the user:
- Number of unique corrections made
- Total number of word replacements
- List of all corrections with counts
- Note that the user can revert any change using the revisions list

## Key Principles

1. **Verify, don't guess** — Only correct terms that web search confirms. If search is inconclusive, leave the original text and note it as uncertain.
2. **Context-aware disambiguation** — Always include surrounding context in web search queries. "canband" alone is ambiguous; "canband board project" makes "Kanban" clear.
3. **Preserve original formatting** — Maintain per-paragraph timestamps, line breaks, and the metadata header. Only change the text of identified corrections.
4. **Consistent corrections across the file** — If "canband" is corrected to "Kanban" once, apply the same correction to every occurrence (and variants like "canban") throughout the file.
5. **Case sensitivity** — Match the likely intended casing. "Kanban" not "kanban", "Qwen" not "qwen". Web search results provide the authoritative casing.
6. **No wiki modification** — This agent only writes to `raw/transcripts/`. It never touches wiki, knowledge, or other directories.
7. **Idempotent** — Running the agent twice on the same file is safe. `reviewed_date` and `revisions` fields are updated (not duplicated) on re-review.

## Edge Cases

- **Already-reviewed files:** If `reviewed_date` exists in metadata, warn the user and ask whether to re-review. If they proceed, replace the existing `revisions` field (don't accumulate old revisions — the new review starts from the current text state).
- **Ambiguous terms:** If a term could have multiple valid corrections depending on context, use the paragraph context to determine the correct one. If still ambiguous, leave unchanged and report it.
- **Partial words / run-together text:** Speech-to-text sometimes merges words ("openaai" instead of "Open AI" or "OpenAI"). Treat these as single suspicious tokens and search for the combined form.
- **No internet access:** If web search is completely unavailable, report that verification is impossible and ask whether to proceed with LLM-only best-guess mode. Do not proceed without explicit user consent.

## Schema Updates

Add `reviewed_date` and `revisions` to the `video-transcript-llm` metadata format in `schema/WIKI_SCHEMA.md`:

- `reviewed_date` (optional, ISO 8601 date) — Date the transcript was last reviewed
- `revisions` (optional, string) — Comma-separated list of `original→corrected(count)` pairs

## Agent Registry Updates

Add `transcript-reviewer` to:
- `CLAUDE.md` agent table
- `schema/WIKI_AGENTS.md` agent registry
- `.claude/agents/` directory

Update `youtube-transcript` agent's Step 8 (confirmation) to include a suggestion to run `transcript-reviewer`.