# Defect Classifier for Gorilla Glass

## Summary
- *Situation*: 
  - At Corning, I worked on building a defect classification system for Gorilla glass inspection lines. 
  - The existing rules-based system led to high false negatives, increasing manual inspection hours and customer complaints. 
  - Hence the business objective was to reduce the manual inspection hours by at least 50%, and customer complaints by >10% over a one-year period. 
  - Engineering goals included <10ms inference latency per inference call, seamless vendor integration, and non-disruptive deployment. 

- *Task*: 
  - I lead this project for the data science aspect, focusing on developing a CNN-based classification system to replace the rules-based approach. 
  - I was responsible for developing the ML model, including all data preprocessing, feature engineering, and model development. 
  - Key classification metrics included high recall for critical defect classes, f1-score for class balance, and AUC-ROC for threshold optimization. 
  - While deployment was lead by sennior software engineers, I assisted in software-related tasks such as integrating the model into the vendor system. 

- *Action*: 
  - I began by gathering defect image data from the inspection system and performend image preprocessing, including normalization and resizing. 
  - To address class imbalance, I implemented data augmentation techniques for undersampled defect categories. 
  - Labels were curated using a combination of manual review and outputs from the rules-based classifier. 
  - After evaluating several CNN architectures, I chose VGG-19 for its strong accuracy on similar image classification tasks and low inference latency. 
  - For deployment, I collaborated with senior engieers to wrap the tensorflow model in C# for seamless integration with vendor inspection software. My contributions included ensuring the ML pipeline adhered to deployment latency constrainsts and validating the model's performance in production-like environments. 

- *Results*: 
  - The system achieved >98% recall for critical defect classes, and significantly improved the overall f1-score across all classes. 
  - As a result of automatic feature extraction by deep learning, classifier development time was reduced by 75%. 
  - Manual inspection hours were reduced by >60%, and customer complaints decreased by 15%. 
  - The model integrated seamlessly into the existing inspection system. 
  - I contributed to stakeholder confidence by implementing CNN image masking to improve model explainability. 

-----------

## Deep Dive
- **Business Goals: Articulate how the problem was framed in terms of business objectives (e.g., reducing manual inspection costs and customer complaints).**
  - The existing rules-based system involved several manual steps, including creating and maintaining the complex decision tree of rules, feature extraction using classical image processing. Although the inference latency was fast, this system did not produce good accuracy results in terms of recall for critical defects. Hence, several manual inspection steps needed to be performed:
    - Several operators would analyze the incoming images from the glass manually, and provide classification for most defect images, across 20+ classes. 
    - A sample of glass sheets undergo a final post-wash manual inspection where the glass is inspected in a dark room individually to judge the entire batch. 
  - Corning had very little margin of error for high-profile customers such as Apple, and hence even after a thorough manual review, customer complaints on glass quality were unacceptable. 

- **Engineering Constraints: Address latency requirements, integration challenges, and operational reliability.**
  - Since the conveyer belt keeps moving when the glass is being inspected, it is critical to classify the defects, if any, under a strict 10ms latency limit. This latency limit includes communication of binary data (images, defect category, metadata) from and to the vendor equipment, as well as the classification time. 
  - Integration challenges included:    
    - Offline inspection system due to security reasons (hence, no cloud or even remote access). 
    - Strong preference for C\# to be used for deployment for long-term maintainability since that was the standard at the inspection sites. 
    - Limited downtime availability to conduct integration experiments and test-runs. 

- **Data Collection: How was the data collected from the vision system? Challenges in data acquisition, such as volume, quality, or format.**
  - Images from the vision system were stored as files in a windows file system. 
  - A data pipeline was created so that these images will automatically be copied over to a postgresql db to be stored as blobs including their metadata such as timestamp, dimensions, glass type, classification from the rules-classifier, etc. 
    - This was done for data retention and versioning. 

- **Data Labeling: How were labels generated and verified (e.g., using the rules-based system)? Steps taken to ensure label quality and avoid biases.**
  - Labels were generated from a mix of manual labeling bootstrapped with rules-classifier predictions, as well as incrementally training the CNN classifier on increasing quantities of data.
  - To ensure label quality, all images used in the training set undergo an independent review from one of the line operators who are considered SMEs. 
  - For lines where cold-start was an issue, the CNN is trained incrementally as new data comes in, and is verified. 
  - Oversampling techniques such as the SMOTE algorithm is used to oversample on the feature space. Data augmentations, such as rotation, flips, blur, are also used to augment undersampled classes. 
    - Experiments are also done using class weights instead of over/undersampling the data, but it is observed that data augmentation is a better approach, as judged by the downstream ML metrics. 

