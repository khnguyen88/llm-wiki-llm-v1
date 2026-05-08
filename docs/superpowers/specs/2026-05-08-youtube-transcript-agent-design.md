# youtube-transcript Agent Design

## Summary

A project agent (`.claude/agents/youtube-transcript.md`) that extracts YouTube video transcripts via the ytscribe.io API, merges paragraph text with per-paragraph timestamps, resolves metadata, and saves a properly formatted source file to `raw/transcripts/`.

## Identity

- **File**: `.claude/agents/youtube-transcript.md`
- **Name**: `youtube-transcript`
- **Invocation**: "Get transcript for `<youtube-url>`" or "Extract transcript from `<youtube-url>`"
- **Type**: Ephemeral extraction agent — saves one file to `raw/transcripts/`, does not modify wiki/

## Operations

### `extract`

The sole operation. Given a YouTube URL:

1. **Parse video ID** from URL (supports `youtube.com/watch?v=`, `youtu.be/`, `youtube.com/shorts/`, `youtube.com/live/`, and raw 11-char IDs)
2. **Fetch paragraph view**: `curl -s "https://ytscribe.io/api/transcript?v={id}"` — extract `<section id="transcript-paragraphs">` HTML, parse into paragraphs
3. **Fetch timestamped view**: `curl -s "https://ytscribe.io/api/transcript?v={id}&view=timestamped"` — extract `<section id="transcript-timestamped">` HTML, parse `[MM:SS]` timestamps and their associated text phrases
4. **Merge timestamps**: The timestamped view returns short phrases each prefixed with `[MM:SS]`. Walk through the timestamped phrases sequentially and assign them to paragraphs: a phrase belongs to paragraph N if the cumulative text of phrases assigned so far matches the start of paragraph N. The paragraph's timestamp is the timestamp of its first assigned phrase. If a phrase cannot be matched, continue to the next phrase (phrases may be split across paragraph boundaries).
5. **Fetch metadata**: Curl `https://www.youtube.com/oembed?url=https://youtube.com/watch?v={id}&format=json` for channel name and title. If any recommended fields (channel, duration, published_date) are missing, prompt the user
6. **Detect sections**: If the transcript has clear topic-transition words (e.g., "let's switch gears", "now I want to talk about"), optionally flag `sections: true` and add `## Section Title` headers. Default: `sections: false` unless auto-detected or user-specified
7. **Write output file**: Save to `raw/transcripts/{channel-or-topic}-{YYYY-MM-DD}.md` with `video-transcript-llm` metadata header
8. **Confirm**: Print the output file path and a 3-line summary (title, channel, paragraph count)

## Output Format

```markdown
<!--
type: video-transcript-llm
url: https://youtube.com/watch?v=zjkBMFhNj_g
fetched_date: 2026-05-08
extraction_tool: ytscribe-api
channel: Andrej Karpathy
duration: 1:03:47
published_date: 2024-02-13
sections: false
-->

# [1hr Talk] Intro to Large Language Models

[0:00] hi everyone so recently I gave a 30-minute
talk on large language models just kind of like
an intro talk...

[1:02] now many people like this model specifically
because it is probably today the most powerful
open weights model...

[5:30] so how do we get the parameters and where
are they from...
```

Each paragraph starts with a `[MM:SS]` timestamp. Paragraph text preserves original spacing from the API. Section headers (when `sections: true`) use `## Title` format.

## Metadata Resolution

| Field | Source | Fallback |
|-------|--------|----------|
| `type` | Hardcoded `video-transcript-llm` | — |
| `url` | Constructed from video ID | — |
| `fetched_date` | Current date (`date +%Y-%m-%d`) | — |
| `extraction_tool` | Hardcoded `ytscribe-api` | — |
| `channel` | YouTube oEmbed `author_name` | Prompt user |
| `duration` | Parse from YouTube page metadata | Prompt user |
| `published_date` | Parse from YouTube page metadata | Omit (optional) |
| `sections` | Auto-detect or default `false` | — |

## Filename Convention

Following `schema/WIKI_SCHEMA.md`: `raw/transcripts/{channel-or-topic}-{YYYY-MM-DD}.md`

The `{channel-or-topic}` slug is derived from the channel name (kebab-case, e.g., `andrej-karpathy`) or topic if the channel name is generic. The date is the fetched date.

## Extraction Approach

Two-pass (Approach A):

1. **Paragraph view** (`/api/transcript?v={id}`) — provides the paragraph-structured text
2. **Timestamped view** (`/api/transcript?v={id}&view=timestamped`) — provides `[MM:SS]` timestamps per phrase

Merge: walk through timestamped phrases sequentially, assigning each to a paragraph based on cumulative text matching. A phrase belongs to the paragraph whose text it continues. The paragraph's timestamp is its first assigned phrase's timestamp. Phrases may span paragraph boundaries — a phrase that straddles two paragraphs is assigned to the earlier one.

## Error Handling

- **ytscribe API returns error**: Report the error to the user, suggest checking the video ID or trying again
- **Video ID not parseable**: Ask user to provide a valid YouTube URL
- **Transcript empty**: Report that no transcript was found (video may not have captions)
- **Metadata missing**: Prompt user for missing recommended fields before writing the file

## Scope

- Saves to `raw/transcripts/` only — does not segment into `processed/` or ingest into `wiki/`
- Does not modify `wiki/`, `knowledge/`, or any other project files
- If user wants to ingest the transcript into the wiki, they invoke the `wiki-maintainer` agent separately