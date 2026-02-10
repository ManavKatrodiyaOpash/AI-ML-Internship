import random
import numpy as np

class KMeans:
    def __init__(self, n_clusters=2, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit_predict(self,x):
        random_index = random.sample(range(0,x.shape[0]),self.n_clusters)
        self.centroids = x[random_index]

        for i in range(self.max_iter):
            cluster_group = self.assign_cluster(x)
            old_centroids = self.centroids
            self.centroids = self.move_centroids(x,cluster_group)

            if (old_centroids == self.centroids).all():
                break

        return cluster_group

    def assign_cluster(self,x):
        cluster_group = []
        distances = []

        for row in x:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))
            min_distance = min(distances)
            index_pos = distances.index(min_distance)
            cluster_group.append(index_pos)
            distances.clear()

        return np.array(cluster_group)

    def move_centroids(self,x,cluster_group):
        new_centroids = []
        cluster_type = np.unique(cluster_group)

        for type in cluster_type:
            new_centroids.append(x[cluster_group == type].mean(axis=0))

        return np.array(new_centroids)