# Documentation for `ch6_feature_importance_analysis.py`

## Overview

This script performs feature importance analysis using various methods, including Mean Decrease Impurity (MDI) and Mean Decrease Accuracy (MDA), on a synthetic dataset generated for classification tasks.

### Functions

- **getTestData(n_features, n_informative, n_redundant, n_samples, random_state, sigmaStd)**: Generates a synthetic dataset with informative, redundant, and noisy features for classification.

- **featImpMDI(fit, featNames)**: Computes feature importance based on the Mean Decrease Impurity from a fitted ensemble model.

- **featImpMDA(clf, X, y, n_splits)**: Computes feature importance based on Out-of-Sample score reduction using cross-validation.

- **groupMeanStd(df0, clstrs)**: Calculates the mean and standard deviation of feature importances grouped by clusters.

- **featImpMDI_Clustered(fit, featNames, clstrs)**: Computes clustered feature importance using MDI.

- **featImpMDA_Clustered(clf, X, y, clstrs, n_splits)**: Computes clustered feature importance using MDA.

### Main Execution

The script generates synthetic datasets, fits models, computes feature importances, and visualizes the results using bar plots and heatmaps.