# Retrieval Augmented Generation for SRE Chatbot

## Summary
- *Situation*:
  - At JPMorgan Chase's Data & Analytics team, I worked on building a firmwide SRE-focused Retrieval-Augmented Generation chatbot. 
  - Analysis of historical SRE incident tickets identified that ~20% were 'information-only', where responses could be automated using our internal knowledge base. The business objectives were to reduce ticket generation by at least 15% and decrease incident resolution times by 10%. 
  - Key challenges include integrating multiple internal data sources, meeting strict latency requirements, evaluating large language models, and establishing user trust in chatbot responses.  

- *Task*: 
  - Lead the project from a data science perspective while contributing significantly to engineering efforts. 
  - Developed critical modules: data extraction and preprocessing, an AWS Lambda-based automated data pipeline, model selection and embedding generation with a fine-tuned Encoder embedding model, Opensearch Retriever, a low-latency statistical Re-ranker, and comprehensive evaluation of RAG components. 
  - Defined key metrics across data pipeline efficiency, retrieval and ranking performance, LLM reliability, and overall system scalability and uptime. 

- *Action*: 
  - Engineered a reliable data scraper within our private cloud, interfacing with APIs from StackOverflow, Confluence, Jira, ServiceNow, GitHub, and Bitbucket. Implemented a scheduler for automatic data refreshing and threshold-based data retention.
  - Preprocessed data by redacting PII, performing OCR, and eliminating machine-generated text. Employed token-based chunking strategies tailored for both Retriever and Reader models.
  - Developed AWS Lambda functions to generate title-weighted vector embeddings using a fine-tuned sentence-transformer model with triplet loss, storing embeddings in AWS OpenSearch for efficient KNN search.
  - Created a statistical re-ranker that combines outlier detection with document frequency analysis to refine the top-k retrieval results, ensuring high relevance and low latency.
  - Integrated LLM (GPT endpoint) with context from retrieved documents and fine-tuned prompts, while implementing guardrails to mitigate hallucinations and irrelevant responses.
  - Led ongoing evaluations using a curated ground truth library, iterating on model and system improvements based on performance metrics and user feedback.

- *Results*:
  - Achieved a 21% reduction in generated tickets post-deployment, surpassing the 15% target, with ongoing surveys to attribute reductions specifically to chatbot usage.
  - Secured a 75% positive user feedback rate through upvote interactions.
  - Integrated the chatbot API with both the UI and incident management tools like ServiceNow and Jira, leading to an over 18% decrease in incident resolution times as users autonomously resolved tickets using auto-generated responses.
-------

## Deep Dive

- **Latency considerations**
  - Round-trip constraint: 2-3 secs.
  - AWS opensearch for vector DB, with approximate KNN search. 
  - FAQ matcher. 
  - Fast statistical re-ranker. 
  - GPU-enabled Sagemaker endpoints. 

- **Data Pipeline**
  - Parameters:
    - Token-based chunk size based on embedding model max context length, 
    - Embedding pretrained model selection, 
    - Fine tuning loss function and hyperparameters (learning rate, batch size, epochs, optimizer). 
  - Metrics: 
    - Average number of chunks per doc, 
    - Distribution of tokens per chunk, 
    - Fraction of docs with embeddings generated, 
    - Out-of-vocab tokens for both language models,
    - Fine-tuning training and validation loss, cosine sim from anchors, recall@k and mrr@k when run with retriever. 
    - Embedding generation latency and resource utilization.   

- **FAQ Router**
  - ?

- **Statistical Reranker**
  - Anomaly detection with MAD, 

- **Embedding Model Fine-Tuning**
  - Hyperparameters:
    - Number of layers frozen, 
    - Learning rate, 
    - Quantization, 
    - Loss function, 
    - Optimizer, 

- **Retriever & Re-ranker**
  - Parameters:
    - Number of top-k to retrieve based on llm max context length, 
    - Vector db KNN search method and distance metric, 
    - Standard deviation thresholding for re-ranker, 
    - FAQ matcher. 
  - Metrics: 
    - Recall@k, MRR@k, 
    - Search latency and throughput. 

- **LLM**
  - Parameters:
    - Model selection, 
    - Temperature, 
    - Top-p nucleus sampling, 
    - Max output tokens, 
    - Guardrails,
  - Metrics: 
    - Cosine similarity scores with golden dataset, 
    - Word overlap: Exact match, BLEU and ROGUE evaluated but not used, 
    - Latency and throughput, 
    - Number of tokens generated, 
    - Cost per interaction, 
    - Fraction of queries blocked by guardrails, 
    - Guardrail accuracy. 

- **System**
  - Metrics: 
    - Upvote feedback, 
    - Click rate for reference urls, 
    - Total latency and throughput, 
    - Usage metrics, 
    - App uptime. 