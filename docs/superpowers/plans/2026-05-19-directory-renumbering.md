# Directory Renumbering — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename pipeline directories with numeric prefixes so processing order is visible in flat directory listings.

**Architecture:** Five git mv operations rename the directories on disk. Then a two-tier text update: Tier 1 does mechanical `old → new` string replacement in config files, scripts, schema docs, and agent definitions. Tier 2 rewrites path-based wikilinks in all `004-wiki/` content files, prefixing them with `004-wiki/`.

**Tech Stack:** Git (mv), Python scripts for wikilink rewriting, grep for verification.

---

## File Map

| File | Role | Change |
|------|------|--------|
| `scripts/config.py` | Single source of truth for all Python path constants | Update 5 dir constants |
| `scripts/sidecar.py` | Sidecar helper — imports `RAW_MARKDOWN_DIR` from config | No change (uses config constant) |
| `scripts/lint.py` | Wiki linter — imports dirs from config, has hardcoded `_VALID_PATH_PREFIXES` tuple | Update `_VALID_PATH_PREFIXES` |
| `scripts/utils.py` | Utility functions — imports dirs from config | No change (uses config constants) |
| `scripts/flush.py` | Session flush — uses `DAILY_DIR` from config | No change (daily/ unnumbered) |
| `scripts/compile.py` | Knowledge compiler — uses `DAILY_DIR`, `KNOWLEDGE_DIR` from config | No change (both unnumbered) |
| `CLAUDE.md` | Architecture table, Key Directories section | Update dir references |
| `AGENTS.md` | Internal KB — references wiki and pipeline dirs | Update dir references |
| `schema/WIKI_SCHEMA.md` | Directory Structure tree, all path references | Update dir references |
| `schema/WIKI_AGENTS.md` | Agent definitions, pipeline stage refs | Update dir references |
| `schema/WIKI_WORKFLOWS.md` | Workflow path references | Update dir references |
| `.claude/agents/*.md` | 12 agent definition files | Update dir references in each |
| `.claude/settings.local.json` | Hook command paths | Update dir references |
| `README.md` | Main readme | Update dir references |
| `README-OWNER-GUIDE.md` | Owner guide | Update dir references |
| `README-USER-GUIDE.md` | User guide | Update dir references |
| `README-PROJECT-COMPARISON.md` | Project comparison | Update dir references |
| `wiki/index.md` | Wiki index | Update dir references |
| `wiki/sources-manifest.md` | Source manifest | Update dir references |
| `wiki/log.md` | Wiki log | Update dir references |
| `wiki/synthesis.md` | Synthesis page | Update dir references + wikilinks |
| `004-wiki/**/*.md` | All wiki content pages (concepts, entities, summaries, qanda) | Tier 2 wikilink rewrites |
| `raw-markdown/*.sidecar.json` | OCR sidecar files | Update if they ref `raw-markdown/` |
| `processed/papers/*.md` | Processed segments with inline citations | Update citation paths |
| `.gitignore` | Git ignore patterns | No change (no dir-specific patterns to update) |

Non-pipeline dirs (`knowledge/`, `daily/`, `schema/`, `scripts/`, `docs/`, `hooks/`, `reports/`, `tools_scripts/`, `.claude/`) stay as-is.

Historical docs in `docs/superpowers/specs/` and `docs/superpowers/plans/` are snapshots — not updated (they reflect state at time of writing).

---

### Task 1: Rename directories on disk

**Files:** Five `git mv` operations

- [ ] **Step 1: Rename `raw/` → `001a-raw/`**

```bash
git mv raw 001a-raw
```

- [ ] **Step 2: Rename `ai-research/` → `001b-ai-research/`**

```bash
git mv ai-research 001b-ai-research
```

- [ ] **Step 3: Rename `raw-markdown/` → `002-raw-preprocessed/`**

```bash
git mv raw-markdown 002-raw-preprocessed
```

- [ ] **Step 4: Rename `processed/` → `003-processed/`**

```bash
git mv processed 003-processed
```

- [ ] **Step 5: Rename `wiki/` → `004-wiki/`**

```bash
git mv wiki 004-wiki
```

- [ ] **Step 6: Verify directories are renamed**

```bash
ls -d */
```

Expected: `001a-raw/`, `001b-ai-research/`, `002-raw-preprocessed/`, `003-processed/`, `004-wiki/`, plus all unnumbered dirs still present.

