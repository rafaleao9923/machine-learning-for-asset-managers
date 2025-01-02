# Clustered MDA and MDI¶

Get full version of MlFinLab

  

In the book Machine Learning for Asset Managers, as an approach to deal with
substitution effects, Clustered Feature Importance was introduced. It clusters
similar features and applies feature importance analysis (like MDA and MDI) at
the cluster level. The value add of clustering is that the clusters are
mutually dissimilar and hence reduces the substitution effects.

It can be implemented in two steps as described in the book:

  1. **Features Clustering** : As a first step we need to generate the clusters or subsets of features we want to analyse with feature importance methods. This can be done using the feature cluster module. It implement the method of generating feature clusters as in the book.

  2. **Clustered Importance** : Now that we have identified the number and composition of the clusters of features. We can use this information to apply MDI and MDA on groups of similar features, rather than on individual features. Clustered Feature Importance can be implemented by simply passing the feature clusters obtained in Step-1 to the clustered_subsets argument of the MDI or MDA feature importance algorithm.

How Cluster Feature Importance can be applied:

  1. Clustered MDI (code Snippet 6.4 page 86 ): We compute the clustered MDI as the sum of the MDI values of the features that constitute that cluster. If there is one feature per cluster, then MDI and clustered MDI are the same.

  2. Clustered MDA (code Snippet 6.5 page 87 ): As an extension to normal MDA to tackle multi-collinearity and (linear or non-linear) substitution effect. Its implementation was also discussed by Dr. Marcos Lopez de Prado in the [Clustered Feature Importance (Presentation Slides)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3517595).

Note

The implementation of Clustered feature importance is included in the
functions for MDI and MDA.

* * *

## Example¶

[![Code implementation
demo](../_images/example_big5.png)](../_images/example_big5.png)

The following are the resulting images from the Clustered MDI & Clustered MDA
feature importances respectively:

[![Clustered MDI](../_images/clustered_mdi.png)](../_images/clustered_mdi.png)

Clustered MDI¶

[![Clustered MDA](../_images/clustered_mda.png)](../_images/clustered_mda.png)

Clustered MDA¶

* * *

## Research Notebook¶

The following research notebooks can be used to better understand the
Clustered Feature Importance and its implementations.

[![Notebook demo](../_images/notebook8.png)](../_images/notebook8.png)

* * *

## Presentation Slides¶

[![../_images/clus_fi.png](../_images/clus_fi.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3517595)
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

  * [de Prado, M.L, 2020. Clustered Feature Importance (Presentation Slides). Available at SSRN.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3517595)

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 4/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257420)

