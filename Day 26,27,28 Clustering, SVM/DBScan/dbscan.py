from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons, make_circles
import matplotlib.pyplot as plt

X, _ = make_moons(n_samples=300, noise=0.05)

db = DBSCAN(eps=0.2, min_samples=5)
labels = db.fit_predict(X)

plt.scatter(X[:,0], X[:,1], c=labels)
plt.title('DBSCAN of moons')
plt.tight_layout()
plt.show()

x, _ = make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=0)
db = DBSCAN(eps=0.2, min_samples=5)
labels = db.fit_predict(x)

plt.scatter(x[:,0], x[:,1], c=labels)
plt.title('DBSCAN of circles')
plt.tight_layout()
plt.show()