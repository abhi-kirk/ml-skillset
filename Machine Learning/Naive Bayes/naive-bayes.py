import numpy as np

class NaiveBayesBinaryClassifier:
    def __init__(self):
        self.class_priors = None
        self.class_means = None
        self.class_variances = None
    
    def fit(self, X, y):
        """
        Train the Naive Bayes model using the training data X and labels y.
        """
        # Number of samples and features
        n_samples, n_features = X.shape
        
        # Calculate class priors (P(y))
        classes = np.unique(y)
        self.class_priors = {}
        for c in classes:
            self.class_priors[c] = np.sum(y == c) / n_samples
        
        # Calculate mean and variance for each feature in each class (P(X|y))
        self.class_means = {}
        self.class_variances = {}
        
        for c in classes:
            X_c = X[y == c]
            self.class_means[c] = np.mean(X_c, axis=0)
            self.class_variances[c] = np.var(X_c, axis=0)
    
    def predict(self, X):
        """
        Predict the class labels for the input samples X.
        """
        y_pred = []
        
        for sample in X:
            # Calculate the posterior probability for each class using Bayes' rule
            posteriors = {}
            
            for c in self.class_priors:
                prior = np.log(self.class_priors[c])  # log(P(y))
                likelihood = np.sum(np.log(self._gaussian_likelihood(sample, c)))  # log(P(X|y))
                posteriors[c] = prior + likelihood
            
            # Choose the class with the maximum posterior probability
            y_pred.append(max(posteriors, key=posteriors.get))
        
        return np.array(y_pred)
    
    def _gaussian_likelihood(self, x, class_label):
        """
        Compute the likelihood of the features x given the class using Gaussian distribution.
        """
        mean = self.class_means[class_label]
        var = self.class_variances[class_label]
        
        # For each feature, calculate the Gaussian probability density
        likelihood = (1 / np.sqrt(2 * np.pi * var)) * np.exp(-(x - mean) ** 2 / (2 * var))
        return likelihood


# Sample data: 10 samples, 2 features
X = np.array([
        [1.2, 2.3], 
        [2.3, 3.4], 
        [3.1, 1.5], 
        [4.5, 2.2], 
        [5.1, 3.3], 
        [6.2, 4.3], 
        [7.1, 5.1], 
        [8.3, 6.2], 
        [9.0, 7.3], 
        [10.2, 8.4]
    ])

# Binary labels (0 or 1)
y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 0])

# Initialize and train the Naive Bayes classifier
model = NaiveBayesBinaryClassifier()
model.fit(X, y)

# Sample test data (2 new samples)
X_test = np.array([[3.0, 2.5], [8.0, 6.5]])

# Make predictions
predictions = model.predict(X_test)

# Print predictions
print("Predictions:", predictions)