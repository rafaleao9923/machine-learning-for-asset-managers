Note

The following implementation and documentation closely follow the work of
Gautier Marti: [CorrGAN: Sampling Realistic Financial Correlation Matrices
using Generative Adversarial Networks](https://arxiv.org/pdf/1910.09504.pdf).

And the work of Donnat, P., Marti, G. and Very, P: [Toward a generic
representation of random variables for machine
learning](https://arxiv.org/pdf/1506.00976.pdf).

# Data Verification¶

Get full version of MlFinLab

  

  

  

Data verification for synthetic data is needed to confirm if it shares some
properties of the original data. Being able to examine and validate
synthetically generated data is critical to building more accurate systems.
Without verification, we would operate on data that might not have any
significance in the real world. We present several methods to examine the
properties of this type of data.

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [CorrGAN: Sampling Realistic Financial Correlation Matrices using Generative Adversarial Networks](https://arxiv.org/pdf/1910.09504.pdf) _by_ Gautier Marti.

  * [Toward a generic representation of random variables for machine learning](https://arxiv.org/pdf/1506.00976.pdf) _by_ Donnat, P., Marti, G. and Very, P.

## Stylized Factors of Correlation Matrices¶

Following the work of Gautier Marti in CorrGAN, we provide function to plot
and verify a synthetic matrix has the 6 stylized facts of empirical
correlation matrices.

The stylized facts are:

  1. Distribution of pairwise correlations is significantly shifted to the positive.

  2. Eigenvalues follow the Marchenko-Pastur distribution, but for a very large first eigenvalue (the market).

  3. Eigenvalues follow the Marchenko-Pastur distribution, but for a couple of other large eigenvalues (industries).

  4. Perron-Frobenius property (first eigenvector has positive entries).

  5. Hierarchical structure of correlations.

  6. Scale-free property of the corresponding Minimum Spanning Tree (MST).

* * *

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium5.png)](../_images/implementation_medium5.png)

[![Code implementation
demo](../_images/implementation_small3.png)](../_images/implementation_small3.png)

[![Code implementation
demo](../_images/implementation_medium5.png)](../_images/implementation_medium5.png)

[![Code implementation
demo](../_images/implementation_small3.png)](../_images/implementation_small3.png)

* * *

### Example¶

[![Code example
demo](../_images/example_medium3.png)](../_images/example_medium3.png)

* * *

## Time Series Codependence Visualization¶

Note

The correlated random walks time series generation and GNPR codependence
measure approaches are fully explored in our [Correlated Random
Walks](correlated_random_walks.html#data-generation-correlated-random-walks)
and [Codependence by
Marti](../codependence/codependence_marti.html#codependence-codependence-
marti) sections.

Following the work of Donnat, Marti, and Very (2016) we provide a method to
plot the GNPR codependence matrix and visualize the different underlying
distributions these time series may have. GNPR was shown to detect all
underlying distributions more accurately than other methods, as it L2
distance, correlation distance, and GPR.

* * *

### Implementation¶

[![Code implementation
demo](../_images/implementation_small3.png)](../_images/implementation_small3.png)

* * *

### Example¶

[![Mix Time Series
Example](../_images/mix_example_single.png)](../_images/mix_example_single.png)

(Left) GPR codependence matrix. Only 5 correlation clusters are seen with no
indication of a global embedded distribution. All 5 correlation clusters and 2
distribution clusters can be seen, as well as the global embedded
distribution.¶

[![Code example
demo](../_images/example_medium3.png)](../_images/example_medium3.png)

* * *

## Optimal Hierarchical Clustering¶

This function plots the optimal leaf hierarchical clustering as shown in
[Marti, G. (2020) TF 2.0 DCGAN for 100x100 financial correlation
matrices](https://marti.ai/ml/2019/10/13/tf-dcgan-financial-correlation-
matrices.html) by arranging a matrix with hierarchical clustering by
maximizing the sum of the similarities between adjacent leaves.

* * *

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium5.png)](../_images/implementation_medium5.png)

* * *

### Example¶

[![Optimal
Clustering.](../_images/optimal_clustering1.png)](../_images/optimal_clustering1.png)

(Left) HCBM matrix. (Right) Optimal Clustering of the HCBM matrix.¶

[![Code example
demo](../_images/example_big2.png)](../_images/example_big2.png)

* * *

## Research Article¶

Read our article on the topic

  

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Marti, G., 2020, May. Corrgan: Sampling realistic financial correlation matrices using generative adversarial networks. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 8459-8463). IEEE.](https://arxiv.org/pdf/1910.09504.pdf)

  * [Donnat, P., Marti, G. and Very, P., 2016. Toward a generic representation of random variables for machine learning. Pattern Recognition Letters, 70, pp.24-31.](https://arxiv.org/pdf/1506.00976.pdf)

