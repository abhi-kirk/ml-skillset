# ML Formulas To Remember

## Sigmoid: 
$$\frac{1}{1 + e^{-z}} = \frac{e^{z}}{1+e^{z}}$$

## Softmax
$$\frac{e^{z_i}}{\sum_{i}e^{z_i}}$$

## Linear Regression
$$\hat{y_i} = w_i^Tx_i + b_i$$

$$l_i = \frac{1}{2} (\hat{y_i} - y_i)^2$$

where $l_i$ is the MSE loss. 

## Logistic Regression / Single Neuron (no activation)
$$z_i = w_i^Tx_i + b_i$$

$$\hat{y_i} = \sigma(z_i) = \frac{1}{1+e^{-z_i}}$$

$$l_i = -[y_i\log(\hat{y_i}) + (1-y_i)\log(1-\hat{y_i})]$$

where $l_i$ is the binary cross-entropy / negative log loss. 

## Loss Gradients
$$\frac{\partial l_i}{\partial w} = (\hat{y_i} - y_i)x_i = r_ix_i$$

$$\frac{\partial l_i}{\partial b} = \hat{y_i} - y_i = r_i$$

$$L = \sum_{i=1}^n l_i$$

$$\frac{\partial L}{\partial w} = \sum_{i=1}^n \frac{\partial l_i}{\partial w}$$

$$\frac{\partial L}{\partial b} = \sum_{i=1}^n \frac{\partial l_i}{\partial b}$$

where $r_i$ is the residual. 

## Parameter Updates
$$w \leftarrow w - \alpha \frac{\partial L}{\partial w}$$

$$b \leftarrow b - \alpha \frac{\partial L}{\partial b}$$

## $R^2$ Statistic
$$\frac{TSS - RSS}{TSS}$$

where: TSS = $\sum (y_i - \bar{y})^2$ and RSS = $\sum_{i=1}^n (y_i - \hat{y_i})^2$. 

## Self-Attention
$$\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

where $d_k$ is the attention head size. 

## Gini Impurity
$$1 - \sum_{i=1}^C p_i^2$$

where $C$ is the number of classes, and $p_i$ is the class proportion. 

## IDF
$$\text{IDF}(t, D) = 1 + \log\left(\frac{N+1}{d+1}\right)$$

where $N$ is the total number of documents ($D$), and $d$ is the number of documents that contain the term $t$. 

## Covariance Matrix
$$\text{cov}(x, y) = \frac{\sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{n-1}$$

## Cosine Similarity
$$\frac{a.b}{\Vert a\Vert.\Vert b\Vert}$$

where $a.b$ is the dot product (summed element-wise multiplication), and $\Vert x\Vert$ represents the 2-norm of $x$. 

## KL Divergence
$$KL(p, q) = \sum_i p_i\log\left(\frac{p_i}{q_i}\right)$$

where $p$ and $q$ are probability distributions. 

$$\text{Cross-Entropy}(y,\hat{y}) = E(y) + KL(y,\hat{y})$$

where $E(y)$ is the entropy (uncertainty) of the true distribution (constant for a given dataset). 

## Z-score
$$\frac{x - \mu}{\sigma}$$