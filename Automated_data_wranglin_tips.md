### Automated data wranglin' tips

Assume we've imported `pandas` as `pd` and `numpy` as `np`...

If we've loaded our data `.csv` file into a data frame `df`, then

`df.shape` is your friend: it will give you the number of columns (which will be 4) and the number of rows (observations per 2x2 cell).

Then, `np.repeat()` and `np.tile()` are you new BFFs!

Once we've used our BFFs to make the levels of the two dependent variables as the future columns of our new long "tidy" formatted data, then it's time to make the column of the measurements. Here, `df.values.reshape()` is our new bestie.

Now that you have your 3 columns, make a `dict` out of them, and turn them into a `pd.DataFrame`, and we're done!

