"""
Lint the knowledge base for structural and semantic health.

Runs 8 checks: broken links, orphan pages, orphan sources, stale articles,
contradictions (LLM), missing backlinks, sparse articles, and unsourced claims.

Supports both Internal KB (knowledge/) and External KB (wiki/).

Usage:
    uv run python lint.py                    # all checks, both KBs
    uv run python lint.py --kb internal      # internal KB only
    uv run python lint.py --kb external      # external KB only
    uv run python lint.py --structural-only  # skip LLM checks (faster, cheaper)
"""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from config import (
    AI_RESEARCH_DIR,
    DAILY_DIR,
    KNOWLEDGE_DIR,
    PROCESSED_DIR,
    RAW_DIR,
    REPORTS_DIR,
    WIKI_DIR,
    now_iso,
    today_iso,
)
from utils import (
    count_inbound_links,
    extract_wikilinks,
    file_hash,
    get_article_word_count,
    get_wiki_sources,
    list_processed_files,
    list_raw_files,
    list_source_files,
    list_wiki_articles,
    list_wiki_pages,
    load_state,
    parse_frontmatter,
    read_all_wiki_content,
    save_state,
    wiki_article_exists,
    wiki_page_exists,
)

ROOT_DIR = Path(__file__).resolve().parent.parent


# ── Internal KB checks ────────────────────────────────────────────────

def check_broken_links_internal() -> list[dict]:
    """Check for [[wikilinks]] that point to non-existent articles in knowledge/."""
    issues = []
    for article in list_wiki_articles():
        content = article.read_text(encoding="utf-8")
        rel = article.relative_to(KNOWLEDGE_DIR)
        for link in extract_wikilinks(content):
            if link.startswith("daily/"):
                continue
            if not wiki_article_exists(link):
                issues.append({
                    "severity": "error",
                    "check": "broken_link",
                    "kb": "internal",
                    "file": str(rel),
                    "detail": f"Broken link: [[{link}]] - target does not exist",
                })
    return issues


def check_orphan_pages_internal() -> list[dict]:
    """Check for internal articles with zero inbound links."""
    issues = []
    for article in list_wiki_articles():
        rel = article.relative_to(KNOWLEDGE_DIR)
        link_target = str(rel).replace(".md", "").replace("\\", "/")
        inbound = count_inbound_links(link_target)
        if inbound == 0:
            issues.append({
                "severity": "warning",
                "check": "orphan_page",
                "kb": "internal",
                "file": str(rel),
                "detail": f"Orphan page: no other articles link to [[{link_target}]]",
            })
    return issues


def check_orphan_sources_internal() -> list[dict]:
    """Check for daily logs that haven't been compiled yet."""
    state = load_state()
    ingested = state.get("ingested", {})
    issues = []
    for log_path in list_raw_files():
        if log_path.name not in ingested:
            issues.append({
                "severity": "warning",
                "check": "orphan_source",
                "kb": "internal",
                "file": f"daily/{log_path.name}",
                "detail": f"Uncompiled daily log: {log_path.name} has not been ingested",
            })
    return issues


def check_stale_articles_internal() -> list[dict]:
    """Check if source daily logs have changed since compilation."""
    state = load_state()
    ingested = state.get("ingested", {})
    issues = []
    for log_path in list_raw_files():
        rel = log_path.name
        if rel in ingested:
            stored_hash = ingested[rel].get("hash", "")
            current_hash = file_hash(log_path)
            if stored_hash != current_hash:
                issues.append({
                    "severity": "warning",
                    "check": "stale_article",
                    "kb": "internal",
                    "file": f"daily/{rel}",
                    "detail": f"Stale: {rel} has changed since last compilation",
                })
    return issues


