# Introduction¶

Get full version of MlFinLab

  

  

  

Note

**Underlying Literature**

The following sources describe this method in more detail:

  * [A review of two decades of correlations, hierarchies, networks and clustering in financial markets](https://arxiv.org/abs/1703.00485) _by_ Marti, G., Nielsen, F., Bińkowski, M. and Donnat, P.

## Networks¶

Networks module creates beautiful and informative visualizations of financial
data, using network theory to describe complex systems such as financial
markets.

Networks takes in a codependence or distance matrix between a set of elements
and converts it into graphs such as a Minimum Spanning Tree, creating a mini
[Flask](https://flask.palletsprojects.com) server using [Plotly’s
Dash](https://dash.plotly.com) to display the interactive graphs.

![../_images/dash_ui.png](../_images/dash_ui.png)

Interactive Minimum Spanning Tree graph of 48 stocks based on daily closing
price data from 15th August 2017 - 10th of August 2020¶

Four aspects of network visualisation tools have been added:

  1. Minimum Spanning Tree (MST).

  2. Average Linkage Minimum Spanning Tree (ALMST).

  3. Planar Maximally Filtered Graph (PMFG).

  4. Triangulated Maximally Filtered Graph (in development).

The methods from the visualisations.py file can be used to create
visualisations given a dataframe of log returns.

* * *

## Input Matrices¶

Methods take distance or correlation matrices as inputs. Tools to calculate
various codependences and distances can be found in the [Codependence
module](../codependence/introduction.html#codependence-introduction). To
create a matrix from a set of observations, the [Codependence Matrix
function](../codependence/codependence_matrix.html#codependence-codependence-
matrix) can be used.

### Correlation Matrix¶

Let \\(n\\) be the number of assets, \\(P_i(t)\\) be price \\(t\\) of asset
\\(i\\) and \\(r_i(t)\\) be the log-return at time \\(t\\) of asset \\(i\\):

\\[r_i(t) = log P_i(t) − log P_i(t − 1)\\]

For each pair of assets \\(i\\), \\(j\\) of assets, compute their correlation:

\\[\rho_{ij} = \frac{⟨r_i r_j⟩ − ⟨r_i⟩⟨r_j⟩}{\sqrt{(⟨r_i^2⟩−⟨r_i⟩^2)
(⟨r_j^2⟩−⟨r_j⟩^2})}\\]

### Distance Matrix¶

Having followed the steps to create a correlation matrix, convert the
correlation coefficients \\(\rho_{ij}\\) into distances:

\\[d_{ij} = \sqrt{2(1- \rho_{ij})}\\]

For a more detailed explanation, please refer to [Correlation-Based Metrics
section](../codependence/correlation_based_metrics.html#codependence-
correlation-based-metrics), as it describes the measures in more detail.

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Marti, G., Nielsen, F., Bińkowski, M. and Donnat, P., 2017. A review of two decades of correlations, hierarchies, networks and clustering in financial markets. arXiv preprint arXiv:1703.00485.](https://arxiv.org/pdf/1703.00485.pdf)

