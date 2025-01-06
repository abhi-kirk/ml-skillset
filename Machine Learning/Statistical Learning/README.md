# Statistical Learning

## Basics
For system: $Y = f(X) + \epsilon$, and estimate $\hat{Y} = \hat{f}(X)$:
- The accuracy of $\hat{Y}$ as a prediction of $Y$ depends on two quantities:
  - *Reducible error*: Can be mitigated by using a proper technique for estimating $f$. 
  - *Irreducible error*: Even if we have a perfect estimate for $f$, such that $\hat{Y} = f(X)$, we will still have errors in the prediction $\hat{Y}$ because $Y$ is also a function of $\epsilon$. 
    - $\epsilon$ may contain unmeasured variables or unmeasured variations. 
- Considering $\hat{f}$ and $X$ are fixed:

    $$E(Y - \hat{Y})^2 = [f(X) - \hat{f}(X)]^2 + Var(\epsilon)$$

    where $[f(X) - \hat{f}(X)]^2$ is the *reducible error*, and $Var(\epsilon)$ is the irreducible error. 

## Bias vs. Variance Tradeoff
Describes the relationship between a model's complexity, the accuracy of its predictions, and how well it can generalize to unseen data. 

**Bias** is the error introduced by approximating a real-life problem/system, which may be extremely complicated, by a simpler model. 
- High bias leads to underfitting. 
- Can be minimized with: More complex model and higher number of parameters. 

**Variance** is the sensitivity of the model to changes in the training dataset. 
- High variance leads to overfitting. 
- Can be minimized with: Regularization, decreasing the number of parameters by using a simpler model. 

**Tradeoff**
- More flexible (higher degrees of freedom) models:
  - Low bias, high variance. 
  - High number of parameters. 
  - Less generalizable. 
  - Less interpretable. 
  - Examples: boosting trees, neural nets. 
- Examples of less flexible models: lasso regression. 
- For a test sample set $(x_0, y_0)$:
    $$E(y_0 - \hat{f}(x_0))^2 = Var(\hat{f}(x_0)) + [Bias(\hat{f}(x_0))]^2 + Var(\epsilon)$$
    i.e. Expected test MSE is the average test MSE that we would obtain if we repeatedly estimated $f$ using a large number of training sets, each tested at $x_0$. 
    - Note that even with zero bias and zero variance, the irreducible error still will be the upper bound on this expected test MSE. 