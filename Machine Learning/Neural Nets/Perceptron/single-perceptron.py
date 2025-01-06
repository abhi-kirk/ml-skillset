import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    URL_ = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    data = pd.read_csv(URL_, header=None)
    # make the dataset linearly separable
    data = data[:100]
    data[4] = np.where(data.iloc[:, -1] == 'Iris-setosa', 0, 1)
    return data


def show_data_2d(data):
    plt.scatter(np.array(data[:50, 0]), np.array(data[:50, 2]), marker='o', label='setosa')
    plt.scatter(np.array(data[50:, 0]), np.array(data[50:, 2]), marker='x', label='versicolor')
    plt.xlabel('petal length')
    plt.ylabel('sepal length')
    plt.legend()
    plt.show()


def response(fn_in):
    if fn_in > 0:
        return 1
    return 0


iris_data = load_data()
x, y = iris_data.iloc[:, 0:-1], iris_data.iloc[:, -1]
x = x.to_numpy().tolist()
y = y.to_numpy().tolist()
x = [[1] + xi for xi in x]  # insert bias feature vector

n, m = len(x), len(x[0])
r = 0.0001
eps = 0.001
# w = [0] * m
w = np.random.randn(m).tolist()
it_error = float("inf")
iterations = 0

while it_error > eps:
    iterations += 1
    error_i = 0
    for i in range(n):
        xi, yi = x[i], y[i]
        output = 0
        for j in range(m):
            output += w[j] * xi[j]
        y_predi = response(output)
        w_bias = [r * (yi-y_predi) * i for i in xi]
        w = [w[i]+w_bias[i] for i in range(m)]
        error_i += abs(yi-y_predi)
    it_error = error_i / n
    print(f"Iteration {iterations} error: {it_error}")

b, w = w[0], w[1:]
print(f"Perceptron trained with bias={b} and weight vector={w}")
