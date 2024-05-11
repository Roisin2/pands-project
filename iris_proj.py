#Analysis.py
# Author: Roisin Stanley
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Reference.
#(https://raw.githubusercontent.com/mwaskom/seaborn-data/71e2436a092d714350de0fc409ca8a8714e7e78f/iris.csv)
  

#3. Write a program called analysis.py that:
#1. Outputs a summary of each variable to a single text file,
#2. Saves a histogram of each variable to png files, and
#3. Outputs a scatter plot of each pair of variables.
#4. Performs any other analysis you think is appropriate.


# read in data from url.
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/71e2436a092d714350de0fc409ca8a8714e7e78f/iris.csv")  

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

# Calculate pairwise correlation matrix (Pearson correlation)
correlation_matrix = data.corr()

# Print the correlation matrix
print(correlation_matrix)

# Function to summarize the data
def sum_data(data):
     try:
         with open('summary.txt', 'w') as f:
             for column in data.columns:
                f.write(f"Summary of {column}:\n")
                f.write(f"{data[column].describe()}\n\n")
     except Exception as e:
         print(f"An error occurred: {e}")

# defining a function sum_data. (A Function to get summary of data from each column in the data frame and saving it)
# Try exception block. If an exception happens the code will action inside the except block
# Opening a file with write mode, the with statement makes the file close.
# In writing to the file – inside the with block, the for loop  runs over each column of the the data
# For every column the function writes a string “summary of” with the column name and a new line character to the file.
# It calls then the describe method on the column which gives the descriptive stats like mean, min max etc. 
# this is then written to the file with two new line characters for spacing.
# If/when error occurs in the try block the except will catch the exception. Eg if dta object don’t have coloumns attribute 
# An error message is printed when the exception is caught in the  variable e


# Function to plot histograms
def plot_histograms(data):
    for column in data.columns:
        plt.figure()
        sns.histplot(data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.savefig(f'{column}_histogram.png')
        plt.close()


# Creating a new fig object in order to plot the histogram. Every column has its own figure.
# Histplot is called from seaborn and it plots a histogram for data in each column.
# kde=True argument adds a kernel density estimate plot on to the histogram 
# – a smooth curve that represented the probability density of the data.
# Setting the title
# Saving the histogram to a png file named after the column with  “_histogram” added to it
# Closing the the figure after a save. This is useful for not using too much memory.


# Function to plot scatter plots      #https://realpython.com/python-enumerate/
def plot_scatter_plots(data):
    for i, col1 in enumerate(data.columns):
        for j, col2 in enumerate(data.columns):
            if i < j:
                plt.figure()
                sns.scatterplot(data=data, x=col1, y=col2, palette='coolwarm', alpha=0.7)
                plt.title(f'Scatter Plot of {col1} vs {col2}')
                plt.grid
                plt.legend
                plt.savefig(f'{col1}_vs_{col2}_scatter.png')
                plt.close()

# The function takes data, a pandas data frame containing data to be plotted.
# There is a nested loop to iterate over all the pairs of columns in the df.
# Outer loop iterates over the columns and inner loop iterates again over the same columns.
# The condition “i<j” lets only one check on each pair of column.
# For each pair of col's a new scatter plot is created by sns scatterplot function.
# X axis is for the values in col1 and y axis is for values in col2.
# The title is set showing the columns that are being compared. color and transparency for interest
# Grid and legend added
# The plot is saves as an image file with a filename based on the column names.
# (Column1_vsColumn2_scatter.png”)
# After saving the plot. A function called plt.close is used to close the window


# Call the functions
sum_data(data)
plot_histograms(data)
plot_scatter_plots(data)

# Box plot for sepal length (x-axis) by species (y-axis)


def plot_box_and_violin_plots(data):
    sns.set_theme(style="whitegrid")  # Optional: Set a grid style
    for feature in ['sepal_length', 'petal_width']:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='species', y=feature, data=data)
        plt.title(f'Box Plot: {feature} by Species')
        plt.savefig(f'{feature}_boxplot.png')
        plt.close()

        plt.figure(figsize=(8, 6))
        sns.violinplot(x='species', y=feature, data=data)
        plt.title(f'Violin Plot: {feature} by Species')
        plt.savefig(f'{feature}_violinplot.png')
        plt.close()



# renamed columns 0,1,2,3 and showed every 50th row
#col = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
#data.rename(columns={col[0]:0, col[1]:1, col[2]:2, col[3]:3},inplace=True)
#print(data.iloc[::50])

# looking at the columns
#print(data.columns)

#
#print (data.shape)
#data.describe() # Gives statistical overview

# Showing info from species column eg there is 3 species and 50 of each
#print(data.species.value_counts())

# Generate histogram with values from the 1st column[0] # Add Labels and a Legend
#plt.hist(data[0], color = "#BF00BF", edgecolor = "white")
#plt.xlabel("X axis")
#plt.ylabel("Y axis")
#plt.title("Histogram of Sepal Length")
# Add a grid  https://www.w3schools.com/python/matplotlib_grid.asp
#plt.grid(color = 'g', linestyle = '--', linewidth = 0.5 )
#plt.show()

# Generate histogram with values from the 2nd column[1] # Add Labels and a Legend
#plt.hist(data[1], color = "#87CEFA", edgecolor = "white")
#plt.xlabel("X axis")
#plt.ylabel("Y axis")
#plt.title("Histogram of Sepal Width")
# Add a grid  https://www.w3schools.com/python/matplotlib_grid.asp
#plt.grid(color = 'g', linestyle = '--', linewidth = 0.5 )
#plt.show()


# ideas for scatter plots needs more thought

df= pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                 columns= iris['feature_names'] + ['target'])
 #select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)
# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values
#plot data
plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker='o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')
plt.show()