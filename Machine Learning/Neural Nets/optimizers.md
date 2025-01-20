# Optimizers

## SGD (Stochastic Gradient Descent)
- *Differences from regular gradient descent*:
  - SGD updates the parameters after computing the gradient on a single training sample (as opposed to the entire training dataset). 
    - Hence batch size with SGD is 1. 
  - Dataset shuffled at the start of each epoch, and random sampling used to select samples used for updates. 
  - Faster initial progress due to more frequent updates. 
  - Noisy (can be an advantage due to exploration). 
  - Scales better since compute & memory cost is lower, and updates are incremental. 

## SGD with Momentum
- *Summary*: Momentum helps the optimizer move faster along directions where the gradient consistently points the same way, and reduces oscillations in directions where the gradient changes frequently. 
- *Working*:
  - Plain SGD update: $w_t = w_{t-1} - \eta g_t$
  - SGD with momemntum: 
    - Include velocity term $v_t = \beta v_{t-1} - \eta g_t$
    - Update: $w_t = w_{t-1} + v_t$
  - Velocity is the moving average of past gradients: accumulates gradients over time to smooth out updates. 
  - $\beta$ is the momentum coefficient (controls how much of the past velocity is retained). 
- *Intuition*:
  - Momentum keeps a running sum of past gradients. This helps build "velocity" in directions with consistent gradients. 
  - In directions with oscillating gradients (e.g., steep slopes), the accumulated velocity cancels out the back-and-forth updates, stabilizing the optimization. 
  - In directions with steady gradients (e.g., flat valleys), the velocity term amplifies updates, helping the optimizer move faster to the minimum. 
- *Advantages*:
  - Helps escape local minima.
  - Speeds up convergence in flat regions. 
  - Stability in steep regions. 
- *Limitations*:
  - Careful tuning of learning rate required. 
  - Does not adjust learning rate based on gradient magnitudes. 

## Adagrad (Adaptive Gradient)
- *Summary*: Instead a fixed learning rate, Adagrad adapts the learning rate based on the magnitude of gradients. 
- *Working*:
  - Accumulates the sum of squared gradients for each parameter. 
  - The learning rate decreases over time as the sum of squared gradients increases. 
  - A global learning rate $\eta$ still needs to be provided by the user as a hyperparameter. 
- *Intuition*:
  - If a parameter's gradient is consistently large, it implies that the loss function is sensitive to change in that parameter. 
  - Smaller updates in this case reduces the risk of oscillations or divergence during optimization. 
  - Conversely, larger updates when loss is less sensitive to the parameter (i.e., smaller accumulated gradients) will ensure faster optimization. 
  - Adagrad hence balances the contribution of each parameter to the optimization process. 
  - Compare to climbing a hill with a steep slope (large gradient) or a flat slope (small gradient). 
- *Advantages*:
  - No manual learning rate tuning (except the global). 
  - Useful for problems with sparse data/features (NLP, recommender systems) since in these cases the parameters are updated unevenly with SGD. 
- *Limitations*:
  - Can cause the learning to halt prematurely. 
  - Not suitable for non-convex optimization such as with multiple local minima since escaping a local minima would require a large update (while the gradients will be small). 

## RMSProp (Root Mean-Squared Propagation)
- *Summary*: Builds on Adagrad to address its primary limitation: aggressive decay of the learning rate over time. 
  - RMSProp introduces a mechanism to limit the growth of the accumulated squared gradients. 
- *Working*:
  - Same as Adagrad, but replaces the cumulative sum of squared gradients with an exponentially decaying moving average of squared gradients. 
  - Prevents the learning rate from decaying too quickly. 
  - Learning rate is adapted for each parameter, however it is still scaled using the user-provided hyperparameter global learning rate $\eta$.
    - $\eta$ remains constant throught training unless explicitly reduced via a learning rate schedule.  
  - Decay rate $\beta$ determines how quickly the moving average of squared gradients "forgets" past gradients. 
- *Advantages*:
  - By using moving average, RMSProp avoids the overly small updates.
  - Effective for deep learning where the loss surface changes dynamically. 
  - Better handling of vanishing and exploding gradients.  
- *Disadvantage*:
  - Now we need to tune two hyperparameters: $\eta$ and the decay rate $\beta$. 
  - Convergence speed can be limited since RMSProp smooths out rapid changes in the gradient magnitude over time. 
  - Does not address Adagrad's limitation of not being able to escape the local minima. 

## Adam (Adaptive Moment Estimation)
- *Summary*: Simultaneously adapts the learning rates for each parameter individually (like Adagrad and RMSProp) while incorporating Momentum to smooth updates. 
- *Working*:
  - Computes exponentially moving average of past gradients (first moment), as well as exponentially moving average of squared gradients (second moment). 
    - Note that a moving average is used instead of cumulative sum. 
  - A decay rate is associated with each of the two moments. 
  - Both moments are then used for the parameter update using the global learning rate. 
- *Advantages*:
  - Over Adagrad: Prevents learning rate to halt prematurely by using a moving average. 
  - Over RMSProp: Adds momentum to smooth updates and accelerates convergence. 
  - Over Momentum: Uses adaptive learning rates, making it robust to noisy gradients and non-stationary loss functions. 
  - Good candidate for deep learning (large datasets, high dimensional parameter space, non-stationary objectives). 
- *Limitations*:
  - Can overfit and hence not generalize well, especially with highly regularized problems. 
  - Requires additional memory and computation for the moving averages of gradients and squared gradients. 


## AdamW (Adam with Decoupled Weight Decay)
- *Summary*: Improves generalization of Adam by decoupling the weight decay from the gradient updates. 