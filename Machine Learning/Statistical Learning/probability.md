## Probability Space
A mathematical construct that provides a formal model of a radom process or experiment. It consists of three elements:
- A sample space $\Omega$: set of all possible outcomes. 
- An event space $F$: Set of events, an event being a set of outcomes in the sample space. 
- Probability function $P$: Assigns each event in the event space a probability, which is a number between 0 and 1. 

Example: Throwing a standard die. 
- $\Omega = \{1,2,3,4,5,6\}$. 
- $F = Set(\{1\}, \{2\}, ..., \{2, 3\}, ...)$. 
- $P(\{1\}) = 1/6$, $P(\{2,3\}) = 2/6$, ...


## Joint Distribution
Given two random variables that are defined on the same probability space, the joint probability distribution is the corresponding probability distribution on all possible pairs of outputs. 
- Encodes the *marginal distributions*, i.e. the distributions of each of the individual random variables. 
- Also encodes the *conditional probability distributions*, which deal with how the outputs of one random variable are distributed when given information on outputs of other random variables. 

<img src="../../imgs/Multivariate_normal_sample.svg" width=500>


## Central Limit Theorem
Taking samples from a population and calculating the sample mean each time, the distribution of these mean will approach the normal distribution as number of experiments (taking samples) are increased. Assumptions (can be relaxed for real-world scenarios):
- The events in every sample are independent from each other. 
- All events in the samples have the same marginal distribution. This marginal distribution can be any distribution. 
- Population variance should be finite. 

Relevance to regression: In standard OLS regression, we assume that the error term is normally distributed. This can be argued with CLT. 

Hypothesis testing: The distribution for the null hypothesis can usually be formulated as the normal distribution under CLT. Example with Click Through Rate (CTR):
- If the claim is that the CTR is 20%, then:
  - We can model the marginal distribution of click/no-click as a binomial distribution with mean of 0.2 and std as a function of this mean. 
- We draw $n$ samples, i.e. we do $n$ (i.i.d) observations of ads. 
  - The sample CTR, according to CLT, will follow a normal distribution with mean as 0.2, and std as a function of mean and $n$. 
- Hence from this normal distribution, we can determine, based on our observed sample mean, if the claim of 20% is valid or not. 