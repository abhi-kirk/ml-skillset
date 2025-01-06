# Bayesian Statistics
Bayesian statistics simply is one branch of statistics that relies on subjective probabilities and Bayes theorem to "update" knowledge regarding events and quantities of interest based on data - in order words, Bayesian statistics can draw/update/alter inferences regarding events/quantities when more data is available. For example, based on some knowledge, we can draw some initial set of inferences regarding the system (referred to as "prior" in Bayesian statistics) and then "update" these inferences based on data (to obtain the so-called "posterior").

Examples with usage in ML:
- In a standard Linear regression model, we can encode our belief that most features don’t matter by using Regularization.
- In a Bayesian Network, if we have some prior real-world knowledge corresponding to some part of the model, we can encode that directly. For example, in a network for medical diagnosis (e.g., this one for the diagnosis of liver disorders), if one parameter corresponds to the probability of an enlarged spleen given a particular liver disorder, and a published journal study has produced an estimate of that probability, we can encode a prior that pushes our model’s estimate towards that probability.
- If we're trying to model a particular problem and we have a lot of data from a related problem, we can use Bayesian hierarchical modeling or other forms of Bayesian Transfer Learning where we’re essentially using the related problem to form a prior belief for our current problem.

## When is it used over frequentist approach?
Reasons:
- Having relatively few data points. 
- Having strong prior intuitions (from pre-existing observations/models) about how things work. 
- Having high levels of uncertainty, or a strong need to quantify the level of uncertainty about a particular model or comparison of models. 
- Wanting to claim something about the likelihood of the alternative hypothesis, rather than simply accepting/rejecting the null hypothesis. 

## Challenges
- Most ML is done in the context of `big data' where the signature of Bayesian models - priors - don't actually play much or a role. 
- Sampling posterior distributions in Bayesian models is computationally expensive and slow. 