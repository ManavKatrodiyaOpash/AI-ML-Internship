import pandas as pd
from sklearn.cluster import KMeans

# Create data (NO LABELS)
data = {
    "StudyHours": [1, 2, 3, 7, 8, 9]
}

df = pd.DataFrame(data)

# Apply KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(df)

# Cluster result
df["Group"] = kmeans.labels_

print(df)
