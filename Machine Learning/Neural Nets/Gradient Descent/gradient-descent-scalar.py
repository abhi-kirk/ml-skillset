import numpy as np


# Implement GD for y = f(x) to find x that minimizes y
def gradient_descent(gradient, start, lr, n_iters, tolerance=1e-6):
    vector = start
    for _ in range(n_iters):
        diff = -lr * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff
    return vector


print(
    gradient_descent(
        gradient=lambda v: 2 * v,
        start=10,
        lr=0.02,
        n_iters=10_000
    )
)
