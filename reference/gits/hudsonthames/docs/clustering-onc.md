> # Optimal Number of Clusters (ONC)¶

Get full version of MlFinLab

  

The ONC algorithm detects the optimal number of K-Means clusters using a
correlation matrix as input.

Clustering is a process of grouping a set of elements where elements within a
group (cluster) are more similar than elements from different groups. A
popular clustering algorithm is the K-means algorithm that guarantees the
convergence in a finite number of steps.

The K-means algorithm has two caveats. It requires the user to set the number
of clusters in advance and the initialization of clusters is random.
Consequently, the effectiveness of the algorithm is random. The ONC algorithm
proposed by Marcos Lopez de Prado addresses these two issues.

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [Detection of false investment strategies using unsupervised learning methods](https://papers.ssrn.com/sol3/abstract_id=3167017) _by_ Marcos Lopez de Prado _and_ Lewis, M.J. _Describes the ONC algorithm in detail. The code in this module is based on the code written by the researchers._

  * [Machine Learning for Asset Managers](https://www.cambridge.org/core/books/machine-learning-for-asset-managers/6D9211305EA2E425D33A9F38D0AE3545) _by_ Marcos Lopez de Prado. _Features additional descriptions of the algorithm and includes exercises to understand the topic in more detail._

  * [Clustering (Presentation Slides)](https://papers.ssrn.com/sol3/abstract_id=3512998) _by_ Marcos Lopez de Prado _and_ Lewis, M.J. _Briefly describes the logic behind the ONC algorithm._

  * [Codependence (Presentation Slides)](https://papers.ssrn.com/sol3/abstract_id=3512994) _by_ Marcos Lopez de Prado _and_ Lewis, M.J. _Explains why the angular distance metric is used to get distances between elements._

Based on the **Detection of false investment strategies using unsupervised
learning methods** paper, this is how the distances and scores are calculated:

Distances between the elements in the ONC algorithm are calculated using the
same angular distance used in the HRP algorithm:

\\[D_{i,j} = \sqrt{\frac{1}{2}(1 - \rho_{i,j})}\\]

where \\(\rho_{i,j}\\) is the correlation between elements \\(i\\) and \\(j\\)
.

Distances between distances in the clustering algorithm are calculated as:

\\[\hat{D_{i,j}} = \sqrt{\sum_{k}(D_{i,k} - D_{j,k})^{2}}\\]

Silhouette scores are calculated as:

\\[S_i = \frac{b_i - a_i}{max\\{a_i,b_i\\}}\\]

where \\(a_i\\) the average distance between element \\(i\\) and all other
components in the same cluster, and \\(b_i\\) is the smallest average distance
between \\(i\\) and all the nodes in any other cluster.

The measure of clustering quality \\(q\\) or \\(t-score\\):

\\[q = \frac{E[\\{S_i\\}]}{\sqrt{V[\\{S_i\\}]}}\\]

where \\(E[\\{S_i\\}]\\) is the mean of the silhouette scores for each
cluster, and \\(V[\\{S_i\\}]\\) is the variance of the silhouette scores for
each cluster.

The ONC algorithm structure is described in the work [Detection of false
investment strategies using unsupervised learning
methods](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3167017) using
the following diagrams:

[![ONC Base
Clustering](../_images/onc_base_clustering.png)](../_images/onc_base_clustering.png)

Structure of ONC’s base clustering stage.¶

In the base clustering stage first, the distances between the elements are
calculated, then the algorithm iterates through a set of possible number of
clusters \\(N\\) times to find the best clustering from \\(N\\) runs of
K-means for every possible number of clusters. For each iteration, a
clustering result is evaluated using the t-statistic of the silhouette scores.

The clustering result with the best t-statistic is picked, the correlation
matrix is reordered so that clustered elements are positioned close to each
other.

[![Structure of ONC’s higher-level
stage](../_images/onc_higher_level.png)](../_images/onc_higher_level.png)

Structure of ONC’s higher-level stage.¶

On a higher level, the average t-score of the clusters from the base
clustering stage is calculated. If more than two clusters have a t-score below
average, these clusters go through the base clustering stage again. This
process is recursively repeated.

Then, based on the t-statistic of the old and new clusterings it is checked
whether the new clustering is better than the original one. If not, the old
clustering is kept, otherwise, the new one is taken.

The output of the algorithm is the reordered correlation matrix, clustering
result, and silhouette scores.

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium2.png)](../_images/implementation_medium2.png)

* * *

## Example¶

An example showing how the ONC algorithm is used can be seen below:

[![Code example
demo](../_images/example_medium1.png)](../_images/example_medium1.png)

* * *

## Presentation Slides¶

[![../_images/cluster_slides.png](../_images/cluster_slides.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512998)

* * *

## References¶

  * [de Prado, M.L. and Lewis, M.J., 2019. Detection of false investment strategies using unsupervised learning methods. Quantitative Finance, 19(9), pp.1555-1565.](https://papers.ssrn.com/sol3/abstract_id=3167017)

  * [de Prado, M.L., 2020. Machine learning for asset managers. Cambridge University Press.](https://www.cambridge.org/core/books/machine-learning-for-asset-managers/6D9211305EA2E425D33A9F38D0AE3545)

  * [de Prado, M.L., 2020. Clustering (Presentation Slides). Available at SSRN 3512998.](https://papers.ssrn.com/sol3/abstract_id=3512998)

  * [de Prado, M.L., 2020. Codependence (Presentation Slides). Available at SSRN 3512994.](https://papers.ssrn.com/sol3/abstract_id=3512994)

