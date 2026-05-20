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
