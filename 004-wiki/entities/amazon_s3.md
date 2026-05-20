---
title: "Amazon S3"
summary: "AWS scalable object storage service supported as a Broadcast destination for storing OpenRouter LLM trace data"
type: entity
sources:
  - raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md
tags:
  - aws
  - storage
  - s3
  - broadcast
  - observability
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Amazon S3

A scalable object storage service from AWS, supported as an [[004-wiki/concepts/broadcast|OpenRouter Broadcast]] destination for storing LLM request/response trace data. ^[001a-raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

## Key Facts

- OpenRouter Broadcast can send traces to any S3-compatible storage, including AWS S3, Cloudflare R2, MinIO, and other compatible services ^[001a-raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- AWS S3 setup requires creating a bucket, an IAM user with programmatic access, and a policy granting `s3:PutObject` on the bucket ^[001a-raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Region is auto-detected for AWS S3 but must be explicitly specified for some S3-compatible services ^[001a-raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- Trace files can be queried using Amazon Athena or Presto with `json_extract_scalar` functions on the metadata field ^[001a-raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]
- For time-based batching (hourly or daily aggregated files), AWS Kinesis Firehose is recommended as an alternative that buffers records and writes batched files to S3 ^[001a-raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/entities/cloudflare_r2]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/data_privacy]]