def check_missing_backlinks_internal() -> list[dict]:
    """Check for asymmetric links in internal KB."""
    issues = []
    for article in list_wiki_articles():
        content = article.read_text(encoding="utf-8")
        rel = article.relative_to(KNOWLEDGE_DIR)
        source_link = str(rel).replace(".md", "").replace("\\", "/")

        for link in extract_wikilinks(content):
            if link.startswith("daily/"):
                continue
            target_path = KNOWLEDGE_DIR / f"{link}.md"
            if target_path.exists():
                target_content = target_path.read_text(encoding="utf-8")
                if f"[[{source_link}]]" not in target_content:
                    issues.append({
                        "severity": "suggestion",
                        "check": "missing_backlink",
                        "kb": "internal",
                        "file": str(rel),
                        "detail": f"[[{source_link}]] links to [[{link}]] but not vice versa",
                        "auto_fixable": True,
                    })
    return issues


def check_sparse_articles_internal() -> list[dict]:
    """Check for internal articles with fewer than 200 words."""
    issues = []
    for article in list_wiki_articles():
        word_count = get_article_word_count(article)
        if word_count < 200:
            rel = article.relative_to(KNOWLEDGE_DIR)
            issues.append({
                "severity": "suggestion",
                "check": "sparse_article",
                "kb": "internal",
                "file": str(rel),
                "detail": f"Sparse article: {word_count} words (minimum recommended: 200)",
            })
    return issues


async def check_contradictions_internal() -> list[dict]:
    """Use LLM to detect contradictions across internal articles."""
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        query,
    )

    wiki_content = read_all_wiki_content()

    prompt = f"""Review this knowledge base for contradictions, inconsistencies, or
conflicting claims across articles.

## Knowledge Base

{wiki_content}

## Instructions

Look for:
- Direct contradictions (article A says X, article B says not-X)
- Inconsistent recommendations (different articles recommend conflicting approaches)
- Outdated information that conflicts with newer entries

For each issue found, output EXACTLY one line in this format:
CONTRADICTION: [file1] vs [file2] - description of the conflict
INCONSISTENCY: [file] - description of the inconsistency

If no issues found, output exactly: NO_ISSUES

Do NOT output anything else - no preamble, no explanation, just the formatted lines."""

    response = ""
    try:
        async for message in query(
            prompt=prompt,
            options=ClaudeAgentOptions(
                cwd=str(ROOT_DIR),
                allowed_tools=[],
                max_turns=2,
            ),
        ):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        response += block.text
    except Exception as e:
        return [{"severity": "error", "check": "contradiction", "kb": "internal", "file": "(system)", "detail": f"LLM check failed: {e}"}]

    issues = []
    if "NO_ISSUES" not in response:
        for line in response.strip().split("\n"):
            line = line.strip()
            if line.startswith("CONTRADICTION:") or line.startswith("INCONSISTENCY:"):
                issues.append({
                    "severity": "warning",
                    "check": "contradiction",
                    "kb": "internal",
                    "file": "(cross-article)",
                    "detail": line,
                })

    return issues


def check_unsourced_claims_internal() -> list[dict]:
    """Check for internal articles missing source references back to daily logs."""
    issues = []
    for article in list_wiki_articles():
        content = article.read_text(encoding="utf-8")
        rel = article.relative_to(KNOWLEDGE_DIR)
        fm = parse_frontmatter(content)
        sources = fm.get("sources", "")
        if not sources or (isinstance(sources, str) and not sources.strip()):
            issues.append({
                "severity": "warning",
                "check": "unsourced_claim",
                "kb": "internal",
                "file": str(rel),
                "detail": "Article has no sources field — claims cannot be traced to daily logs",
            })
    return issues


# ── External KB checks ────────────────────────────────────────────────

def check_broken_links_external() -> list[dict]:
    """Check for [[wikilinks]] that point to non-existent pages in wiki/."""
    issues = []
    for page in list_wiki_pages():
        content = page.read_text(encoding="utf-8")
        rel = page.relative_to(WIKI_DIR)
        for link in extract_wikilinks(content):
            if link.startswith("raw/") or link.startswith("ai-research/") or link.startswith("processed/"):
                continue  # source file references, not wiki links
            if link in ("index", "sources-manifest", "log", "synthesis"):
                continue  # structural pages
            if not wiki_page_exists(link):
                issues.append({
                    "severity": "error",
                    "check": "broken_link",
                    "kb": "external",
                    "file": str(rel),
                    "detail": f"Broken link: [[{link}]] - target does not exist",
                })
    return issues