- **Data Preprocessing: Normalization, resizing, and pixel standardization techniques. Handling missing data or noise in the defect images.**
  - All images are converted to greyscale, and downsized to 256x256 pixels. This is done to reduce computational cost (moreover, CNNs can only handle fixed size inputs). The images are also normalized to a zero mean and unit variance pixel values. 
  - For this use-case, noisy images can be divided into two categories:
    - The defect class is ambiguous. In this case, a SME is consulted along with analyzing image metadata to create hard samples for training. If the label is still ambiguous, the sample is ignored. 
    - Other artifacts are present in the image alongside the actual defect. I use a balance of intentionally including noise patterns and removal of noise artifacts using image processing, to make sure that the noise distribution is uniform across classes. I make sure that distribution is consistent in the training and validation splits. 
    - I remove batch-specific or background-specific features from images to avoid the CNN learning from them. 

- **Feature Engineering and Augmentation:**
  - Keras library is used to automatically augment a fraction of images (rotate, zoom, crop) randomly for every batch size. 
  - To catch corner cases for extremely undersampled classes, I create a cascade system, where if the classified prediction belongs to a predetermined set, a secondary image processing module will look for very specific patterns in these images to optionally overrule the prediction as a new defect class. Note that this new defect class is the extremely undersampled class and is not used in training the CNN. 
  
- **Usage of SMOTE:**
  - After training the CNN, we treat the convolutional blocks as a feature extractor. Each image is passed through the CNN’s convolutional layers to produce a final feature vector (for example, a flattened output from the last convolutional layer or a fully-connected layer before the final classification layer). These feature vectors form a tabular, numerical dataset, where each row corresponds to an image and each column to a learned feature. 
  - At this stage, the data is no longer in raw pixel form but is a set of extracted numerical embeddings. Since SMOTE operates on numeric, tabular data, applying SMOTE to these feature vectors is both appropriate and beneficial. 
  - We then train a Random Forest on the SMOTE-augmented feature set to classify defect types.
  - This approach leverages the CNN’s ability to learn complex, domain-specific representations while allowing classical oversampling techniques like SMOTE to handle class imbalance at the feature level, ultimately improving minority class recall and overall model robustness.

- **Model Selection: Why was VGG-19 chosen over alternatives like ResNet, Inception, or custom architectures? Trade-offs between performance, latency, and deployment requirements.**
  - From the results of various experiments on defect data, VGG19 offers a good balance between performance and latency. Models like AlexNet were not deep enough to enable enough model complexity (sufficient model complexity allows for extraction of a rich feature set, from edges to high-level representations), and more complex models like ResNet proved to easily overfit (as measured by a high training loss, and a low validation loss, relative to VGG-19) and hence seems to have larger training data requirements. 
    - Experiments show that even after implementing several ResNet regularization techniques such as batch norm, early stopping, learning rate scheduling, etc. overfitting seems to be unavoidable. It is hypothesized that this may be due to the feature space not being complex enough. 
  - VGG also has a straightforward design based on sequential convolutional layers and ReLU activations, making it easier to implement, debug and interpret. 
  - VGG weights are readily available (trained on ImageNet) which we use for transfer learning by freezing the first few layers. 
  - While VGG is inferior to ResNet or Inception on the latency front, we were able to use parallel and batch computing to keep our inference latency within good margins of the threshold. 
  - VGG is less computationally demanding than ResNet. 
  - A custom architecture is not built because of its high design and validation cost. 

- **Training and Optimization: Hyperparameter tuning methods (e.g., grid search, random search). Loss function choice and alignment with class imbalance. Handling overfitting (e.g., dropout, regularization).**
  - Using the well-studied hyperparameters given in the VGG-19 paper as the bound centers, I create baselines and then bootstrap random search to tune the hyperparameters. 
  - Categorical cross-entropy loss is used. Class imbalance is minimized as noted above with SMOTE and data augmentation techniques. 
  - Overfitting is handled with:
    - Having consistent data/feature distributions across the training and validation splits. 
    - Increasing dataset size. 
    - Early stopping. 
    - Decreased batch size. 
    - Dropouts. 
    - Weight decay with L2 regularization. 
    - Learning rate decay. 
    - k-fold Cross-validation. 
    - Post-feature training, switching the fully-connected layers for a random forest trained on the CNN-extracted features. 

- **Experiment Tracking: Tools or frameworks used for versioning and tracking experiments.**
  - After moving to Databricks for training, MLFlow was used for experiment tracking and model versioning. 
  - Data tracking and versioning was done with appropriate metadata tags in the postgresql DB. 

