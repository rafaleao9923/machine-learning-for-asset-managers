Note

The following implementation and documentation closely follow the work of Dr.
Gautier Marti: [CorrGAN: Sampling Realistic Financial Correlation Matrices
using Generative Adversarial Networks](https://arxiv.org/pdf/1910.09504.pdf).

Warning

In order to use this module, you should additionally install _TensorFlow_ For
more details, visit our [MlFinLab installation
guide](../getting_started/installation.html#getting-started-installation).

# CorrGAN¶

Get full version of MlFinLab

  

  

  

Dr. Gautier Marti proposed a novel approach for sampling realistic financial
correlation matrices. He used a generative adversarial network (a GAN, named
CorrGAN) to recover most of the known “stylized facts” about empirical
correlation matrices based on asset returns.

It was trained on approximately 10,000 empirical correlation matrices
estimated on S&P 500 returns sorted by a permutation induced by a hierarchical
clustering algorithm.

[![Empirical vs Generated Correlation
Matrices](../_images/sample_corrmat.png)](../_images/sample_corrmat.png)

(Left) Empirical correlation matrix estimated on stocks returns; (Right) GAN-
generated correlation matrix. (Courtesy of
[marti.ai](https://marti.ai/ml/2019/10/13/tf-dcgan-financial-correlation-
matrices.html))¶

Gautier Marti found that previous methods for generating realistic correlation
matrices were lacking. Other authors found as well that “there is no algorithm
available for the generation of reasonably random financial correlation
matrices with the Perron-Frobenius property. […] we expect the task of finding
such correlation matrices to be highly complex”

The Perron-Frobenius property is one of many “stylized facts” that financial
correlation matrices exhibit and it is difficult to reproduce with previous
methods.

Being able to generate any number of realistic correlation matrices is a game
changer for these reasons.

CorrGAN generates correlation matrices that have many “stylized facts” seen in
empirical correlation matrices. The stylized facts CorrGAN recovered are:

  1. Distribution of pairwise correlations is significantly shifted to the positive.

  2. Eigenvalues follow the Marchenko-Pastur distribution, but for a very large first eigenvalue (the market).

  3. Eigenvalues follow the Marchenko-Pastur distribution, but for a couple of other large eigenvalues (industries).

  4. Perron-Frobenius property (first eigenvector has positive entries).

  5. Hierarchical structure of correlations.

  6. Scale-free property of the corresponding Minimum Spanning Tree (MST).

* * *

## Implementation¶

[![Code implementation
demo](../_images/implementation_medium5.png)](../_images/implementation_medium5.png)

* * *

## Example¶

Note

Due to the CorrGAN trained models being too large to be included in the
mlfinlab package (> 100 MB). We included them as a downloadable package
[here](https://drive.google.com/uc?id=1aKY_ed7rjQVJnMxktKCU-
YisCaS3a47t&export=download). Extract the `corrgan_models` folder and copy it
in the `mlfinlab` folder.

Note

The higher the dimension, the longer it takes CorrGAN to generate a sample.
For more information refer to the research notebook.

[![Code example
demo](../_images/example_medium3.png)](../_images/example_medium3.png)

* * *

## Research Notebook¶

The following research notebook can be used to better understand the sampled
correlation matrices.

[![Notebook demo](../_images/notebook5.png)](../_images/notebook5.png)

* * *

## Research Article¶

Read our article on the topic

  

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Marti, G., 2020, May. Corrgan: Sampling realistic financial correlation matrices using generative adversarial networks. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 8459-8463). IEEE.](https://arxiv.org/pdf/1910.09504.pdf)

