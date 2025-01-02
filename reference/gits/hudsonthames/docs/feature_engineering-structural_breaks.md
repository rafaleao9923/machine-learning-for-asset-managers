# Structural Breaks¶

Get full version of MlFinLab

  

This implementation is based on Chapter 17 of the book Advances in Financial
Machine Learning. Structural breaks, like the transition from one market
regime to another, represent the shift in the behaviour of market
participants.

The first market participant to notice the changes in the market can adapt to
them before others and, consequently, gain an advantage over market
participants who have not yet noticed market regime changes.

To quote Marcos Lopez de Prado, “Structural breaks offer some of the best
risk/rewards”.

We can classify the structural break in two general categories:

  1. **CUSUM tests** : These test whether the cumulative forecasting errors significantly deviate from white noise.

  2. **Explosiveness tests** : Beyond deviation from white noise, these test whether the process exhibits exponential growth or collapse, as this is inconsistent with a random walk or stationary process, and it is unsustainable in the long run.

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 17 _by_ Marcos Lopez de Prado. _Describes structural breaks in more detail._

  * [Testing for Speculative Bubbles in Stock Markets: A Comparison of Alternative Methods](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.511.6559&rep=rep1&type=pdf) _by_ Ulrich Homm _and_ Jorg Breitung. _Explains the Chu-Stinchcombe-White CUSUM Test in more detail._

  * [Tests of Equality Between Sets of Coefficients in Two Linear Regressions](http://web.sonoma.edu/users/c/cuellar/econ411/chow) _by_ Gregory C. Chow. _A work that inspired a family of explosiveness tests._

## CUSUM tests¶

### Chu-Stinchcombe-White CUSUM Test on Levels¶

We are given a set of observations \\(t = 1, ... , T\\) and we assume an array
of features \\(x_{i}\\) to be predictive of a value \\(y_{t}\\) .

\\[y_{t} = \beta_{t}x_{t} + \epsilon_{t}\\]

Authors of the **Testing for Speculative Bubbles in Stock Markets: A
Comparison of Alternative Methods** paper suggest assuming \\(H_{0} :
\beta_{t} = 0\\) and therefore forecast \\(E_{t-1}[\Delta y_{t}] = 0\\). This
allows working directly with \\(y_{t}\\) instead of computing recursive least
squares (RLS) estimates of \\(\beta\\) .

As \\(y_{t}\\) we take the log-price and calculate the standardized departure
of \\(y_{t}\\) relative to \\(y_{n}\\) (CUSUM statistic) with \\(t > n\\) as:

\\[\begin{split}\begin{equation} \begin{split} S_{n,t} & =
(y_{t}-y_{n})(\hat\sigma_{t}\sqrt{t-n})^{-1}, \ \ t>n \\\ \hat\sigma_{t}^{2} &
= (t-1)^{-1} \sum_{i=2}^{t}({\Delta y_{t_{i}}})^2 \\\ \end{split}
\end{equation}\end{split}\\]

With the \\(H_{0} : \beta_{t} = 0\\) hypothesis, \\(S_{n, t} \sim N[0, 1]\\) .

We can test the null hypothesis comparing CUSUM statistic \\(S_{n, t}\\) with
critical value \\(c_{\alpha}[n, t]\\), which is calculated using a one-sided
test as:

\\[c_{\alpha}[n, t] = \sqrt{b_{\alpha} + \log{[t-n]}}\\]

The authors in the above paper have derived using Monte Carlo method that
\\(b_{0.05} = 4.6\\) .

The disadvantage is that \\(y_{n}\\) is chosen arbitrarily, and results may be
inconsistent due to that. This can be fixed by estimating \\(S_{n, t}\\) on
backward-shifting windows \\(n \in [1, t]\\) and picking:

\\[\begin{equation} S_{t}= \sup_{n \in [1, t]} \\{ S_{n, t}\\}
\end{equation}\\]

#### Implementation¶

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

* * *

## Explosiveness tests¶

### Chow-Type Dickey-Fuller Test¶

The Chow-Type Dickey-Fuller test is based on an \\(AR(1)\\) process:

\\[y_{t} = \rho y_{t} + \varepsilon_{t}\\]

where \\(\varepsilon_{t}\\) is white noise.

This test is used for detecting whether the process changes from the random
walk (\\(\rho = 1\\)) into an explosive process at some time \\(\tau^{*}T\\),
\\(\tau^{*} \in (0,1)\\), where \\(T\\) is the number of observations.

So, the hypothesis \\(H_{0}\\) is tested against \\(H_{1}\\):

\\[\begin{split}\begin{equation} \begin{split} H_{0} & : y_{t} = y_{t-1} +
\varepsilon_{t} \\\ H_{1} & : y_{t}=\begin{cases} y_{t-1} + \varepsilon_{t} \
\text{for} \ \ t= 1, ..., \tau^*T \\\ \rho y_{t-1} + \varepsilon_{t} \
\text{for} \ \ t= \tau^*T+1, ..., T, \text{ with } \rho > 1 \end{cases}
\end{split} \end{equation}\end{split}\\]

To test the hypothesis, the following specification is being fit:

\\[\Delta y_{t} = \delta y_{t-1} D_{t}[\tau^*] + \varepsilon_{t}\\]

\\[\begin{split}\begin{equation} \begin{split} D_{t}[\tau^*] & = \begin{cases}
0 \ \text{if} \ \ t < \tau^*T \\\ 1 \ \text{if} \ \ t \geq \tau^*T \end{cases}
\end{split} \end{equation}\end{split}\\]

So, the hypothesis tested are now transformed to:

\\[\begin{split}\begin{equation} \begin{split} H_{0} & : \delta = 0 \\\ H_{1}
& : \delta > 1 \\\ \end{split} \end{equation}\end{split}\\]

And the Dickey-Fuller-Chow(DFC) test-statistics for \\(\tau^*\\) is:

\\[DFC_{\tau^*} = \frac{\hat\delta}{\hat\sigma_{\delta}}\\]

As described in the **Advances in Financial Machine Learning** :

The first drawback of this method is that \\(\tau^{*}\\) is unknown, and the
second one is that Chow’s approach assumes that there is only one break and
that the bubble runs up to the end of the sample.

To address the first issue, in the work **Tests for Parameter Instability and
Structural Change With Unknown ChangePoint** [available
here](https://pdfs.semanticscholar.org/77c9/86937d205592a007df3661778a5ed4fc4e38.pdf),
Andrews proposed to try all possible \\(\tau^{*}\\) in an interval \\(\tau^{*}
\in [\tau_{0}, 1 - \tau_{0}]\\)

For the unknown \\(\tau^{*}\\) the test statistic is the Supremum Dickey-
Fuller Chow which is the maximum of all \\(T(1 - 2\tau_{0})\\) values of
\\(DFC_{\tau^{*}}\\) :

\\[\begin{equation} SDFC = \sup_{\tau^* \in [\tau_0,1-\tau_0]} \\{
DFC_{\tau^*}\\} \end{equation}\\]

To address the second issue, the Supremum Augmented Dickey-Fuller test was
introduced.

#### Implementation¶

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

* * *

### Supremum Augmented Dickey-Fuller¶

This test was proposed by Phillips, Shi, and Yu in the work **Testing for
Multiple Bubbles: Historical Episodes of Exuberance and Collapse in the S &P
500** [available
here](http://korora.econ.yale.edu/phillips/pubs/art/p1498.pdf). The advantage
of this test is that it allows testing for multiple regimes switches (random
walk to bubble and back).

The test is based on the following regression:

\\[\Delta y_{t} = \alpha + \beta y_{t-1} + \sum_{l=1}^{L}{\gamma_{l} \Delta
y_{t-l}} + \varepsilon_{t}\\]

And, the hypothesis \\(H_{0}\\) is tested against \\(H_{1}\\):

\\[\begin{split}\begin{equation} \begin{split} H_{0} & : \beta \le 0 \\\ H_{1}
& : \beta > 0 \\\ \end{split} \end{equation}\end{split}\\]

The Supremum Augmented Dickey-Fuller fits the above regression for each end
point \\(t\\) with backward expanding start points and calculates the test-
statistic as:

\\[\begin{equation} SADF_{t} = \sup_{t_0 \in [1, t-\tau]}\\{ADF_{t_0, t}\\} =
\sup_{t_0 \in [1, t-\tau]}
\Bigg\\{\frac{\hat\beta_{t_0,t}}{\hat\sigma_{\beta_{t_0, t}}}\Bigg\\}
\end{equation}\\]

where \\(\hat\beta_{t_0,t}\\) is estimated on the sample from \\(t_{0}\\) to
\\(t\\), \\(\tau\\) is the minimum sample length in the analysis, \\(t_{0}\\)
is the left bound of the backwards expanding window, \\(t\\) iterates through
\\([\tau, ..., T]\\) .

In comparison to SDFC, which is computed only at time \\(T\\), the SADF is
computed at each \\(t \in [\tau, T]\\), recursively expanding the sample
\\(t_{0} \in [1, t - \tau]\\) . By doing so, the SADF does not assume a known
number of regime switches.

[![structural breaks](../_images/sadf.png)](../_images/sadf.png)

Image showing SADF test statistic with 5 lags and linear model. The SADF line
spikes when prices exhibit a bubble-like behavior, and returns to low levels
when the bubble bursts.¶

The model and the add_const parameters of the **get_sadf** function allow for
different specifications of the regression’s time trend component.

Linear model (model=’linear’) uses a linear time trend:

\\[\Delta y_{t} = \beta y_{t-1} + \sum_{l=1}^{L}{\gamma_{l} \Delta y_{t-l}} +
\varepsilon_{t}\\]

Quadratic model (model=’quadratic’) uses a second-degree polynomial time
trend:

\\[\Delta y_{t} = \beta y_{t-1} + \sum_{l=1}^{L}{\gamma_{l} \Delta y_{t-l}} +
\sum_{l=1}^{L}{\delta_{l}^2 \Delta y_{t-l}} + \varepsilon_{t}\\]

Adding a constant (add_const=True) to those specifications results in:

\\[\Delta y_{t} = \alpha + \beta y_{t-1} + \sum_{l=1}^{L}{\gamma_{l} \Delta
y_{t-l}} + \varepsilon_{t}\\]

and

\\[\Delta y_{t} = \alpha + \beta y_{t-1} + \sum_{l=1}^{L}{\gamma_{l} \Delta
y_{t-l}} + \sum_{l=1}^{L}{\delta_{l}^2 \Delta y_{t-l}} + \varepsilon_{t}\\]

respectively.

#### Implementation¶

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

The function used in the SADF Test to estimate the \\(\hat\beta_{t_0,t}\\) is:

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

Tip

**Advances in Financial Machine Learning** book additionally describes why log
prices data is more appropriate to use in the above tests, their computational
complexity, and other details.

The SADF also allows for explosiveness testing that doesn’t rely on the
standard ADF specification. If the process is either sub- or super martingale,
the hypotheses \\(H_{0}: \beta = 0, H_{1}: \beta \ne 0\\) can be tested under
these specifications:

Polynomial trend (model=’sm_poly_1’):

\\[y_{t} = \alpha + \gamma t + \beta t^{2} + \varepsilon_{t}\\]

Polynomial trend (model=’sm_poly_2’):

\\[log[y_{t}] = \alpha + \gamma t + \beta t^{2} + \varepsilon_{t}\\]

Exponential trend (model=’sm_exp’):

\\[y_{t} = \alpha e^{\beta t} + \varepsilon_{t} \Rightarrow log[y_{t}] =
log[\alpha] + \beta t^{2} + \xi_{t}\\]

Power trend (model=’sm_power’):

\\[y_{t} = \alpha t^{\beta} + \varepsilon_{t} \Rightarrow log[y_{t}] =
log[\alpha] + \beta log[t] + \xi_{t}\\]

Again, the SADF fits the above regressions for each end point \\(t\\) with
backward expanding start points, but the test statistic is taken as an
absolute value, as we’re testing both the explosive growth and collapse. This
is described in more detail in the **Advances in Financial Machine Learning**
book p. 260.

The test statistic calculated (SMT for Sub/Super Martingale Tests) is:

\\[SMT_{t} = \sup_{t_0 \in [1, t-\tau]} \Bigg\\{\frac{ | \hat\beta_{t_0,t} | }{\hat\sigma_{\beta_{t_0, t}}}\Bigg\\}\\]

From the book:

Parameter phi in range (0, 1) can be used (phi=0.5) to penalize large sample
lengths ( “this corrects for the bias that the \\(\hat\sigma_{\beta_{t_0,
t}}\\) of a weak long-run bubble may be smaller than the
\\(\hat\sigma_{\beta_{t_0, t}}\\) of a strong short-run bubble, hence biasing
method towards long-run bubbles” ):

\\[SMT_{t} = \sup_{t_0 \in [1, t-\tau]} \Bigg\\{\frac{ | \hat\beta_{t_0,t} | }{\hat\sigma_{\beta_{t_0, t}}(t-t_{0})^{\phi}}\Bigg\\}\\]

* * *

## Example¶

[![Code example
demo](../_images/example_medium5.png)](../_images/example_medium5.png)

* * *

## Presentation Slides¶

[![../_images/lecture8.png](../_images/lecture8.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3270269)

Note

  * pg 1-14: Structural Breaks

  * pg 15-24: Entropy Features

  * pg 25-37: Microstructural Features

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 8/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3270269)

  * [Homm, U. and Breitung, J., 2012. Testing for speculative bubbles in stock markets: a comparison of alternative methods. Journal of Financial Econometrics, 10(1), pp.198-231.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.511.6559&rep=rep1&type=pdf)

  * [Chow, G.C., 1960. Tests of equality between sets of coefficients in two linear regressions. Econometrica: Journal of the Econometric Society, pp.591-605.](http://web.sonoma.edu/users/c/cuellar/econ411/chow)

