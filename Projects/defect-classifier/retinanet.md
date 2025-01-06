- **RetinaNet Motivation**
  - For some inspection lines where several defects were being captured by the vision system in individual images, I developed and deployed a (short-lived) RetinaNet model which allowed a one-pass defect detection and classification system. 

- **My Role**
  - Tuning focal loss. 
  - Some manual creation of bounding boxes and labeling. 
  - Testing with IOU metric. 
  - Testing for inference speed and accuracy, and comparison with vanilla VGG-19. 

- **Dataset**
  - For the RetinaNet classifier, the detection training data was much smaller, and was created by manually including bounding boxes on relevant images. 

- **Model Selection: For inspection lines requiring defect image detection, discuss why RetinaNet was chosen over alternatives like YOLO or Mask R-CNN.**
  - As opposed to YOLO or Mask R_CNN, RetinaNet is a single-stage detection + classifier method, which strikes a balance between simpler architecture, high precision, and low real-time inference latency. 
    - R-CNN is high accurate but slower and more complex, while YOLO is very fast but less accurate. 
    - Since most of the image regions contain the background (hence, making the number of bounding boxes unbalanced between low positives and high number of negatives), RetinaNet is a good choice since it uses a special Focal loss to reduce the impact of easy negatives. 
    - Focal loss is a modified cross-entropy loss with an additional factor that adjusts the loss based on the difficulty of each example (i.e. higher the predicted probability [easy negative], lower is the contribution to the loss). 

- **RetinaNet Deployment: Why short-lived?**:
  - Initially, we encountered a scenario where some inspection lines produced images with multiple defects, which our standard VGG-19 model wasn’t optimized for. 
  - To address this, I developed and briefly deployed a RetinaNet-based solution. This approach handled multi-defect detection and classification more effectively—at least during the short period it was live. 
  - However, after a few weeks, our vendor updated their equipment and the issue of multiple defects per image largely disappeared. Given that the overhead of maintaining RetinaNet was no longer justified, our leadership decided to revert to the simpler CNN-only VGG-19 model. 
  - So, while I did implement and deploy RetinaNet for a time, my experience on that front was limited to an initial deployment and short production window. I didn’t face the long-term challenges or iteration cycles that often accompany a fully matured deployment. Still, the experience did allow me to understand the complexities of integrating a more advanced detection model into the pipeline, from training and inference optimization to initial integration tests.