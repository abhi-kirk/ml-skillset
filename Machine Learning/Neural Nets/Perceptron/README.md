## Single Layer Perceptron
- For binary classification, find a (linear) function s.t. $f(\bf{x}) = 1$ when $\bf{w}.\bf{x} + b > 0$, and $f(\bf{x}) = 0$ otherwise. 
  - Hence, we need to find $\bf{w}$ and $b$. 
- Since the function is linear, it can only classify features that have linearly separable classes. 
- Even though guaranteed to converge for linearly separable classes, the perceptron can choose *any* linear solution (i.e. in the margin around the linearly separable hyperplane). SVM was designed to choose the optimal hyperplane. 
- Stops updating the weights as soon as all samples are classified correctly. This leads to poor generalizations. 

### Definitions
- $r$ is the learning rate of the algorithm. 
- $y = f(\bf{z})$ denotes the perceptron output for an input vector $\bf{z}$. 
- $D = \{(\bf{x}_1, d_1), ..., (\bf{x}_i, d_i), ...,  (\bf{x}_n, d_n)\}$ is the training set of $n$ samples. 
  - $\bf{x}_i$ is the $m$-dimensional input vector. 
  - $d_i$ is the desired output value (i.e. class label) for the $i^{th}$ sample. 
- $w_j$ is the $j^{th}$ value of the weight vector, to be multiplied by the $j^{th}$ feature for each input sample. 
- $x_{i, j}$ is the value of the $j^{th}$ feature for the $i^{th}$ sample. 
  - $x_{i, 0} = 1$, hence $w_0$ is the constant bias. 
- $w_j(t)$ is the weight $j$ at time $t$.  

### Algorithm (Perceptron Rule)
1. Initialize the weight vector $\bf{w}$ with zeros or (uniform/normal distributed) random values. 
2. For each sample $i$: 
   1. Compute: $\bf{x}_i.\bf{w}$ = $x_{i, 0}.w_0 + ... + x_{i, m}.w_m$. 
   2. Get actual output: $y_i = f(\bf{x}_i.w)$. 
   3. Update the weights: $w_j(t+1) = w_j(t) + r.(d_i-y_i(t)).\bf{x}_{i, j}$ for all features $j = \{1, ..., m\}$. 
      1. Hence weights are updated after every training sample. 
3. Repeat Step 2. until the iteration error $\frac{1}{n}\sum_{i=1}^{n}|d_i-y_i(t)| < \epsilon$. 

### Differences with Gradient Descent
- Gradient descent minimizes a quadratic cost function by taking derivatives of the function w.r.t. the weights. 
- The output ($y_i$) of GD is real-valued rather than binary/categorical as with Perceptron Rule. 
- The weights are updated based on all samples in the training set rather than incrementally updating weights after each sample. 
- If the weights are updated incrementally, then GD becomes *Stochastic GD* which is equivalent to Perceptron Rule albeit for regression. 
  - Stochastic GD also has the flexibity to utilize a sample of the training set (called a batch) for updating weights. 