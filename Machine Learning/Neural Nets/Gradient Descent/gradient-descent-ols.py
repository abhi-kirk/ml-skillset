import numpy as np


# Implement GD for Ordinary Least Squares
# Regression: f(x) = b0 + b1*x1 + ... + bn*xn
# Cost function: C = 1/2n * \sum_i (y_i-b0-bixi)^2
# Gradient: \nabla C = [mean(b0+bixi-yi), mean((b0+bixi-yi)*xi)]
def ssr_gradient(x, y, w):
    res = w[0] + w[1] * x - y  # y_pred - y
    return res.mean(), (res * x).mean()


def gradient_descent(
        gradient, x, y, weights_initial,
        lr, epochs, tolerance=1e-6
):
    weights = weights_initial
    for _ in range(epochs):
        # weight update using all 6 observations
        diff = -lr * np.array(gradient(x, y, weights))
        if np.all(np.abs(diff) <= tolerance):
            break
        weights += diff
    return weights


x = np.array([5, 15, 25, 35, 45, 55])  # 6 observations, 1 feature
y = np.array([5, 20, 14, 32, 22, 38])  # 6 target values

print(
    gradient_descent(
        gradient=ssr_gradient,
        x=x,
        y=y,
        weights_initial=np.array([.5, .5]),  # weights for 1 feature, and 1 bias
        lr=0.0008,
        epochs=100_000
    )
)
