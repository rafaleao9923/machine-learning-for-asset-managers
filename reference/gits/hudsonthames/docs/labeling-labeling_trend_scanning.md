# Trend Scanning¶

Get full version of MlFinLab

  

  

[![../_images/trend_scanning_plot.png](../_images/trend_scanning_plot.png)](../_images/trend_scanning_plot.png)

Trend Scanning is both a classification and regression labeling technique
introduced by Marcos Lopez de Prado in the following lecture slides: [Advances
in Financial Machine Learning: Lecture 3/10 (seminar
slides)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257419), and
again in his text book [Machine Learning for Asset
Managers](https://www.cambridge.org/core/books/machine-learning-for-asset-
managers/6D9211305EA2E425D33A9F38D0AE3545).

[![trend scanning backward-
looking](../_images/trend_scanning_backward.png)](../_images/trend_scanning_backward.png)

Result of applying backward-looking Trend scanning to EEM ETF daily close
prices. The colour of a point in the plot represents the t-value.¶

For some trading algorithms, the researcher may not want to explicitly set a
fixed profit / stop loss level, but rather detect overall trend direction and
sit in a position until the trend changes. For example, market timing strategy
which holds ETFs except during volatile periods. Trend scanning labels are
designed to solve this type of problems.

This algorithm is also useful for defining market regimes between downtrend,
no-trend, and uptrend.

Implementation in the MlFinLab package supports both forward-looking and
backward-looking window approaches.

The idea of forward-looking trend-scanning labels are to fit multiple
regressions from time t to t + L (L is a maximum observation window) and
select the one which yields maximum t-value for the slope coefficient, for a
specific observation. For the backward-looking trend-scanning labels the
regressions are fit from time t to t - L.

Tip

  1. Classification: By taking the sign of t-value for a given observation we can set {-1, 1} labels to define the trends as either downward or upward.

  2. Classification: By adding a minimum t-value threshold you can generate {-1, 0, 1} labels for downward, no-trend, upward.

  3. The t-values can be used as sample weights in classification problems.

  4. Regression: The t-values can be used in a regression setting to determine the magnitude of the trend.

The output of this algorithm is a DataFrame with t1 (time stamp for the
farthest observation), t-value, returns for the trend, and bin. The user can
also specify MAE/MSE metric used to define best-fit linear regression by
change the value of **metric** parameter in the function call.

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [Advances in Financial Machine Learning: Lecture 3/10 (seminar slides)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257419) _by_ Marcos Lopez de Prado.

  * [Machine Learning for Asset Managers](https://www.cambridge.org/core/books/machine-learning-for-asset-managers/6D9211305EA2E425D33A9F38D0AE3545) _by_ Marcos Lopez de Prado.

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium9.png)](../_images/implementation_medium9.png)

* * *

## Example¶

[![Code example
demo](../_images/example_medium7.png)](../_images/example_medium7.png)

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 8/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257419)

  * [de Prado, M.L., 2020. Machine learning for asset managers. Cambridge University Press.](https://www.cambridge.org/core/books/machine-learning-for-asset-managers/6D9211305EA2E425D33A9F38D0AE3545)

