# Author: Roisin Stanley
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Reference.
#(https://raw.githubusercontent.com/mwaskom/seaborn-data/71e2436a092d714350de0fc409ca8a8714e7e78f/iris.csv)
# Raw data taken from Github page belonging to the inventor of Seaborn.  

# read in data from url.
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/71e2436a092d714350de0fc409ca8a8714e7e78f/iris.csv")  

##### sys.stdout.write(<some string text here>) #https://www.geeksforgeeks.org/sys-stdout-write-in-python/

# see all data - showing 150 rows and 5 columns
print(data)

# all the values of first row will be present
print(data.iloc[0])

# first five rows
print(data.head())

# last five
print(data.tail())

# Showing the Types of data - floats and objects
print(data.dtypes) 

# renamed columns 0,1,2,3 and showed every 50th row
col = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
data.rename(columns={col[0]:0, col[1]:1, col[2]:2, col[3]:3},inplace=True)
print(data.iloc[::50])

# looking at the columns
print(data.columns)

#
print (data.shape)
data.describe() # Gives statistical overview

# Showing info from species column eg there is 3 species and 50 of each
print(data.species.value_counts())

# Generate histogram with values from the 1st column[0] # Add Labels and a Legend
plt.hist(data[0], color = "#BF00BF", edgecolor = "white")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Histogram of Sepal Length")
# Add a grid  https://www.w3schools.com/python/matplotlib_grid.asp
plt.grid(color = 'g', linestyle = '--', linewidth = 0.5 )
plt.show()

# Generate histogram with values from the 2nd column[1] # Add Labels and a Legend
plt.hist(data[1], color = "#87CEFA", edgecolor = "white")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Histogram of Sepal Width")
# Add a grid  https://www.w3schools.com/python/matplotlib_grid.asp
plt.grid(color = 'g', linestyle = '--', linewidth = 0.5 )
plt.show()


```# ideas for scatter plots needs more thought

df= pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                 columns= iris['feature_names'] + ['target'])
# select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)
# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values
# plot data
plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker='o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')
plt.show()