Information-driven bars are based on the notion of sampling a bar when new
information arrives to the market. The two types of information-driven bars
implemented are imbalance bars and run bars. For each type, tick, volume, and
dollar bars are included.

For those new to the topic, it is discussed in the graduate level textbook:
Advances in Financial Machine Learning, Chapter 2.

Warning

This is a very advanced financial data structure with very little to no
academic papers written about them. Our team has analysed the statistical
properties and its not clear to us how to use this structure.

We highly recommend that you read the literature, plus that of microstructural
features before committing to this data structure.

* * *

# Run Bars¶

Get full version of MlFinLab

  

  

Run bars share the same mathematical structure as imbalance bars, however,
instead of looking at each individual trade, we are looking at sequences of
trades in the same direction. The idea is that we are trying to detect order
flow imbalance caused by actions such as large traders sweeping the order book
or iceberg orders.

2 types of run bars are implemented in MlFinLab:

>   1. Expected number of ticks, defined as EWMA (book implementation)
>
>   2. Constant number of expected number of ticks.
>
>

* * *

## Implementations¶

There are 2 different implementations which have been discussed in the
previous section.

### EMA Version¶

#### Tick Bars¶

[![Code implementation
demo](../_images/implementation_medium6.png)](../_images/implementation_medium6.png)

#### Volume Bars¶

[![Code implementation
demo](../_images/implementation_medium6.png)](../_images/implementation_medium6.png)

#### Dollar Bars¶

[![Code implementation
demo](../_images/implementation_medium6.png)](../_images/implementation_medium6.png)

### Constant Version¶

#### Tick Bars¶

[![Code implementation
demo](../_images/implementation_medium6.png)](../_images/implementation_medium6.png)

#### Volume Bars¶

[![Code implementation
demo](../_images/implementation_medium6.png)](../_images/implementation_medium6.png)

#### Dollar Bars¶

[![Code implementation
demo](../_images/implementation_medium6.png)](../_images/implementation_medium6.png)

* * *

## Example¶

[![Code example
demo](../_images/example_medium4.png)](../_images/example_medium4.png)

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

