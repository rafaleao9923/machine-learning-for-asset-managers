  

# Introduction to Sampling¶

Get full version of MlFinLab

  

In financial machine learning, samples are not independent. For the most part,
traditional machine learning algorithms assume that samples are IID, in the
case of financial machine learning samples are neither identically distributed
nor independent. In this section we will tackle the problem of samples
dependency.

As you will remember, we mostly label our data sets using the triple-barrier
method, as per Advances in Financial Machine Learning. Each label in a triple-
barrier event has a label index and a label end time (t1) which corresponds to
time when one of barriers were touched.

Note

**Underlying Literature**

The following sources describe this method in more detail:

  * [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086), Chapter 4 _by_ Marcos Lopez de Prado.

This module explores those ideas further and provides implementations for
researchers.

