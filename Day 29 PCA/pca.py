import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

x,y = load_iris(return_X_y=True)

x_scale = StandardScaler().fit_transform(x)
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scale)

plt.scatter(x_pca[:,0], x_pca[:,1], c=y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
plt.show()

print(pca.explained_variance_ratio_)