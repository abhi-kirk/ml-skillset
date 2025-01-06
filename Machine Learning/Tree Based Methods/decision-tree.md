# Decision Tree

**Setup**:
- Let $X\in(n, m)$ be the feature matrix with $n$ number of samples, and $m$ number of features. 
- Let $y\in(n, 1)$ be the label vector of categories (classification) or real-valueed (regression). 
- `Gini impurity`:
  - Measure of how "pure" the samples are in a given node. 
  - Given by $1 - \sum_{1}^{k}p^2$, where $k$ is the total number of classes, and $p_i$ is the fraction of samples in the $i^{th}$ class. 

## Training
**Steps**:
1. Start with all samples belonging to a root node. The goal is yo split the node into child nodes that are more "pure" in terms of class distribution (i.e., with low Gini impurity). 
2. Calculate the Gini impurity for the root node. 
3. Find the best split:
   1. For each feature, consider all possible thresholds that can split the data. 
      1. For continuous features, thresholds are midpoints between consecutive sorted values. 
      2. For categorical features, consider all possible subsets of categories. 
   2. For each potential split, divide the data into two groups (left and right chold nodes), and calculate the Gini impurity for each node. 
   3. Compute the weighted average Gini impurity of left and right child nodes, weighted by the fraction of samples in the node. 
   4. Select the split with the lowest Gini impurity. 
4. Recursively find the best split for child nodes until a stopping criterion is met. Common ones are:
   1. Max depth, 
   2. Minimum number of samples per node, 
   3. Node is pure, 
   4. Improvement in Gini impurity is below a threshold. 
5. Once the tree is fully grown, assign a class label to each leaf node by taking the majority class of the samples in that node. 
6. To avoid overfitting, `Prune` the tree by removing nodes that provide little predictive power. 

**Time Complexity**: $O(m.n^2)$
- Finding the best split $O(n\log{n}) + O(n^2) := O(n^2)$
  - For each node, the algorithm evaluates potential splits for each feature. 
  - Since this involves sorting for continuous features, time complexity is $O(n\log(n))$. 
  - For each possible split point ($O(n)$), Gini impurity is calculated whic itself is $O(n)$. 
- Evaluating all features $O(m)$. 

## Inference
Traverse the tree from root node to leaf node, to determine the predicted class for a new sample. Gini impurity is not used in this process. 

**Steps**:
1. At each node, evaluate the split criterion (*not Gini impurity*) based on the feature and threshold used to split the data during training. 
2. Move to the left or the right child node based on the result of the condition. 
3. Continue evaluating the split criterion and traversing the tree unitl you reach the leaf node. 
4. Once the leaf node is reached, assign the class label associated with the leaf node to the sample. 
   1. This class is the majority class from the training samples that reached this leaf node. 

**Time Complexity**: $O(d)$
- $d$ is the tree depth. 
  - In a balanced tree, $d = \log{n}$ since the tree divides the data evenly in each split. 
  - Worst case, $d = n$ when each split reduces the dataset by one sample. 
- Note that the complexity is independent of $m$ since we don't evaluate all features (we already know which features to split on, from training). 