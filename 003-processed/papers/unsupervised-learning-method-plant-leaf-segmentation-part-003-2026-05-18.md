---
title: "Unsupervised Learning Method for Plant and Leaf Segmentation"
source: "raw/papers/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation.pdf"
part: 3
total_parts: 4
date: "2026-05-18"
created: "2026-05-18T00:00:00Z"
section: "Evaluation Measures & Experimental Results"
word_count: 350
has_images: true
has_tables: true
tags: [plant-segmentation, evaluation-metrics, dice-score, benchmark-results, plant-phenotyping, CVPPP, LSC]
---

**[Part 3 of 4]** | Previous: [Part 2: Proposed Method](unsupervised-learning-method-plant-leaf-segmentation-part-002-2026-05-18.md) | Next: [Part 4: Conclusions & References](unsupervised-learning-method-plant-leaf-segmentation-part-004-2026-05-18.md)

---

## III. EVALUATION MEASURES

For our pipeline we adopted evaluation metrics that used in the LSC challenge [1]. LSC depended on four important metrics that also used in multi object segmentation. These metrics based on Dice score for binary segmentation that measures how much overlap between ground truth and algorithm result of the binary segmentation masks. The four metrics used in our pipeline are:

**Fig. 4.** Leaf Detection (LD) steps

*[Image: Fig. 4 -- leaf detection pipeline. See original PDF for full image.]*

- **Symmetric Best Dice (SBD):** used to calculate the segmentation accuracy (average Dice) among all objects (leaves). Best Dice (BD) is defined as equation (4).

*[Formula 4 -- original formula not decoded. See PDF.]*

where | . | represents number of pixels. L_a_i and L_b_i are sets of segmented leaf belong to L_a and L_b respectively. SBD between L_gt and L_ar is defined as equation (5).

*[Formula 5 -- original formula not decoded. See PDF.]*

- **Foreground-Background Dice (FBD):** represents the Dice score of the foreground mask with respect to the ground truth.
- **Difference in Count (DiC):** the difference between the leaves in pipeline result and the ground truth (see equation (6)).

*[Formula 6 -- original formula not decoded. See PDF.]*

- **|DiC|:** which is the absolute value of DiC.

---

## IV. EXPERIMENTAL RESULTS

In this section, we discuss the evaluation of our method according to the same metric functions that have been used in the contest. We compare our results with the methods participated in the challenge as described on [11]. Our method has promising results on all the metrics, we got better values in term of SBD and comparable with the other state-of-art results as shown in table I for set A1 data set, and table II that shows our results for A2 dataset. See figure 5 which shows some of our final algorithmic results. Although A1 is very different from A2, the same parameters are used. One image for training is enough to train the parameters. In testing phase, the learned parameters are used to test all the other images in the datasets.

### Table I: Quantitative Comparison for A1 Data Set

| Method     | SBD  | FBD  | |DiC| | DiC  |
|------------|------|------|-------|------|
| IPK        | 74.4 | 97.0 | 2.2   | -1.8 |
| Nottingham | 68.3 | 95.3 | 3.8   | -3.5 |
| MSU        | 66.7 | 94.0 | 2.5   | -2.5 |
| Wageningen | 71.1 | 94.7 | 2.2   | 1.3  |
| **Ours**   | **74.6** | **94.9** | **2.9**   | **-1.4** |

### Table II: Quantitative Comparison for A2 Data Set

| Method     | SBD  | FBD  | |DiC| | DiC  |
|------------|------|------|-------|------|
| IPK        | 76.9 | 96.3 | 1.2   | -1.0 |
| Nottingham | 71.3 | 93.0 | 1.9   | -1.9 |
| MSU        | 66.6 | 87.7 | 2.0   | -2.0 |
| Wageningen | 75.7 | 95.1 | 0.4   | -0.2 |
| **Ours**   | **72.1** | **94.8** | **1.3**   | **-0.8** |

Our method achieves the highest SBD (74.6) on the A1 dataset and competitive results on A2. The method is fully unsupervised and requires only one training image to learn parameters that generalize across the entire dataset.

**Fig. 5.** (a) Input images (selected from A1 group), (b) Ground-truth, (c) Foreground background segmentation using EM and K-means algorithms, (d) Leaf detection using watershed and morphological operations.

*[Image: Fig. 5 -- qualitative results. See original PDF for full image.]*

---

**[Part 3 of 4]** | Previous: [Part 2: Proposed Method](unsupervised-learning-method-plant-leaf-segmentation-part-002-2026-05-18.md) | Next: [Part 4: Conclusions & References](unsupervised-learning-method-plant-leaf-segmentation-part-004-2026-05-18.md)