def check_orphan_pages_external() -> list[dict]:
    """Check for external wiki pages with zero inbound links from other wiki pages."""
    issues = []
    all_pages = list_wiki_pages()
    # Build a map of link targets from all pages
    inbound: dict[str, int] = {}
    for page in all_pages:
        content = page.read_text(encoding="utf-8")
        for link in extract_wikilinks(content):
            if link.startswith("raw/") or link.startswith("ai-research/") or link.startswith("processed/"):
                continue
            inbound[link] = inbound.get(link, 0) + 1

    for page in all_pages:
        rel = page.relative_to(WIKI_DIR)
        link_target = str(rel).replace(".md", "").replace("\\", "/")
        if inbound.get(link_target, 0) == 0:
            issues.append({
                "severity": "warning",
                "check": "orphan_page",
                "kb": "external",
                "file": str(rel),
                "detail": f"Orphan page: no other wiki pages link to [[{link_target}]]",
            })
    return issues


def check_orphan_sources_external() -> list[dict]:
    """Check for raw/ and ai-research/ files not yet ingested, or processed/ segments not yet ingested."""
    issues = []
    ingested_sources = set()

    # Collect all source paths referenced from wiki articles
    for page in list_wiki_pages():
        for src in get_wiki_sources(page):
            ingested_sources.add(src.strip())

    # Check raw/ files
    for src_file in list_source_files():
        rel = str(src_file.relative_to(ROOT_DIR)).replace("\\", "/")
        if rel not in ingested_sources:
            issues.append({
                "severity": "suggestion",
                "check": "orphan_source",
                "kb": "external",
                "file": rel,
                "detail": f"Source not yet ingested: {rel}",
            })

    # Check processed/ files
    for proc_file in list_processed_files():
        rel = str(proc_file.relative_to(ROOT_DIR)).replace("\\", "/")
        if rel not in ingested_sources:
            issues.append({
                "severity": "suggestion",
                "check": "orphan_source",
                "kb": "external",
                "file": rel,
                "detail": f"Processed segment not yet ingested: {rel}",
            })

    return issues


def check_missing_backlinks_external() -> list[dict]:
    """Check for asymmetric links in external wiki."""
    issues = []
    all_pages = list_wiki_pages()
    # Build a map of outbound links per page
    outbound: dict[str, set[str]] = {}
    for page in all_pages:
        rel = str(page.relative_to(WIKI_DIR)).replace(".md", "").replace("\\", "/")
        content = page.read_text(encoding="utf-8")
        links = set()
        for link in extract_wikilinks(content):
            if link.startswith("raw/") or link.startswith("ai-research/") or link.startswith("processed/"):
                continue
            links.add(link)
        outbound[rel] = links

    for page in all_pages:
        rel = str(page.relative_to(WIKI_DIR)).replace(".md", "").replace("\\", "/")
        for link in outbound.get(rel, set()):
            if link in outbound and rel not in outbound[link]:
                issues.append({
                    "severity": "suggestion",
                    "check": "missing_backlink",
                    "kb": "external",
                    "file": f"{rel}.md",
                    "detail": f"[[{rel}]] links to [[{link}]] but not vice versa",
                    "auto_fixable": True,
                })
    return issues


def check_sparse_articles_external() -> list[dict]:
    """Check for external wiki pages with fewer than 200 words."""
    issues = []
    for page in list_wiki_pages():
        word_count = get_article_word_count(page)
        if word_count < 200:
            rel = page.relative_to(WIKI_DIR)
            issues.append({
                "severity": "suggestion",
                "check": "sparse_article",
                "kb": "external",
                "file": str(rel),
                "detail": f"Sparse article: {word_count} words (minimum recommended: 200)",
            })
    return issues


