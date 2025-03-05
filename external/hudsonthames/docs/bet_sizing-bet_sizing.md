# Bet Sizing in ML¶

Get full version of MlFinLab

  

“There are fascinating parallels between strategy games and investing. Some of
the best portfolio managers I have worked with are excellent poker players,
perhaps more so than chess players. One reason is bet sizing, for which Texas
Hold’em provides a great analogue and training ground. Your ML algorithm can
achieve high accuracy, but if you do not size your bets properly, your
investment strategy will inevitably lose money. In this chapter we will review
a few approaches to size bets from ML predictions.” [Advances in Financial
Machine Learning](https://www.wiley.com/en-
us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 10: Bet
Sizing, pg 141.

The code in this directory falls under 3 submodules:

  1. Bet Sizing: We have extended the code from the book in an easy to use format for practitioners to use going forward.

  2. EF3M: An implementation of the EF3M algorithm.

  3. Chapter10_Snippets: Documented and adjusted snippets from the book for users to experiment with.

[![../_images/bet_sizing.png](../_images/bet_sizing.png)](../_images/bet_sizing.png)

Note

**Underlying Literature**

The following sources describe this method in more detail:

  * [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 10 _by_ Marcos Lopez de Prado.

* * *

## Bet Sizing Methods¶

Functions for bet sizing are implemented based on the approaches described in
chapter 10.

### Bet Sizing From Predicted Probability¶

Assuming a machine learning algorithm has predicted a series of investment
positions, one can use the probabilities of each of these predictions to
derive the size of that specific bet.

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

### Dynamic Bet Sizes¶

Assuming one has a series of forecasted prices for a given investment product,
that forecast and the current market price and position can be used to
dynamically calculate the bet size.

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

### Strategy-Independent Bet Sizing Approaches¶

These approaches consider the number of concurrent active bets and their
sides, and sets the bet size is such a way that reserves some cash for the
possibility that the trading signal strengthens before it weakens.

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

[![Code implementation
demo](../_images/implementation_big1.png)](../_images/implementation_big1.png)

### Additional Utility Functions For Bet Sizing¶

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

* * *

## Chapter 10 Code Snippets¶

Chapter 10 of [Advances in Financial Machine
Learning](https://www.wiley.com/en-
us/Advances+in+Financial+Machine+Learning-p-9781119482086) contains a number
of Python code snippets, many of which are used to create the top level bet
sizing functions. These functions can be found in
`mlfinlab.bet_sizing.ch10_snippets.py`.

### Snippets For Bet Sizing From Probabilities¶

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

### Snippets for Dynamic Bet Sizing¶

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

[![Code implementation
demo](../_images/implementation_medium1.png)](../_images/implementation_medium1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

* * *

## Research Notebook¶

The following research notebooks can be used to better understand bet sizing.

[![Notebook demo](../_images/notebook1.png)](../_images/notebook1.png)

[![Notebook demo](../_images/notebook1.png)](../_images/notebook1.png)

* * *

## Presentation Slides¶

[![../_images/lecture51.png](../_images/lecture51.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257497)

Note

  * pg 1-9: Bet Sizing

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 5/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257497)

