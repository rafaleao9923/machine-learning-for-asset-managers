Note

The following implementations and documentation, closely follows the lecture
notes from Cornell University, by Marcos Lopez de Prado: [Codependence
(Presentation
Slides)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994).

# Information Theory Metrics¶

Get full version of MlFinLab

  

  

  

We can gauge the codependence from the information theory perspective. In
information theory, (Shannon’s) entropy is a measure of information
(uncertainty). As described in the [Cornell lecture slides,
p.13](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994) , entropy
is calculated as:

\\[H[X] = -\sum\limits_{x \in S_{X}}p[x]log[p[x]]\\]

Where \\(X\\) is a discrete random variable that takes a value \\(x\\) from
the set \\(S_{X}\\) with probability \\(p[x]\\) .

In short, we can say that entropy is the expectation of the amount of
information when we sample from a particular probability distribution or the
number of bits to transmit to the target. So, if there is a correspondence
between random variables, the correspondence will be reflected in entropy. For
example, if two random variables are associated, the amount of information in
the joint probability distribution of the two random variables will be less
than the sum of the information in each random variable. This is because
knowing a correspondence means knowing one random variable can reduce
uncertainty about the other random variable.

\\[H[X+Y] = H[X] + H[Y], X \bot Y\\]

This module presents two ways of measuring correspondence:

  1. Mutual Information

  2. Variation of Information

The following figure highlights how we can view the relationships of various
information measures associated with correlated variables \\(X\\) and \\(Y\\)
through the below figure. ([Cornell lecture slides,
p.24](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994))

[![Entropy Relational
Diagram](../_images/entropy_relation_diagram.png)](../_images/entropy_relation_diagram.png)

The correspondence between joint entropy, marginal entropies, conditional
entropies, mutual information and variation of information (Lopez de Prado,
2020).¶

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [Codependence (Presentation Slides)](https://ssrn.com/abstract=3512994) _by_ Marcos Lopez de Prado.

  * [Mutual information is copula entropy](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6077935) _by_ Ma, J. and Sun, Z.

  * [Low bias histogram-based estimation of mutual information for feature selection](https://www.researchgate.net/publication/257014935) _by_ Hacine-Gharbi, A., Ravier, P., Harba, R. and Mohamadi, T.

  * [A binning formula of bi-histogram for joint entropy estimation using mean square error minimization](https://www.researchgate.net/publication/320887281) _by_ Hacine-Gharbi, A. and Ravier, P.

* * *

## Mutual Information¶

According to Lopez de Prado: “**Mutual Information** is defined as the
decrease in uncertainty (or informational gain) in \\(X\\) that results from
knowing the value of \\(Y\\). Mutual information is not a metric as it doesn’t
satisfy the triangle inequality”. The properties of non-negativity and
symmetry are satisfied. Mutual information is calculated as:

\\[\begin{split}\begin{align*} I[X, Y]=& H[X] - H[X|Y]\\\ =& H[X] + H[Y] -
H[X,Y]\\\ =& \sum\limits_{x \in S_{X}} \sum\limits_{y \in
S_{Y}}p[x,y]log[\frac{p[x,y]}{p[x]p[y]}]\\\ \end{align*}\end{split}\\]

Mutual information has a grouping property:

\\[I[X, Y, Z] = I[X, Y] + I[(X, Y), Z]\\]

where \\((X, Y)\\) is a joint distribution of \\(X\\) and \\(Y\\) .

It can also be normalized using a known upper boundary:

\\[I[X, Y] \le min\\{H[X] + H[Y]\\}\\]

An alternative way of estimating the Mutual information is through using
copulas. A link between Mutual information and copula entropy was presented in
the paper by [Ma, Jian & Sun, Zengqi. (2008). Mutual information is copula
entropy](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994).

[A blog post by Gautier
Marti](https://gmarti.gitlab.io/qfin/2020/07/01/mutual-information-is-copula-
entropy.html) includes descriptions of two alternative estimators of copula
entropy:

  * First, estimate the copula (as a normalized ranking of the observations). Then apply the standard mutual information estimator on the normalized rankings of the observations.

\begin{gather*} X_{unif} = \frac{X_{ranked}}{N}\\\ Y_{unif} =
\frac{Y_{ranked}}{N}\\\ I[X, Y] = \sum\limits_{x \in S_{X_{unif}}}
\sum\limits_{y \in S_{Y_{unif}}}p[x,y]log[\frac{p[x,y]}{p[x]p[y]}]
\end{gather*}

  * First, estimate the copula (as a normalized ranking of the observations). Then and calculate the entropy of a copula. Estimator of the Mutual Information would be equal to negative copula entropy:

\begin{gather*} X_{unif} = \frac{X_{ranked}}{N}\\\ Y_{unif} =
\frac{Y_{ranked}}{N}\\\ I[X, Y] = (-1) * H[C(X, Y)] \end{gather*}

According to Gautier Marti, these two estimators have some advantages over the
standard approach:

  * First, continuous marginals (think the distribution of returns of each stock) have a potentially unbounded support making it hard to bin properly.

  * Second, the discretization process to estimate the density used to compute the entropy, may introduce biases in the mutual information estimate due to a rather difficult and arbitrary binning of the support.

Using their copula \\(C(X,Y)\\), allows to bypass the estimation of the
margins. The copula has compact support in \\([0, 1]\\), and its margins are
uniform.

Alternative Mutual Information estimators are also available in the below
function.

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium3.png)](../_images/implementation_medium3.png)

* * *

## Variation of Information¶

According to Lopez de Prado: “**Variation of Information** can be interpreted
as the uncertainty we expect in one variable if we are told the value of
another”. The variation of information is a true metric and satisfies the
axioms from the introduction.

\\[\begin{split}\begin{align*} VI[X,Y]=& H[X|Y] + H[Y|X]\\\ =& H[X] +
H[Y]-2I[X,Y]\\\ =& 2H[X,Y]-H[X]-H[Y]\\\ \end{align*}\end{split}\\]

The upper bound of Variation of information is not firm as it depends on the
sizes of the population which is problematic when comparing variations of
information across different population sizes, as described in [Cornell
lecture slides,
p.21](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994)

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium3.png)](../_images/implementation_medium3.png)