def check_unsourced_claims_external() -> list[dict]:
    """Check for external wiki pages whose sources don't trace back to raw/ or ai-research/."""
    issues = []
    all_source_files = set()
    for src_file in list_source_files():
        all_source_files.add(str(src_file.relative_to(ROOT_DIR)).replace("\\", "/"))
    for proc_file in list_processed_files():
        all_source_files.add(str(proc_file.relative_to(ROOT_DIR)).replace("\\", "/"))

    for page in list_wiki_pages():
        rel = page.relative_to(WIKI_DIR)
        sources = get_wiki_sources(page)
        if not sources:
            issues.append({
                "severity": "warning",
                "check": "unsourced_claim",
                "kb": "external",
                "file": str(rel),
                "detail": "Article has no sources field — claims cannot be traced to source files",
            })
            continue

        for src in sources:
            src_stripped = src.strip().strip('"').strip("'")
            if src_stripped and src_stripped not in all_source_files:
                # Check if it's a partial match (e.g., directory prefix)
                found = any(s.endswith(src_stripped) or src_stripped.endswith(s) for s in all_source_files)
                if not found:
                    issues.append({
                        "severity": "warning",
                        "check": "unsourced_claim",
                        "kb": "external",
                        "file": str(rel),
                        "detail": f"Source not found on disk: {src_stripped}",
                    })
    return issues


async def check_contradictions_external() -> list[dict]:
    """Use LLM to detect contradictions across external wiki pages."""
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        TextBlock,
        query,
    )

    parts = []
    for page in list_wiki_pages():
        rel = page.relative_to(WIKI_DIR)
        content = page.read_text(encoding="utf-8")
        parts.append(f"## {rel}\n\n{content}")

    wiki_content = "\n\n---\n\n".join(parts)

    prompt = f"""Review this external knowledge base for contradictions, inconsistencies, or
conflicting claims across articles.

## External Wiki

{wiki_content}

## Instructions

Look for:
- Direct contradictions (article A says X, article B says not-X)
- Inconsistent recommendations (different articles recommend conflicting approaches)
- Outdated information that conflicts with newer entries

For each issue found, output EXACTLY one line in this format:
CONTRADICTION: [file1] vs [file2] - description of the conflict
INCONSISTENCY: [file] - description of the inconsistency

If no issues found, output exactly: NO_ISSUES

Do NOT output anything else - no preamble, no explanation, just the formatted lines."""

    response = ""
    try:
        async for message in query(
            prompt=prompt,
            options=ClaudeAgentOptions(
                cwd=str(ROOT_DIR),
                allowed_tools=[],
                max_turns=2,
            ),
        ):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        response += block.text
    except Exception as e:
        return [{"severity": "error", "check": "contradiction", "kb": "external", "file": "(system)", "detail": f"LLM check failed: {e}"}]

    issues = []
    if "NO_ISSUES" not in response:
        for line in response.strip().split("\n"):
            line = line.strip()
            if line.startswith("CONTRADICTION:") or line.startswith("INCONSISTENCY:"):
                issues.append({
                    "severity": "warning",
                    "check": "contradiction",
                    "kb": "external",
                    "file": "(cross-article)",
                    "detail": line,
                })

    return issues


# ── Report generation ──────────────────────────────────────────────────

