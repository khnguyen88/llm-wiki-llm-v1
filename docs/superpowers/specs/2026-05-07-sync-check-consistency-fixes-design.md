# Sync Check Consistency Fixes

**Date:** 2026-05-07
**Scope:** Fix 5 inconsistencies found by sync-check across 3 files
**Approach:** Direct file edits (Approach A)

## Problem

The 2026-05-07 sync-check identified 5 inconsistencies across 3 files:

1. **README.md lines 135-143**: `.claude/agents/` tree lists 8 agents, missing `web-search.md` and `ai-research.md`
2. **wiki/index.md**: 131 entity links use `[[entitie/...]]` instead of `[[entities/...]]`
3. **wiki/index.md**: 60 concept links use `[[concept/...]]` instead of `[[concepts/...]]`
4. **wiki/sources-manifest.md**: 143 stray pipe-delimited data rows between frontmatter and the proper markdown table (lines 9-151)

AGENTS.md and all other config files are verified consistent — no changes needed there.

## Design

### Fix 1: README.md — Add missing agents to project structure tree

**File:** `README.md`
**Lines:** 135-143

Change the `.claude/agents/` subtree from:

```
│   └── agents/                   # Project-specific agents
│       ├── wiki-maintainer.md
│       ├── document-processor.md
│       ├── knowledge-compiler.md
│       ├── wiki-linter.md
│       ├── wiki-query.md
│       ├── wiki-repair.md
│       ├── sync-check.md
│       └── context-loader.md
```

To:

```
│   └── agents/                   # Project-specific agents
│       ├── wiki-maintainer.md
│       ├── document-processor.md
│       ├── knowledge-compiler.md
│       ├── wiki-linter.md
│       ├── wiki-query.md
│       ├── wiki-repair.md
│       ├── sync-check.md
│       ├── context-loader.md
│       ├── web-search.md
│       └── ai-research.md
```

The tree connector for `context-loader.md` changes from `└──` to `├──`, and `ai-research.md` becomes the new `└──`.

### Fix 2: wiki/index.md — Correct entity wikilink paths

**File:** `wiki/index.md`

Replace all occurrences of `[[entitie/` with `[[entities/` (131 instances). The directory is `wiki/entities/` — the wikilink path must match.

### Fix 3: wiki/index.md — Correct concept wikilink paths

**File:** `wiki/index.md`

Replace all occurrences of `[[concept/` with `[[concepts/` (60 instances). The directory is `wiki/concepts/` — the wikilink path must match.

### Fix 4: wiki/sources-manifest.md — Remove stray data rows

**File:** `wiki/sources-manifest.md`

Remove lines 9-151, which contain pipe-delimited data rows that are duplicates of the proper markdown table starting at line 153. Keep:
- Lines 1-8: YAML frontmatter
- Line 9: blank line after frontmatter (will be preserved)
- Lines 153+: The proper `# Sources Manifest` heading, table header, separator, and data rows

The resulting file will have frontmatter, a blank line, then the proper markdown table with no duplicate rows between them.

## Verification

After all fixes:
1. `grep -c 'entitie/' wiki/index.md` should return 0
2. `grep -c '\[\[concept/' wiki/index.md` should return 0 (exact wikilink prefix, won't match `[[concepts/`)
3. README.md `.claude/agents/` subtree should list 10 agents
4. wiki/sources-manifest.md should have frontmatter → blank line → markdown table, with no stray rows