import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone


def call_api(chat_model_provider_id, chat_model_key, embedding_model_provider_id, embedding_model_key, web_search_query):
    url = "http://localhost:3000/api/search"
    payload = {
        "chatModel": {
            "providerId": chat_model_provider_id,
            "key": chat_model_key
        },
        "embeddingModel": {
            "providerId": embedding_model_provider_id,
            "key": embedding_model_key
        },
        "optimizationMode": "quality",
        "sources": ["web", "academic"],
        "query": web_search_query,
        "history": [],
        "systemInstructions": "Include the original message and source contents just cleaned up, but be sure to include inline citations using [n] notation referencing numbered sources. After the main response, add a References section listing each source with its number, title, published date of sources (if possible), and URL. Provide metadata such as search/fetch date, api/tool used.",
        "stream": False
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=600) as response:
        return response.read().decode("utf-8")


def slugify(text):
    """Convert text to a kebab-case slug for file naming."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:80]


def extract_website(url):
    """Extract domain from URL for the website field."""
    if not url:
        return ""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.netloc
        # Strip www. prefix
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception:
        return ""


def format_schema_header(query, sources, search_date, tool_used, tool_model, embedding_model):
    """Format the ai-research-multi HTML comment metadata header per WIKI_SCHEMA.md."""
    lines = [
        "type: ai-research-multi",
        f"search_date: {search_date}",
        f"query: {query}",
        f"tool_used: {tool_used}",
        f"tool_model: {tool_model}",
    ]
    if embedding_model:
        lines.append(f"embedding_model: {embedding_model}")
    lines.append("sources:")

    for src in sources:
        meta = src.get("metadata", {})
        url = meta.get("url", "")
        title = meta.get("title", "")
        published = meta.get("published_date", "")
        website = extract_website(url)

        lines.append(f"  - url: {url}")
        if title:
            lines.append(f'    title: "{title}"')
        if website:
            lines.append(f"    website: {website}")
        if published:
            lines.append(f"    published_date: {published}")

    return "<!--\n" + "\n".join(lines) + "\n-->"


def main():
    parser = argparse.ArgumentParser(description="Dependency-free HTTP caller for Vane web search")
    parser.add_argument("chat_model_provider_id", help="UUID of chat model provider")
    parser.add_argument("chat_model_key", help="Chat model key (e.g., gemma4:31b-cloud)")
    parser.add_argument("embedding_model_provider_id", help="UUID of embedding model provider")
    parser.add_argument("embedding_model_key", help="Embedding model key")
    parser.add_argument("web_search_query", help="Web search query to send to Vane")
    parser.add_argument("--save", action="store_true",
                        help="Save result to ai-research/web/ as ai-research-multi schema file")
    parser.add_argument("--output-dir", default="ai-research/web",
                        help="Directory to save output file (default: ai-research/web)")

    args = parser.parse_args()
    raw = call_api(args.chat_model_provider_id, args.chat_model_key,
                    args.embedding_model_provider_id, args.embedding_model_key,
                    args.web_search_query)

    try:
        result = json.loads(raw)
        message = result.get("message", "")
        sources = result.get("sources", [])
        search_date = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

        # Build schema-formatted header
        header = format_schema_header(
            query=args.web_search_query,
            sources=sources,
            search_date=search_date,
            tool_used="vane_web_search",
            tool_model=args.chat_model_key,
            embedding_model=args.embedding_model_key
        )

        output_parts = [header, ""]

        # Message body (preserved verbatim)
        if message:
            output_parts.append(message)

        # Sources reference section
        if sources:
            output_parts.append("\n---\n\n## Sources\n")
            for i, src in enumerate(sources, 1):
                meta = src.get("metadata", {})
                title = meta.get("title", f"Source {i}")
                url = meta.get("url", "")
                line = f"[{i}] {title}"
                if url:
                    line += f" — {url}"
                output_parts.append(line)

        full_output = "\n".join(output_parts)
        sys.stdout.buffer.write(full_output.encode("utf-8", errors="replace"))
        sys.stdout.buffer.write(b"\n")

        # Save to file if --save flag is provided
        if args.save:
            slug = slugify(args.web_search_query)
            date_str = search_date[:10]  # YYYY-MM-DD for filename
            filename = f"{slug}-{date_str}.md"
            filepath = os.path.join(args.output_dir, filename)
            os.makedirs(args.output_dir, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(full_output + "\n")
            sys.stderr.write(f"Saved to {filepath}\n")

    except (json.JSONDecodeError, KeyError):
        # Fallback: output raw response if parsing fails
        sys.stdout.buffer.write(raw.encode("utf-8", errors="replace"))
        sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()