"""
BFS crawl of OpenRouter docs using crawl4ai REST API.
Fetches all documentation pages and saves each as a markdown file.
"""

import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)

CRAWL4AI_URL = "http://localhost:11235/crawl"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "raw" / "document"
DATE = "2026-04-29"
WEBSITE_NAME = "openrouter"
BATCH_SIZE = 5
BATCH_DELAY = 2  # seconds between batches

# Complete URL list from llms.txt (BFS seed → discovered links)
ALL_URLS = [
    "https://openrouter.ai/docs/quickstart.mdx",
    "https://openrouter.ai/docs/guides/overview/principles.mdx",
    "https://openrouter.ai/docs/guides/overview/models.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/overview.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/images.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/image-generation.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/pdfs.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/audio.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/videos.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/video-generation.mdx",
    "https://openrouter.ai/docs/guides/overview/multimodal/tts.mdx",
    "https://openrouter.ai/docs/guides/overview/auth/oauth.mdx",
    "https://openrouter.ai/docs/guides/overview/auth/management-api-keys.mdx",
    "https://openrouter.ai/docs/guides/overview/auth/byok.mdx",
    "https://openrouter.ai/docs/faq.mdx",
    "https://openrouter.ai/docs/guides/overview/report-feedback.mdx",
    "https://openrouter.ai/docs/guides/routing/model-fallbacks.mdx",
    "https://openrouter.ai/docs/guides/routing/provider-selection.mdx",
    "https://openrouter.ai/docs/guides/routing/auto-exacto.mdx",
    "https://openrouter.ai/docs/guides/routing/model-variants/free.mdx",
    "https://openrouter.ai/docs/guides/routing/model-variants/extended.mdx",
    "https://openrouter.ai/docs/guides/routing/model-variants/exacto.mdx",
    "https://openrouter.ai/docs/guides/routing/model-variants/thinking.mdx",
    "https://openrouter.ai/docs/guides/routing/model-variants/online.mdx",
    "https://openrouter.ai/docs/guides/routing/model-variants/nitro.mdx",
    "https://openrouter.ai/docs/guides/routing/routers/auto-router.mdx",
    "https://openrouter.ai/docs/guides/routing/routers/body-builder.mdx",
    "https://openrouter.ai/docs/guides/routing/routers/free-models-router.mdx",
    "https://openrouter.ai/docs/guides/features/workspaces.mdx",
    "https://openrouter.ai/docs/guides/features/presets.mdx",
    "https://openrouter.ai/docs/guides/features/response-caching.mdx",
    "https://openrouter.ai/docs/guides/features/tool-calling.mdx",
    "https://openrouter.ai/docs/guides/features/server-tools/overview.mdx",
    "https://openrouter.ai/docs/guides/features/server-tools/web-search.mdx",
    "https://openrouter.ai/docs/guides/features/server-tools/web-fetch.mdx",
    "https://openrouter.ai/docs/guides/features/server-tools/datetime.mdx",
    "https://openrouter.ai/docs/guides/features/server-tools/image-generation.mdx",
    "https://openrouter.ai/docs/guides/features/plugins/overview.mdx",
    "https://openrouter.ai/docs/guides/features/plugins/web-search.mdx",
    "https://openrouter.ai/docs/guides/features/plugins/response-healing.mdx",
    "https://openrouter.ai/docs/guides/features/structured-outputs.mdx",
    "https://openrouter.ai/docs/guides/features/message-transforms.mdx",
    "https://openrouter.ai/docs/guides/features/zero-completion-insurance.mdx",
    "https://openrouter.ai/docs/guides/features/zdr.mdx",
    "https://openrouter.ai/docs/app-attribution.mdx",
    "https://openrouter.ai/docs/guides/features/guardrails.mdx",
    "https://openrouter.ai/docs/guides/features/service-tiers.mdx",
    "https://openrouter.ai/docs/guides/features/input-output-logging.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/overview.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/arize.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/braintrust.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/clickhouse.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/opik.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/datadog.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/grafana.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/langfuse.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/langsmith.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/newrelic.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/otel-collector.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/posthog.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/ramp.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/s3.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/sentry.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/snowflake.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/weave.mdx",
    "https://openrouter.ai/docs/guides/features/broadcast/webhook.mdx",
    "https://openrouter.ai/docs/guides/privacy/data-collection.mdx",
    "https://openrouter.ai/docs/guides/privacy/provider-logging.mdx",
    "https://openrouter.ai/docs/guides/best-practices/latency-and-performance.mdx",
    "https://openrouter.ai/docs/guides/best-practices/prompt-caching.mdx",
    "https://openrouter.ai/docs/guides/best-practices/uptime-optimization.mdx",
    "https://openrouter.ai/docs/guides/best-practices/reasoning-tokens.mdx",
    "https://openrouter.ai/docs/guides/administration/activity-export.mdx",
    "https://openrouter.ai/docs/guides/administration/api-key-rotation.mdx",
    "https://openrouter.ai/docs/guides/administration/crypto-api.mdx",
    "https://openrouter.ai/docs/guides/administration/organization-management.mdx",
    "https://openrouter.ai/docs/guides/administration/usage-accounting.mdx",
    "https://openrouter.ai/docs/guides/administration/user-tracking.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/automatic-code-review.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/create-agent-harness-tui.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/create-headless-agent.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/claude-code-integration.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/claude-desktop-integration.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/codex-cli.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/junie.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/mcp-servers.mdx",
    "https://openrouter.ai/docs/guides/coding-agents/openclaw-integration.mdx",
    "https://openrouter.ai/docs/guides/evaluate-and-optimize/distillation.mdx",
    "https://openrouter.ai/docs/guides/evaluate-and-optimize/model-migrations/claude-4-7.mdx",
    "https://openrouter.ai/docs/guides/evaluate-and-optimize/model-migrations/claude-4-6.mdx",
    "https://openrouter.ai/docs/guides/evaluate-and-optimize/model-migrations/gpt-5-4.mdx",
    "https://openrouter.ai/docs/guides/evaluate-and-optimize/rag.mdx",
    "https://openrouter.ai/docs/guides/evaluate-and-optimize/red-teaming.mdx",
    "https://openrouter.ai/docs/guides/get-started/enterprise-quickstart.mdx",
    "https://openrouter.ai/docs/guides/get-started/for-providers.mdx",
    "https://openrouter.ai/docs/guides/get-started/free-models-router-playground.mdx",
    "https://openrouter.ai/docs/guides/get-started/sovereign-ai.mdx",
    "https://openrouter.ai/docs/guides/get-started/stripe-projects.mdx",
    "https://openrouter.ai/docs/guides/community/frameworks-and-integrations-overview.mdx",
    "https://openrouter.ai/docs/guides/community/awesome-openrouter.mdx",
    "https://openrouter.ai/docs/guides/community/effect-ai-sdk.mdx",
    "https://openrouter.ai/docs/guides/community/arize.mdx",
    "https://openrouter.ai/docs/guides/community/langchain.mdx",
    "https://openrouter.ai/docs/guides/community/livekit.mdx",
    "https://openrouter.ai/docs/guides/community/langfuse.mdx",
    "https://openrouter.ai/docs/guides/community/mastra.mdx",
    "https://openrouter.ai/docs/guides/community/openai-sdk.mdx",
    "https://openrouter.ai/docs/guides/community/anthropic-agent-sdk.mdx",
    "https://openrouter.ai/docs/guides/community/pydantic-ai.mdx",
    "https://openrouter.ai/docs/guides/community/tanstack-ai.mdx",
    "https://openrouter.ai/docs/guides/community/vercel-ai-sdk.mdx",
    "https://openrouter.ai/docs/guides/community/xcode.mdx",
    "https://openrouter.ai/docs/guides/community/zapier.mdx",
    "https://openrouter.ai/docs/guides/community/infisical.mdx",
    "https://openrouter.ai/docs/api/reference/overview.mdx",
    "https://openrouter.ai/docs/api/reference/streaming.mdx",
    "https://openrouter.ai/docs/api/reference/embeddings.mdx",
    "https://openrouter.ai/docs/api/reference/limits.mdx",
    "https://openrouter.ai/docs/api/reference/authentication.mdx",
    "https://openrouter.ai/docs/api/reference/parameters.mdx",
    "https://openrouter.ai/docs/api/reference/errors-and-debugging.mdx",
    "https://openrouter.ai/docs/api/reference/responses/overview.mdx",
    "https://openrouter.ai/docs/api/reference/responses/basic-usage.mdx",
    "https://openrouter.ai/docs/api/reference/responses/reasoning.mdx",
    "https://openrouter.ai/docs/api/reference/responses/tool-calling.mdx",
    "https://openrouter.ai/docs/api/reference/responses/web-search.mdx",
    "https://openrouter.ai/docs/api/reference/responses/error-handling.mdx",
    "https://openrouter.ai/docs/client-sdks/overview.mdx",
    "https://openrouter.ai/docs/client-sdks/usage-for-agents.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/overview.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/analytics.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/apikeys.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/chat.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/credits.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/embeddings.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/endpoints.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/generations.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/guardrails.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/models/models.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/oauth.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/organization.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/providers.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/rerank.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/responses.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/tts.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/videogeneration.mdx",
    "https://openrouter.ai/docs/client-sdks/typescript/api-reference/workspaces.mdx",
    "https://openrouter.ai/docs/client-sdks/python/overview.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/analytics.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/apikeys.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/chat.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/credits.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/embeddings.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/endpoints.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/generations.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/guardrails.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/models/models.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/oauth.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/organization.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/providers.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/rerank.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/responses.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/tts.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/videogeneration.mdx",
    "https://openrouter.ai/docs/client-sdks/python/api-reference/workspaces.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/analytics.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/apikeys.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/chat.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/credits.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/embeddings.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/endpoints.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/generations.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/guardrails.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/models/models.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/oauth.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/organization.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/providers.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/rerank.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/responses.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/tts.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/videogeneration.mdx",
    "https://openrouter.ai/docs/client-sdks/go/api-reference/workspaces.mdx",
    "https://openrouter.ai/docs/client-sdks/dev-tools/devtools.mdx",
    "https://openrouter.ai/docs/client-sdks/agent-migration.mdx",
    "https://openrouter.ai/docs/agent-sdk/overview.mdx",
    "https://openrouter.ai/docs/agent-sdk/usage-for-agents.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/overview.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/working-with-items.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/api-reference.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/dynamic-parameters.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/next-turn-params.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/stop-conditions.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/streaming.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/text-generation.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/message-formats.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/tools.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/tool-approval-state.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/examples/weather-tool.mdx",
    "https://openrouter.ai/docs/agent-sdk/call-model/examples/skills-loader.mdx",
    "https://openrouter.ai/docs/api/api-reference/responses/create-responses.mdx",
    "https://openrouter.ai/docs/api/api-reference/o-auth/exchange-auth-code-for-api-key.mdx",
    "https://openrouter.ai/docs/api/api-reference/o-auth/create-auth-keys-code.mdx",
    "https://openrouter.ai/docs/api/api-reference/analytics/get-user-activity.mdx",
    "https://openrouter.ai/docs/api/api-reference/tts/create-audio-speech.mdx",
    "https://openrouter.ai/docs/api/api-reference/chat/send-chat-completion-request.mdx",
    "https://openrouter.ai/docs/api/api-reference/credits/get-credits.mdx",
    "https://openrouter.ai/docs/api/api-reference/embeddings/create-embeddings.mdx",
    "https://openrouter.ai/docs/api/api-reference/embeddings/list-embeddings-models.mdx",
    "https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints-zdr.mdx",
    "https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints.mdx",
    "https://openrouter.ai/docs/api/api-reference/generations/get-generation.mdx",
    "https://openrouter.ai/docs/api/api-reference/generations/list-generation-content.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/create-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/get-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/delete-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrail-key-assignments.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/bulk-assign-keys-to-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/bulk-unassign-keys-from-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrail-member-assignments.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/bulk-assign-members-to-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/bulk-unassign-members-from-guardrail.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/list-key-assignments.mdx",
    "https://openrouter.ai/docs/api/api-reference/guardrails/list-member-assignments.mdx",
    "https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key.mdx",
    "https://openrouter.ai/docs/api/api-reference/api-keys/list.mdx",
    "https://openrouter.ai/docs/api/api-reference/api-keys/create-keys.mdx",
    "https://openrouter.ai/docs/api/api-reference/api-keys/get-key.mdx",
    "https://openrouter.ai/docs/api/api-reference/api-keys/delete-keys.mdx",
    "https://openrouter.ai/docs/api/api-reference/api-keys/update-keys.mdx",
    "https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages.mdx",
    "https://openrouter.ai/docs/api/api-reference/models/get-models.mdx",
    "https://openrouter.ai/docs/api/api-reference/models/list-models-count.mdx",
    "https://openrouter.ai/docs/api/api-reference/models/list-models-user.mdx",
    "https://openrouter.ai/docs/api/api-reference/organization/list-organization-members.mdx",
    "https://openrouter.ai/docs/api/api-reference/providers/list-providers.mdx",
    "https://openrouter.ai/docs/api/api-reference/rerank/create-rerank.mdx",
    "https://openrouter.ai/docs/api/api-reference/video-generation/create-videos.mdx",
    "https://openrouter.ai/docs/api/api-reference/video-generation/get-videos.mdx",
    "https://openrouter.ai/docs/api/api-reference/video-generation/list-videos-content.mdx",
    "https://openrouter.ai/docs/api/api-reference/video-generation/list-videos-models.mdx",
    "https://openrouter.ai/docs/api/api-reference/workspaces/list-workspaces.mdx",
    "https://openrouter.ai/docs/api/api-reference/workspaces/create-workspace.mdx",
    "https://openrouter.ai/docs/api/api-reference/workspaces/get-workspace.mdx",
    "https://openrouter.ai/docs/api/api-reference/workspaces/delete-workspace.mdx",
    "https://openrouter.ai/docs/api/api-reference/workspaces/update-workspace.mdx",
    "https://openrouter.ai/docs/api/api-reference/workspaces/bulk-add-workspace-members.mdx",
    "https://openrouter.ai/docs/api/api-reference/workspaces/bulk-remove-workspace-members.mdx",
]


