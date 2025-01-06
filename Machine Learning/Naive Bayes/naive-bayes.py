from statistics import mean, stdev
from sklearn.datasets import make_blobs
from scipy.stats import norm

def fit_distribution(data):
    mu = mean(data)
    sigma = stdev(data)
    return norm(mu, sigma)

def class_probability(X, prior, dist1, dist2):
    return prior * dist1.pdf(X[0]) * dist2.pdf(X[1])

# generate data
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# extract data for each class
Xy0, Xy1 = X[y==0], X[y==1]

# calculate priors for each class
prior0, prior1 = len(Xy0)/len(y), len(Xy1)/len(y)

# create PDFs for first feature, for each class
X1y0 = fit_distribution(Xy0[:, 0])
X1y1 = fit_distribution(Xy1[:, 0])

# create PDFs for second feature, for each class
X2y0 = fit_distribution(Xy0[:, 1])
X2y1 = fit_distribution(Xy1[:, 1])

# select sample for testing 
Xsample, ysample = X[0], y[0]

# calculate probability for each class
py0 = class_probability(Xsample, prior0, X1y0, X2y0)
py1 = class_probability(Xsample, prior1, X1y1, X2y1)

print(f"Class 0 probability = {py0 * 100}")
print(f"Class 1 probability = {py1 * 100}")