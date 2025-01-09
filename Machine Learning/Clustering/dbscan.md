# DBSCAN Clustering

## Parameters
- **Epsilon $\epsilon$**: Radius around a point to consider its neighborhood. 
- **MinPts**: Minimum number of points required to form a dense region. 

## Definitions
- **Core point**: A point with at least **MinPts** points within the $\epsilon$ radius. 
- **Border point**: A point within $\epsilon$ of a core point but with fewer than **MinPts** neighbors in its own radius. 
- **Noise point**: A point that is neither a core point or a border point. 

## Steps
- Initially all unvisited points are labeled as noise points. 
- Choose a random unvisited point. If it's a core point, start a new cluster. Mark it as visited. 
- Expand the cluster by adding all $\epsilon$-neighborhood points to the cluster. 
- For each $\epsilon$-neighborhood point:
  - Mark it as visited. 
  - If it's a core point, keep expanding the cluster recursively. 
  - If it's a border point, do not expand further. 

## Properties
- Automatically determines the number of clusters. 
- Does not assume clusters are spherical. 
- Sensitive to hyperparameters. 
- Not all points may be clustered (can be an advantage or disadvantage). 
- Performance drops in high-dimensional spaces due to curse of dimensionality. 
- Can be difficult to analyze clustering performance. 


# HDBSCAN

Differences from DBSCAN:
- Hierarchical density-based: build a cluster hierarchy. 
- Handles high-dimensional data better than DBSCAN. 
