# Learning to Rank Algorithms
- Only considering pairwise approaches where learning is based on relative order in the pair. 
- Objective is to predict the relative order of documents, ensuring that a more relevant document is ranked higher than a less relevant one. 
- Taking pairs of items $(x_i,x_j)$ for a given query, where $x_i$ is more relevant than $x_j$. 

## RankNet
- *Summary*: Uses a neural net to minimize a pairwise cross-entropy ranking loss using gradient descent. 
- *Loss*: $-\sum_{(i,j)}[y_{ij}\log{(p_{ij})} + (1-y_{ij})\log{(1-p_{ij})}]$, where: 
  - $y_{ij}=1$ if $x_i$ is more relevant than $x_j$, otherwise $y_{ij}=0$, 
  - $p_{ij} = \text{sigmoid}(s_i-s_j)$, where $s_k$ is the relevance score assigned to $x_k$. 
  - The loss penalizes predictions that deviate from the true order. 
- *Gradients*: Computed for parameters $s_i$ and $s_j$ for the pair $(i,j)$. 
  - $g_i = p_{ij} - y_{ij}$ and $g_j = y_{ij} - p_{ij}$. 
  - These gradients are used to compute the loss gradients with respect to the neural net parameters using chain rule. 


## LambdaNet
- *Summary*: Variant of RankNet that uses gradient scaling to directly optimize ranking metrics such as nDCG during the training process. 
- *Lambda gradients*: 
  - $\lambda_{ij} = \Delta\text{nDCG}.(p_{ij} - y_{ij})$, where $\Delta\text{nDCG}$ is the change in the nDCG metric if $x_i$ and $x_j$ were swapped. 
- Because of the gradient scaling, LambdaNet does not explicitly minimize the cross-entropy loss. 

## LambdaMART
- *Summary*: Combines ideas from LambdaNet and MART (Multiple Additive Regression Trees) to leverage boosted trees. 
- *Notes*:
  - Metric-aware gradient scaling with additive gradient boosted trees. 
  - Trees are grown to predict the Lambda gradients at every iteration. 