# Generated from: optimal_clustering.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Optimal Clustering


import numpy as np
import pandas as pd
# from sklearn.neighbors.kde import KernelDensity
from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt


# 1. What is the main difference between outputs from hierarchical and partitionning clustering algorithms. Why can't the output from the latter be converted into the output of the former ?
#
# The output from a partinioning clustering algorithm (for instance, k-means) is a partition whereas the output from the hierarchical clustering algorithms is a tree known as a dendrogram as well. We can get from the tree multiple partitions but we cannot get from a partition, a hierarchical clustering. The reason is that the later doesn't provide enough information (in distance or similarity) on how other groups in the hierarchical tree are distanced. 


# 2. Is MSCI's GICS classification system an example of hierarchical or partitionning clustering ? Using the appropriate algorithm on a correlation matrix, try to replicate the MSCI classification. To compare the clustering output with MSCI's, use the clustering distance introduction in Section 3.
#
# THe GICS® classification system is an example of hierarchical clustering (more information on how the clustering is made can be found under [here](https://www.msci.com/documents/1296102/11185224/GICS+Methodology+2020.pdf/9caadd09-790d-3d60-455b-2a1ed5d1e48c?t=1578405935658). 
#
# We can use a hierarchical clustering on the companies returns.


# Download the data from IEX 

# Disclaimer, it would have been much more precise to use bar data to construct our correlation matrix 

# Retrieve the company's categorisation 

# Build the hierarchical clustering and compare


# 3. Modify Code Snippets 4.1 and 4.2 to work with a spectral biclustering algorithm. Do you get fundamentally different results ? 


# çç


# 3. Modify Code Snippets 4.1 and 4.2 to work with a spectral biclustering algorithm. Do you get fundamentally different results ? 


# çç

