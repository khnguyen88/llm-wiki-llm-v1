---
title: "Performance Thresholds"
summary: "OpenRouter routing parameters that deprioritize providers based on throughput and latency percentile metrics, calculated over a 5-minute rolling window"
type: concept
sources:
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
tags:
  - openrouter
  - performance
  - throughput
  - latency
  - routing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Performance Thresholds

OpenRouter routing parameters that deprioritize (not exclude) providers based on throughput and latency percentile metrics. Providers that do not meet the specified thresholds are moved to the end of the routing list rather than excluded entirely, so requests still complete even if no preferred provider qualifies. ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Key Points

- `preferred_min_throughput` sets a minimum tokens-per-second threshold; providers below it are deprioritized ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `preferred_max_latency` sets a maximum latency threshold in seconds; providers above it are deprioritized ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Both thresholds accept a single number (applies to p50) or an object with percentile cutoffs: p50, p75, p90, p99 ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Percentile metrics are calculated over a rolling 5-minute window; when multiple cutoffs are specified, all must be met for a provider to be in the preferred group ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- These thresholds do not guarantee a provider meeting the performance level; they only deprioritize underperforming providers — unlike `max_price`, which prevents execution if no provider meets the price constraint ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Details

### Percentile Semantics

- **p50** (median): 50% of requests perform better than this value
- **p75**: 75% of requests perform better than this value
- **p90**: 90% of requests perform better than this value; reflects typical worst-case performance
- **p99**: 99% of requests perform better than this value; reflects rare worst-case performance

Higher percentiles (p90, p99) give more confidence about worst-case performance, while lower percentiles (p50) reflect typical performance. ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

### Use Cases

- **Real-time applications**: Use p90 or p99 latency thresholds for consistent response times
- **Batch processing**: Use p50 throughput thresholds for average performance
- **SLA compliance**: Use multiple percentile cutoffs to enforce performance across tiers
- **Cost optimization**: Combine with `sort: "price"` to get the cheapest provider meeting performance requirements

When combined with `partition: "none"` in the `sort` object and [[concepts/model_fallback]], performance thresholds can select the cheapest or fastest endpoint across multiple models. ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/provider_routing]]
- [[concepts/model_fallback]]
- [[summaries/openrouter-guides-routing-provider-selection]]