- [ ] **Step 7: Commit directory renames**

```bash
git add -A
git commit -m "refactor: rename pipeline directories with numeric prefixes"
```

---

### Task 2: Update `scripts/config.py` — the single source of truth

**Files:**
- Modify: `scripts/config.py:25-36,62`

All Python scripts import directory paths from `config.py`. Fix it first so everything downstream picks up the new paths automatically.

- [ ] **Step 1: Update directory path constants**

In `scripts/config.py`, change lines 25-36 and 62:

```python
# External KB paths
WIKI_DIR = ROOT_DIR / "004-wiki"
WIKI_CONCEPTS_DIR = WIKI_DIR / "concepts"
WIKI_ENTITIES_DIR = WIKI_DIR / "entities"
WIKI_SUMMARIES_DIR = WIKI_DIR / "summaries"
WIKI_QANDA_DIR = WIKI_DIR / "qanda"
WIKI_INDEX_FILE = WIKI_DIR / "index.md"
WIKI_SOURCES_MANIFEST_FILE = WIKI_DIR / "sources-manifest.md"
WIKI_LOG_FILE = WIKI_DIR / "log.md"

RAW_DIR = ROOT_DIR / "001a-raw"
AI_RESEARCH_DIR = ROOT_DIR / "001b-ai-research"
PROCESSED_DIR = ROOT_DIR / "003-processed"
```

And line 62:

```python
RAW_MARKDOWN_DIR = ROOT_DIR / "002-raw-preprocessed"
```

- [ ] **Step 2: Verify scripts still import correctly**

```bash
uv run python -c "from scripts.config import WIKI_DIR, RAW_DIR, AI_RESEARCH_DIR, PROCESSED_DIR, RAW_MARKDOWN_DIR; print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add scripts/config.py
git commit -m "refactor: update directory path constants in config.py"
```

---

### Task 3: Update `scripts/lint.py` — hardcoded path prefixes

**Files:**
- Modify: `scripts/lint.py:537`

The `_VALID_PATH_PREFIXES` tuple at line 537 is a hardcoded string tuple, not derived from config paths. Update it.

- [ ] **Step 1: Update `_VALID_PATH_PREFIXES`**

In `scripts/lint.py`, change line 537:

```python
_VALID_PATH_PREFIXES = ("001a-raw/", "001b-ai-research/", "003-processed/")
```

- [ ] **Step 2: Verify lint module loads without error**

```bash
uv run python -c "from scripts.lint import _VALID_PATH_PREFIXES; print(_VALID_PATH_PREFIXES)"
```

Expected: `('001a-raw/', '001b-ai-research/', '003-processed/')`

- [ ] **Step 3: Commit**

```bash
git add scripts/lint.py
git commit -m "refactor: update valid path prefixes in lint.py"
```

---

### Task 4: Update project-level docs (CLAUDE.md, AGENTS.md, READMEs)

**Files:**
- Modify: `CLAUDE.md`
- Modify: `AGENTS.md`
- Modify: `README.md`
- Modify: `README-OWNER-GUIDE.md`
- Modify: `README-USER-GUIDE.md`
- Modify: `README-PROJECT-COMPARISON.md`

- [ ] **Step 1: Update `CLAUDE.md` — Architecture table and Key Directories section**

Replace in `CLAUDE.md`:

| Old | New |
|-----|-----|
| `raw/` | `001a-raw/` |
| `ai-research/` | `001b-ai-research/` |
| `raw-markdown/` | `002-raw-preprocessed/` |
| `processed/` | `003-processed/` |
| `wiki/` | `004-wiki/` |

Architecture table becomes:

```markdown
| KB       | Raw source                                    | Compiled to  | Schema             |
| -------- | --------------------------------------------- | ------------ | ------------------ |
| External | `001a-raw/` + `001b-ai-research/` → `003-processed/` → `004-wiki/` | `004-wiki/` | `schema/WIKI_*.md` |
| Internal | `daily/` (conversation logs)                    | `knowledge/` | `AGENTS.md`        |
```

Key Directories section becomes:

