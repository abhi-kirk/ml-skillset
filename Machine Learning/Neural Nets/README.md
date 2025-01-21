# Neural Nets Recipe

Sources: 
- [A. Karpathy Blog](https://karpathy.github.io/2019/04/25/recipe/)
- [Google Research Tuning Playbook](https://github.com/google-research/tuning_playbook)

## Data: Qualititative Analysis
- Thoroughly inspect your data. 
  - Scan data manually and with EDA tools: look at distributions, patterns, limits, outliers, imbalances, biases. 
  - For the task at hand, are local features enough, or do we need global context?
  - What variation is spurious and can be preprocessed out?
  - How far can we downsample?
  - Handle noise in labels. 
- Helps in debugging the neural net predictions. 

~~~
We should now have a good understanding of the dataset. 
~~~


## Get Baselines
- Setup training/eval pipeline. 
- Fix random seed. 
- Turn off data augmentations. 
- Visualize data just before passing it to the net. 
- Choose the simplest model possible for the task, and verify decreasing training loss. 
- Verify loss@init: `-log(1/n_classes)`. 
- Init well to eliminate "hockey stick" training curves. 
- Get human baseline metrics. 
- Get input-independent baseline, i.e. set all inputs to zero. 
- Overfit one batch. 
  - Batch size should be selected as the largest batch size supported by the available hardware. 
- Chart dependencies using backprop: 
  - E.g. set the loss to sum of outputs from the $i^{th}$ sample only, and run backward pass. 
  - Analyzing gradients, only the $i^{th}$ input should have a non-zero gradient. 
- Visualize first-layer weights where fundamental features are learned. 
- Vectorize the code later, one loop at a time. 

~~~
We should now have a semi-automated training/eval pipeline, which, when provided with any appropriate model, spits out all kinds of metrics and debugging results. 
~~~

## Complexify
- Pick initial model architecture directly from papers, even if it overfits the data. 
- Complexiy model input slowly and verify performance boost at each time (e.g. feeding smaller images first and making them bigger later). 
- Learning rate decay schedules (in papers) heavily depend on the size of dataset - adjust accordingly. 
  - Disable initially, and tune it. 

~~~
We should now have a large model that is (over)fitting the training dataset. 
~~~

## Regularize
- Get more real data. 
- More aggressive data augmentations, or simulated data. 
- Transfer learning. 
- Remove features that are not useful since model may overfit to this noise. 
- Dropouts. 
- Weight decay. 
- Early stopping. 

~~~
We should now have reduced overfitting considerably. 
~~~

## Tune
- Random over grid search. 
  - Neural nets are sensitive to some parameters than the rest. 
- Knowledge distillation. 

~~~
SOTA!
~~~