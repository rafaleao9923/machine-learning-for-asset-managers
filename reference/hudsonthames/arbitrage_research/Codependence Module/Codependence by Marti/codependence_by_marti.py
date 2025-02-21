# Generated from: codependence_by_marti.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# * Reference: __Some contributions to the clustering of financial time series and applications to credit default swaps__ _by_ Gautier Marti


# ## Abstract


# GPR and GNPR distances are a part of a novel technique for measuring the distance between two random variables that allows to separate the measurement of distribution information and the dependence information. A mix of both types of information can be used in a chosen proportion.


# ## GPR and GNPR distances


# This description is based on the paper by _Gautier Marti_ __“Some contributions to the clustering of financial time series and applications to credit default swaps”__  [available here](https://www.researchgate.net/publication/322714557).


# ### Classification of distances


# According to _Gautier Marti_:
#
# "Many statistical distances exist to measure the dissimilarity of two random variables, and therefore two i.i.d. random processes. Such distances can be roughly classified in two
# families:
#
# 1. __distributional distances__, ... which focus on dissimilarity between probability distributions and quantify divergences in marginal behaviours,
#
# 2. __dependence distances__, such as the distance correlation or copula-based kernel dependency measures ..., which focus on the joint behaviours of random variables, generally ignoring their distribution properties.
#
# However, we may want to be able to discriminate random variables both on distribution and dependence. This can be motivated, for instance, from the study of financial assets returns: are two perfectly correlated random variables (assets returns), but one being normally distributed and the other one following a heavy-tailed distribution, similar?
#
# From risk perspective, the answer is no ..., hence the propounded distance of this article".


# ### GPR distance


# From __“Some contributions to the clustering of financial time series and applications to credit default swaps”__ :
#
# __Definition:__ (Distance $d_{\Theta}$ between two random variables). Let $\theta \in [0, 1]$. Let $(X, Y) \in \nu^{2}$ , where $\nu$ is the space of all continuous
# real-valued random variables. Let $G = (G_{X}, G_{Y})$, where $G_{X}$ and $G_{Y}$ are respectively $X$ and $Y$ marginal cdfs. We define the following distance
#
# $$d_{\Theta}^{2}(X, Y) = \Theta d_{1}^{2}(G_{X}(X), G_{Y}(Y)) + (1 - \Theta) d_{0}^{2}(G_{X}, G_{Y})$$
#
# where
#
# $$d_{1}^{2}(G_{X}(X), G_{Y}(Y)) = 3 \mathbb{E}[|G_{X}(X) - G_{Y}(Y)|^{2}]$$
#
# and
#
# $$d_{0}^{2}(G_{X}, G_{Y}) = \frac{1}{2} \int_{R} (\sqrt{\frac{d G_{X}}{d \lambda}} - \sqrt{\frac{d G_{Y}}{d \lambda}})^{2} d \lambda$$


# __Example:__ (Distance $d_{\Theta}$ between two Gaussians). Let $(X, Y)$ be a bivariate Gaussian vector, with $X \sim \mathcal{N}(\mu_{X}, \sigma_{X}^{2})$,
# $Y \sim \mathcal{N}(\mu_{Y}, \sigma_{Y}^{2})$ and $\rho (X,Y)$. We obtain,
#
# $$d_{\Theta}^{2}(X, Y) = \Theta \frac{1 - \rho_{S}}{2} + (1 - \Theta) (1 - \sqrt{\frac{2 \sigma_{X} \sigma_{Y}}{\sigma_{X}^{2} + \sigma_{Y}^{2}}} e^{ - \frac{1}{4} \frac{(\mu_{X} - \mu_{Y})^{2}}{\sigma_{X}^{2} + \sigma_{Y}^{2}}})$$
#
# The use of this distance is referenced as the generic parametric representation (GPR) approach.
#
# From the paper:
#
# "GPR distance is a fast and good proxy for distance $d_{\Theta}$ when the first two moments $\mu$ and ${\sigma}$ predominate. Nonetheless, for datasets which contain heavy-tailed distributions, GPR fails to capture this information".


# __Property:__ Let $\Theta \in [0,1]$. The distance $d_{\Theta}$verifies $0 \le d_{\Theta} \le 1$.
#
# __Property:__ For $0 < \Theta < 1$, $d_{\Theta}$ is a metric.
#
# __Property:__ [Diffeomorphism](https://en.wikipedia.org/wiki/Diffeomorphism) invariance. Let $h: \nu \rightarrow \nu$ be a diffeomorphism. Let $(X, Y) \in \nu^{2}$. Distance $d_{\Theta}$ is invariant under diffeomorphism, i.e.
#
# $$d_{\Theta}(h(X), h(Y)) = d_{\Theta}(X, Y)$$


# ### GNPR distance


