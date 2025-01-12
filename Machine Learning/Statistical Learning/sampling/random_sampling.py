# sample from a given probability distribution
# inverse transform sampling method
# source: https://stackoverflow.com/questions/4265988/generate-random-numbers-with-a-given-numerical-distribution

import random
from collections import Counter

def random_distribution(l):
    # sum of probs in l should sum to 1 to be a valid probability distribution
    r = random.uniform(0, 1)
    s = 0
    for item, prob in l:
        s += prob
        if s >= r:
            return item
    return item

population = [1, 2, 3, 4, 5, 6]
weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]

samples = []
for _ in range(1000):
    samples.append(random_distribution(zip(population, weights)))
print(Counter(samples))