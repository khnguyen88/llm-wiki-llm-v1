# Remove Batch-Ingester, Standardize on Subagent-Driven Wiki-Maintainer Ingestion

**Date**: 2026-05-01
**Status**: Draft

## Problem

The batch-ingester agent (`scripts/ingest_external.py`) produces lower-quality wiki pages than the wiki-maintainer agent's interactive 10-step Ingest operation. Batch-ingested summaries lack the descriptive depth, cross-referencing, and provenance tracking that subagent-driven ingestion provides. The script-driven approach treats each source as a prompt template call, missing the interactive reconciliation and entity/concept merging that wiki-maintainer performs.

## Decision

Remove the batch-ingester agent, its script, prompt template, and GitHub Actions workflow entirely. Standardize all ingestion on subagent-driven dispatch using the wiki-maintainer agent: one fresh subagent per source, review between tasks, fast iteration.

## Rationale

- **Quality**: Wiki-maintainer's interactive process produces richer, more descriptive wiki pages with proper citations, cross-references, and entity reconciliation. Compare `wiki/summaries/karpathy-github-llm-wiki.md` (subagent-driven) vs. batch-ingested output.
- **Isolation**: Each source gets a dedicated subagent context, preventing cross-contamination and allowing review between tasks.
- **Simplicity**: Removing 587 lines of Python script + prompt template + CI workflow reduces maintenance burden. The sources-manifest and wiki/log already track ingestion state.
- **YAGNI**: No helper script for listing pending sources — `wiki/sources-manifest.md` already tracks what's been ingested.

## Deletions

| File | Reason |
|------|--------|
| `.claude/agents/batch-ingester.md` | Agent definition no longer needed |
| `scripts/ingest_external.py` | Batch ingestion engine — replaced by subagent-driven wiki-maintainer |
| `scripts/prompts/ingest-prompt.txt` | Prompt template for the deleted script |
| `.github/workflows/ingest.yml` | CI workflow that invoked the deleted script |

## Modifications

### Schema Files

**`schema/WIKI_AGENTS.md`**
- Remove the "Batch Ingester Agent" section (lines 128-149)
- Add an "Ingestion Pattern" subsection under general agent guidance:

> **Ingestion Pattern**: All source ingestion uses subagent-driven dispatch — one fresh subagent per source, using the wiki-maintainer agent. The operator reviews between tasks and iterates fast. This produces higher-quality, more descriptive wiki pages than batch script-based ingestion because each source gets full interactive attention with cross-referencing, reconciliation, and provenance tracking.

**`schema/WIKI_WORKFLOWS.md`** — No changes (Ingest workflow is already defined correctly).

**`schema/WIKI_SCHEMA.md`** — No changes (no batch-ingester references).

### Agent Files

**`.claude/agents/sync-check.md`**
- Remove `batch-ingester.md` from file check lists (lines 38, 118)

**`.claude/agents/wiki-maintainer.md`** — No changes (Ingest operation is already correct).

### Top-Level Config

**`CLAUDE.md`**
- Remove the `batch-ingester` row from the agent dispatch table (line 39)
- The wiki-maintainer row already covers "Process this source" / "Ingest X"

**`AGENTS.md`**
- Remove `batch-ingester.md` from project structure tree (line 337)
- Remove "ingest_external.py - Batch Ingest" section (lines 567-585)
- Add a note under Script Details: "Source ingestion is subagent-driven — dispatch one wiki-maintainer subagent per source, review between tasks. See `schema/WIKI_AGENTS.md` → Ingestion Pattern."

### README Files

**`README.md`**
- Remove `batch-ingester.md` from project structure tree (line 146)

**`README-USER-GUIDE.md`**
- Remove `batch-ingester` from agent listing (line 149) and dispatch table (line 197)

**`README-OWNER-GUIDE.md`**
- Remove batch-ingester dispatch rule (line 99)
- Remove known issues entry about max-words default (line 114)

### Spec/Plan Docs

**`docs/superpowers/specs/2026-05-01-restore-lint-checks-and-rebuild-wiki-design.md`**
- Change "Run `batch-ingester` agent" (line 104) to use wiki-maintainer subagent dispatch

**`docs/superpowers/plans/2026-05-01-wiki-knowledge-rebuild.md`**
- Update "batch-ingesting" reference (line 5) to use subagent-driven wiki-maintainer language

**`docs/superpowers/plans/2026-05-01-consistency-fixes-and-user-guides.md`**
- Remove/update all batch-ingester references (lines 24, 42, 333, 338, 377-379, 387, 392, 798, 846, 994, 1009, 1071)

## Ingestion Pattern Documentation

The subagent-driven pattern replaces all batch ingestion:

1. **Dispatch**: For each source, dispatch a fresh subagent using the wiki-maintainer agent
2. **Review**: After each source completes, review the output before moving to the next
3. **Iterate**: Fast iteration — if quality is insufficient, re-dispatch with adjustments
4. **Track**: `wiki/sources-manifest.md` and `wiki/log.md` continue to track ingestion state

This is the same as the existing wiki-maintainer Ingest operation, just invoked per-source via subagent dispatch rather than in bulk via script.

## Out of Scope

- No new scripts or helper tools to replace the deleted `ingest_external.py`
- No changes to wiki-maintainer's Ingest operation (already correct)
- No changes to `schema/WIKI_WORKFLOWS.md` or `schema/WIKI_SCHEMA.md`
- No changes to `.claude/settings.json` (no batch-ingester hooks)