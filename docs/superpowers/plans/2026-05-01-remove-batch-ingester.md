# Remove Batch-Ingester Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove the batch-ingester agent and all associated scripts/workflows, then update all referencing docs to standardize on subagent-driven wiki-maintainer ingestion.

**Architecture:** Delete 4 files (agent doc, script, prompt template, CI workflow), then update 9+ files that reference batch-ingester to remove those references and document the subagent-driven ingestion pattern instead.

**Tech Stack:** Markdown editing, git

---

## File Structure

| Action | File | What changes |
|--------|------|-------------|
| Delete | `.claude/agents/batch-ingester.md` | Entire file removed |
| Delete | `scripts/ingest_external.py` | Entire file removed |
| Delete | `scripts/prompts/ingest-prompt.txt` | Entire file removed |
| Delete | `.github/workflows/ingest.yml` | Entire file removed |
| Modify | `schema/WIKI_AGENTS.md` | Remove Batch Ingester section, add Ingestion Pattern subsection |
| Modify | `.claude/agents/sync-check.md` | Remove batch-ingester.md from file check lists |
| Modify | `CLAUDE.md` | Remove batch-ingester row from agent dispatch table |
| Modify | `AGENTS.md` | Remove batch-ingester from structure tree, remove ingest_external.py section, add subagent-driven note |
| Modify | `README.md` | Remove batch-ingester from structure tree, remove ingest_external.py line |
| Modify | `README-USER-GUIDE.md` | Remove batch-ingester from agent listing, dispatch table, and commands |
| Modify | `README-OWNER-GUIDE.md` | Remove batch-ingester dispatch rule and known issues entry |
| Modify | `docs/superpowers/specs/2026-05-01-restore-lint-checks-and-rebuild-wiki-design.md` | Update batch-ingester reference |
| Modify | `docs/superpowers/plans/2026-05-01-wiki-knowledge-rebuild.md` | Update ingest_external.py references |
| Modify | `docs/superpowers/plans/2026-05-01-consistency-fixes-and-user-guides.md` | Update all batch-ingester/ingest_external references |

---

### Task 1: Delete batch-ingester artifacts

**Files:**
- Delete: `.claude/agents/batch-ingester.md`
- Delete: `scripts/ingest_external.py`
- Delete: `scripts/prompts/ingest-prompt.txt`
- Delete: `.github/workflows/ingest.yml`

- [ ] **Step 1: Delete the agent definition**

```bash
rm .claude/agents/batch-ingester.md
```

- [ ] **Step 2: Delete the batch ingestion script**

```bash
rm scripts/ingest_external.py
```

- [ ] **Step 3: Delete the prompt template**

```bash
rm scripts/prompts/ingest-prompt.txt
```

- [ ] **Step 4: Delete the GitHub Actions workflow**

```bash
rm .github/workflows/ingest.yml
```

- [ ] **Step 5: Verify deletions**

```bash
ls .claude/agents/batch-ingester.md 2>&1
ls scripts/ingest_external.py 2>&1
ls scripts/prompts/ingest-prompt.txt 2>&1
ls .github/workflows/ingest.yml 2>&1
```

Expected: All four should report "No such file or directory".

- [ ] **Step 6: Commit**

```bash
git add -A .claude/agents/batch-ingester.md scripts/ingest_external.py scripts/prompts/ingest-prompt.txt .github/workflows/ingest.yml
git commit -m "$(cat <<'EOF'
chore: remove batch-ingester agent, script, prompt, and CI workflow

Replaced by subagent-driven wiki-maintainer ingestion pattern for
higher quality output. See docs/superpowers/specs/2026-05-01-remove-batch-ingester-design.md.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Update schema/WIKI_AGENTS.md

**Files:**
- Modify: `schema/WIKI_AGENTS.md` (lines 128-149)

- [ ] **Step 1: Remove the Batch Ingester Agent section**

Remove lines 128-149 in `schema/WIKI_AGENTS.md`. The section starts with `## Batch Ingester Agent` and ends with `Full definition: .claude/agents/batch-ingester.md`. Delete the entire section including the blank line after it.

- [ ] **Step 2: Add the Ingestion Pattern subsection**

After the Wiki Repair Agent section (which ends with `Full definition: .claude/agents/wiki-repair.md` on line 124), add:

```markdown

---

## Ingestion Pattern

All source ingestion uses **subagent-driven dispatch** — one fresh subagent per source, using the wiki-maintainer agent. The operator reviews between tasks and iterates fast. This produces higher-quality, more descriptive wiki pages than batch script-based ingestion because each source gets full interactive attention with cross-referencing, reconciliation, and provenance tracking.

The pattern:

1. **Dispatch**: For each source, dispatch a fresh subagent using the wiki-maintainer agent
2. **Review**: After each source completes, review the output before moving to the next
3. **Iterate**: Fast iteration — if quality is insufficient, re-dispatch with adjustments
4. **Track**: `wiki/sources-manifest.md` and `wiki/log.md` continue to track ingestion state

This replaces the former batch-ingester agent and `scripts/ingest_external.py`.
```

