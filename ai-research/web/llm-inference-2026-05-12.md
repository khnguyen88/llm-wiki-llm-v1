---
title: "LLM Inference Optimization, Infrastructure, and Scaling"
summary: "Comprehensive research on LLM inference covering optimization techniques (speculative decoding, quantization, pruning, distillation), serving infrastructure (vLLM, TensorRT-LLM, TGI, SGLang), continuous batching, GPU memory bottlenecks, context length scaling, inference-time compute, and cost optimization"
type: ai-research-multi
sources:
  - ai-research/web/llm-inference-2026-05-12.md
tags:
  - llm
  - inference
  - optimization
  - quantization
  - speculative-decoding
  - vllm
  - tensorrt-llm
  - gpu
  - batching
  - cost-optimization
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: merged
---

<!--
type: ai-research-multi
search_date: 2026-05-12T12:00:00Z
query: "LLM inference optimization techniques: speculative decoding, quantization, serving infrastructure, continuous batching, GPU memory, prefill/decode, context length scaling, inference-time compute, cost optimization"
tool_used: WebSearch
tool_model: built-in
embedding_model: N/A
sources:
  - url: https://zylos.ai/research/2026-01-11-ai-inference-optimization
    title: "AI Inference Optimization Techniques (2025-2026)"
    website: zylos.ai
    published_date: "2026-01-11"
  - url: https://zylos.ai/research/2026-01-15-llm-inference-optimization
    title: "LLM Inference Optimization and Quantization 2026"
    website: zylos.ai
    published_date: "2026-01-15"
  - url: https://callsphere.ai/blog/llm-inference-optimization-quantization-speculative-decoding-2026.md
    title: "LLM Inference Optimization: Quantization, Speculative Decoding, and Beyond"
    website: callsphere.ai
    published_date: "2026-01-01"
  - url: https://arxiv.org/html/2603.01399
    title: "Quasar: Quantized Self-Speculative Acceleration for Rapid Inference via Memory-Efficient Verification"
    website: arxiv.org
    published_date: "2026-03-01"
  - url: https://www.clarifai.com/blog/model-serving-framework/
    title: "vLLM vs Triton vs TGI: Choosing the Right LLM Serving Framework"
    website: clarifai.com
    published_date: "2025-01-01"
  - url: https://turion.ai/blog/vllm-vs-tgi-vs-triton-benchmarks/
    title: "vLLM vs TGI vs Triton: LLM Inference Server Benchmarks"
    website: turion.ai
    published_date: "2025-01-01"
  - url: https://awesomeagents.ai/tools/best-open-source-llm-inference-servers-2026/
    title: "Best Open-Source LLM Inference Servers 2026"
    website: awesomeagents.ai
    published_date: "2026-01-01"
  - url: https://digiterialabs.com/ai/insights/open-source-serving-stacks-2026
    title: "Best Open-Source LLM Serving Stack in 2026? vLLM vs TGI vs TensorRT-LLM"
    website: digiterialabs.com
    published_date: "2026-01-01"
  - url: https://mljourney.com/vllm-vs-tgi-vs-triton-inference-server-choosing-the-right-llm-serving-framework/
    title: "vLLM vs TGI vs Triton Inference Server: Choosing the Right LLM Serving Framework"
    website: mljourney.com
    published_date: "2025-01-01"
  - url: https://arxiv.org/pdf/2503.08311
    title: "Mind the Memory Gap: Unveiling GPU Bottlenecks in Large-Batch LLM Inference"
    website: arxiv.org
    published_date: "2025-03-01"
  - url: https://huggingface.co/blog/tngtech/llm-performance-prefill-decode-concurrent-requests
    title: "Prefill and Decode for Concurrent Requests - Optimizing LLM Performance"
    website: huggingface.co
    published_date: "2025-01-01"
  - url: https://arxiv.org/html/2507.06608v4
    title: "Proactive Intra-GPU Disaggregation of Prefill and Decode in LLM Serving (Nexus)"
    website: arxiv.org
    published_date: "2025-07-01"
  - url: https://huggingface.co/docs/transformers/continuous_batching_architecture
    title: "Continuous batching architecture"
    website: huggingface.co
    published_date: "2025-01-01"
  - url: https://arxiv.org/html/2410.18038v2
    title: "POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference"
    website: arxiv.org
    published_date: "2024-10-01"
  - url: https://arxiv.org/pdf/2604.14853
    title: "Adaptive Test-Time Compute Allocation for LLMs"
    website: arxiv.org
    published_date: "2026-04-01"
  - url: https://arxiv.org/abs/2604.10739v1
    title: "When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling"
    website: arxiv.org
    published_date: "2026-04-01"
  - url: https://arxiv.org/abs/2602.12279v1
    title: "UniT: Unified Multimodal Chain-of-Thought Test-time Scaling"
    website: arxiv.org
    published_date: "2026-02-01"
  - url: https://arxiv.org/pdf/2505.21825
    title: "Let Me Think! A Long CoT Can Be Worth Exponentially Many Short Ones"
    website: arxiv.org
    published_date: "2025-05-01"
  - url: https://arxiv.org/pdf/2511.14772
    title: "Test-Time Scaling of LLMs: A Survey from a Subproblem Structure Perspective"
    website: arxiv.org
    published_date: "2025-11-01"
  - url: https://www.youngju.dev/blog/llm/2026-03-03-llm-context-window-extension-guide.en
    title: "Complete Guide to LLM Context Window Extension: From RoPE, ALiBi, and YaRN to Ring Attention"
    website: youngju.dev
    published_date: "2026-03-03"
  - url: https://metricgate.com/blogs/rope-vs-alibi-positional-encoding/
    title: "RoPE vs ALiBi Positional Encoding"
    website: metricgate.com
    published_date: "2025-01-01"
  - url: https://amaarora.github.io/posts/2025-09-21-rope-context-extension.html
    title: "How LLMs Scaled from 512 to 2M Context: A Technical Deep Dive"
    website: amaarora.github.io
    published_date: "2025-09-21"
  - url: https://arxiv.org/pdf/2410.06205
    title: "Round and Round We Go! (RoPE mechanistic analysis, ICLR 2025)"
    website: arxiv.org
    published_date: "2024-10-01"
  - url: https://saraswatmks.github.io/2025/12/rope-scaling-llms.html
    title: "Simple Guide to RoPE Scaling in Large Language Models"
    website: saraswatmks.github.io
    published_date: "2025-12-01"
  - url: https://www.vectorlay.com/blog/how-to-reduce-inference-costs
    title: "How to Cut LLM Inference Costs: 6 Strategies That Actually Work"
    website: vectorlay.com
    published_date: "2025-01-01"
  - url: https://iterathon.tech/blog/llm-inference-optimization-production-guide-2026
    title: "LLM Inference Optimization Production Guide 2026"
    website: iterathon.tech
    published_date: "2026-01-01"
  - url: https://www.morphllm.com/llm-inference-optimization
    title: "LLM Inference Optimization: Cut Cost and Latency at Every Layer (2026)"
    website: morphllm.com
    published_date: "2026-01-01"
  - url: https://oneuptime.com/blog/post/2026-01-30-llm-deployment-architecture/view
    title: "How to Build LLM Deployment Architecture"
    website: oneuptime.com
    published_date: "2026-01-30"
  - url: https://www.bentoml.com/blog/6-production-tested-optimization-strategies-for-high-performance-llm-inference
    title: "6 Production-Tested Optimization Strategies for High-Performance LLM Inference"
    website: bentoml.com
    published_date: "2025-01-01"
  - url: https://inferencerig.com/performance/llm-quantization-explained-gguf-awq-and-gptq-a-practical-how-to-guid/
    title: "GGUF vs AWQ vs GPTQ: LLM Quantization Explained (2026)"
    website: inferencerig.com
    published_date: "2026-01-01"
  - url: https://mljourney.com/gguf-vs-gptq-vs-awq-which-llm-format-should-you-use/
    title: "GGUF vs GPTQ vs AWQ: Which LLM Format Should You Use?"
    website: mljourney.com
    published_date: "2025-01-01"
  - url: https://blog.premai.io/llm-quantization-guide-gguf-vs-awq-vs-gptq-vs-bitsandbytes-compared-2026/
    title: "LLM Quantization Guide: GGUF vs AWQ vs GPTQ vs bitsandbytes Compared (2026)"
    website: blog.premai.io
    published_date: "2026-01-01"
  - url: https://insiderllm.com/guides/model-formats-explained-gguf-gptq-awq-exl2/
    title: "Model Formats Explained: GGUF vs GPTQ vs AWQ vs EXL2"
    website: insiderllm.com
    published_date: "2025-01-01"
  - url: https://antoniobrundo.org/knowledge/llm-quantization-guide.html
    title: "LLM Quantization: GPTQ vs AWQ vs GGUF"
    website: antoniobrundo.org
    published_date: "2025-01-01"
  - url: https://arxiv.org/html/2507.14397v1
    title: "Efficient LLM Inference: Bandwidth, Compute, Synchronization, and Capacity (LIMINAL)"
    website: arxiv.org
    published_date: "2025-07-01"
  - url: https://arxiv.org/html/2509.12993v2
    title: "HPIM: Heterogeneous Processing-In-Memory Accelerator for LLM Inference"
    website: arxiv.org
    published_date: "2025-09-01"
  - url: https://arxiv.org/abs/2502.16963
    title: "Make LLM Inference Affordable: Augmenting GPU Memory with NDP-DIMM"
    website: arxiv.org
    published_date: "2025-02-01"
  - url: https://localaimaster.com/blog/speculative-decoding-guide
    title: "Speculative Decoding Guide: EAGLE, Medusa, n-grams (2026)"
    website: localaimaster.com
    published_date: "2026-01-01"
  - url: https://arxiv.org/html/2508.08192v1
    title: "Efficient Speculative Decoding for Llama at Scale: Challenges and Solutions"
    website: arxiv.org
    published_date: "2025-08-01"
  - url: https://nvidia.github.io/TensorRT-LLM/features/speculative-decoding.html
    title: "Speculative Decoding - TensorRT LLM"
    website: nvidia.github.io
    published_date: "2025-01-01"
  - url: https://arstechnica.com/ai/2026/05/googles-gemma-4-open-ai-models-use-speculative-decoding-to-get-up-to-3x-faster/
    title: "Google's Gemma 4 open AI models use speculative decoding to get up to 3x faster"
    website: arstechnica.com
    published_date: "2026-05-01"
  - url: https://arxiv.org/abs/2604.04988v1
    title: "Prune-Quantize-Distill: An Ordered Pipeline for Efficient Neural Network Compression"
    website: arxiv.org
    published_date: "2026-04-01"
  - url: https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf
    title: "Compact Language Models via Pruning and Knowledge Distillation (MINITRON, NeurIPS 2024)"
    website: neurips.cc
    published_date: "2024-01-01"
  - url: https://arxiv.org/abs/2603.11881v1
    title: "Bielik-Minitron-7B: Structured Pruning + KD for Polish Language"
    website: arxiv.org
    published_date: "2026-03-01"
  - url: https://www.arxiv.org/pdf/2602.09130
    title: "UNICOMP: A Unified Evaluation of LLM Compression"
    website: arxiv.org
    published_date: "2026-02-01"
  - url: https://arxiv.org/abs/2603.01875v1
    title: "KDFlow: A User-Friendly and Efficient KD Framework for LLMs"
    website: arxiv.org
    published_date: "2026-03-01"
  - url: https://docs.sglang.io/advanced_features/pd_disaggregation.html
    title: "PD Disaggregation - SGLang Documentation"
    website: sglang.io
    published_date: "2025-01-01"
  - url: https://docs.sglang.io/advanced_features/hicache_design.html
    title: "HiCache System Design and Optimization - SGLang Documentation"
    website: sglang.io
    published_date: "2025-01-01"
  - url: https://enricopiovano.com/blog/vllm-internals-architecture-deep-dive
    title: "vLLM Internals: A Deep Dive into the Architecture of High-Performance LLM Inference"
    website: enricopiovano.com
    published_date: "2025-01-01"
  - url: https://github.com/vllm-project/vllm/pull/15353
    title: "Paged Attention v3 - vLLM PR"
    website: github.com
    published_date: "2025-03-01"
  - url: https://research.ibm.com/publications/mind-the-memory-gap-unveiling-gpu-bottlenecks-in-large-batch-llm-inference
    title: "Mind the Memory Gap (IBM Research)"
    website: research.ibm.com
    published_date: "2025-03-01"
