# Raw Returns¶

Get full version of MlFinLab

  

  

Labeling data by raw returns is the most simple and basic method of labeling
financial data for machine learning. Raw returns can be calculated either on a
simple or logarithmic basis. Using returns rather than prices is usually
preferred for financial time series data because returns are usually
stationary, unlike prices. This means that returns across different assets, or
the same asset at different times, can be directly compared with each other.
The same cannot be said of price differences, since the magnitude of the price
change is highly dependent on the starting price, which varies with time.

The simple return for an observation with price \\(p_t\\) at time \\(t\\)
relative to its price at time \\(t-1\\) is as follows:

\\[R_t = \frac{p_{t}}{p_{t-1}} - 1\\]

And the logarithmic return is:

\\[r_t = log(p_t) - log(p_{t-1})\\]

The label \\(L_t\\) is simply equal to \\(r_t\\), or to the sign of \\(r_t\\),
if binary labeling is desired.

\\[\begin{split}\begin{equation} \begin{split} L_{t} = \begin{cases} -1 &\
\text{if} \ \ r_t < 0\\\ 0 &\ \text{if} \ \ r_t = 0\\\ 1 &\ \text{if} \ \ r_t
> 0 \end{cases} \end{split} \end{equation}\end{split}\\]

If desired, the user can specify a resampling period to apply to the price
data prior to calculating returns. The user can also lag the returns to make
them forward-looking.

The following shows the distribution of logarithmic daily returns on Microsoft
stock during the time period between January 2010 and May 2020.

[![raw returns
image](../_images/Raw_returns_distribution.png)](../_images/Raw_returns_distribution.png)

Distribution of logarithmic returns on MSFT.¶

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium9.png)](../_images/implementation_medium9.png)

* * *

## Example¶

Below is an example on how to use the raw returns labeling method.

[![Code example
demo](../_images/example_medium7.png)](../_images/example_medium7.png)

* * *

## Research Notebook¶

The following research notebook can be used to better understand the raw
return labeling technique.

[![Notebook demo](../_images/notebook9.png)](../_images/notebook9.png)

* * *

## Presentation Slides¶

  

