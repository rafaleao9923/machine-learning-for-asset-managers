Note

The following implementations and documentation closely follow the work of
Gautier Marti: [Some contributions to the clustering of financial time series
and applications to credit default
swaps](https://www.researchgate.net/publication/322714557).

# Copula-Based Metrics¶

Get full version of MlFinLab

  

  

  

The work mentioned above introduces a new approach of representing the random
variables that splits apart dependency and distribution without losing any
information. It also contains a distance metric between two financial time
series based on a novel approach.

According to the author’s classification:

“Many statistical distances exist to measure the dissimilarity of two random
variables, and therefore two i.i.d. random processes. Such distances can be
roughly classified in two families:

> 1\. distributional distances, […] which focus on dissimilarity between
> probability distributions and quantify divergences in marginal behaviours,
>
> 2\. dependence distances, such as the distance correlation or copula-based
> kernel dependency measures […], which focus on the joint behaviours of
> random variables, generally ignoring their distribution properties.

However, we may want to be able to discriminate random variables both on
distribution and dependence. This can be motivated, for instance, from the
study of financial assets returns: are two perfectly correlated random
variables (assets returns), but one being normally distributed and the other
one following a heavy-tailed distribution, similar? From risk perspective, the
answer is no […], hence the propounded distance of this article”.

Tip

Read the original work to understand the motivation behind creating the novel
technique deeper and check the reference papers that prove the above
statements.

* * *

## Spearman’s Rho¶

Following the work of Marti:

“[The Pearson correlation coefficient] suffers from several drawbacks: \- it
only measures linear relationship between two variables; \- it is not robust
to noise \- it may be undefined if the distribution of one of these variables
have infinite second moment.

More robust correlation coefficients are copula-based dependence measures such
as Spearman’s rho:

\\[\begin{split}\rho_{S}(X, Y) &= 12 E[F_{X}(X), F_{Y}(Y)] - 3 \\\ &=
\rho(F_{X}(X), F_{Y}(Y))\end{split}\\]

and its statistical estimate:

\\[\hat{\rho}_{S}(X, Y) = 1 - \frac{6}{T(T^2-1)}\sum_{t=1}^{T}(X^{(t)}-
Y^{(t)})^2\\]

where \\(X\\) and \\(Y\\) are univariate random variables, \\(F_{X}(X)\\) is
the cumulative distribution function of \\(X\\) , \\(X^{(t)}\\) is the \\(t\\)
-th sorted observation of \\(X\\) , and \\(T\\) is the total number of
observations”.

Our method is a wrapper for the scipy spearmanr function. For more details
about the function and its parameters, please visit [scipy
documentation](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.spearmanr.html).

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium3.png)](../_images/implementation_medium3.png)

* * *

## Generic Parametric Representation (GPR) distance¶

Theoretically, Marty defines the distance \\(d_{\Theta}\\) between two random
variables as:

” Let \\(\theta \in [0, 1]\\) . Let \\((X, Y) \in \nu^{2}\\) , where \\(\nu\\)
is the space of all continuous real-valued random variables. Let \\(G =
(G_{X}, G_{Y})\\) , where \\(G_{X}\\) and \\(G_{Y}\\) are respectively \\(X\\)
and \\(Y\\) marginal cdfs. We define the following distance

\\[d_{\Theta}^{2}(X, Y) = \Theta d_{1}^{2}(G_{X}(X), G_{Y}(Y)) + (1 - \Theta)
d_{0}^{2}(G_{X}, G_{Y})\\]

where

\\[d_{1}^{2}(G_{X}(X), G_{Y}(Y)) = 3 \mathbb{E}[|G_{X}(X) - G_{Y}(Y)|^{2}]\\]

and

