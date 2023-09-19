## Python Looping Homework Assignment

### Part 1: `for` loops with lists and `range()`

#### 1. Lists:

a) Write a program (i.e. code cell) that takes a list of numbers and prints each number multiplied by 2.

Example Input: `[2, 4, 6, 8]`

Example Output:
```
4
8
12
16
```

b) Given a list of strings, write a program that prints out the elements of the string in reverse order without reversing the list itself.

Example Input: `["apple", "pear", "kiwi", "grape"]`

Example Output:
```
grape
kiwi
pear
apple
```

#### 2. Using the range() function:

a) Write code that uses a `for` loop and the `range()` function to print numbers 0 through 9.

b) Use the `range()` function to print numbers from 5 to 15.

c) Create a program that prints out the first 10 even numbers using the `range()` function.

### Part 2: Dictionaries and Loops

a) Create a dictionary where the keys are student names and the values are their favorite colors. Write a program that prints out each student's name and their favorite color.

Example Output:
```
Alex's favorite color is Blue.
Jordan's favorite color is Green.
Taylor's favorite color is Red.
```

b) Given a dictionary with product names as keys and their quantities as values, write a program that doubles the quantity of each product and prints out the updated quantities.

Example Input: `{"apple": 5, "banana": 3, "cherries": 10}`

Example Output:
```
apple now has 10.
banana now has 6.
cherries now have 20.
```

### Part 3: Storing Results of a For Loop in a New List and List Comprehensions
#### 1. not using list comprehension

a) Write a program that takes a list of numbers and creates a new list with each number multiplied by 2.

Example Input: `[1, 3, 5, 7]`

Example Output (new list): `[2, 6, 10, 14]`

b) Given a list of words, create a new list that contains the first letter of each word.

Example Input: `["Apple", "Banana", "Cherry", "Date"]`

Example Output (new list): `["A", "B", "C", "D"]`

#### 2. using list comprehension
c) Use a list comprehension to compute and save the square roots of a list of numbers from 1 to 10.

Input list: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

Expected Output: 
```
[1.0,
 1.4142135623730951,
 1.7320508075688772,
 2.0,
 2.23606797749979,
 2.449489742783178,
 2.6457513110645907,
 2.8284271247461903,
 3.0,
 3.1622776601683795]
```

d) Given a list of words, use a list comprehension to create a new list containing the last letter of each word.

Example Input: `["apple", "pear", "kiwi", "grape"]`

Expected Output: `["e", "r", "i", "e"]`

---

### Part 4: nested loops

a) Write some code to "flatten" the following list-of-lists-of-lists:
```
deep_list = [[[1, 2, 3, 4], [5, 6, 7, 8]],
            [[9, 10, 11, 12], [13, 14, 15, 16]],
            [[17, 18, 19, 20], [21, 22, 23, 42]]]
```
(that is, make into a simple list of `ints`)

b) Write code that, given a list of strings like this:
```
myStrLst = ["able", "was", "I", "ere", "I", "saw", "elba"]
```
reverses ***both*** the order of the strings in the list ***and*** the order of the letters in each string.  

**Warning** This one is tough, and requires you put together a few of the skills we've learned, so don't get frustrated if it takes you a lot of trial and error! That's what coding is often like!
