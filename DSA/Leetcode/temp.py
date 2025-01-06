import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	n = X.shape[0]
	
	X = X.tolist()
	if y is not None:
		y = y.tolist()
		
	if n <= batch_size:
		if y is None:
			return [X]
		return [X, y]
	
	iters = n // batch_size
	if n % batch_size > 0:
		iters += 1
		
	res = []
	start, stop = 0, batch_size
	for i in range(iters):
		if y is None:
			batch = [X[start:stop, :]]
		else:
			batch = [X[start:stop, :], y[start:stop]]
		start += batch_size
		stop += batch_size
		
		res.append(batch)
	
	return res


print(batch_iterator(
    np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 
    np.array([1, 2, 3, 4, 5]), 
    batch_size=2)
)