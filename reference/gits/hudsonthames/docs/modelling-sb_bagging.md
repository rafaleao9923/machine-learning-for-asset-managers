# Sequentially Bootstrapped Ensembles¶

Get full version of MlFinLab

  

In the sampling section we have shown that sampling should be done by
Sequential Bootstrapping.

The SequentiallyBootstrappedBaggingClassifier and
SequentiallyBootstrappedBaggingRegressor extend [sklearn](https://scikit-
learn.org/)’s Bagging Classifier/Regressor by using Sequential Bootstrapping
instead of random sampling.

In order to build the indicator matrix we need the Triple Barrier Events
(samples_info_sets) and price bars used to label the training data set. That
is why samples_info_sets and price bars are input parameters for the
classifier/regressor.

To better understand the underlying method, you may be interested in reading
the [Sequential Bootstrapping](../sampling/sequential_boot.html#sampling-
sequential-boot) page of MlFinLab documentation.

Note

**Underlying Literature**

The following sources describe this method in more detail:

  * [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 4 _by_ Marcos Lopez de Prado.

* * *

## Implementation¶

Warning

This model is computationally expensive and may take some time to run.

The model from the MlFinlab package before version 1.4.0 was already orders of
magnitude faster than the original, described in Advances in Financial Machine
Learning.

We’ve further improved the model, starting from MlFinLab version 1.5.0 the
execution is up to 200 times quicker compared to the models from version 1.4.0
and earlier. (The speed improvement depends on the size of the input dataset)

[![Code implementation
demo](../_images/implementation_medium10.png)](../_images/implementation_medium10.png)

[![Code implementation
demo](../_images/implementation_medium10.png)](../_images/implementation_medium10.png)

* * *

## Example¶

An example of using the SequentiallyBootstrappedBaggingClassifier

[![Code example
demo](../_images/example_big7.png)](../_images/example_big7.png)

* * *

## Research Notebook¶

The following research notebooks can be used to better understand Ensemble
Methods.

[![Notebook demo](../_images/notebook10.png)](../_images/notebook10.png)

* * *

## Research Article¶

Read our article on the topic

  

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

