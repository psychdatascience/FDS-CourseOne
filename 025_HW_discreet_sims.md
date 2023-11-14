### Homework Assignment: Discrete Distributions

---

#### Problem 1: Binomial Simulation of Card Drawing
- **Objective**: Simulate the probability of drawing a red or black card from a standard deck of 52 playing cards.
- **Task**:
  1. Use NumPy's binomial distribution function to simulate 100 trials of drawing a card.
  2. Assume the probability of drawing a red card is 0.5 (since there are 26 red and 26 black cards).
  3. Count the number of times a red card is drawn.
  4. Calculate the empirical probability of drawing a red card based on the simulation.
  5. Compare this probability with the assumed theoretical probability.

#### Problem 2: Binomial vs. Gaussian Approximation
- **Objective**: Compare a simulated binomial distribution with its Gaussian approximation.
- **Task**:
  1. Re-do the above simulation 2000 times, storing the number of red cards drawn each time (might be a good time to write a function)
  2. Plot the distribution of red cards drawn.
  3. Compute the mean and standard deviation of the simulated distribution.
  4. Calculate the mean and standard deviation from the Gaussian approximation formulae; how do these compared with those from the simulations?

#### Problem 3: Simulating an Election in a Fictional Country
- **Objective**: Simulate election results based on polling data and voter turnout estimates in a fictional country with 4 states.
- **Task**:
  1. Assume each state has a different number of voters and different probabilities for voting for candidate A or B, based on fictional polling data.
  2. Use the binomial distribution to simulate the voting process in each state.
  3. Assume certain voter turnout percentages for each state.
  4. Calculate the total votes for each candidate and determine the winner.
  5. Perform the simulation multiple times and discuss the variability in election outcomes.



rewrite the dice code to just store the sums, then use seaboard hist to overlay the plots below...

Increase `k` incrementally (e.g., 2, 5, 10, 20) and observe how the distribution evolves. Illustrate how, as `k` increases, the distribution approximates a normal distribution.

\# Simulate different numbers of dice

dice_counts = [2, 5, 10, 20]

for num_dice in dice_counts:

​    plot_dice_roll_distribution(num_dice, 1000)

