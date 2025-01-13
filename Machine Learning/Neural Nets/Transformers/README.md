# Transformers

## Architecture
- Input is a stream of tokens, and output is generative text, in the form of one token at a time. 
- Attention mechanism (using multi-header self-attention blocks) produces embeddings for each input token.
  - This mechanism allows the transformer to communicate contextual meaning across tokens, by assigning different amount of weight or "attention" to each token in the sequence and then averaging.  
  - Positional embeddings (dimension is equal to context length) are added to token embeddings. 
- A fully-connected neural net head is then used for predicting the next token. 
  - This mechanism allows the transformer to think and produce output. 
- Architectures:
  - For an encoder architecture, the attention mechanism has access to both past and future tokens. 
    - Models: BERT and embedding models. 
    - Tasks: Summarization, NER. 
    - Benchmarks: STS (Semantic Textual Similarity), SNLI (Stanford Natural Language Inference dataset), SentEval ()
  - For a decoder architecture, the attention mechanism has access to only the past tokens. 
    - Models: GPT, Llama, Mistral. 
    - Tasks: Generative text. 
    - Benchmarks: 
  - For an encoder-decoder architecture, the K and V weights are communicated from the encoder to decoder. 
    - Models: T5, BART. 
    - Tasks: Language translation. 
    - Benchmarks: 

## Transformer Challenges
- Mostly trained with English text
- Large amounts of data required to train/fine-tune; also costly
- Context length limitation
- Very low explainability; hallucinations
- Data bias