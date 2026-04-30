"""Rename existing openrouter .md files to include 3-digit index from ALL_URLS order."""
import re
from pathlib import Path
from urllib.parse import urlparse

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "raw" / "document"
WEBSITE = "openrouter"
DATE = "2026-04-29"

# Read ALL_URLS from crawl script
src = (Path(__file__).resolve().parent / "crawl_openrouter_docs.py").read_text(encoding="utf-8")
match = re.search(r"ALL_URLS\s*=\s*\[(.*?)\]", src, re.DOTALL)
if not match:
    raise RuntimeError("Could not find ALL_URLS in crawl script")
ALL_URLS = re.findall(r'"(https://[^"]+)"', match.group(1))

url_to_index = {url: idx + 1 for idx, url in enumerate(ALL_URLS)}


def derive_webpage_name(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if path.startswith("docs/"):
        path = path[len("docs/"):]
    path = re.sub(r"\.mdx$", "", path)
    path = path.replace("/", "-")
    return path or "docs-index"


# Build name->index map
name_to_idx = {}
for url in ALL_URLS:
    wn = derive_webpage_name(url)
    name_to_idx[wn] = url_to_index[url]

prefix = f"{WEBSITE}-"
suffix = f"-{DATE}"
renamed = 0
skipped = 0

for old_file in sorted(OUTPUT_DIR.glob(f"{WEBSITE}-*-{DATE}.md")):
    stem = old_file.stem

    # Already has index? (openrouter-001-xxx-2026-04-29)
    after_prefix = stem[len(prefix):]
    if re.match(r"^\d{3}-", after_prefix):
        skipped += 1
        continue

    webpage_name = after_prefix[: -len(suffix)]
    idx = name_to_idx.get(webpage_name)
    if idx is None:
        print(f"NO_MATCH: {old_file.name}")
        skipped += 1
        continue

    new_name = f"{WEBSITE}-{idx:03d}-{webpage_name}-{DATE}.md"
    new_file = OUTPUT_DIR / new_name

    # Update content header: add Index line
    content = old_file.read_text(encoding="utf-8")
    if "Index:" not in content:
        content = re.sub(
            r"(Webpage: [^\n]+)\n(\-\->)",
            rf"\1\nIndex: {idx}\n\2",
            content,
        )

    new_file.write_text(content, encoding="utf-8")
    if new_file != old_file:
        old_file.unlink()
    renamed += 1

print(f"Renamed: {renamed}, Skipped: {skipped}")