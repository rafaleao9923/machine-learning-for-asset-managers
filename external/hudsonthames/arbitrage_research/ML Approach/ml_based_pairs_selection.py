# Generated from: ml_based_pairs_selection.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# * Reference: __Enhancing a Pairs Trading strategy with the application of Machine Learning__ _by_ Simão Moraes Sarmento and Nuno Horta


from IPython.display import Image
import pandas as pd
import arbitragelab as al
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


# # Implementation of a Machine Learning based Pairs Selection Framework
#
# ## Abstract
#
# In this paper[1], Horta and Sarmento propose a two-stage solution to applying machine learning to the problem of pairs trading. The first stage involves the application of a clustering algorithm to infer any meaningful clusters and using these groups to generate pairs that will be run through a selection process that will supply a list of pairs that comply with the conditions set. 
#
# The second stage should start by training forecasting algorithms to predict the spreads of the selected pairs. Furthermore, decile-based and quintile-based thresholds should be collected to integrate the trading model. Having fitted the forecasting algorithms and obtained the two combinations for the thresholds, the model can be applied to the validation set. From the validation performance, the best threshold combination is selected. At this point, the model is finally ready to be applied on unseen data, from which the performance may be inferred.
#
# ## Introduction
#
# This notebook will focus on the first stage, which refers to the pairs selection methodology. It will involve the application of PCA to distill the returns universe into a lower dimensional form. Then the OPTICS algorithm will be applied, on the expectation that it infers meaningful clusters of assets from which to select the pairs. The motivation is to let the data explicitly manifest itself, rather than manually defining the groups each security should belong to. The proposed methodology encompasses the following steps:
#
# - Dimensionality reduction - find a compact representation for each security;
# - Unsupervised Learning - apply an appropriate clustering algorithm;
# - Select pairs - define a set of rules to select pairs for trading.


Image(filename='images/prposed_framework_diagram.png') 


# ---


# # Usage of Implementation
#
# To start using this module we first need to set up our asset universe, in this case, the dataset used is the daily price data of every asset in the S&P 500.


prices_df = pd.read_csv('./data/data.csv').set_index('Date').dropna()
prices_df.index = pd.to_datetime(prices_df.index)

prices_df = prices_df.last('10Y')

prices_df.sample(10)


# ## Step 1 - Dimensionality Reduction
#
#
#
# ### Using PCA to find a compact representation for each security
#
# - Extracts common underlying risk factors from securities’ returns;
# - Produces a compact representation for each security;
#
# Before applying PCA, the pricing data needs to be converted to returns and then normalized by subtracting the mean and dividing by the standard deviation, as follows:
#
# Returns 
#
# $$ R_{i, t} = \frac{P_{i,t} - P_{i,t-1}} {P_{i,t-1}} $$
#
#
# Data Normalization
#
# $$ Y_{i} =  \frac{R_{i} - \bar{R_{i}}} {\sigma_{i}} $$
#
# Decomposition
#
# By applying PCA, $A$ is decomposed into the resulting eigenvectors and eigenvalues. An $n$ number of eigenvectors is selected where $n$ represents the number of features to describe the transformed data. The matrix containing the eigenvalues is set as the feature vector. The final dataset is obtained by multiplying the original matrix A by the feature vector.


ps = al.ml_approach.OPTICSDBSCANPairsClustering(prices_df)

# Here the first parameter is the number of features to reduce to.
ps.dimensionality_reduction_by_components(5)

# The following will plot the feature vector from the previous method call.
ps.plot_pca_matrix();


# A quick visual inspection of the feature vector shows a good amount of densely packed groups/clusters. If the points are too sparse, this likely suggests that you don't have enough datapoints.


# ## Step 2 - Unsupervised Learning
# ### Applying OPTICS clustering algorithm
#
# - No need to specify the number of clusters in advance;
# - Robust to outliers;
# - Suitable for clusters with varying density
#
#
# The first method is to use the OPTICS clustering algorithm and letting the built-in automatic 
# procedure to select the most suitable $\epsilon$ for each cluster. 


%matplotlib inline

clustered_pairs = ps.cluster_using_optics(min_samples=3)
ps.plot_clustering_info(method='OPTICS', n_dimensions=3);


# ### Applying DBSCAN clustering algorithm
#
# The second method is to use the DBSCAN clustering algorithm. This is to be used when the user 
# has domain-specific knowledge that can enhance the results given the algorithm's parameter 
# sensitivity. A possible approach to finding $\epsilon$ described in [2] is to inspect the knee plot and fix a 
# suitable $\epsilon$ by observing the global curve turning point.


ps.plot_knee_plot();


# The following are example results of DBSCAN clustering using different $\epsilon$ values, showing the efficacy of the method at different _'k-distance'_ values from the knee plot. 


ps.cluster_using_dbscan(eps=0.1, min_samples=3, metric='euclidean')
ps.plot_clustering_info(method='DBSCAN @ eps: 0.1', figsize=(8,8));

