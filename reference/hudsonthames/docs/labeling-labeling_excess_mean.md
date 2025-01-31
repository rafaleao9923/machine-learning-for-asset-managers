# Excess Over Mean¶

Get full version of MlFinLab

  

  

Using cross-sectional data on returns of many different stocks, each
observation is labeled according to whether, or how much, its return exceeds
the mean return. It is a common practice to label observations based on
whether the return is positive or negative. However, this may produce
unbalanced classes, as during market booms the probability of a positive
return is much higher, and during market crashes they are lower (Coqueret and
Guida, 2020). Labeling according to a benchmark such as mean market return
alleviates this issue.

A dataframe containing forward returns is calculated from close prices. The
mean return of all stocks at time \\(t\\) in the dataframe is used to
represent the market return, and excess returns are calculated by subtracting
the mean return from each stock’s return over the time period \\(t\\). The
numerical returns can then be used as-is (for regression analysis), or can be
relabeled to represent their sign (for classification analysis).

At time \\(t\\):

\begin{gather*} P_t = \\{p_{t,0}, p_{t,1}, ..., p_{t,n}\\} \\\ R_t =
\\{r_{t,0}, r_{t,1}, ..., r_{t,n}\\} \\\ \mu_t = mean(R_t) \\\ L(R_t) =
\\{r_{t,0} - \mu_t, r_{t,1} - \mu_t, ..., r_{t,n} - \mu_t\\} \end{gather*}

If categorical rather than numerical labels are desired:

\\[\begin{split}\begin{equation} \begin{split} L(r_{t,n}) = \begin{cases} -1
&\ \text{if} \ \ r_{t,n} - \mu_t < 0\\\ 0 &\ \text{if} \ \ r_{t,n} - \mu_t =
0\\\ 1 &\ \text{if} \ \ r_{t,n} - \mu_t > 0\\\ \end{cases} \end{split}
\end{equation}\end{split}\\]

If desired, the user can specify a [resampling
period](https://pandas.pydata.org/pandas-
docs/stable/user_guide/timeseries.html#dateoffset-objects) to apply to the
price data prior to calculating returns. The user can also lag the returns to
make them forward-looking.

The following shows the distribution of numerical excess over mean for a set
of 20 stocks for the time period between Jan 2019 and May 2020.

[![labeling over
mean](../_images/distribution_over_mean.png)](../_images/distribution_over_mean.png)

Distribution of returns over mean for 20 stocks.¶

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [Machine Learning for Factor Investing](http://www.mlfactor.com/), Chapter 5.5.1 _by_ Coqueret, G. and Guida, T.

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium9.png)](../_images/implementation_medium9.png)

* * *

## Example¶

Below is an example on how to create labels of excess over mean.

[![Code example
demo](../_images/example_medium7.png)](../_images/example_medium7.png)

* * *

## Research Notebook¶

The following research notebooks can be used to better understand labeling
excess over mean.

[![Notebook demo](../_images/notebook9.png)](../_images/notebook9.png)

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Coqueret, G. and Guida, T., 2020. Machine Learning for Factor Investing. CRC Press.](http://www.mlfactor.com/)

