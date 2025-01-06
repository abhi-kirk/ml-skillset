**Introduction**
- Simplified way of implementing the Bayes' theorem. 
  - Bayes theorem is computationally expensive, and requires a large number of samples. 
  - Assumptions: Each input is independent of all other input variables. 
    - Calculations of the conditional probability become tractable. 
- Probabilistic model: We are interested in estimating the conditional probability of the class label, given the observations. 
  - Calculate $P(y_i|x_1,...,x_n)$, where $i=1,...,k$ are the distinct class labels. 
  - The class label associated with the highest probability is returned. 
- The above conditional probability can be calculated as a joint probability, but it would be intractable. 

$$P(y_i|x_1,...,x_n) = P(x_1,...,x_n,y_i) = P(x_1|x_2,...,x_n,y_i).P(x_2|x_3,...,x_n,y_i)...P(y_i)$$

- Problem formulated using Bayes' theorem:

$$P(y_i|x_1,...,x_n) = \frac{P(x_1,...,x_n|y_i).P(y_i)}{P(x_1,...,x_n)}$$

- The above is also intractable since calculating $P(x_1,...,x_n|y_i)$ will require estimating a probability distribution for all different combinations of input values. 
- Naive Bayes:
  - Denominator is removed since it is constant and has the effect of only normalizing the result. 
  - Numerator using the input feature independence assumption:

  $$P(x_1,...,x_n|y_i) = P(x_1|y_i)...P(x_n|y_i)$$

  - The above calculation is performed for each class label, and the label with the highest probability is selected as the result of classification (*Maximum a-Posteriori* (MAP) decision rule). 

  $$P(y_i|x_1,...,x_n) = P(y_i).\prod_{j=1,..,n}P(x_j|y_i)$$
---

**Calculations**
- *Prior* $P(y_i)$ is simply estimated by dividing the frequency of observations in the training dataset by the total number of examples in the training set. 
- The conditional probability (distribution) of a feature given a class label $P(x_j|y_i)$ can be estimated depending on the data type of the feature:
  - Binary: Binomial distribution (*Binomial Naive Bayes*), 
  - Categorical: Multinomial Naive Bayes (*Multinomial Naive Bayes*), 
  - Numeric: Gaussian distribution (*Gaussian Naive Bayes*). 
- Any other type of distribution can be used based on prior knowledge of the dataset. 
- If real-valued features do not have a well-defined distribution, then a *kernel density estimator* can be used to estimate the probability distributions. 
---

**Enhancements**
- Since several probabilities are being multiplied together to get the class conditional probability, the output can become numerically unstable, especially as the number of features increase. 
  - Solution is to take the sum of logarithms such as:

  $$P(y_i|x_1,...,x_n) = \log(P(y_i)) + \sum_{j=1,..,n}\log(P(x_j|y_i))$$

- Since we estimate probability distributions for all classes and all features, a *generative model* can be built to generate new data by sampling these distributions. 
- Input data drift (such as varying distributions over time) can be easily accounted for, by appending new data to the old data and then re-generating the distributions. 
- It is noted that the classifier performance will decrease as feature dependence increases (since this will violate the core algorithm assumption). 