# Sample Weights¶

Get full version of MlFinLab

  

MlFinLab supports two methods of applying sample weights. The first is
weighting an observation based on its given return as well as average
uniqueness. The second is weighting an observation based on a time decay.

* * *

## Implementations¶

### By Returns and Average Uniqueness¶

The following function utilizes a samples average uniqueness and its return to
compute sample weights:

[![Code implementation
demo](../_images/implementation_medium12.png)](../_images/implementation_medium12.png)

### Example¶

This function can be utilized as shown below assuming we have already found
our barrier events

[![Code example
demo](../_images/example_small6.png)](../_images/example_small6.png)

### By Time Decay¶

The following function assigns sample weights using a time decay factor

[![Code implementation
demo](../_images/implementation_medium12.png)](../_images/implementation_medium12.png)

### Example¶

This function can be utilized as shown below assuming we have already found
our barrier events

[![Code example
demo](../_images/example_small6.png)](../_images/example_small6.png)

* * *

## Research Notebook¶

The following research notebooks can be used to better understand the
previously discussed sampling methods

Note

This is the same notebook as seen in the Sample Uniqueness docs.

[![Notebook demo](../_images/notebook13.png)](../_images/notebook13.png)

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

