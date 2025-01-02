# MDI, MDA, and SFI¶

Get full version of MlFinLab

  

  

****“Backtesting is not a research tool. Feature importance is.” (Lopez de
Prado)****

  

Note

**Underlying Literature**

The following sources describe this method in more detail:

  * [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 8 _by_ Marcos Lopez de Prado.

* * *

## 3 Algorithms for Feature Importance¶

The book describes three methods to get importance scores:

  1. **Mean Decrease Impurity (MDI)** : This score can be obtained from tree-based classifiers and corresponds to sklearn’s feature_importances attribute. MDI uses in-sample (IS) performance to estimate feature importance.

  2. **Mean Decrease Accuracy (MDA)** : This method can be applied to any classifier, not only tree based. MDA uses out-of-sample (OOS) performance in order to estimate feature importance.

  3. **Single Feature Importance (SFI)** : MDA and MDI feature suffer from substitution effects. If two features are highly correlated, one of them will be considered as important while the other one will be redundant. SFI is a OOS feature importance estimator which doesn’t suffer from substitution effects because it estimates each feature importance separately.

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_big5.png)](../_images/implementation_big5.png)

[![Code implementation
demo](../_images/implementation_medium8.png)](../_images/implementation_medium8.png)

[![Code implementation
demo](../_images/implementation_medium8.png)](../_images/implementation_medium8.png)

* * *

## Example¶

An example showing how to use various feature importance functions:

[![Code example
demo](../_images/example_big5.png)](../_images/example_big5.png)

The following are the resulting images from the MDI, MDA, and SFI feature
importances respectively:

[![../_images/mdi_feat_imp.png](../_images/mdi_feat_imp.png)](../_images/mdi_feat_imp.png)
[![../_images/mda_feat_imp.png](../_images/mda_feat_imp.png)](../_images/mda_feat_imp.png)
[![../_images/sfi_feat_imp.png](../_images/sfi_feat_imp.png)](../_images/sfi_feat_imp.png)

* * *

## Research Notebook¶

[![Notebook demo](../_images/notebook8.png)](../_images/notebook8.png)

* * *

## Presentation Slides¶

[![../_images/lecture_41.png](../_images/lecture_41.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257420)

Note

These slides are a collection of lectures so you need to do a bit of scrolling
to find the correct sections.

>   * pg 19-29: Feature Importance + Clustered Feature Importance.
>
>   * pg 109: Feature Importance Analysis
>
>   * pg 131: Feature Selection
>
>   * pg 141-173: Clustered Feature Importance
>
>   * pg 176-198: Shapley Values
>
>

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 4/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257420)