-->

# LLM Inference: Optimization Techniques, Infrastructure, and Scaling

This research covers LLM inference across eight focus areas: optimization techniques, serving infrastructure, continuous batching, GPU memory bottlenecks, context length scaling, inference-time compute, cost optimization, and the prefill/decode distinction.

## 1. Speculative Decoding

Speculative decoding exploits the **memory-bandwidth bottleneck** in LLM inference. A small/fast "draft" model proposes K tokens, and the large "target" model verifies all K in a **single forward pass**. Since generating 1 token vs. 5 tokens costs roughly the same wall time (bandwidth-bound), accepted tokens are essentially "free." The output is **mathematically identical** to standard autoregressive decoding [1][5][35].

### EAGLE (Extrapolation Algorithm for Greater Language-model Efficiency)

- **EAGLE-1 (2024):** Feature-level drafting --- predicts target model hidden states (second-to-top-layer features) instead of tokens. Speedup: 2.5--3x [35].
- **EAGLE-2 (2024):** Dynamic tree attention --- builds a tree of candidate continuations instead of a linear chain, verifying all branches in one forward pass. Speedup: 3--3.5x [35].
- **EAGLE-3 (2025):** Multi-layer hidden state aggregation, pushing speedups to 3.5--4x. Available for Llama 3.1, Qwen 2.5, DeepSeek, and Llama 4 Maverick [1][35].
- **Meta's production-scale EAGLE (Aug 2025):** Tree attention optimization, multi-round speculative sampling with PyTorch-2 compilation (1.5x speedup), disaggregated prefill/decode serving, quantized draft models (INT4 FFN), and pre-computed static tree structures. Achieved **94% GPU utilization** in production [1].