# According to _Marti_:
#
# "To apply the propounded distance $d_{\Theta}$ on sampled data without parametric assumptions, we have to define its statistical estimate $\tilde{d}_{\Theta}$ working on realizations of the i.i.d. random variables.
#
# Distance $d_{1}$ working with continuous uniform distributions can be approximated by normalized rank statistics yielding to discrete uniform distributions.
#
# Distance $d_{0}$ working with densities can be approximated by using its discrete form working on histogram density estimates".


# __Definition:__ (Empirical distance) Let $(X^{t})_{t=1}^{T}$ and $(Y^{t})_{t=1}^{T}$ be $T$ realizations of real-valued random variables $X, Y \in \nu$ respectively. An empirical distance between realizations of random variables can be defined by
#
# $$\tilde{d}_{\Theta}^{2}((X^{t})_{t=1}^{T}, (Y^{t})_{t=1}^{T}) \stackrel{\text{a.s.}}{=} \Theta \tilde{d}_{1}^{2} + (1 - \Theta) \tilde{d}_{0}^{2}$$
#
# where
#
# $$\tilde{d}_{1}^{2} = \frac{3}{T(T^{2} - 1)} \sum_{t = 1}^{T} (X^{(t)} - Y^{(t)}) ^ {2}$$
#
# and
#
# $$\tilde{d}_{0}^{2} = \frac{1}{2} \sum_{k = - \infty}^{+ \infty} (\sqrt{g_{X}^{h}(hk)} - \sqrt{g_{Y}^{h}(hk)})^{2}$$
#
# $h$ being here a suitable bandwidth, and $g_{X}^{h}(x) = \frac{1}{T} \sum_{t = 1}^{T} \mathbf{1}(\lfloor \frac{x}{h} \rfloor h \le X^{t} < (\lfloor \frac{x}{h} \rfloor + 1)h)$ being a density histogram estimating dpf $g_{X}$ from
# $(X^{t})_{t=1}^{T}$ , $T$ realization of a random variable $X \in \nu$.


# The use of this distance is referenced as the generic non-parametric representation (GNPR) approach.
#
# From the paper:
#
# "To use effectively $d_{\Theta}$ and its statistical estimate, it boils down to select a particular value for $\Theta$. We suggest here an exploratory approach where one can test 
#
# - (i) distribution information ($\Theta = 0$),
# - (ii) dependence information ($\Theta = 1$), and
# - (iii) a mix of both information ($\Theta = 0.5$).
#
# Ideally, $\Theta$ should reflect the balance of dependence and distribution information in the data.
#
# In a supervised setting, one could select an estimate $\hat{\Theta}$ of the right balance $\Theta^{*}$ optimizing some loss function by techniques such as cross-validation. Yet, the lack of a clear loss function makes the estimation of $\Theta^{*}$ difficult in an unsupervised setting".


# **Note:** The implementation of GNPR in the ArbitrageLab package was adjusted so that $\tilde{d}_{0}^{2}$
# (dependence information distance) is being calculated using the 1D Optimal Transport Distance following the example in the
# [POT package documentation](https://pythonot.github.io/auto_examples/plot_OT_1D.html#sphx-glr-auto-examples-plot-ot-1d-py).
# This solution was proposed by Marti.
#
# Distributions of random variables are approximated using histograms with a given number of bins as input.
#
# Optimal Transport Distance is then obtained from the Optimal Transportation Matrix (OTM) using
# the Loss Matrix (M) as shown in 
# [Optimal Transport blog post by Marti](https://gmarti.gitlab.io/qfin/2020/06/25/copula-optimal-transport-dependence.html):
#
# $$\tilde{d}_{0}^{2} = tr (OT^{T} * M)$$
#
# where $tr( \cdot )$ is trace of a matrix and $\cdot^{T}$ is a transposed matrix.
#
# This approach solves the issue of defining support for underlying distributions and choosing a number of bins.


# ---


# ## Usage of the algorithms


# This part shows how the GPR and the GNPR distances can be used to measure codependence between a set of stocks


import arbitragelab as al
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Loading the dataset of stocks
stocks = pd.read_csv('../../Sample-Data/stock_prices.csv')
stocks.set_index('Date', inplace=True)
stocks.index = pd.to_datetime(stocks.index)

# Taking first 10 stocks for better output visualization
stocks = stocks.iloc[:,0:10]
stocks.head()


# Calculating returns of a given dataset of stocks
stocks_returns = stocks.pct_change()[1:]
stocks_returns.iloc[:,0:10].head()


# Calculating GPR distance between two tickers - EEM and EWG
gpr_dist = al.codependence.gpr_distance(stocks_returns['EEM'], stocks_returns['EWG'], theta=0.5)
print('GPR distance between EEM and EWG measuring a mix of distribution and dependence information is: ', gpr_dist)


