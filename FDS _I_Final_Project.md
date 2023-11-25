## FDS I Final Project

### Objective: 

Predict the % chance that candidate "Barnes" will beat candidate "Noble" for a fictional country with 11 states  that uses an electoral college system.

The data you get are:

* A list of the state populations (vector)

* A set of polling data (% estimated to vote for candidate "A") for each state from seven national polling entities (matrix)

* A list of the estimated quality of each of 7 polling entities (company, university, think tank, etc.) (vector). Higher numbers are better (e.g. the poll is considered more reliable)

The facts you know about the data are

* Each state gets awarded 1 electoral college vote per 1000 people in the state.
* Everybody votes; voter turnout is 100%
* The state populations are fixed (obviously)
* The quality of the polls can be considered fixed (there has to uncertainty associated with these ratings but we don't know what it is, so we'll consider them to be constants)
* each poll was based on 2000 people in each state

---

The starter notebook will work us through the basic analysis of predicting the election winner based on the data at hand. In other words, it will provide the basic code for a single simulation without any added variability. Your mission (and you have no choice but to accept it!), will be to package this code into a loop that will predict the outcomes of many elections given known variability, namely, that the polls cannot be perfectly accurate; they are subject to ***binomial*** variability.

---

Once your code is finished, debugged, and ready to go, do 10,000 simulations of the election!

*Make sure and put a `rnd.seed(42)` just before your simulation runs do that all our results are comparable.*

The post-simulation part of your notebook should include:

* a plot of the sampling distribution of the popular vote for candidate "A" 

  - overlaid with a line indicating the best-fit normal distribution, 

  * with the area corresponding to "A" winning the popular vote shaded in a different color, 
  * and a vertical line indicating the win/loss cutoff value.

* a plot of the sampling distribution of electoral college votes, with a vertical line indicating the win/loss cutoff value.

* An estimate of the probability that candidate "A" will win the election (i.e. win the electoral vote)

---

This almost goes without saying but, along the way, in the pre-simulation part of your notebook, feel free to make plots that you might think help you or your potential audience. 
