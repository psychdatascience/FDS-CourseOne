

---

**Pandas Indexing, Grouping, and Aggregating Homework**

**Dataset**: You will be using the famous "Titanic" dataset. This dataset contains the information about passengers who were onboard the Titanic. You can load it directly from the seaborn library.

```python
import seaborn as sns

titanic = sns.load_dataset('titanic')
```

**Instructions**:

1. **Exploring the Dataset**:
   a. Display the first 10 rows of the dataset.
   b. How many rows and columns does the dataset have?

2. **Using `.loc` and `.iloc` methods**:
   a. Select the rows from index 5 to 15 and columns "age" and "fare" using the `.loc` method.
   b. Select the first 5 rows and first 3 columns using the `.iloc` method.
   c. Find the age of the passenger at the 100th index using `.iloc`.

3. **Using `groupby()` and `aggregate()` methods**:
   a. Group the dataset by 'sex' and find the mean age for each gender.
   b. Group the dataset by 'class' (passenger class) and find the maximum and minimum age in each class.
   c. Group the dataset by both 'sex' and 'class'. Find the total number of passengers and the average fare for each group.

4. **Using Pivot Tables**:
   a. Create a pivot table that shows the median age of passengers for each combination of 'sex' and 'class'.
   b. Create another pivot table that shows the total fare collected for each combination of 'embark_town' and 'deck'.
   c. Plot a heatmap using seaborn to visualize the results of any one of the above pivot tables.

