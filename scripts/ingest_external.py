"""
Batch ingestion script for the external wiki knowledge base.

Reads source documents from raw/ and ai-research/, uses the Claude Agent SDK
to extract wiki content pages (summaries, entities, concepts), then updates
structural files (index, manifest, log) deterministically via Python.

Usage:
    uv run python ingest_external.py                    # ingest new/changed sources only
    uv run python ingest_external.py --all              # force re-ingest everything
    uv run python ingest_external.py --file raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md
    uv run python ingest_external.py --dry-run          # show what would be ingested
    uv run python ingest_external.py --max-words 30000  # skip files over 30k words (default)
    uv run python ingest_external.py --workers 4        # parallel mode (experimental)
"""

from __future__ import annotations

import argparse
import asyncio
import re
import sys
from pathlib import Path

from config import (
    AI_RESEARCH_DIR,
    PROCESSED_DIR,
    PROMPTS_DIR,
    RAW_DIR,
    ROOT_DIR,
    WIKI_CONCEPTS_DIR,
    WIKI_ENTITIES_DIR,
    WIKI_INDEX_FILE,
    WIKI_LOG_FILE,
    WIKI_QANDA_DIR,
    WIKI_SOURCES_MANIFEST_FILE,
    WIKI_SUMMARIES_DIR,
    now_iso,
    today_iso,
)
from utils import (
    file_hash,
    list_source_files,
    list_wiki_pages,
    load_state,
    parse_frontmatter,
    save_state,
    slugify,
    snake_slugify,
    wiki_page_type,
)


# ── Helpers ────────────────────────────────────────────────────────────────


def word_count(path: Path) -> int:
    """Count words in a file, stripping HTML comment blocks."""
    text = path.read_text(encoding="utf-8", errors="replace")
    # Strip HTML comments (openrouter docs start with <!-- metadata -->)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return len(text.split())


def read_prompt_template() -> str:
    """Read the ingest prompt template file."""
    template_path = PROMPTS_DIR / "ingest-prompt.txt"
    if not template_path.exists():
        print(f"Error: Prompt template not found at {template_path}")
        print("Override with scripts/prompts/ingest-prompt.txt")
        sys.exit(1)
    return template_path.read_text(encoding="utf-8")


def build_existing_pages_context() -> tuple[str, str]:
    """Build context strings of existing entities and concepts for deduplication.

    Returns (entities_list, concepts_list) as formatted bullet strings.
    """
    entities = []
    concepts = []

    for page in list_wiki_pages():
        page_type = wiki_page_type(page)
        if page_type not in ("entity", "concept"):
            continue

        rel = page.relative_to(ROOT_DIR / "wiki")
        content = page.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(content)
        title = fm.get("title", page.stem)

        if page_type == "entity":
            entities.append(f"- {rel} (title: \"{title}\")")
        elif page_type == "concept":
            concepts.append(f"- {rel} (title: \"{title}\")")

    entities_str = "\n".join(entities) if entities else "(No existing entities)"
    concepts_str = "\n".join(concepts) if concepts else "(No existing concepts)"
    return entities_str, concepts_str


def derive_summary_slug(source_path: Path) -> str:
    """Derive a kebab-case summary slug from a source filename.

    Handles openrouter-style names like:
      openrouter-001-quickstart-2026-04-29.md -> openrouter-quickstart
      openrouter-018-guides-routing-provider-selection-2026-04-29.md -> openrouter-guides-routing-provider-selection
    """
    stem = source_path.stem
    # Strip trailing date pattern (YYYY-MM-DD)
    stem = re.sub(r"-?\d{4}-\d{2}-\d{2}$", "", stem)
    # Strip numeric index: "-001-" -> "-"
    stem = re.sub(r"-\d{3}-", "-", stem)
    return slugify(stem) if stem else slugify(source_path.stem)


def derive_source_title(source_path: Path) -> str:
    """Derive a display title from the source filename."""
    stem = source_path.stem
    # Strip trailing date
    stem = re.sub(r"-?\d{4}-\d{2}-\d{2}$", "", stem)
    # Strip numeric index
    stem = re.sub(r"-\d{3}-", " ", stem)
    # Convert hyphens to spaces, title case
    return stem.replace("-", " ").strip().title()


def build_prompt(
    source_path: Path,
    template: str,
    existing_entities: str,
    existing_concepts: str,
) -> str:
    """Fill the prompt template with source document and context."""
    source_rel = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
    source_content = source_path.read_text(encoding="utf-8", errors="replace")
    wc = word_count(source_path)
    source_title = derive_source_title(source_path)
    summary_slug = derive_summary_slug(source_path)
    today = today_iso()

    return template.format(
        source_rel_path=source_rel,
        source_content=source_content,
        word_count=wc,
        source_title=source_title,
        summary_slug=summary_slug,
        today=today,
        existing_entities_list=existing_entities,
        existing_concepts_list=existing_concepts,
    )


