# AdaBoost (Adaptive Boost)
The core principle is to fit a sequence of weak learners on repeatedly modified versions of the data. 

**Training Algorithm**
1. For the first stump, initialize the sample weights as 1/#samples. 
2. Create the stump using the input dataset, by choosing the feature which maximizes the entropy/Gini gain. 
3. Determine *stump influence*:
   1. Calculate the errors/residuals for each sample. 
   2. Calculate the stump total error as the sum of weighted misclassified samples. 
   3. Calculate the *stump influence* with a $\log$ formula of stump total error, such that higher stump total error results in a lower stump influence.  
4. Update sample weights:
   1. New weight = old weight * $e^{\plusmn\text{stump influence}}$, where negative exponential is used for misclassified samples. Then normalize the weights. 
   2. Intuition is that we are increasing the sample weight if it was misclassified. 
5. Create new dataset by using the new weights as the probability distribution, so that misclassified samples appear more often in the new dataset. 
6. Repeat from Step 2 until a stopping criterion is reached, which can be:
   1. Number of stumps, or
   2. Stabilization of stump total error. 

---

**Training Parameters**
- Estimator: Decision tree (stump), Random Forest, etc. 
- Number of estimators as stopping criterion. 
- Learning rate: Weight applied to each classifier at each boosting iteration. A higher weight increases the contribution of each classifier. 

---

**Inference Algorithm**
- All stumps classify/regress on the new data. 
- Predictions from all stumps are combined through a weighted majority, where weights are the stump-weights determined during training, to produce the final prediction. 