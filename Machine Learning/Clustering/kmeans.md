# KMeans Clustering

## Steps
- Choose the hyperparameter $k$ as the number of clusters. 
  - Use elbow method or silhouette score to choose $k$. 
- Initialize $k$ centroids by either:
  - Randomly choosing $k$ points as centroids, or
  - Smarter initializtion with **kmeans++**. 
- For each point:
  - Calculate the distance (euclidean, cosine) to each centroid. 
  - Assign to closest centroid. 
- Update the $k$ centroids for the $k$ clusters. 
- Repeat until:
  - The update to centroids is below a given threshold, or
  - Maximum number of iterations reached. 
- Implicit objective is to minimize the within-cluster sum of squares. 

## Limitations
- Choice of $k$. 
- Sensitivity to initialization. 
- Assumption of spherical clusters. 
- Affected by outliers. 
- Computationally expensive. 