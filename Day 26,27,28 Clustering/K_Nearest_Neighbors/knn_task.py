import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from KNeighborsClassifier import Knn

df = pd.read_csv("Social_Network_Ads.csv")
print(df)
df = df.iloc[:,1:]
print(df)

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

x = df.iloc[:,0:3].values
x = StandardScaler().fit_transform(x)
y = df.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print(accuracy_score(y_test, y_pred))

my_knn = Knn(k=5)
my_knn.fit(x_train, y_train)
y_pred = my_knn.predict(x_test)
print(accuracy_score(y_test, y_pred))