"""BFS crawl of Claude Code docs via crawl4ai REST API and save as indexed markdown files."""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

API_URL = "http://localhost:11235/crawl"
URL_LIST = os.path.join(os.path.dirname(__file__), "claude_en_urls.txt")
OUTPUT_DIR = Path(r"C:\_AAA\JVR\llm-wiki-llm-v1\raw\document")
WEBSITE_NAME = "claude-code"
DATE = "2026-04-29"
BATCH_SIZE = 5
DELAY_BETWEEN_BATCHES = 2  # seconds


def read_urls(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def url_to_page_name(url: str) -> str:
    m = re.search(r"/docs/en/(.+?)(?:\.md)?$", url)
    if m:
        return m.group(1).replace("/", "-")
    return "unknown"


def crawl_batch(urls: list[str]) -> list[dict]:
    payload = json.dumps({
        "urls": urls,
        "word_count_threshold": 1,
        "cache_mode": "bypass",
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("results", [])
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"  ERROR crawling batch: {e}", file=sys.stderr)
        return []


def build_file_content(url: str, page_name: str, markdown: str, index: int) -> str:
    title = page_name.replace("-", " ")
    title = " ".join(w.capitalize() for w in title.split())

    header = (
        f"<!--\n"
        f"url: {url}\n"
        f"download_date: {DATE}\n"
        f"website: {WEBSITE_NAME}\n"
        f"webpage: {page_name}\n"
        f"-->\n\n"
        f"# {title}\n\n"
    )
    return header + markdown


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    urls = read_urls(URL_LIST)
    total = len(urls)
    print(f"Starting BFS crawl of {total} Claude Code doc pages...")

    # Build an index mapping URL -> (idx, page_name, filename)
    url_meta = {}
    for i, url in enumerate(urls):
        idx = i + 1
        page_name = url_to_page_name(url)
        filename = f"{WEBSITE_NAME}-{idx:03d}-{page_name}-{DATE}.md"
        url_meta[url] = (idx, page_name, filename)

    success = 0
    failed = 0

    for batch_start in range(0, total, BATCH_SIZE):
        batch_end = min(batch_start + BATCH_SIZE, total)
        batch_urls = urls[batch_start:batch_end]
        print(f"\nBatch {batch_start // BATCH_SIZE + 1}: URLs {batch_start + 1}-{batch_end}")

        results = crawl_batch(batch_urls)

        for result in results:
            url = result.get("url", "")
            if url not in url_meta:
                print(f"  Unknown URL in results: {url}", file=sys.stderr)
                continue

            idx, page_name, filename = url_meta[url]
            filepath = OUTPUT_DIR / filename

            if not result.get("success", False):
                error = result.get("error_message", "unknown error")
                print(f"  [{idx}/{total}] FAILED: {filename} - {error}")
                failed += 1
                continue

            md_obj = result.get("markdown", {})
            markdown = md_obj.get("raw_markdown", "") if isinstance(md_obj, dict) else ""

            if not markdown:
                print(f"  [{idx}/{total}] WARNING: Empty markdown for {url}", file=sys.stderr)
                failed += 1
                continue

            content = build_file_content(url, page_name, markdown, idx)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  [{idx}/{total}] Saved: {filename} ({len(markdown):,} chars)")
            success += 1

        if batch_end < total:
            print(f"  Pausing {DELAY_BETWEEN_BATCHES}s...")
            time.sleep(DELAY_BETWEEN_BATCHES)

    print(f"\nDone! Success: {success}, Failed: {failed}, Total: {total}")


if __name__ == "__main__":
    main()