# Volatility Estimators¶

Get full version of MlFinLab

  

In finance, volatility (usually denoted by \\(\sigma\\)) is the degree of
variation of a trading price series over time, usually measured by the
standard deviation of logarithmic returns. Volatility is an essential metric
for trading, including short-term day trading and swings trading, in which the
primary focus is on daily and weekly price movements. In fact, volatility
estimates can provide a profit opportunity by identifying swings and helping
with bet and portfolio sizing. In order to find an edge in option trading, we
need an estimate of future realized volatility to trade against that implied
by the options. There are two types of volatility, historic volatility and
implied volatility. Historic volatility measures a time series of past market
prices, whereas implied volatility looks forward in time, being derived from
the market price of a market-traded derivative (in particular, an option). But
before we can forecast future volatility we need to be able to measure what it
has been in the past thanks to different historic volatility estimators. These
methods use some or all of the usually available daily prices that
characterize a traded security: open (O), high (H), low (L), and close (C).
The most common method used to estimate the historical volatility is the
close-to-close method. In this approach, the historical volatility is defined
as either the annualized variance or standard deviation of log returns.

\\[s^{2}=\frac{1}{N} \sum_{i=1}^{N}\left(x_{\mathrm{i}}-\bar{x}\right)^{2}\\]

where \\(x_{\mathrm{i}}\\) are the logarithmic returns, \\(\bar{x}\\) is the
mean return in the sample and N is the sample size.

Many different methods have been developed to estimate the historical
volatility.

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

    

  * [Volatility trading](https://www.wiley.com/en-us/Volatility+Trading%2C+%2B+Website%2C+2nd+Edition-p-9781118416723), Chapter 2 _by_ Euan Sinclair.

  * [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 19 _by_ Marcos Lopez de Prado.

* * *

## Parkinson Estimator¶

In 1980, Parkinson introduced the first advanced volatility estimator based
only on high and low prices (HL), which can be daily, weekly, monthly, or
other. Parkinson estimator is five times more efficient than the close-to-
close volatility estimator as it would need fewer time periods to converge to
the true volatility as it uses two prices from each period instead of just one
as with the close-to-close estimator. A slightly different versions of the
estimator are present in the literature. According to Sinclair, Parkinson
estimator is defined as:

\\[\sigma=\sqrt{\frac{1}{4 N \ln 2} \sum_{i=1}^{N}\left(\ln
\frac{h_{i}}{1_{i}}\right)^{2}}\\]

where \\(h_{\mathrm{i}}\\) is the high price in the trading period and
\\(l_{\mathrm{i}}\\) is the low price.

According to De Prado, the estimator can be defined as:

\\[\mathrm{E}\left[\frac{1}{T} \sum_{t=1}^{T}\left(\log
\left[\frac{H_{t}}{L_{t}}\right]\right)^{2}\right]=k_{1} \sigma_{H L}^{2}\\]

where \\(k_{1}=4 \log [2]\\), \\(H_{\mathrm{t}}\\) is the high price for bar
t, and \\(L_{\mathrm{t}}\\) is the low price for bar t.

The limitation of this estimator is that prices are only sampled discretely
because markets are only open for part of the day. This means that the
unobservable true price may not make a high or a low when we can actually
measure it, hence Parkison estimator will systematically underestimate
volatility.

### Implementation¶

The following function implemented in MlFinLab can be used to derive Parkinson
volatility estimator.

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

[![../_images/parkinson_sinclair.png](../_images/parkinson_sinclair.png)](../_images/parkinson_sinclair.png)

[![Code example
demo](../_images/example_small2.png)](../_images/example_small2.png)

[![../_images/parkinson_deprado.png](../_images/parkinson_deprado.png)](../_images/parkinson_deprado.png)

* * *

## Garman-Klass Estimator¶

Garman and Klass proposed in 1980 a volatility estimator that aimed to extend
Parkinson’s volatility by using not only the high and low but also the opening
and closing prices. During their research, Garman and Klass realized that
markets are most active during the opening and closing of a trading session.
Furthermore, they assumed the price change process is a geometric Brownian
motion with continuous diffusion. Given these assumptions, Garman-Klass
estimator is defined as:

\\[\sigma=\sqrt{\frac{1}{N} \sum_{i=1}^{N} \frac{1}{2}\left(\ln
\frac{h_{i}}{l_{i}}\right)^{2}-\frac{1}{N} \sum_{i=1}^{N}(2 \ln 2-1)\left(\ln
\frac{c_{i}}{c_{i-1}}\right)^{2}}\\]

where \\(h_{\mathrm{i}}\\) is the high price, \\(l_{\mathrm{i}}\\) is the low
price and \\(c_{\mathrm{i}}\\) is the closing price in the trading period.

The Garman-Klass volatility estimator tries to make the best use of the
commonly available price information and as such is up to eight time more
efficient than the close-to-close volatility estimator. However, like
Parkinson estimator, the Garman Klass estimator also provides a biased
estimate of volatility as its discrete sampling doesn’t allow to take into
account opening jumps in price and trend movements.

### Implementation¶

The following function implemented in MlFinLab can be used to derive Garman-
Klass volatility estimator.

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

[![../_images/garman_klass.png](../_images/garman_klass.png)](../_images/garman_klass.png)

* * *

## Rogers-Satchell Estimator¶

Volatility estimators like Parkinson’s and Garman-Klass have been shown to be
more efficient than the close-to-close volatility estimator. However, these
estimators assume that the underlying process follows a geometric Brownian
motion with zero drift, which isn’t always the case in real markets.
Particularly, during periods when the asset trends strongly, these estimators
then overestimate volatility. From this observation, Rogers and Satchell
proposed in 1991 a new estimator that allows for non zero drift:

\\[\sigma=\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(\ln
\frac{h_{i}}{c_{i}}\right)\left(\ln \frac{h_{i}}{o_{i}}\right)+\left(\ln
\frac{1_{i}}{c_{i}}\right)\left(\ln \frac{1_{i}}{o_{i}}\right)}\\]

where \\(h_{\mathrm{i}}\\) is the high price, \\(l_{\mathrm{i}}\\) is the low
price, \\(o_{\mathrm{i}}\\) is the opening price and \\(c_{\mathrm{i}}\\) is
the closing price in the trading period.

The main advantage of the Rogers-Satchell estimator is that it provides better
volatility estimates during periods when the asset trends strongly. The main
limitation of this estimator is the discrete sampling that doesn’t allow to
take into account opening jumps in price.

### Implementation¶

The following function implemented in MlFinLab can be used to derive Rogers-
Satchell volatility estimator.

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

[![../_images/rogers_satchell.png](../_images/rogers_satchell.png)](../_images/rogers_satchell.png)

* * *

## Yang-Zhang Estimator¶

Yang Zhang estimator is a volatility estimator that allows to overcome the
main limitation of Parkinson’s, Garman-Klass’s and Rogers-Satchell’s
estimators, that being the existing bias due to the discrete sampling as it
doesn’t account for the opening jumps in price. In fact, Yang Zhang devised in
2000 an estimator that combines the classical and Rogers-Satchell estimator,
showing that it has the minimum variance and is both unbiased and independent
of process drift and opening gaps.

\\[\sigma=\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(\ln
\frac{h_{i}}{c_{i}}\right)\left(\ln \frac{h_{i}}{o_{i}}\right)+\left(\ln
\frac{l_{i}}{c_{i}}\right)\left(\ln \frac{l_{i}}{o_{i}}\right)}\\]