```markdown
- `001a-raw/` — Source documents (human-curated, read-only for LLM)
- `001b-ai-research/` — AI-discovered web sources (LLM-writes, immutable once saved)
- `002-raw-preprocessed/` — Document conversion + OCR output (pre-chunking)
- `003-processed/` — Segmented markdown from large raw files (LLM-owned)
- `004-wiki/` — External KB (LLM-owned)
- `daily/` — Conversation logs (immutable)
- `knowledge/` — Internal KB (LLM-owned)
```

- [ ] **Step 2: Update `AGENTS.md` — all directory references**

Find and replace all occurrences of `raw/`, `ai-research/`, `raw-markdown/`, `processed/`, `wiki/` with their numbered equivalents. Use the same mapping as Step 1.

- [ ] **Step 3: Update `README.md` — all directory references**

Same find-and-replace mapping.

- [ ] **Step 4: Update `README-OWNER-GUIDE.md`, `README-USER-GUIDE.md`, `README-PROJECT-COMPARISON.md`**

Same find-and-replace mapping. These are less frequently modified but may reference directories.

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md AGENTS.md README.md README-OWNER-GUIDE.md README-USER-GUIDE.md README-PROJECT-COMPARISON.md
git commit -m "docs: update directory references in project-level docs"
```

---

### Task 5: Update schema docs

**Files:**
- Modify: `schema/WIKI_SCHEMA.md`
- Modify: `schema/WIKI_AGENTS.md`
- Modify: `schema/WIKI_WORKFLOWS.md`

- [ ] **Step 1: Update `schema/WIKI_SCHEMA.md` — Directory Structure tree (lines 7-52)**

Replace the entire directory structure block with updated paths:

```markdown
001a-raw/              # Source documents (immutable)
  articles/       # Article sources (web articles, blog posts)
  papers/         # Paper sources (PDFs, academic papers)
  repos/          # Repository sources (GitHub repos)
  datasets/       # Dataset sources
  assets/         # Images and attachments
  document/       # Documents (papers, PDFs, datasets)
  web/            # Web sources (articles, repos, tweets)
  forum-thread/   # Forum discussions
  transcripts/    # Conversation transcripts

001b-ai-research/      # AI-discovered web sources (LLM-writes, immutable once saved)
  articles/
  papers/
  repos/
  datasets/
  assets/
  document/
  web/
  forum-thread/
  transcripts/

002-raw-preprocessed/  # Document conversion + OCR output (pre-chunking)

003-processed/        # Segmented markdown from large raw files
  articles/       # Segmented articles
  papers/         # Segmented papers
  repos/          # Segmented repos
  datasets/       # Segmented datasets
  assets/         # Segmented assets
  document/       # Segmented document sources
  web/            # Segmented web sources
  forum-thread/   # Segmented forum discussions
  transcripts/    # Segmented conversation transcripts

004-wiki/             # LLM-generated content
  index.md        # Catalog of all wiki pages
  log.md          # Chronological operation log
  sources-manifest.md # Source tracking: 001a-raw/003-processed paths → ingest status
  synthesis.md    # Overarching thesis/summary
  concepts/       # Concept pages
  entities/       # Entity pages
  summaries/      # Source document summaries
  qanda/          # Q&A articles
