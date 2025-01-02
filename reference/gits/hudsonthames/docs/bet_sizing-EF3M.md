# Exact Fit using first 3 Moments (EF3M)¶

Get full version of MlFinLab

  

The EF3M algorithm was introduced in a paper by Marcos Lopez de Prado and
Matthew D. Foreman, titled [“A mixture of Gaussians approach to mathematical
portfolio oversight: the EF3M
algorithm”](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1931734).

The abstract reads: “An analogue can be made between: (a) the slow pace at
which species adapt to an environment, which often results in the emergence of
a new distinct species out of a once homogeneous genetic pool, and (b) the
slow changes that take place over time within a fund, mutating its investment
style. A fund’s track record provides a sort of genetic marker, which we can
use to identify mutations. This has motivated our use of a biometric procedure
to detect the emergence of a new investment style within a fund’s track
record. In doing so, we answer the question: “What is the probability that a
particular PM’s performance is departing from the reference distribution used
to allocate her capital?” The EF3M approach, inspired by evolutionary biology,
may help detect early stages of an evolutionary divergence in an investment
style, and trigger a decision to review a fund’s capital allocation.”

The Exact Fit of the first 3 Moments (EF3M) algorithm allows the parameters of
a mixture of Gaussian distributions to be estimated given the first 5 moments
of the mixture distribution, as well as the assumption that the mixture
distribution is composed of a number of Gaussian distributions.

A more thorough investigation into the algorithm can be found in one of our
Research Notebooks.

[![../_images/ef3m.png](../_images/ef3m.png)](../_images/ef3m.png)

Note

**Underlying Literature**

The following sources describe this method in more detail:

  * [A mixture of Gaussians approach to mathematical portfolio oversight: the EF3M algorithm](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1931734) _by_ Marcos Lopez de Prado and Matthew D. Foreman.

* * *

## M2N Implementation¶

A class for determining the means, standard deviations, and mixture proportion
of a given distribution from it’s first four or five statistical moments.

[![Code implementation
demo](../_images/implementation_big1.png)](../_images/implementation_big1.png)

## Utility Functions For Fitting Of Distribution Mixtures¶

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

[![Code implementation
demo](../_images/implementation_small1.png)](../_images/implementation_small1.png)

* * *

## Research Notebook¶

The following research notebooks can be used to better understand bet sizing.

[![Notebook demo](../_images/notebook1.png)](../_images/notebook1.png)

Chapter 10 refers to Advances in Financial Machine Learning.

[![Notebook demo](../_images/notebook1.png)](../_images/notebook1.png)

* * *

## Presentation Slides¶

[![../_images/ef3m_slides.png](../_images/ef3m_slides.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2172468)

* * *

## References¶

  * [de Prado, M.L, 2012. Portfolio Oversight: An Evolutionary Approach. Available at SSRN 2172468.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2172468)

  * [de Prado, M.L. and Foreman, M.D., 2014. A mixture of Gaussians approach to mathematical portfolio oversight: The EF3M algorithm. Quantitative Finance, 14(5), pp.913-930.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1931734)

