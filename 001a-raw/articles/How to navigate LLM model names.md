---
title: "How to navigate LLM model names"
source: "https://developers.redhat.com/articles/2025/04/03/how-navigate-llm-model-names"
author:
  - "[[Trevor Royer]]"
published: 2025-04-03
created: 2026-04-23
description: "Learning the naming conventions of large language models (LLMs) helps users select the right model for their needs."
tags:
  - "clippings"
---
One of the first challenges of working with large language models (LLMs) is understanding their names. This article will demystify some of the common naming conventions used by popular models. I will break down the naming conventions of LLMs, explaining how branded names, versioning, model size, and purpose play a role in their identification. Understanding these conventions helps users select the right model for their needs.

Branded names

## Branded names

Unsurprisingly, models have names that help to brand them. These names are intended to help identify a group of models produced by the same company and likely share some common architectures and training data. Like any product name, its origin varies based on the model's creators and their intended branding message—whether technical, symbolic, or purely for marketing appeal.

Here are a few examples:

- IBM's Granite model evokes rock-solid reliability, as its name suggests.
- Alternatively, some names are derived from acronyms, like Meta's Llama which stands for **L** arge **La** nguage **M** odel **M** eta **A** I.
Versions

## Versions

Along with the branded name, models generally also include a version number. Most models use a simplified semantic versioning system with major and minor version numbers, often omitting patch versions.

Major version number changes generally indicate a major change, such as an update to the underlying model architecture or training technique, updates to the training data, or perhaps even a significant change to the model performance. A major version change may indicate compatibility issues with LLM-serving tools like vLLM, potentially requiring new releases to support the new model version.

Minor version number changes generally correspond to incremental improvements to the model or a retraining on updated data.

Model size

## Model size

Most models will include some number in the model name such as "8B" or "278M" indicating parameter count in billions (B) or millions (M). Parameters (or weights) are numerical values learned during training, used in the model's calculations when generating responses.

