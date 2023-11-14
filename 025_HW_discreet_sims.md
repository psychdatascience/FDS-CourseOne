### Homework Assignment: Discrete Distributions

---

#### Problem 1: Binomial Simulation of Card Drawing
- **Objective**: Simulate the probability of drawing a red or black card from a standard deck of 52 playing cards.
- **Task**:
  1. Use NumPy's binomial distribution function to simulate 100 trials of drawing a card.
  2. Assume the probability of drawing a red card is 0.5 (since there are 26 red and 26 black cards).
  3. Count the number of times a red card is drawn.
  4. Calculate the empirical probability of drawing a red card based on the simulation.
  5. Compare this probability with the assumed theoretical probability (i.e., is it around 0.5?).

#### Problem 2: Binomial vs. Gaussian Approximation
- **Objective**: Compare a simulated binomial distribution with its Gaussian approximation.
- **Task**:
  1. Re-do the above simulation 2000 times, storing the number of red cards drawn each time (might be a good time to write a function)
  2. Plot the distribution of red cards drawn.
  3. Compute the mean and standard deviation of the simulated distribution.
  4. Calculate the mean and standard deviation from the Gaussian approximation formulae; how do these compared with those from the simulations?

#### Problem 3: Simulating an Election in a Fictional Country
- **Objective**: Simulate election results based on polling data and voter turnout estimates in a fictional country with 4 states. The winner is by overall popular vote (there is no electoral college).
- **Task**:
  1. Assume each state has a different number of voters and different probabilities for voting for candidate A or B, based on fictional polling data.
  2. Also assume different voter turnout percentages for each state.
  3. Use the binomial distribution to simulate the voting process in each state.
  4. Calculate the total votes for each candidate and determine the winner.
  5. Perform the simulation a "large number" of times and plot the distribution along with a vertical line showing where the original outcome was.

#### Problem 4: Effects of Sample Size on the Distribution of Sums
- **Objective**. To see how the distribution of sums of discrete variables approachs a continuous Gaussian distribution with increasing addends. 
- **Task**.
  1. Rewrite the dice code from the tutorial to just store the sum on each set of rolls (rather than incrementing the counts of possible sums as we did in the tutorial).
  2. Functionlize the code such that your function takes 1) the number of dice to roll and 2) the number of rolls to do is input arguments, and returns a vector of the sums for all the rolls as output.
  3. Run the code for (``for()``)  2, 4, 8, 16, and 32 dice.
  4. Plot the results as overlaid KDEs like we did for the coin flips in the tutorial.



