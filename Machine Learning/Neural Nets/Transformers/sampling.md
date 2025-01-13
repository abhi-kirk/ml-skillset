# Transformer Decoder

## Challenges
- Decoding is done iteratively, which is computationally expensive. 
- Not computationally possible to optimally predict the entire future sequence. 
  - We will have to recursively predict probabilities for all vocab tokens, and multiply them till we reach the special token. 
- Quality and diversity of the generated text depends on the method used and its hyperparameters. 


## Decoding Methods:
- *Greedy Search Decoding*
  - Simply select the highest probability token at every iteration. 
  - Advantage: Easy to implement, little cost to compute. 
  - Limitation: Not optimal, tends to produce repetitive output sequences. 
- *Beam Search Decoding*
  - Keeps track of the top-b most probable tokens, where b is referred to as the number of beams. Take the log probabilities sum for every path, and select the max. 
  - Advantage: More optimal than greedy. 
  - Limitation: More compute intensive, introduces a hyperparameter, still repetitive. 

## Temperature
- Out probabilities are computed as: $P(y_t=w_i|y_{<t}, \mathbf{x}) = \text{softmax}(z_{t,i}) = \frac{\exp(z_{t,i})}{\sum_{j=1}^{V}\exp(z_{t,j})}$, where $V$ is the length of the vocab, $i$ is the index of the chosen token in the vocab, and $t$ is the current time step. 
- We can introduce a hyperparameter $T$ such that: $P(y_t=w_i|y_{<t}, \mathbf{x}) = \frac{\exp(z_{t,i}/T)}{\sum_{j=1}^{V}\exp(z_{t,j}/T)}$. 
- If $T<<1$, the distribution becomes peaked around the origin and the rare tokens are suppressed. 
- If $T>>1$, the distribution is flattened and each token becomes equally likely. 

## Sampling Methods:
- *Random Sampling*: Sample from the output distribution over the full vocab. 
- *Top-k Sampling*: Only consider the top-$k$ tokens with highest probabilities. 
- *Top-p (Nucleus) Sampling*: Only consider the tokens which result in the cumulative sum of probabilities of $p$. 
- Random, top-$k$ and top-$p$ samplings can be all used together. Example
  - Limit the output tokens to $k$, 
  - Further limit to tokens where cumulative sum (taken in descending order) reaches $p$, 
  - Sample randomly from these tokens. 