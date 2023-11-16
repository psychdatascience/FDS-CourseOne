## FDS I Final Project

### Objective: 

Predict the winner of a presidential election between candidates "A" and "B" for a fictional county that uses an electoral college system.

The relevant data for the states is in stateData.csv. This has columns that give for each state:

* the population for each state
* the expected voter turnout for each state
* the current poll results indicating the percentage of voter that will vote for candidate "A"

The electoral college votes are for each state are 1/1000 of the population rounded up to the nearest integer.

Do 10,000 simulations of the election. Your report should include

* a plot of the sampling distribution of the popular vote for candidate "A" overlaid with a line indicating the best-fit normal distribution, with the area corresponding to "A" winning the popular vote shaded in a different color, and a vertical line indicating the win/loss cutoff value.
* a plot of the sampling distribution of electoral college votes, with a vertical line indicating the win/loss cutoff value.
* An estimate of the probability that candidate "A" will win the election.

The code should employ functions as much as possible.

