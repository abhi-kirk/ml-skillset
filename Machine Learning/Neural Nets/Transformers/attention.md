## Self-Attention
- In a batch sequence, currently, the tokens are not talking to each other. We want to couple them such that tokens can have different *affinities* for each other.
- However, this coupling should not involve communication from the future tokens.
- Easiest way for the tokens to communicate is simply averaging the past sequence token embeddings from a given time step.
    - This strategy is very *lossy* since we have lost information regarding the special arrangement of tokens.
    - We will bring this information back later.
- The math trick allows us to compute this averaging efficiently.
- **Summary**: We want to do efficient weighted aggregation of past token embeddings for each sequence. 


### Solution:
- We want the weights-aggregation of the past embeddings to be more informative/complex than a simple average.
- Every single token (in every position) will emmit two vectors: **Query** and **Key**.
    - Query: *What am I looking for?*
    - Key: *What do I contain?*
- Affinities between tokens is obtained by taking the dot product between the Keys and Queries.
    - For a token, take the dot product of my Query with all the Keys from past tokens.
    - This dot product becomes the weight matrix.
    - Higher the dot product (i.e., what I'm looking for, and what the other token contains, is similar) --> higher the affinity.
- A third vector is also emmitted by each token: **Value**
    - Value: *What will I communicate to you?*
- Attention ($Q,K,V$) = softmax($\frac{QK^T}{\sqrt{d_k}}$)$V$
    - The scaling factor of $\sqrt{d_k}$, where $d_k$ is the `head_size`, is required to keep the weights normalized at a diffused variance (i.e., no peaks), especially at initialization.
- **Important Notes**
    - Attention is a communication mechanism. Can be seen as nodes in a directed graph looking at each other and aggregating information with a weighted sum from all the nodes in the past for the sequence. The graph is connected in an auto-regressive manner for language modeling.
    - There is no notion of space, contrary to convolutions which are done specifically over a spatial dimension. If spatial information is needed, we need to encode it separately outside of attention mechanism.
    - Elements across the batch never talk to each other. E.g., for a batch size of 4, we have 4 separate directed graphs which are not conncted to each other.
    - For a generative use-case, we have a constraint that tokens cannot communicate with future tokens. For the general use-case, we can remove this constraint such as with sentiment analysis (tokens can talk to the ones in past and future, and spit out a sentiment). If the constraint is removed, it is called an *Encoder* block, otherwise its called a *Decoder* block.
    - Difference between self- and cross-attention: In self-attention, the Keys, Query and Value all come from the same source (batch). If Keys and Values come from a separate external source, it is called cross-attention. 


## Multi-Head Attention
- Running several independent self-attention heads in parallel, with the `head_size` scaled down proportional to the number of heads.
- Independent heads can enable different *types* of communication among tokens.
- We also include a *Feedforward NN (MLP)* after gathering all communication from all heads.
    - The MLP computation is executed on each node (output of Multi-Head Attention) independently, and enables the nodes to individually *think* about the information that has been gathered from other nodes.
    - Implemented after multi-headed attention block, and before computing the logits.
- We next create **Transformer Blocks** of Multi-Head Attention and MLP (Feedforward NN) to intersperse *communication* and *computation*, respectively.
    - These blocks are independent and run in parallel. 


## Deep Network Issues
With very deep networks like this one, we may run into optimization issues. 

**Solutions**:
- *Skip Connections* ([Paper](https://arxiv.org/pdf/1512.03385))
    - We transform the data, and have an addition to the output from the original features.
    - During backprop, addition operation simply passes through the gradients. Hence with skip connections, we will have a gradient *super highway* for gradients to flow to the original inputs unimpeded (at least at initialization; later in the optimization the transformation blocks kick in).
    - We implemenet skip/residual connections with self-attention and feedforward networks separately - where we fork off, do computations (self-attention or feedforward), and come back to sum the results. 
- *Layer Normalization* ([Paper](https://arxiv.org/pdf/1607.06450))
    - Very similar to Batch Normalization; but making sure each token embedding has zero mean and unit variance at initialization.
    - Pre-Norm formulation (slight departure from paper): The *Add & Norm* operation in the paper is implemented after the attention and feedforward layers. However, now it is common practice to implement Normalization before these transformation layers.
    - Aside from inserting it before transformation layers, we also insert it before the final transformer linear layer.
    - Implemented at a per token level. 
- *Dropouts* ([Paper](https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf))
    - Inserted right after computations / transformations are done.
    - Regularization technique to reduce overfitting. 