- [ ] **Step 3: Commit**

```bash
git add schema/WIKI_AGENTS.md
git commit -m "$(cat <<'EOF'
docs: replace batch-ingester section with subagent-driven ingestion pattern

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Update sync-check.md

**Files:**
- Modify: `.claude/agents/sync-check.md` (lines 38, 118)

- [ ] **Step 1: Remove batch-ingester.md from agent files list**

In `.claude/agents/sync-check.md`, on line 38, remove:

```markdown
- `.claude/agents/batch-ingester.md`
```

- [ ] **Step 2: Remove batch-ingester.md from Files to Read list**

In `.claude/agents/sync-check.md`, on line 118, remove:

```markdown
14. `.claude/agents/batch-ingester.md`
```

Renumber any subsequent entries if needed. After removal, the entry that was line 119 (`15. wiki/index.md`) becomes line 118, and the entry that was line 120 (`16. wiki/sources-manifest.md`) becomes line 119.

- [ ] **Step 3: Remove ingest_external.py from script names section**

In `.claude/agents/sync-check.md`, on line 47, remove:

```markdown
- `scripts/ingest_external.py` — flags: `--all`, `--file`, `--dry-run`, `--max-words`, `--workers`
```

- [ ] **Step 4: Commit**

```bash
git add .claude/agents/sync-check.md
git commit -m "$(cat <<'EOF'
docs: remove batch-ingester references from sync-check agent

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md` (line 39)

- [ ] **Step 1: Remove batch-ingester row from agent dispatch table**

In `CLAUDE.md`, remove the line:

```markdown
| `batch-ingester`     | "Ingest all pending sources", "Bulk ingest raw docs"         |
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "$(cat <<'EOF'
docs: remove batch-ingester from CLAUDE.md agent dispatch table

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: Update AGENTS.md

**Files:**
- Modify: `AGENTS.md` (lines 337, 400, 567-585)

- [ ] **Step 1: Remove batch-ingester.md from project structure tree**

In `AGENTS.md` around line 337, remove the line:

```markdown
|       |-- batch-ingester.md
```

- [ ] **Step 2: Remove ingest_external.py from project structure tree**

In `AGENTS.md` around line 400, remove the line:

```markdown
|   |-- ingest_external.py           #   Bulk ingest raw/ai-research → wiki
```

- [ ] **Step 3: Remove ingest_external.py - Batch Ingest section**

In `AGENTS.md`, remove lines 567-585 (the entire "### ingest_external.py - Batch Ingest" section including the CLI examples, `--max-words`, `--workers`, incremental tracking, and post-ingest notes). The section starts with `### ingest_external.py - Batch Ingest` and ends just before the `---` separator that precedes the `## State Tracking` section.

- [ ] **Step 4: Add subagent-driven ingestion note**

After removing the section, add a brief note in its place (before the `---` separator):

```markdown
### Source Ingestion

Source ingestion is subagent-driven — dispatch one wiki-maintainer subagent per source, review between tasks. See `schema/WIKI_AGENTS.md` → Ingestion Pattern.
```

- [ ] **Step 5: Commit**

```bash
git add AGENTS.md
git commit -m "$(cat <<'EOF'
docs: remove batch-ingester/ingest_external references from AGENTS.md

Replace with subagent-driven ingestion note pointing to WIKI_AGENTS.md.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 6: Update README.md

**Files:**
- Modify: `README.md` (lines 122, 146)

- [ ] **Step 1: Remove ingest_external.py from scripts tree**

In `README.md` around line 122, remove the line:

```markdown
│   └── ingest_external.py        #   Bulk ingest raw/ai-research → wiki
```

- [ ] **Step 2: Remove batch-ingester.md from agents tree**

In `README.md` around line 146, remove the line:

```markdown
│       └── batch-ingester.md
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
docs: remove batch-ingester and ingest_external from README structure tree

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 7: Update README-USER-GUIDE.md

**Files:**
- Modify: `README-USER-GUIDE.md` (lines 128, 149, 178-182, 197)

- [ ] **Step 1: Remove ingest_external.py from scripts directory**

In `README-USER-GUIDE.md` around line 128, remove:

```markdown
  ingest_external.py # Bulk ingest raw/ai-research -> wiki
```

- [ ] **Step 2: Remove batch-ingester.md from agent listing**

In `README-USER-GUIDE.md` around line 149, remove:

```markdown
    batch-ingester.md
```

Also update the agent count on line 140 from `9 project-specific Claude Code agents` to `8 project-specific Claude Code agents`.