The number of parameters directly impacts the size of the model when it is stored as a file and how much vRAM is needed to load the model onto a GPU. For example, [granite-3.2-8b-instruct](https://huggingface.co/ibm-granite/granite-3.2-8b-instruct) can reasonably fit on an A10 GPU with 24 GB of vRAM with a limited context length, while a [llama-3.1-405b-instruct](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) requires over 900 GB of vRAM and is commonly run on sixteen H100's with 80 GB of vRAM each.

Model purposes

## Model purposes

LLMs are designed for different tasks, and understanding their use cases is crucial in selecting the right model. The purpose of the model is often included directly in the name of the specific model. The following sections describe each of these model purposes.

### Base models

Base models are the generic models that act as the starting point for other more specialized models. These models are rarely used out of the box and typically serve as a foundation for fine-tuning a model for specific purposes. Some companies include "base" in the model name to make it explicit that the model is intended for fine-tuning, but others do not.

### Instruct models

Instruct models are one of the most common model types you will encounter, and if you are looking for a conversational model this is most likely what you want. Instruct models are fine-tuned to be instructed what to do and are ideal for prompt engineering and general chat use cases. Some older models will use "chat" to describe the model, but that has fallen out of favor for "instruct" in most modern models.

### Vision models

Vision models such as [granite-vision-3.2-2b](https://huggingface.co/ibm-granite/granite-vision-3.2-2b) are an emerging category of models that are becoming rapidly adopted. Vision models are generally multi-modal, meaning they can accept text and images as an input and provide text as an output. Vision models can be useful for asking questions about an image, asking the model to describe the content of an image, or even doing image-to-text conversion.

Some models are labeled as "vision-instruct," meaning that they are optimized to do both and can be a good choice if you are looking for a general chat model that can also do vision tasks.

### Code models

Code models are optimized to help with coding activities and coding assistants. Dedicated code models have fallen out of favor compared to general instruct models, and many newer instruct models will include the ability to act as a code model.

### Embedding models

Embedding is the process of converting text to a numerical token to be stored, queried, and retrieved from a vector database. Embedding models are often used in retrieval-augmented generation (RAG) alongside instruct models.

### Guard or guardian models

Guard or guardian models are designed to help identify unsafe content or questions. Guard models are often used in chat-based workflows. This is where the user's question is first sent to the guard model which attempts to determine if it is safe to proceed, and then the question is sent to the instruct model. Sometimes the guard model may also be used on the response from the LLM to ensure that the model is not responding with unacceptable content.

In the case that a guard model does detect unacceptable language, it will often respond with a simple pre-determined response stating that it can't respond to that type of question.

### Reasoning models

DeepSeek R1 recently put reasoning models on the map for the general public as it took the world and stock market by storm. Unlike traditional LLMs that simply attempt to predict the next word in the sequence, reasoning models try to work through a chain-of-thought processing, internally asking and refining questions before delivering a final response.

Model quantization

## Model quantization

Quantization is the process of converting a model weights from high precision data types such as 32-bit or 16-bit floating point numbers to lower precision types such as 8-bit floating point or integer values. By converting these data types, the size of the model can be dramatically reduced on disk, and when loaded into vRAM at the cost of a potential reduction in accuracy and quality of responses.

The Llama 405b model discussed earlier requires 900+ GB uses a fp16 data type, but converting that to fp8 drops the model to around 450 GB.

Models that have been quantized will often include terms like "fp8" or "int8" in the name indicating the data type the quantized model uses.

Some Neural Magic models will also use a naming convention such as "w4a16" which indicates that the weight parameters use 4-bit values while the activation parameters retain the original 16-bit data types. Using advanced quantization techniques, Neural Magic is able to optimize the models for different scenarios with minimal impact to accuracy and performance.

To learn more about how Neural Magic applies these techniques to Granite models, take a look at their [blog](https://developers.redhat.com/articles/2025/01/30/compressed-granite-3-1-powerful-performance-small-package). Selecting a quantized model can help to reduce the overall cost of running the model and increase the number of tokens a model server can process.

Model distillation

## Model distillation

Distillation is a technique for creating smaller, more efficient models from larger ones. It has recently gained traction, most notably with DeepSeek.

In simple terms, distillation is a technique where data scientists attempt to create a new, smaller model (a student model) using an existing larger model (the teacher model). This technique reduces the training time and produces models that are smaller and faster than their teacher models while maintaining similar accuracy and response quality.

With models such as [deepseek-r1-distill-llama-70b](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B), we can infer that this version of the model was trained using Llama 70B as the teacher model.

Mixture of experts

## Mixture of experts

Mixture of experts (MoE) is a methodology for improving inference performance speeds of models where only a portion of the model's parameters are "active" for each request. Instead of each token being processed by every single parameter in the model, an expert layer is used where each token is processed by a single "expert", and some of the common parameters shared by all models. MoE allows models to leverage the capabilities of larger models while maintaining the inference performance of smaller models.

Two common naming conventions exist for Mixture of experts.

[Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) indicates that it uses 8 experts, with 7 billion active parameters when processing a token. However, the total size of this model is 46 billion parameters (note that this model is not 56 billion parameters because some of the parameters are shared by all experts).  
  
[Llama-4-Scout-17B-16E](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E) indicates that it uses 16 experts, with 17 billion active parameters per token. Like Mixtral, Llama 4 Scout requires 109 billion parameters to load instead of 16\*17=272 due to its shared parameters between all experts.

Final thoughts

## Final thoughts

Understanding LLM model names may seem overwhelming at first, but it's easier to navigate by understanding the key naming components. Having a better understanding of models at a glance will help you pick the right model for your specific use case and hardware requirements.

As the field continues to evolve, new naming conventions will continue to emerge. With this guide, you now have a solid foundation to navigate LLM model names with confidence.

*Last updated: May 19, 2025*