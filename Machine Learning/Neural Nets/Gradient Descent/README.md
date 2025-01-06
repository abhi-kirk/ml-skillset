## Gradient Descent

### Important
- Works on differentiable functions only since a gradient needs to be calculated. 
- Can get stuck in a local minima or saddle point. 
- Derivatives:
  - Derivative of a function shows how much a value changes when function arguments are modified. 
  - Zero derivatives might indicate a minimum, maximum or a saddle point. 
- Gradients:
  - Gradient of a function $f(x)$ of several independent variables $x = [x_1, ..., x_m]$ is defined as the vector function of the *partial derivatives* of $f(x)$ w.r.t each independent variable: $\nabla f(x) = [\partial f(x)/\partial x_1, ..., \partial f(x)/\partial x_m]$. 
- Gradient descent algorithm:
  - Start with an arbitrarily (initial) chosen point $x$ $= [x_1, ..., x_m]$, 
  - Update this point in the direction of the *negative gradient*: $x \leftarrow x - \eta\nabla f(x)$, where $\eta$ is a small positive *learning rate*. 

### Stochastic Gradient Descent
- Approximates the gradient with an estimate from a sample drawn from given data. 

### Regression:
- Given data $x$ (scalar, vector or matrix), and observations $y$ (scalar or vector), find a linear fit: 
$$y = b_0 + b_1x = bx$$
- *Ordinary Least Squares (OLS)* cost function to be minimized: 
  - *Sum of Squared Residuals (SSR)*, or
  - *Mean Squared Error (MSE)* = SSR/$n$, where $n$ is the number of observations. 
  $$f(x) = \frac{1}{2n}\sum_{i=1}^{n}(y_i-b_ix_i)^2$$