- [ ] **Step 3: Remove ingest_external.py commands from Core Commands table**

In `README-USER-GUIDE.md`, remove these rows from the Core Commands table (around lines 178-182):

```markdown
| `uv run python scripts/ingest_external.py` | Ingest new/changed sources |
| `uv run python scripts/ingest_external.py --all` | Force re-ingest all sources |
| `uv run python scripts/ingest_external.py --dry-run` | Show what would be ingested |
| `uv run python scripts/ingest_external.py --max-words 30000` | Skip files over N words |
```

- [ ] **Step 4: Remove batch-ingester from agent dispatch table**

In `README-USER-GUIDE.md` around line 197, remove:

```markdown
| `batch-ingester` | "Ingest all pending sources", "Bulk ingest raw docs" |
```

- [ ] **Step 5: Update First Ingestion section**

In `README-USER-GUIDE.md` around lines 27-38, replace the First Ingestion section content. Remove the `uv run python scripts/ingest_external.py` commands and replace with:

```markdown
### First Ingestion

```bash
# Add source documents to raw/ (any subfolder)
cp ~/my-article.md raw/articles/

# Ingest into the wiki using subagent-driven dispatch
# Tell Claude Code: "Ingest raw/articles/my-article.md using wiki-maintainer"
```
```

- [ ] **Step 6: Commit**

```bash
git add README-USER-GUIDE.md
git commit -m "$(cat <<'EOF'
docs: remove batch-ingester and ingest_external from user guide

Update first ingestion section to use wiki-maintainer subagent dispatch.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 8: Update README-OWNER-GUIDE.md

**Files:**
- Modify: `README-OWNER-GUIDE.md` (lines 69, 99, 114, 130)

- [ ] **Step 1: Remove ingest_external.py from scripts reference table**

In `README-OWNER-GUIDE.md` around line 69, remove the row:

```markdown
| `ingest_external.py` | Bulk ingest raw/ai-research -> wiki | `--all`, `--file <path>`, `--dry-run`, `--max-words N`, `--workers N` | `scripts/state.json` (ingestion tracking) |
```

- [ ] **Step 2: Remove batch-ingester dispatch rule**

In `README-OWNER-GUIDE.md` around line 99, remove:

```markdown
| "Ingest all pending sources" | `batch-ingester` | Run ingest_external.py, then lint + repair |
```

- [ ] **Step 3: Remove --max-words known issue**

In `README-OWNER-GUIDE.md` around line 114, remove:

```markdown
- **`--max-words` default**: Script default is 30000. The GitHub Actions workflow overrides to 3000 for cost control. The batch-ingester agent doc matches the script at 30000.
```

- [ ] **Step 4: Remove check ingestion status maintenance task**

In `README-OWNER-GUIDE.md` around line 130, remove:

```markdown
| Check ingestion status | Anytime | `uv run python scripts/ingest_external.py --dry-run` |
```

- [ ] **Step 5: Update external ingest data flow**

In `README-OWNER-GUIDE.md` around line 36-39, update the External Ingest data flow. Change line 3 from:

```markdown
3. wiki-maintainer (or ingest_external.py) processes source
```

to:

```markdown
3. wiki-maintainer processes source (subagent-driven dispatch)
```

And change line 6 from:

```markdown
6. Lint + repair if batch ingesting
```

to:

```markdown
6. Lint + repair if needed
```

- [ ] **Step 6: Commit**

```bash
git add README-OWNER-GUIDE.md
git commit -m "$(cat <<'EOF'
docs: remove batch-ingester references from owner guide

Update data flow to reflect subagent-driven wiki-maintainer pattern.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 9: Update spec and plan docs

**Files:**
- Modify: `docs/superpowers/specs/2026-05-01-restore-lint-checks-and-rebuild-wiki-design.md`
- Modify: `docs/superpowers/plans/2026-05-01-wiki-knowledge-rebuild.md`
- Modify: `docs/superpowers/plans/2026-05-01-consistency-fixes-and-user-guides.md`

- [ ] **Step 1: Update restore-lint-checks spec**

In `docs/superpowers/specs/2026-05-01-restore-lint-checks-and-rebuild-wiki-design.md` line 104, change:

```markdown
2. Run `batch-ingester` agent to re-ingest all sources from `raw/` and `ai-research/`
```

to:

```markdown
2. Re-ingest all sources from `raw/` and `ai-research/` using wiki-maintainer subagent dispatch
```

- [ ] **Step 2: Update wiki-knowledge-rebuild plan**

In `docs/superpowers/plans/2026-05-01-wiki-knowledge-rebuild.md`:

Line 5, change:
```markdown
**Goal:** Fully rebuild `wiki/` and `knowledge/` from sources by batch-ingesting all 397 raw files and compiling 5 daily logs.
```
to:
```markdown
**Goal:** Fully rebuild `wiki/` and `knowledge/` from sources by subagent-driven ingestion of all raw files (using wiki-maintainer) and compiling 5 daily logs.
```

