# Hierarchical Correlation Block Model (HCBM)¶

Get full version of MlFinLab

  

  

  

Note

The following implementation and documentation closely follow the work of
Marti, Andler, Nielsen, and Donnat: [Clustering financial time series: How
long is enough?](https://arxiv.org/pdf/1603.04017.pdf).

## HCBM¶

According to the research paper, it has been verified that price time series
of traded assets for different markets exhibit a hierarchical correlation
structure. Another property they exhibit is the non-Gaussianity of daily asset
returns. These two properties prompt the use of alternative correlation
coefficients, with the most used correlation coefficient is the Pearson
correlation coefficient, and the definition of the Hierarchical Correlation
Block Model (HCBM).

Warning

Pearson correlation only captures linear effects. If two variables have strong
non-linear dependency (squared or abs for example) Pearson correlation won’t
find any pattern between them. For information about capturing non-linear
dependencies, read our
[Introduction](../codependence/introduction.html#codependence-introduction) to
Codependence.

The HCBM model consists of correlation matrices having a hierarchical block
structure. Each block corresponds to a correlation cluster. The HCBM defines a
set of nested partitions \\(P = \\{P_0 \supseteq P_1 \supseteq ... \supseteq
P_h\\}\\) for some \\(h \in [1, N]\\) for \\(N\\) univariate random variables.
Each partition is further subdivided and partitioned again for \\(k\\) levels
where \\(1 \leq k \leq h\\). We define \\(\underline{\rho_k}\\) and
\\(\bar{\rho_k}\\) such that for all \\(1 \leq i,j \leq N\\), we have
\\(\underline{\rho_k} \leq \rho_{i,j} \leq \bar{\rho_k}\\), when
\\(C^{(k)}(X_i) = C^{(k)}(X_j)\\) and \\(C^{(k+1)}(X_i) \neq C^{(k+1)}(X_j)\\)
(\\(C^{(k)}(X_i)\\) denotes the cluster \\(X_i\\) in partition \\(P_k\\)).

This implies that \\(\underline{\rho_k}\\) and \\(\bar{\rho_k}\\) are the
minimum and maximum correlation factors respectively within all clusters
\\(C^{(k)}_i\\) in the partition \\(P_k\\) at depth \\(k\\). In order for the
generated matrix to have a proper nested correlation hierarchy, we must have
\\(\bar{\rho_k} < \underline{\rho_{k+1}}\\) hold true for all \\(k\\).

Figure 1 is a sample HCBM matrix generated with \\(N = 256\\), \\(k = 4\\),
\\(h = 4\\), \\(\underline{\rho_k} = 0.1\\), and \\(\bar{\rho_k} = 0.9\\).

[![Hierarchical Correlation Block Model
\(HCBM\)](../_images/hcbm_sample.png)](../_images/hcbm_sample.png)

Figure 1. (Left) HCBM matrix. (Right) Left HCBM matrix permuted once.¶

Figure 1 shows how an HCBM matrix has different levels of hierarchical
clusters. The picture on the right shows how a correlation matrix is most
commonly observed from asset returns.

* * *

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium5.png)](../_images/implementation_medium5.png)

* * *

### Example¶

[![Code example
demo](../_images/example_medium3.png)](../_images/example_medium3.png)

* * *

## Time Series Generation from HCBM Matrix¶

To generate financial time series models from HCBM matrices we will consider
two models.

  * The standard, but not entirely accurate, gaussian random walk model. Its increments are realization from a \\(N\\)-variate Gaussian \\(X \sim N(0, \Sigma)\\)

  * The \\(N\\)-variate Student’s t-distribution, with degree of freedom \\(v = 3\\), \\(X \sim t_v(0, \frac{v-2}{v}\Sigma)\\)

The advantage of using the \\(N\\)-variate Student’s t-distribution is that it
captures heavy-tailed behavior and tail-dependence. The authors assert that
“It has been shown that this distribution (Student’s t-distribution) yields a
much better fit to real returns than the Gaussian distribution”

Both distributions are parameterized by a covariance matrix \\(\Sigma\\). We
define \\(\Sigma\\) such that the underlying correlation matrix has a HCBM
structure as shown in Figure 1.

Figure 2 shows both distributions created from an HCBM matrix. It has 1000
samples

[![HCBM Time
Series](../_images/hcbm_time_series.png)](../_images/hcbm_time_series.png)

Figure 2. (Left) Time Series generated from a Gaussian Distribution. (Right)
Time Series generated from a Student-t distribution.¶

* * *

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium5.png)](../_images/implementation_medium5.png)

* * *

### Example¶

[![Code example
demo](../_images/example_medium3.png)](../_images/example_medium3.png)

* * *

## Research Notebook¶

The following research notebook can be used to better understand the
Hierarchical Correlation Block Model.

[![Notebook demo](../_images/notebook5.png)](../_images/notebook5.png)

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Marti, G., Andler, S., Nielsen, F. and Donnat, P., 2016. Clustering financial time series: How long is enough?. arXiv preprint arXiv:1603.04017.](https://arxiv.org/pdf/1603.04017.pdf)

