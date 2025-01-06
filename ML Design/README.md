# ML Design Template

## Clarifying requirements 
- Business objectives + metrics
- Product features 
- Data access/availability + scale
- Performance constraints 
- Privacy / Regulatory

## ML formulation / High Level Design
- Business -> ML objectives -> ML category
- ML Input/output
- ML architecture (binary / multi-class / multi-label / cascade)
  - Baseline -> Simple ML -> Complex ML
- ML Metrics (including user feedback)

## Data preprocessing 
- Data engineering (ETL, dtypes, formats)
    - data pipelines (schema, storage)
    - data extraction, structuring, transformations, cleaning
- Feature generation + balancing + splits + labeling + sampling
    - training data patterns/distributions should match inference data patterns/distributions
    - labeling: quantify accuracy, check feedback loop length, perturbation stability, auto-labeling 
    - feature distribution across classes
- Data leakage
    - scaling, oversampling and inputing data before splits can cause data leakage
    - hyperparameter tuning based on testing results
    - detection: feature importance wrt each class
- Privacy + biases
- Robustness to upstream 

## Modeling 
- General approach:
    - step 1: create baselines without ML (using heuristics / rules / random / existing / human)
    - step 2: simplest ml models
    - step 3: optimize simple ml models
    - step 4: complex models
- Model selection: Simple baseline -> complex
    - bias vs. variance, explainability, incremental improvements
    - model assumptions
    - ensembles
    - experiment tracking with data versioning, hyperparameters & output metrics (system, business, performance)
- Training details
    - objective / loss functions (+handling multiple objectives, regularization)
    - exploitation vs. exploration
    - overfit a single batch first
    - grid search for hyperparameters
- “good” vs ”useful” model
- Several models for different tasks instead of a single model for all tasks
- **NeuralNet specific (can fail silently)**:
    1. data: 
        - inspect random sample of raw data manually
        - look at distributions
        - label accuracy/noise
    2. baselines: 
        - setup full training + eval pipeline and experiment with simple models
        - fix random seed
        - turn off data augmentation
        - verify loss @ init
        - init weights well
        - baseline interpretable metrics
        - zero-input and human baselines
        - overfit one batch
        - increase model capacity incrementally to see loss decreasing
        - verify data just before the net
        - visualize prediction dynamics on a single test batch over the training run to reveal instabilities
        - check data leakage: set loss dependent on only a single sample and check gradients
        - in code, brute force functionality first before vectorizing
    3. modeling:
        - start with a well-established model from papers
        - use adam for optimizer with a constant learning rate
        - incrementally increase data/signal complexity to the model
    4. regularize:
        - get more data (raw / data augmentation / simulated or generated data)
        - use pretrained nets
        - stick to supervised learning
        - reduce number of features
        - decrease batch size
        - dropouts
        - weight decay penalty
        - early stopping (esp. with larger models)
        - visualize first layer weights (should not look like noise)
    5. tune:
        - random over grid search
        - hyper-parameter optimization
        - model ensembles
        - knowledge distillation
        - keep training even after loss levels off

## Evaluation 
- Offline + online + fairness/bias
    - cross-validation
- Perturbation testing (adding noise to simulate real-world scenarios)
- Invariance testing (certain inputs shouldn’t lead to changes in outputs, e.g. to check biases)
- Interpretability
- Statistical significance of model parameters (if possible)
- Evaluating model performance on different data groups/subsets (e.g. to check fairness)
- Degenerative feedback loops (when model predictions affect training data inputs which affect model predictions)
- Alternative ML models

## Deployment
- Cloud/on-prem
    - latency vs. throughput
    - real-time vs. batched/queued
- Model compression: distillation, pruning, quantization, low-rank optimization, compilation
- Inference infrastructure: auto-scaling, distributed serving
- Testing for change management 
    - shadow deployment & A/B testing
    - canary release
- Continued/online/incremental learning
- Model monitoring, data distribution monitoring
    - feature validation
- ML system maintenance, SRE
- Data, features and model updates - frequency and method
    - train model on data from different time periods to see performance change / improvements
    - scheduler