### Medusa Heads

Trains K parallel prediction heads on top of the target model's features. No separate draft model needed. Simpler architecture but **lower acceptance rate (50--65%)** vs. EAGLE's 70--80%. Speedup: 1.8--2.5x. Being superseded by EAGLE-2/3 in 2026 deployments [35].

### Draft Model Speculation

Typical pairings: Llama 3.1 70B + Llama 3.2 1B (60--75% acceptance); Qwen 2.5 72B + Qwen 2.5 7B (75--82% acceptance). Requires same tokenizer and similar instruction-tuning style [35].

### N-gram / Prompt-Lookup Decoding

Zero training, zero extra VRAM. Looks up recent context tokens in prompt + generated text and copies K tokens as drafts. Acceptance: 80%+ for repetitive content, 30--60% for code, 20--40% for chat. Speedup: 1.3--2x typical, up to 3x for repetitive content. Recommended as the **first technique to try** before adding EAGLE [35].

### Multi-Token Prediction (MTP)

Built into models like DeepSeek V3, Llama-Nemotron-Ultra, and Google Gemma 4. Auxiliary heads predict 1--2 tokens beyond current position. Google Gemma 4 (May 2026) uses MTP drafters (74M params for E2B model) claiming **up to 3x speedup** on local hardware [37].

### Quasar (ICML 2026)

Novel training-free framework that uses **quantized verification** to accelerate the verification bottleneck in self-speculative decoding. Uses a W8A8 quantized model as verifier instead of full-precision, halving memory traffic while maintaining acceptance length. Orthogonal to any drafting strategy [3].

### Real Benchmarks (Single H100, Llama 3.1 70B AWQ INT4, batch=1, vLLM)

| Method | Tokens/sec | Speedup |
|---|---|---|
| Baseline (no speculation) | 28 | 1.0x |
| n-gram (K=5) | 42 | 1.5x |
| Draft: Llama 3.2 1B (K=5) | 62 | 2.2x |
| EAGLE-2 (K=5) | 84 | 3.0x |
| EAGLE-3 (K=7) | 102 | 3.6x |

Source: [35]

### Key Caveats

- **Batched serving:** Speedup drops dramatically --- 1.4--1.8x at batch=8, ~1.0x at batch=64+. Speculation is best for single-stream/interactive use cases [35].
- **Temperature matters:** Greedy = 2.5--3.5x; temp 0.6 = 1.7--2.3x; temp 1.0 no top-p = often slower [35].
- **Acceptance rate < 40%:** Speculation hurts --- lower K, switch to n-gram, or disable [35].

## 2. Quantization Methods

Quantization reduces the numerical precision of model weights, shrinking file size and speeding up inference at the cost of some accuracy [1][2][30][31][32][33][34].

### Format Comparison

| Feature | GGUF | AWQ | GPTQ |
|---|---|---|---|
| **Type** | File format + K-quant/I-quant algorithms | Quantization algorithm | Quantization algorithm |
| **Best hardware** | CPU, Apple Silicon, hybrid CPU+GPU | NVIDIA GPU (vLLM + Marlin) | NVIDIA GPU (vLLM + Marlin) |
| **CPU support** | First-class | None | None |
| **Quality (4-bit)** | ~92--95% retention; best perplexity at 4-bit | ~95%+ retention; best HumanEval at 4-bit | ~90--95% retention; weaker on code tasks |
| **Speed (vLLM, H200)** | 93 tok/s (wrong ecosystem) | 741 tok/s (with Marlin) | 712 tok/s (with Marlin) |
| **Primary toolchain** | Ollama, llama.cpp, LM Studio | vLLM, AutoAWQ, TensorRT-LLM | vLLM, GPTQModel, Transformers |
| **Calibration** | Optional (imatrix improves quality) | Required (~128--512 samples) | Required (~2,048+ samples) |
| **Quantization time** | ~15 min | 10--30 min (7B model) | 2--4 hours (7B model on A100) |

Source: [30][31][32]

### Quality Benchmarks (Qwen3-32B on H200)

| Format | Perplexity | HumanEval Pass@1 | Throughput |
|---|---|---|---|
| BF16 baseline | 6.56 | 56.1% | 461 tok/s |
| GGUF Q4_K_M | 6.74 (+2.7%) | 51.8% | 93 tok/s |
| AWQ + Marlin | 6.84 (+4.3%) | 51.8% | 741 tok/s |
| GPTQ + Marlin | 6.90 (+5.2%) | 46.3% | 712 tok/s |

