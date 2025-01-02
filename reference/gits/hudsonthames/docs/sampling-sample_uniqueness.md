# Sample Uniqueness¶

Get full version of MlFinLab

  

Let’s look at an example of 3 samples: A, B, C.

Imagine that:

  * A was generated at \\(t_1\\) and triggered on \\(t_8\\)

  * B was generated at \\(t_3\\) and triggered on \\(t_6\\)

  * C was generated on \\(t_7\\) and triggered on \\(t_9\\)

In this case we see that A used information about returns on \\([t_1,t_8]\\)
to generate label-endtime which overlaps with \\([t_3, t_6]\\) which was used
by B, however C didn’t use any returns information which was used by to label
other samples. Here we would like to introduce the concept of concurrency.

We say that labels \\(y_i\\) and \\(y_j\\) are concurrent at \\(t\\) if they
are a function of at least one common return at \\(r_{t-1,t}\\)

In terms of concurrency label C is the most ‘pure’ as it doesn’t use any piece
of information from other labels, while A is the ‘dirtiest’ as it uses
information from both B and C. By understanding average label uniqueness you
can measure how ‘pure’ your dataset is based on concurrency of labels. We can
measure average label uniqueness using get_av_uniqueness_from_triple_barrier
function from the mlfinlab package.

This function is the orchestrator to derive average sample uniqueness from a
dateset labeled by the triple barrier method.

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium12.png)](../_images/implementation_medium12.png)

* * *

## Example¶

An example of calculating average uniqueness given that we have already have
our barrier events can be seen below:

[![Code example
demo](../_images/example_medium9.png)](../_images/example_medium9.png)

We would like to build our model in such a way that it takes into account
label concurrency (overlapping samples). In order to do that we need to look
at the bootstrapping algorithm of a Random Forest.

Lets move onto the next section on Sequential Bootstrapping.

* * *

## Research Notebook¶

The following research notebook can be used to better understand the
previously discussed sampling method.

[![Notebook demo](../_images/notebook13.png)](../_images/notebook13.png)

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

