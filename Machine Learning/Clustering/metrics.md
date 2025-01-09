# Clustering metrics

## Silhouette score
- Measures how similar a sample is to its own cluster (cohesion) compared to other clusters (separation). 
- For each point:
  - $a$: Calculate average distance to all other points in the same cluster. 
  - $b$: Calculate average distance to all points in the nearest cluster. 
  - *Silhouette score*: $\frac{b-a}{\max{(a,b)}}$
- Range [-1, 1], where higher indicates better clustering (compact, well-separated). 
  - 1: well-clustered point, 
  - 0: point is on the boundary between clusters, 
  - -1: point might be in the wrong cluster. 
- Sensitive to dataset geometry and cluster density. 

## Davies-Bouldin index
- Measures the average similarity ratio of each cluster to its most similar cluster. 
- For each cluster:
  - $S_i$: Calculate average distance (scatter) within cluster $i$. 
  - $D_{ij}$: Distance between cluster centroids $i$ and $j$. 
  - Cluster similarity: $R_{ij} = \frac{S_i + S_j}{D_{ij}}$. 
  - Find highest similarity: $R_i = \max{(R_{ij})}$. 
  - *DB index* is the average of $R_i$ for all clusters: $\frac{1}{p}\sum_{i}^{p}R_i$. 
- Range $\geq 0$, where lower indicates better clustering (compact, well-separated). 
  - Penalizes clusters that are either large (high scatter) or close to other clusters (poor separation). 
- Sensitive to the number of clusters: higher number of clusters will lead to higher DB values. 