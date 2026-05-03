---
title: "Cloudflare R2"
summary: "Cloudflare's S3-compatible object storage service, supported as a Broadcast destination for OpenRouter LLM trace data"
type: entity
sources:
  - raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md
tags:
  - cloudflare
  - storage
  - s3-compatible
  - broadcast
  - observability
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Cloudflare R2

An S3-compatible object storage service from Cloudflare, supported as an [[concepts/broadcast|OpenRouter Broadcast]] destination alongside AWS S3 and other S3-compatible services. ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

## Key Facts

- R2 setup requires creating an R2 bucket in the Cloudflare dashboard and generating an API token with write permissions from R2 > Manage R2 API Tokens ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- R2 requires specifying a custom endpoint URL (e.g., `https://your-account-id.r2.cloudflarestorage.com`) in the S3 configuration's Custom Endpoint field ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- The Region field is required for R2 and other S3-compatible services where auto-detection is not available ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/amazon_s3]]
- [[concepts/broadcast]]