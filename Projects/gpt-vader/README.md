# GPT-Vader Training Stats

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