print('-' * 100)

ps.cluster_using_dbscan(eps=0.022, min_samples=3, metric='euclidean')
ps.plot_clustering_info(method='DBSCAN @ eps: 0.022', figsize=(8,8));

print('-' * 100)

ps.cluster_using_dbscan(eps=0.015, min_samples=3, metric='euclidean')
ps.plot_clustering_info(method='DBSCAN @ eps: 0.015', figsize=(8,8));


# The first plot shows the results with the upper bound value of 0.1, which was not sensitive enough to detect any groups. The second plot was set with the optimal value from the knee plot of 0.022 which detected a good amount of structure. The final plot was set with lower bound value of 0.015, which only managed to detect very densely packed clusters. 


# ## Step 3 - Select Pairs
# ### Finding resulting pairs that pass the following set of rules
#
# Sarmento and Horta suggest four criteria to further filter the potential pairs to increase the probability of selecting pairs of securities whose prices will continue to mean revert in the future. 
# - Cointegration using the Engle-Granger Test. 
# - Hurst Exponent $H$: Keep the pairs with (spread) $H<0.5$ for mean-reversion. 
# - Halflife: Keep the pairs with (spread) halflife in between $1$ day and $1$ year.
# - Minimum number of crossing mean in a year: Keep the pairs with (spread) crossing its mean $12$ times a year.
#
#
# These four criteria indicate attractive characteristics for potential tradable pairs of securities. The Engle-Granger tests the pair for cointegration. A Hurst exponent below 0.5 indicates that the pair of prices regresses strongly to the mean. Pairs with extreme half-life values, below 1 or above 356, are excluded from the selected pairs. Extreme half-life values indicate a price series that either reverts too quickly or too slowly to be traded. Finally, the price series must cross the long-term spread mean on average at least 12 times a year.


# <div class="alert alert-warning">
#
# **Warning:** The following pairs selection function is computationally heavy, so execution is going to be long and might slow down your system.
#
# </div>


# Removing duplicates from clustered pairs
clustered_pairs = list(set(clustered_pairs))


# Load data into spread selector
sp = al.spread_selection.CointegrationSpreadSelector(prices_df=prices_df,
                                                     baskets_to_filter=clustered_pairs)
                                                    

# Filtered spreads that passed the criteria by specifying hedge ratio calculation method as well as filtering conditions.
filtered_spreads = sp.select_spreads()


# The module can also work with user-specified spreads to test if a spread passes cointegration selection criterion.
spread = sp.spreads_dict['AAL_FTI'].copy() # Let's take an arbitrary spread.
pairs_selector_custom = al.spread_selection.CointegrationSpreadSelector(prices_df=None, baskets_to_filter=None)
stats = pairs_selector_custom.generate_spread_statistics(spread, log_info=True) # log_info=True to save stats.
print(stats)


filtered_spreads_custom = pairs_selector_custom.apply_filtering_rules(adf_cutoff_threshold=0.9, hurst_exp_threshold=0.5)
print(filtered_spreads_custom)


# Checking the resulting spreads
filtered_spreads


len(filtered_spreads)


# Plot one of the spreads
sp.spreads_dict['AAL_FTI'].plot(figsize=(12,6));


# The following detailed spread statistics can be obtained
sp.selection_logs.loc[['AAL_FTI']].T


# ---


# # Conclusion
#
# This notebook describes the proposed Pairs Selection Framework also shows example usage of the implemented framework to efficiently reduce the search space and select quality trading pairs. 
#
# - Ten years of daily stock price data for 400 securities were reduced to 5 dimensions through PCA. 
# - 1643 spreads from the clusters met the four selection criteria. 
#
# Key takeaways:
# - The number of pairs left for a trader to handle is much less compared to the number of pairs generated through an open combinatorial search of the whole asset universe.
# - (Based on the previous research) Most of the final pairs selected follow expected economic sectoral clusters even though there was no implied industry/sectoral grouping anywhere in the framework.
#
# Solutions to common pitfalls:
# - Dimensionality reduction techniques need a certain amount of data to work reliably, so if instability is encountered at this junction, it is suggested to increase the amount of data.
# - The number of PCA components needs to balance the amount of variance represented with density in euclidean distance. The rule of thumb is a number less than 15 components.
# - When in doubt use OPTICS.
# - For the clustering methods, the _'minimum samples'_ argument needs to be large enough so that the generated clusters are homogeneous. The rule of thumb is a number larger than 3.


# # References
# 1. Sarmento, Simão. & Horta, Nuno. (2020). Enhancing a Pairs Trading strategy with the application of Machine Learning. Available at: http://premio-vidigal.inesc.pt/pdf/SimaoSarmentoMSc-resumo.pdf
#
# 2. Rahmah N, Sitanggang S (2016). Determination of Optimal Epsilon (Eps) Value on DBSCAN Algorithm to Clustering Data on Peatland Hotspots in Sumatra. Available at: https://doi.org/10.1088/1755-1315/31/1/012012

