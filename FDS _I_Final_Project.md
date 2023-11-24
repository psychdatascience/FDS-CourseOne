## FDS I Final Project

### Objective: 

Predict the chance that candidate "A" will beat "B" for a fictional country that uses an electoral college system.

The data you get are:

    * A list of the state populations (vector)

    * A set of polling data (% estimated to vote for candidate "A") for each state from a few national polling entities (matrix)

    * A list of the estimated quality of each polling entity (company, university, think tank, etc.) (vector)

The facts you know about the data are

    * Each state gets awarded 1 electoral college vote per 1000 people in the state.

    * Everybody votes; voter turnout is 100%

Do 10,000 simulations of the election. Your report should include

* a plot of the sampling distribution of the popular vote for candidate "A" overlaid with a line indicating the best-fit normal distribution, with the area corresponding to "A" winning the popular vote shaded in a different color, and a vertical line indicating the win/loss cutoff value.
* a plot of the sampling distribution of electoral college votes, with a vertical line indicating the win/loss cutoff value.
* An estimate of the probability that candidate "A" will win the election.

The code should employ functions as much as possible.

