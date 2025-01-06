import numpy as np


# Implement Stochastic GD for Ordinary Least Squares
# Randomly selects mini-batches for gradient computation
# Regression: f(x) = b0 + b1*x1 + ... + bn*xn
# Cost function: C = 1/2n * \sum_i (y_i-b0-bixi)^2
# Gradient: \nabla C = [mean(b0+bixi-yi), mean((b0+bixi-yi)*xi)]
def ssr_gradient(x, y, b):
    res = b[0] + b[1] * x - y
    return res.mean(), (res * x).mean()


def gradient_descent(
        gradient, batch_size, x, y, start,
        lr, epochs, tolerance=1e-6
):
    n_obs = len(y)
    xy = np.c_[x.reshape(n_obs, -1), y.reshape(n_obs, -1)]
    vector = start
    for _ in range(epochs):
        np.random.shuffle(xy)
        for begin in range(0, n_obs, batch_size):
            stop = begin + batch_size
            x_batch, y_batch = xy[begin:stop, :-1], xy[begin:stop, -1]
            diff = -lr * np.array(gradient(x_batch, y_batch, vector))
            if np.all(np.abs(diff) <= tolerance):
                break
            vector += diff
    return vector


x = np.array([5, 15, 25, 35, 45, 55])
y = np.array([5, 20, 14, 32, 22, 38])

print(
    gradient_descent(
        gradient=ssr_gradient,
        batch_size=3,
        x=x,
        y=y,
        start=np.array([.5, .5]),
        lr=0.0008,
        epochs=100_000
    )
)