* * *

## Discretization¶

Both mutual information and variation of information are using random
variables that are discrete. To use these tools for continuous random
variables the discretization approach can be used.

For the continuous case, we can quantize the values to estimate \\(H[X]\\).
Following the [Cornell lecture slides,
p.26](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994) :

\\[\begin{split}\begin{align*} H[X] =&
\int_{\infty}^{\infty}f_{X}[x]log[f_{X}[x]]dx\\\ \: \approx&
-\sum\limits_{i=1}^{B_{X}}f_{X}[x_{i}]log[f_{X}[x_{i}]]\Delta_{x}\\\
\end{align*}\end{split}\\]

where the observed values \\(\\{x\\}\\) are divided into \\(B_{X}\\) bins of
equal size \\(\Delta_{X}\\), \\(\Delta_{X} = \frac{max\\{x\\} -
min\\{x\\}}{B_{X}}\\) , and \\(f_{X}[x_{i}]\\) is the frequency of
observations within the i-th bin.

So, the discretized estimator of entropy is:

\\[\hat{H}[X]=-\sum\limits_{i=1}^{B_{X}}\frac{N_{i}}{N}log[\frac{N_{i}}{N}]+log[\Delta_{X}]\\]

where \\(N_{i}\\) is the number of observations within the i-th bin, \\(N =
\sum_{i=1}^{B_{X}}N_{i}\\) .

From the above equations, the size of the bins should be chosen. The results
of the entropy estimation will depend on the binning. The works by [Hacine-
Gharbi et al. (2012)](https://www.researchgate.net/publication/257014935) and
[Hacine-Gharbi and Ravier
(2018)](https://www.researchgate.net/publication/320887281) present optimal
binning for marginal and joint entropy.

This optimal binning method is used in the mutual information and variation of
information functions.

### Implementation¶

[![Code implementation
demo](../_images/implementation_medium3.png)](../_images/implementation_medium3.png)

* * *

## Examples¶

The following example highlights how the various metrics behave under various
variable dependencies:

  1. Linear

  2. Squared

  3. \\(Y = abs(X)\\)

  4. Independent variables

[![Code example
demo](../_images/example_big1.png)](../_images/example_big1.png)

[![Linear Codependence](../_images/linear.png)](../_images/linear.png)

Linear¶

[![Squared Codependence](../_images/squared.png)](../_images/squared.png)

Squared¶

[![Absolute Codependence](../_images/abs.png)](../_images/abs.png)

Absolute¶

[![No Relationship](../_images/independent.png)](../_images/independent.png)

Independent¶

* * *

## Presentation Slides¶

[![../_images/codep_slides.png](../_images/codep_slides.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994)
[![../_images/codependence_slides.png](../_images/codependence_slides.png)](https://drive.google.com/file/d/1pamteuYyc06r1q-BR3VFsxwa3c7-7oeK/view)

* * *

## References¶

  * [de Prado, M.L., 2020. Codependence (Presentation Slides). Available at SSRN 3512994.](https://ssrn.com/abstract=3512994)

  * [Ma, J. and Sun, Z., 2011. Mutual information is copula entropy. Tsinghua Science & Technology, 16(1), pp.51-54.](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6077935)

  * [Hacine-Gharbi, A., Ravier, P., Harba, R. and Mohamadi, T., 2012. Low bias histogram-based estimation of mutual information for feature selection. Pattern recognition letters, 33(10), pp.1302-1308.](https://www.researchgate.net/publication/257014935)

  * [Hacine-Gharbi, A. and Ravier, P., 2018. A binning formula of bi-histogram for joint entropy estimation using mean square error minimization. Pattern Recognition Letters, 101, pp.21-28.](https://www.researchgate.net/publication/320887281)

