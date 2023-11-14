compare empirical with normal approx for binom



rewrite the dice code to just store the sums, then use seaboard hist to overlay the plots below...

Increase `k` incrementally (e.g., 2, 5, 10, 20) and observe how the distribution evolves. Illustrate how, as `k` increases, the distribution approximates a normal distribution.

\# Simulate different numbers of dice

dice_counts = [2, 5, 10, 20]

for num_dice in dice_counts:

​    plot_dice_roll_distribution(num_dice, 1000)

