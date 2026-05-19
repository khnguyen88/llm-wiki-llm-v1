---
title: "LLM Model Names Decoded: A Developer's Guide to Parameters, Quantization & Formats"
source: "https://blog.starmorph.com/blog/llm-model-names-decoded"
author:
  - "[[Dylan Boudro]]"
published: 2026-04-05
created: 2026-04-23
description: "A practical guide to decoding LLM model names — what B, IT, GGUF, Q4_K_M, MoE, and every other suffix means. Includes comparison tables, links to the best research resources, and real examples from Gemma 4, Qwen 3.5, and Llama 4."
tags:
  - "clippings"
---
**TL;DR:** "B" = billions of parameters. "IT" = instruction tuned. "Q4\_K\_M" = 4-bit quantization, a common default. "GGUF" = the format for Ollama and local tools. "MoE" = only a fraction of parameters activate per token. This guide decodes every component of LLM model names, explains quantization formats and file types, and points you to the best resources for researching which model fits your hardware and use case.

If you've ever stared at a Hugging Face model page and seen something like `unsloth/DeepSeek-R1-Distill-Qwen-32B-GGUF` and wondered what any of that means — this guide is for you.

The open-weight model ecosystem has exploded. Gemma 4, Qwen 3.5, Llama 4, DeepSeek, Mistral — every family ships dozens of variants across different sizes, architectures, quantization levels, and file formats. Picking the right one for your hardware and use case shouldn't require a PhD.

