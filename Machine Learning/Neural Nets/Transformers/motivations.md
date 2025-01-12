## Metric: Negative log-likelihood
- Likelihood is product of probabilities of model parameters (we want to maximize it)
- Right now the model is simply the bigram statistical model (probabilities of characters occuring together)
- Since this product can be very small, we use log for convenience
- $\log(a.b.c) = \log(a) + \log(b) + \log(c)$
- Since higher log(a*b*c) means better model, we take negative of it to treat as a loss function (lower the better, where 0 is perfect model)
- Can also use average instead of sum for log probabilities
- The probababilities can be calculated with Neural Nets, or a lookup table for a bigram model. 