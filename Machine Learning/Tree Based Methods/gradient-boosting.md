# Gradient Boosting Method (GBM) Trees
GBMs use additive models where each iteration performs: $F_{i+1} = F_i - f_i$, where $F_i$ is the strong model at step $i$, and $f_i$ is the weak model at step $i$. 

[Steps](https://developers.google.com/machine-learning/decision-forests/intro-to-gbdt):
1. Strong model is initialized as $F_0(x) = 0$. 
2. Calculate the error of the strong model: $F_0(x) - y$. 
3. Fit a weak model (decision tree), with labels as the error of the strong model ($F_0(x)-y$), to the data to obtain $f_0(x)$. 
4. The strong model for the next iteration is calculated from the predictions of the weak model: $F_1(x) = F_0(x) - f_0(x)$.
5. Repeat from Step 2 until a stopping criterion is reached.  

*Shrinkage* (analogous to learning rate) is usually applied to the weak model before added to the strong model as:

$$F_{i+1} = F_i - \nu f_i$$

The above is equivalent to performing a gradient descent step in the function space. 

# XGBoost (Extreme Gradient Boosting)
XGBoost is a parallelized and optimized version of GBM trees. 
- Parallelization is within a single tree. It is not possible to parallelize the ensemble itself. 
- Regularization is applied with $L_1$ and $L_2$. 
- Usage of sparse matrices with sparsity-aware algorithms. 
- Better support for multi-core processing. 
- Improved data structures for better cache utilization. 