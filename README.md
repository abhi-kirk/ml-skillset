# Research Method

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