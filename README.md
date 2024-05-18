# An analysis of the Iris Data Set using Python

[Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) was a statistician and biologist and this data is from a paper he released in 1936.
I read in the [raw data](https://raw.githubusercontent.com/mwaskom/seaborn-data/71e2436a092d714350de0fc409ca8a8714e7e78f/iris.csv) using a url found on Github from a reliable source, Michael Waskom - the inventor of sea born.
 I found that the data was almost pretreated for me compared to other sources such as [UCI](https://archive.ics.uci.edu/dataset/53/iris )

 ![Iris Flowers](https://miro.medium.com/v2/resize:fit:1000/1*nfK3vGZkTa4GrO7yWpcS-Q.png)

## My Summary of the Iris Data Set

The Iris Data Set is quite famous and is a much used data set for teaching and learning.
This is due to the many options available to look at for analysis, as there are 3 species with 4 attributes each.
From my reading it seems this data set is held in high regard as being the gold standard for algorithm testing and also machine learning.

![Scatter plot of petal width versus species](image.png)

![Scatter plot of Sepal length versus species](image-1.png)


The Iris flowers themselves are the Setosa, Versicolor and Virginica. There are 150 samples of the flowers -  with 50 of each species.
 Then within each Species, are the four attributes which are Petal Length and Width, and Sepal Width and Length. This in my opinion makes for easier tasks for novice learners.

 *The Purpose of this task was to complete a program called analysis.py that:*

1. Outputs a summary of each variable to a single text file
2. Saves a histogram of each variable to png files
3. Outputs a scatter plot of each pair of variables
4. Performs any analysis appropriate.

 *Task 1*
The first task required a little research and a lot of trial and error but i think my solution works quiet well.

I used a function called "sum_data" in order to save a summary of all the data from each column in the data frame. Then I used a Try exception block.
If an exception happens the code will work inside the except block, opening a file with write mode. (The with statement makes the file close.)
In writing to the file – inside the with block, the for loop runs over each column of the the data.
For every column, the function writes a string “summary of” - with the column name and a new line character to the file.
It then calls the describe method on the column, which gives the descriptive statistics like mean, min max etc. The results are then written to the file.
If an error occurs in the try block, the except will catch the exception. Eg if data object doesn't have a columns attribute.
An error message is printed when the exception is caught in the variable "e".

*Task 2*
 Creating a new fig object in order to plot the histogram. Every column has its own figure.
 Histplot is called from seaborn and it plots a histogram for data in each column.
 kde=True argument adds a kernel density estimate plot on to the histogram – a smooth curve that represents the probability density of the data.
 I saved the histogram to a png file, named after the column -  with  “_histogram” added.
 By closing the the figure after a save is useful for not using too much memory.

*Task 3*
I used [enumerate](https://realpython.com/python-enumerate/)

 The function takes data, a pandas data frame containing data to be plotted.
There is a nested loop to iterate over all the pairs of columns in the df.
An Outer loop iterates over the columns and inner loop iterates again over the same columns.
 The condition “i< j" lets only one check on each pair of columns. And for each pair of columns, a new scatter plot is created by seaborn's sns scatterplot function.

 For the plot, the x axis is for the values in col1, and y axis is for values in col2.
 A title is set showing the columns that are being compared with color and transparency for interest, a grid and legend are also added.
 The plot is saves as an image file with a filename based on the column names.
 (Column1_vsColumn2_scatter.png”)
 After saving the plot. A function called plt.close is used to close the window.

### Getting Started

The user will need to have Jupyter Notebook Editor for [Visual Studio Code](https://code.visualstudio.com/) in order to clone the repository.
     The code used is python, so [Anaconda](https://www.anaconda.com/download) is my recommendation as it has so many built in functions such as Pandas, Matplotlib and Numpy and Seaborn.

Libraries imported are:

[matplotlib](https://matplotlib.org/): pyplot makes plots! Anything from scatter plots and histograms and pie charts.

[pandas](https://pandas.pydata.org/):This was used alot in my analysis here. Its fast and efficient for data manipulation with tools for reading and writing data between in-memory data structures and different formats like CSV and text files.

[seaborn](https://seaborn.pydata.org/): This is wonderful for making nice visual displays.
I believe its built on matplotlib.

 [numpy](https://numpy.org/): It is quick to go through large lists (arrays or matrices)

### References

1. <https://raw.githubusercontent.com/mwaskom/seaborn-data/71e2436a092d714350de0fc409ca8a8714e7e78f/iris.csv>
This Raw data taken from Github page belonging to the inventor of Seaborn.

2. <https://en.wikipedia.org/wiki/Iris_flower_data_set>

3. ["geeksforgeeks.org"](https://www.geeksforgeeks.org/
python-basics-of-pandas-using-iris-dataset/)

4. ["Tutorial point"](https://www.tutorialspoint.com/
exploratory-data-analysis-on-iris-dataset)

5. <https://stackoverflow.com/questions/65569132/python-pandas-error-and-exception-handling>

6. <https://realpython.com/python-enumerate/>

7. <https://www.researchgate.net/publication356718128_The_iris_data_set_In_search_of_the_source_of_Virginia>

8. <https://www.datacamp.com/tutorial/types-of-data-plots-and-how-to-create-them-in-python>

9. <https://www.adventuresinmachinelearning.com/plotting-the-perfect-line-of-best-fit-in-python/>

10. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html>

11. <https://miro.medium.com/v2/resize:fit:1000/1*nfK3vGZkTa4GrO7yWpcS-Q.png> Iris Image

12. <https://www.datacamp.com/tutorial/types-of-data-plots-and-how-to-create-them-in-python>

13. <https://www.adventuresinmachinelearning.com/plotting-the-perfect-line-of-best-fit-in-python/>

14. <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html>

#### Acknowledgements

Lecturers in ATU Andrew Beatty and Ian Mc Loughlin, for lectures through online platform.

#### Getting help

If there is an issue or a query please don't hesitate to submit an issue on git hub.

#### Author

  I study at [ATU](https://www.atu.ie/). I am a mature student returning to education. I have a Bachelors of Business Studies from the former Institute of Technology Sligo - now part of ATU. I find this an interesting subject and hope to continue learning online from the beautiful north west of Ireland. I will be looking for work in the near future and at this moment I will leave my contact as my University Email; <G00438900@ATU.ie>

  ***

#### End