# ── Wiki page snapshots ───────────────────────────────────────────────────


def snapshot_wiki_pages() -> dict[str, set[str]]:
    """Snapshot current wiki page stems by type for diffing."""
    result: dict[str, set[str]] = {"summaries": set(), "entities": set(), "concepts": set()}
    for page in list_wiki_pages():
        pt = wiki_page_type(page)
        if pt in ("summary", "entity", "concept"):
            result[f"{pt}s"].add(page.stem)
    return result


def diff_wiki_pages(before: dict[str, set[str]]) -> dict[str, list[str]]:
    """Diff current wiki state against a before snapshot.

    Returns dict with 'summaries', 'entities', 'concepts' lists of new page stems,
    plus 'updated' list of pages whose hash changed.
    """
    after = snapshot_wiki_pages()
    diff: dict[str, list[str]] = {"summaries": [], "entities": [], "concepts": [], "updated": []}

    for key in ("summaries", "entities", "concepts"):
        new_stems = after[key] - before[key]
        diff[key] = sorted(new_stems)

    return diff


# ── Structural file updates ───────────────────────────────────────────────


def _update_footer(content: str, today: str, detail: str) -> str:
    """Update the last-updated footer line in a structural file."""
    return re.sub(
        r"\*Last updated:.*?\*",
        f"*Last updated: {today} ({detail})*",
        content,
    )


def update_wiki_index(diff: dict[str, list[str]], today: str) -> None:
    """Append new page entries to wiki/index.md sections."""
    if not WIKI_INDEX_FILE.exists():
        return

    content = WIKI_INDEX_FILE.read_text(encoding="utf-8")

    # Map diff keys to index section headings
    section_map = {
        "entities": "## Entities",
        "concepts": "## Concepts",
        "summaries": "## Summaries",
    }

    for diff_key, section_heading in section_map.items():
        new_stems = diff.get(diff_key, [])
        if not new_stems:
            continue

        subdir = diff_key.rstrip("s") if diff_key != "summaries" else "summaries"
        bullets = []
        for stem in new_stems:
            # Find the actual page to get its display title
            target_dir = WIKI_INDEX_FILE.parent / subdir
            page_file = target_dir / f"{stem}.md"
            display = stem.replace("_", " ").replace("-", " ").title()
            if page_file.exists():
                fm = parse_frontmatter(page_file.read_text(encoding="utf-8", errors="replace"))
                display = fm.get("title", display)

            bullets.append(f"- [[{subdir}/{stem}|{display}]]")

        # Insert bullets after the section heading, before the next section
        bullet_text = "\n".join(bullets)
        pattern = f"({re.escape(section_heading)}\\n)"
        replacement = f"\\1{bullet_text}\n"
        content = re.sub(pattern, replacement, content, count=1)

    content = _update_footer(content, today, f"batch ingest: {sum(len(v) for v in diff.values())} pages")
    WIKI_INDEX_FILE.write_text(content, encoding="utf-8")


def update_sources_manifest(
    source_path: Path,
    summary_slug: str,
    today: str,
) -> None:
    """Append a row to wiki/sources-manifest.md."""
    if not WIKI_SOURCES_MANIFEST_FILE.exists():
        return

    content = WIKI_SOURCES_MANIFEST_FILE.read_text(encoding="utf-8")
    source_rel = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")

    new_row = f"| {source_rel} | ingested | [[summaries/{summary_slug}]] | {today} |"

    # Insert before the --- footer separator
    if "\n---\n" in content:
        content = content.replace("\n---\n", f"\n{new_row}\n---\n", 1)
    else:
        content += f"\n{new_row}\n"

    content = _update_footer(content, today, f"ingested {source_rel}")
    WIKI_SOURCES_MANIFEST_FILE.write_text(content, encoding="utf-8")


def update_wiki_log(
    source_path: Path,
    diff: dict[str, list[str]],
    today: str,
    cost: float,
) -> None:
    """Append an ingest entry to wiki/log.md."""
    if not WIKI_LOG_FILE.exists():
        return

    source_rel = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
    source_title = derive_source_title(source_path)
    summary_slug = derive_summary_slug(source_path)

    lines = [f"## [{today}] ingest | {source_title}"]
    lines.append(f"- Source: {source_rel}")
    lines.append(f"- Created summary: summaries/{summary_slug}.md")

    if diff.get("entities"):
        lines.append(f"- Created entities: {', '.join(f'entities/{e}.md' for e in diff['entities'])}")
    if diff.get("concepts"):
        lines.append(f"- Created concepts: {', '.join(f'concepts/{c}.md' for c in diff['concepts'])}")
    lines.append(f"- Updated index.md, sources-manifest.md")
    lines.append(f"- Cost: ${cost:.4f}")

    entry = "\n".join(lines)
    content = WIKI_LOG_FILE.read_text(encoding="utf-8")

    # Insert before the footer
    footer = "*Append new entries at the bottom*"
    if footer in content:
        content = content.replace(footer, f"{entry}\n\n{footer}")
    else:
        content += f"\n\n{entry}\n"

    WIKI_LOG_FILE.write_text(content, encoding="utf-8")


