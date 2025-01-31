# Model Fingerprint Algorithm¶

Get full version of MlFinLab

  

Another way to get a better understanding of a machine learning model is to
understand how feature values influence model predictions. Feature effects can
be decomposed into 3 components (fingerprints):

  * **Linear component**

  * **Non-linear component**

  * **Pairwise interaction component**

Yimou Li, David Turkington, and Alireza Yazdani published a paper in the
Journal of Financial Data Science [‘Beyond the Black Box: An Intuitive
Approach to Investment Prediction with Machine
Learning’](https://www.statestreet.com/content/dam/statestreet/documents/ss_associates/SSGMJFDSWint20BeyondtheBlackBox.pdf)
which describes in details the algorithm of extracting **linear** , **non-
linear** and **pairwise** feature effects. This module implements the
algorithm described in the article.

Tip

  * I would like to highlight that this algorithm is one of the tools that our team uses the most! There are 2 classes which inherit from an abstract base class, you only need to instantiate the child classes.

  * This algorithm is also a favourite of multiple award winning hedge funds!

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_big5.png)](../_images/implementation_big5.png)

[![Code implementation
demo](../_images/implementation_small5.png)](../_images/implementation_small5.png)

[![Code implementation
demo](../_images/implementation_small5.png)](../_images/implementation_small5.png)

* * *

## Example¶

[![Code example
demo](../_images/example_big5.png)](../_images/example_big5.png)

[![../_images/effects.png](../_images/effects.png)](../_images/effects.png)

* * *

## Research Article¶

Read our article on the topic

  

* * *

## References¶

[![../_images/jfds.jpg](../_images/jfds.jpg)](https://www.statestreet.com/content/dam/statestreet/documents/ss_associates/SSGMJFDSWint20BeyondtheBlackBox.pdf)

  * [Li, Y., Turkington, D. and Yazdani, A., 2020. Beyond the black box: an intuitive approach to investment prediction with machine learning. The Journal of Financial Data Science, 2(1), pp.61-75.](https://www.statestreet.com/content/dam/statestreet/documents/ss_associates/SSGMJFDSWint20BeyondtheBlackBox.pdf)

