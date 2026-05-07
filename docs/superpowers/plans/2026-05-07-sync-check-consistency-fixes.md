# Sync Check Consistency Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix 5 inconsistencies found by the 2026-05-07 sync-check across 3 files

**Architecture:** Direct file edits — targeted find-and-replace and line deletions. No new files, no scripts, no structural changes.

**Tech Stack:** Markdown files only (README.md, wiki/index.md, wiki/sources-manifest.md)

---

## File Structure

| File | Action | What changes |
|------|--------|-------------|
| `README.md` | Modify lines 135-143 | Add 2 missing agent entries to `.claude/agents/` tree |
| `wiki/index.md` | Modify ~191 lines | Fix `[[entitie/` → `[[entities/` and `[[concept/` → `[[concepts/` wikilink paths |
| `wiki/sources-manifest.md` | Delete lines 9-151 | Remove 143 stray duplicate data rows |

---

### Task 1: Fix README.md — Add missing agents to project structure tree

**Files:**
- Modify: `README.md:135-143`

- [ ] **Step 1: Edit the agent tree in README.md**

Replace the old `.claude/agents/` subtree (lines 135-143):

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

With the corrected subtree:

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

- [ ] **Step 2: Verify README.md agent count**

Run: `grep -c '\.md' README.md` after the agents section, or visually confirm the tree shows 10 agent files.

Expected: 10 `.md` entries under `.claude/agents/`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "fix: add web-search and ai-research agents to README.md project structure tree"
```

---

### Task 2: Fix wiki/index.md — Correct entity wikilink paths

**Files:**
- Modify: `wiki/index.md`

- [ ] **Step 1: Replace all `[[entitie/` with `[[entities/`**

Use the Edit tool with `replace_all: true` to change every `[[entitie/` to `[[entities/` in `wiki/index.md`. There are 131 occurrences — all entity wikilinks currently use the singular (incorrect) path `entitie/` instead of the actual directory name `entities/`.

- [ ] **Step 2: Verify no broken entity links remain**

Run: `grep -c 'entitie/' wiki/index.md`

Expected: 0

- [ ] **Step 3: Commit**

```bash
git add wiki/index.md
git commit -m "fix: correct entity wikilink paths from entitie/ to entities/ in wiki index"
```

---

### Task 3: Fix wiki/index.md — Correct concept wikilink paths

**Files:**
- Modify: `wiki/index.md`

- [ ] **Step 1: Replace all `[[concept/` with `[[concepts/`**

Use the Edit tool with `replace_all: true` to change every `[[concept/` to `[[concepts/` in `wiki/index.md`. There are 60 occurrences — all concept wikilinks currently use the singular (incorrect) path `concept/` instead of the actual directory name `concepts/`.

- [ ] **Step 2: Verify no broken concept links remain**

Run: `grep -c '\[\[concept/' wiki/index.md`

Expected: 0 (note: `\[\[concept/` won't match `[[concepts/` because it requires the opening bracket and no trailing 's')

- [ ] **Step 3: Commit**

```bash
git add wiki/index.md
git commit -m "fix: correct concept wikilink paths from concept/ to concepts/ in wiki index"
```

---

### Task 4: Fix wiki/sources-manifest.md — Remove stray data rows

**Files:**
- Modify: `wiki/sources-manifest.md`

- [ ] **Step 1: Read the current file to confirm line ranges**

Read `wiki/sources-manifest.md` and confirm:
- Lines 1-8: YAML frontmatter (starts with `---`, ends with `---`)
- Lines 9-151: Stray pipe-delimited rows (duplicate data)
- Line 152+: Blank line, then `# Sources Manifest` heading and proper markdown table

- [ ] **Step 2: Remove the stray rows**

Delete lines 9-151 (the 143 pipe-delimited data rows between frontmatter and the proper table). The file should go from frontmatter closing `---` directly to a blank line, then the `# Sources Manifest` heading and proper table.

- [ ] **Step 3: Verify the file structure**

Read the modified file and confirm:
- Frontmatter (lines 1-8) is intact
- No stray pipe-delimited rows between frontmatter and the heading
- The proper markdown table with `# Sources Manifest`, header, separator, and data rows follows

- [ ] **Step 4: Commit**

```bash
git add wiki/sources-manifest.md
git commit -m "fix: remove duplicate stray data rows from wiki/sources-manifest.md"
```

---

### Task 5: Final verification

- [ ] **Step 1: Run all verification checks**

```bash
grep -c 'entitie/' wiki/index.md          # Expected: 0
grep -c '\[\[concept/' wiki/index.md       # Expected: 0
grep 'web-search.md' README.md             # Expected: match
grep 'ai-research.md' README.md            # Expected: match
```

- [ ] **Step 2: Verify wiki/index.md wikilinks resolve**

Spot-check a few entity and concept wikilinks to confirm they point to files that exist:

```bash
ls wiki/entities/grok.md wiki/entities/openrouter.md wiki/concepts/rag.md wiki/concepts/mcp.md
```

Expected: All files exist (if any don't, that's a separate lint issue, not this fix)