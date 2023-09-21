**Homework Assignment: Control Structures**

**Objective**: To gain hands-on experience with `if` statements and `while` loops in Python.

---

**0. Logic:**

a) Write come code that determines whether either of the letters in `test_strs = [“y”, “o”]` are in the string `comp_str = “Hello World!”`.

b) In logic and computing there is a comparison called an “exclusive or” or “xor”. An xor test produces `True`(or 1) only when one *but not both* of its inputs are `True`. Note that this is different than an `or`, which yields `True` if *either* input is true. Write a line of code that performs an xor on two Boolean variables, a and b, using the tests we know about: `and`, `or`, and `not`. Test you code for all four possible combinations of a and b.

**1. Age Category:**

Write a program that:  

a) Asks the user to input their age.  
b) Based on the age, classifies them into one of the following categories:

  - Infant (0-2 years)
  - Child (3-12 years)
  - Teenager (13-19 years)
  - Adult (20-64 years)
  - Senior (65 years and above)

*Hint*: Use the `if-elif-else` structure.

---

**2. Number Classifier:**

Ask the user to input a number. Write a program to:  

a) Check if the number is positive, negative, or zero.  
b) Check if the number is even or odd.  

Sample output: “Your number, 42, is positive and even."

—

**3. Simple Calculator:**

Design a calculator that can perform addition, subtraction, 
multiplication, and division. The program should:  

a) Ask the user to input two numbers.  
b) Ask the user to select an operation.  
c) Perform the selected operation on the two numbers and display the 
result.  

Make sure to handle invalid operations with an appropriate error message.

---

**4. Guessing Game:**

a) The program should produce a random answer between 1 and 10.  

    - use `import random` (we only have to do this once, at the top of the program)
    - then `answer = random.randint()` to get the random answer
    
b) Ask the user to guess the number.  
c) Provide hints like "Too High" or "Too Low" based on the user's guess.  
d) The user should have some maximum number of attempts.  
e) After the maximum number of incorrect attempts or if the user guesses correctly, reveal the 
correct number.  

---

**5. Counter Contrast:**

Write two versions of a program that asks the user for a positive integer 
`n` and then prints the numbers from 1 up to `n`.  

a) First, use a `for` loop.  
b) Next, use a `while` loop.  

Which loop structure do you prefer in this context, and why?  

---

**6. Multiplication Table:**

Write a program that:  

a) Asks the user for a number `n`.  
b) Generates and prints the multiplication table for the number up to 10.  

For example, if the user inputs `5`, the output should be:  
```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

Implement this twice:  
a) Using a `for` loop.  
b) Using a `while` loop.  

Which loop structure do you think is better in this context, and why?  

---

Think about writing a program for which the user must enter a positive number. If they don't, the program should prompt them again until they do.    

Would you use a `for` loop or a `while` loop to do this? Why?  

---

**Notes**:

- Make sure to comment your code! We don’t heavily comment the code in the tutorials, because we want you to focus on reading the code itself but, in practice, you should comment, comment, comment!
- Ensure your program handles unexpected inputs gracefully.
