# Bayesian Linear Regression

## Frequentist LR
The frequentist view of linear regression assumes data is generated from the model: 

$$y = \beta^TX + \epsilon$$ 

where $y$ is the response variable, $\beta$ are the model parameters, $X$ is the data (features), and $\epsilon$ is the error term due to random sampling noise or latent variables. 

### Characteristics:
- The output from OLS is the single point estimate given the training data and the 'best' estimated model parameters. 
- The parameters, once estimated, can be used to make prediction for new data points.  
- The uncertainty in predictions due to amount of data is not reflected in the response point estimates. 

## Bayesian LR
The bayesian view of linear regression assumes responses are sampled from a probability distribution such as a normal (Gaussian) distribution as:

$$y \sim N(\beta^TX, \sigma^2)$$

where the OLS prediction $\beta^TX$ is the mean, and $\sigma^2$ is the variance. The model parameters are also themselves drawn from a *posterior* probability distribution:

$$P(\beta|y,X) = \frac{P(y|\beta,X).P(\beta)}{P(y|X)}$$

Shown above is the Baye's Rule which corresponds to: 

$$Posterior = \frac{Likelihood * Prior}{Normalization}$$

### Characteristics:
- Domain knowledge can be used to formulate priors. 
  - Informative priors are those with specific distribution shapes and/or parameters, given prior beliefs (due to data or intuition) or domain knowledge. 
  - Non-informative priors are generally taken as normal distributions with large variances, i.e. "let the data speak". 
- The end result of bayesian modeling is not a single point estimate of model parameters, but a distribution which reflects the uncertainty due to low amount of data and also incorporates prior beliefs. 
  - Response variable distributions can then be generated using model parameters sampled from their estimated distributions. 
- As the amount of data increases, the likelihood increases (uncertainty decreases) and the prior gets washed out. 
  - With infinite data, the mean of posteriors will converge to the OLS estimates. 
  - We can also update our priors with new information. 
- In practice, calculating the exact parameter posterior distribution is computationally intractable for continuous values. Hence we use sampling methods to approximate the posterior. 
  - MCMC (Markov Chain Monte Carlo) is such a sampling method. 
    - Monte Carlo is the family of such algorithms. 
    - Markov Chain mean the next sample drawn is based only on the previous sample value. 


### Time-Series Modeling
Bayesian LR (i.e. including priors) avoids over-fitting, especially with multi-variate analysis with large number of parameters over a short time period. 
- Common in economic forecasting. 
- Can be compared to Ridge regression where an $L_2$ penalty is imposed on the OLS regression problem. 
- Allows us to incorporate uncertainty in the model parameters which can change over time with forecasting. 