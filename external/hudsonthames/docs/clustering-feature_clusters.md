# Feature Clustering¶

Get full version of MlFinLab

  

This module implements the clustering of features to generate a feature subset
described in the book [Machine Learning for Asset
Managers](https://www.cambridge.org/core/books/machine-learning-for-asset-
managers/6D9211305EA2E425D33A9F38D0AE3545) (snippet 6.5.2.1 page-85). This
subsets can be further utilised for getting Clustered Feature Importance using
the clustered_subsets argument in the Mean Decreased Impurity (MDI) and Mean
Decreased Accuracy (MDA) algorithm.

The algorithm projects the observed features into a metric space by applying
the dependence metric function, either correlation based or information theory
based (see the codependence section). Information-theoretic metrics have the
advantage of recognizing redundant features that are the result of nonlinear
combinations of informative features.

Next, we need to determine the optimal number of clusters. The user can either
specify the number cluster to use, this will apply a hierarchical clustering
on the defined distance matrix of the dependence matrix for a given linkage
method for clustering, or the user can use the ONC algorithm which uses
K-Means clustering, to automate these task.

The caveat of this process is that some silhouette scores may be low due to
one feature being a combination of multiple features across clusters. This is
a problem, because ONC cannot assign one feature to multiple clusters. Hence,
the following transformation may help reduce the multicollinearity of the
system:

For each cluster \\(k = 1 . . . K\\), replace the features included in that
cluster with residual features, so that it do not contain any information
outside cluster \\(k\\). That is let \\(D_{k}\\) be the subset of index
features \\(D = {1,...,F}\\) included in cluster \\(k\\), where:

\\[D_{k}\subset{D}\ , ||D_{k}|| > 0 \ , \forall{k}\ ; \ D_{k} \bigcap D_{l} =
\Phi\ , \forall k \ne l\ ; \bigcup \limits _{k=1} ^{k} D_{k} = D\\]

Then, for a given feature \\(X_{i}\\) where \\(i \in D_{k}\\), we compute the
residual feature \\(\hat \varepsilon _{i}\\) by fitting the following equation
for regression:

\\[X_{n,j} = \alpha _{i} + \sum \limits _{j \in \bigcup _{l<k}} \ D_{l} \beta
_{i,j} X_{n,j} + \varepsilon _{n,i}\\]

Where \\(n = 1,\dots,N\\) is the index of observations per feature. Note if
the degrees of freedom in the above regression are too low, one option is to
use as regressors linear combinations of the features within each cluster by
following a minimum variance weighting scheme so that only \\(K-1\\) betas
need to be estimated. This transformation is not necessary if the silhouette
scores clearly indicate that features belong to their respective clusters.

Note

**Underlying Literature**

The following sources describe this method in more detail:

  * [Machine Learning for Asset Managers](https://www.cambridge.org/core/books/machine-learning-for-asset-managers/6D9211305EA2E425D33A9F38D0AE3545) _by_ Marcos Lopez de Prado.

  * [Clustered Feature Importance (Presentation Slides)](https://ssrn.com/abstract=3517595) _by_ Marcos Lopez de Prado.

* * *

## Implementation¶

This module creates clustered subsets of features described in the
presentation slides: [Clustered Feature
Importance](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3517595) by
Marcos Lopez de Prado.

[![Code implementation
demo](../_images/implementation_medium2.png)](../_images/implementation_medium2.png)

* * *

## Example¶

An example showing how to generate feature subsets or clusters for a give
feature DataFrame. The example will generate 4 clusters by Hierarchical
Clustering for given specification.

[![Code example
demo](../_images/example_medium1.png)](../_images/example_medium1.png)

* * *

## Research Notebook¶

The for better understanding of its implementations see the notebook on
Clustered Feature Importance.

[![Notebook demo](../_images/notebook2.png)](../_images/notebook2.png)

* * *

## References¶

  * [de Prado, M.L., 2020. Machine learning for asset managers. Cambridge University Press.](https://www.cambridge.org/core/books/machine-learning-for-asset-managers/6D9211305EA2E425D33A9F38D0AE3545)

  * [de Prado, M.L., 2020. Clustered Feature Importance (Presentation Slides). Available at SSRN.](https://ssrn.com/abstract=3517595)

