## FDS I Final Project

### Objective: 

Predict the % chance that candidate "A" will beat "B" for a fictional country with 11 states  that uses an electoral college system.

The data you get are:

* A list of the state populations (vector)

* A set of polling data (% estimated to vote for candidate "A") for each state from seven national polling entities (matrix)

* A list of the estimated quality of each polling entity (company, university, think tank, etc.) (vector)

The facts you know about the data are

* Each state gets awarded 1 electoral college vote per 1000 people in the state.

* Everybody votes; voter turnout is 100%

* The state populations are fixed (obviously)

* The quality of the polls can be considered fixed (there has to uncertainty associated with these ratings but we don't know what it is, so we'll consider them to be constants)

---

Once your code is finished, debugged, and ready to go, do 10,000 simulations of the election!

The post-simulation part of your notebook should include:

* a plot of the sampling distribution of the popular vote for candidate "A" 

  - overlaid with a line indicating the best-fit normal distribution, 

  * with the area corresponding to "A" winning the popular vote shaded in a different color, 
  * and a vertical line indicating the win/loss cutoff value.

* a plot of the sampling distribution of electoral college votes, with a vertical line indicating the win/loss cutoff value.

* An estimate of the probability that candidate "A" will win the election (i.e. win the electoral vote)

---

This almost goes without saying but, along the way, in the pre-simulation part of your notebook, feel free to make plots that you might think help you or your potential audience. 
