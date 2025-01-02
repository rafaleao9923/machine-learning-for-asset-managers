# Combinatorial Purged CV (CPCV)¶

Get full version of MlFinLab

  

  

This implementation is based on Chapter 12 of the book [Advances in Financial
Machine Learning](https://www.wiley.com/en-
us/Advances+in+Financial+Machine+Learning-p-9781119482086).

Given a number φ of backtest paths targeted by the researcher, CPCV generates
the precise number of combinations of training/testing sets needed to generate
those paths, while purging training observations that contain leaked
information.

CPCV can be used for both for cross-validation and backtesting. Instead of
backtesting using single path, the researcher may use CPCV to generate various
train/test splits resulting in various paths.

CPCV algorithm:

>   1. Partition T observations into N groups without shuffling, where groups
> n = 1, … , N − 1 are of size [T∕N], and the Nth group is of size T − [T∕N]
> (N − 1).
>
>   2. Compute all possible training/testing splits, where for each split N −
> k groups constitute the training set and k groups constitute the testing
> set.
>
>   3. For any pair of labels (y_i , y_j), where y_i belongs to the training
> set and y j belongs to the testing set, apply the PurgedKFold class to purge
> y_i if y_i spans over a period used to determine label y j . This class will
> also apply an embargo, should some testing samples predate some training
> samples.
>
>   4. Fit classifiers ( N ) on the N−k training sets, and produce forecasts
> on the respective N−k testing sets.
>
>   5. Compute the φ [N, k] backtest paths. You can calculate one Sharpe ratio
> from each path, and from that derive the empirical distribution of the
> strategy’s Sharpe ratio (rather than a single Sharpe ratio, like WF or CV).
>
>   6. When combinatorial splits were generated, CombinatorialPurgedKFold
> class contains backtest paths formed from train/test splits.
>
>

[![Combinatorial Cross-
Validation](../_images/combinatorial_cv.png)](../_images/combinatorial_cv.png)

Image showing splits for **CPCV(6,2)**¶

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_small2.png)](../_images/implementation_small2.png)

[![Code implementation
demo](../_images/implementation_medium4.png)](../_images/implementation_medium4.png)

* * *

## Presentation Slides¶

[![../_images/lecture_4.png](../_images/lecture_4.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257420)

Note

These slides are a collection of lectures so you need to do a bit of scrolling
to find the correct sections.

>   * pg 14-18: CV in Finance
>
>   * pg 30-34: Hyper-parameter Tuning with CV
>
>   * pg 122-126: Cross-Validation
>
>

  

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 4/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257420)