# Calculating GPR distance between two tickers - EEM and EWG using only dependence information
gpr_dist = al.codependence.gpr_distance(stocks_returns['EEM'], stocks_returns['EWG'], theta=1)
print('GPR distance between EEM and EWG measuring dependence information is: ', gpr_dist)


# Calculating GNPR distance between two tickers - EEM and EWG
gpr_dist = al.codependence.gnpr_distance(stocks_returns['EEM'], stocks_returns['EWG'], theta=0.5)
print('GNPR distance between EEM and EWG measuring a mix of distribution and dependence information is: ', gpr_dist)


# Calculating GNPR distance between two tickers - EEM and EWG using only distribution information and 100 bins
gpr_dist = al.codependence.gnpr_distance(stocks_returns['EEM'], stocks_returns['EWG'], theta=0, n_bins=100)
print('GNPR distance between EEM and EWG measuring distribution information is: ', gpr_dist)


# These codependence measures can also be used on the whole dataframes, the results will be codependence matrices.


# Calculating GPR distance between all stocks with Θ = 0.5
gpr_matrix = al.codependence.get_dependence_matrix(stocks_returns, dependence_method='gpr_distance',theta=0.5)

print('GPR distance matrix measuring a mix of distribution and dependence information:')
gpr_matrix


# Calculating GNPR distance between all stocks with Θ = 1
gnpr_matrix_dep = al.codependence.get_dependence_matrix(stocks_returns, dependence_method='gnpr_distance',theta=1)

# Calculating GNPR distance between all stocks with Θ = 0.5
gnpr_matrix_mix = al.codependence.get_dependence_matrix(stocks_returns, dependence_method='gnpr_distance',theta=0.5)

# Calculating GNPR distance between all stocks with Θ = 0
gnpr_matrix_dist = al.codependence.get_dependence_matrix(stocks_returns, dependence_method='gnpr_distance',theta=0)

print('GNPR distance matrix measuring distribution information:')
gnpr_matrix_dist


# ### Heatmap of GNPR distribution information distance


# Plotting the heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(gnpr_matrix_dist, ax = ax, cbar_kws={'label': 'GNPR distribution distance'})

ax.set_title('Heatmap of GNPR distribution information distance (Θ = 0)')
plt.show()


# ### Heatmap of GNPR mix of distribution and dependence information distance


# Plotting the heatmap
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(gnpr_matrix_mix, ax = ax, cbar_kws={'label': 'GNPR mixed distance'})

ax.set_title('Heatmap of GNPR mix of distribution and dependence information distance (Θ = 0.5)')
plt.show()


# ### Heatmap of GNPR dependence information distance


# Plotting the heatmap
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(gnpr_matrix_dep, ax = ax, cbar_kws={'label': 'GNPR dependence distance'})

ax.set_title('Heatmap of GNPR dependence information distance (Θ = 1)')
plt.show()


# As seen from the heat maps of GNPR distance matrices, distribution and information distances show different types of codependency. However, when using a mixed approach with $\Theta = 0.5$ the distribution information part is too high, which makes the dependence information adjustment hardly visible, so for a balanced output one may want to increase $\Theta$ in this particular example. 


# ---


# ## Conclusion


# This notebook describes the GPR and the GNPR distances how they may be used in real-life applications.  
#
# These novel distances were originally presented by the _Gautier Marti_ in the work __“Some contributions to the clustering of financial time series and applications to credit default swaps”__  [available here](https://www.researchgate.net/publication/322714557).
#
# Key takeaways from the notebook:
# - Distances can be roughly classified in two families:
#   - Distributional distances, which focus on dissimilarity between probability distributions and quantify divergences in marginal behaviours.
#   - Dependence distances, which focus on the joint behaviours of random variables, generally ignoring their distribution properties.
# - Distance $d_{\Theta}$ between two random variables allows to discriminate random variables both on distribution and dependence.
# - Distance $d_{\Theta}$ is a metric that falls in range $[0, 1]$.
# - GPR distance is a fast and good proxy for distance $d_{\Theta}$ between two Gaussians.
# - GNPR distance is a proxy for distance $d_{\Theta}$ that works on i.i.d. random variables, it requires a declared width of bins for values discretization.
# - $d_{\Theta}$ should be chosen to reflect the balance of dependence and distribution information in the data.
# - The ArbitrageLab implementation has $\tilde{d}_{0}^{2}$ in GNPR is adjusted to using 1D Optimal Transport Distance to solve the issue of defining support for underlying distributions and choosing a number of bins.


# ## References


# 1. Marti, Gautier. (2017). Some contributions to the clustering of financial time series and applications to credit default swaps. Available at: https://www.researchgate.net/publication/322714557
#
# 2. Marti, Gautier. (2020). Measuring non-linear dependence with Optimal Transport. Available at: https://gmarti.gitlab.io/qfin/2020/06/25/copula-optimal-transport-dependence.html

