---
title: "Unsupervised Learning Method for Plant and Leaf Segmentation"
source: "raw/papers/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation.pdf"
part: 1
total_parts: 4
date: "2026-05-18"
created: "2026-05-18T00:00:00Z"
section: "Abstract & Introduction"
word_count: 350
has_images: true
has_tables: false
tags: [plant-segmentation, unsupervised-learning, kmeans, expectation-maximization, leaf-segmentation, computer-vision, plant-phenotyping]
---

<!-- SEGMENT MAP
Part 1: Abstract & Introduction (this segment)
Part 2: Proposed Method (FB Segmentation + Leaf Segmentation)
Part 3: Evaluation Measures & Experimental Results
Part 4: Conclusions & References
-->

**[Part 1 of 4]** | Next: [Part 2: Proposed Method](unsupervised-learning-method-plant-leaf-segmentation-part-002-2026-05-18.md)

---

## Unsupervised Learning Method for Plant and Leaf Segmentation

Noor M. AL-Shakarji, Yasmin M. Kassim, Kannappan Palaniappan

Department of Computer Science, University of Missouri-Columbia, MO 65211, USA

Department of Computer Science, University of Technology, Baghdad, Iraq
Department of Computer Engineering, Al-Nahrain University, Baghdad, Iraq
Email: { nmahyd, ymkgz8 } @mail.missouri.edu, palaniappank@missouri.edu

**Abstract** -- Plant phenotyping is a recent application of computer vision in agriculture and food security. To automatically recognize plants species, we need first to extract the plant and associated substructures. Manual segmentation of plant structures is tedious, error prone and expensive. Automatic plant segmentation is useful for leaf extraction, identification, and counting. We have developed a robust and fast unsupervised approach for plant extraction and leaf detection. K-means based mask (of the pot) followed by Expectation Maximization (EM) algorithm is adapted to estimate a mixture model for identifying the foreground area for the plant. We utilized the EM with 3 RGB channels to identify the foreground verses background for plant localization. K-means has been used to extract the circular plant can as one of the intermediate result to fuse it with EM results for noise removal since the images suffered from contrast and illumination variations. For leaf segmentation, we utilized distance transform and watershed segmentation to localize the leaves individually followed by stem link algorithm to connect the stem with corresponding leaves. The results have been evaluated by the same algorithms that have been used in the contest of plant phenotyping [1]. In our work, we used A1 and A2 datasets to test our algorithm. We achieved promising score in some evaluation metrics and comparable in the others.

**Index Terms** -- Plant segmentation, unsupervised learning, kmean, expectation maximization, leaf segmentation

---

## I. INTRODUCTION

Studying plants phenotype is important for Biologists. The appearance and performance describe plant functions. Identifying and evaluating phenotypes will help to increase production and prevent plant diseases. Previously, biologists extract such information manually from the plants, however, image-based approaches help the experts to reduce time consuming by monitoring the digital plant images automatically. Many monitoring systems that have been developed commercially need a constant environment for image acquiring to prevent any fault identification. However, the situations with respect to varying plant environment will cause problems for image analysis, i.e. challenging may be illumination changes, camera resolution and plants with different shapes and sizes. Improvement in monitoring systems, would be helpful to identify and track plant growth. Several of computer vision approaches for monitoring system focus on plant and leaf segmentation, counting, and growth tracking, which remain challenging for plant imaging area. For segmentation, there is a rich history of papers that either use supervised, unsupervised, or semi-supervised methods [2] [3] [4] [5]. Although tracking is widely used on surveillance system [6] [7], there are also interesting papers in plant tracking, e.g [8] [9] segment and track leaves growing over time.

In this paper we used a dataset provided through the Leaf Segmentation Challenge (LSC) of the Computer Vision Problems in Plant Phenotyping (CVPPP 2014) workshop (ECCV) [1]. This data set consists of two different species of plant (Arabidopsis and Tobacco). Many authors work on this data set with different techniques. Pape et al. used unsupervised clustering and distance maps to segment leaves [10]. Nottingham leaf segmentation process [11] uses SLIC [12] superpixels-based method that does not require any training with distance map and watershed transform to extract leaves. Yin, et al. extends a multi-leaf alignment and tracking framework [13] that used in different plant data set by using advanced segmentation [11].

\* These authors contributed equally.

Dataset: http://www.plant-phenotyping.org/CVPPP2014-dataset

**Fig. 1.** (a) Input image, (b) Foreground background segmentation, (c) Leaf Detection (d) Stem linking algorithm

*[Image: Fig. 1 -- pipeline overview diagram. See original PDF for full image.]*

The rest of this paper is organized as follows: Section II describes our proposed method. Section III describes the evaluation metric that we used to evaluate our pipeline, while section IV shows the experimental results followed by conclusion.

---

**[Part 1 of 4]** | Next: [Part 2: Proposed Method](unsupervised-learning-method-plant-leaf-segmentation-part-002-2026-05-18.md)
