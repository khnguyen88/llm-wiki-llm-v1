---
title: "Openrouter Guides Features Broadcast S3"
summary: "Configuration guide for sending OpenRouter Broadcast traces to S3-compatible object storage including AWS S3, Cloudflare R2, and MinIO"
type: summary
sources:
  - raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md
tags:
  - openrouter
  - broadcast
  - s3
  - observability
  - tracing
  - cloudflare-r2
  - storage
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast S3

## Key Points

- S3/S3-Compatible is a Broadcast destination that sends traces to any S3-compatible object storage service, including AWS S3, Cloudflare R2, MinIO, and others ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Setup requires creating an S3 bucket with write credentials, enabling Broadcast in Settings > Observability, and configuring the S3 destination with bucket name, region, custom endpoint, access key, secret key, and optional session token and path template ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Each trace is saved as a separate JSON file with the format `{traceId}-{timestamp}.json` ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Path templates customize object organization using variables: `{prefix}`, `{date}`, `{year}`, `{month}`, `{day}`, `{apiKeyName}`; default is `openrouter-traces/{date}` ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Custom metadata from the `trace` field is included in the `metadata` field of each observation within the JSON trace file, with four supported keys: `trace_id`, `trace_name`, `span_name`, `generation_name` ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- When Privacy Mode is enabled, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is sent normally ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

## Quotes

- "For time-based batching (e.g., hourly or daily aggregated files), consider using AWS Kinesis Firehose instead, which buffers records and writes batched files to S3." ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

## Notes

- Cloudflare R2 requires a custom endpoint URL (e.g., `https://your-account-id.r2.cloudflarestorage.com`) and the Region field is required for some S3-compatible services ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Trace files include full input/output messages, token counts, costs, and timing data alongside custom metadata ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- S3 trace files can be queried using JSON-aware engines like Amazon Athena or Presto ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- The `user` field maps to `userId` and `session_id` maps to `sessionId` in the trace JSON ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/amazon_s3]]
- [[entities/cloudflare_r2]]
- [[concepts/broadcast]]
- [[concepts/data_privacy]]
- [[concepts/observability]]