where \\(h_{\mathrm{i}}\\) is the high price, \\(l_{\mathrm{i}}\\) is the low
price, \\(o_{\mathrm{i}}\\) is the opening price and \\(c_{\mathrm{i}}\\) is
the closing price in the trading period.

The efficiency of Yang-Zhang estimator has a peak value of 14, meaning that
using only two days’ data for this estimator gives the same accuracy as the
classical estimator using three week’s data. However, where the process is
dominated by opening jumps the efficiency reduces to almost one, which means
there is no improvement over the classical clos-to-close estimator.

### Implementation¶

The following function implemented in MlFinLab can be used to derive Yang-
Zhang volatility estimator.

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

[![../_images/yang_zhang.png](../_images/yang_zhang.png)](../_images/yang_zhang.png)

* * *

## Corwin-Shultz Estimator¶

Corwin-Schultz is a bid-ask spread estimator from daily high and low prices to
measure the bid-ask spread of shares, using the formula:

\\[S_{t}=\frac{2\left(e^{\alpha_{t}}-1\right)}{1+e^{\alpha_{t}}}\\]

where

\\[\alpha_{t}=\frac{\sqrt{2 \beta_{t}}-\sqrt{\beta_{t}}}{3-2
\sqrt{2}}-\sqrt{\frac{\gamma_{t}}{3-2 \sqrt{2}}}\\]

\\[\beta_{t}=\mathrm{E}\left[\sum_{j=0}^{1}\left[\log
\left(\frac{H_{t-j}}{L_{t-j}}\right)\right]^{2}\right]\\]

\\[\gamma_{t}=\left[\log \left(\frac{H_{t-1, t}}{L_{t-1,
t}}\right)\right]^{2}\\]

The estimator is based on the assumption that daily high prices are typically
buyer initiated and low prices are seller initiated, and therefore the ratio
of high-to-low prices for a day reflects both the fundamental volatility of
stock and its bid-ask spread. Furthermore, it assumes that the volatility
component of the high-to-low price ratio increases proportionately with the
length of trading interval whereas the component due to bid-ask spreads does
not. Corwin-Schultz estimation bias and the frequency of negative estimates
increase in liquid assets or when price volatility is high.

### Implementation¶

