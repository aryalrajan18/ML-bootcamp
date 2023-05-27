# -*- coding: utf-8 -*-
"""Linear Regression-ML day1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Io-_PPc1-8KDiFOe6ABDYQdLfzeXLhaO
"""

!ls

import pandas as pd

df = pd.read_csv("data.csv")

df.head()

df

df.tail

df.tail()

import matplotlib.pyplot as plt

df

plt.scatter(df['x'],df['y'])

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model

X=df.drop('y', axis=1)
Y=df['y']
model.fit(X,Y)

X= df.drop('y',axis=1)
Y = df['y']

model.fit(X,Y)

x = [num for num in range(18)]
x

new_inputs = pd.DataFrame({"x": x})

model.predict(new_inputs)

plt.scatter(df['x'],df['y']) 
plt.plot(x,y)

y= model.predict(new_inputs)

