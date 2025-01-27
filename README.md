# ML Research Method

- *Problem formulation*
  - Business metrics to ML metrics. 
  - Managing expectations. 

- *Research literature*
  - Benchmark with hyperparameters from papers, and then improve. 
  - Correlate type, quality and quantity of data used with published performance metrics. 

- *Experiment design*
  - Simple to complex models, evaluating with metrics and trade-offs at each step. 
  - Not to over-engineer designs by adding unnecessary complexity. 
  - Keeping engineering, scalability and safety (if applicable) in mind. 

- *Model evaluation*
  - Both ML and business metrics. 
  - Track data, models and results. 

- *Dealing with uncertainty*
  - Augment training data to real-world conditions. 
  - Split into training, validation and testing datasets. Validation data used for hyperparameter tuning, and testing data rarely evaluated to avoid bias. 

- *Real-world experimentation*
  - A/B tests when possible. 
  - Canary releases before full prod. 
  - Model monitoring including data drift. 

- *Debugging and interpreting results*
  - Feature importance using perturbation analysis, or decision tree splits, or hypothesis testing. 
  - Visualize higher dimension data in lower ddimensions using UMAP. 
  - Statistical analysis where possible (linear models). 

- *Collaboration and communication*
  - Different but accurate explanations for different audiences. 
  - Ask for help when stuck or unsure. 

- *Ethical considerations*
  - Fairness and bias in training data. 
  - Transparency and explainability. 
  - Privacy and security, regulatory compliance. 
  - Impact to society. 


# Books

| Name                                     | Type       | Author           |
| ---------------------------------------- | ---------- | ---------------- |
| Designing Data Intensive Applications    | Software   | Martin Kleppmann |
| System Design Interview                  | Software   | Alex Xu          |
| System Design Interview Vol.2            | Software   | Alex Xu          |
| Graph Databases in Action                | Graph      | Dave Bechberger  |
| Practical Natural Language Processing    | ML         | Sowmya Vajjala   |
| Practical Gremlin                        | Graph      | Kelvin Lawrence  |
| Hands-On ML with SKLearn and Tensorflow  | ML         | Aurelien Geron   |
| Staff Engineer                           | Leadership | Will Larson      |
| NLP with Transformers                    | ML         | Lewis Tunstall   |
| An Introduction to Statistical Learning  | ML         | Gareth James     |
| Designing ML Systems                     | ML         | Chip Huyen       |
| Thinking Fast and Slow                   | Leadership | Daniel Kahneman  |
| SRE - How Google Runs Production Systems | Software   | Betsy Beyer      |


# Papers

| ML Area          | Year | Title                                                                                                                                                                     | Author/Institution  | Tech                              |
| ---------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------- |
| Clustering       | 1996 | [DBSCAN](https://file.biolab.si/papers/1996-DBSCAN-KDD.pdf)                                                                                                               | Ester et. al        | Density-based Clustering          |
| NLP              | 2003 | [A Neural Probabilistic Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)                                                                      | Bengio et. al       | MLP                               |
| Clustering       | 2013 | [HDBSCAN](https://github.com/vatika/Algorithm-Name-Detection/blob/master/big_dataset/Density-Based%20Clustering%20based%20on%20Hierarchical%20Density%20Estimates.pdf)    | Campella et. al     | Density-based Clustering          |
| DL               | 2015 | [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385)                                                                                          | Kaiming et. al      | Skip Connections                  |
| DL               | 2015 | [Delving Deep into Rectifiers](https://arxiv.org/pdf/1502.01852)                                                                                                          | Kaiming et. al      | ReLU, Weight Initialization       |
| CNN              | 2015 | [Very Deep Convolutional Networks for Large Scale Image Recognition](https://arxiv.org/pdf/1409.1556)                                                                     | Oxford              | VGG-16                            |
| NLP              | 2016 | [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/pdf/1508.07909)                                                                           | Sennrich et. al     | BPE                               |
| NLP              | 2017 | [Attention is All You Need](https://arxiv.org/pdf/1706.03762)                                                                                                             | Google Brain        | Transformer                       |
| CNN              | 2018 | [Focal Loss for Dense Object Detection](https://arxiv.org/pdf/1708.02002)                                                                                                 | Facebook AI         | RetinaNet - CNN with Segmentation |
| NLP              | 2018 | [Universal Language Model Fine-Tuning for Text Classification](https://arxiv.org/pdf/1801.06146)                                                                          | Howard et. al       | ULMFiT                            |
| NLP              | 2018 | [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)              | OpenAI              | GPT-1                             |
| NLP              | 2019 | [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | OpenAI              | GPT-2                             |
| NLP              | 2019 | [BERT](https://arxiv.org/pdf/1810.04805)                                                                                                                                  | Google              | BERT                              |
| NLP              | 2020 | [Language Models are Few Shot Learners](https://arxiv.org/pdf/2005.14165)                                                                                                 | OpenAI              | GPT-3                             |
| NLP              | 2022 | [Efficient Training of Language Models to Fill in the Middle](https://arxiv.org/pdf/2207.14255)                                                                           | OpenAI              | GPT-4 FIL Special Token           |
| Knowledge Graphs | 2022 | [Mining Root Cause Knowledge Graph from Cloud Service Incident Investigation for AIOps](https://arxiv.org/pdf/2204.11598)                                                 | Salesforce Research | RCA with Knowledge Graphs         |
| NLP              | 2023 | [SolidGoldMagikarp](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation)                                                           | Rumbelow et. al     | Tokenization Issues (GPT-2)       |
| NLP              | 2024 | [Apple Intelligence Foundation Language Models](https://arxiv.org/pdf/2407.21075)                                                                                         | Apple               | Apple LLMs                        |