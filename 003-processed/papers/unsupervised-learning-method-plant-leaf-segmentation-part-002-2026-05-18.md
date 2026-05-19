---
title: "Unsupervised Learning Method for Plant and Leaf Segmentation"
source: "raw/papers/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation.pdf"
part: 2
total_parts: 4
date: "2026-05-18"
created: "2026-05-18T00:00:00Z"
section: "Proposed Method"
word_count: 500
has_images: true
has_tables: false
tags: [plant-segmentation, unsupervised-learning, kmeans, expectation-maximization, leaf-segmentation, watershed, distance-transform, stem-link-algorithm]
---

**[Part 2 of 4]** | Previous: [Part 1: Abstract & Introduction](unsupervised-learning-method-plant-leaf-segmentation-part-001-2026-05-18.md) | Next: [Part 3: Evaluation & Results](unsupervised-learning-method-plant-leaf-segmentation-part-003-2026-05-18.md)

---

## II. OUR PROPOSED METHOD

There are two main steps to accomplish our goal, step 1 is to segment the region as plant and non plant regions and step 2 is to extract the individual leaves from the segmented region. For the first step, there are many methods for segmentation [14][20], however, we utilized the Expectation Maximization (EM) and K-means algorithms to provide fast automated system. Extracting the plant by the EM algorithm leads to noisy result due to image noisy acquisition, e.g. intensity and illumination variations, and leaves sizes. Figure 2 shows some images with these challenges that can affect the segmentation. In addition, utilizing k-means alone is not practical since it is very easy to stuck in local optimal. Thus, EM and K-means are both utilized by fusing their results to get a pure and clear mask for foreground and background. For the second step; leaf segmentation, we followed some determined morphological stages with distance transform of local maxima and watershed segmentation approach to get the leaves isolated.

**Fig. 2.** (a) Green soil similar in color with the plant, (b) Blurred contrast, (c) Different leaf sizes

*[Image: Fig. 2 -- challenging input images. See original PDF for full image.]*

### A. Step1: Foreground background (FB) segmentation

In this section, we describe how to fuse the two methods; EM and K-means, to get our final FB segmentation masks.

**Method 1: Expectation-Maximization.** We utilized EM for the main part of the extraction since it tends to get stuck less than K-means in local optimal. The idea is to assign data points partially to different clusters instead of assigning to only one cluster. To do this partial assignment, we model each cluster using a probabilistic distribution, so there is a certain probability assigned to each data point, the final clusters assignment will depends upon the highest probability score. Mixture of Gaussian is used to represent our model which is a weighted sum of K Gaussian distributions, the summation of all the weights is 1. Let's assume theta_j as the parameter of jth distribution with w_j is the corresponding weight as described in equation (1).

*[Formula 1 -- original formula not decoded. See PDF.]*

The goal is to find parameter of the model Theta that maximize the log likelihood over our distribution. The EM work iteratively with two main steps, the E-step which creates a function for the expectation of the log-likelihood evaluated using the current estimate for the parameters, and a maximization (M) step, which computes parameters that maximizing the expected log-likelihood found on the E step. These parameter-estimates are then used to determine the distribution of latent variables in the next E step until convergence as described in equation (2). In our work, X is our feature vector that corresponds to RGB color. We train only one image to get the parameters, then test the rest of images depending upon those estimated parameters.

*[Formula 2 -- original formula not decoded. See PDF.]*

**Fig. 3.** Foreground background (FB) extraction steps

*[Image: Fig. 3 -- FB extraction pipeline. See original PDF for full image.]*

**Method 2: K-means segmentation.** K-means is one of the unsupervised algorithms that usually used in many applications, the idea is to cluster similar points into isolated clusters depending upon two parameters centroid and number of clusters. In each iteration, it assigns each object to the cluster that has the closest centroid, then recalculate the new centroids from the assigned data clusters. The algorithm converges by minimizing the total distortion in our objective function as described in equation (3).

*[Formula 3 -- original formula not decoded. See PDF.]*

K-means is used to get the circular mask for the plant's can to get rid of the false positive noise and undesired segments form background caused because of noisy image acquisition. Our input to the algorithm is a and b vector from the LAB color space since it perceptually uniform and closer to human vision, the output is three images represent the three clusters, we will use just one set of the clusters as a mask to EM results. All the intermediate results are shown in figure 3.

### B. Step2: Leaf segmentation

After extracting the plant form background, we need to identify the leaves of the plant individually. We use distance map calculation [21] to extract the centroid of each leaf from the local maximum of distance transform map. Watershed segmentation [22] is applied on distance map with optimal initial marker (centroid) over the image space. To connect the stems of the leaves, we develop the stem link algorithm (SLA) which dilate the stems to be connected to the surrounding regions, then assign the stem to the largest connected component sticked to it. The idea behind that is the fact that the stem is always oriented to the corresponding leaf, which is usually pick the larger connected leaf, so dilating them leads to know for which leaf or connected component that stem belongs to as shown in figure 4.

---

**[Part 2 of 4]** | Previous: [Part 1: Abstract & Introduction](unsupervised-learning-method-plant-leaf-segmentation-part-001-2026-05-18.md) | Next: [Part 3: Evaluation & Results](unsupervised-learning-method-plant-leaf-segmentation-part-003-2026-05-18.md)