I wrote this as a companion to my [local LLM inference tools guide](https://blog.starmorph.com/blog/local-llm-inference-tools-guide), which covers *how to run* models. This guide explains what all those cryptic suffixes mean and points you toward the best resources for researching which model fits your setup.

- [Anatomy of a Model Name](#anatomy-of-a-model-name)
- [Parameters: What the Numbers Mean](#parameters-what-the-numbers-mean)
- [Training Variants: Base vs Instruct vs Chat](#training-variants-base-vs-instruct-vs-chat)
- [Quantization Demystified](#quantization-demystified)
- [Model Formats: GGUF vs Safetensors vs Others](#model-formats-gguf-vs-safetensors-vs-others)
- [Format Compatibility Matrix](#format-compatibility-matrix)
- [Architecture: Dense vs Mixture of Experts](#architecture-dense-vs-mixture-of-experts)
- [Community Fine-Tunes and Variants](#community-fine-tunes-and-variants)
- [The 2026 Model Landscape](#the-2026-model-landscape)
- [How to Read a Hugging Face Model Card](#how-to-read-a-hugging-face-model-card)
- [Decision Framework: Finding the Right Model](#decision-framework-finding-the-right-model)
- [Glossary](#glossary)

## Anatomy of a Model Name

Let's decode a real model name, piece by piece.

Take `bartowski/Qwen3.5-32B-Instruct-GGUF-Q4_K_M`:

| Component | Value | Meaning |
| --- | --- | --- |
| **Organization** | `bartowski` | Who published this variant (community quantizer) |
| **Family** | `Qwen3.5` | Model family and version (Alibaba's Qwen, generation 3.5) |
| **Size** | `32B` | 32 billion parameters |
| **Training** | `Instruct` | Instruction-tuned (follows prompts) |
| **Format** | `GGUF` | File format (for Ollama, LM Studio, llama.cpp) |
| **Quantization** | `Q4_K_M` | 4-bit precision, K-quant method, medium block size |

Here's another: `google/gemma-4-26B-A4B-it`

| Component | Value | Meaning |
| --- | --- | --- |
| **Organization** | `google` | Official release from Google |
| **Family** | `gemma-4` | Gemma generation 4 |
| **Size** | `26B-A4B` | 26B total params, 4B active (Mixture of Experts) |
| **Training** | `it` | Instruction tuned |

The general pattern: **\[Org/\] Family-Version-Size \[-Active\] -Training \[-Format\] \[-Quantization\]**

Not every model follows this exactly — naming is more convention than standard. But once you know the components, you can decode anything.

## Parameters: What the Numbers Mean

The "B" in model names stands for **billions of parameters** — the trainable numerical weights that a neural network learns during training. More parameters generally means more knowledge capacity, but also more memory required.

### Size Tiers

| Tier | Parameter Range | RAM Needed (Q4\_K\_M) | Best For |
| --- | --- | --- | --- |
| **Tiny** | 1-3B | 2-3 GB | Edge devices, quick tasks, mobile |
| **Small** | 4-9B | 3-6 GB | General chat, summarization, simple coding |
| **Medium** | 13-14B | 8-10 GB | Strong coding, reasoning, creative writing |
| **Large** | 27-32B | 18-22 GB | Complex reasoning, nuanced writing |
| **Extra Large** | 70B+ | 40+ GB | Near-frontier quality, research |

**The rule of thumb for Q4\_K\_M GGUF**: take the parameter count in billions, multiply by roughly 0.6, and that's your approximate file size in GB. A 7B model is ~4GB, a 32B is ~19GB, a 70B is ~40GB.

You'll also see "M" for millions — `278M` means 278 million parameters. These are tiny models for embedding, classification, or on-device use.

### Bigger Isn't Always Better

A well-trained 14B model frequently outperforms a mediocre 70B. Training data quality, architecture choices, and fine-tuning matter as much as raw parameter count. Phi-4-reasoning at 14B beats DeepSeek-R1 (671B total) on some math benchmarks. Qwen2.5-Coder at 14B scores ~85% on HumanEval, competitive with models 5x its size.

The best way to evaluate this is hands-on experimentation. Browse the [Ollama model library](https://ollama.com/library), check [Hugging Face trending models](https://huggingface.co/models?sort=trending), or explore what's popular on [OpenRouter](https://openrouter.ai/models) — then try a few models at your hardware tier and see what works for your workflow.

**Further reading:** [AI Model Parameters Explained](https://travis.media/blog/ai-model-parameters-explained/) · [LLM Model Sizes Guide](https://apxml.com/courses/getting-started-local-llms/chapter-3-finding-selecting-local-llms/model-sizes-parameters) · [Phi-4 Reasoning Technical Report](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/)

## Training Variants: Base vs Instruct vs Chat

When you see `-base`, `-instruct`, `-it`, or `-chat` in a model name, it tells you how the model was fine-tuned after initial pretraining.

### Base (Pretrained)

- Trained on massive text corpora via next-token prediction
- Completes text patterns but doesn't follow instructions reliably
- Like a student who's read every book but hasn't learned to answer exam questions
- **When to use:** Fine-tuning your own model, research, text completion

### Instruct / IT (Instruction Tuned)

- Fine-tuned on instruction-response pairs (supervised fine-tuning)
- Follows user prompts reliably: "Summarize this," "Write a function that..."
- The standard variant for most use cases
- **When to use:** Coding, Q&A, summarization, analysis — virtually everything

### Chat

- Further optimized for multi-turn conversations with RLHF or DPO
- Better at maintaining context across a conversation
- **When to use:** Chatbot applications, interactive assistants

### Other Training Suffixes

| Suffix | Meaning |
| --- | --- |
| `-DPO` | Trained with Direct Preference Optimization (alignment technique) |
| `-RLHF` | Trained with Reinforcement Learning from Human Feedback |
| `-reasoning` / `-thinking` | Optimized for chain-of-thought reasoning |
| `-vision` / `-VL` | Supports image input (vision-language) |
| `-coder` | Fine-tuned specifically for code generation |

**For general use, always pick the instruct/IT variant.** Base models are for researchers and fine-tuners. If you're running a model in Ollama or LM Studio, you want instruct.

**Further reading:** [Base vs Instruct vs Chat Models (Medium)](https://medium.com/@yashwanths_29644/llm-finetuning-series-05-llm-architectures-base-instruct-and-chat-models-a6219c39c362) · [Foundation vs Instruct vs Thinking Models](https://blog.alexewerlof.com/p/base-models-vs-instruct-models) · [Choosing the Right Model (BentoML)](https://bentoml.com/llm/getting-started/choosing-the-right-model)

## Quantization Demystified

Quantization reduces the numerical precision of model weights — storing each weight in fewer bits. This shrinks file size and speeds up inference at the cost of some accuracy.

### Precision Formats

Full-precision models store each weight as a 16-bit or 32-bit floating point number. Quantization compresses these down:

| Format | Bits per Weight | Description | Typical Use |
| --- | --- | --- | --- |
| **FP32** | 32 | Full precision, gold standard | Training reference |
| **BF16** | 16 | Brain Float 16 (same range as FP32, lower precision) | Default for LLM training |
| **FP16** | 16 | Half precision (narrower range than BF16) | GPU inference |
| **FP8** | 8 | 8-bit float | Cutting-edge training/inference |
| **INT8** | 8 | 8-bit integer, fixed-point | Post-training quantization |
| **INT4 / FP4** | 4 | 4-bit, aggressive compression | Local inference on constrained hardware |

When you see `BF16` or `FP16` in a model name, it means the weights are stored at that precision — no quantization applied. These are the highest-quality downloads but also the largest files.

### GGUF Quantization Levels

GGUF files use a naming scheme: **Q \[bits\] \_ \[method\] \_ \[size\]** — for example, Q4\_K\_M.

- **Q** = quantized
- **Number** = bits per weight (2, 3, 4, 5, 6, 8)
- **K** = K-quant method (smarter bit allocation across layers)
- **S / M / L** = Small / Medium / Large block size

| Level | Bits | Size (7B model) | Quality | Recommendation |
| --- | --- | --- | --- | --- |
| **Q2\_K** | 2 | ~2.7 GB | Poor — significant loss | Emergency only |
| **Q3\_K\_S** | 3 | ~2.9 GB | Fair — noticeable degradation | Very constrained hardware |
| **Q3\_K\_M** | 3 | ~3.1 GB | Fair | Tight budgets |
| **Q4\_K\_S** | 4 | ~3.6 GB | Good | Budget hardware |
| **Q4\_K\_M** | 4 | ~3.8 GB | Good — 92% quality retention | **The mainstream default** |
| **Q5\_K\_S** | 5 | ~4.6 GB | Very good | Between Q4 and Q6 |
| **Q5\_K\_M** | 5 | ~4.8 GB | Very good — near-imperceptible loss | When you have extra RAM |
| **Q6\_K** | 6 | ~5.5 GB | Excellent | Quality-sensitive tasks |
| **Q8\_0** | 8 | ~7 GB | Near-lossless | When VRAM isn't a concern |
| **F16** | 16 | ~14 GB | Perfect | Maximum quality baseline |

**The sweet spot for most users is Q4\_K\_M.** It's the default quantization in Ollama, retains ~92% of the original model's quality, and cuts file size by roughly 75% compared to FP16.

### What K-Quant Actually Does

K-quants use a two-level quantization scheme. Weights are grouped into 32-weight blocks, packed into 256-weight "super-blocks." Per-block scale factors are computed, then those scales are quantized *again* (double quantization). This preserves more information than naive bit reduction.

The **S/M/L** suffix controls which layers get extra precision:

- **S (Small):** All tensors at the base bit-width — smallest file
- **M (Medium):** Some attention and feed-forward tensors get higher bit-width — better quality, slightly larger
- **L (Large):** More tensors at higher bit-width — best quality, largest file

For example, Q4\_K\_M stores most tensors at 4-bit but promotes half of the attention and feed-forward weights to 6-bit.

### I-Quants (Importance Matrix)

A newer family of quantization (IQ2\_M, IQ3\_M, IQ4\_XS) uses importance matrices to identify and protect critical weights during quantization. IQ4\_XS can compress more aggressively than Q4\_K\_M with comparable quality. You'll see these from quantizers like unsloth.

### GPU-Native Quantization Methods

GGUF isn't the only game in town. If you have an NVIDIA GPU, these formats run faster:

| Format | Creator | Key Advantage | Hardware |
| --- | --- | --- | --- |
| **AWQ** | MIT / NVIDIA | Activation-aware, ~95% quality at 4-bit, fastest with Marlin kernel | NVIDIA GPU only |
| **GPTQ** | Frantar et al. | First practical LLM quantization, wide tool support | NVIDIA GPU only |
| **EXL2** | turboderp | Per-layer mixed bit-widths (2-8 bit), fastest interactive inference | NVIDIA GPU only |

These methods produce files stored as safetensors (not GGUF) and run through tools like vLLM, ExLlamaV2, or HuggingFace Transformers. They're GPU-only — no CPU fallback.

**When to use what:**

- **On CPU or mixed CPU/GPU** → GGUF (Q4\_K\_M default)
- **On NVIDIA GPU, maximum throughput** → AWQ with Marlin kernel
- **On NVIDIA GPU, maximum quality-per-byte** → EXL2

**Further reading:** [GGUF Quantization Explained (WillItRunAI)](https://willitrunai.com/blog/quantization-guide-gguf-explained) · [K-Quants and I-Quants Guide](https://kaitchup.substack.com/p/choosing-a-gguf-model-k-quants-i) · [GPTQ vs AWQ vs EXL2 vs llama.cpp](https://oobabooga.github.io/blog/posts/gptq-awq-exl2-llamacpp/) · [AWQ Paper (MLSys 2024)](https://arxiv.org/abs/2306.00978) · [Quantization Methods Compared](https://ai.rs/ai-developer/quantization-methods-compared)

## Model Formats: GGUF vs Safetensors vs Others

The file format determines which tools can load the model. This is one of the most common sources of confusion.

### GGUF

- **Created by:** Georgi Gerganov (llama.cpp project)
- **Extension:** `.gguf`
- **What it is:** A single-file format packaging weights, tokenizer, and metadata. Designed for local inference with extensive quantization support.
- **Runs on:** Ollama, LM Studio, llama.cpp, KoboldCpp
- **Pros:** Single-file portability, CPU-friendly, quantization from 2-bit to 8-bit
- **Cons:** Requires conversion from safetensors, slower than GPU-native formats on NVIDIA

### Safetensors

- **Created by:** Hugging Face
- **Extension:** `.safetensors`
- **What it is:** A secure serialization format — pure data, no executable code. Replaced PyTorch's pickle format which had arbitrary code execution vulnerabilities.
- **Runs on:** vLLM, HuggingFace Transformers, TGI, SGLang
- **Pros:** Secure, fast loading (76x faster than pickle on CPU), the standard for training/fine-tuning
- **Cons:** Full-precision models require substantial VRAM

### MLX

- **Created by:** Apple Machine Learning Research
- **Extension:** `.safetensors` (MLX-converted)
- **What it is:** Apple Silicon-native format leveraging unified memory. No data copying between CPU and GPU.
- **Runs on:** MLX framework, LM Studio (Mac), Ollama (Mac, since March 2026)
- **Pros:** Optimized for Apple Silicon, leverages all system RAM
- **Cons:** Apple Silicon only

### Others

| Format | Use Case | Note |
| --- | --- | --- |
| **ONNX** | Cross-platform/mobile/browser deployment | Not commonly used for LLMs |
| **TensorRT** | Maximum NVIDIA GPU throughput | GPU-architecture-specific, not portable |
| **PyTorch.bin** | Legacy | Being replaced by safetensors everywhere |

### The Key Insight

**GGUF is for local inference.** If you're using Ollama, LM Studio, or llama.cpp, you need GGUF (or MLX on Mac).

**Safetensors is for everything else** — GPU inference with vLLM, training, fine-tuning, and as the canonical format on HuggingFace.

You cannot fine-tune from GGUF. If you want to fine-tune, start with the safetensors version, train with LoRA/QLoRA, then convert the result to GGUF for serving.

**Further reading:** [Common AI Model Formats (HuggingFace Blog)](https://huggingface.co/blog/ngxson/common-ai-model-formats) · [What is GGUF? Complete Guide](https://ggufloader.github.io/what-is-gguf.html) · [Safetensors Security Audit](https://huggingface.co/blog/safetensors-security-audit) · [MLX GitHub](https://github.com/ml-explore/mlx) · [Ollama: Importing Models](https://docs.ollama.com/import)

## Format Compatibility Matrix

Which tools support which formats — at a glance:

| Format | Ollama | LM Studio | vLLM | llama.cpp | ExLlamaV2 | HF Transformers |
| --- | --- | --- | --- | --- | --- | --- |
| **GGUF** | ✅ | ✅ | — | ✅ | — | — |
| **Safetensors** | ✅ (auto-converts) | ✅ | ✅ | — | — | ✅ |
| **AWQ** | — | — | ✅ | — | — | ✅ |
| **GPTQ** | — | — | ✅ | — | ✅ | ✅ |
| **EXL2** | — | — | — | — | ✅ | — |
| **MLX** | ✅ (Mac) | ✅ (Mac) | — | — | — | — |

Ollama can import safetensors models via a `Modelfile` and auto-converts them to GGUF. On Apple Silicon, Ollama now uses MLX as its backend (since March 2026).

## Architecture: Dense vs Mixture of Experts

You'll see "MoE" in model descriptions and encoded in names like `35B-A3B` or `8x7B`. This is an architectural choice that fundamentally changes the size-to-performance equation.

### Dense Models

Every parameter is used for every token. A 32B dense model activates all 32 billion parameters on every input.

- **Examples:** Gemma 4 31B, Qwen3.5-27B, Llama 3.1 70B
- **Naming:** Just the parameter count — `32B`, `70B`
- **RAM required:** Proportional to total parameter count

### Mixture of Experts (MoE)

The model contains multiple "expert" sub-networks. A router selects only a few experts per token — the rest stay idle.

- **Examples:** Qwen3.5-35B-A3B (35B total, 3B active), Llama 4 Scout (109B total, 17B active)
- **Naming:** Total-B-A-Active-B format (e.g., `35B-A3B`) or described in model card
- **RAM required:** Based on *total* parameters (all experts must be in memory)
- **Compute cost:** Based on *active* parameters (only selected experts run)

| Model | Total Params | Active Params | Experts | Behavior |
| --- | --- | --- | --- | --- |
| Qwen3.5-35B-A3B | 35B | 3B | MoE | Large-model knowledge, small-model speed |
| Qwen3.5-122B-A10B | 122B | 10B | MoE | Near-frontier quality |
| Qwen3.5-397B-A17B | 397B | 17B | MoE | Frontier-class open model |
| Llama 4 Scout | 109B | 17B | 16 | 10M token context window |
| Llama 4 Maverick | 400B | 17B | 128 | Beats GPT-4o on many benchmarks |
| Gemma 4 26B-A4B | 26B | 4B | MoE | Near-31B quality at 4B compute |
| DeepSeek-V3 | 671B | 37B | MoE | Strong coding + general |
| GLM-5 | 744B | 40B | MoE | MIT licensed, trained on Huawei chips |

**The tradeoff:** An MoE model gives you the knowledge capacity of a much larger model at a fraction of the compute cost per token. But you still need enough RAM to hold all the parameters — the router needs access to every expert, even if it only activates a few at a time.

**Practical example:** Qwen3.5-35B-A3B has 35B total parameters (needs ~20GB at Q4\_K\_M) but runs at the speed of a 3B model. Compare that to a 3B dense model that needs ~2GB but has far less knowledge capacity. The MoE trades memory for intelligence.

**Further reading:** [A Visual Guide to Mixture of Experts](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts) · [MoE LLMs: Key Concepts (Neptune.ai)](https://neptune.ai/blog/mixture-of-experts-llms) · [NVIDIA MoE Blog](https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/)

## Community Fine-Tunes and Variants

Beyond official releases, a vibrant community creates derivative models. These suffixes tell you what was done:

### Common Derivative Suffixes

| Suffix | Meaning | Example |
| --- | --- | --- |
| **\-distilled / -Distill** | Smaller model trained to mimic a larger "teacher" model | `DeepSeek-R1-Distill-Qwen-32B` |
| **\-abliterated** | Safety refusal behavior surgically removed post-training | `Llama-3.2-abliterated` |
| **\-uncensored** | Trained on unfiltered data to remove guardrails | `Dolphin-Mixtral-8x7B` |
| **\-reasoning** | Optimized for chain-of-thought reasoning | `Phi-4-reasoning` |
| **\-LoRA** | Fine-tuned with Low-Rank Adaptation (adapter weights only) | Various community models |

### Key Community Contributors

| Name | Role | Known For |
| --- | --- | --- |
| **bartowski** | GGUF quantizer | Most prolific quantizer on HuggingFace — multiple quant levels for every major release |
| **unsloth** (Daniel Han) | Fine-tuning framework + quantizer | Dynamic 2.0 quantization with per-layer optimization, 2-5x faster fine-tuning |
| **Nous Research** (Teknium) | Fine-tuning lab | Hermes series — premium fine-tunes with minimal content filtering |
| **Eric Hartford** | Fine-tuner | Dolphin uncensored model family |
| **TheBloke** | GGUF/GPTQ quantizer | Pioneer of community quantization (less active since 2024, bartowski inherited the role) |
| **mlx-community** | MLX converters | Pre-converted models for Apple Silicon users |

### Distillation Explained

Distillation is a technique where a smaller "student" model is trained to replicate a larger "teacher" model's outputs. The most famous example: `DeepSeek-R1-Distill-Qwen-32B` — a Qwen 2.5 32B model fine-tuned on 800,000 chain-of-thought reasoning samples generated by DeepSeek-R1 (671B). The result outperforms OpenAI o1-mini on multiple benchmarks despite being ~20x smaller.

When you see "-Distill" in a name, it means: this model learned its skills from a bigger model, not just from raw data.

**Further reading:** [Abliteration Explained (HuggingFace Blog)](https://huggingface.co/blog/mlabonne/abliteration) · [DeepSeek-R1 Distilled Models](https://www.emergentmind.com/topics/deepseek-r1-distilled-models) · [LoRA vs QLoRA (Modal)](https://modal.com/blog/lora-qlora) · [Unsloth Dynamic 2.0 GGUFs](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) · [bartowski on HuggingFace](https://huggingface.co/bartowski)

## The 2026 Model Landscape

The open-weight ecosystem moves fast. Here's where the major families stand as of April 2026.

### Gemma 4 (Google) — Apache 2.0

Natively multimodal across all sizes. The 26B MoE achieves near-31B quality with only 4B active parameters.

| Model | Params | Architecture | Context | Modalities |
| --- | --- | --- | --- | --- |
| Gemma 4 E2B | 2.3B | Dense | 128K | Text, Image, Video, Audio |
| Gemma 4 E4B | 4.5B | Dense | 128K | Text, Image, Video, Audio |
| Gemma 4 26B-A4B | 26B total / 4B active | MoE | 256K | Text, Image, Video |
| Gemma 4 31B | 31B | Dense | 256K | Text, Image, Video |

**Best for:** Multimodal tasks at any size. The E4B is remarkable — audio, video, and image understanding at 4.5B parameters.

### Qwen 3.5 (Alibaba) — Apache 2.0

The widest size range of any model family. Features hybrid thinking/non-thinking mode and a new Gated DeltaNet architecture.

| Model | Params | Architecture | Context |
| --- | --- | --- | --- |
| Qwen3.5-0.8B | 0.8B | Dense | 262K |
| Qwen3.5-4B | 4B | Dense | 262K |
| Qwen3.5-9B | 9B | Dense | 262K |
| Qwen3.5-27B | 27B | Dense | 262K |
| Qwen3.5-35B-A3B | 35B / 3B active | MoE | 262K |
| Qwen3.5-122B-A10B | 122B / 10B active | MoE | 262K |
| Qwen3.5-397B-A17B | 397B / 17B active | MoE | 262K |

**Best for:** Versatility. 201 languages, strong coding (Qwen2.5-Coder), and the 35B-A3B MoE runs on 8GB+ VRAM with Q4\_K\_M quantization. The most popular base for community fine-tunes.

Meta's first MoE generation. Scout's 10M token context window is industry-leading.

| Model | Params | Architecture | Context |
| --- | --- | --- | --- |
| Llama 4 Scout | 109B / 17B active | MoE (16 experts) | 10M |
| Llama 4 Maverick | 400B / 17B active | MoE (128 experts) | 1M |
| Llama 4 Behemoth | ~2T / 288B active | MoE (16 experts) | TBD (preview) |

**Best for:** Long context use cases. Scout fits on a single H100 GPU with a 10-million-token window.

### Other Notable Families

| Family | Key Model | Params | Standout Feature |
| --- | --- | --- | --- |
| **DeepSeek** | R1-Distill-Qwen-32B | 32B | Best local reasoning via distillation |
| **Phi-4** (Microsoft) | Phi-4-reasoning | 14B | Beats 671B models on math benchmarks |
| **GLM-5** (Zhipu AI) | GLM-5 | 744B / 40B active | MIT license, trained without NVIDIA chips |
| **Mistral** | Mistral Large 3 | 675B / 41B active | Apache 2.0, strong multilingual |
| **Hermes 4** (Nous) | Hermes 4 405B | 405B | Minimal content filtering, strong reasoning |
| **MiniMax** | M2 | 229B / 10B active | $0.26/M input — cheapest frontier-class API |

### Trends Defining 2026

**MoE everywhere.** Almost every major release uses Mixture of Experts. The pattern: massive total parameters for knowledge, small active parameters for speed.

**Hybrid reasoning.** Models like Qwen 3.5 can toggle between fast responses and deep chain-of-thought reasoning in a single model. No separate "thinking" variant needed.

**Distillation economy.** DeepSeek-R1 proved you can get 80%+ of frontier reasoning in a 7-32B model. Everyone is distilling now.

**Context windows keep growing.** Llama 4 Scout: 10M tokens. Qwen 3.5: 262K native. Gemma 4: 256K.

The landscape changes quickly — check [LMSYS Chatbot Arena](https://huggingface.co/spaces/lmarena-ai/arena-leaderboard) for current rankings, and browse [OpenRouter](https://openrouter.ai/models) or the [Ollama library](https://ollama.com/library) to see what the community is actually using.

**Further reading:** [Gemma 4 Announcement (Google Blog)](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) · [Qwen 3.5 on GitHub](https://github.com/QwenLM/Qwen3.5) · [Llama 4 Models (Meta)](https://www.llama.com/models/llama-4/) · [DeepSeek Complete Guide (BentoML)](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond) · [GLM-5 Guide](https://www.nxcode.io/resources/news/glm-5-open-source-744b-model-complete-guide-2026) · [Hermes 4 (Nous Research)](https://hermes4.nousresearch.com/)

## How to Read a Hugging Face Model Card

Hugging Face is where most models live. Here's what to look for on a model page.

### Repository Name

Format: `organization/model-name`

- `google/gemma-4-4b-it` → Official Google release, Gemma 4, 4B params, instruction-tuned
- `bartowski/Qwen3.5-27B-GGUF` → Community GGUF quantization by bartowski
- `unsloth/DeepSeek-R1-Distill-Llama-8B` → Unsloth's optimized version

### Key Files

| File | What It Is |
| --- | --- |
| `README.md` | Model card — architecture, benchmarks, usage, license |
| `config.json` | Architecture blueprint (layers, vocab size, attention heads) |
| `model.safetensors` | The actual weights (may be sharded: `model-00001-of-00003.safetensors`) |
| `tokenizer.json` | Tokenizer definition |
| `generation_config.json` | Default generation settings (temperature, top\_p) |

1. **License** — Apache 2.0 is most permissive. Llama Community License has commercial restrictions above 700M users. Some models restrict commercial use entirely.
2. **Parameter count and architecture** — Dense or MoE? How many active parameters?
3. **Context length** — How much text can the model process at once?
4. **Quantization available** — Check if bartowski or unsloth have GGUF versions in separate repos.
5. **Benchmark scores** — Compare against similar-sized models for your use case (MMLU for general knowledge, HumanEval for coding, GSM8K for math).

### Finding the Right Variant

If the official repo is `google/gemma-4-31b-it` (safetensors, full precision), you'll find quantized versions at:

- `bartowski/gemma-4-31B-it-GGUF` — Standard GGUF quantizations
- `unsloth/gemma-4-31B-it-GGUF` — Dynamic quantization variants
- `mlx-community/gemma-4-31B-it-MLX` — Apple Silicon format

## Decision Framework: Finding the Right Model

There's no single "best model" for a given hardware setup — it depends on your task, your quality expectations, and how the model was trained, not just parameter count. The landscape changes quickly and new models regularly reshuffle the rankings. Rather than prescribing specific models, here's a framework for how to research and evaluate your options.

### Step 1: Know Your Hardware Limits

Your RAM determines the *maximum* model size you can load. This table shows approximate upper bounds at Q4\_K\_M quantization:

| Your Setup | Approximate Max Size (Q4\_K\_M) | Where to Explore |
| --- | --- | --- |
| **8GB RAM** | ~7B dense, or small MoE | [Ollama library](https://ollama.com/library) — filter by size |
| **16GB RAM / Mac** | ~14B dense | [LM Studio Discover](https://lmstudio.ai/) — browse by hardware compatibility |
| **32GB Mac** | ~32B dense | [HuggingFace Models](https://huggingface.co/models?sort=trending) — check model cards for RAM requirements |
| **64GB+ Mac** | 70B+ dense, large MoE | [OpenRouter](https://openrouter.ai/models) — try models via API before downloading |
| **NVIDIA 8-12GB VRAM** | ~9B dense | [Ollama library](https://ollama.com/library) or vLLM with AWQ |
| **NVIDIA 24GB VRAM** | ~27B dense | Community benchmarks at [LocalLLM.in](https://localllm.in/) |

These are rough guidelines — actual requirements depend on context length, batch size, and the specific model architecture. MoE models need RAM for their full parameter count even though they only activate a fraction per token.

### Step 2: Explore What the Community Is Using

The best way to find the right model is to see what others with similar hardware and use cases are running. Here are the best places to research:

- **[Ollama Model Library](https://ollama.com/library)** — Browse popular models, see download counts, and try them with one command. The tags show available sizes and quantizations.
- **[Hugging Face Trending Models](https://huggingface.co/models?sort=trending)** — See what's new and popular. Read model cards for benchmarks, hardware requirements, and community feedback.
- **[OpenRouter](https://openrouter.ai/models)** — Try models via API before committing to a local download. Great for comparing quality across families before choosing one to run locally.
- **[LM Studio](https://lmstudio.ai/)** — Visual model browser that shows hardware compatibility. Good for beginners exploring what fits their system.
- **[LMSYS Chatbot Arena](https://huggingface.co/spaces/lmarena-ai/arena-leaderboard)** — Community-voted rankings across hundreds of models. Useful for comparing quality across model families.
- **[LocalLLM.in](https://localllm.in/)** — Benchmarks specifically for local inference, organized by VRAM tier.

As of April 2026, some of the most popular open-weight model families include Qwen 3.5, Gemma 4, DeepSeek (V3 and R1 distills), GLM-5, MiniMax M2, Kimi K2.5, and Phi-4 — but this list shifts regularly as new models release. Don't take any single recommendation as definitive. Try a few models yourself and evaluate quality for your specific tasks.

### Step 3: Which Quantization?

The ladder, from minimum to maximum quality:

1. **You're very memory-constrained** → Q3\_K\_M (noticeable quality loss, but it runs)
2. **Standard recommendation** → **Q4\_K\_M** (92% quality, fits most setups)
3. **You have extra RAM** → Q5\_K\_M (near-imperceptible loss)
4. **You have plenty of RAM** → Q6\_K or Q8\_0 (effectively lossless)

**General rule: prefer a larger model at lower quantization over a smaller model at higher quantization.** A 14B at Q4\_K\_M almost always beats a 7B at Q8\_0.

### Step 4: Which Format?

| Your Tool | Format to Download |
| --- | --- |
| Ollama | GGUF (or let Ollama auto-convert) |
| LM Studio | GGUF or MLX (Mac) |
| llama.cpp | GGUF |
| vLLM | Safetensors (or AWQ for GPU quantization) |
| Fine-tuning | Safetensors (always start with full precision) |
| Apple Silicon native | MLX |

### Quick-Start: Trying Models with Ollama

The fastest way to experiment is with Ollama — one command to download and run. Here are some examples to get started, but browse the [full Ollama library](https://ollama.com/library) to see what's currently popular:

```
# Browse what's available
ollama list

# Try a small model (fits 8GB+ RAM)
ollama run gemma4:4b

# Try a medium model (fits 16GB+ RAM)
ollama run qwen3.5:9b

# Try a larger model (fits 32GB+ RAM)
ollama run qwen3.5:27b

# Specify a quantization level
ollama run qwen3.5:9b-q5_K_M

# See what Ollama downloaded
ollama list
```

The Ollama library, LM Studio's model browser, and OpenRouter's model list are all good starting points for discovering what's available. Try a few models at your hardware tier, compare the output quality for your specific use case, and see what works best for you.

## Glossary

Quick reference for every abbreviation you'll encounter in model names.

| Term | Meaning |
| --- | --- |
| **B** | Billions of parameters |
| **M** | Millions of parameters |
| **IT / Instruct** | Instruction-tuned — fine-tuned to follow prompts |
| **Base** | Pretrained only — raw text completion |
| **Chat** | Optimized for multi-turn conversation |
| **GGUF** | GPT-Generated Unified Format — single-file format for local inference |
| **Safetensors** | HuggingFace's secure tensor serialization |
| **Q4\_K\_M** | 4-bit K-quant, medium blocks — the mainstream default |
| **Q8\_0** | 8-bit quantization — near-lossless |
| **F16 / FP16** | 16-bit floating point — half precision |
| **BF16** | Brain Float 16 — default training precision |
| **AWQ** | Activation-Aware Weight Quantization — GPU-optimized 4-bit |
| **GPTQ** | GPT Quantization — early GPU quantization method |
| **EXL2** | ExLlamaV2 format — mixed bit-width GPU quantization |
| **MLX** | Apple's ML framework for Apple Silicon |
| **MoE** | Mixture of Experts — only a fraction of params active per token |
| **Dense** | All parameters active on every token |
| **LoRA** | Low-Rank Adaptation — efficient fine-tuning method |
| **QLoRA** | Quantized LoRA — fine-tuning with 4-bit base model |
| **DPO** | Direct Preference Optimization — alignment technique |
| **RLHF** | Reinforcement Learning from Human Feedback |
| **Distilled** | Trained to mimic a larger model's outputs |
| **Abliterated** | Safety refusals surgically removed |
| **VL** | Vision-Language — supports image input |
| **A\_B suffix** | Active parameters in MoE (e.g., A4B = 4B active) |
| **imatrix** | Importance matrix — used during quantization for better quality |
| **K-quant** | Mixed-precision quantization with importance-based bit allocation |
| **bpw** | Bits per weight — average precision across the model |

---

*This guide is part of a series on local AI inference. For tool comparisons and hardware recommendations, see [Local LLM Inference in 2026: The Complete Guide](https://blog.starmorph.com/blog/local-llm-inference-tools-guide). For Apple Silicon-specific advice, see [Best Mac Mini for Local LLMs](https://blog.starmorph.com/blog/best-mac-mini-for-local-llms).*

---

\> Apple Silicon LLM Inference Guide

Get the premium PDF with Apple Silicon chip comparison matrix, GGUF quantization reference card, memory budget calculators, and model name decoder with worked examples.

[\[Get the Premium Guide — $19\]](https://starmorph.com/config/apple-silicon-llm-inference-guide)

## Sources

### Research Papers

[arXivPost-Training Quantization for LLMs (2025 Survey)](https://arxiv.org/abs/2507.18553) [arXivEfficient Weight Quantization for On-Device LLMs](https://arxiv.org/abs/2503.01483) [arXivLatent Space Factorization in LoRA (2025)](https://arxiv.org/abs/2510.19640) [arXivMemory-Efficient LLM Finetuning (2025)](https://arxiv.org/abs/2511.07842) [arXivSurvey on LLM Inference Engines and Optimization](https://arxiv.org/abs/2505.01658) [arXivSpeculative Decoding: Accelerating LLM Inference (2026)](https://arxiv.org/abs/2602.12957)

### Resources

[Hugging Face Documentation](https://huggingface.co/docs) [Ollama Model Library](https://ollama.com/library) [OpenRouter Model Directory](https://openrouter.ai/models)