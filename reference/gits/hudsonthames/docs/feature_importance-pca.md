# PCA Features and Analysis¶

Get full version of MlFinLab

  

A partial solution to solve substitution effects is to orthogonalize features
- apply PCA to them. However, PCA can be used not only to reduce the dimension
of your data set, but also to understand whether the patterns detected by
feature importance are valid.

Suppose, that you derive orthogonal features using PCA. Your PCA analysis has
determined that some features are more ‘principal’ than others, without any
knowledge of the labels (unsupervised learning). That is, PCA has ranked
features without any possible overfitting in a classification sense.

When your MDI, MDA, SFI analysis selects as most important (using label
information) the same features that PCA chose as principal (ignoring label
information), this constitutes confirmatory evidence that the pattern
identified by the ML algorithm is not entirely overfit. Here is the example
plot of MDI feature importance vs PCA eigen values:

[![../_images/pca_correlation_analysis.png](../_images/pca_correlation_analysis.png)](../_images/pca_correlation_analysis.png)

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium8.png)](../_images/implementation_medium8.png)

[![Code implementation
demo](../_images/implementation_small5.png)](../_images/implementation_small5.png)

[![Code implementation
demo](../_images/implementation_medium8.png)](../_images/implementation_medium8.png)

* * *

## Example¶

Let’s see how PCA feature extraction is analysis are done using MlFinLab
functions:

[![Code example
demo](../_images/example_medium6.png)](../_images/example_medium6.png)

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

