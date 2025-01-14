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

- *Research literature*

- *Experiment design*

- *Model evaluation*

- *Dealing with uncertainty*

- *Real-world experimentation*

- *Debugging and interpreting results*

- *Collaboration and communication*

- *Ethical considerations*