def update_wiki_synthesis(source_path: Path, diff: dict[str, list[str]], today: str) -> None:
    """Update wiki/synthesis.md with new source reference if relevant."""
    synthesis_file = WIKI_DIR / "synthesis.md"
    if not synthesis_file.exists():
        return

    content = synthesis_file.read_text(encoding="utf-8")
    source_rel = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
    source_title = derive_source_title(source_path)

    # Add source to frontmatter sources list if not already present
    if source_rel not in content:
        lines = content.split("\n")
        new_lines = []
        in_sources = False
        for line in lines:
            new_lines.append(line)
            if line.strip().startswith("sources:"):
                in_sources = True
            elif in_sources and line.strip().startswith("- "):
                pass  # continue in sources list
            elif in_sources and not line.startswith("  ") and not line.strip().startswith("-"):
                # End of sources list — insert new source before this line
                indent = "  "
                new_lines.insert(len(new_lines) - 1, f"{indent}- {source_rel}")
                in_sources = False
        content = "\n".join(new_lines)

    # Update frontmatter timestamps
    content = re.sub(
        r'(updated:)\s*["\']?\d{4}-\d{2}-\d{2}[^"\']*["\']?',
        f'updated: "{today}T12:00:00Z"',
        content,
    )
    content = re.sub(
        r'(updated:)\s*\d{4}-\d{2}-\d{2}(?!\d)',
        f'updated: "{today}T12:00:00Z"',
        content,
    )

    # Update footer
    content = _update_footer(content, today, f"ingested {source_title}")

    synthesis_file.write_text(content, encoding="utf-8")


def update_structural_files(
    source_path: Path,
    diff: dict[str, list[str]],
    cost: float,
) -> None:
    """Update all structural files after a successful ingestion."""
    today = today_iso()
    summary_slug = derive_summary_slug(source_path)

    update_wiki_index(diff, today)
    update_sources_manifest(source_path, summary_slug, today)
    update_wiki_log(source_path, diff, today, cost)
    update_wiki_synthesis(source_path, diff, today)


# ── Core ingestion ─────────────────────────────────────────────────────────


async def ingest_source(
    source_path: Path,
    template: str,
    max_words: int,
) -> tuple[float, dict | None]:
    """Ingest a single source document into the wiki.

    Returns (cost, diff) where diff describes new pages created.
    Returns (0.0, None) if the file was skipped.
    """
    wc = word_count(source_path)
    if wc > max_words:
        rel = source_path.relative_to(ROOT_DIR)
        print(f"  Skipping {rel} — {wc} words exceeds --max-words {max_words}")
        return 0.0, None

    # Build context
    existing_entities, existing_concepts = build_existing_pages_context()
    prompt = build_prompt(source_path, template, existing_entities, existing_concepts)

    # Snapshot before
    before = snapshot_wiki_pages()

    # Call Claude Agent SDK
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        query,
    )

    cost = 0.0
    try:
        async for message in query(
            prompt=prompt,
            options=ClaudeAgentOptions(
                cwd=str(ROOT_DIR),
                system_prompt={"type": "preset", "preset": "claude_code"},
                allowed_tools=["Read", "Write", "Edit", "Glob", "Grep"],
                permission_mode="acceptEdits",
                max_turns=30,
            ),
        ):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        pass  # LLM writes files directly via tools
            elif isinstance(message, ResultMessage):
                cost = message.total_cost_usd or 0.0
    except Exception as e:
        print(f"  Error: {e}")
        return 0.0, None

    # Diff after
    diff = diff_wiki_pages(before)
    return cost, diff


# ── Parallel ingestion ─────────────────────────────────────────────────────


async def ingest_source_parallel(
    source_path: Path,
    template: str,
    max_words: int,
    semaphore: asyncio.Semaphore,
    results: list,
) -> None:
    """Wrapper for parallel ingestion with semaphore limiting."""
    async with semaphore:
        cost, diff = await ingest_source(source_path, template, max_words)
        results.append((source_path, cost, diff))


