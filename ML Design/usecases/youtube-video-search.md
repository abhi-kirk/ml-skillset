# [Youtube Video Search](https://bytebytego.com/courses/machine-learning-system-design-interview/youtube-video-search)

## Problem Statement
Design a search system for videos. Input is text query, and output is a list of videos that are most relevant to the query. We can leverage video text and content data. No user personalization is required. 

## Clarifying Requirements
- How many results to show the user?
- Can the user apply filters to their search?
  - Video length, category, posted date, number of likes, channel subscriptions
- Latency requirements
- Does the user needs to be logged in to the system to search?
- Data access
  - User's search history + any feedback (specifc to content search)
  - Video DB + video attributes
- Business metrics:
  - overall click-through rate, post-search click-through rate, view times, ad revenue, overall time the user spends on the site

## ML Formulation
- A Learning to Rank problem, where the input is user query, and the output is a ranked list sorted in order of decreasing relevance to the query. 
- Inputs: user query text, video db (including all attributes such as video length, channel subscribers, number of likes, video category), user applied filters. 
- Outputs: ranked list of videos (+ corresponding match scores) for the UI to display. 
- ML architecture:
  - LTR with XGBoost or Neural Nets (pairwise embedding samples as inputs, Retrieval with a vector DB, and rank prediction as output)
  - Create and use graph-based algorithms by creating + updating embeddings for user and video features. 
- ML Metrics: 
  - MRR@k, Recall@k, Precision@k, MAP, Final loss value (when using NNs), nDCG score. 

## Data Preprocessing
- Data pipeline
  - ML training: 
    - 