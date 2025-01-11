# Gradient Boosted Trees (GBT)
- *Summary*: Combines the prediction of multiple shallow weak-learner decision trees to create a strong predictive model. 
- *Loss*: MSE or cross-entropy, with a regularization term. 
- *Steps*:
  - Start with an initial guess for predicted probabilities, such as sigmoid(log-odds) for binary classification. 
  - For each sample, compute the negative gradient with respect to the output predictions. 
  - Fit a shallow decision tree to predict the negative gradients. Instead of Gini impurity split criteria, use reduction in loss as the criteria to split. 
  - Add the learning rate-scaled predictions to the previous predictions. 
  - Repeat until convergence. 
- *Notes*:
  - One GBT iteration is equivalent to a single gradient descent iteration. Hence the reason for starting with an initial guess. 
  - Since each tree is actually predicting the real-valued gradient, the trees are actually solving a regression problem, not classification. 

## XGBoost Features
- *Regularization*: Adds $L_1$ and $L_2$ regularization to the objective function. 
- *Parallel and Distributed Computing with GPU acceleration*
- *Supports custom objective functions*
- *Learning rate shrinkage and Early Stopping*
- *Tree pruning with Max Depth*: Constructs trees fully and then trims them. 
- *Built-in cross validation*