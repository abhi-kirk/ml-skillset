# Convolutional Neural Nets (CNN)
- *Summary*: Deep neural nets specifically designed to process and analyze data that has a grid-like structure, such as images, videos and time-series data. 
- *Architecture*:
  - *Convolution layers*: Extracts spatial and hierarchial features from the input data. Uses small filters/kernels that slide over the input data to detect specific features. Stride and padding used to control the kernel sliding. Activations applied after each convolution operation. 
  - *Pooling*: To reduce computational complexity and overfitting. 
  - Convolution and Pooling blocks are repeated to build hierarchial feature representations. 
  - *Fully Connected layer*: Flatten the output from convolutional blocks and apply FC layers with activation for a specific objective. 
- *Backprop*: 
  - At the end of the forward pass, loss function is computed which is a function of the kernel weights. 
  - Gradient of the loss, with respect to the kernel weights, is used to update the weights using chain rule and an optimizer. 
- *Advantages over FC neural nets*: 
  - Weight sharing
  - Ability to extract increasingly complex features
- *Notes*:
  - Batch Normalization: Normalizes intermediate feature maps (across a mini-batch of training samples) to improve stability and convergence during training. 
    - Introduces learnable parameters scale and shift. 
    - Prevents issues like exploding or vanishing gradients. 
    - Reduces sensitivity to initialization. 
    - Acts as a regularizer. 
    - Applied after the convolution operation and before the activation function. 
  - Dropout: Randomly disables a fraction of neurons during training to prevent overfitting. 

## AlexNet
- *Key contributions*:
  - First network to use the CNN architecture for image processing using ReLU activation, dropout regularization, data augmentation and GPU training. 
- *Architecture*:
  - 8 layers: 5 convolution + 3 FC
  - Large filters in early layers
- *Limitations*:
  - Overfitting
  - Limited accuracy

## VGG
- *Key contributions*:
  - Demonstrated increasing network depth with a consistent architecture improves performance. 
  - Smaller filters to reduce parameters and have a larger receptive field. 
  - Showed that network depth is critical for extracting hierarchial features. 
- *Architecture*:
  - 16-19 layers
  - Small filters
- *Limitations*:
  - Slow training due to large number of parameters

## ResNet
- *Key contributions*:
  - Introduced skip/residual connections for gradients to flow directly to layers at the back. 
  - This enabled deeper architectures, and showed they outperform shallow ones. 
- *Architecture*:
  - 50-100+ layers. 
  - Very small filters in early layers. 
- *Limitations*:
  - Increased computational cost. 

## Why VGG over ResNet?
- For smaller datasets, especially for incremental learning with cold start, ResNet overfits. 
- VGG has a simpler and uniform architecture: easier to understand, implement and debug. 
- VGG's hierarchial feature extraction is useful for transfer learning and image masking visualization. 
- ResNet was a fairly newer architecture at the time. 

## Image Masking for Explaianability (Occlusion Sensitivity)
- Visualization technique that highlights regions of an image that are most important for a specific class prediction by the CNN. 
- Grad-CAM offers a (possibly superior) alternative by analyzing gradients of the output with respect to the feature maps to compute importance. 
- Why Occlusion Sensitivity over Grad-CAM?
  - Grad-CAM was introduced in 2017-2018 and hence was fairly new/experimental at the time of developing the defect classifier. 
  - Occlusion sensitivity is direct and intuitive (no gradient dependency), which helps with the problem statement of CNN explainability to non-technical audiences (line operators, plant management). 
  - It is architecture agnostic, and can even be used for non-CNN methods in other inspection lines not in the immediate scope of CNN installation. 
- Occlusion Sensitivity limitations:
  - High computation cost: Hence, only a small (but critical) sample of inference images in prod are used. 
  - Masking a region also removes its contextual relationship with the surrounding regions. 

## Two-Stage Hybrid Learning with Random Forest
- *Summary*: Leverages CNN for feature extraction, and Random Forest for classification to reduce overfitting, especially in the case of cold starts where limited training data is available. 
- *Limitations*:
  - Suboptimal separate CNN and RF trainings. CNN does not learn from RF training. 
  - Increased model complexity. 
  - Have to train CNN and RF separately, with increased time for testing. 

## Morphological Transformations for CNN Post-Processing
- *Morphological Operations*:
  - Erosion: 
    - Removes pixels from the boundaries of objects. 
    - For each pixel, if the structuring element fits entirely within the object, the pixel is retained; otherwise, it's removed. 
  - Dilation:
    - Adds pixels to the boundaries of objects. 
    - For each pixel, if any part of the structuring element overlaps with the object, the pixel is retained. 
  - Opening:
    - Erosion then Dilation. 
    - Removes small noise. 
  - Closing: 
    - Dilation then Erosion. 
    - Fills small holes or gaps. 
- *Steps*:
  - Identify the region of interest for the rarely-occuring defect type. 
  - Apply morphological transformations to this region to enhance the defect type features. 
  - Use connected component analysis to detect this feature, and thresholding to classify it as the new defect type. 
- *Integration with CNN*:
  - Used as a post-processing module to detect rare defect types which have a very specific location and spatial features. This type is being misclassified as a few existing defect types since the rare defect does not have its own class. 
  - Overrule the defect type using this module. 