def derive_webpage_name(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if path.startswith("docs/"):
        path = path[len("docs/"):]
    path = re.sub(r"\.mdx$", "", path)
    path = path.replace("/", "-")
    return path or "docs-index"


def make_header(url: str, webpage_name: str, index: int) -> str:
    return (
        f"<!--\n"
        f"URL: {url}\n"
        f"Download Date: {DATE}\n"
        f"Website: {WEBSITE_NAME}\n"
        f"Webpage: {webpage_name}\n"
        f"Index: {index}\n"
        f"-->\n\n"
    )


def crawl_batch(urls: list[str]) -> list[dict]:
    payload = {
        "urls": urls,
        "browser_config": {"headless": True},
        "crawler_config": {"type": "CrawlerRunConfig", "cache_mode": "BYPASS"},
    }
    try:
        resp = requests.post(CRAWL4AI_URL, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        if data.get("success") and "results" in data:
            return data["results"]
        else:
            log.error(f"crawl4ai error: {data.get('detail', data)}")
            return []
    except Exception as e:
        log.error(f"Request failed: {e}")
        return []


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total = len(ALL_URLS)
    saved = 0
    failed = 0
    empty = 0

    log.info(f"Starting BFS crawl of {total} OpenRouter docs pages via crawl4ai")
    log.info(f"Output: {OUTPUT_DIR}")

    for i in range(0, total, BATCH_SIZE):
        batch_urls = ALL_URLS[i : i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
        log.info(f"Batch {batch_num}/{total_batches}: {len(batch_urls)} URLs")

        results = crawl_batch(batch_urls)

        # Build index map: url → 1-based position in ALL_URLS
        url_to_index = {url: idx + 1 for idx, url in enumerate(ALL_URLS)}

        for result in results:
            url = result.get("url", "")
            success = result.get("success", False)
            error = result.get("error_message", "")

            if not success or error:
                log.warning(f"  FAILED {url}: {error}")
                failed += 1
                continue

            md_obj = result.get("markdown") or {}
            raw_md = md_obj.get("raw_markdown", "")

            if not raw_md or len(raw_md.strip()) < 50:
                log.warning(f"  EMPTY {url}")
                empty += 1
                continue

            webpage_name = derive_webpage_name(url)
            idx = url_to_index.get(url, 0)
            filename = f"{WEBSITE_NAME}-{idx:03d}-{webpage_name}-{DATE}.md"
            filepath = OUTPUT_DIR / filename

            header = make_header(url, webpage_name, idx)
            content = header + raw_md.strip() + "\n"

            filepath.write_text(content, encoding="utf-8")
            saved += 1
            log.info(f"  Saved {filename} ({len(raw_md)} chars)")

        if i + BATCH_SIZE < total:
            time.sleep(BATCH_DELAY)

    log.info(f"Done. Saved: {saved}, Empty: {empty}, Failed: {failed}, Total: {total}")

    # Print summary file list
    saved_files = sorted(OUTPUT_DIR.glob(f"{WEBSITE_NAME}-*-2026-04-29.md"))
    log.info(f"Files in output dir: {len(saved_files)}")


if __name__ == "__main__":
    main()