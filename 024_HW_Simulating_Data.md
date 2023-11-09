## Python/Numpy/Matplotlib Homework: Simulating Data

### Objective:
The goal of this homework is to practice data simulation and visualization techniques using Python with libraries such as Numpy and Matplotlib. You will create synthetic datasets that mimic certain properties and visualize them using different types of plots.

### Problem 1: Noisy Phase-Shifted Sine Waves

**Background:**
Sine waves are a mathematical curve that describes a smooth periodic oscillation. In real-life scenarios, such as the measurement of hormone levels in the body, the signals can often be modeled as sine waves with some noise.

**Task:**
1. Generate two noisy sine waves that represent the levels of two different hormones over time. Each sine wave should have:
    - 1000 points.
    - A frequency of 1 cycle in 24 hrs.
    - A noise level that is normally distributed with a mean of 0 and a standard deviation of 0.1.
    - A phase shift for the second hormone, representing a delay in its cycle compared to the first.

2. Plot the two sine waves on the same graph over a period of 10 days.
    - The x-axis should represent time in hours or days.
    - The y-axis should represent the hormone level.
    - Include a legend to differentiate between the two hormones.
    - Title the graph appropriately.

3. Ensure your plot has gridlines for better readability.

### Problem 2: Correlated Data and Marginal Distributions

**Background:**
Understanding the relationship between two variables is a fundamental aspect of statistical analysis. Scatter plots are a common visual tool for representing this relationship. Additionally, viewing the marginal distributions of each variable can provide insights into their individual characteristics.

**Task:**
1. Create a dataset containing 500 pairs of `x` and `y` values that are linearly correlated with:
    - A correlation coefficient approximately equal to 0.8.
    - Normally distributed residuals with a mean of 0 and standard deviation of 1.

2. Generate a scatterplot of the `x` and `y` values.
    - Label the x-axis as "Variable X".
    - Label the y-axis as "Variable Y".

3. Alongside the scatterplot, create two histograms representing the marginal distributions of `x` and `y`.
    - Position the histogram of `x` values above the scatterplot.
    - Position the histogram of `y` values to the right of the scatterplot.
    - Use subplots to create a clean layout.

4. Ensure all plots share their respective axes (x with x, and y with y).