- **Alternative Modeling Approaches: Consideration of other solutions, such as unsupervised learning, transfer learning, or ensemble methods.**
  - Transfer learning is used from VGG-19 as noted above. 
  - The convolutional layers are cascaded with a RF classifier which improves overall overfitting, as well as F1-scores. Another cascade layer is for catching extremely undersampled classes using traditional image processing techniques. 
  - Since deployment requirements were strict (including no cloud access), ensemble methods are not used so as to keep the overall workflow simple.

- **Metrics and Validation: Why recall and F1-score were prioritized, and how thresholds were set using AUC curves. Cross-validation strategy and split methods. Techniques to evaluate model robustness (e.g., adversarial testing, invariance tests).**
  - For each of the critical defect classes (for which recall needs to be very high), we plot the AUC-ROC curve as critical class (positive) vs. rest of the classes (negative). Thresholds are optimized to maximize the TPR-FPR metric (specifically, reduce threshold to increase recall for critical classes).  
  - After doing data balancing, a random split of 80/20 is used. K-fold cross validation is used to check for overfitting. 
  - Further testing is done to check for reproducibility, robustness to noise, robustness to small changes in data distributions. 
    - Compare mean and standard deviation of output probabilities to baseline. 

- **Error Analysis: Analysis of misclassified images and corrective actions. Insights gained from confusion matrices and their impact on model improvement.**
  - Confusion matrices are used for error analysis of misclassified images, especially to identify classification overlaps. Corrective actions include:
    - Probability threshold tuning for critical classes using AUC-ROC curves. 
    - Improving data quality of sets of classes with most overlapped misclassifications. 
    - Checking for any patterns where further data augmentation can help (e.g. image rotation). 
    - Improving label quality with the help of SMEs.
  - Using the above approach, I was able to significantly improve the recall rate for critical defect classes during the testing phase of the project.  

- **Model Interpretability: CNN image masking: How it works, and how it built stakeholder trust.**
  - Used Saliency maps to compute relative importance of pixels for the predicted classification; displayed as a heatmap overlayed on top of the image. This pixel importance is created by sliding a mask on top of the image, executing inference for each mask position, and collecting probabilities for the actual predicted class. The intuition is that if the masked image area is important for correct classifictaion, the probabilities of this classification will drop due to the masking. 
  - At inference time, some manual inspection is still needed by an operator. The operator, for a small sample of classified images (still once/few seconds), is shown the saliency map overlayed on top of the classified image, for explanability and building confidence in predictions. 
  - Also helped in error analysis of neural nets and identifying misclassification issues. 

- **Deployment:** 
  - Model Compression:
    - Parallelized inference across 4 multi-core GPUs and efficient GPU memory management. 
    - Batch inference: several inference requests for the same image channel to a single GPU instance.  
    - Post-training quantization: FP16 Precision. 
    - Some model pruning: removing individual weights with the smallest magnitudes. 
  - Infrastructure and Tools: I assisted Senior Software Engineers in the team to create a C\# wrapper library for the tensorflow models, to be productionaized. This was necessary to build a real-time inference communication stream (using TCP/IP packets) between the inference GPU system and the vendor vision equipment. No cloud computing was available, hence, several workstations with NVIDIA GPUs were set up in the inspection room for CNN inference. Intelligent routing of incoming image data to different workstations, along with batch processing on GPUs and efficient GPU memory management allowed for low latency distributions, well within threshold. 
  - Testing and Validation: During the six month trial, the team chose daily scheduled times from 4 high-traffic and high-impact inspection lines, to enable the CNN classifier system. Metrics such as Recall and F1-score for critical classes, overall accuracy rate, and confusion matrix tracking were used to show classification improvements before and after the trial periods. Reduction in operator overrules metric helped us quantify the reduction in manual inspection hours. 
  - Monitoring and Maintenance: 
    - Dashboards were setup to monitor:
      - Volume of incoming data, 
      - Classification prediction class and probability distributions, 
      - Changes in line operating conditions, 
      - Inference times, 
      - Operator overrules, 
      - Periodic evaluation recall and f1-scores, 
      - Number of times rollback to rules-classifier was necessary due to any model or engineering issues with the classification system. 
    - For each Corning inspection site in Asia, I provided training classes to the plant personnel to:
      - Educate, at a high level, the basic functionality of the CNN system (i.e., why manual feature extraction is no longer needed), 
      - Change management process, 
      - New metrics being collected, 
      - Rollback procedures. 