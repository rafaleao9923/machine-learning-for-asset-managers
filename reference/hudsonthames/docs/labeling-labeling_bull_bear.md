# Bull Bear States¶

Get full version of MlFinLab

  

  

Bull and Bear are commonly mentioned market dynamics that assist in deploying
certain strategies. In this module, two algorithms for bull and bear market
detection have been implemented. Pagan and Sossounov’s and Lunde and
Timmermann’s algorithms are commonly used to detect different market regimes.

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [A simple framework for analysing bull and bear markets](https://onlinelibrary.wiley.com/doi/pdf/10.1002/jae.664) _by_ Pagan, A.R. and Sossounov, K.A.

  * [Duration dependence in stock prices: An analysis of bull and bear markets](https://repec.cepr.org/repec/cpr/ceprdp/DP4104.pdf) _by_ Lunde, A. and Timmermann, A.

* * *

## Pagan and Sossounov¶

Influenced by Bry and Boschan’s paper ([Cyclical Analysis of Time Series:
Selected Procedures and Computer Programs,
1971.](https://www.nber.org/system/files/chapters/c2145/c2145.pdf) ), Pagan
and Sossounov developed an algorithm to classify bull and bear states. The
classification goes through four different filtering methods. The filtering
steps are as followed:

  1. Use a window length for both directions to determine local extrema.

  2. Censor the first and last months to eliminate bias.

  3. Remove cycles with length shorter than the given parameter.

  4. Remove phases with length shorter than the given parameter unless if the change is greater than the threshold.

After each filtering method, the corresponding data undergoes an alternation
filter that combines consecutive peaks and troughs.

[![Code implementation
demo](../_images/implementation_medium9.png)](../_images/implementation_medium9.png)

## Lunde and Timmermann¶

Lunde and Timmermann’s algorithm is based on realizing the absolute change
from the highest or lowest point. Two parameters are used for Lunde and
Timmermann: \\(\lambda_1\\) and \\(\lambda_2\\). The parameters are considered
as switches that indicate the change of states.

[![Code implementation
demo](../_images/implementation_small7.png)](../_images/implementation_small7.png)

Tip

In their paper, Lunde and Timmermann consider both symmetric (\\(\lambda_1 =
\lambda_2 =0.2\\)) and asymmetric (\\(\lambda_1 = 0.2, \lambda_2 = 0.1\\))
parameters.

* * *

## Example¶

Below is an example on how to create labels for bull and bear detection.

[![Code example
demo](../_images/example_medium7.png)](../_images/example_medium7.png)

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Pagan, A.R. and Sossounov, K.A., 2003. A simple framework for analysing bull and bear markets. Journal of applied econometrics, 18(1), pp.23-46.](https://onlinelibrary.wiley.com/doi/pdf/10.1002/jae.664)

  * [Lunde, A. and Timmermann, A., 2004. Duration dependence in stock prices: An analysis of bull and bear markets. Journal of Business & Economic Statistics, 22(3), pp.253-273.](https://repec.cepr.org/repec/cpr/ceprdp/DP4104.pdf)

