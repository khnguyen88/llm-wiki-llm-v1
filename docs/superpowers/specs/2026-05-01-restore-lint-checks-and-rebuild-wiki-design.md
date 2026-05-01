# Design: Restore 4 Lint Checks & Rebuild Wiki

Date: 2026-05-01

## Background

Four lint checks were removed from documentation in commit `4b7ffc8` because they were never implemented in `scripts/lint.py` — they existed only in specs. The sync-check agent caught this doc-code mismatch, and the fix was to remove the specs rather than implement the checks.

However, these checks address real quality concerns:
- Missing summaries make wiki pages harder to navigate and index
- Duplicate concepts silently fragment knowledge
- Citations without validation can point to nonexistent sources
- Malformed citations undermine provenance tracking

Additionally, some docs still reference the removed checks (WIKI_SCHEMA.md, wiki-maintainer.md), creating new inconsistencies.

## Decision

Restore all 4 checks as working implementations in `lint.py`, update all documentation to reflect a 12-check specification, and rebuild the wiki from scratch so all pages conform to the updated schema.

Order: **checks first, then wiki rebuild.** The new checks will validate the rebuilt wiki as it's created.

## Lint Check Implementations

All 4 checks follow the existing `check_<name>_<kb>() -> list[dict]` pattern in `scripts/lint.py`.

### Check 8: Missing Summary (suggestion)

- **Internal**: `check_missing_summary_internal()`
- **External**: `check_missing_summary_external()`
- Scan every page's frontmatter for the `summary` field
- Flag pages where `summary` is missing or an empty string
- Issue dict: `{severity: "suggestion", check: "missing_summary", kb: ..., file: ..., detail: "Missing summary field in frontmatter"}`

### Check 9: Duplicate Concept (error)

- **Internal**: `check_duplicate_concept_internal()`
- **External**: `check_duplicate_concept_external()`
- Build a `dict[str, list[str]]` mapping lowercase title → list of file paths
- After scanning all pages, any title with 2+ entries is flagged
- Issue dict: `{severity: "error", check: "duplicate_concept", kb: ..., file: ..., detail: "Duplicate title 'X' also in: file1, file2"}`

### Check 10: Malformed Citation (error)

- **External only**: `check_malformed_citation_external()`
- No internal variant — internal KB (`knowledge/`) doesn't use claim citations
- Regex: `\^\[([^\]]+)\]` to find all `^[...]` markers in wiki page bodies
- Valid citation syntax: `^[<path>]` or `^[<path>:<line>]` or `^[<path>:<start>-<end>]`
- Path must start with `raw/`, `ai-research/`, or `processed/`
- Line numbers must be positive integers; ranges must have end >= start
- Flag violations: invalid path prefix, non-numeric lines, reversed ranges, missing brackets
- Issue dict: `{severity: "error", check: "malformed_citation", kb: "external", file: ..., detail: "..."}`

### Check 11: Broken Citation (error)

- **External only**: `check_broken_citation_external()`
- No internal variant — internal KB doesn't use claim citations
- For each valid citation marker, resolve the source path against the filesystem
- Flag if the referenced file doesn't exist
- For line-range citations, read the source file and flag if the range exceeds the file's line count
- Valid path prefixes: `raw/`, `ai-research/`, `processed/`
- Issue dict: `{severity: "error", check: "broken_citation", kb: "external", file: ..., detail: "..."}`

### Registration

In `main()`, add 2 new check entries to `internal_checks` (missing_summary, duplicate_concept) and 4 to `external_checks` (all four). Update the docstring from "Runs 8 checks" to "Runs 12 checks".

## Documentation Updates

All files referencing lint checks must be updated from 8→12:

| File | Change |
|---|---|
| `schema/WIKI_WORKFLOWS.md` | Add checks 8-11 to the lint specification section |
| `schema/WIKI_AGENTS.md` | "8-check specification" → "12-check specification" |
| `schema/WIKI_SCHEMA.md` | Citation validation reference now points to real (implemented) checks |
| `.claude/agents/wiki-linter.md` | Add checks 8-11 to the linter agent's check list |
| `.claude/agents/wiki-maintainer.md` | Already lists 12 checks — confirm the 4 are present and not marked as removed |
| `.claude/agents/knowledge-compiler.md` | "8 health checks" → "12 health checks" |
| `AGENTS.md` | Update lint table (add 4 rows) and count references (8→12) |
| `scripts/lint.py` | Docstring: "Runs 8 checks" → "Runs 12 checks" |
| `README-OWNER-GUIDE.md` | "8 structural + 1 LLM" → "12 structural + 1 LLM", remove note about 4 unimplemented checks |
| `README.md` | "Expanded linter from 8 to 12 checks" is now accurate again |

After all changes, run the sync-check agent to verify consistency.

## Wiki Rebuild

### What gets deleted

- `wiki/` — entire directory (all compiled articles)
- `knowledge/` — entire directory (internal KB articles)

### What gets preserved

- `raw/` — human-curated sources (read-only)
- `ai-research/` — LLM-discovered sources (immutable once saved)
- `processed/` — segmented markdown from large raw files (LLM-owned but immutable)
- `daily/` — conversation logs (immutable)

### Rebuild steps

1. Delete `wiki/` and `knowledge/` directories
2. Re-ingest all sources from `raw/` and `ai-research/` using wiki-maintainer subagent dispatch
3. Run `knowledge-compiler` agent to rebuild `knowledge/` from `daily/` logs
4. Run `wiki-linter` agent with `--structural-only` to validate all 12 checks
5. Fix any lint issues found during validation
6. Run `wiki-linter` agent again (with LLM contradiction check) for full validation

### Expected outcomes

- All wiki pages will have proper `summary` fields (check 8 validates this)
- All wiki pages will have unique titles (check 9 validates this)
- Any claim citations generated by wiki-maintainer will be syntactically valid (check 10) and point to real files (check 11)
- Frontmatter will use `created`/`updated` instead of the old `date` field