import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("salaries.csv")
#independent variable
x = dataset.iloc[:, :-1].values
#all rows, dependent var column
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_TEST, y_train, y_TEST = train_test_split(
    x, y, test_size = 0.33, random_state = 0
    )

#from sklearn.preprocessing import StandardScaler
#not necessary with certain libraries

#fit linear regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#predict results from test set
y_pred = regressor.predict(x_TEST)

#plotting real data TRAINING SET ###
plt.scatter(x_train, y_train, color = 'red')
#regression line
#creating training data regressor w training set preds
train_pred = regressor.predict(x_train)
plt.plot(x_train, train_pred, 'blue')
plt.title("TRAINING Home Prices")
plt.ylabel("Home Prices")
plt.show()

#plotting real data TEST SET ###
plt.scatter(x_TEST, y_TEST, color = 'red')
#regression line
#creating training data regressor w training set preds
train_pred_TEST = regressor.predict(x_train)
plt.plot(x_train, train_pred_TEST, 'blue')
plt.title("TEST Home Prices")
plt.xlabel("Square footage")
plt.ylabel("Home Prices")
plt.show()