\\[d_{0}^{2}(G_{X}, G_{Y}) = \frac{1}{2} \int_{R} (\sqrt{\frac{d G_{X}}{d
\lambda}} - \sqrt{\frac{d G_{Y}}{d \lambda}})^{2} d \lambda "\\]

For two Gaussian random variables, the distance \\(d_{\Theta}\\) is therefore
defined by Marti as:

” Let \\((X, Y)\\) be a bivariate Gaussian vector, with \\(X \sim
\mathcal{N}(\mu_{X}, \sigma_{X}^{2})\\) , \\(Y \sim \mathcal{N}(\mu_{Y},
\sigma_{Y}^{2})\\) and \\(\rho (X,Y)\\) . We obtain,

\\[d_{\Theta}^{2}(X, Y) = \Theta \frac{1 - \rho_{S}}{2} + (1 - \Theta) (1 -
\sqrt{\frac{2 \sigma_{X} \sigma_{Y}}{\sigma_{X}^{2} + \sigma_{Y}^{2}}} e^{ -
\frac{1}{4} \frac{(\mu_{X} - \mu_{Y})^{2}}{\sigma_{X}^{2} + \sigma_{Y}^{2}}})
"\\]

The use of this distance is referenced as the generic parametric
representation (GPR) approach.

From the paper:

“GPR distance is a fast and good proxy for distance \\(d_{\Theta}\\) when the
first two moments \\(\mu\\) and \\({\sigma}\\) predominate. Nonetheless, for
datasets which contain heavy-tailed distributions, GPR fails to capture this
information”.

Tip

The process of deriving this definition as well as a proof that
\\(d_{\Theta}\\) is a metric is present in the work: [Some contributions to
the clustering of financial time series and applications to credit default
swaps](https://www.researchgate.net/publication/322714557).

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium3.png)](../_images/implementation_medium3.png)

* * *

## Generic Non-Parametric Representation (GNPR) distance¶

The statistical estimate of the distance \\(\tilde{d}_{\Theta}\\) working on
realizations of the i.i.d. random variables is defined by the author as:

” Let \\((X^{t})_{t=1}^{T}\\) and \\((Y^{t})_{t=1}^{T}\\) be \\(T\\)
realizations of real-valued random variables \\(X, Y \in \nu\\) respectively.
An empirical distance between realizations of random variables can be defined
by

\\[\tilde{d}_{\Theta}^{2}((X^{t})_{t=1}^{T}, (Y^{t})_{t=1}^{T})
\stackrel{\text{a.s.}}{=} \Theta \tilde{d}_{1}^{2} + (1 - \Theta)
\tilde{d}_{0}^{2}\\]

where

\\[\tilde{d}_{1}^{2} = \frac{3}{T(T^{2} - 1)} \sum_{t = 1}^{T} (X^{(t)} -
Y^{(t)}) ^ {2}\\]

and

\\[\tilde{d}_{0}^{2} = \frac{1}{2} \sum_{k = - \infty}^{+ \infty}
(\sqrt{g_{X}^{h}(hk)} - \sqrt{g_{Y}^{h}(hk)})^{2}\\]

\\(h\\) being here a suitable bandwidth, and \\(g_{X}^{h}(x) = \frac{1}{T}
\sum_{t = 1}^{T} \mathbf{1}(\lfloor \frac{x}{h} \rfloor h \le X^{t} < (\lfloor
\frac{x}{h} \rfloor + 1)h)\\) being a density histogram estimating dpf
\\(g_{X}\\) from \\((X^{t})_{t=1}^{T}\\) , \\(T\\) realization of a random
variable \\(X \in \nu\\) “.

The use of this distance is referenced as the generic non-parametric
representation (GNPR) approach.

As written in the paper:

” To use effectively \\(d_{\Theta}\\) and its statistical estimate, it boils
down to select a particular value for \\(\Theta\\) . We suggest here an
exploratory approach where one can test

>   1. distribution information (θ = 0),
>
>   2. dependence information (θ = 1), and
>
>   3. a mix of both information (θ = 0,5).
>
>

Ideally, \\(\Theta\\) should reflect the balance of dependence and
distribution information in the data. In a supervised setting, one could
select an estimate \\(\hat{\Theta}\\) of the right balance \\(\Theta^{*}\\)
optimizing some loss function by techniques such as cross-validation. Yet, the
lack of a clear loss function makes the estimation of \\(\Theta^{*}\\)
difficult in an unsupervised setting”.

Note

The implementation of GNPR in the MlFinLab package was adjusted so that
\\(\tilde{d}_{0}^{2}\\) (dependence information distance) is being calculated
using the 1D Optimal Transport Distance following the example in the [POT
package
documentation](https://pythonot.github.io/auto_examples/plot_OT_1D.html#sphx-
glr-auto-examples-plot-ot-1d-py). This solution was proposed by Marti.

Distributions of random variables are approximated using histograms with a
given number of bins as input.

Optimal Transport Distance is then obtained from the Optimal Transportation
Matrix (OTM) using the Loss Matrix (M) as shown in [Optimal Transport blog
post by Marti](https://gmarti.gitlab.io/qfin/2020/06/25/copula-optimal-
transport-dependence.html):

\\[\tilde{d}_{0}^{2} = tr (OT^{T} * M)\\]

where \\(tr( \cdot )\\) is trace of a matrix and \\(\cdot^{T}\\) is a
transposed matrix.

This approach solves the issue of defining support for underlying
distributions and choosing a number of bins.

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium3.png)](../_images/implementation_medium3.png)

* * *

## Examples¶

The following example shows how the above functions can be used:

[![Code example
demo](../_images/example_medium2.png)](../_images/example_medium2.png)

* * *

## Research Notebook¶

The following research notebook can be used to better understand the
codependence metrics described above.

[![Notebook demo](../_images/notebook3.png)](../_images/notebook3.png)

* * *

## Presentation Slides¶

[![../_images/codependence_slides.png](../_images/codependence_slides.png)](https://drive.google.com/file/d/1pamteuYyc06r1q-BR3VFsxwa3c7-7oeK/view)

* * *

## References¶

  * [Marti, G., 2017. Some contributions to the clustering of financial time series and applications to credit default swaps (Doctoral dissertation, Université Paris-Saclay (ComUE)).](https://www.researchgate.net/publication/322714557)

