import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("HomeData2.csv")
x = dataset.iloc[:, 6:7].values
#all rows, dependent var column
y = dataset.iloc[:, 2].values

#plotting real data TRAINING SET ###
plt.scatter(x,y, color = 'red')
plt.show()
