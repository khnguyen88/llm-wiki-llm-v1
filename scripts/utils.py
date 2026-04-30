"""Shared utilities for the personal knowledge base."""

import hashlib
import json
import re
from pathlib import Path

from config import (
    AI_RESEARCH_DIR,
    CONCEPTS_DIR,
    CONNECTIONS_DIR,
    DAILY_DIR,
    INDEX_FILE,
    KNOWLEDGE_DIR,
    LOG_FILE,
    PROCESSED_DIR,
    QA_DIR,
    RAW_DIR,
    STATE_FILE,
    WIKI_CONCEPTS_DIR,
    WIKI_DIR,
    WIKI_ENTITIES_DIR,
    WIKI_QANDA_DIR,
    WIKI_SOURCES_MANIFEST_FILE,
    WIKI_SUMMARIES_DIR,
)


# ── State management ──────────────────────────────────────────────────

def load_state() -> dict:
    """Load persistent state from state.json."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"ingested": {}, "query_count": 0, "last_lint": None, "total_cost": 0.0}


def save_state(state: dict) -> None:
    """Save state to state.json."""
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


# ── File hashing ──────────────────────────────────────────────────────

def file_hash(path: Path) -> str:
    """SHA-256 hash of a file (first 16 hex chars)."""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


# ── Slug / naming ─────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


# ── Wikilink helpers ──────────────────────────────────────────────────

def extract_wikilinks(content: str) -> list[str]:
    """Extract all [[wikilinks]] from markdown content, stripping display text from pipe syntax.

    Supports both [[target]] and [[target|display text]] Obsidian-style links.
    """
    links = re.findall(r"\[\[([^\]]+)\]\]", content)
    return [link.split("|")[0].strip() for link in links]


def wiki_article_exists(link: str) -> bool:
    """Check if a wikilinked article exists on disk."""
    path = KNOWLEDGE_DIR / f"{link}.md"
    return path.exists()


# ── Wiki content helpers ──────────────────────────────────────────────

def read_wiki_index() -> str:
    """Read the knowledge base index file."""
    if INDEX_FILE.exists():
        return INDEX_FILE.read_text(encoding="utf-8")
    return "# Knowledge Base Index\n\n| Article | Summary | Compiled From | Updated |\n|---------|---------|---------------|---------|"


def read_all_wiki_content() -> str:
    """Read index + all wiki articles into a single string for context."""
    parts = [f"## INDEX\n\n{read_wiki_index()}"]

    for subdir in [CONCEPTS_DIR, CONNECTIONS_DIR, QA_DIR]:
        if not subdir.exists():
            continue
        for md_file in sorted(subdir.glob("*.md")):
            rel = md_file.relative_to(KNOWLEDGE_DIR)
            content = md_file.read_text(encoding="utf-8")
            parts.append(f"## {rel}\n\n{content}")

    return "\n\n---\n\n".join(parts)


def list_wiki_articles() -> list[Path]:
    """List all wiki article files."""
    articles = []
    for subdir in [CONCEPTS_DIR, CONNECTIONS_DIR, QA_DIR]:
        if subdir.exists():
            articles.extend(sorted(subdir.glob("*.md")))
    return articles


def list_raw_files() -> list[Path]:
    """List all daily log files."""
    if not DAILY_DIR.exists():
        return []
    return sorted(DAILY_DIR.glob("*.md"))


# ── Index helpers ─────────────────────────────────────────────────────

def count_inbound_links(target: str, exclude_file: Path | None = None) -> int:
    """Count how many wiki articles link to a given target."""
    count = 0
    for article in list_wiki_articles():
        if article == exclude_file:
            continue
        content = article.read_text(encoding="utf-8")
        if f"[[{target}]]" in content:
            count += 1
    return count


def get_article_word_count(path: Path) -> int:
    """Count words in an article, excluding YAML frontmatter."""
    content = path.read_text(encoding="utf-8")
    # Strip frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:]
    return len(content.split())


def build_index_entry(rel_path: str, summary: str, sources: str, updated: str) -> str:
    """Build a single index table row."""
    link = rel_path.replace(".md", "")
    return f"| [[{link}]] | {summary} | {sources} | {updated} |"


# ── External wiki helpers ──────────────────────────────────────────────

def list_wiki_pages() -> list[Path]:
    """List all external wiki article files (concepts, entities, summaries, qanda)."""
    articles = []
    for subdir in [WIKI_CONCEPTS_DIR, WIKI_ENTITIES_DIR, WIKI_SUMMARIES_DIR, WIKI_QANDA_DIR]:
        if subdir.exists():
            articles.extend(sorted(subdir.glob("*.md")))
    return articles


def wiki_page_exists(link: str) -> bool:
    """Check if a wikilinked wiki page exists on disk."""
    for subdir in [WIKI_CONCEPTS_DIR, WIKI_ENTITIES_DIR, WIKI_SUMMARIES_DIR, WIKI_QANDA_DIR]:
        if not subdir.exists():
            continue
        candidate = subdir / f"{link.split('/')[-1]}.md"
        if candidate.exists():
            return True
    return False


def list_source_files() -> list[Path]:
    """List all source files in raw/ and ai-research/ (all subfolders)."""
    files = []
    for base in [RAW_DIR, AI_RESEARCH_DIR]:
        if not base.exists():
            continue
        for md_file in sorted(base.rglob("*.md")):
            files.append(md_file)
    return files


def list_processed_files() -> list[Path]:
    """List all files in processed/ (all subfolders)."""
    if not PROCESSED_DIR.exists():
        return []
    return sorted(PROCESSED_DIR.rglob("*.md"))


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown content into a dict."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end].strip()
    result = {}
    current_list_key = None
    for line in fm_text.split("\n"):
        line = line.strip()
        if line.startswith("- "):
            if current_list_key and current_list_key in result:
                if isinstance(result[current_list_key], list):
                    result[current_list_key].append(line[2:].strip().strip('"').strip("'"))
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val == "":
                result[key] = []
                current_list_key = key
            else:
                result[key] = val
                current_list_key = None
    return result


def get_wiki_sources(article_path: Path) -> list[str]:
    """Extract source file paths from a wiki article's frontmatter."""
    content = article_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    sources_raw = fm.get("sources", "")
    if isinstance(sources_raw, str):
        if not sources_raw:
            return []
        return [s.strip().strip('"').strip("'") for s in sources_raw.split(",") if s.strip()]
    return sources_raw
