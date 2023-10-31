**Homework Assignment: Basic Plotting with Matplotlib**

**Objective:**  
Gain proficiency in creating basic plots using Matplotlib, and understand the difference between the `pyplot` approach and the object-oriented `ax` methods.

**Tools to be used:**  
- Python
- Matplotlib library

**Part 1: Using `pyplot.plot`**

1. **Basic Line Plot:**  
   a. Generate a list of numbers from 0 to 10, incremented by 0.5.  
   b. Plot the numbers against their square values using an available style of your choice.  
   c. Label the x-axis as 'X', the y-axis as 'X^2', and give the plot a title "Plot of X vs X^2".

2. **Plot Annotations:**  
   a. Use the plot from 1.b.  
   b. Annotate the point (5, 25) with the text "This is (5,25)".  
   c. Highlight the point (5, 25) with a red circle.  

**Part 2: Using Object-Oriented `ax` methods**

3. **Basic Line Plot:**  
   a. Generate a list of numbers from -10 to 10, incremented by 1.  
   b. Create a subplot object and plot the numbers against their cube values.  
   c. Label the x-axis as 'Y', the y-axis as 'Y^3', and give the plot a title "Plot of Y vs Y^3".
4. **Plot Annotations (using `ax`):**  
   a. Use the plot from 3.b.  
   b. Annotate the point (-5, -125) with the text "This is (-5,-125)".  
   c. Highlight the point (-5, -125) with a blue circle.  
5. **Combining Plots:**  
   a. Plot both functions (X^2 and Y^3) on the same figure, using different colors for each function.  
   b. Add a legend for the two plots
6. **Functional Plotting:**  
   a. Write a function to plot its two input arguments, y and x, against one another. It should label the y-axis "activity" and the x-axis "time", and have a good looking style.  
   b. Test your function with python list and numpy 1D array inputs. (and does it work with one of each?).  
   c. Add a third argument to let the users choose between a solid line, circle markers, or both.  
   

Pro Tips: 

* to highlight a single point on a plot, try adding a `.scatter()` plot of a single point to your `axes`
* in general, a function that does plotting using `matplotlib` should return a `figure` (i.e. `fig`) object