The following function implemented in MlFinLab can be used to derive Corwin-
Shultz estimator.

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

### Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

[![../_images/corwin_shultz.png](../_images/corwin_shultz.png)](../_images/corwin_shultz.png)

* * *

## Cho-Frees Estimator¶

Cho Frees estimator is a volatility estimator which eliminates, at least
asymptotically, the biases that are caused by the discreteness of observed
stock prices. Assuming that the observed prices are continuously monitored,
using the notion of how quickly the price changes rather than how much the
price changes an estimator is constructed:

\\[\hat{\sigma}^{2}=2 \hat{\mu} \delta /\left(\log \left(\delta+\hat{\mu}
\bar{\tau}_{n}\right)-\log \left(\delta-\hat{\mu}
\bar{\tau}_{n}\right)\right)\\]

where \\(\delta=\log (1+d)\\) being d a known constant (1/8 for the New York
Stock Exchange for example), \\(\hat{\mu}=\bar{\tau}_{n}^{-1} \log
\left(P\left(\tau_{n}\right)\right)\\) and \\(\bar{\tau}_{n}=\tau_{n} / n\\).

It is shown that this estimator has desirable asymptotic properties, including
consistency and normality. Also, it outperforms natural estimators for low and
middle-priced stocks. Further, simulation studies demonstrate that the
proposed estimator is robust to certain misspecifications in measuring the
time between price changes.

### Implementation¶

The following function implemented in MlFinLab can be used to derive Cho-Frees
estimator.

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

[![../_images/cho_frees.png](../_images/cho_frees.png)](../_images/cho_frees.png)

* * *

## First Exit Time Estimator¶

The first exit times estimator is a volatility estimator that derives from Cho
Frees estimator, and as the latter, it considers how quickly the price changes
rather than how much the price changes. The estimator is constructed by
considering a price corridor, \\(\Delta\\) up and \\(\Delta\\) down from the
initial spot price. Each time the upper or lower barrier of the corridor is
touched, the barrier is reset around the current price, and the times to reach
the barrier noted form a sequence of exit times from which the volatility is
estimated using the formula:

\\[\sigma=\frac{\Delta}{\sqrt{E[\tau]}}\\]

where \\(E[\tau]\\) is the sample mean of the hitting times after n
observations The sample volatility derived with this formula is biased unless
n is large, therefore we can derive the unbiased volatility by considering
this relationship between the two:

\\[E[f(\bar{\tau})]=\sigma\left(1+\frac{1}{4 n}\right)\\]

where \\(E[f(\bar{\tau})]\\) is the unbiased volatility.

This estimator assumes Brownian motion for the log-price process and a
negligible drift in prices, hence its estimates may be biased in periods of
time during which prices trends significantly.

### Implementation¶

The following function implemented in MlFinLab can be used to derive the first
exit times estimator.

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

[![../_images/first_exit_times.png](../_images/first_exit_times.png)](../_images/first_exit_times.png)

* * *

## Research Notebook¶

The following research notebook can be used to better understand the
volatility estimators.

[![Notebook demo](../_images/notebook7.png)](../_images/notebook7.png)

* * *

## References¶

  * [Sinclair, E. (2008) Volatility Trading. John Wiley & Sons, Hoboken, NJ.](https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781118662724.fmatter)

  * [Lopez de Prado, M. (2018) Advances in Financial Machine Learning. New York, NY: John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

  * [Parkinson, Michael H.. “The Extreme Value Method for Estimating the Variance of the Rate of Return.” The Journal of Business 53 (1980): 61-65.](https://www.cmegroup.com/trading/fx/files/michael_parkinson.pdf)

  * [Garman, M. B., and M. J. Klass. 1980. “On the Estimation of Security Price Volatilities from Historical Data.” Journal of Business 53:67–78.](http://janroman.dhis.org/finance/Stock%20Market/M.%20Garman%20and%20M.%20Klass.pdf)

  * [Rogers, L., S. Satchell, and Y. Yoon. 1994. “Estimating the Volatility of Stock Prices: A Comparison of Methods that Use High and Low Prices.” Applied Financial Economics 4:241–247.](https://www.researchgate.net/profile/L-Rogers/publication/24071335_Estimating_the_Volatility_of_Stock_Prices_A_Comparison_of_Methods_That_Use_High_and_Low_Prices)

  * [Yang, D., and Q. Zhang. 2000. “Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices.” Journal of Business 73:477–491.](http://www.atmif.com/papers/range.pdf)

  * [Corwin S.A. and Schultz P. (2012), A Simple Way to Estimate Bid-Ask Spreads from Daily High and Low Prices. The Journal of Finance, 67: 719-760](http://sites.nd.edu/scorwin/files/2019/11/Internet-Appendix_FINAL.pdf)

  * [Cho D, Frees E. “Estimating the Volatility of Discrete Stock Prices.” Working paper, University of Wisconsin-Madison, 1986.](https://www.jstor.org/stable/2328470)

