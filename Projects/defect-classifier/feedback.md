# Feedback on the "Defect Classifier for Gorilla Glass" Project Overview and Q&A

## Potential Areas for Further Detail or Clarification

### 1. Data Labeling and Class Imbalance
- [CLARIFIED] You mention using SMOTE, traditionally a tabular data technique, for image data. SMOTE isn’t straightforward for images since it’s not directly applicable to pixel data. Consider clarifying if you actually used a conceptually similar approach (e.g., extensive data augmentation or generating synthetic images using other means).
- [CLARIFIED] If you used class weighting or image-specific augmentation to handle imbalance, emphasize how these were tuned and why augmentation outperformed class weighting.

### 2. Model Architecture and Selection
- [CLARIFIED] The choice of VGG-19 is justified by accuracy and latency trade-offs. However, you mention ResNet easily overfitted and required more data: Be ready to explain what experiments led to concluding that ResNet was overfitting more. Did you try additional regularization, data augmentation, or fewer layers before discarding ResNet?

### 3. Latency and Deployment Constraints
- You have a 10ms latency requirement. Interviewers may ask:
  - [CLARIFIED] Did you consider model compression, quantization, or hardware acceleration (e.g., TensorRT) to further reduce inference time?
  - [CLARIFIED] How did you batch inference requests, if at all, and what impact did that have on latency?
- [CLARIFIED] The “no open-source” constraint can raise questions since deep learning frameworks are often open-source. Be prepared to explain if you used a company-approved distribution, a proprietary inference library, or a framework already integrated into the vendor’s system.

### 4. Integration and Offline Environment
- With no cloud or remote access, how were model updates and retraining cycles performed?
- Did you have a secure process for transferring trained models from a separate environment into the offline production environment?

### 5. Incremental / Online Learning
- You mention incremental training as new data arrives.
  - Interviewers may ask how you prevented catastrophic forgetting and ensured stable performance over time.
  - Were there any triggers or schedules for retraining, and how did you validate these incrementally updated models?

### 6. Model Interpretability / Explainability
- You mention CNN masking and saliency maps. Interviewers might ask:
  - Which specific interpretability technique (e.g., Grad-CAM, Integrated Gradients) was chosen and why?
  - How did you ensure these explanations were meaningful, not just to technical stakeholders but also to line operators?

### 7. Data Pipeline and Versioning
- For data versioning and experiment tracking, you mention using PostgreSQL and MLflow.
  - Consider explaining how you ensured data consistency between training and validation sets over multiple iterations.
  - How were changes to the data schema handled, and how did you ensure reproducibility?

### 8. Error Analysis and Continuous Improvement
- You describe using confusion matrices for error analysis.
  - Interviewers might ask about specific root causes identified and how they fed back into data collection or modeling strategies. Be ready to give a concrete example of a discovered error pattern and how you addressed it.

### 9. Metrics and Thresholding
- You emphasize recall for critical classes. Interviewers might ask:
  - Why not optimize precision for certain classes? How did you balance multiple objectives?
  - Did you use Precision-Recall curves or other metrics (like F-beta scores) specifically tuned for high recall?

### 10. Complexity of the Final System
- The final solution includes a CNN classifier, cascade modules, and sometimes a random forest on CNN features.
  - Be prepared to justify the added complexity. Could a single, more robust model have replaced multiple steps? If not, why was the layered approach necessary?

## Missing or Less Addressed Topics
- **Model Drift / Domain Shift**: Consider explaining how you would handle changes in the manufacturing process over time.
- **Robustness to Environmental Factors**: More detail on handling variations in lighting, camera angles, or glass types might be expected.
- **Detailed Steps in Transfer Learning**: Specify which layers of VGG-19 you froze or fine-tuned, and how that improved convergence or accuracy.