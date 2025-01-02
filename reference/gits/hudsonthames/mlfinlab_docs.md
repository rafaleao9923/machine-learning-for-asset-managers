# Introduction

Get full version of MlFinLab

**Note**

**Underlying Literature**

The following sources describe this method in more detail:

- [A review of two decades of correlations, hierarchies, networks and clustering in financial markets](https://arxiv.org/abs/1703.00485) *by* Marti, G., Nielsen, F., Bińkowski, M. and Donnat, P.

## Networks

Networks module creates beautiful and informative visualizations of financial data, using network theory to describe complex systems such as financial markets.

Networks takes in a codependence or distance matrix between a set of elements and converts it into graphs such as a Minimum Spanning Tree, creating a mini [Flask](https://flask.palletsprojects.com) server using [Plotly's Dash](https://dash.plotly.com) to display the interactive graphs.

**Interactive Minimum Spanning Tree graph of 48 stocks based on daily closing price data from 15th August 2017 - 10th of August 2020**

Four aspects of network visualisation tools have been added:

1. Minimum Spanning Tree (MST).
2. Average Linkage Minimum Spanning Tree (ALMST).
3. Planar Maximally Filtered Graph (PMFG).
4. Triangulated Maximally Filtered Graph (in development).

The methods from the visualisations.py file can be used to create visualisations given a dataframe of log returns.

## Input Matrices

Methods take distance or correlation matrices as inputs. Tools to calculate various codependences and distances can be found in the [Codependence module](../codependence/introduction.html#codependence-introduction). To create a matrix from a set of observations, the [Codependence Matrix function](../codependence/codependence_matrix.html#codependence-codependence-matrix) can be used.

### Correlation Matrix

Let $n$ be the number of assets, $P_{i}(t)$ be price $t$ of asset $i$ and $r_{i}(t)$ be the log-return at time $t$ of asset $i$:

$r_{i}(t) = logP_{i}(t) - logP_{i}(t - 1)$

For each pair of assets $i$, $j$ of assets, compute their correlation:

$\rho_{ij} = \frac{\left\langle r_{i}r_{j} \right\rangle - \left\langle r_{i} \right\rangle\left\langle r_{j} \right\rangle}{\left. \sqrt{\left( \left\langle r_{i}^{2} \right\rangle - \left\langle r_{i} \right\rangle^{2} \right)\left( \left\langle r_{j}^{2} \right\rangle - \left\langle r_{j} \right\rangle^{2} \right.} \right)}$

### Distance Matrix

Having followed the steps to create a correlation matrix, convert the correlation coefficients $\rho_{ij}$ into distances:

$d_{ij} = \sqrt{2\left( 1 - \rho_{ij} \right)}$

For a more detailed explanation, please refer to [Correlation-Based Metrics section](../codependence/correlation_based_metrics.html#codependence-correlation-based-metrics), as it describes the measures in more detail.

## Presentation Slides

## References

- [Marti, G., Nielsen, F., Bińkowski, M. and Donnat, P., 2017. A review of two decades of correlations, hierarchies, networks and clustering in financial markets. arXiv preprint arXiv:1703.00485.](https://arxiv.org/pdf/1703.00485.pdf)

---

# 7 Point Backtesting Protocol

Get full version of MlFinLab

In 2018, Robert D. Arnott, Campbell R. Harvey, and Harry Markowitz published a paper listing a backtesting protocol in the era of machine learning. In fact, that was the name of the paper.

The research protocol applies to quantitative finance in general, and not only to machine learning applications. They list 7 categories which we mention below but the paper, of course, dives into much greater detail.

**Note**

**Underlying Literature**

- [A Backtesting Protocol in the Era of Machine Learning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3275654), by Robert D. Arnott, Campbell R. Harvey, and Harry Markowitz.

## The Protocol

As per Exhibit 2, pg.16:

1. **Research Motivation**
   1. Does the model have a solid economic foundation?
   2. Did the economic foundation or hypothesis exist before the research was conducted?

2. **Multiple Testing and Statistical Methods**
   1. Did the researcher keep track of all models and variables that were tried (both successful and unsuccessful) and are the researchers aware of the multiple-testing issue?
   2. Is there a full accounting of all possible interaction variables if interaction variables are used?
   3. Did the researchers investigate all variables set out in the research agenda or did they cut the research as soon as they found a good model?

3. **Data and Sample Choice**
   1. Do the data chosen for examination make sense? And, if other data are available, does it make sense to exclude these data?
   2. Did the researchers take steps to ensure the integrity of the data?
   3. Do the data transformations, such as scaling, make sense? Were they selected in advance? And are the results robust to minor changes in these transformations?
   4. If outliers are excluded, are the exclusion rules reasonable?
   5. If the data are winsorized, was there a good reason to do it? Was the winsorization rule chosen before the research was started? Was only one winsorization rule tried (as opposed to many)?

4. **Cross-Validation**
   1. Are the researchers aware that true out-of-sample tests are only possible in live trading?
   2. Are steps in place to eliminate the risk of out-of-sample "iterations" (i.e., an in-sample model that is later modified to fit out-of-sample data)?
   3. Is the out-of-sample analysis representative of live trading? For example, are trading costs and data revisions taken into account?

5. **Model Dynamics**
   1. Is the model resilient to structural change and have the researchers taken steps to minimize the overfitting of the model dynamics?
   2. Does the analysis take into account the risk/likelihood of overcrowding in live trading?
   3. Do researchers take steps to minimize the tweaking of a live model?

6. **Complexity**
   1. Does the model avoid the curse of dimensionality?
   2. Have the researchers taken steps to produce the simplest practicable model specification?
   3. Is an attempt made to interpret the predictions of the machine learning model rather than using it as a black box?

7. **Research Culture**
   1. Does the research culture reward quality of the science rather than finding the winning strategy?
   2. Do the researchers and management understand that most tests will fail?
   3. Are expectations clear (that researchers should seek the truth not just something that works) when research is delegated?

## Presentation Slides

## References

- [A Backtesting Protocol in the Era of Machine Learning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3275654), by Robert D. Arnott, Campbell R. Harvey, and Harry Markowitz.

---