# Directional Change¶

Get full version of MlFinLab

  

The Directional Change module contains functions and classes related to the
detection of general price movement and feature generation based on direction
split. It is planned to later build a Regime Change module on top of
Directional Change tools.

These include:

    

  * signal

  * total_price_movement

  * time_for_completion

  * time_adjusted_return

Note

**Underlying Literature**

  * [Detecting Regime Change in Computational Finance](https://www.routledge.com/Detecting-Regime-Change-in-Computational-Finance-Data-Science-Machine/Chen-Tsang/p/book/9780367536282) _by_ Jun Chen & Edward P K Tsang

  * [Directional Changes: A New Way to Look at Price Dynamics](https://www.researchgate.net/publication/320000412) _by_ Edward P K Tsang

* * *

## Is Directional Change¶

Directional Change (DC) is a metric which samples data points at their peaks
and troughs in their movement. Price movements are defined by two types of
events: **Directional Change (DC) Event** and **Overshoot (OS) Event**. With a
pre-defined **Threshold** , every price curve can be dissected by these two
components.

The value of the threshold needs to be pre-defined by the observer. It
represents how big of a price change the observer considers as significant.

A DC Event will be confirmed when the price change reaches the threshold. A DC
Event is not usually immediately followed by an opposite DC Event, but by an
OS Event. An OS Event records the price movement from one DC Event to the
next.

Price movements are partitioned into uptrend and downtrend. When the price
changes from Point A to Point B, the price change reaches a threshold
\\(\theta\\), then a DC Event is confirmed. Point A is then considered as an
**Extreme point (EXT)**. And Point B is considered as a **Directional Change
Confirmation (DCC) point**. Similarly, the next DC Event is confirmed at Point
D. The price movement between two DC Events is considered an OS Event (from
Point B to C).

![../_images/directional_change_event.png](../_images/directional_change_event.png)

Figure 1: Directional Change Event. [(Jun Chen & Edward P K Tsang
2020)](https://www.routledge.com/Detecting-Regime-Change-in-Computational-
Finance-Data-Science-Machine/Chen-Tsang/p/book/9780367536282)¶

### Implementation¶

This is an implementation of the is_directional_change function over a time
series.

[![Code implementation
demo](../_images/implementation_medium7.png)](../_images/implementation_medium7.png)

### Example¶

[![Code example
demo](../_images/example_small2.png)](../_images/example_small2.png)

* * *

## Total Price Movement¶

This indicator measures the absolute percentage of the price change in a
trend. As shown in Figure 1, Total Price Movement (TMV) is used to measure the
percentage change from Point A to Point C, normalized by the threshold. It
usually measures the total price change of a DC event and an OS event. It is
defined as:

\\[TMV_{EXT}(n) = (P_{EXT}(n) - P_{EXT}(n-1)) / P_{EXT}(n-1) * \theta\\]

### Implementation¶

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

### Example¶

[![Code example
demo](../_images/example_small2.png)](../_images/example_small2.png)

* * *

## Time for Completion¶

This indicator measures the amount of the physical time (T) that it takes to
complete a TMV trend. As shown in Figure 1, it measures the time from Time 3
to Time 9. It is defined as:

\\[T(n) = t_{EXT}(n) - t_{EXT}(n - 1),\\]

where \\(t_{EXT}(n)\\) represents the time at \\(n-th\\) extreme point.

### Implementation¶

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

### Example¶

[![Code example
demo](../_images/example_small2.png)](../_images/example_small2.png)

* * *

## Time Adjusted Return¶

This indicator measures the absolute return (R) in a trend. It is calculated
by dividing the absolute TMV by the time interval T. It measures the
percentage of price change per time unit:

\\[R(n) = TMV_{EXT}(n) / T(n) * \theta\\]

where \\(R(n)\\) represents the value of the time-adjusted return of DC at the
\\(n-th\\) extreme point.

### Implementation¶

[![Code implementation
demo](../_images/implementation_small4.png)](../_images/implementation_small4.png)

### Example¶

[![Code example
demo](../_images/example_small2.png)](../_images/example_small2.png)

## References¶

  * [Chen, J. and Tsang, E.P., 2020. Detecting Regime Change in Computational Finance: Data Science, Machine Learning and Algorithmic Trading. CRC Press.](https://www.routledge.com/Detecting-Regime-Change-in-Computational-Finance-Data-Science-Machine/Chen-Tsang/p/book/9780367536282)

  * [Tsang, E.P., 2017, March. Directional changes: A new way to look at price dynamics. In International Conference on Computational Intelligence, Communications, and Business Analytics (pp. 45-55). Springer, Singapore.](https://www.researchgate.net/publication/320000412)