Line 7, change:
```markdown
**Architecture:** Use `scripts/ingest_external.py` for external KB (wiki/) and `scripts/compile.py` for internal KB (knowledge/). The 5 files over 10k words are handled by raising the `--max-words` limit — the ingestion script can handle them, it just takes longer per file. After ingestion, run the 12-check lint to validate the rebuilt wiki.
```
to:
```markdown
**Architecture:** Use wiki-maintainer subagent dispatch for external KB (wiki/) and `scripts/compile.py` for internal KB (knowledge/). Each source is processed by a fresh wiki-maintainer subagent, with review between sources. After ingestion, run the 12-check lint to validate the rebuilt wiki.
```

Lines 40, 103, 111, 119, 127, 133 — Replace all `uv run python scripts/ingest_external.py ...` commands with `# Ingest [source] using wiki-maintainer subagent dispatch` commentary, since these commands no longer work. For each line, replace the specific command with a note like:

```markdown
# Ingest using wiki-maintainer subagent dispatch (script removed)
```

- [ ] **Step 3: Update consistency-fixes plan**

In `docs/superpowers/plans/2026-05-01-consistency-fixes-and-user-guides.md`, update all references. This file has the most references. Key changes:

- Line 24: Remove the bullet `- .claude/agents/batch-ingester.md — Update --max-words default 3000→30000`
- Line 27: Remove the bullet `- scripts/ingest_external.py — Add update_wiki_synthesis() function`
- Lines 333, 338: Remove batch-ingester.md from Task 5 title and files list
- Lines 377-392: Remove the Step 3 (Update batch-ingester.md) and its commit, and remove batch-ingester.md from the git add command
- Lines 507-592: Remove or update Task 8 (Implement synthesis.md update in ingest_external.py) — note that the script no longer exists. Mark this task as superseded by the subagent-driven pattern.
- Lines 681-687: Remove ingest_external.py CLI examples
- Line 777: Remove `ingest_external.py` line from structure tree
- Line 798: Remove `batch-ingester.md` line from structure tree
- Lines 827-830: Remove ingest_external.py command rows from Core Commands table
- Line 846: Remove batch-ingester row from agent dispatch table
- Line 931: Update `wiki-maintainer (or ingest_external.py) processes source` to `wiki-maintainer processes source`
- Line 964: Remove ingest_external.py row from scripts reference table
- Line 994: Remove batch-ingester dispatch rule row
- Line 1009: Remove `--max-words` known issues bullet
- Line 1025: Remove check ingestion status row
- Line 1071: Remove `--max-words` consistency verification checkbox

For each of these, the exact edit depends on the surrounding context. The implementer should read each section and make the appropriate removal or replacement.

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/specs/2026-05-01-restore-lint-checks-and-rebuild-wiki-design.md docs/superpowers/plans/2026-05-01-wiki-knowledge-rebuild.md docs/superpowers/plans/2026-05-01-consistency-fixes-and-user-guides.md
git commit -m "$(cat <<'EOF'
docs: update spec/plan references from batch-ingester to subagent-driven

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

### Task 10: Verify no remaining references

- [ ] **Step 1: Grep for remaining batch-ingester references**

```bash
grep -r "batch-ingester\|batch_ingester\|ingest_external" --include="*.md" --include="*.py" --include="*.yml" --include="*.txt" .
```

Expected: Zero results (or only the new design spec and this plan file itself).

- [ ] **Step 2: Grep for ingest-prompt references**

```bash
grep -r "ingest-prompt\|ingest_prompt" --include="*.md" --include="*.py" --include="*.yml" --include="*.txt" .
```

Expected: Zero results.

- [ ] **Step 3: Verify agents directory**

```bash
ls .claude/agents/
```

Expected: No `batch-ingester.md` file. Should show: wiki-maintainer.md, document-processor.md, knowledge-compiler.md, wiki-linter.md, wiki-repair.md, wiki-query.md, sync-check.md, context-loader.md.

- [ ] **Step 4: Verify scripts directory**

```bash
ls scripts/
```

Expected: No `ingest_external.py`. Should show: compile.py, query.py, lint.py, flush.py, config.py, utils.py.

- [ ] **Step 5: Verify prompts directory is empty or removed**

```bash
ls scripts/prompts/ 2>&1
```

Expected: Either empty directory or "No such file or directory" if the directory was auto-cleaned.

- [ ] **Step 6: Final commit with any remaining fixes**

If the grep in Step 1 found any remaining references, fix them and commit. If clean, skip this step.

```bash
git add -A
git commit -m "$(cat <<'EOF'
chore: clean up remaining batch-ingester references

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```