Source: [30]

### Critical Insights

- **The kernel matters as much as the algorithm.** AWQ without Marlin is 10.9x slower than AWQ with Marlin. Always verify kernel support [30].
- **Don't mix ecosystems.** GGUF belongs in llama.cpp/Ollama. AWQ/GPTQ belong in vLLM. Using GGUF in vLLM yields 93 tok/s with 958ms TTFT --- catastrophically bad [30].
- **GPTQ shows a code generation gap** (~10% below AWQ/GGUF on HumanEval), likely due to calibration overfitting [30].
- **FP8 is emerging on H100/Blackwell** as the production format --- lossless quality, 33% faster than FP16, 50% VRAM savings. NVFP4 on Blackwell achieves 3.5x memory reduction vs. FP16 with <1% accuracy degradation [1][2].
- **EXL2** (ExLlamaV2) offers variable bits-per-weight and fastest single-user inference on NVIDIA GPUs, but has a smaller ecosystem [33].

### Decision Framework

| Your Setup | Best Format | Why |
|---|---|---|
| Ollama / LM Studio / Mac / CPU | **GGUF Q4_K_M** | Only format with real CPU support |
| vLLM production serving (NVIDIA) | **AWQ + Marlin** | Fastest throughput; best quality/speed ratio |
| Multi-LoRA serving (vLLM) | **GPTQ + Marlin** | Better multi-LoRA support in vLLM |
| QLoRA fine-tuning | **bitsandbytes NF4** | Only format supporting training adapters |
| Maximum quality, ample VRAM | **GGUF Q8_0 or FP8** | Near-lossless quality |

Source: [30][31][33]

## 3. Serving Infrastructure

### Framework Comparison (2026)

| Framework | Throughput Leader | Deployment Ease | Hardware Lock-in | Status (Apr 2026) |
|---|---|---|---|---|
| **vLLM** | Best balance | 5/5 (pip install) | None (NVIDIA, AMD, CPU, TPU) | Active, v0.19.0 |
| **TensorRT-LLM/Triton** | Raw throughput | 2/5 (compile step) | NVIDIA only | Active, v1.2.0 |
| **TGI** | Moderate | 4/5 (single Docker cmd) | NVIDIA, AMD, Intel | **Maintenance mode since Dec 2025** |
| **SGLang** | Prefix-heavy workloads | 4/5 | NVIDIA, AMD | Active, v0.5.10 |

Source: [5][6][7][8][9]

### Benchmark Results (8xH100, Llama 70B-class, FP8)

| Metric | TensorRT-LLM | vLLM | TGI |
|---|---|---|---|
| Throughput @ batch 128 | ~4,800 tok/s | ~3,400 tok/s | ~2,900 tok/s |
| TTFT p50 (2K prompt) | ~82 ms | ~105 ms | ~118 ms |
| Inter-token latency p50 | ~11 ms | ~14 ms | ~16 ms |
| GPU memory utilization | 92% | 88% | 85% |
| Max concurrent requests | 512 | 1024 | 256 |

Source: [6]

### vLLM --- The Reliable Default

- **PagedAttention**: Virtual memory-style KV cache management reducing fragmentation from 60--80% to <4% [1][41].
- **Continuous batching**: Iteration-level scheduling eliminates head-of-line blocking [1][41].
- **2026 additions**: Disaggregated prefill/decode, speculative decoding, LoRA hot-swapping, Triton-based attention backend for multi-vendor GPU support [5].
- **Quantization**: FP8, INT4, INT8, GPTQ, AWQ, GGUF --- broadest support [5].
- **Model support**: 200+ architectures including MoE and multimodal [5].
- **V1 engine** (default from v0.8.0): Unified chunked-prefill paradigm replacing the separate prefill/decode paths. PagedAttention custom kernels replaced by FlashAttention 2/3 backends. FlashAttention 3 provides ~11% throughput improvement on V1 [42][43].
- **Weakness**: Slight compute overhead from block table lookups (10--20%); long prompts slower than TGI v3 [5].

### TensorRT-LLM + Triton --- Maximum Performance

- **Ahead-of-time compilation**: Model to optimized engine (15--45 min per model); must recompile for any config change [5].
- **In-flight batching**: NVIDIA's term for continuous batching, plus enterprise-grade KV cache controls [5].
- **FP8 native compute**: Performs attention directly in FP8 on Hopper/Blackwell (vLLM dequantizes back to FP16) [5].
- **Priority eviction and KV event API**: Enables KV-aware load balancing and fine-grained cache control [5].
- **Weakness**: NVIDIA lock-in; complex build pipeline; ~28 min compilation per model; high operational burden [5].

### SGLang --- The Emerging Challenger

