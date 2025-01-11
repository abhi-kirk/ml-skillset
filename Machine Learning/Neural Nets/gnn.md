# Graph Neural Nets
GNNs work directly with graph-structured data and leverage the relational information in the graph structure. 
- Nodes exchange information with their neighbors via *message passing*. 
- Each layer of GNN represents a single hop in the network. 
- Node embeddings are updated by aggregating information. 

## GNN Link Prediction
Steps:
- *Graph representation*: Model the data as a graph with node embeddings. 
- *Edge embeddings*: Compute edge embeddings using averaging or concatenation of respective nodes. 
- *Negative edge sampling*: Static or dynamic during training; hard negative mining. 
- *Training*:
  - Loss function: 
    - Cross-entropy for predicting edge vs. no edge. 
    - Contrastive or Triplet loss can be used (will have to mine hard negatives). 
  - Activation function: sigmoid or softmax to compute prediction probabilities.

Note:
- *Sparse graphs*: Unbalanced with higher number of no-edges vs edges. 
- *Dynamic graphs*: If the graph changes, need to re-train or use temporal GNN models. 
- *Scalability*: Computational challenges for message passing and embedding storage. 
- *Evaluation*: AUC, precision-recall, MRR. 
- *Heterogenous graph*: When the node types represent different entities (e.g., symptoms, root-causes), the graph would be heterogenous. 

## Graph Convolutional Network (GCN)
- Uses all neighbors for message passing. 
- Assumes uniform neighbor importance. 
- *Cannot handle unseen nodes during inference.*
- Works well on smaller datasets. 
- Works well on homogenous and static graphs. 

## GraphSAGE (Sample and Aggregate)
- Extends GCN by sampling a fixed number of neighbors for each node, improving scalability. 
- Assumes uniform neighbor importance. 
- *Can handle unseen nodes during inference.*
- Works well on both small and large datasets due to neighbor sampling. 
- Can handle any type of data, and both static and dynamic graphs. 

## Graph Attention Network (GAT)
- Uses all neighbors for message passing. 
- Uses attention mechanism to weigh neighbors differently during aggregation. 
- *Cannot handle unseen nodes during inference.*
- Requires large amounts of data due to attention mechanism. 
- Requires data to have meaningful edge relationships. 
- Can handle both homogenous and heterogenous, but only static, graphs. 

## Why the word "Convolution"?
- CNN: 
  - Exploits the regular grid structure to aggregate information. Each node (pixel) has four neighbors. 
  - Convolution refers to applying a filter/kernel to a local patch of data (in the grid) to aggregate spatially close information. 
  - Each output is a weighted sum of its local neighborhood, where the weights are the learned parameters of the filter. 
- GCN:
  - Each node can have a variable number of neighbors and there is no grid, hence CNN cannot be applied.
  - Each node aggregates information from its neighbors; hence the aggregation function acts like a convolution filter. 
  - The learned weights (how to combine neighbor node embeddings) are shared across all nodes, similar to CNN kernels. 

## GraphSAGE Hyperparameters
- Neighborhood sampling size
- Number of layers/hops
- Hidden dimension at each layer
- Aggregator function for neighbor embeddings
- Optimizer, Learning rate, Batch size, Dropouts, Weight Decay
- Inductive mode training to handle unseen nodes during inference
- Negative sampling strategy
- Link prediction neural net
