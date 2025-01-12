# reservoir sampling problem: 
# Processing a stream of data one item at a time, and we don't know the length of the stream in advance.
# We want to sample k elements from the stream such that each element is equally likely to be chosen.

import random

def reservior_sampling(stream, k):
    res = []
    for i in range(len(stream)):
        item = stream[i]
        if i < k:
            res.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                res[j] = item
    return res

stream = range(1, 101)
k = 5
result = reservior_sampling(stream, k)
print(f"Randomly selected items: {result}")