- **RadixAttention**: Radix tree-based prefix caching achieving **85--95% hit rates** on few-shot workloads (vs. 15--25% for vLLM's prefix caching) [5].
- **~29% faster than vLLM** on shared-prefix workloads (RAG, multi-turn chat) [5].
- **HiCache**: Hierarchical GPU -> CPU -> Distributed KV caching with configurable prefetch and write-back policies [39].
- **PD Disaggregation**: Separate prefill and decode instances connected via high-speed KV cache transfer (Mooncake, NIXL, ASCEND backends) [38].
- **HybridRadixTree**: Unified cache for Full/Mamba/SWA attention types (merged April 2026) [40].
- **xGrammar**: Up to 10x faster JSON structured output decoding [5].
- **Weakness**: Fewer supported architectures than vLLM [5].

### TGI v3 --- Maintenance Mode

- **13x faster on long prompts** (>200K tokens) via conversation caching [5].
- **3x larger token capacity** on constrained hardware [5].
- **Rust core**: Lower per-request latency overhead [5].
- **CRITICAL**: Entered maintenance mode December 11, 2025 --- no new features, only bug fixes [5].

### Decision Framework

| Your Situation | Recommendation |
|---|---|
| Default/new deployment | **vLLM** --- broadest model support, easiest ops |
| RAG / multi-turn agents / structured output | **SGLang** --- RadixAttention compounds savings on prefix-heavy workloads |
| Single model at massive scale on H100/B200 | **TensorRT-LLM/Triton** --- best raw throughput if you can amortize compilation |
| Multi-model serving (LLM + vision + embeddings) | **Triton** --- ensemble pipelines serve heterogeneous models together |
| Multi-tenant SaaS with per-customer LoRA | **vLLM** --- only option with sub-millisecond LoRA hot-swap |
| CPU-only / air-gapped / dev workstation | **llama.cpp / Ollama** --- not for production scale |

Source: [5][6][7][8][9]

## 4. Continuous Batching and the Prefill/Decode Distinction

### Prefill vs. Decode: Different Bottlenecks

- **Prefill phase**: Compute-intensive (parallel processing of all prompt tokens). A single long prompt can saturate GPU compute [11][13].
- **Decode phase**: Memory-bandwidth-bound (sequential token generation). Throughput increases nearly linearly with batch size at low concurrency until GPU compute saturates [11].
- **Mixed prefill-decode batches** average **250ms per iteration** vs. **15ms for decode-only** batches --- a ~17x slowdown [12].
- **Decode kernel latency increases up to 10x** when co-scheduled with prefill [12].

### Continuous Batching Architecture

- **Request lifecycle**: PENDING -> PREFILLING -> DECODING -> FINISHED [13].
- **Chunked prefill**: Splits long prompts across multiple steps, interleaving with ongoing decode tokens. Prevents a single long prefill from blocking all decode requests. Provides **+50% throughput improvement** in standard vLLM deployments but introduces a tunable tradeoff between TTFT and TBT via chunk size [11][13].
- **CUDA graphs**: Eliminate CPU overhead by recording and replaying execution sequences; new batch shapes cached in an LRU [13].
- **Async batching**: Overlaps CPU preparation of batch N+1 with GPU computation of batch N, requiring ~2x VRAM [13].
- **Soft reset** when KV cache fills: evicts the oldest request, appends its generated tokens to its prompt, and re-queues it [13].
- Continuous batching delivers **up to 23x throughput improvement** over static batching [1].

### Disaggregated Prefill/Decode

SGLang and others now support **separate prefill and decode instances** connected via high-speed KV cache transfer (RDMA-based Mooncake, NIXL backends). This solves two problems: (1) prefill interruption of ongoing decode batches, and (2) DP attention imbalance across workers [38].

The **Nexus** system (arxiv 2507.06608) proposes **intra-GPU disaggregation** with dynamic SM partitioning:
- Up to **2.2x higher throughput**, **20x lower TTFT**, and **2.5x lower TBT** vs. vLLM
- Matches or exceeds disaggregated vLLM using **half the GPU resources** [12].

### POD-Attention (ASPLOS 2025)

First GPU kernel that efficiently computes attention for hybrid batches by running prefill and decode operations **concurrently on the same SM**:
- SM-aware CTA scheduling ensures prefill and decode CTAs are co-located, maximizing both compute and memory bandwidth utilization simultaneously [14].
- Up to **59% speedup** in attention computation (mean 28%), **up to 22% throughput improvement** [14].

## 5. GPU Memory Hierarchy and Hardware Considerations

### The Memory Wall: DRAM Bandwidth Is the True Bottleneck

Research from NVIDIA (LIMINAL, arxiv 2507.14397) and BSC/IBM (Mind the Memory Gap, arxiv 2503.08311) establishes that **LLM inference remains memory-bound even at large batch sizes** [10][15]:

- The attention kernel's arithmetic intensity remains **nearly constant** as batch size increases (~0.5--1 FLOPS/byte), unlike matmul kernels whose arithmetic intensity scales with batching [10].
- Over **50% of attention kernel cycles are stalled** due to data access delays (DRAM bandwidth saturation) at maximum batch sizes [10].
- GPU compute utilization remains **under 35%** even at maximum batch size [10].
- L1 and L2 cache hit rates drop dramatically with increasing batch size (L1 from ~16% at batch=1 to ~2% at max batch) [10].

### Hardware Configurations Analyzed (LIMINAL)

| Config | Memory BW (TB/s) | Compute (PFLOPS/s) | Capacity | Notes |
|---|---|---|---|---|
| xPU-HBM3 | 4 | 2.25 | 96 GB | Based on Blackwell GPU (HBM3e) |
| xPU-HBM4 | 18 | 2.25 | 192 GB | HBM4 |
| xPU-3D-DRAM | 30 | 2.25 | 36 GB | Advanced 3D-stacked DRAM |
| xPU-SRAM | 117 | 1.13 | 512 MB | Serve from SRAM |
| xPU-COWS | 2250 | 28.13 | 11 GB | Collectives-optimized wafer-scale |

Source: [15]

### Key Performance Data (Llama3-405B, batch=1)

| System | 4K context UTPS | 128K context UTPS |
|---|---|---|
| xPU-HBM3-TP8 | 86 | 80 |
| xPU-HBM3-TP32 | 290 | 271 |
| xPU-HBM3-TP128 | 776 | 743 |

Source: [15]

### Critical Insights

- **No HBM3-based hardware can reach 1,000 TPS** on large models (Llama-405B, DeepSeek V3) at large context [15].
- Beyond ~4x HBM3 bandwidth, **synchronization latency** becomes the first-order bottleneck [15].
- **SRAM-only designs become 10x less cost-effective** at low throughput due to lack of "elasticity" [15].
- **3D-DRAM and HBM4** are the most promising near-term paths, providing both bandwidth and capacity improvements [15].

### Batching Configuration Advisor (BCA)

The BCA approach identifies an **optimal batch size (B_opt)** based on throughput plateaus and latency SLOs, freeing GPU memory for **model replication** (running multiple model instances concurrently). This improved throughput by **33.7% for OPT-1.3B** and **7.5% for OPT-2.7B** [10].

### Near-Data Processing Alternatives

- **Hermes** (arxiv 2502.16963): Uses NDP-DIMMs to augment consumer GPUs. Exploits activation sparsity (20% "hot" neurons handle 80% of compute). Deploys LLaMA2-70B on consumer hardware at 13.75 tokens/s with **75.24x average speedup** over offloading-based systems [16].
- **HPIM** (arxiv 2509.12993): Heterogeneous Processing-In-Memory integrating SRAM-PIM (attention) and HBM-PIM (GEMV). Achieves **34.3x speedup** vs. A100 GPU [17].

### Multi-GPU Serving

- **Tensor parallelism** splits model layers across GPUs (single vLLM flag) [25].
- **Pipeline parallelism** stages layers across GPUs with batch queuing to hide pipeline bubble latency [41].
- Running Llama 70B on 2x RTX 4090 vs. single A100 80GB on AWS: **$706/mo vs. $3,604/mo** (80% savings) [25].

## 6. Context Length Scaling Techniques

### Rotary Position Encoding (RoPE)

RoPE encodes absolute position via rotation matrices; the dot product depends only on relative offset (m-n). Used by LLaMA, Mistral, Qwen, DeepSeek, Gemma [19][20].

**Key insight from ICLR 2025 paper (Barbero et al.):** RoPE does NOT simply decay attention with distance --- this common claim is false for realistic (Gaussian) queries/keys. **High frequencies** construct positional attention heads (diagonal, previous-token patterns) --- provably impossible without RoPE. **Low frequencies** serve as semantic information channels that degrade over long contexts. The **p-RoPE** proposal removes the lowest frequencies to create robust semantic channels, improving perplexity over standard RoPE on Gemma 2B [21][22].

### RoPE Scaling Methods

| Method | Max Scale | Notes |
|---|---|---|
| Linear (PI) | 2--4x | Degrades quickly beyond 4x |
| NTK-Aware | 4--8x | Better high-freq preservation |
| Dynamic NTK | 8--16x | Adaptive but inconsistent |
| YaRN | 16--32x | Best for extreme extension; used by Qwen, DeepSeek, LLaMA 3 |
| Fine-tuning | 64x+ | Optimal but expensive |

Source: [19][21][22]

**YaRN** combines NTK-by-Parts + attention temperature scaling (softmax temperature sqrt(s)). Extends 32x with only 0.1% training data [19].

### ALiBi (Attention with Linear Biases)

Adds per-head linear bias proportional to distance. Enables zero-shot length extrapolation but has a **strong locality/recency bias** that hurts tasks requiring long-range dependencies (code, theorem proving, retrieval) [19][20].

### Sliding Window Attention (SWA)

Limits attention to a fixed window of recent tokens. Reduces memory from O(n^2) to O(n*w) where w is window size. Mistral uses SWA with a 4096-token window. SGLang's HybridRadixTree now supports SWA component for hybrid cache management [19][40].

### Ring Attention

Distributes sequences across GPUs for hardware-level context extension. Used by Gemini for 2M token contexts. Enables processing sequences longer than single-GPU memory capacity by passing KV blocks across devices [19].

### LLaMA 3's Approach

Increasing the base wavelength from 10K to 500K effectively provides more "slow enough" frequencies for long contexts. This is equivalent to YaRN-style scaling applied at training time [21].

## 7. Inference-Time Compute (Test-Time Compute Scaling)

### Sequential vs. Parallel Scaling

- **Parallel scaling** (best-of-N, majority voting): More samples of the same problem. Subject to diminishing returns and exponential cost [23][24].
- **Sequential scaling** (longer chain-of-thought): Extends reasoning depth. Can be **exponentially more powerful** than parallel scaling --- polynomial-length CoT enables computation provably impossible with polynomially many O(1)-length CoTs (under complexity assumption TC^0 != L) [23].

### The Overthinking Problem (arxiv 2604.10739)

Extended reasoning can **degrade accuracy**:
- Marginal utility drops from +3.2%/500 tokens (0.5--2K) to **-0.3%/500 tokens** (12--16K) on AIME [24].
- **Flip ratio exceeds 1.0 at ~7K tokens**, meaning negative flips (correct -> incorrect) dominate beyond this point [24].
- Early stopping at moderate budgets (~6K tokens) can reduce computation by ~50% with only ~6% accuracy loss [24].
- Overthinking indicators (hesitation markers, answer oscillation, confidence drops) achieve **76.3% precision at 80% recall** for predicting negative flips [24].

### Adaptive Compute Allocation (arxiv 2604.14853)

Formalizes input-adaptive test-time compute as a constrained optimization problem:
- Not all inputs deserve the same inference compute. Some problems are easy, some are "responsive" (more compute helps), some are intractable (more compute is wasted) [25].
- **Inverted-U allocation pattern**: Easy and hard problems receive minimal compute, while medium-difficulty ("responsive") problems receive the most [25].
- Up to **12.8% relative accuracy improvement** on MATH under matched budget constraints over uniform allocation [25].

### Practical Implications for 2026

1. **Adaptive compute allocation** is replacing uniform allocation --- easy problems get fewer resources, responsive problems get more [25].
2. **Cost-aware evaluation** should accompany accuracy metrics --- reporting Pareto frontiers of accuracy vs. compute [24][25].
3. **Overthinking detection** enables early stopping without performance loss [24].
4. **Meta-reasoning** --- learning when and how to reason --- is identified as a key open direction [27].

## 8. Cost Optimization Strategies for Production Deployments

### The Core Problem

- Inference represents **two-thirds of AI compute spending** [25].
- The LLM inference market is projected to hit **$50 billion in 2026** (47% YoY growth) [26].
- Most teams **overpay by 3--5x** due to infrastructure misconfiguration [25].
- OpenAI reduced GPT-4 pricing by **94%** between GPT-4 and GPT-4o, primarily through inference optimizations [25].

### Six Core Optimization Strategies

1. **GPU Right-Sizing**: Moving a 7B model from A100 ($3.67/hr) to RTX 4090 ($0.49/hr) saves **87%**. If GPU VRAM utilization is below 70%, you're overpaying [25].

2. **Quantization (Model-Level)**: AWQ 4-bit recommended for production (fastest 4-bit, excellent vLLM support, <1% quality loss). A 70B model drops from 140GB (FP16) to 35GB (INT4), fitting on 2x RTX 4090 instead of 2x A100 80GB [25][26].

3. **Continuous Batching (System-Level)**: The **single most impactful optimization** for throughput. Serves 5--10x more requests per GPU. vLLM's PagedAttention eliminates KV cache fragmentation. **23x throughput improvement** measured in production [1][25].

4. **Consumer GPUs for Inference**: RTX 4090 delivers **4x more FP32 TFLOPS** than A100 while costing **7x less per hour**. For models that fit in 24GB VRAM (most quantized models), there's "no rational reason" to use datacenter GPUs [25].

5. **Distributed Inference / Model Sharding**: Tensor parallelism splits model layers across GPUs (single vLLM flag). Running Llama 70B on 2x RTX 4090 vs. single A100 80GB on AWS: **$706/mo vs. $3,604/mo** (80% savings) [25].

6. **Eliminate Hidden Infrastructure Costs**: AWS adds **18--50%+** in hidden fees (egress, storage, NAT gateway, load balancer, CloudWatch) [25].

### Application-Layer Optimizations

| Technique | Savings | Effort |
|---|---|---|
| **Semantic Caching** | 3--10x for repetitive queries | Medium |
| **Prompt Caching** | 80--90% latency reduction on cached prefixes | Low |
| **Context Compression** | 50--70% token reduction | Low |
| **Model Routing** | 2--5x aggregate cost savings | Medium |
| **Speculative Decoding** | 2--5x speedup | Medium |

Source: [25][26]

### Model Routing Strategy

- Route simple queries (summarize, translate, extract) to **8B models** ($0.10--0.25/M tokens)
- Route standard queries to **70B models** ($0.88--3/M tokens)
- Route complex reasoning to **405B+ models** ($10+/M tokens)
- Typical aggregate savings: **2--5x** [26]

### Stacked Optimization Impact

Before/After case study (VectorLay):
- Before: AWS p4d.24xlarge (8x A100), FP16, no batching = **$23,510/month ($282K/year)**
- After: 2x RTX 4090, AWQ INT4, vLLM batching = **$706/month ($8,472/year)**
- **97% cost reduction** with same model quality and throughput [25]

### Key Metrics to Track

| Metric | Why It Matters |
|---|---|
| **Tokens per task** (not per request) | Maps directly to cost |
| **Time to First Token (TTFT)** | Dominated by prefill; improved by caching |
| **Tokens per second** | Decode throughput under realistic concurrency |
| **Cost per task** | The bottom-line metric |
| **GPU memory utilization** | Below 70% = overpaying |
| **Cache hit rate** | Target 50--70% for mature apps |

Source: [26]

## 9. Pruning and Distillation

### Structured Pruning + Knowledge Distillation (MINITRON)

NVIDIA's MINITRON (NeurIPS 2024) establishes best practices:
1. Train largest model, then prune+distill iteratively
2. Width pruning > depth pruning after retraining
3. Use distillation (KLD) exclusively for retraining
4. Logit-only distillation sufficient when depth isn't reduced much
- Compressed Nemotron-4 15B to MINITRON 8B and 4B using **40x fewer training tokens** than training from scratch
- MINITRON 8B achieves up to 16% improvement in MMLU over training from scratch [29]

### UNICOMP Benchmark (arxiv 2602.09130, Feb 2026)

Comprehensive evaluation of pruning, quantization, and KD across 40+ datasets:
- **Knowledge bias**: Knowledge tasks are relatively preserved; reasoning, multilingual, and instruction-following degrade substantially
- **Quantization provides the best overall trade-off** between retained performance and efficiency
- **Distillation yields strong runtime acceleration** but at very high computational cost
- **Semi-structured 2:4 pruning** is not competitive despite hardware support
- **Low-Rank Clone** (soft pruning + distillation) outperforms hard-structured pruning approaches [28]

### Ordered Pipeline: Prune -> Quantize -> Distill (arxiv 2604.04988)

Key finding: **Stage ordering matters**. Pruning acts as a capacity-reduction pre-conditioner that stabilizes subsequent quantization. QAT provides the dominant latency benefit. KD applied last recovers accuracy in the sparse INT8 regime. Proxy metrics (parameter count, FLOPs) don't reliably predict wall-clock inference time [28].

### KDFlow (arxiv 2603.01875)

Novel KD framework with decoupled architecture: FSDP2 for student training + SGLang for teacher inference. Transmits hidden states (not full logits) via zero-copy transfer. Achieves **1.44x to 6.36x speedup** over existing KD frameworks. Supports both off-policy and on-policy distillation and cross-tokenizer KD [34].

## Sources

1. [AI Inference Optimization Techniques (2025-2026) | Zylos Research](https://zylos.ai/research/2026-01-11-ai-inference-optimization)
2. [LLM Inference Optimization and Quantization 2026 | Zylos Research](https://zylos.ai/research/2026-01-15-llm-inference-optimization)
3. [Quasar: Quantized Self-Speculative Acceleration for Rapid Inference via Memory-Efficient Verification](https://arxiv.org/html/2603.01399)
4. [LLM Inference Optimization: Quantization, Speculative Decoding, and Beyond](https://callsphere.ai/blog/llm-inference-optimization-quantization-speculative-decoding-2026.md)
5. [Best Open-Source LLM Serving Stack in 2026? vLLM vs TGI vs TensorRT-LLM](https://digiterialabs.com/ai/insights/open-source-serving-stacks-2026)
6. [vLLM vs TGI vs Triton: LLM Inference Server Benchmarks | TURION.AI](https://turion.ai/blog/vllm-vs-tgi-vs-triton-benchmarks/)
7. [Best Open-Source LLM Inference Servers 2026](https://awesomeagents.ai/tools/best-open-source-llm-inference-servers-2026/)
8. [vLLM vs Triton vs TGI: Choosing the Right LLM Serving Framework | Clarifai](https://www.clarifai.com/blog/model-serving-framework/)
9. [vLLM vs TGI vs Triton Inference Server: Choosing the Right LLM Serving Framework | ML Journey](https://mljourney.com/vllm-vs-tgi-vs-triton-inference-server-choosing-the-right-llm-serving-framework/)
10. [Mind the Memory Gap: Unveiling GPU Bottlenecks in Large-Batch LLM Inference](https://arxiv.org/pdf/2503.08311)
11. [Prefill and Decode for Concurrent Requests - Optimizing LLM Performance | HuggingFace](https://huggingface.co/blog/tngtech/llm-performance-prefill-decode-concurrent-requests)
12. [Proactive Intra-GPU Disaggregation of Prefill and Decode in LLM Serving (Nexus)](https://arxiv.org/html/2507.06608v4)
13. [Continuous batching architecture | HuggingFace](https://huggingface.co/docs/transformers/continuous_batching_architecture)
14. [POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference](https://arxiv.org/html/2410.18038v2)
15. [Efficient LLM Inference: Bandwidth, Compute, Synchronization, and Capacity (LIMINAL)](https://arxiv.org/html/2507.14397v1)
16. [Make LLM Inference Affordable: Augmenting GPU Memory with NDP-DIMM](https://arxiv.org/abs/2502.16963)
17. [HPIM: Heterogeneous Processing-In-Memory Accelerator for LLM Inference](https://arxiv.org/html/2509.12993v2)
18. [Adaptive Test-Time Compute Allocation for LLMs](https://arxiv.org/pdf/2604.14853)
19. [Complete Guide to LLM Context Window Extension: From RoPE, ALiBi, and YaRN to Ring Attention](https://www.youngju.dev/blog/llm/2026-03-03-llm-context-window-extension-guide.en)
20. [RoPE vs ALiBi Positional Encoding | MetricGate](https://metricgate.com/blogs/rope-vs-alibi-positional-encoding/)
21. [How LLMs Scaled from 512 to 2M Context: A Technical Deep Dive](https://amaarora.github.io/posts/2025-09-21-rope-context-extension.html)
22. [Round and Round We Go! (RoPE mechanistic analysis, ICLR 2025)](https://arxiv.org/pdf/2410.06205)
23. [Let Me Think! A Long CoT Can Be Worth Exponentially Many Short Ones](https://arxiv.org/pdf/2505.21825)
24. [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](https://arxiv.org/abs/2604.10739v1)
25. [How to Cut LLM Inference Costs: 6 Strategies That Actually Work | VectorLay](https://www.vectorlay.com/blog/how-to-reduce-inference-costs)
26. [LLM Inference Optimization Production Guide 2026 | Iterathon](https://iterathon.tech/blog/llm-inference-optimization-production-guide-2026)
27. [Test-Time Scaling of LLMs: A Survey from a Subproblem Structure Perspective](https://arxiv.org/pdf/2511.14772)
28. [UNICOMP: A Unified Evaluation of LLM Compression](https://www.arxiv.org/pdf/2602.09130)
29. [Compact Language Models via Pruning and Knowledge Distillation (MINITRON, NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
30. [GGUF vs AWQ vs GPTQ: LLM Quantization Explained (2026)](https://inferencerig.com/performance/llm-quantization-explained-gguf-awq-and-gptq-a-practical-how-to-guid/)
31. [GGUF vs GPTQ vs AWQ: Which LLM Format Should You Use? | ML Journey](https://mljourney.com/gguf-vs-gptq-vs-awq-which-llm-format-should-you-use/)
32. [LLM Quantization Guide: GGUF vs AWQ vs GPTQ vs bitsandbytes Compared (2026)](https://blog.premai.io/llm-quantization-guide-gguf-vs-awq-vs-gptq-vs-bitsandbytes-compared-2026/)
33. [Model Formats Explained: GGUF vs GPTQ vs AWQ vs EXL2 | InsiderLLM](https://insiderllm.com/guides/model-formats-explained-gguf-gptq-awq-exl2/)
34. [KDFlow: A User-Friendly and Efficient KD Framework for LLMs](https://arxiv.org/abs/2603.01875v1)
35. [Speculative Decoding Guide: EAGLE, Medusa, n-grams (2026)](https://localaimaster.com/blog/speculative-decoding-guide)
36. [Efficient Speculative Decoding for Llama at Scale: Challenges and Solutions](https://arxiv.org/html/2508.08192v1)
37. [Google's Gemma 4 open AI models use speculative decoding to get up to 3x faster](https://arstechnica.com/ai/2026/05/googles-gemma-4-open-ai-models-use-speculative-decoding-to-get-up-to-3x-faster/)
38. [PD Disaggregation - SGLang Documentation](https://docs.sglang.io/advanced_features/pd_disaggregation.html)
39. [HiCache System Design and Optimization - SGLang Documentation](https://docs.sglang.io/advanced_features/hicache_design.html)
40. [HybridRadixTree: Support Unified HybridRadixTree V2 (SGLang PR #21206)](https://github.com/sgl-project/sglang/pull/21206)
41. [vLLM Internals: A Deep Dive into the Architecture of High-Performance LLM Inference](https://enricopiovano.com/blog/vllm-internals-architecture-deep-dive)
42. [Flash Attention 3 Support - vLLM PR #12093](https://github.com/vllm-project/vllm/pull/12093)
43. [Paged Attention v3 - vLLM PR #15353](https://github.com/vllm-project/vllm/pull/15353)
44. [LLM Inference Optimization: Cut Cost and Latency at Every Layer (2026) | Morph](https://www.morphllm.com/llm-inference-optimization)
45. [How to Build LLM Deployment Architecture](https://oneuptime.com/blog/post/2026-01-30-llm-deployment-architecture/view)
46. [6 Production-Tested Optimization Strategies for High-Performance LLM Inference](https://www.bentoml.com/blog/6-production-tested-optimization-strategies-for-high-performance-llm-inference)
47. [Simple Guide to RoPE Scaling in Large Language Models](https://saraswatmks.github.io/2025/12/rope-scaling-llms.html)
48. [Bielik-Minitron-7B: Structured Pruning + KD for Polish Language](https://arxiv.org/abs/2603.11881v1)
49. [UniT: Unified Multimodal Chain-of-Thought Test-time Scaling](https://arxiv.org/abs/2602.12279v1)
50. [Prune-Quantize-Distill: An Ordered Pipeline for Efficient Neural Network Compression](https://arxiv.org/abs/2604.04988v1)
51. [Speculative Decoding - TensorRT LLM](https://nvidia.github.io/TensorRT-LLM/features/speculative-decoding.html)
52. [LLM Quantization: GPTQ vs AWQ vs GGUF](https://antoniobrundo.org/knowledge/llm-quantization-guide.html)
53. [Mind the Memory Gap (IBM Research)](https://research.ibm.com/publications/mind-the-memory-gap-unveiling-gpu-bottlenecks-in-large-batch-llm-inference)