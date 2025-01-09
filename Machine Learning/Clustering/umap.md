# UMAP (Uniform Manifold Approximation and Projection)

## Steps
- Understand the local neighborhood in high-dimensional space
- Capture the global structure in low-dimensional space
- Compress the data to lower dimensions
- Optimize the layout

## Parameters
- **n_neighbors**: Controls the size of the local neighborhood used in constructing the graph in the high-dimensional space. 
- **min_dist**: Minimum distance between points in the low-dimensional space. 
- **n_components**: Number of dimensions in the reduced space. 
- **distance metric**: How distance is measured in the high-dimensional space. 