import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


class LR:
    def __init__(self):
        self.m= None
        self.b = None

    def fit(self, x_train, y_train):
        num = 0
        den = 0

        for i in range(len(x_train)):
            num = num + ((y_train[i]-y_train.mean())* (x_train[i]-x_train.mean()))
            den = den + ((x_train[i]-x_train.mean())* (x_train[i]-x_train.mean()))

        self.m = (num/den)
        self.b = y_train.mean() - (self.m * x_train.mean())
        print(self.m)
        print(self.b)

    def predict(self, x_test):
        print(self.m * x_test + self.b)

data = {
    "X_Value": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50
    ],
    "Y_Value": [
        102, 108, 120, 117, 130, 128, 140, 138, 150, 147,
        160, 155, 168, 165, 175, 178, 182, 188, 195, 192,
        210, 205, 218, 215, 225, 232, 228, 240, 245, 238,
        255, 260, 258, 270, 268, 280, 285, 278, 295, 292,
        305, 310, 308, 320, 325, 322, 335, 330, 345, 340
    ]
}

df = pd.DataFrame(data)
print(df)

lr = LR()
x = df['X_Value']
y = df['Y_Value']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

lr.fit(x, y)
lr.predict(x_test)