# Incident Root-Cause Search Engine

## Summary
- *Situation*:
  - As a Machine Learning Engineer at JPMorgan Chase, I worked on an SRE incident root-cause search engine. 
  - Our existing incident search engine only does TF-IDF based query-to-historical incident matching based on the BM25 algorithm. It does not take into account query/incident context, and also does not assist with finding the issue root-cause. 
  - The business objectives were to enhance this search engine to address these drawbacks by reducing incident resolution times by at least 10%. 
  - Currently this product is in UAT testing by SMEs. 

- *Task*:
  - Leading the project from the data science aspect, while keeping engineering resource constrainsts in mind. 
  - Developed modules: incident data extraction, text preprocessing and embedding generation. As a first step, developed a retriever-only solution to generate semantic similarity based search results. 
  - As step 2, I developed a more complete search engine pipeline by enhancing the retrieval process using a graph neural net, and then leveraging Learning To Rank methods to fine-tune the final ranked list displayed to the user. 
  - Ranking metrics such as MAP@k, MRR@k and NDCG@k are used throughout to make sure improvements in all metrics can be quantified with every step. 

- *Action*: 
  - Incident data is extracted from ServiceNow and Jira incident management systems using their respective APIs, and is first preprocessed to remove PII, machine generated text, etc. 
  - Symptoms and Root-Causes from each incident text are extracted using a generative language model. An embedding model then created embeddings for both, for each ticket. 
  - Symptom- and RootCause-clusters are then created separately using KMeans clustering using cosine distance metric. An incident graph is built from these nodes, and embeddings updated using the GraphSAGE algorithm for the link prediction task between symptom and root-cause nodes. Cross-entropy loss is used for the binary classification problem with positive and negative samples. 
  - Rankings from both the embedding-match retriever, and the more complex GNN-based retriever are combined using a weighted average (weights determined from their respective MRR@20 performance metric). 
  - XGBoost Learning to Rank, with pairwise contrastive loss, is used to re-rank the retriever rankings by using various categorical and numerical features extracted from the user query text and incident ticket.
  - Incident graph visualization developed with Plotly-Dash to provide further incident insights to SREs. 

- *Results*: 
  - Still in user-acceptance testing with SRE SMEs. 
  - Testing using held-out data show >30% improvement in ranking metrics over the keyword-match approach. This should translate to better incident resolution times. 
  - GNN inference latency is an ongoing challenge. 

---------------

# Deep-Dive
