# Excess Over Median¶

Get full version of MlFinLab

  

  

In this method, a cross-sectional dataset of close prices of many different
stocks are used, which is converted to returns. The median return at each time
index is calculated and used as a proxy for market return. The median return
is then subtracted from each observation’s return to find the numerical excess
return over median. If desired, the numerical values can be converted to
categorical values according to the sign of the excess return. The labels can
then be used in training regression and classification models.

At time \\(t\\):

\begin{gather*} P_t = \\{p_{t,0}, p_{t,1}, \dots, p_{t,n}\\} \\\ R_t =
\\{r_{t,0}, r_{t,1}, \dots, r_{t,n}\\} \\\ m_t = median(R_t) \\\ L(R_t) =
\\{r_{t,0} - m_t, r_{t,1} - m_t, \dots, r_{t,n} - m_t\\} \end{gather*}

If categorical rather than numerical labels are desired:

\\[\begin{split}\begin{equation} \begin{split} L(r_{t,n}) = \begin{cases} -1
&\ \text{if} \ \ r_{t,n} - m_t < 0\\\ 0 &\ \text{if} \ \ r_{t,n} - m_t = 0\\\
1 &\ \text{if} \ \ r_{t,n} - m_t > 0\\\ \end{cases} \end{split}
\end{equation}\end{split}\\]

If desired, the user can specify a resampling period to apply to the price
data prior to calculating returns. The user can also lag the returns to make
them forward-looking. In the paper by Zhu et al., the authors use monthly
forward-looking labels.

[![Distribution Over
Median](../_images/distribution_over_median_monthly_forward.png)](../_images/distribution_over_median_monthly_forward.png)

Distribution of monthly forward stock returns. This is the labeling method
used in the paper by Zhu et al.¶

Note

**Underlying Literature**

The following sources elaborate extensively on the topic:

  * [The benefits of tree-based models for stock selection](https://link.springer.com/article/10.1057/jam.2012.17) _by_ Zhu, M., Philpotts, F. and Stevenson, M.

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium9.png)](../_images/implementation_medium9.png)

* * *

## Example¶

Below is an example on how to create labels of excess over median from real
data.

[![Code example
demo](../_images/example_medium7.png)](../_images/example_medium7.png)

* * *

## Research Notebook¶

The following research notebooks can be used to better understand labeling
excess over median.

[![Notebook demo](../_images/notebook9.png)](../_images/notebook9.png)

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Zhu, M., Philpotts, F. and Stevenson, M., 2012. The benefits of tree-based models for stock selection. Journal of Asset Management, 13(6), pp.437-448.](https://link.springer.com/article/10.1057/jam.2012.17)

