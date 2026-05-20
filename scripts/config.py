"""Path constants and configuration for the personal knowledge base."""

from pathlib import Path
from datetime import datetime, timezone
import os

# ── Paths ──────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent.parent
DAILY_DIR = ROOT_DIR / "daily"
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
CONCEPTS_DIR = KNOWLEDGE_DIR / "concepts"
CONNECTIONS_DIR = KNOWLEDGE_DIR / "connections"
QA_DIR = KNOWLEDGE_DIR / "qa"
REPORTS_DIR = ROOT_DIR / "reports"
SCRIPTS_DIR = ROOT_DIR / "scripts"
PROMPTS_DIR = SCRIPTS_DIR / "prompts"
HOOKS_DIR = ROOT_DIR / "hooks"
AGENTS_FILE = ROOT_DIR / "AGENTS.md"

INDEX_FILE = KNOWLEDGE_DIR / "index.md"
LOG_FILE = KNOWLEDGE_DIR / "log.md"
STATE_FILE = SCRIPTS_DIR / "state.json"

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

# ── Document processing pipeline ────────────────────────────────────────

# Tool endpoints (from .env or defaults)
DOCLING_URL = os.getenv("DOCLING_SERVE_URL", "http://localhost:5001")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", None)

# Pre-processing
PDF_SPLIT_PAGE_SIZE = int(os.getenv("PDF_SPLIT_PAGE_SIZE", "25"))

# Chunking thresholds
CHUNK_MAX_WORDS = int(os.getenv("CHUNK_MAX_WORDS", "3000"))
CHUNK_TARGET_WORDS = int(os.getenv("CHUNK_TARGET_WORDS", "1500"))

# OCR cascade thresholds
DOCLING_CONFIDENCE_THRESHOLD = float(os.getenv("DOCLING_CONFIDENCE_THRESHOLD", "0.8"))
ARRASE_CONFIDENCE_FLOOR = float(os.getenv("ARRASE_CONFIDENCE_FLOOR", "0.7"))
LLM_OCR_CONFIDENCE_FLOOR = float(os.getenv("LLM_OCR_CONFIDENCE_FLOOR", "0.5"))

# Auto-remediation
MAX_AUTO_ATTEMPTS = int(os.getenv("MAX_AUTO_ATTEMPTS", "3"))
WEBSEARCH_CONFIDENCE_FLOOR = float(os.getenv("WEBSEARCH_CONFIDENCE_FLOOR", "0.6"))

# New directory
RAW_MARKDOWN_DIR = ROOT_DIR / "002-raw-preprocessed"

# ── Timezone ───────────────────────────────────────────────────────────
TIMEZONE = "America/Chicago"


def now_iso() -> str:
    """Current time in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today_iso() -> str:
    """Current date in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")
