# Experiments for GPT-Vader Pretraining

## EDA
- Fraction of text as Markdown tables. 
- Distribution of data across various teams and products. 
- 

## GPT-Vader Training Stats
- **Data**: JPMC Confluence data extracted from Confluence Cloud API as Markdown files (16 GB compressed text). 
  - Number of unique non-zero length Confluence spaces: ~33K. 
  - Total number of documents: ~4M with a total of ~178B total unicode characters. 

- **Tokenizer**: Byte-Pair Encoding (BPE) with `<|endoftext|>` special token to separate docs. 
  - Custom BPE tokenizer trained with vocab size: 32K. 
  - Total number of tokens: ~5B. 
  - Compression ratio: 3.34. 

- **LLM Pre-Training**: Decoder Transformer with Multi-Headed Self-Attention. 
  - Embedding size: 768. 
  - Max context length: 1024 tokens. 
  - Number of Transformer blocks = Number of Self-Attention heads = 12. 
  - Total number of LLM parameters: 124M (same as GPT-2 med/large). 
  - Compute used: 8x A10 NVIDIA GPUs. 
  - Number of iterations: 20K (resulting in 1.2 sec/iteration). 
  - BERTScore F1 for last model checkpoint: 0.65, on 50 JPMC-specific QA-pairs, as compared to 0.4 for GPT-3.5. 


## Research Method

- *Problem formulation*
  - Understanding LLM and Transformer technology (and challenges) with pretraining

- *Research literature*
  - Seminal papers on Transformers and GPT

- *Experiment design*
  - Confluence data extraction, EDA, preprocessing, storage and splits
  - Selecting hyperparameters for tokenizer and LLM from GPT-2 paper
  - Analyzing transformer architecture for GPT-2
  - Setting up training pipeline with various optimizations for GPU runs

- *Model evaluation*
  - BERTScore F1 for GPT-Vader vs. GPT-2 on JPMC-specific reference data

- *Dealing with uncertainty*
  - Experiments with probabilistic LLM sampling strategies

- *Real-world experimentation*
  - Decoding methods: greedy, beam-search with various sampling methods (top0k, nucleus)
  - Feedback from real users

- *Debugging and interpreting results*
  - Error analysis: revealed significant markdown formatting introducing noise
  - Analyzing tokenizer vocabulary
  - Visualize embeddings by reducing them into 2D with UMAP. 

- *Collaboration and communication*
  - Explaining methodology to team, and incorporating feedback
  - Tracking experimentation and results with comet-ml (similar to mlflow)
  - Documentation

- *Ethical considerations*
  - Removal of PII and toxic data as a preprocessing step
  - Can implement LLM guardrails if project taken forward