# Purged and Embargo¶

Get full version of MlFinLab

  

  

This implementation is based on Chapter 7 of the book [Advances in Financial
Machine Learning](https://www.wiley.com/en-
us/Advances+in+Financial+Machine+Learning-p-9781119482086).

The purpose of performing cross validation is to reduce the probability of
over-fitting and the book recommends it as the main tool of research. There
are two innovations compared to the classical K-Fold Cross Validation
implemented in [sklearn](https://scikit-learn.org/).

  1. The first one is a process called **purging** which removes from the _training_ set those samples that are build with information that overlaps samples in the _testing_ set. More details on this in section 7.4.1, page 105.

[![purging image](../_images/purging.png)](../_images/purging.png)

Image showing the process of **purging**. Figure taken from page 107 of the
book.¶

2\. The second innovation is a process called **embargo** which removes a
number of observations from the _end_ of the test set. This further prevents
leakage where the purging process is not enough. More details on this in
section 7.4.2, page 107.

[![embargo image](../_images/embargo.png)](../_images/embargo.png)

Image showing the process of **embargo**. Figure taken from page 108 of the
book.¶

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium4.png)](../_images/implementation_medium4.png)

[![Code implementation
demo](../_images/implementation_medium4.png)](../_images/implementation_medium4.png)

* * *

## Research Notebook¶

[![Notebook demo](../_images/notebook4.png)](../_images/notebook4.png)

[![Notebook demo](../_images/notebook4.png)](../_images/notebook4.png)

* * *

## Presentation Slides¶

[![../_images/lecture_4.png](../_images/lecture_4.png)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257420)

Note

These slides are a collection of lectures so you need to do a bit of scrolling
to find the correct sections.

>   * pg 14-18: CV in Finance
>
>   * pg 30-34: Hyper-parameter Tuning with CV
>
>   * pg 122-126: Cross-Validation
>
>

  

* * *

## References¶

  * [de Prado, M.L., 2018. Advances in financial machine learning. John Wiley & Sons.](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)

  * [de Prado, M.L., 2018. Advances in Financial Machine Learning: Lecture 4/10 (seminar slides). Available at SSRN 3270269.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257420)

