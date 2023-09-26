## Python Programming Homework: Functions, Modules, and Namespaces

### Objective:
The purpose of this homework is to reinforce your understanding of functions, namespaces, and Python modules. By the end of the assignment, you should be more familiar with organizing and structuring your Python code using these concepts.

---

### Task Overview:

1. **Function Design for Unit Conversions**: Write functions for basic conversions between imperial and metric units.
2. **Module Creation**: Organize your conversion functions into a custom Python module.
3. **Namespace Exploration**: Demonstrate an understanding of local and global scopes and their implications.

---

### Detailed Requirements:

1. #### Function Design for Unit Conversions:
    - Design and implement functions for the following conversions:
        - Miles to Kilometers and vice versa.
        - Fahrenheit to Celsius and vice versa.
        - Kilograms to Pounds and vice versa.
    - Each conversion should have its dedicated function. For instance, `miles_to_km()`, `km_to_miles()`, etc.
    - Each function should `return` its answer (not just print it).

2. #### Module Creation:
    - Organize all the conversion functions you've created into a Python module named `unit_conversions.py`.
    - In a separate script, import your module and demonstrate the use of each function.

3. #### Namespaces
   - Make a module with filename "mylen.py"
       * add a function named `len` to the module
       * the function should return the number 42 no matter what
   - Create a list `mylist` (or whatever) with some elements in it (they can be numbers or anything)
   - ***Before importing you module***, try a `len(mylise)`
   - Import mylen.py (`import mylen`)
       * verify that `mylen.len()` works as expected
   - Now do a `from mylen import len`
   - Finally, repeat the `len(mylist)`

In your own words, compare the outputs of the two `len(mylest)` calls. What happened? Why? What does this tell you about the egalitarian nature of Python?

---

### Hints and Tips:

- Ensure each function handles user input effectively and returns results in a clear format.
- Test each function thoroughly to ensure accurate conversions.
- Comment your code!

---

###  Submission :

1. Your main notebook demonstrating the use of your module converted to pdf
2. A link to your notebook on GitHub as usual
3. A link to your `unit_conversions.py` module containing your functions.

---