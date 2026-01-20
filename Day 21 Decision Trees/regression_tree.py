import numpy as np


from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# House size (sq ft)
x = np.array([[500], [800], [1000], [1200], [1500], [1800]])

# House price (in lakhs)
y = np.array([15, 20, 25, 30, 40, 50])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(y_pred)

mse = mean_squared_error(y_test, y_pred)
print(mse)