import numpy as np
from collections import Counter

class Knn:
    def __init__(self,k):
        self.n_neighbors = k
        self.x_train = None
        self.y_train = None

    def fit(self,x_train,y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self,x_test):
        y_pred = []

        for i in x_test:
            distances = []
            for j in self.x_train:
                distances.append(np.linalg.norm(i-j))
            n_neighbors = sorted(list(enumerate(distances)),key=lambda x:x[1])[0:self.n_neighbors]
            label = self.majority_counts(n_neighbors)
            y_pred.append(label)

        return np.array(y_pred)

    def majority_counts(self,neighbors):
        votes = []
        for i in neighbors:
            votes.append(self.y_train[i[0]])
        votes = Counter(votes)

        return votes.most_common()[0][0]