# Return Versus Benchmark¶

Get full version of MlFinLab

  

  

Labeling versus benchmark is featured in the paper [Evaluating multiple
classifiers for stock price direction prediction, by Ballings et al.,
2015.](https://www.sciencedirect.com/science/article/abs/pii/S0957417415003334)
In this paper, the authors label yearly forward stock returns against a
predetermined benchmark, and use that labeled data to compare the performance
of several machine learning algorithms in predicting long term price
movements.

Labeling against benchmark is a simple method of labeling financial data in
which time-indexed returns are labeled according to whether they exceed a set
value. The benchmark can be either a constant value, or a pd.Series of values
with an index matching that of the returns. The labels can be the numerical
value of how much each observation’s return exceeds the benchmark, or the sign
of the excess.

At time \\(t\\), given that price of a stock is \\(p_{t, n}\\), benchmark is
\\(B_t\\) and return is:

\\[r_{t,n} = \frac{p_{t,n}}{p_{t-1,n}} - 1\\]

Note that \\(B_t\\) is a scalar value corresponding to the benchmark at time
\\(t\\), while \\(B\\) is the vector of all benchmarks across all timestamps.
The labels are:

\\[L(r_{t,n}) = r_{t,n} - B_t\\]

If categorical labels are desired:

\\[\begin{split}\begin{equation} \begin{split} L(r_{t, n}) = \begin{cases} -1
&\ \text{if} \ \ r_{t,n} < B_t\\\ 0 &\ \text{if} \ \ r_{t,n} = B_t\\\ 1 &\
\text{if} \ \ r_{t,n} > B_t\\\ \end{cases} \end{split}
\end{equation}\end{split}\\]

The simplest method of labeling is just returning the sign of the return.
However, sometimes it is desirable to quantify the return compared to a
benchmark to better contextualize the returns. This is commonly done by using
the mean or median of multiple stocks in the market. However, that data may
not always be available, and sometimes the user might wish a specify a
constant or more custom benchmark to compare returns against. Note that these
benchmarks are unidirectional only. If the user would like a benchmark that
captures the absolute value of the returns, then the fixed horizon method
should be used instead.

If desired, the user can specify a [resampling
period](https://pandas.pydata.org/pandas-
docs/stable/user_guide/timeseries.html#dateoffset-objects) to apply to the
price data prior to calculating returns. The user can also lag the returns to
make them forward-looking. In the paper by Ballings et al., the authors use
yearly forward returns, and compare them to benchmark values of 15%, 25%, and
35%.

The following shows the returns for MSFT stock during March-April 2020,
compared to the return of SPY as a benchmark during the same time period.
Green dots represent days when MSFT outperformed SPY, and red dots represent
days when MSFT underperformed SPY.

[![labeling vs
benchmark](../_images/MSFT_Return_vs_Benchmark.png)](../_images/MSFT_Return_vs_Benchmark.png)

Comparison of MSFT return to SPY return.¶

Note

**Underlying Literature**

This labeling method is sourced from the following: \- Chapter 5.5.1 of
**Machine Learning for Factor Investing** , _by_ Coqueret, G. and Guida, T.
(2020).

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium9.png)](../_images/implementation_medium9.png)

* * *

## Example¶

Below is an example on how to use the return over benchmark labeling technique
on real data.

[![Code example
demo](../_images/example_medium7.png)](../_images/example_medium7.png)

* * *

## Research Notebook¶

The following research notebook can be used to better understand the return
against benchmark labeling technique.

[![Notebook demo](../_images/notebook9.png)](../_images/notebook9.png)

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Ballings, M., Van den Poel, D., Hespeels, N. and Gryp, R., 2015. Evaluating multiple classifiers for stock price direction prediction. Expert systems with Applications, 42(20), pp.7046-7056.](https://www.sciencedirect.com/science/article/abs/pii/S0957417415003334)