def generate_report(all_issues: list[dict], kb_scope: str) -> str:
    """Generate a markdown lint report."""
    errors = [i for i in all_issues if i["severity"] == "error"]
    warnings = [i for i in all_issues if i["severity"] == "warning"]
    suggestions = [i for i in all_issues if i["severity"] == "suggestion"]

    lines = [
        f"# Lint Report - {today_iso()}",
        "",
        f"**Scope:** {kb_scope}",
        f"**Total issues:** {len(all_issues)}",
        f"- Errors: {len(errors)}",
        f"- Warnings: {len(warnings)}",
        f"- Suggestions: {len(suggestions)}",
        "",
    ]

    for severity, issues, marker in [
        ("Errors", errors, "x"),
        ("Warnings", warnings, "!"),
        ("Suggestions", suggestions, "?"),
    ]:
        if issues:
            lines.append(f"## {severity}")
            lines.append("")
            for issue in issues:
                fixable = " (auto-fixable)" if issue.get("auto_fixable") else ""
                kb_tag = f"[{issue.get('kb', '?')}]" if kb_scope == "both" else ""
                lines.append(f"- **[{marker}]** {kb_tag} `{issue['file']}` - {issue['detail']}{fixable}")
            lines.append("")

    if not all_issues:
        lines.append("All checks passed. Knowledge base is healthy.")
        lines.append("")

    return "\n".join(lines)


# ── Main ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Lint the knowledge base(s)")
    parser.add_argument(
        "--structural-only",
        action="store_true",
        help="Skip LLM-based checks (contradictions) - faster and free",
    )
    parser.add_argument(
        "--kb",
        choices=["internal", "external", "both"],
        default="both",
        help="Which knowledge base to lint (default: both)",
    )
    args = parser.parse_args()

    all_issues: list[dict] = []

    # Internal KB checks
    if args.kb in ("internal", "both"):
        print("Running Internal KB (knowledge/) lint checks...")
        internal_checks = [
            ("Broken links", check_broken_links_internal),
            ("Orphan pages", check_orphan_pages_internal),
            ("Orphan sources", check_orphan_sources_internal),
            ("Stale articles", check_stale_articles_internal),
            ("Missing backlinks", check_missing_backlinks_internal),
            ("Sparse articles", check_sparse_articles_internal),
            ("Unsourced claims", check_unsourced_claims_internal),
        ]

        for name, check_fn in internal_checks:
            print(f"  Checking: {name}...")
            issues = check_fn()
            all_issues.extend(issues)
            print(f"    Found {len(issues)} issue(s)")

        if not args.structural_only:
            print("  Checking: Contradictions (LLM)...")
            issues = asyncio.run(check_contradictions_internal())
            all_issues.extend(issues)
            print(f"    Found {len(issues)} issue(s)")
        else:
            print("  Skipping: Contradictions (--structural-only)")

    # External KB checks
    if args.kb in ("external", "both"):
        print("\nRunning External KB (wiki/) lint checks...")
        if not WIKI_DIR.exists():
            print("  Skipping: wiki/ directory does not exist")
        else:
            external_checks = [
                ("Broken links", check_broken_links_external),
                ("Orphan pages", check_orphan_pages_external),
                ("Orphan sources", check_orphan_sources_external),
                ("Missing backlinks", check_missing_backlinks_external),
                ("Sparse articles", check_sparse_articles_external),
                ("Unsourced claims", check_unsourced_claims_external),
            ]

            for name, check_fn in external_checks:
                print(f"  Checking: {name}...")
                issues = check_fn()
                all_issues.extend(issues)
                print(f"    Found {len(issues)} issue(s)")

            if not args.structural_only:
                print("  Checking: Contradictions (LLM)...")
                issues = asyncio.run(check_contradictions_external())
                all_issues.extend(issues)
                print(f"    Found {len(issues)} issue(s)")
            else:
                print("  Skipping: Contradictions (--structural-only)")

    # Generate and save report
    report = generate_report(all_issues, args.kb)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"lint-{today_iso()}.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport saved to: {report_path}")

    # Update state
    state = load_state()
    state["last_lint"] = now_iso()
    save_state(state)

    # Summary
    errors = sum(1 for i in all_issues if i["severity"] == "error")
    warnings = sum(1 for i in all_issues if i["severity"] == "warning")
    suggestions = sum(1 for i in all_issues if i["severity"] == "suggestion")
    print(f"\nResults: {errors} errors, {warnings} warnings, {suggestions} suggestions")

    if errors > 0:
        print("\nErrors found - knowledge base needs attention!")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())