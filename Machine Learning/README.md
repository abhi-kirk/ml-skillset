# Formulas To-Remember

## Sigmoid: 
$$\frac{1}{1 + e^{-z}}$$

## Softmax
$$\frac{e^{z_i}}{\sum_{i}e^{z_i}}$$

## Logistic Regression
$$P(X=1) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}$$

## $R^2$ Statistic
$$\frac{TSS - RSS}{TSS}$$
where: TSS = $\sum (y_i - \bar{y})^2$ and RSS = $\sum_{i=1}^n (y_i - \hat{y_i})^2$. 

## Self-Attention
$$\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
where $d_k$ is the attention head size. 

## Binary Cross-Entropy / Log Loss
$$-\frac{1}{n}\sum_{i=1}^n [y_i\log(p_i) + (1-y_i)\log(1-p_i)]$$

## MSE Gradient
$$\frac{1}{n}(\hat{y_i} - y_i)X$$
where $\hat{y_i} - y_i$ is the residual, and $n$ is the number of samples. 

## Gini Impurity
$$1 - \sum_{i=1}^C p_i^2$$
where $C$ is the number of classes, and $p_i$ is the class proportion. 

## IDF
$$\text{IDF}(t, D) = 1 + \log\left(\frac{N+1}{d+1}\right)$$
where $N$ is the total number of documents ($D$), and $d$ is the number of documents that contain the term $t$. 

## Covariance Matrix
$$\text{cov}(x, y) = \frac{\sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{n-1}$$

## Cosine Similarity
$$\frac{a.b}{||a||.||b||}$$
where $a.b$ is the dot product (summed element-wise multiplication), and $||x||$ represents the 2-norm of $x$. 

## Single Neuron
$$z_i = \sum_{j=1}^m w_jx_j + b$$
$$\sigma(z_i) = \frac{1}{1 + e^{-z_i}}$$
$$L = \frac{1}{n}\sum_{i=1}^n (\sigma(z_i) - y_i)^2 = \frac{1}{n}\sum_{i=1}^n r_i^2$$
$$\frac{\partial L}{\partial w_j} = \frac{1}{n}\sum_{i=1}^n r_i \sigma'(z_i)x_{ij}$$
$$\frac{\partial L}{\partial b} = \frac{1}{n} r_i\sigma'(z_i)$$
$$w_j \leftarrow w_j - \alpha\frac{\partial L}{\partial w_j}$$
$$b \leftarrow b - \alpha\frac{\partial L}{\partial b}$$

## KL Divergence
$$KL(p, q) = \sum_i p_i\log\left(\frac{p_i}{q_i}\right)$$
where $p$ and $q$ are probability distributions. 