# Single Futures Roll¶

Get full version of MlFinLab

  

## Introduction¶

Working with futures contracts has the unique problem that a given contract
has an expiration date. To ensure the adequacy of the data, we need to account
for the “switching” between the contracts that expire and the ones that take
their place.

Simply performing an auto-roll and stitching the contracts together doesn’t
account for the price difference between the old contract and the new one when
the expiry date actually comes. Often this difference is quite small, however,
for some contracts, it can be quite substantial (especially if the underlying
asset has high carry costs).

Ignoring the price difference may lead to false spikes/pitfalls around the
expiry data that, in their turn, may falsely signify a trading opportunity
where actually there is none.

The answer to the problem is the “ETF trick” from the Advances in Financial
Machine Learning by professor Marcos Lopez de Prado.

## Procedure¶

_“The ETF trick can handle the rolls of a single futures contract,_ _as a
particular case of a 1-legged spread. However, when dealing with a single
futures contract, an equivalent_ _and more direct approach is to form a time
series of cumulative roll gaps, and detract that gaps series from_ _the price
series.”_

Note

On further expirations the adjustment factor need to be accounted for as
follows:

>   * **Absolute returns:** adjustment_factor = previous_adjustment_factor +
> new_roll_gap.
>
>   * **Relative returns:** adjustment_factor = previous_adjustment_factor *
> new_roll_gap.
>
>

To generate the correct continuous contract, a 3-step procedure needs to be
performed:

  1. Get absolute and relative roll gaps.

  2. Filter out rows with price info of the nearest contract only.

  3. Apply the roll gaps on the copy of the first contract.

## Implementation:¶

[![Code implementation
demo](../_images/implementation_medium6.png)](../_images/implementation_medium6.png)

## Example¶

[![Code example
demo](../_images/example_big3.png)](../_images/example_big3.png)

![https://hudsonthames.org/wp-
content/uploads/2019/08/futures_roll_4.png](https://hudsonthames.org/wp-
content/uploads/2019/08/futures_roll_4.png)

## Research Notebook¶

The following research notebooks can be used to better understand the Futures
Roll.

[![Notebook demo](../_images/notebook6.png)](../_images/notebook6.png)

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

