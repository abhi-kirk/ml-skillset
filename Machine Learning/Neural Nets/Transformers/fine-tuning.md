## BERTScore
- Computes Precision, Recall and F1 scores given generated text and reference text. 
- Steps:
  - Convert generated and reference text to tokens using a BERT tokenizer. 
  - Create embeddings for each token using a BERT model (compatible with the tokenizer used in the previous step). 
  - Compute cosine similarities between each token embedding in the generated text, with each token embedding in the reference text. 
  - *Recall*:
    - For each token in the reference text, find the maximum cosine similarity with any token in the generated text. 
    - Compute the average of these maximum similarities across all tokens in the reference text. 
  - *Precision*:
    - For each token in the generated text, find the maximum cosine similarity with any token in the reference text. 
    - Compute the average of these maximum similarities across all tokens in the generated text. 


## Knowledge Distillation
- *Task*: Fine-tuning a smaller *student* model to mimic the behavior of a slower, larger, but better performing *teacher*. 
- *Intuition*: Augment the ground truth labels with a distribution of "soft probabilities" from the teacher which provide complementary information for the student to learn from. 
- *Steps*:
  - Feed an input sequenece to teacher to generate a vector of logits. 
  - Apply softmax on logits, along with a high Temperature, to flatten the probability distribution (or "soften" the probabilities). 
  - Feed the input sequence to student as well, with the same Temperature, to get soft probabilities from student. 
  - Apply Kullback-Leiber (KL) divergence to measure the difference between the two probability distributions. 
  - Define a knowledge distillation loss proprotional to the KL divergence. 
  - Student loss is then the weighted average of the original (task-dependent) loss with ground truth labels, and the knowledge distillation loss. 
- Student model should ideally by the smaller variant of the teacher pretrained model. 


## KL Divergence
- $D_{KL} = \sum_{i}^{V}T_i\log(\frac{T_i}{S_i})$, where: 
  - $V$ is the vocab size (or truncated vocab size), 
  - $T_i$ is the softened teacher probability for $i^{th}$ token, 
  - $S_i$ is the softened student probability for $i^{th}$ token. 