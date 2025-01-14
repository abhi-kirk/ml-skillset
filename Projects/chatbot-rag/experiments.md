# Experiments for Chatbot-RAG

## EDA
- Distribution of chunk sizes (markdown header vs additional token based chunking)

## Embedding model selection
- Models considered: OpenAI, FlagEmbedding, BERT
- Evaluation: 
  - public benchmarks
  - retrieval performance on JPMC docs; metrics used: MRR, accuracy
  - engineering metrics: ease of use and fine-tuning, cost

## Fine-Tuning Embedding model
- The bge-large FlagEmbedding model has 24 transformer blocks. We froze the embedding layer, as well as the top 12 layers and fine-tuned the rest. 
- Triplet loss is used with appropriately labeled custom data (5000 samples). 
  - Hard negative mining is used for (anchor, negative) pairs. 
  - Also experimented with constrastive loss and Maytroshka loss. 

## LLM model selection
- Models considered: 
  - Open source: Falcon, Llama, Mistral
    - Llama: Research-oriented but open-source. Limited context window. 
    - Mistral: Efficiency and performance at smaller scale. Also open-source. Limited model sizes and context window. 
    - Falcon: Small context window. 
  - Commercial: GPT, Claude
    - High cost. 


## Research Method

- *Problem formulation*
  - Analysis on historical tickets: SRE business metrics
  - RAG system with local models, then endpoint

- *Research literature*
  - Local LLM models: Falcon, Mistral, Llama
  - Vector DBs: understanding how indexing works with ANN
  - LLM concepts from seminal papers

- *Experiment design*
  - Data preprocessing: cleaning, chunking
  - Retriever parameters experiments: k, distance metric
  - Reranker
  - Title-weighted embeddings
  - LLM guardrails

- *Model evaluation*
  - Separate retriever and reader metrics
  - Business metrics

- *Dealing with uncertainty*
  - Thorough golden dataset for testing across teams
  - Robust cloud infrastructure
  - Including diverse data in fine-tuning dataset

- *Real-world experimentation*
  - Canary release before large-scale prod
  - Incorporating feedback from users

- *Debugging and interpreting results*
  - 

- *Collaboration and communication*

- *Ethical considerations*