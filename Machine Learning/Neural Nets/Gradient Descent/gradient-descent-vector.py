import numpy as np


# Implement GD for y = f(x_1,..,x_n) to find x_1,...,x_n that minimizes y
def gradient_descent(gradient, start, lr, n_iters, tolerance=1e-6):
    vector = start
    for _ in range(n_iters):
        diff = -lr * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):  # gradient goes to zero
            break
        vector += diff
    return vector


print(
    gradient_descent(
        gradient=lambda v: np.array([
            2 * v[0], 4 * v[1] ** 3
        ]),  # f(v) = v1^2 + v2^4
        start=np.array([2.0, 1.5]),
        lr=0.002,
        n_iters=10_000
    )
)