async def run_parallel(
    pending: list[Path],
    template: str,
    max_words: int,
    workers: int,
    state: dict,
) -> float:
    """Run ingestion in parallel with N workers."""
    semaphore = asyncio.Semaphore(workers)
    results: list[tuple[Path, float, dict | None]] = []

    tasks = [
        ingest_source_parallel(path, template, max_words, semaphore, results)
        for path in pending
    ]
    await asyncio.gather(*tasks)

    # Sequential structural updates + state tracking
    total_cost = 0.0
    for source_path, cost, diff in results:
        rel = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
        if diff is not None:
            update_structural_files(source_path, diff, cost)
            state.setdefault("external_ingested", {})[rel] = {
                "hash": file_hash(source_path),
                "ingested_at": now_iso(),
                "cost_usd": cost,
            }
            state["total_cost"] = state.get("total_cost", 0.0) + cost
            total_cost += cost
            new_pages = sum(len(v) for v in diff.values())
            print(f"  Done. {new_pages} new pages. Cost: ${cost:.4f}")
        save_state(state)

    return total_cost


# ── Main ───────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch ingest raw docs into wiki")
    parser.add_argument("--all", action="store_true", help="Force re-ingest all sources")
    parser.add_argument("--file", type=str, help="Ingest a specific source file")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be ingested")
    parser.add_argument("--max-words", type=int, default=30000, help="Skip files over N words (default: 30000)")
    parser.add_argument("--workers", type=int, default=1, help="Parallel workers (default: 1, sequential)")
    args = parser.parse_args()

    state = load_state()

    # Determine which files to ingest
    if args.file:
        target = Path(args.file)
        if not target.is_absolute():
            target = ROOT_DIR / args.file
        if not target.exists():
            print(f"Error: {args.file} not found")
            sys.exit(1)
        pending = [target]
    else:
        all_sources = list_source_files()
        if args.all:
            pending = all_sources
        else:
            pending = []
            external = state.get("external_ingested", {})
            for source_path in all_sources:
                rel = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
                prev = external.get(rel, {})
                if not prev or prev.get("hash") != file_hash(source_path):
                    pending.append(source_path)

    if not pending:
        print("Nothing to ingest. Use --all to force re-ingest.")
        return

    # Apply max-words filter for dry-run display
    within_limit = []
    over_limit = []
    for p in pending:
        if word_count(p) > args.max_words:
            over_limit.append(p)
        else:
            within_limit.append(p)

    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"{prefix}Files to ingest ({len(within_limit)}):")
    for f in within_limit:
        rel = f.relative_to(ROOT_DIR)
        print(f"  - {rel} (~{word_count(f)} words)")

    if over_limit:
        print(f"\n{prefix}Skipped ({len(over_limit)}) -- exceed --max-words {args.max_words}:")
        for f in over_limit:
            rel = f.relative_to(ROOT_DIR)
            print(f"  - {rel} (~{word_count(f)} words)")

    if args.dry_run:
        return

    if args.workers > 1:
        print(f"\nRunning {len(within_limit)} files with {args.workers} workers (parallel)...")
        print("Warning: parallel mode may cause entity/concept page conflicts.")
        print("Run lint + repair afterward to fix any issues.\n")
        total_cost = asyncio.run(run_parallel(within_limit, read_prompt_template(), args.max_words, args.workers, state))
    else:
        template = read_prompt_template()
        total_cost = 0.0
        total_new_pages = 0
        success = 0
        failed = 0

        for i, source_path in enumerate(within_limit, 1):
            rel = source_path.relative_to(ROOT_DIR)
            print(f"\n[{i}/{len(within_limit)}] Ingesting {rel}...")

            cost, diff = asyncio.run(ingest_source(source_path, template, args.max_words))

            if diff is not None:
                update_structural_files(source_path, diff, cost)

                source_rel = str(rel).replace("\\", "/")
                state.setdefault("external_ingested", {})[source_rel] = {
                    "hash": file_hash(source_path),
                    "ingested_at": now_iso(),
                    "cost_usd": cost,
                }
                state["total_cost"] = state.get("total_cost", 0.0) + cost
                save_state(state)

                new_pages = sum(len(v) for v in diff.values())
                total_new_pages += new_pages
                total_cost += cost
                success += 1
                print(f"  Done. {new_pages} new pages. Cost: ${cost:.4f}")
            else:
                failed += 1

        print(f"\nBatch complete. {success} succeeded, {failed} failed, {len(over_limit)} skipped.")
        print(f"Total cost: ${total_cost:.2f} | New wiki pages: {total_new_pages}")

    wiki_count = len(list_wiki_pages())
    print(f"Wiki now has {wiki_count} content pages.")


if __name__ == "__main__":
    main()