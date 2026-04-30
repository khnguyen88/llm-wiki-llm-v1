"""Path constants and configuration for the personal knowledge base."""

from pathlib import Path
from datetime import datetime, timezone

# ── Paths ──────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent.parent
DAILY_DIR = ROOT_DIR / "daily"
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
CONCEPTS_DIR = KNOWLEDGE_DIR / "concepts"
CONNECTIONS_DIR = KNOWLEDGE_DIR / "connections"
QA_DIR = KNOWLEDGE_DIR / "qa"
REPORTS_DIR = ROOT_DIR / "reports"
SCRIPTS_DIR = ROOT_DIR / "scripts"
HOOKS_DIR = ROOT_DIR / "hooks"
AGENTS_FILE = ROOT_DIR / "AGENTS.md"

INDEX_FILE = KNOWLEDGE_DIR / "index.md"
LOG_FILE = KNOWLEDGE_DIR / "log.md"
STATE_FILE = SCRIPTS_DIR / "state.json"

# External KB paths
WIKI_DIR = ROOT_DIR / "wiki"
WIKI_CONCEPTS_DIR = WIKI_DIR / "concepts"
WIKI_ENTITIES_DIR = WIKI_DIR / "entities"
WIKI_SUMMARIES_DIR = WIKI_DIR / "summaries"
WIKI_QANDA_DIR = WIKI_DIR / "qanda"
WIKI_INDEX_FILE = WIKI_DIR / "index.md"
WIKI_SOURCES_MANIFEST_FILE = WIKI_DIR / "sources-manifest.md"
WIKI_LOG_FILE = WIKI_DIR / "log.md"

RAW_DIR = ROOT_DIR / "raw"
AI_RESEARCH_DIR = ROOT_DIR / "ai-research"
PROCESSED_DIR = ROOT_DIR / "processed"

# ── Timezone ───────────────────────────────────────────────────────────
TIMEZONE = "America/Chicago"


def now_iso() -> str:
    """Current time in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today_iso() -> str:
    """Current date in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")
