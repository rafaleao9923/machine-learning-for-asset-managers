# Other Microstructural Features¶

Get full version of MlFinLab

  

This module implements features from Advances in Financial Machine Learning,
Chapter 18: Entropy features and Chapter 19: Microstructural features.

[![Kyle's Lambda](../_images/kyle_lambda.png)](../_images/kyle_lambda.png)

Closing prices in blue, and Kyle’s Lambda in red¶

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 18 & 19 _by_ Marcos Lopez de Prado.

## Message Encoding¶

Entropy is used to measure the average amount of information produced by a
source of data. In financial machine learning, sources of data to get entropy
from can be tick sizes, tick rule series, and percent changes between ticks.
Estimating entropy requires the encoding of a message. The researcher can
apply either a binary (usually applied to tick rule), quantile or sigma
encoding.

### Implementation¶

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

## Second and Third Generation Features¶

When bars are generated (time, volume, imbalance, run) researcher can get
inter-bar microstructural features: Kyle/Amihud/Hasbrouck lambdas, and VPIN.

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

## Features Generator¶

Some microstructural features need to be calculated from trades (tick
rule/volume/percent change entropies, average tick size, vwap, tick rule sum,
trade based lambdas). MlFinLab has a special function which calculates
features for generated bars using trade data and bar date_time index.

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Example¶

[![Code example
demo](../_images/example_big4.png)](../_images/example_big4.png)

* * *

## Research Notebook¶

The following research notebooks can be used to better understand labeling
excess over mean.

[![Notebook demo](../_images/notebook7.png)](../_images/notebook7.png)

[![Notebook demo](../_images/notebook7.png)](../_images/notebook7.png)

* * *

## Presentation Slides¶

[![../_images/lecture8.png](../_images/lecture8.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3270269)

Note

  * pg 1-14: Structural Breaks

  * pg 15-24: Entropy Features

  * pg 25-37: Microstructural Features

[![../_images/micro_slides.png](../_images/micro_slides.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3193702)

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

  * [de Prado, M.L., 2018. Market Microstructure in the Age of Machine Learning. Available at SSRN 3193702.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3193702)

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 8/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3270269)

