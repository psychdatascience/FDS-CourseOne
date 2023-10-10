---

### Python Homework: Data Analysis with Pandas and Seaborn

**Objective:**  

* Practice reading, summarizing, and visualizing CSV data using the `pandas` and `seaborn` libraries.
* Practice writing functions

**Dataset:**  
For this assignment, use the "Iris" dataset, a classic dataset in data science and statistics. It contains measurements for 150 iris flowers from three different species.

This is by no means a "behavioral science" data set, but there are certain classic data sets that every data science student has to touch once, and this is one of them.

The dataset is available [here](https://www.kaggle.com/datasets/saurabh00007/iriscsv/)
Or paste "https://www.kaggle.com/datasets/saurabh00007/iriscsv/" into your browser.

If you don't have a kaggle account, you'll be asked to create one – please do that, it's free and you'll eventually want one anyway!

1. **Reading the Dataset:**
    - Use `pandas` to read the Iris dataset into a data frame.
    - The dataset does not contain headers. Assign the following column names to your data frame: `['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']`

2. **Data Summarization:**
    - Compute the following summary statistics for each of the numerical columns (`sepal_length`, `sepal_width`, `petal_length`, `petal_width`):
        * Mean
        * Median
        * Standard Deviation
    - Write these summary statistics to a new CSV file named `iris_summary.csv`.

3. **Data Visualization:**
    - Use `seaborn` to create the following plots:
        a. A pair plot (`pairplot`) of all numerical columns colored by the `species` column.
        b. A box plot showing the distribution of each numerical column grouped by `species`.

4. **Plotting Function**
    - Write a function that uses `seaborn` to visualize the iris data.

    - Your function should:

        * take an iris-like data frame as an input
        * allow the user to choose between a strip, violin, or box plot
        * set one of the above three be the default
        * have a docstr with meaningful help so users can get help() on it
        * produce the plot requested by the user (of course!)