```

Also update the Sources Manifest description line and any other body text referencing directory paths.

- [ ] **Step 2: Update `schema/WIKI_AGENTS.md` — pipeline stage references**

Find and replace all `raw/`, `ai-research/`, `raw-markdown/`, `processed/`, `wiki/` → numbered equivalents.

- [ ] **Step 3: Update `schema/WIKI_WORKFLOWS.md` — workflow path references**

Same find-and-replace.

- [ ] **Step 4: Commit**

```bash
git add schema/WIKI_SCHEMA.md schema/WIKI_AGENTS.md schema/WIKI_WORKFLOWS.md
git commit -m "docs: update directory references in schema docs"
```

---

### Task 6: Update agent definitions

**Files:**
- Modify: `.claude/agents/document-converter.md`
- Modify: `.claude/agents/document-processor.md`
- Modify: `.claude/agents/markdown-chunker.md`
- Modify: `.claude/agents/ocr-remediator.md`
- Modify: `.claude/agents/wiki-maintainer.md`
- Modify: `.claude/agents/wiki-linter.md`
- Modify: `.claude/agents/wiki-repair.md`
- Modify: `.claude/agents/wiki-query.md`
- Modify: `.claude/agents/sync-check.md`
- Modify: `.claude/agents/ai-research.md`
- Modify: `.claude/agents/youtube-transcript.md`
- Modify: `.claude/agents/transcript-reviewer.md`

- [ ] **Step 1: Update all agent files — mechanical find-and-replace**

For each of the 12 agent files, replace:

| Old | New |
|-----|-----|
| `raw/` | `001a-raw/` |
| `ai-research/` | `001b-ai-research/` |
| `raw-markdown/` | `002-raw-preprocessed/` |
| `processed/` | `003-processed/` |
| `wiki/` | `004-wiki/` |

**Order matters:** Replace `raw-markdown/` BEFORE `raw/` to avoid partial-match collision (otherwise `raw-markdown/` becomes `001a-raw-markdown/`).

- [ ] **Step 2: Verify no stale references remain in agent files**

```bash
grep -rn "raw/" .claude/agents/ | grep -v "001a-raw/" | grep -v "002-raw-preprocessed/" | grep -v ".git/"
grep -rn "processed/" .claude/agents/ | grep -v "003-processed/"
grep -rn "\bwiki/" .claude/agents/ | grep -v "004-wiki/" | grep -v "wiki-maintainer\|wiki-linter\|wiki-repair\|wiki-query"
```

Expected: no output from any of the three commands.

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/
git commit -m "refactor: update directory references in agent definitions"
```

---

### Task 7: Update `.claude/settings.local.json` — hook paths

**Files:**
- Modify: `.claude/settings.local.json`

- [ ] **Step 1: Update directory references in hooks config**

Replace `wiki/` → `004-wiki/`, `raw/` → `001a-raw/`, `processed/` → `003-processed/`, `raw-markdown/` → `002-raw-preprocessed/` in `.claude/settings.local.json`.

- [ ] **Step 2: Commit**

```bash
git add .claude/settings.local.json
git commit -m "refactor: update hook paths in settings.local.json"
```

---

### Task 8: Update wiki admin pages (index, log, sources-manifest, synthesis)

**Files:**
- Modify: `004-wiki/index.md`
- Modify: `004-wiki/log.md`
- Modify: `004-wiki/sources-manifest.md`
- Modify: `004-wiki/synthesis.md`

- [ ] **Step 1: Update admin page body text — mechanical find-and-replace**

Replace `raw/` → `001a-raw/`, `ai-research/` → `001b-ai-research/`, `processed/` → `003-processed/`, `wiki/` → `004-wiki/` in the body text (not wikilinks yet — those are Task 9).

- [ ] **Step 2: Update wikilinks in admin pages**

The admin pages may contain wikilinks like `[[concepts/foo]]`. Update these to `[[004-wiki/concepts/foo]]` (same pattern as Task 9).

Also update direct self-references: `[[log]]` → `[[004-wiki/log]]`, `[[synthesis]]` → `[[004-wiki/synthesis]]`, `[[index]]` → `[[004-wiki/index]]`, `[[sources-manifest]]` → `[[004-wiki/sources-manifest]]`.

- [ ] **Step 3: Commit**

```bash
git add 004-wiki/index.md 004-wiki/log.md 004-wiki/sources-manifest.md 004-wiki/synthesis.md
git commit -m "refactor: update directory references in wiki admin pages"
```

---

### Task 9: Rewrite wikilinks in all wiki content pages

**Files:** All `004-wiki/concepts/*.md`, `004-wiki/entities/*.md`, `004-wiki/summaries/*.md`, `004-wiki/qanda/*.md`

This is the largest task by file count. Every path-based wikilink inside `004-wiki/` must be prefixed with `004-wiki/`.

- [ ] **Step 1: Create a Python script for wikilink rewriting**

Create `scripts/rewrite_wikilinks.py`:

```python
"""Rewrite wikilinks in 004-wiki/ to include the 004-wiki/ prefix."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "004-wiki"

# Patterns for wikilinks that need prefixing
# Matches [[concepts/X]], [[entities/X]], [[summaries/X]], [[qanda/X]]
# Also [[synthesis]], [[index]], [[sources-manifest]], [[log]] (bare, no subdir)
WIKILINK_RE = re.compile(
    r"\[\[(concepts|entities|summaries|qanda)/",
)
BARE_RE = re.compile(
    r"\[\[(synthesis|index|sources-manifest|log)\]\]"
)

CHANGED = 0

for md_file in sorted(WIKI_DIR.rglob("*.md")):
    content = md_file.read_text(encoding="utf-8")
    original = content

    content = WIKILINK_RE.sub(r"[[004-wiki/\1/", content)
    content = BARE_RE.sub(r"[[004-wiki/\1]]", content)

    if content != original:
        md_file.write_text(content, encoding="utf-8")
        CHANGED += 1
        print(f"  Updated: {md_file.relative_to(ROOT)}")

print(f"\nUpdated {CHANGED} files")
```

