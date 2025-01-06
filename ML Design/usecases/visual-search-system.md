# [Visual Search System](https://bytebytego.com/courses/machine-learning-system-design-interview/visual-search-system)

## Problem Statement
A system helps users discover images that are visually similar to a selected image. In this chapter, we design a visual search system similar to Pinterest’s. 


## Clarifying Requirements
- What are the business metrics that need to be achieved?
  - Positive feedback from user leading to higher click through rate. 
  - Higher engagement time on the app/website. 
  - Higher sales for recommended similar products. 

- What are the product features?
  - User can crop the image and then search for similar results. 
  - Results shown in new window or same. 
  - How much data shown to the user for the similar products without actively navigating to the dedicated page for the similar product. 
  - Constraints on how large the image can be for searching (resolution, size, etc.). 
  - What image/product features should be considered when doing a similarity search.
  - After showing the results, would the user have the ability to re-sort or filter them. 
  - Will user data be used/stored for the search. 
  - SLA for the search, factoring in higher traffic times. 
  - User feedback collection. 

*Let’s summarize the problem statement. We are asked to design a visual search system. The system retrieves images similar to the query image provided by the user, ranks them based on their similarities to the query image, and then displays them to the user. The platform only supports images, with no video or text queries allowed. For simplicity, no personalization is required.*


## ML Formulation
- ML objective is to do an image similarity search, and rank the top-k results. 
  - Input is color image pixels (any size). 
  - Output is a list of k image references, sorted in decreasing order of relevance. 

- ML techniques:
  - Simple (baseline): Use image pixels as baselines for feature comparisons. Use greyscale images. No ML training. 
  - Simple (should not implement): Handcraft image features using traditional image processing techniques such as with openCV image transformations. 
  - Moderate: Use a CNN to train the image corpus (using product types as lebels) for a classification task, and obtain the class-specific feature vectors. 
    - Use the user image to create its feature vector, and do a similarity search with corpus feature vectors. 
  - Complex: Create image embeddings, and use a vector database to search and sort the image corpus. 
    - Image embeddings can be created by transforming the image pixels to dense vector representations using attention-based deep neural net models. 

- Metrics: 
  - Accuracy of top-k detection, Mean Reciprocal Rank. 
  - Image similarity defined by metrics: cosine similarity (for dense representations), euclidean distance, etc. 
  - Business metrics mentioned above: user feedback, user engagement time, click through rate, sales for recommended products. 


## Data Preprocessing
- Offline (ml training): 
  - Preprocess the corpus images (size standardization), data augmentations such as shifts, crops, rotations - especially aligning with real user cropping behaviors. 
    - Enhance poor quality images with denoising. 
  - Label images with products: use already-available tags for images + additional manual or ml incremental labeling. 
  - Segmentation to increase labeled dataset. 
  - EDA to check for class imbalance, image quality. Also analyze image metadata to look for things like label redundancy. 
  - Split to train, valid, test datasets. 
  - Offload to vector db with a refresh frequency. Tag with class names. 

- Online (ml inference): 
  - Once the user selects or crops an image to initiate the similarity search, the input image goes through following steps: image standardization (normalize the size), embedding/feature vector generation. 
  - Use vector db to do the search and retrieve the top-k results, along with associated probabilities. 
  - Also store image metadata (such as user feedback) for offline model improvements. 


## Modeling
- Model selection: 
  - With the CNN approach, do model selection (VGG16, VGG19, ResNet). RetinaNet is a CNN implementation which includes segmentation as well, so might be a good candidate. 
  - Check baselines, and incrementally add model capacity. 
  - For the embeddings apporach, check recent literature on how image pixels can be transformed to a dense vector representation using attention networks (only if our corpus training data is large). 
  - Bias vs. variance: More complex models might be more accurate but might overfit, less generalizable, and less explainable. CNN is more mature tech than attention networks, and hence might be a good idea to go with that if the accuracy improvement for attention is not significant. 
  - Transfer learning. 
  - Tradeoffs for latency vs accuracy (CNNs vs transformers). 
    - Building retrieval based models or distillation to fine-tune for lower latency. 

- Model assumptions: 
  - Output features have enough separation for a good classification downstream - check with PCA and do feature visualization. 
  - Class labels are sufficient and accurate - check with SMEs, and do A/B testing with test users. 
  - Model separates the classes sufficiently - check model output probability distributions. 

- Hyperparameters: 
  - Multi-class classification problem: Use softmax as the activation function, cross-entropy as the loss, ReLU to include non-linearity, and Adam as the optimizer. 
  - Start with a shallow network, and increase model capacity incrementally, keeping an eye on overfitting. 
  - Regularize with loss function modifications (l1, l2), network modifications (dropouts), and data regularizations (augmentation). 
  - Tune hyperparameters (grid-search, random) using the validation set. 

- Exploitation vs. Exploration:
  - Hyperparameter tuning: proven hyperparameters from paper vs. random over grid search
  - Diversity in dataset for training: keeping feature imbalance for higher accuracy vs. data augmentations for better generalization
  - Model architecture selection: proven best architectures from papers vs. experimentation on own dataset. 
    - Separate models for difficult classes. 
  - Diversity in search space to improve user engagement and avoid repetitive results. 
    - Multi-modal embeddings (combining metadata or text features when available) to enhance relevance. 
    - Sample from output distribution instead of taking the top-matched result. 

- Good vs. Useful model:
  - During validation, also always compute business metrics: top-k accuracy and MRR. 
  - Track inference latency (with buffer), and compare with SLAs. 


## Evaluation
- ML metrics: 
  - Train/valid losses, prediction accuracy, f1-score (macro, micro, per-class). 
  - Top-k accuracy, MRR. 
- Engineering metrics:
  - Inference latency given throughput.
  - Inference $ cost. 
- Business metrics:
  - A/B testing on a canary release: click through rate, revenue increase.
- Fairness metrics:
  - Per-class F1 score. 
  - Potential biases: representation across popular and less popular categories to avoid model overfitting. 
- Other considerations:
  - Degenrative feedback loop: popular products get more usage with visual search, increasing its revenue and amount of training data, which might bias the model. 
  - Interpretability: input masking for CNNs, Grad-CAM/SHAP for CNNs to help visualize what the model "sees". 


## Deployment
- Offline:
  - Distributed ML training on GPU clusters with batching and gradient accumulation. 
  - Data storage classes - bronze, silver, gold - for data versioning and tracking. 
  - Experiment tracking with mlflow. 
  - Data refresh and model update frequency and pipelines. 

- Online:
  - Model compression: distillation, pruning, low-rank optimization, quantization, compilation. 
  - Distributed/parallelized inference with horizontal scaling on cloud. 
  - Caching for frequenctly searched images to reduce load on vector database and ensuring faster response. 
  - Model monitoring: track data and output probability distributions. 
  - Re-ranking and filtering output with business logic/priorities.
  - Approximate Nearest Neighbor (ANN) service: instead of exact cosine sim matches, we approximate due to large amount of corpus data. 
    - Use clustering/tagging and reduce search space. 
  - Incremental model (re-)training and feedback loop. 