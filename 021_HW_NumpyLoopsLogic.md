**Homework: Loops and Logical Testing with NumPy**

**Objective:** To understand and implement for loops, while loops, and logical testing with NumPy arrays.

---

**Problem 1: Basic Array Element Comparisons**

Given the following NumPy array:
```python
import numpy as np
arr = np.array([2, 5, 8, 10, 3, 6, 7])
```

Write a Python script that checks and prints which elements of the array are even.

---

**Problem 2: Find Prime Array Elements**

Given a 1D NumPy integer array of arbitrary length, write a Python script that checks to see which elements are prime numbers, and builds a corresponding `True`/`False` array.

Pro Tip: Write a function to check if a single input number is prime, then call that function from within the `for()` loop used to iterate over the vector. This function will also contain a loop.

---

**Problem 3: Nested For Loops with 2D Arrays**

Suppose you have a 1D NumPy array `a` of shape `n x n`, initialized with zeros:

```python
import numpy as np
n = 10
a = np.zeros((n,n), dtype=int)
```

Write a Python script that fills this array with numbers from the Fibonacci sequence such that:

1. The Fibonacci sequence *starting with 0* runs across the first row.
2. Fibonacci sequences run down each column *starting with the number in the first row*.

Print the matrix.

Recall that the Fibonacci sequence starts with the numbers 0 and 1, and each subsequent number is the sum of the two preceding ones:

---

**Problem 4: While Loop Within a For Loop**

Given a list of NumPy arrays:
```python
arrays_list = [np.array([10, 20, 30, 40, 50]), np.array([5, 15, 25]), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])]
```

Write a Python script that:
1. Iterates over each array in the list using a for loop.
2. For each array, starts at the first element and sums consecutive elements using a while loop until the sum is greater than or equal to 50. The script should print the sum and the index where it stopped for each array.

---

**Problem 5: Logical Testing with NumPy**

Given a 2D NumPy array:
```python
data = np.array([[5, 8, 3], [7, 2, 9], [6, 4, 1]])
```

Write a Python script that Identifies and prints the location (row and column) of all elements that are greater than 6.