- [ ] **Step 2: Run the script**

```bash
uv run python scripts/rewrite_wikilinks.py
```

- [ ] **Step 3: Verify a few wikilinks were rewritten correctly**

```bash
grep -r "\[\[concepts/" 004-wiki/concepts/ --include="*.md" -l | head -5
```

Expected: no output (all should now be `[[004-wiki/concepts/`).

```bash
grep -r "\[\[004-wiki/concepts/" 004-wiki/ --include="*.md" -c | head -5
```

Expected: files with counts of rewritten wikilinks.

- [ ] **Step 4: Commit**

```bash
git add 004-wiki/ scripts/rewrite_wikilinks.py
git commit -m "refactor: rewrite wikilinks with 004-wiki/ prefix in all wiki content"
```

---

### Task 10: Update citation paths in processed files

**Files:** `003-processed/papers/*.md` (and any other processed segments with `^[raw/...]` citations)

- [ ] **Step 1: Find processed files with raw/ citations**

```bash
grep -rl "\^\[raw/" 003-processed/
```

- [ ] **Step 2: Update citations**

Replace `^[raw/` → `^[001a-raw/` in all files found. Use a targeted sed/perl command:

```bash
for f in $(grep -rl "\^\[raw/" 003-processed/); do
  sed -i 's/\^\[raw\//^[001a-raw\//g' "$f"
done
```

Windows (PowerShell):

```powershell
Get-ChildItem -Path "003-processed" -Recurse -Filter "*.md" | ForEach-Object {
    (Get-Content $_.FullName -Raw) -replace '\^\[raw/', '^[001a-raw/' | Set-Content $_.FullName -NoNewline
}
```

- [ ] **Step 3: Verify no stale citation paths remain**

```bash
grep -rn "\^\[raw/" 003-processed/ 004-wiki/
```

Expected: no output.

- [ ] **Step 4: Commit**

```bash
git add 003-processed/
git commit -m "refactor: update citation paths in processed files"
```

---

### Task 11: Update OCR sidecar files

**Files:** `002-raw-preprocessed/*.sidecar.json`

- [ ] **Step 1: Check if sidecar files reference old directory names**

```bash
grep -rl "raw-markdown\|raw/" 002-raw-preprocessed/*.sidecar.json
```

- [ ] **Step 2: Update if needed**

If sidecar files contain `raw-markdown/` or `raw/`, replace with `002-raw-preprocessed/` and `001a-raw/` respectively.

- [ ] **Step 3: Commit (if changes made)**

```bash
git add 002-raw-preprocessed/
git commit -m "refactor: update directory references in sidecar files"
```

---

### Task 12: Run linter and sync-check for verification

**Files:** None (verification only)

- [ ] **Step 1: Run wiki linter to check for broken links**

```bash
uv run python scripts/lint.py
```

- [ ] **Step 2: Run sync-check agent**

Review `.claude/agents/sync-check.md` and verify schema/agent consistency against the new directory layout.

- [ ] **Step 3: Fix any lint errors**

If the linter reports broken citations or malformed paths, investigate and fix. The most likely source: claim citations in wiki pages that still reference `raw/` instead of `001a-raw/`.

- [ ] **Step 4: Final commit with any fixes**

```bash
git add -A
git commit -m "fix: resolve lint issues after directory renumbering"
```

---

### Task 13: Clean up the wikilink rewrite script

**Files:**
- Delete: `scripts/rewrite_wikilinks.py`

The script was a one-shot migration tool. Remove it.

- [ ] **Step 1: Delete the temporary script**

```bash
rm scripts/rewrite_wikilinks.py
```

- [ ] **Step 2: Commit**

```bash
git add scripts/rewrite_wikilinks.py
git commit -m "chore: remove one-shot wikilink rewrite script"
```
