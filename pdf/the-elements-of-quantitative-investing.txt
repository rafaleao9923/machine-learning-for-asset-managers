This version: August 9, 2024.Please read the chapters carefully and send comments and correc-tions to the author. I prefer that you send annotated copy of the
pdf. Second best: quote part of the paragraph where the correctionis to be made. Include the date of the draft you are review. Anycontribution will be acknowledged in the nal copy.
Email:paleologo@gmail.com
THE ELEMENTSOF QUANTITATIVE INVESTING



# THE ELEMENTSOF QUANTITATIVE INVESTING

# (August 9, 2024)

## Giuseppe A. Paleologo

# LOGO


CopyrightPublished by John Wiley & Sons, Inc., Hoboken, New Jersey.Published simultaneously in Canada. c<provide-copyright-year> by John Wiley & Sons, Inc. All rights reserved.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in anyformor by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except aspermitted under Section 107 or 108 of the 1976 United States Copyright Act, without either the prior
written permission of the Publisher, or authorization through payment of the appropriate per-copyfee tothe Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers, MA 01923, (978) 750-8400,fax (978) 646-8600, or on the web at [http://www.copyright.com.](http://www.copyright.com.) Requests to the Publisher for permission
shouldbe addressed to the Permissions Department, John Wiley & Sons, Inc., 111 River Street, Hoboken,NJ07030, (201) 748-6011, fax (201) 748-6008.
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best eortsinpreparing this book, they make no representations or warranties with respect to the accuracy orcompleteness of the contents of this book and specically disclaim any implied warranties of
merchantability or tness for a particular purpose. No warranty may be created or extended by salesrepresentatives or written sales materials. The advice and strategies contained herin may not besuitable for your situation. You should consult with a professional where appropriate. Neither thepublisher nor author shall be liable for any loss of prot or any other commercial damages, including
but not limited to special, incidental, consequential, or other damages.For general information on our other products and services please contact our Customer CareDepartment with the U.S. at 877-762-2974, outside the U.S. at 317-572-3993 or fax 317-572-4002.
Wiley also publishes its books in a variety of electronic formats. Some content that appears in print,however, may not be available in electronic format.Library of Congress Cataloging-in-Publication Data:
Title, etcPrinted in the United States of America.10 9 8 7 6 5 4 3 2 1


To Tofu, Again

v


vi


# Contents

## IntroductionPrerequisitesWhat Are the Questions?: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : : xviixxixx

## OrganizationAcknowledgments1 The Map and the Territory: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : xxiixxv 5

## 1.11.21.3 The SecuritiesModes of ExchangeWho Are the Market Participants?: : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : 1197

## 1.4 Where Do Excess Returns Come From?1.3.11.3.2 The Sell SideThe Buy Side: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : :^151911

## 1.52 Returns: Properties and ModelsThe Elements of Quantitative Investing : : : : : : : : : : : : : : 2923

2.1 Returns2.1.12.1.2: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :DenitionsExcess Returns: : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : (^303031)
2.1.32.1.4 Log ReturnsEstimating Prices and Returns: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : (^3234)

## vii


## viii








- 2.2 Conditional Heteroscedastic Models (CHM)2.1.52.2.1 Stylized FactsGARCH(1, 1) and Return Stylized Facts: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : :: : : : : : :
   - 2.2.22.2.32.2.4 ??Realized VolatilityGARCH as random recursive equationsGARCH(1, 1) Estimation: : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : :: : : : : : :
- 2.3 State-Space Estimation of Variance2.2.52.3.1 Combining CHM and Realized VolatilityMuth's Original Model: EWMA: : : : : : : : : : : : : : : :: : : : : : : : : : : :: : : : : : :
- 2.4 ?Appendix2.3.22.4.1 ?The Kalman Filter: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :The Harvey-Shephard Model: : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : :
- 2.5 Exercises2.4.2 : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :Kalman Filter Examples : : : : : : : : : : : : : : : :
- 3 Linear Models of Returns3.13.2 Factor ModelsInterpretations of Factor Models: : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : :
   - 3.2.13.2.23.2.3 Graphical ModelSuperposition of EectsSingle-Asset Product: : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : :
- 3.33.4 Alpha Spanned and Alpha OrthogonalTransformations3.4.1 Rotations: : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : :
- 3.5 Applications3.4.23.4.3 ProjectionsPush-Outs: : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : :
   - 3.5.13.5.23.5.3 Performance AttributionRisk Management: Forecast and DecompositionPortfolio Management : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : :: :
- 3.63.7 Factor Models Types?Appendix3.5.4 Alpha Research: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : :
   - 3.7.13.7.23.7.3 Linear RegressionLinear Regression DecompositionThe Frisch-Waugh-Lovell Theorem: : : : : : : : : : : : : : : : : : : :: : : : : : : : : : :: : : : : : : : : :
- 3.8 Exercises3.7.4 : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :The Singular Value Decomposition : : : : : : : : : :
- 4 Evaluating Excess Returns4.14.2 Backtesting Best PracticesThe Backtesting Protocol : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : :
- 4.3 The Rademacher Anti-Serum4.2.14.3.1 Cross-Validation and Walk ForwardSetup : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : :: : : : : : : : : :
- 4.4 ?Appendix4.3.24.4.1 Main result and InterpretationProofs for RAS: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : :
- 5 Evaluating Risk5.1 Evaluating The Covariance Matrix5.1.1 Robust Loss Functions for Volatility Estimation: : : : : : : : : : : : : : : : :: : :
- 5.2 Evaluating the Precision Matrix5.1.25.2.1 Application to Multivariate ReturnsMinimum-Variance Portfolios: : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : :: : : : : : : : : :
- 5.3 Ancillary Tests5.2.25.3.1 Mahalanobis DistanceModel Turnover: : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : :
   - 5.3.25.3.3 Testing BetasCoecient of Determination?: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : :
- 6 Fundamental Factor Models6.1 The Inputs and the Process6.1.1 The Inputs : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : :
- 6.2 Cross-Sectional Regression6.1.26.2.1 The ProcessRank-Decient Loadings Matrices: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : :
- 6.3 Estimating The Factor Covariance Matrix6.2.26.3.1 ?Factor Covariance Matrix ShrinkageConditions for Constrained Identication: : : : : : : : : : : : :: : : : : : : : :: : : : : :
   - 6.3.26.3.36.3.4 Dynamic Conditional CorrelationShort-Term Factor UpdatingCorrecting for Autocorrelation in Factor Returns: : : : : : : : : : : : : :: : : : : : : : : : :: :
- 6.4 Estimating the Idiosyncratic Covariance Matrix6.4.16.4.2 Bootstrapping the Idiosyncratic Covariance MatrixExponential Weighting : : : : : : : : : : : : : : : : :: : : : : : : : : ::
   - 6.4.36.4.46.4.5 Visual InspectionShort-Term Idio UpdateO-Diagonal Clustering: : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : :
- 6.56.6 Winsorization of ReturnsSelecting Factors: the Large Number of Predictor Case6.4.6 Idiosyncratic Covariance Matrix Shrinkage: : : : : : : : : : : : : : : : : : : : : : :: : : : : :: : : : :
- 6.7 ?Advanced Model Topics6.7.16.7.2 Linking ModelsCurrency Rebasing: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : :
- 6.86.9 A Tour of FactorsFurther Reading: : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : : : :
- 7 Statistical Factor Models7.1 Statistical Models: The Basics7.1.1 Best Low-Rank Approximation and PCA: : : : : : : : : : : : : : : : : : :: : : : : : :
- 7.2 Beyond the Basics7.1.27.1.3 Maximum Likelihood Estimation and PCACross-Sectional and Time-Series Regressions via SVD: : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : :
   - 7.2.17.2.2 The Spiked Covariance ModelSpectral Limit Behavior of the Spiked CovarianceModel : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : :
   - 7.2.37.2.47.2.5 Optimal Shrinkage of EigenvaluesEigenvalues: Experiments Vs. TheoryChoosing the Number of Factors : : : : : : : : : : :: : : : : : : : : : :: : : : : : : : :
- 7.3 Real-Life Stylized Behavior of PCA7.3.17.3.2 Concentration of EigenvaluesControlling the Turnover of Eigenvectors: : : : : : : : : : : : : : : : :: : : : : : : : : : : : :: : : : : : :
- 7.4 Interpreting Principal Components7.4.17.4.2 The Clustering ViewThe Regression View: : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : :
- 7.5 Statistical Model Estimation in Practice7.5.17.5.2 Weighted and Two-Stage PCAImplementing Statistical Models in Production: : : : : : : : : : : : : :: : : : : : : : : : : :: : :
- 7.67.7 Further ReadingExercises : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : : : : :
- 8 Portfolio Management: The Basics8.18.2 Why Mean-Variance Optimization?Mean-Variance Optimal Portfolios : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : :
- 8.3 Trading in Factor Space8.3.18.3.2 Factor-Mimicking PortfoliosAdding, Estimating, and Trading a New Factor: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : :: : :
- 8.4 Trading in Idio Space8.3.3 Factor Portfolios from Sorts: : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : :
- 8.58.6 Drivers of Information Ratio: Information Coecient and Diver-sicationInvestment Performance Metrics: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : :
   - 8.6.18.6.28.6.3 Expected ReturnVolatilitySharpe Ratio: : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : :
- 8.7 ?Appendix8.6.48.7.1 CapacityConvex Optimization: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : :
   - 8.7.28.7.38.7.4 DualityLocal AnalysisSolutions to Specic Optimization Problems: : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : :: : : : :
   - 8.7.58.7.6 Optimality of FMPsSingle-Factor Covariance Matrix Updating: : : : : : : : : : : : : : : : : : :: : : : : :
- 9 Beyond Simple Mean-Variance9.19.2 Shortcomings of Nave MVOConstraints and Modied Objectives: : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : :
   - 9.2.19.2.29.2.3 Types of ConstraintsDo Constraints Improve or Worsen Performance?Constraints as Penalties: : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : :: :
- 9.3 How Does Estimation Error Aect Sharpe Ratio?9.3.19.3.2 The Impact of Alpha ErrorThe Impact of Risk Error: : : : : : : : : : : : : : : :: : : : : : : : : : : : : : :: : : : : : : :
- 9.49.5 Trading Sharpe For Capacity?Appendix9.5.1 Theorems on Sharpe Eciency Loss: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : :: : : : : : : : :
- 10 Market-Impact-Aware Portfolio Management10.1 Market Impact10.1.1 Temporary Market Impact: : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : :
- 10.2 Multiperiod Optimization10.3 Baldacci-Benveniste-Ritter10.3.1 Comparison to Single-Period Optimization: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : :: : : : : :
   - 10.3.2 The No-Market-Impact Limit10.3.3 Optimal Liquidation10.3.4 Deterministic Alpha: : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : :
   - 10.3.5 AR(1) Signal10.3.6 Mixing Signals10.3.7 Essential Statistics for AR(1) Processes: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : :: : : : : : :
- 10.4 Further Reading11 Hedging : : : : : : : : : : : : : : : : : : : : : : : : : : : :
- 11.1 Toy Story11.2 Factor Hedging11.2.1 The General Case: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : :
- 11.3 Hedging Tradable Factors with Time-Series Betas11.4 Factor-Mimicking Portfolios of Time Series : : : : : : : : : : :: : : : : : : :
- 11.512 Dynamic Risk Allocation?Appendix : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :
- 12.1 The Kelly Criterion12.2 Mathematical properties12.3 The Fractional Kelly Strategy: : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : : :
- 12.4 Fractional Kelly and Drawdown Control13 Ex Post Performance Attribution : : : : : : : : : : : : : :
- 13.1 Performance Attribution: The Basics13.2 Performance Attribution with Errors13.2.1 Two Paradoxes: : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : :
- 13.3 Maximal Performance Attribution13.2.2 Estimating Attribution Errors13.2.3 Paradox Resolution : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : :: : : : : : : : : : : : :
- 13.4 Selection vs. Sizing Attribution13.4.1 Connection to the Fundamental Law of Active Man-agement: : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : : : : : : : : : : : :
- 13.5 Appendix13.4.2 Long-Short Performance Attribution13.5.1 Proof of the Selection vs. Sizing Decomposition? : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :: : : : : : : : :: :
- IndexIndex



# Introduction

## This book originates from notes I wrote for two university courses. The rst isORIE5256 - Topics in Risk Management and Portfolio Construction, a courseoered in the program for M.S. in Financial Engineering at Cornell Univer-

## When I set out to write this booklet, my objective was to write the quantitativesity. The second is MATH-GA 2708.001 - Algorithmic Trading & QuantitativeStrategies, oered in the Mathematics Department at New York University.

## introduction I had wanted to read at the beginning of my journey in nance.Given the scope and goals of quantitative investing, it is only possible to covera small fraction of it in a course, or even in a book. To address this problem, I

## made three choices.First and most important, I aim for synthesis. A book is, rst of all, a

## knowledge lter. In the preface to his classic [Kelley, 1955], Kelley wrote thathe wanted to title his book \What Every Young Analyst Should Know"; thatbook was barely three hundred pages long. It still feels fresh and necessary

## today. In order to keep my book of manageable length, my working principlehas been to focus on real-world problems and then use thethat allow me to address the problem at hand. A recurrent theme in the booksimplesttechniques

## is that almost everything in it is either linear or quadratic. In the process ofwriting, I have ruthlessly eliminated topics of secondary importance, materialthat was too hard for the payo that it gave the readers, and also topics or

## ideas that are not suciently well-formed, or too experimental. Even if youxvii


choose not to read my book, I implore you to internalize the following lesson,learned by practitioners through sweat and tears:thousands and thousands of theory papers, in love with technical virtuosity buttheory is cheap. There are
oblivious of reality. Do not fall into temptation; by applications be driven.Secondly, I consider risk management and portfolio management as in-^1.
trinsically connected. Asset return modeling, volatility estimation, portfoliooptimization,example, hedging belongs to risk and portfolio optimization, and analysis ofex anteandex postperformance analytics are all linked. For
performance feeds back into portfolio construction. Connectedness of topics isa good thing.
with more standard econometric results. The past ten years have witnessed anexplosion of research around high-dimensional estimation problems, specicallyThird, I occasionally integrate some tools from the eld of statistical learning
the estimation of high-dimensional covariance matrices. The emphasis in manyof these contributions is on prediction (and, correspondingly, less interest innull hypothesis testing), on nite-sample bounds, and on 'pn' use cases.

the six values that Italo Calvino [Calvino, 1999] hoped to preserve in thecurrent millennium: Lightness, Quickness, Exactitude, Visibility, Multiplicity,The style of the book is also, I hope, a bit dierent. I have kept in mind
and Consistency. My aversion to advanced mathematics notwithstanding, Imust warn the reader that the book is not easy. During my lectures, I haveinduced more than one student into a comatose stupor. Afterwards, a few

(^1) References to \By Demons be Driven" by Pantera and to Warcraft 3 are intentional.xviii


Figure 1:students left nance altogether and successfully pursued careers in classicalPunk fanzineSideburn#1, page 2 (1977), by Tony Moon.
ballet. Another student keeps sending me postcards from Ibiza. A handfulhave become portfolio managers at hedge funds and risk managers. Yet, it isthe easiest book I could write for the task at hand, and it is written in the
friendliestwrong message|if I claimed that the problems I present are now settled, andthat the book is the last word on the subject. On the contrary, you and I arestyle I am capable of. Also, I would be lying|and conveying the
1970]: a spirit of openness and curiosity, even when facing advanced topics. Iin this book together, and together we shall keep a beginner's mind [Suzuki,will point out the limits of my theories and the open problems for you to work
on. If you are old enough to have lived in the Seventies and liked punk music,you may remember a cyclostyled zine (Figure 1). On its second page it showedxix


three power chords; below them, a command: \NOW FORM A BAND." Maythis book be your eld guide to being a punk quantitative researcher. It will bea life well lived.

PrerequisitesThe book should be accessible to a beginning graduate or advanced undergrad-uate student in Physics, Mathematics, Statistics, or Engineering. This means
having a working relationship, and if possible, a romantic one, with advancedlinear algebra, probability theory, and statistics. Even more important is to havea deep interest in quantitative modeling of real-life phenomena. Many readers
will be either members of a systematic trading team, or work as quantitativeresearchers in the central team of a hedge fund or a quantitative asset manager.The book's material is organized in such a way that you do not need to
go through mathematical proofs. You can rely only on informal statements ofmathematical results. To understand the main points of the chapters that willsuce. The appendices at the end of the chapters contain rigorous statements,
proofs, and background material. If you plan on actively doing research, youshould denitely go through the appendix.Even if you read only the main body, you should be used to thinking
in mathematical models. The Book of Nature is written in a mathematicallanguage 2 2. Be comfortable with:
to our gaze. But the book cannot be understood unless one rst learns to comprehendthe language and read the letters in which it is composed. It is written in the language ofmathematics, and its characters are triangles, circles, and other geometric gures without\Philosophy is written in this grand book, the universe, which stands continually open
which it is humanly impossible to understand a single word of it; without these, one wandersxx


```
 Working with linear algebra, at least at the level of Strang [2019] andTrefethen and Bau [1997].Some applied probability, at the level of Ross [2023]. Exposure to some simple
control theory and state space models helps. You can come to this fromEconometrics [Shumway and Stoer, 2011, Harvey, 1990], Control Theory[Simon, 2006], or Statistics [Hyndman et al., 2008].
 Some optimization modeling is a plus. The rst few chapters of Boyd andVandenberghe [2004] would be ideal. However, I cover the basic theory in anappendix.
```
What Are the Questions?I have selected the minimal set the topics that address the essential questionsin the life of a quantitative researcher.

1. How do model returns in a way that allows me to generate risk and returnforecasts?(a) How do I model multivariate returns?
    (b)(c) How do I incorporate asset-specic data in my model?And how do I test these models, either developed by me or bycommercial vendors?
    (d) How do I describe and forecast risk?(e) What are excess returns?(f)How do I convert risk appetite and expected returns into a portfolio?
about in a dark labyrinth" Galilei [1623].
xxi


2. How do I backtest alpha?3. How do I account for transaction costs in portfolio management?4. How do I represent the information in my signals?
5. How do I trade a billion signals?6. How do I distinguish skill from luck?
OrganizationLike Caesar's Gaul, this book is divided into three parts. The rst part focuseson returns modeling. I cover the basics of GARCH early on because they are
needed for factor modeling; and then I cover factor models because they are nec-essary for everything. I have separate chapters for fundamental and statisticalmodels. These topics are covered in depth, and both the treatment and some of
the modeling approaches are novel. Finally, I cover data snooping/backtestingas a separate chapter, since it is an essential element of return models.

(MVO). I emphasize the geometric intuition behind much of mean-varianceysis, bothThe second part is devoted to portfolio construction and performance anal-ex anteandex post. The focus is on mean-variance optimization
optimization. Rotations, projections, and angles are prevalent throughout. Thisallows for a synthetic, elegant characterization of performance and for conciseproofs. The statistics of the Sharpe Ratio are covered in some detail. The
decomposition of payos into timing components, factor and idiosyncratic PnL,and stock selection versus sizing of positions is rigorously demonstrated. Modelerror plays an important role in this part. If an optimization problem is Othello,
then model error must be Iago: it can drive the optimization insane. Unlike inxxii


Shakespeare's tragedies, we can try to rewrite the ending and save Desdemonaat last.
ity allocation and performance attribution. These are essential components ofthe investment process, and belong in a book with the word \Elements" in itsThe third part is the shortest. It contains results about intertemporal volatil-
title.Each chapter is organized like an onion. The rst sections convey the
essential ideas using simple quantitative methods and are aimed at a broadaudience. Sections marked with a star \skipped on a rst reading. Proofs of new results or basic technical material?" are more advanced and can be
are relegated to the appendices at the end of the chapters. The goal is not todisrupt the 
ow of learning. As mentioned at the beginning of this preface, thecontent of this book was taught rst, written later. It is meant to be read aloud
and discussed, but it should be suitable for self-study. The dependencies amongthe chapter are shown in Figure 2.
Riverdale, New YorkAugust 9, 2024 Giuseppe \gappy" A. Paleologo

xxiii


8. Basic Portfolio Management1. The Map & Territory3. Linear Models 2. Univariate Returns
9. Advanced Portfolio Management
7. Evaluating Risk 8. Fundamental Factor 9. StatisticalModelsModels Factor
Portfolio Management 10. Tcost-Aware 11. Hedging
13. Ex Post Performance Attribution6. Backtesting Excess Returns
12. Dynamic Risk Allocation
Figure 2:Chapter Dependencies.

xxiv


# Acknowledgments

## The following people have proofread, commented, discussed the content of thisbook. Some of them are old friends, some oered their help as I post earlydraft of the book online. Meeting them (usually online) has been an unforeseen

pleasure in the writing of the book, and I am grateful for their generosity andthe many corrections they sent my way. Unfortunately all the remaining errorsare the responsibility of the author (^3).

## Sandro C. AndradeJerome BenvenisteVictor Bomers

## Thomas ByrneBen ChaddhaYuyao Che

## Ruolag DengBill FalloonTom Fleming

## Jean-Francois FortinErnesto GuridiAlex Hermeneanu

Kevin Jacobs (^3) And of his cat Tofu.

## xxv


Bob JansenAmanda JimenezFredrik Jafvert
Yassine KachradJessie LiSamuel Londner
Baridhi MalakarPaul-Henri MeminFrancesco Mina
Simon MinovitskyAbhijit NaikAndrew Novotny
Adam NunesTomSiddhant PyasiO Nuallain
Damon PetersenHenrik Hiro PetterssonAlexis Plascencia
David PopovicKrutarth SatoskarTanmay Satpathy
Abishek SaxenaAshutosh Singh@systematicls(X pseudonym)
Gianmario TamagnoneHoward Zhang
xxvi


Siqi Zheng@0xfdf(X pseudonym)
G.A.P.

xxvii


xxviii



# Notation

## RRN+ Field of real numbers[0Set of natural numbers; 1 )

## x;y;:::xX;;yY;:::;::: scalarsvectorsmatrices

## xX 
0 ;+X^0 vector or matrix transposeMoore-Penrose pseudoinversecovariance matrix

## diag ([[xX]]i;xi;jxi 1 ;:::;xn) Diagonal matrix with scalarsielement of a matrix on-th element of a vectori-th row andx 1 ;:::;xj-th columnnon the main diagonal

## [[trace (XX]]i;;j X) ijTrace operator: trace (-th row of matrix-th column of matrixX XX) =Pi[X]i;i

## ei;j(t) Kroneker's delta:Dirac's delta function:vector whose elements are all ones: [i;j= 1 if(t) = 0 fori=j, 0 otherwisete 6 = 0, and]i= 1 for allR 11 i(t)dt= 1

(^1) qefixg indicator function, equal to 1 ifunit function invector whosei-th element is 1 and the others are zero:L (^2) :q(x) := 1 xis true, 0 otherwise
Ikmxkp [identity matrix of sizepe-norm, fori]j=i;j p1: (^2) Pni=1mjxijmp


kkxHkkQ 2 poperator norm for a symmetric positive denite matrixmaxx^0 QxxkHx, for a symmetric positive denite matrixk=kxk. Q. H:

bhhxAxc;;yBii largest integer that is less than, or equal to,scalar product of two vectors, i.e.scalar product of two matrices:hAx; (^0) Byi2R:= trace (x A (^0) B)
xE?(y);E (^2) (Rn) Hadamard product of two vectors and matrices: [random variablesexpectation of random variables or random vectorsandare independent xy]i:=xiyi
EEvar(^((xf)x())) expectation of a functionaverage of a vectorvariance of a random variablex:E^(xf) :=of random variablexn  1 Pixi 
Lrviid rv 1 :Rn!Rn shift operator:random variablesindependent identically distributed random variablesL 1 x:= (x 2 ;x 3 ;:::;xn;0)^0 , i.e., [L 1 ]i;j:=i;j  1
pdf=d positive deniteequality in distribution of two random variablesrv distributed according to a distribution, e.g.N(0;1)
) convergence in distributionequivalence of optimization problems: for constantsmaxx2Sf(x)maxx2S[af(x) +b] a >0,b


# Before the TradePart I


# The Map and the TerritoryChapter 1

## 1. What are the instruments we are trading?The Questions

## 2. Who are the players?3. What are the sources of excess returns?

## When considering the meaning of a word, it's often instructive to go back to itsetymology, so let's play this game. Despite being a Germanic language, EnglishThis chapter is a guide to the essential components of quantitative investing.

## adopted many words from Latin, sometimes by way of French. \Investing"comes from \Investire", which in Latin meant \to cover with a vest", or \to putin a vest". So it should be hardly surprising that two thousand years later, vests

## would become the favorite garment of hedge fund managers. In the Middle Ages,the verb took on the additional meaning \to surround, to have ownership of". Itis also possible that the modern meaning overtook the old because, in ceremonies

## in which ownership was transferred, the new owner was \invested" with a cloakand other regalia. In Italian{the direct successor to Latin{ the old meaning isgone, and \investire" only means \to receive possession of something". As for

## \quantitative", that is Latin too: \quantum", a noun denoting something that 5


can be measured, increased, and decreased. We will deal with ownership, soldand bought in units that can be measured, increased and decreased. This is,unfortunately, the whole of nance. You can own a house, a painting, a bet on
the survival of humankind, or even an idea. Each one of these investment topicsdeserves its own book, written by a competent author. In writing this book, Ihave chosen to trade o generality in favor of detail. I have covered each subject
with the goal in mind that you would have sucient information to understandit, implement it, and critique it. However, even an analytical book needs anintroduction that puts things in their proper context. In this chapter, I aim
to provide that context. You will have a broad understanding of the classes ofsecurities to which these methods apply; and of the way these securities aretraded, and by whom. This is a necessary prerequisite to explore fundamental
questions: where are excess returns coming from? What causes these tradingopportunities? Finally, I will present the essential components that make upthe analytical framework of a quantitative portfolio manager. The underlying
message is that to be successful, an investor must understand how things work.A seminal early book on investing is titled \The Intelligent Investor" [Graham,2006]. To double down on Latin, the original meaning of \intelligent" is \to
read into something", similar to \insightful" in the English language. Yoursuccess will come from reasoning about the behavior of your counterparties,the rules governing the trading of your assets, and the functioning of exchanges.
Many budding quants focus on quantitative methods. The fact is that theoryis cheap and is often not hard. What is hard is putting the right tool at theservice of the right insight.
while it lasts.Finally, this is the only chapter without mathematics. You should enjoy


We will be concerned with1.1. The Securitiesthese concepts in more detail.standardized productsthat areliquid. We explain
If you own a house, you can live in it or rent it out (your claim) and it isyours. This claim is not absolute, however. In most countries, the local orTo \own" an object is eectively to ownclaimson that object in the future.
central government may need your property for reasons of public welfare andcan require you to exchange your claim for cash at a fair price. If you own apainting, you may enjoy it in the connes of your house, but may not necessarily

(e.g., consider a zombie apocalypse scenario). Dening ownership of an \idea"own its reproduction rights. If you own a bet on the future of humanity, yourcounterparty may have someforce majeureclauses that prevent it from paying
is especially challenging and prone to be treated onthe innite and ever-changing nature of the meaning of property rights, ourcoverage is very narrow. Specically, we focus on the subset of contracts thatad hocbasis. Compared to
are standardized and liquid. We buy and sellcome in a few varieties, and their attributes are clearly dened and known toall potential buyers and sellers. Examples are:standardizedclaims. These claims
 Equities and ETFsof companies, and entitle us to receive future cash payments generated bythe economic activities of these companies.. These give us partial ownership in companies, or groups
 Futurescontingent on the state of the world at a future date, at a price determinedtoday.. These contracts deliver a physical commodity or a cash payment
 Bondsparties. An investor lends money to a borrower, in exchange for a xed. These are contracts that allow the transfer of debt claims among 7


 cash 
ow in the future (for example, periodic interest payments and a nalpayment). A bond makes this claim transferable to other lenders.Vanilla options. These are claims that depend on the future value of some
underlying asset; for example, you may receive the right (but not the obliga-tion) to buy a stock at a future, at a price determined today. The nature ofthese claims is standardized, hence the term \vanilla".
 Interest Rate Swaps (IRS)deterministic cash 
ow stream for an uncertain one, which depends on interestrates at future dates.. These contracts allow the exchange of a certain,
 Credit Default Swaps (CDS)failure of a company at a future date, in exchange for recurring xed payments.Secondly, these contracts are. These contracts insure the buyer against theliquid. For our purposes, a liquid contract is one
that can be bought and sold at large enough sizes, and at suciently short timehorizons, to enable quantitative strategies to be implemented. This means thatif we plan to buy or sell a contract, we should be able to do so without incurring
a transaction cost so high that our strategy is not economically attractiveeven for small trading sizes, and that the waiting time due to searching acounterparty should not be so long as to make the transaction economically
unattractive.Increased standardization tends to enhance liquidity by consolidating demand,The properties of standardization and liquidity are closely intertwined.
as it aggregates dispersed demand from bespoke products towards a smallerset of standardized ones. Furthermore, standardization streamlines the tradingprocess, reducing transaction costs and bolstering robustness, thereby fostering
investor trust and attracting greater participation, thus enhancing liquidity.However, the downside is that customers may sacrice the ability to trade certain 8


useful product characteristics. Determining the optimal level of customization,even at the expense of liquidity, remains an ongoing process of learning andadaptation. For instance, prior to the 2008 nancial crisis, Credit Default
Swaps (CDSs) exhibited greater variety. However, the \Big Bang" initiated bythe International Swaps and Derivatives Association (ISDA) on April 8, 2009,simplied contract terms, including standardizing coupon rates (100bps and
500bps) and introducing a standard upfront payment, which played a pivotalrole in restoring condence in this asset class [Vause, 2010].Trading and liquidity are at the core of the book. In order to better under-
stand the trading process and the nature of liquidity, we should describe insome detail how trading on-exchange and over-the-counter happens.
1.2. Modes of ExchangeAt any given time, economic agents want to buy or sell contracts. They want todo so quickly, securely, and cheaply. The three options around which trading is
currently organized are exchanges, over-the-counter, and dark pools. Exchangesare venues in which the orders of buyers and sellers are anonymized and matchedagainst each other. Orders are characterized by size, the number of contracts,
direction (buy or sell), and price. They represent requests to buy or sell a numberof contracts. The exchange records such active orders on a ledger, known as thelimit-order book (LOB), and employs a set of priority rules to match buy and
sell orders in the exchanges aptly named matching engine. In order to tradeon an exchange, one must be a member of that exchange. Membership entailsapparent benets and less-apparent responsibilities. Market participants must
maintain sound governance, risk processes, and capital structure. 9


a push toward consolidation, which reduces operating costs and gives the ownerpricing power. On the other side, technical and process innovations introduceExchanges evolve continuously due to two driving forces. On one side, there's
new competitors into the market. In the US alone, there are more than a dozenequity stock exchanges. Exchange-traded assets, such as stocks, options, andfutures (including Forex futures), are often liquid, although this condition is
neither necessary nor sucient: some exchange-traded assets are traded inminimal volumes and, therefore, are not liquid, and some very liquid productsare traded o-exchange.
In this case, the buyer or seller transacts through an institutional marketparticipant, the broker-dealer, which is connected to other broker-dealers andOther assets are not traded on exchanges, butover-the-counter (OTC).
facilitates the matching of orders. Bonds, Interest Rate Swaps, Forex currencies,Forex Futures, CDS are examples of contracts traded OTC. Some of these,like currencies, are among the world's most liquid contracts. A precondition
for liquidity is standardization. Think of a house. \The New York housingmarket" is very dierent from the stock market in that each of the 15.4 billionoutstanding Apple shares (as of July 2024) is indistinguishable from the other
and sells in a matter of seconds. In contrast, a house has many attributesthat make it unique: location, size, age, blueprint, and condition. Anothercharacteristic of liquid markets is the large number of participants. When
numerous participants are involved in a market, competing for a relativelylow number of contracts, transactions become more frequent, the necessity forbilateral bargaining diminishes. The ability of any individual participant to
in
uence the price signicantly is reduced. To illustrate, consider the housingmarket as a counterpoint: when selling a house, you typically negotiate with one


specic buyer (out of a few eligible ones), who may spend many hours searchingfor the right property and may engage in intense bargaining, sometimes to thepoint of contention, to secure the best possible price.
does not make its limit order book transparent) are additional venues thatare distinct from exchanges (although sometimes owned by them). Dark PoolsFinally,Dark Pools(a type of ATS, or Alternative Trading System, that
address the needs of certain institutional investors to execute orders withoutdisplaying their trading intentions. By design, dark pools hide order details andonly make trades details available after execution. As of 2024, approximately
16% of US shares are traded on Dark Pools.
1.3. Who Are the Market Participants?It is convention to partition traders into thefacilitates trading by providing services; the latter receives trade for their ownSell SideandBuy Side. The former
benet. Below I describe the participant types. For a more detailed description,see Harris [2003].
1.3.1. The Sell SideThe sell side comprises brokers, dealers and broker-dealers.
 Dealersopposite side of the trade; they are protable if, on average, they sell (buy) ata price higher (lower) than what they initially paid to buy (sell) the asset. The^1 fulll their clients' demand, thus providing liquidity. They take the

(^1) Ch. 13 in Harris [2003]. 11


ask pricedierence between buy and sell prices is thewith clients, they quote the buy price (the) for a contract. They are eectivelybid pricespreadmaking a market. When dealers interact) and the sell price (or, since these
quotes make transactions possible. In OTC markets, dealers are the primaryliquidity providers. The most sophisticated among such markets allow thedealers to quote prices, quantities, and other attributes continuously. For
example, xed-income products can be traded on Dealerweb or Bloomberg.In order markets or for highly bespoke products, the dealers quote on request,possibly one-sided only, for a specic quantity and with an expiration time.
The quote, or the spread if the quote is two-sided, depends on the quantity.Similarly to speculators, dealers trade on their own behalf. Like speculators,they hold a portfolio (or aninventoryof positions) and face the issue of facing
trading counterparties that may be more informed than themselves. Unlikespeculators, dealers are passive traders, in that they respond to their clients.Also, unlike speculators, dealers enjoy special regulatory status. Because
dealers observe the demand 
ow of their clients, they are informed agents,often serving the needs of informed clients. The dealers' prot originates fromthe realized spread of their trade (which is usually lower than the quoted
spread) but also from the specic information the dealer derives from theorder 
ow. One specic type of 
ow originates from retail investors (who weintroduce later in the chapter). These investors access the market indirectly
through brokers. Brokers have special arrangements to direct market orders todealers, who commit to execute them while oering certain price guaranteeson the trade.
In summary, dealers are liquidity providers, and they are compensated forservices through trading prots.


 Brokersorder from a client, together with information about the client's time andprice preferences, it searches for the most eective channel to execute it in^2 trade on behalf of their clients. When the broker receives an
accordance with these preferences. For example, a client sends a broker anorder to buy a certain number of shares of a company. The broker is a memberof all major exchanges. It splits the large order into smaller orders and routes
them to the various markets at times that meet the execution horizon ofthe client or its expected cost. Unlike dealers, brokers are intermediarieswho take no risk by holding contract positions at any given time. The
intermediation service they provide is benecial, however, and it comes withits own risks. First, brokers provide exchange access to non-member clientsand they provide OTC dealer access to non-institutional clients. Institutional
clients, too, may want to enlist a broker when interacting with dealers,since the broker anonymizes the clients. Secondly, broker intermediationsolves bilateral settlement risk: money is exchanged for contracts after the
trade occurs. Clients need to know and trust their counterparty to protectthemselves from insolvency, reneging, or non-compliance. There is a smallnumber of brokers compared to the number of traders, so that clients need
to approve (and be approved by) only by few counterparties; a reduction intime, cost, and risk. This, of course, does not eliminate counterparty risk. Ittransfers it to the brokers. The brokers manage it by vetting the clients, and
by requiring that clients deposit capital at the broker, which the broker usesin case of client insolvency. The brokers alsoof the client. In addition to these services, brokers, and especiallyclearandsettletrades on behalfprime

brokers (^2) Ch.7 in Harris [2003]., the subclass of brokers servicing hedge funds and other sophisticated


```
investors, oer their clients other services:{ Custodial servicessecurities.. Brokers ensure receipt, recording, and safekeeping of
{ Rehypothecationfor the brokers' own needs in exchange for fees or rebates. For example,brokers may use client securities as collateral for their own transaction or. Clients may allow the brokers to use their securities
```
{ lend them to other clients.Margin loansThey charge them SOFR. Brokers lend clients short-term capital to buy securities. (^3) plus a spread.
{ Location of short positionsrst, and buy them back at a later time, with the expectation that futureprices will be lower than current ones. Brokers enable these transactions. Clients may want toshortstocks, i.e., sell shares
by lending shares from a third party and making them available to theclients. The clients then sell them in the open market, buy them back at alater time and return them to the broker. After the initial sale, but before
{ the buyback, the broker invests the cash proceeds at a rate SOFR plus aspread. The client receives from the broker SOFR minus a spread.Research reports and services, as well as broker specic data. These services
{ used to be bundled in broker commissions but after the implementationof MIFID II regulation, they are now charged separately.Capital introductions, in which brokers facilitate the connection between
In summary, brokers oer diversied services, the most important of whichis to facilitate clients' transactions. They are compensated by commissions,hedge funds and potential investors.
cash loans.^3 Secured Overnight Financing Rate (SOFR) is a measure of the interest rate for overnight 14


(PFOF), which is the compensation brokers receive from market makers forinterest on cash balances, interest on lending, and payment for order 
owrouting orders to them.
Broker-Dealers, also calledin a single entity. They act both on behalf of the client and on their ownbehalf. This introduces a tension. The dealer's arm is incentivized to usedual traders, combine the previous two functions
the broker's information in trading to its advantage. Maybe the simplestaction isdemand for a security, and buys it in advance before this demand manifestsfront-running: the dealer is aware of incoming buying or selling
in the market and is re
ected in prices. To mitigate this type of behavior,regulations are in place to safeguard the interest of the client. The mostimportant law regulating brokers, dealers, and broker-dealers is the Securities
Exchange Act of 1934 (or `1934 Act').
1.3.2. The Buy SideThe buy side usually trades with the sell side. You (the reader of this book)are likely to be a member of this group, even though certain dealers face
quantitative challenges similar to yours. It is important to understand whothe actors in the buy-side drama (occasionally, tragedy) are, because you willcontinuously interact with them, and your excess returns will be the outcome
of this interaction. We could classify the buy-side actors according to severalcriteria. For example, the sub-industry to which they belong: life insurers,mutual funds, hedge funds, and so on. I opt to classify them (subjectively!)
based on the type of investing they perform. Indexersare passive investors. Their portfolios replicate the compositions


of the benchmarks, or indices, generated by data providers like MSCI, S&P,Russell, CRSP, or from exchanges like FTSE 100, TOPIX, and DeutscheBorse. These indices are updated on a quarterly or biannual basis, and
they comprise bond indices as well, like the Bloomberg Agg (until 2016owned by Barclays). Several investment vehicles track indices; mutual fundsand exchange-traded funds are the largest in terms of size. Large rms in
this group are Blackrock, Vanguard, and State Street. Indexers make up alarge and growing share of the total asset base. According to estimates byChinco and Sammon [2023], they represent over 37% of the US stock market
 capitalization as of 2020.Hedgersreducing nancial risk originating from their core businesses. For example,are rms participating in markets with the primary objective of
currency risk is faced by any rm doing business internationally. Firms suchas airlines and manufacturing companies purchase fossil fuels (gas, Brent,and West Texas Intermediate), whose price variability can be very disruptive.
Hedgers primarily participate in derivative markets: futures, swaps, andoptions. Hedgers dier from other participants that also hedge, such asdealers or hedge funds, in that hedging is the primary activity they perform.
 Institutional active managersThey run strategies that are sometimes benchmarked to commercial indicesand hope to beat them. There is some evidence of underperformance of fundsare rms investing on behalf of their clients.
serving retail investors; see S&P SPIVA report2023]. Both show that over 60% of funds underperform their benchmarksover a one-year trailing basis. The outperformance of funds over one year^4 or the Renitiv study [Glow,

is not persistent: as of January 2024, 91% of funds trail the performance (^4) https://www.spglobal.com/spdji/en/research-insights/spiva/.


```
of the S&P500 over the previous 15 years. On the other side, funds servinginstitutions seem to beat their benchmarks [Gerakos and Linnainmaa, 2021].Thetracking error is a measure of the risk they can take when diering
from their reference benchmarks. Otherwise stated, their portfolios can beexpressed as the sum of the positions in a benchmark, and of discretionarypositions of a \tracking portfolio". A large tracking error gives the funds
\index huggers," i.e., index funds in disguise.much discretion; a low one makes them close to the indices, and makes themAsset allocatorsmanage portfolios composed of securities in multiple asset
classes. Within an asset class, the portfolio closely follows a representativebenchmark. One can view asset allocators as managers of a portfolio ofasset classes. The relative weight of these asset classes in the portfolio is
```
either constant or changes slowly. Common asset classes are equities, bonds,commodities, and cash equivalentsalternative asset managers like private equity rms, venture capital, hedge (^5). In addition, asset allocators invest in
 funds, and real estate.Informed tradersThese rms are usually organized as partnerships, although a few are publicinclude primarily hedge funds and principal trading rms.
companies. They face fewer constraints than institutional managers. Whereasprincipal trading rms only have general partners (GPs, the principals)investing their own money, hedge funds also have limited partners (LPs)
short-dated treasuries, or commercial paper.who do not invest actively^5 Cash Equivalents are highly liquid assets with low returns, like bank certicates of deposit,^6. These rms pursue absolute returns (i.e., not
(on behalf of the LPs). To resolve this con
ict of interest, the SEC regulates the class ofinvestors who can be LPs (high net-worth, sophisticated investors), and gives LPs special^6 GPs in hedge funds are both principals (since they invest their own money) and agents


tracking a benchmark), which exhibit low correlation to the indices of majorasset classesand data to achieve this goal. They fulll two major functions. The rst one (^7). Informed traders invest heavily in human capital, technology,
isestimates of the true value of securities. If the security prices dier from theirestimates, they trade to exploit the mispricing. If the price is lower than theirprice discovery. By using all information available to them, they generate
estimate, they buy the security. In the process, they increase its price andbring it closer to equilibrium. Mispricing can take many forms. If the samesecurity is oered at dierent prices on dierent exchanges,arbitrageurs(a
subset of informed traders) will try to exploit the dierence; of course, thismay not be easy to do, so the dierence either persists, or disappears veryquickly due to technology investment in low-latency trading. The second
1.4; hedge funds and market makers have developed specialized strategiesrole of informed traders is liquidity provisioning. Supply and demand ofcertain assets is predictable to a certain degree. I provide examples in Section
that predict imbalances, hold (or short) securities before the liquidity needmaterializes, and meet the liquidity needs at the event. The range of possibleintervals between prediction and event can be vast { from sub-second for
 high-frequency market makers to weeks or months for hedge funds.Retail investorsinvestors made up approximately 20% of total volume; the share was slightlytrade for their own account via retail brokers. In 2020, retail
more than 10% in 2011. Several studies, across dierent national marketsand periods, have shown that retail traders are consistently unprotable
privileges within the fund.exposure; b) some hedge funds have an asymmetric exposure to the market [Agarwal andNaik, 2004]. (^7) This is not always true in practice because a) some hedge funds have an explicit market


[Barber and Odean, 2013]; retail trader 
ow is uninformed. This is one ofthe reasons why it is highly sought after by dealers, who will pay the retailbrokers for routing it to them (payment for order 
ow).
1.4. Where Do Excess Returns ComeFrom?
Now that we have introduced the main actors in the play (usually a tragedy,rarely a comedy, and occasionally a farce) of investing, we can discuss thesources of excess returns. The \excess" qualier means \in excess of portfolio
invested in risk-free assets, such as short-dated US Treasurys." This topic iscentral both to academic nancial research and to practitioners. Academicnance is primarily concerned with the question ofeciency. In the words of
Malkiel [1987]:A capital market is said to be ecient if it fully and correctly
reveals all available information in determining security prices. For-mally, the market is said to be ecient with respect to some infor-mation set,, if security prices would be unaected by revealing that
an information set,information to all participants. Moreover, eciency with respect toprots by trading on the basis of, implies that it is impossible to make economic.
\information setAn exceptionally concise denition, if there ever was one. At its core is theof the traded securities. Nowadays, this information can be obtained with". This could be, for example, the set of all historical prices


relativelyinformationis lawfully made available to the general public from: (i) Federal, state, or local^8 little eort. A dierent type of information set is publicly available (^9) , dened in the US as \any information that you reasonably believe
government records; (ii) Widely distributed media; or (iii) Disclosures to thegeneral public that are required to be made by federal, state, or local law." Aneven ner information set is the set ofallinformation available toanyinvestor.
Academic research tries to determine the validity of the statement that \securityprices would be unaected by revealing that information to all participants."Note that this does not mean thatis not helpful to predict future prices.
Indeed, there is empirical evidence that asset prices are predictable. However,the hypothesis is that current prices may not be aected. We do not trade in thedirection of returns, up to the point that the investing opportunity disappears.
This is unintuitive. Why would we not take advantage of an informativeprediction? One reason isfuture return of an asset, the uncertainty around the prediction is too high forrisk. Even if we have some information about the
us to take advantage of it. For example, say that, to the best of our knowledgeofcustodied at the broker will return a measly 2%. Does this imply that we will, we expect the US market to appreciate 8% next year, while our cash
rebalance our portfolio to 100% a market-tracking asset like SPY? Hardly. Thereason is that the standard deviation of market returns is 20%, a little toohigh for comfort. Risk, however is not the only reason. Another one isliquidity.
Indeed, the road to hell of an investor is littered with quite accurate predictionsof assets that barely trade or do not trade at all. A famous example is the 8
of good quality, accounting for corporate actions, is hard, expensive and requires skill.GRAMM-LEACH-BLILEY ACT. 9 The \relatively" here denotes a bit of sarcasm. Collecting long time series historical pricesPRIVACY OF CONSUMER FINANCIAL INFORMATION UNDER TITLE V OF THEx163.3 (w) (1).


spin-o of Palm (a now-defunct mobile device company) by 3Com (a telecomequipment maker, also defunct) in 2000. 3Com 
oated on the public market 5%of the shares of Palm, while retaining the other 95%. Right after the IPO, Palm
had a market value of $54B, while 3Com had a market capitalization of $28B.The implied value of 3Com assets was $-22B, even though the company hadno debt, $1B in cash, and positive cash 
ow. Either 3Com was dramatically
undervalued, or Palm was dramatically overvalued. An investor could havetherefore bought 3Com shares and shorted Palm for an equal amount. Theportfolio comprised of these two assets was a synthetic asset whose return
(pun intended) supply. In order to short a share, the investor must rst borrowcould be predicted. There was a problem, however. Palm shares were in shortit, at a rate decided by the lender. If quoted at all, these rates were so high
as to make the trade either unattractive or impossible. Risk and Liquidityare not the only two factors limiting the exploitation of information. We listtwo more. The rst one isfunding. Consider a scenario in which the certain
assets, or certain portfoliosdistress. We are managing a small hedge fund, which has also lost money inthis environment. Based on historical examples, we have a strong belief that^10 , have lost much of their value due to market
\deleveraging spirals". However, we do not have much capital available to postsuch assets will rebound. Such scenarios occur quite regularly, especially inas margin. In addition, we need a capital buer in order to withstand a possible
additional loss in the very short term. Funding constraints prevent us frombuying the asset, in spite of our accurate forecast.A signicant source of excess returns arises from
ow predictability. Some

agents, notably institutional investors and market makers, but not only, will (^10) As in the case of the pair 3Com-Palm, we can interpret portfolios as synthetic assets.


trade known securities on known dates. Speculators can then take advantage ofthis information by providing liquidity beforehandinstances of this is index rebalancing. Several index providers update the (^11). One of the most important
weights of their indices on predetermined dates using well-dened rules. Somesecurities are added to the index, others are removed, and nally most ofthe remaining ones have an updated weight. The term used for this process
iseective July 15, 2013. The announcement was made on July 10, 2013; butseveral investors could have forecasted the event well before that date. Theseindex reconstitution. For example, TSLA was added to the NASDAQ 100,
investors would then purchase TSLA shares and sell them at the closing auctionof July 15, 2013. The ETF, mutual funds and bespoke products that trackthe index have an obligation to buy TSLA on the close of that day, and the
resulting demand is likely to push up the stock price. The informed investorsproviding liquidity do not do so risk-free. They hold the stocks until the eectivedate, and over these days are exposed to the risk that TSLA may suer from
company-specic or industry-specic losses. Moreover, there is the remote riskthat the reconstitution be cancelled or postponed. The size of passive investingis large and its estimate ranges from 17.5% [Novick, 2017] to 38% [Chinco and
Sammon, 2023] of total assets under management. The buyer of index productsbears the indirect cost of such rebalancing [Li, 2021]. This is just one prominentexample of predictable 
ows, but several others exist, usually smaller in size,
but also not as widely known as index rebalancing. Their common featureis the existence of institutional or procedural constraints (sometimes driven 11
selling a security based on a demand forecast of said security; but in the latter case, theforecast relies onNote that this is not the same asnon-publicinformation.front running. The latter also consists of buying or


by internal processes, other times by regulatory requirements) that introducepredictability in the demand of securities.Finally, we consider a last source of excess returns:informational advantage.
This means that the investors do not only dier by their risk attitude, theirtolerance to illiquity, their funding level, but also by their information sets.This is what is often meant by \statistical arbitrage," the ability to predict
returns accurately based on insights our competitors do not have.some of them cannot exploit this information. We have listed several possibleIn summary, even assuming accurate information owned by participants,
causes of return predictability: pure arbitrage;heterogeneous risk preferences, liquidity, funding, 
ow predictability;
These categories are not exclusive. For example, 
ow predictability and liquidityare related, albeit not identical; and the distinction between being compensated informational advantages.
for risk-taking and holding an actual information advantage is usually unclear.However, these broad classes can help us reasoning about one strategy's edge.
1.5. The Elements of Quantitative In-vesting
The investment process is usually viewed as a highly structured process. Thereare separate components, the development of which is the responsibility ofseparate teams. In Figure 1.1 I show a possible organization of these components,
which I follow in the organization of the book. I review them below. 23


```
Expected ReturnsRisk
Cost
VolumesPrices Before The Trade During The Trade After The TradePnL
CharacteristicsUnstructuredTime Series
```
Data
Portfolio ConstructionSignal AggregationRisk ConstraintsHedging Intertemporal VolatilityLeverageAttributionSignalPnL
Figure 1.1: Data. The essential inputs to investing are under the \Data" section to theThe components of the investment process.
extreme left.{ Prices and trading volumesminutely, every 5, 10, 15 minutes, or daily. For high-frequency strategiesare often collected at regular intervals, e.g.,
{ it may be necessary to use order-level exchange data.Characteristicstime stamp. Consider them as descriptors of the security. For a stock,are numerical vectors associated with a security and a
a characteristic may be a measure of \quality", like the free cash 
owgenerated by the rm in the most recent quarter, divided by the marketcap of the rm. Another widely used characteristic is the realized return
{ of the stock over a certain interval, for example the past six months.Time Seriesin that they are not associated to individual securities, but rather providedier from characteristics (which are multivariate time series)
additional information entering the investment process. Examples of timeseries are the Consumer Price Index (CPI), which can be used to estimatein
ation rate in the U.S.; the yield of the 10-year Treasury bond; the
Federal Funds Eective Rate, the overnight rate for unsecured lendingof reserves among commercial banks; and the VIX, a forward-looking


```
{ measure of US equities market volatility.Time Series of Unstructured DataPrices, characteristics and times series are structured data i.e. numerical,are the dark matter of nancial data.
categorical, or ordinal (i.e., rankings), and in tabular form. Unstructureddata are usually character sequences representing natural language (ex-amples are earnings transcripts and rm news), or images (for example,
```
 Before the Tradesatellite images), video/audio les, or multimodal data, i.e., a combinationof all of the above formats.. Data are used to develop three components that enter the
portfolio construction during the trade. Because they precede the tradingprocess, I classify their development as being \before the trade".{ Risk. The word \risk" can mean many things. In the context of this book,
{ we will use portfolio volatility as a proxy for risk. Estimating this volatilityfor an arbitrary portfolio is a challenging task.Expected Returns. In order to be protable, a trading strategy needs to
have informative predictions of future returns. This is often viewed as theparamount concern of a quantitative investor, and to a large extent it is.In nearly all modern trading systems there is more than one estimate of
{ expected returns. The number of estimates can run in the thousands ormillions.Transaction Costs and Market Impact. Trading securities is expensive,
and these costs are unavoidable when deploying a strategy. Among otherthings, transaction costs determine whether a predicted return at somehorizon can be turned into a protable strategy or not; and what is the
 During the Trademaximum prot that can be extracted from such a strategy.. The three components developed in the previous stage 25


are combined in the portfolio construction phase. This happens \duringthe trade", because the portfolio construction procedure results in real-timetrading decisions, and these decisions determine the Prots and Loss of the
strategy. The decisions taken in the portfolio construction process are:{ Incorporation of Risk Constraintsmaximum risk that it can take. This is usually represented in the portfolio. A strategy's PnL is a function of the
construction problem either in the form of constraints, or in the form ofpenalties added to the objective function. Risk constraints and penaltiescan have a very material impact on the performance of the strategy.
{ Signal AggregationAs I mentioned above, there can be many signals for the returns of a singleasset. A problem encountered in practice is combining such signals into a. We use the termsignalfor a model of expected returns.
{ single signal.Hedging Decisionsrisk. In layman's terms: they can lose money because their returns are. Certain trading strategies haveexposureto systematic
hedgedcorrelated to market-wide sources of risk. Some of these sources can beimportant concept in portfolio construction., which means that such risk can be counterbalanced. This is an
 After the TradeLoss (PnL), both for the overall portfolio, and for its constituents.{ Performance Attribution. The trading process generates a time series of Prot and. In the portfolio construction phase we estimate
expected returns of individual signals. This is anwe observe the actual PnL of the portfolio. Performance attribution isthe practice of tracing back performance to its possible sources, to seeex anteexercise.Ex post,
what worked and what did not, so that we can learn from the experience.Moreover, performance attribution can also be employed to assess whether 26


{ we have skill in sizing our bets.Intertemporal Volatility Allocation and Leveragerisk across periods? This decision is very consequential to capital growth.. How should we allocate
(AUM).A closely related question is that of leverage, dened as the ratio betweenGross Market Value (GMV) of the portfolio and Assets under Management
I stress that dierent arrangements are possible; for example, Narang [2024]employs a simpler scheme, and Pedersen [2015] has yet another one. Some ofthe individual elements I introduce are present in these models of quantitative
investing.


1. Market participants can be broadly classied into sell-side andThe Takeaways
    buy-side participants. The sell-side participants are: Dealers;Brokers;Broker-Dealers.
The buy-side participants are: Indexers;Hedgers;Institutional Active Managers;
2. Excess returns arise from ve major sources: Asset Allocators;Informed Traders (e.g., hedge funds, principal trading rms);Retail Investors.
    (a) Risk;(b) Liquidity;(d) Predictable 
ows;(c) Funding constraints;
3. Quantitative investing employs elementary analytical models thatcan be partitioned in three broad groups:(a) Risk measurement models and data;(e) Informational advantage in predicting future returns.
    (b) Market Impact models;(c) Models of expected returns of assets.


# Chapter 2Returns: Properties and

# Models

## 1. How do we dene returns for equities, bonds, credit instruments,The Questions

## 2. What are the stylized properties of returns?3. futures?Why is volatility an important measure for risk and portfolioconstruction?

## 4. What is GARCH? How do we use it?5. How do we use Kalman Filtering to estimate volatility?6. How do we model multivariate returns?

## asset returns are the basic constituents of portfolios. We cannot hope tounderstand portfolio behavior without a solid understanding of their buildingWe start with models of univariate returns for one reason. First, single-

## blocks. Therefore, it is necessary to summarize the salient empirical propertiesof stock returns and the most common processes employed to model them,specically to model volatility eectively. Second, these models have general

## applicability and are even more useful when combined with other families ofmodels for multivariate returns. GARCH and exponential moving averages are 29


essential tools for the working modeler. In the process, I introduce models thatjustify their use. Exponential moving averages nd their motivation in linearstate-space models, while GARCH is an instance of a nonlinear state-space
model. These models will be your friends for life. The chapter has four parts.First, we lay out denitions of returns. Second, we summarize some \stylizedfacts" (empirical features of returns that are ubiquitous and relevant to risk
management). Third, we skim GARCH models and realized volatility models.Because both topics have been covered extensively in textbooks, my goal isto introduce the essentials, their associated insights, and provide a jump-o
point for the reader. Lastly, I touch on the State-Space Model for VarianceEstimation.
2.1. Returns2.1.1. Denitions
We have a set ofuse dollars throughout as currency. It is customary to assume that each of theseassets is innitely divisible. We buy the equivalent of a unit of currency fornassets and a currency, also called the numeraire^1. We will
assetdene returns is from the closing prices of security 1 i. We denote the value of the asset tomorrowion days 0 and 1, which weRi. An equivalent way to
the FrenchThis word comes to English from the Latinnumeraire. numerarius, or \a number", \a unit", through


denotePi(0) andPi(1), respectively. Theri(1) :=Pi(1)Preturni (0)Pi(0)^2 is dened as
We extend this denition to the case in which the security pays a dividend. Theholder of the asset receives an amountPi(0) andPi(1) respectively. Thedividend-adjusted returnDi(1), and the return is then dened asis dened as

We denote the vector of daily returns between epochsri(1) :=Pi(1) +DPii(0)(1) Pi(0)t 1 andtas (r 1 (t);:::;rn(t)).
A great deal of equity risk management deals with the properties of this vector.For a portfolioProt and Loss (PnL) in a single period is given by the change in the valuew 2 Rn, wherewiis a monetary amount invested in asseti, the
of the portfolio. The number of shares owned in assetThe value of the portfolio in period one isin value isPi(wi=Pi(0))Pi(1) Piwi. In vector form, this equalsPi(wi=Pi(0))iPis given byi(1), and the changew 0 wr.i=Pi(0).

risk-free rate2.1.2. Excess ReturnsIn the rest of the book, we will not use security returns, but returns minus the. If, for example, we model daily returns, the risk-free raterfis
the interest rate paid by the investor for borrowing cash over the same period,or paid to the investor for cash held in their account 2 3. If we hold a security, we
[2015] and Connor et al. [2010].borrower by the lending institution is risk-free plus a small spread, and the rate paid by the 3 Denitions of returns, log returns, dividend-adjusted returns are in Ruppert and MattesonThe two rates are not exactly the same: when borrowing, the eective rate charged to the


pay interest on the cash position of that security. If we are short, we receiveinterest. Cash is to all eects a security, but a special one, in the sense thatit has much lower volatility (for modeling purposes, negligible volatility) than
the other risky assets. We borrow or lend an amount equal to the Net MarketValue (NMV) of our portfolio, i.e., the sum of the values of each position. Thereturn of a portfolio is
The formula allows us to eliminate the risk-free asset from the portfolio andXi wiri (Xi wi)rf=Xi wi(ri rf)
provides a natural interpretation of security returns as returns in excess of arate received in the absence of investing. In the U.S.A., the reference rate is areference overnight lending rate, like the Secured Overnight Financing Rate
(SOFR)^4.
2.1.3. Log ReturnsIfThe variance of this portfolio can be computed by using just two pieces ofrfollows a multivariate Gaussian distribution, then so does the portfolio.
information: the portfolio weights, and the covariance matrix of the returns.least know thatThe question of whether net returns are Gaussian is an empirical one. We atifnet returns are Gaussian, they are very tractable for analysis
at a given point in time. However, they are not easily tractable in time seriessame institution to a lender is risk-free minus a spread. For modeling purposes, we considerthem identical.

(^4) https://www.newyorkfed.org/markets/reference-rates/sofr.


analysis. For example, dene the cumulative total return over periods 1ri(1 :T) :=PPii((0)T)  1 ;:::;T.

==(PriiP((TTi() + 1)(T )1)PPiir((iTT(T   1)2)1) + 1):::PPii(1)(0):::( ri(1) + 1) (^1)   1
Ifdistributed, and its distribution rapidly diverges from the normal distribution.riThe variance of the cumulative returns is not a simple function of the(t) are normally distributed, the cumulative total return is not normal
single-period variances.~r(t) :=On the other side, log returns are additive over time compounding. Letlog(1 +ri(t)). Then, the log of the compound return is equal to the
sum of the log returns in the same period, and if the log return is normal, so isthe log of the compound returns. If the returns are independent, the varianceof the log of compound log return is equal to the sum of the variances. We
can reconcile the two view of returns { raw and log { if the approximationlogthis case, we can make the approximation(x) =x 1 +o(jx  1 j) is suciently accurate, i.e., if net returns are small. Inr~i'ri, which is suciently accurate
provided the returns are not too large.A common approximation for the compounded net return of an asset over


time is given by Yt (r(t) + 1) 1 = exp (^) Xt ~r(t)!  1
'=1 +Xt Xr~t(t)r~(t)  1
Always verify the accuracy of the approximation, for example comparing theestimate of models developed usingapproximation is usually considered adequate for daily interval measurementsrandr~. When the assets are equities, the
or shorter.
2.1.4. Estimating Prices and ReturnsTo estimate return, we need prices. Prices, however, depend crucially on theway a market is designed. Over-the-counter markets [Harris, 2003] dier from
exchanges that employ limit-order books [Bouchaud et al., 2018]. Within asingle exchange, the trading mechanism can change over the course of theday, with auctions often taking place at the beginning and at the close of the
trading day. As a result of market design, the observation of prices exhibitsmeasurement error. The most conspicuous example of such an error is thebid-ask spread. In limit-order books, the buy orders have a price attribute (the
\bidding" price per share the buyer is willing to pay) and a quantity. Similarly,the sell orders have a price attribute, or \asking price" and a quantity. Askingprices are higher than bidding prices, and the dierence is called the bid-ask


spread. This spread is a multiple of the minimum tick sizeoccur, a buy order or a sell order must cross the spread; either event can occur.As a result, the transaction price will be either at the top or the bottom of the^5. For a transaction to
bid-ask spread interval. Successive transactions will have dierent price marksdue to the partial randomness of buying and selling transaction. The bid-askspread bounce is not the only source of measurement error. For example, prices
can dier by exchanges, and the selection of price by timestamp depends on thechoice of data integration. Then, there may be outright measurement errors. Itis important to consider the fact that prices are imperfectly observed early on,

rather than ignore them and their impact and face unintended consequences.Perhaps the simplest model is the Roll model for asset prices [Roll, 1984]. Inthis model (^6) , the \true" pricemtof an asset evolves as an arithmetic random
walk, and we imperfectly observe the pricemt+1=mt+t+1 pt. In formulas:(evolution)
witht;tindependent random variables (serially and from each other) dis-pt+1=mt+1+t+1 (observation)
tributed according to a standard normal.consequence: consecutive price dierences are negatively correlated. The priceBefore we try to estimate prices, the model has an immediate and testable
dierence is above $1. (^5) As of publication time, the minimum tick size is $0.01 in US exchanges for shares tradingpt+1:=t+1+(t+1 t), which is zero in expectation.
(^6) A detailed discussion of the Roll model and its extensions is in Hasbrouck [2007].


However, E(pt+1pt) =  2
The lag-one autocorrelation can also be used to estimate the measurement error.E(pt+1ps) =0; s < t
The presence of large non-zero autocorrelations beyond lag one may point tomodel inadequacy, in the sense that there are actual long-term dependencies inthe price processmt. The model can be extended to arbitrary lags. An optimal
estimator forAppendix, Section 2.4.1, and specically in Example 2.1 of Section 2.4.2. Theestimator is given bymtis provided by the Kalman lter. The lter is covered in the

where the explicit formula form^t+1jtK=(1 2 (0 ;K1) is given in the Appendix. The smaller) ^mtjt ^1 +Kpt
the ratioaverage observation if the price observations are accurate. The gist of themodel is that an exponential moving averages of prices is preferable to just=, the higher theK, which makes sense: we do not need to
taking the last price in the measurement period. If we want the daily closingprice, for example, we may want to use a weighted average of 5-minute intervalprices in the preceding interval. There is a caveat, however. Suppose we have
estimatesrinTm:=^(nm^ 1)nTTm^=mandt^, and we use these estimates to compute returns at intervals(n m^1)nTT the two estimates are positively correlated. One should1. Because we employ the same observed pricespTboth; i.e.
always check that (1 K)T1 to alleviate this spurious correlation. 36


2.1.5. Stylized FactsBefore building the house, we need to look at the bricks, namely, the statisticalproperties of the single-stock returns. Below I list some \stylized facts" about

stock returns, and discuss their relevance to risk modeling and management.Returns have a lower bound at -1. We usually characterize the properties of~r(t) :=log(1 +r(t)). We focus on the properties ofr~(t), but alsoj~r(t)jand~r (^2) (t),
the volatility of the log returns. Here are some properties. See Cont [2001],Taylor [2007], Zivot [2009], Ratli-Crain et al. [2023].1. Absence of autocorrelations. Lagged autocorrelations are small unless you
observe prices and returns at time scales in which the market microstruc-ture becomes relevant (say, intraday). See Figure 2.1.Table 2.1: Sample skewness and kurtosis of daily log
returns andnonparametric bootstrap with replacement (5000 variates).Range: 1/3/2001-12/8/2017.p= 0:Skewness01 condence intervals estimated usingKurtosis
StockAAPLIBMNRG Mean Left Right Mean Left Right-0.20.10.4 -0.5-0.2-0.5 0.20.51.2 14.35.77.1 3.65.47.9 20.07.88.7
WATSPY -2.0-0.1 -3.3-0.7 -0.60.6 29.8 12.811.4 6.5 48.116.0

2. Heavy tailsbehavior. This will be made more precise in the following section, but theprobability of a large return is higher than what would be consistent with. Theunconditionaldistribution of returns shows heavy tail
    any \thin-tailed" distribution with innite moments. Examples of samplekurtosis are in Table 2.1. Theconditional 37 (say, conditional on the return's


0.00.20.4 0 5 10 15 20

```
0.60.81.0
Lag
```
```
ACF
0.00.20.4 0 5 10 15 20
```
```
0.60.81.0
Lag
```
```
ACF
(a) (b)
0.00.20.4 0 5 10 15 20
```
```
0.60.81.0
Lag
```
```
ACF
0.00.20.4 0 5 10 15 20
```
```
0.60.81.0
Lag
```
```
ACF
(c) (d)
0.00.20.4 0 5 10 15 20
```
```
0.60.81.0
Lag
```
```
ACF
0.00.20.4 0 5 10 15 20
```
```
0.60.81.0
Lag
```
ACF

(a) AAPL, (b) IBM, (c) NRG, (d) WAT, (e) SPY, (f) XLK.Figure 2.1:Autocorrelation plot of daily log returns (range: 1/3/2000-12/8/2017) for(e) (f)


3. entire history up to timebehavior as well, but with lighter tails than the unconditional one.Autocorrelation of absolute returns and second momentst) distribution of returns may show heavy tail. The time series
    jlute values is greatest and is called the \Taylor Eect" in the literature[Taylor, 1986, Granger and Ding, 1995].Ri(t)jandR^2 i show strong autocorrelation. The autocorrelation of abso-
4. Aggregational Gaussianityreturns, as opposed to daily or intraday returns), the distribution ofreturns becomes closer to a Gaussian distribution.. At longer time scales (say, weekly or monthly
Realitylike the geometric diusion process at the core of simple derivative pricingmodels:^7 is in stark contrast with simple models of univariate price dynamics

This model predicts Gaussian, independent log returns, which are inconsistentdP(t) =P(t)dt+P(t)dW(t) (2.1)
with the empirical evidence. First, returns show little serial autocorrelation.Thispredictable based on the history of returns or some additional explanatorydoes not meanthat returns are independent, nor that returns are un-
variables. Regarding the former point: zero-autocorrelation does not implyindependence.Regarding the latter,returns are predictable. This is not only an article of

faith of active investors, who usually do a terrible job at it, but also a relativelythe words of Cont [2001], \most measures of volatility of an asset are negatively correlated (^7) Note, however, that I am not including the Leverage Eect among the stylized facts. In
with the returns of that asset". This eect is not suciently strong in recent data, as shownby Ratli-Crain et al. [2023]. 39


uncontroversial empirical nding among academicsthey are predictable, they are not so trivially predictable.Regarding heavy tails: for asset returns, we restrict our attention to power-^8. Nevertheless, even though

tailed distributions: the complement of the cumulative distribution functionfollows a power law:Gaussian returns: ifrF(xN) :=(0;P1), then a common approximation [Wasserman,(r > x) =Cx  (^) , with >0. Compare this to
2004] for the tail probability isp (^12) e x (^2) = 2 x (^1)  x 13 F(x)p (^12) e x (^2) = (^21) x (2.2)
For the caseand the symmetric inequality of the left tail:jxj1, the right-side inequality can be used to bound quantiles
FF((xx))pp^1122 ee  xx^22 ==^22 ))FF  ^11 (1()  )qq2 log[(2 log[(p 2 p 2 ) (1 (^1) ] )) ^1 ] (2.3)(2.4)
The approximation is quite accurate:qmoments of any order. A power-tail random variable with exponent2 log[1=(p 2 )]for 10  (^10) <  <1. A Gaussian random variable has nite q2 log[1=(p 2 )]F ^1 ()  has nite 0 : 965 
moment only up toto constants, by (1=) 1 =. It is not controversial that the unconditional log returns have heavyplog(1. A Gaussian random variable has quantiles bounded, up=), while a power-tail one has a quantile of the form
tails. It is still not settled what the exponentis. It seems, however, that 8 '4. This is important for estimation purposes. A associated with the distribution
entry \Predictability and correlation" (John Cochrane has written extensively on the subject, e. g., Cochrane [2008] and the bloghttps://tinyurl.com/predcochrane)


sucient condition for the estimability of the volatility of returns is that theirfourth moment is nite. To see this, recall that the Central Limit Theoremsays that, ifxtare iid random variables with meanand variance (^2) , then
Tmeanresult on ^1 =^2 PpTTt=1Eand variance(xrt (^2) ): assume thatconverges in distribution to a Gaussian random variable with (^2). The theorem allows us to establish an asymptoticriare iid. Setxt:=rt (^2). If we want to estimate
Ecase. However, a related question is whether theis heavy-tailed. If the heavy tailed characteristic of conditional returns is ignored(r^2 t) using the CLT, then we need niteness ofconditionalE(r^4 t). This seems to be thereturn distribution
or considered inessential, then it is possible to model returns as a process withconditional Gaussian returns and heavy-tailed unconditional ones. This family,denoted Conditional Heteroscedastic Models, is rich and the subject of the
following subsection. We won't cover models with long-range dependence and/orheavy tailed conditional and unconditional returns, like Levy processes andFARIMA models. No model covers all the empirical features observed in stock
returns. GARCH models (and mixture models in general) have the benet ofbeing easy to interpret, simulate, and estimate.
2.2. Conditional Heteroscedastic Mod-els (CHM)
This family of models was rst proposed in the early 1980s by Engle [1982],Engle and Bollerslev [1986]. By the next decade they had been generalized


```
and applied to several economic domainsEconometrics book.The most popular and studied model in this family is the GARCH(1,1)^9. They are extensively covered in any
model. It has good empirical properties, its theoretical properties have beencharacterized, and can be estimated eciently. It also conveys the gist of thelarge set of models in this family. The fundamental insight of the model is to
make theThe laws for GARCH(1,1) areparametersin the model a part of the state of the stochastic process.
```
hr^2 ttt==h (^) Nt 0 (0t+;1) 1 rt^2   1 + 1 h^2 t  1 (2.5)(2.6)(2.7)
In the equation above,of returns by virtue of Equation (2.5). The parametersto be non-negative. The evolution of the processhtis the volatility at timehttis determined by Equationand it determines the size 0 ; 1 ; 1 are assumed
(2.6)process when we remove the term. To gain some intuition, let us look at the second equation of the GARCH 1 rt (^2)   1. The equation
Cizek et al. [2011], Ruppert and Matteson [2015], Tsay [2010], Lutkepohl [2005] are standard^9 The literature on GARCH models alone is immense; Tsay [2010], Zivot and Wang [2003],h^2 t=^0 +^1 h^2 t ^1 (2.8)
references, and survey are Andersen et al. [2006, 2013]. The handbook Andersen et al. [2009]has dedicated chapters covering univariate [Terasvirta, 2009a] and multivariate GARCH[Terasvirta, 2009b], moments of GARCH models [Lindner, 2009], their detailed extremalproperties [Davis and Mikosch, 2009], multivariate GARCH. For a recent empirical paper on
the performance of GARCH, TARCH, EGARCH and a few other models, see Hansen andLunde [2005], Brownlees et al. [2011]. 42


can be rewritten as h (^2) t h (^2) = 1 (h (^2) t  1  h (^2) )
where h (^2) := 1   (^01)
The value ofHigh values of the squared returnthat 1 >0. This in turn increases the probability of large squared returnsh^2 t converges toh^2 at a geometric rate, so long as 0r (^2) t shock the volatility upward, provided< 1 <1.
in the following period, giving rise to a rich dynamic behavior. The increasein volatility cannot continue unabated, because the termdampen variances that are much greater than the \equilibrium level" 1 (h (^2) t  1  hh (^22). This) will
can be seen through substitution in the second equation of the model:h (^2) t=h (^2) + 1 Xi (^1) =1 i 1   (^1) rt (^2)  i (2.9)
One could replace the true values offormula by saying that the variance estimate is an exponential moving averageof non-iid returns, since they are modulated by 0 ; 1 ; 1 with estimates, and interpret theht, in light of Equation (2.5).
2.2.1. GARCH(1, 1) and Return Stylized FactsThe GARCH model improves on the distributional properties of returnsby making them closer to normal; see Figure 2.2. How does the GARCH(1, 1)rt,
model stack up against the stylized facts?1. Absence of autocorrelations. This property is satised (not hard to verify


2. directly).Heavy Tailsand Starica, 2000], the tails of the unconditional returns are heavy tailed.. The unconditional returns are leptokurtic. Moreover [Mikosch
3. So, this checks out.absolute return) before you celebrate.Autocorrelation of absolute and squared returnsHowever, wait until point 4 below (autocorrelation of. The ACF for GARCH(1,
    1) is positive for both absolute and squared returns. For squared returns,it has the form [He and Terasvirta, 1999, Ruppert and Matteson, 2015]
    However, if we look at kurtosis and lag-1 autocorrelation for commonn=^8 >><>>:^111 ((1^  ^1  ^2 +^1111 )^1 n   ^11212 ) ififnn >= 1^1
    stock indices, it appears that the autocorrelation predicted by the modelfor a given observed kurtosis level isSee Terasvirta [2009a]. too highto that observed in practice.
4.Summing up, some but not all of the stylized facts about log returns areAggregational Gaussianityproperty, to the best my knowledge, it is satised in simulations.. Although there are no known results on this
captured by GARCH(1, 1).


```
lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
−5^05 llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
−4 −2 theoretical 0 2 4
```
```
sample
typelGARCH(1, 1)lUNCONDITIONAL llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
ll
llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
−5^1005 llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
−4 −2 theoretical 0 2 4
```
```
sample
(a) typelGARCH(1, 1)(b)lUNCONDITIONAL
llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
llll
lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
−5^1005 lllllllllllllllllllllllllll
```
```
15
−2 theoretical 0 2
```
```
sample
typelGARCH(1, 1)lUNCONDITIONAL llll
```
```
llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
llllll
llllllllllllllllllllllll
−10^0 llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
10
−4 −2 theoretical 0 2 4
```
```
sample
(c) typelGARCH(1, 1)(d)lUNCONDITIONAL
lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
−5^1005 llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
−4 −2 theoretical 0 2 4
```
```
sample
typelGARCH(1, 1)lUNCONDITIONAL llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
```
```
lll
−5^0
```
(^105)
−4 −2 theoretical 0 2 4
sample
Figure 2.2:Quantile-Quantile plot for daily log returns (blue dots) and GARCH(1,(e) typelGARCH(1, 1)(f)lUNCONDITIONAL
(a) AAPL, (b) IBM, (c) NRG, (d) WAT, (e) SPY, (f) XLK. Return range:1) residuals (orange dots) of log returns against the theoretical normal distribution for1/3/2001-12/8/2017.


Table 2.2:between the theoretical normal distribution andthe empirical distribution of log returns andresiduals of GARCH(1, 1) of log returns. Thedistance is reduced in all instances, with theKolmogorov-Smirnov distances
10.largest improvements for the two proxies for themarket (SPY) and the technology sector (XLK).For background on the Kolmogorov-Smirovdistance, see DeGroot and Schervish [2012], Ch.
StockAAPLIBMNRG Unconditional GARCH(1, 1)0.0670.0780.088 0.0440.0470.060
WATSPYXLK 0.1090.0980.091 0.0910.0400.043
We now look at GARCH(1, 1) through dierent modeling approaches. First, we2.2.2.could reformulate it as a random iterated function. Rewrite Equation (2.6) as?GARCH as random recursive equations
Set h^2 t=^0 +^1 h^2 t ^1 ^2 t ^1 +^1 h^2 t ^1
The random variablesatare iid. Thenat:=^1 +^1 ^2 t ^1

h^2 t=ath^2 t  1 + (^0)


Table 2.3:p (^) valuerespectively. The values of^(x= 1 +)/xminxn [ (^) P; see Clauset et al. [2009]. The value of. We use the Maximum Likelihood Estimator (MLE)ilogEstimated(xi=xmin (^) )]  for left and right tail of probability density function (^1) increase sizably for the two indices SPY and XLK., wherenis the number of observations above a cut-oxminis set to -2.5 and 2.5
StockAAPL Unconditional GARCH(1, 1)Left Tail4.8 4.6 Unconditional GARCH(1, 1)Right Tail4.8 4.9
IBMNRGWATSPY 4.34.03.44.1 3.95.93.25.9 4.23.84.34.2 4.64.14.08.5
This formulation shows that the process is Markovian, and that the varianceXLK 5.0 6.3 4.4 5.9
process is governed by an autoregressive equation with random coecientsBy recursion [Lindner, 2009], we can rewrite the equations as at.
This allows us to study the process using the toolkit of random recursiveh^2 t=^ Yi=0k at i!h^2 t k+^00 @1 +Xi=0k iYj =0^1 at j^1 A
equationsprocess. Nelson [1990] characterizes the conditions for convergence. In the caseThe distribution of^10. aiplays the essential role in the convergence of the
(^) by Kesten [1973]; Diaconis and Freedman [1999] survey the general recursive equations 010 = 0:The convergence properties of Random Recursive Equations (RREs) were studied rst
xA monograph on RREs, covering both the univariate and multivariate case, is Buraczewskiet al. [2016].t=f(xt  1 ;t+1), where (t)^1 t=1is an iid random sequence, of which RREs are a special case.


1. If2. If3. IfEEE(log(log(logaaattt))) = 0, then><0, then0, thenhhh^2 t (^2) t (^2) t!1!is a driftless random walk.0 a.s.a.s.
In the case1. If2. IfEE(log(log (^0) aa>tt))0:<0, then0, thenhh (^2) tt!1converges to a nondegenerate distribution witha.s.
The kurtosis of the process isa support on [^0 =(1 ^1 );^1 ).
so the process is leptokurtic as long ask=3(1 +^1  ^112 + ^21 )(1^1  ^1  ^13  ^121 )= 3 11 > 0. How about skewness? The^1 ( ^1 (+^1 +^1 )^21  )^2221 >^3
unconditional returns are not skewed, becauseE[(r 1  E(r 1 )) (^3) ] =E(h (^31) )E( (^3) t) = 0
Finally, we point out that not only are the unconditional returns leptokurtic, butdo in fact have Pareto tails, provided the process is stationary:for some >0; see Mikosch and Starica [2000], Buraczewski et al. [2016].P(rt> x)x  (^) ,
2.2.3.Although GARCH models are highly general, the vast majority of CHM appli-cations are indeed GARCH(1, 1), so we restrict our analysis to this case for?GARCH(1, 1) Estimation
simplicity. Generalization to nite-order processes is straightforward. Dene:= ( 0 ; 1 ; 1 ), and letfbe the log density function of the standard normal


distribution. rt=htt
By repeated substitution, we can express the unobserved varianceh^2 t=(h^2 t ^1 ;r^2 t ^1 ;) h^2 t as a
function of the sequencet=rt=htis given by r 1 ;:::;rt  1 ,h 1 and. The log-likelihood of the sequence
We can then estimate the parametersL() =XtT=1fht(r^1 of the model by maximizing the log-;:::;rrt t ^1 ;)

likelihood. As an example, consider the GARCH(1, 1) model. The recursiveequation forh (^2) tis given by Equation (2.9), so we solve
mins:t:hXtT=1t= log 0 h 12 t 1  +  rh t 12 t  (^2) t 1  (^1) + 1 Xti =1 (^11) i  (^1) r (^2) t i! 1 = (^2) t= 1;:::;T
2.2.4. Realized VolatilityCHMs model the asset volatility as an (unobserved) state of the return stochasticprocess. Once we have an estimate of the volatility at timetof returns, the rest
is trivial. An alternative route would be to estimate directly the volatility fromthe data, for example with a simple moving-window estimator of the empiricalvolatility. This approach would not work if the epochs for which we need the
estimates are days, and we only have daily data. In recent years, tick-level 49


price data have become widely available; indeed, order-book level data are alsoavailable (with the entire process of order arrivals, llings, and cancellations).It is now possible to compute 1-minute returns, enabling us to estimate the
volatility of returns for daily predictions by using these high-frequency data.Below we review some of the statistical properties of realized volatility (RV)measurements. The starting point is Equation (2.1), i.e., a diusion process for
the log pricep(t) = logP(t): dp=dt+dW
(the volatility) are constants. In all applications of interest, the drift is muchwheresmaller than the volatility:W(t) is a Brownian process. The scalarsj j . The quantity^2 =R(the drift) andis termed the (daily) >^0
Sharpe Ratiothe process in the interval [0length 1=n. The measured return isand will gure prominently in the rest of the book;1] and measure the state variabler(j) :=p(j=n) p((j 1)=np^11 ). Clearly,at intervals of. We observer(j)
are iid random variables, andestimators for drift and moments arer(j)N(=n;^2 =n). The maximum likelihood
^^ ^^21 ==XXjj [rr((jj) =) p=n^(1)] ^2 p(0)
daily Sharpe Ratio computed on returns.^11 This is the Sharpe Ratio of log returns, which is to a rst approximation close to the


We also consider theuncentered^estimator of the volatility (^22) =Xj r (^2) (j)^12 (2.10)
(MLE) estimator for the drift does not depend on the number of intervalsThe rst remarkable phenomenon is that the Maximum Likelihood EstimatorMoreover, one can show thatvar( ^) =var(p(1) p(0)), andp(1) p(0)n.
Nnumber of intervals either. To estimate the variance offew formulas. The moments of(;), so thatvar( ^) =^2. The estimation error does not depend on ther(j) are those of a Gaussian random variable^ 12 and^ 22 we need a
with mean=nand varianceE[r(j)] = (^) n^2 =n: (2.11)
EE[[rr^24 ((jj)] =)] =^ n (^) n^24 ++ 6n^2  (^) n (^2) n (^2) + 3n 2  2 (2.12)(2.13)
Shephard [2002] and a survey is Andersen and Benzoni [2009]. Also useful are the surveys ofAndersen et al. [2006, 2013], which situate realized volatility in the context of risk managementtechniques. Essential readings on realized volatility estimators are Zhang et al. [2005], which^12 An early analysis of the \vanilla" Realized Variance estimator is Barndor-Nielsen and
presents several estimators and introduces the idea of subsampling for RV; the series ofpapers Barndor-Nielsen et al. [2008, 2009] on kernel-based estimators; the empirical paperby Liu et al. [2015], comparing several estimators, which includes subsampling and kernel.This list of estimators is not exhaustive. For example, Hansen and Lunde Hansen and Lunde
[2006b] analyze an autocorrelation-adjusted estimator introduced in French et al. [1987].Bipower estimators are studied by Podolskij and Vetter [2009] and maximum likelihood onesby At-Sahalia et al. [2005]. Moreover, these estimators depend on several parameters, likesampling and subsampling intervals, or the choice of kernel.


so that var(r (^2) (j)) = 2n 2  (^2) + 4 (^) n (^2) n (^2) (2.14)
and E(^ 22 ) = (^2) + (^) n (^2) from Equation (2.12)
The estimatorvar(^^2222 ) =2has a small nite-sample bias and is asymptotically consistent.n^4 + 4^ n^2 ^2 from Equation (2.14)
Insight 2.1:Based on Equationsfor variance estimation, since the bias is inversely proportional toEstimating Variance(2.12)and(2.14), you can use uncentered returnsn, and
the estimator is consistent.
the price process occurs intowithin an interval of length 1Let us re
ect on the steps we took. We discretized the interval over which=nn, assuming the price had no measurement error.subintervals, and retained only the last price
We saw that the drift estimator is unbiased, but its variance does not dependon the discretization: we have more estimates of the drift, but they are noisier.Unfortunately, there is no easy way to measure the drift, i.e., the expected
return, of a security; otherwise, all Statistics undergraduates would be rich.Conversely, we have identied an uncentered estimator of the true varianceAs the numbernof intervals approaches innity, the estimator is unbiased. Its (^2).
variance decreases like 2^2 =n, which is good news: in principle, we can estimate 52


to arbitrary accuracy the volatility of the returns at timethe true volatility varies very little over time, we can use this estimate to predictvariance at timet+ 1. The good news here is that if you need volatility estimatest; and provided that
over a long time scale for your decisions (e.g., days), but have data over ashorter time scale (e.g., minutes), you do not have to devise a generative modellike CHMs or others. What assumptions do not hold in this line of reasoning?
Here is a list of issues to consider:1. We ignored market microstructure. One source of noise is the bid-askspread [Harris, 2003]. When the seller initiates the transaction, she receives
the bid price; when the buyer initiates it, he pays the ask price. Thereis an intrinsic error in the measurement of price, which is approximatelyequal to half the bid-ask spread. We model this error by assuming that log

2. prices in intervalidentically distributed (iid) random variables.Another form of microstructure is thinly-traded securities, etc. If a stocktarept+t, where the noise termstare independent,
3. trades less than once every ve minutes on average, then using one-minuteintervals is probably not a good modeling choice.We assumed that volatility is changing slowly, or is ideally constant.
    This is not the case in practice. One approach is to impose a model onthe time series of realized variances, so that we can produce an errorestimate. E.g., a simple AR(1) model^(t+ 1) =a+b^(t) +(t+ 1),
4. withWe ignored the distinction between open-to-close and close-to-open inter-val. Close-to-open returns are often fundamentally driven. Also, we are(t+ 1)N(0;1).
    ignoring the large volatility and bid-ask spreads in the rst minutes ofthe trading day.


broad set of estimators, with several choices of parameters, for assets in dierentasset classes (equities, futures, indices). They use Romano and Wolf's procedureFor the rest of us, the question is: what to choose? Liu et al. [2015] compare a
for multiple comparison [Romano and Wolf, 2005] and Hansencondence set" [Hansen et al., 2011]. They nd that the Vanilla RV at 5-minutesintervals performs competitively across various assets and asset classes. Thereet al.\model
are a few cases where this is not true. When higher-frequency measurementsare available, this estimator is outperformed by a one-minute subsampled RV,by 1- and 5-second interval realized kernel. In addition, at lower frequencies,
5- and 15-minute truncated RV [Mancini, 2009, 2011] also outperforms vanillaRV. However, where available, 5-min nonoverlapping intervals seem to be areasonable choice.
2.2.5. Combining CHM and Realized VolatilityIs it possible to have the best of both worlds, GARCH models and realizedvolatility? Hansen et al. [2012] present a model, RealGARCH(1,1), that combine
both. rt=htt

hx^2 tt== (^)  (^0) ++h (^12) th+^2 t u (^1) t+
xt  (^1) (2.15)
The rst two equations are similar to the standard GARCH(1, 1) model, withone dierence: the term proportional toproportional toxt  1. This variable is the observed estimate of the realizedrt (^2)   1 has been replaced by a term


variance at timeof variancelast Equation (2.15) models the dynamic behavior of the realized variance. Itr (^2) t  1 , then the model will probably outperform GARCH(1, 1). Thet; when this estimator is more accurate than the rough estimate
posits a linear dependence onvariablesu 1 ;:::;utare iid random variables, not necessarily with zero mean.htand on a stochastic termut. The random
2.3. State-Space Estimation of Variance2.3.1. Muth's Original Model: EWMA
A very popular estimator of the expected value of a time seriesdata up to timetakes the form t, is theexponentially weighted moving average(or EWMA). Itfxsg, based on
for some 0< K <1. We discount the past by giving its observations exponen-x^t= (1 K)Xs^1 =0Ksxt s
tially decreasing weights, which makes sense, and even more so when we writethe estimate as a recursion:
A low value ofKforgets the past faster. The formula is computationally ecient^xt= (1 K)xt+Kx^t ^1
both in terms of storage and computation. For uncentered variance estimationof a return, this takes the form
^^2 t= (1 K 55 )r^2 t+K^^2 t  1 (2.16)


Insight 2.2:Recall Equation (2.9):GARCH are EWMA with an oset
This is, save for an oset, very similar to Equation (2.16):h^2 t=^1  ^01 +^1 Xi^1 =1^1 i ^1 r^2 t i
(we have changed the indexing convention to make it consistent withGARCH). The two are identical when^t^2 = (1 K)Xi^1 =1 0 K= 0,i ^1 r^2 t   1 i= 1 K, and 1 =K.
to GARCH models (for a rare example, see Ding and Meade [2010]); amongpractitioners, including major commercial risk model providers like RiskMetrics,In academic journals, EWMA receives relatively low attention compared
Barra, and Axioma, it is the other way around. Aside from these practicalconsiderations, is it possible to motivate the approach based on a model? Wedevote this section to understanding and extending this simple formula.
brie
y covered in the Appendix, Section 2.4.1. Rather than giving it a generaltreatment and then specializing to a specic model, we will jump right in theWe will employ linear state-space models and Kalman Filters, which are
middle with a relevant example. As it happens, this example is also the simplestnon-trivial example of a state-space model. The model [Muth, 1960] posits thatthere is a scalarstatextthat evolves randomly over time with the addition of
a Gaussian disturbance to its previous value. We observe the state imperfectly;


theobservationytis a noisy measure valuext+1=xt+tx+1t. In formulas:
yt+1tt=xNNt+1(0(0;;+1)1)t+1
The innovations and the measurement noises are Gaussian with mean zero, andthey are independent of each other:alltands. I skipped the derivation, which the interested reader can nd in thes?ts?tfor alls 6 =t, ands?tfor
Appendix. Dene the ratio of measurement to innovation noisestationary ^t+1jtstandard deviation of the state estimate is given by::==. The
and the optimal estimation recursion is^^2 t+1jt=^2 1 +p(2^2 )^2 + 1
^xt+1Kjt:==(1^^2 t+1 ^^2 tj+1Kt+)^jtxt^2 jt  1 +Kyt

For1 the formula simplies:x^tjt=1 +x^tjt  1 +1 + (^1) yt
This is an exponential weighted average with a simple interpretation. Imaginethat the state does not change at all. Then we want to use all the history wecan, since old observations and new ones are drawn from the same distribution.


0.2

0.40.6

0.81.0

0.0 2.5 5.0 7.5 10.0

K

Figure 2.3:The half-life of EWMA is indeed long. Conversely, when the state changes at aRelationship betweenKand:==.

rapid pace, i.e.,According to Muth's original model applied to volatility estimation, the stateis the instantaneous variance, and the observation'0, then we want to discount the past very aggressively.ytisrt (^2) , which is equal tot 2
in expectation.then the observation error is not normally distributed. More importantly, theThe model has obvious shortcomings. If returns are normally distributed,
model allows for negative values of the variance, and additionally models thevariance evolution as the sum of iid innovations. Over time, the distributionof the variance becomes more and more spread out: the standard deviation of
the distribution grows as the square root of the number of periods. In practice,however, volatility appears to revert to a long-term average.


with non-normal innovations and measurement errors, provided that these arenot too heavy-tailed. As for the other shortcomings, we can rene the model toWe cannot directly address the rst problem. Kalman lters can work well
accommodate them. For example, we can introduce a mean-reverting model ofvariance, so that it behaves like an autoregressive process. We extend slightlythe state equation by adding a mean-reversion term:

The state reverts to valuext+1when it is away from this equilibrium value. The=xt (xt ) +t+1

stationary distribution ofand standard deviation equal tois still xtis Gaussian, with the expected value equal to (^2) =(2  (^2) ). The optimal variance estimator
However, compared to the rst model, the value of^xt+1jt=(1 K)^xtjt ^1 +KyKt, when >0, issmaller.
Otherwise stated, the mean reversion term makes the distribution of the truevariance more concentrated around its long-term mean. This means that wediscount the past less. The detailed derivation of these formulas is in the
Appendix, Section 2.4.2.Insight 2.3:On the Relative Merits of ECH and EWMA
TODO


2.3.2.As a nal example of the 
exibility that linear state-space models can oer, Ipresent the model by Harvey and Shephard [1996], which has several desirable?The Harvey-Shephard Model
features: it has a closed-form solution; the volatility is by design positive andthe distribution of the volatility itself is log-normal, hence right-skewed, as wewould expect; and the stock returns are locally lognormal.
The generating process for returnsrt=e +exp(rtxtis assumed to be=2)t  1 (2.17)
wherein time, lognormally distributed. Dene is a known constant, andtN(0;1); hence returns are, at any point

)) loguuut (^2) tt:= log(1 += exp(=xt+ logxt=2)rtt 2 )t ^
where :=E(logt^2 )'   1 :27, andtis a zero-mean random variable with=xt+t+^
standard deviation stdev(logyt:= logt^2 )u' (^2) t  2 :22. Dene
= log[(log(1 +rt)  )^2 ] 


so that we get an observation equation:yt=xt+t
Now, we posit an evolution equation forxt+1=b+axxt:t+t

This is the same model as AR(1), from which we obtain an estimate (^) given by= 0, then the formulas take a simple form:ut'rtand the state estimate isx^t. If
SinceRt=x^expt+1(jtexp= (1(xt =2)Kt)^) is a lognormal random variable, the estimatedxtjt ^1 +K[log[(log(1 +rt) ^ )^2 ] ^ ]
standard deviation of^tR+1tjist=q(eexp(^xt+1jt) 1)eexp(^xt+1jt)
A simplied Harvey-Shephard model starts with Equationapplies the rst-order approximationex  1 'x, and the parameter(2.17), to which it = 0:
Dene rt= exp(xt=2)t
logr^2 t:==xxtt+ log+t+t^2


whereis completed by the Equations, also from the original model, andtare dened as for the Harvey-Shephard model above. The model

xt+1yt== logb+axr (^2) tt + t
The state estimate and volatility estimates arex^t+1jt=(1 K)^xtjt  1 +K[logr (^2) t  ]
^t+1jt=ex^t+1jt=^2
2.4.2.4.1. The Kalman Filter?Appendix
This section contains a short treatment of the Kalman Filter (KF). The KalmanFilter predates Kalman's original articles in the early 1960's [Kalman, 1960,Kalman and Bucy, 1961]. At the time of their publication, computers had
(re)discovery of the lter by Kalman very timely. Rockets used by the Apollobecome available that made calculations feasible in real time. This made theprogram contained implementations of the Kalman Filter in 2KB of RAM.
Since the 60s, the topic of linear control and ltering has 
ourished. Thousandsof papers have been written on it, and there are several monographs coveringthe Kalman Filter in details from dierent perspectives: control [Simon, 2006,
Whittle, 1996], statistical [Harvey, 1990], econometric [Hansen and Sargent,2008]. I cover the KF for two reasons. First, because, for somewhat mysterious


reasons, the derivation of the KF is often more complicated than it should be.A rigorous yet, I hope, intuitive proof essentially ts in half a page and shouldsave the reader a few hours. Secondly, I wanted to present the model under

two dierent lenses, and show its close connection to the Linear QuadraticRegulator (LQR). Both are essential tools in the arsenal of the quantitativenance researcher, so there is value in catching two birds with one stone (^13).
normal random vector with mean and covariance matrixWe need the following elementary fact. Letz:= [x;y]^0 be multivariate
The random vectorz:=^264 xyx^375 , conditional oncov(yZ=) =b^264 is still normally distributed,xy;;xx xy;;yy^375
with conditional mean and covariance matrix equal toE(xjy=b) =x+x;y y; (^1) y(b y) (2.18)
This can be veried directly by integration.cov(xjy=b) =x;x x;y y;^1 yy;x (2.19)
vectorThe vectorOur model has two components. The rst is axt. This vector follows a simple evolution rule:tis random, serially independent, and distributed according tostate, represented by a randomxt+1 =Axt+t+1.
a multivariate normal distribution. The state is not observable directly; theonly thing we know is its probability distribution at time 1. We assume it isnormal with known mean and covariance matrix. In addition, over time we
(^13) However, should you catch birds, please don't use stones, but nets, or food. 63


```
observe a vectoryt+1=Bxt+1+ytt+1, which is a linear transformation of. Note the similarity with the factor model equation:xt, corrupted by noise:
observationstate $$ factor returnasset return
```
What is dierent is that factors returns are usually not modeled as being seriallydependent.The vectortis random, serially independent, independent of (t) (^1) t=1, and
distributed according to a multivariate normal distribution.Summing up, the distributions ofx 1 ;t;tare given by
x (^1) ttNNN(((^x 000 ;;;^ (^0) ))) tt??ss;;tt??ss+1+1 s < ts < t
And the Linear State Space Model is given byxt+1=Axt+t+1 (2.20)
I denote^xtjt  1 ,^tjt  1 , the conditional estimates for the mean and covarianceyt+1=Bxt+1+t+1 (2.21)
matrix of the statex^tjt,^tjtthe estimates based on informationxt, based on the informationy 0 ;:::;y (^0) y;:::;t. yt  1. And I denote


The vectorztis dened as the combination of state and observation:zt:= (^264) xt
Based on information up to timet 1, the covarianceyt^37514 ofZtis
We observeyt. The vectorcov(zt) =^264 B^xttjt is normally distributed. We compute thex^1 t B^tjt x^1 tBB^00 +^375
conditional covariance of^tjt=^tjt  1  ^tjt  1 B 0 x(tBgiven^tjt  1 yBt 0 using Equations (2.18, 2.19):+)  (^1) B^tjt  1 (update step)
^xtjt=[=^xItj t  1 ^+tjt ^^1 tBjt ^0 ( 1 BB^^0 (tBjt ^^1 tBjt ^0 + 1 B^0 +) ^1 B) ]^^1 (tyjt t ^1 Bx^tjt  1 ) (2.22)(2.23)
Once we have the posterior distribution given the observationdistribution offollowing conditional mean and covariance matrix:xt+1follows from Equation (2.20).xt+1is Gaussian with theyt, the conditional
^x^tt+1+1jjtt==AA^x^ttjjtt A 10 ++A^tjtB (^0) (B^tjtB 0 (prediction step)+)  (^1) (yt Bx^tjt  1 ) (2.24)(2.25)
The measurement and time update equations above are the whole of the Kalmanproperties: for random vectors (^14) Here and elsewhere in the book (see, for example, FAQ 3.1) we use the following elementary;and a commensurable matrixB,cov(B) =Bcov()B 0
and cov(B;) =Bcov(;). 65


Filter. If we combine Equations (2.22) and (2.24), the covariance matrix evolvesaccording to the equation:
This is called a^t+1jt=ARiccati recursion(^tjt ^1  ^tjt ^1. In steady state the covariance matrix does notB^0 (B^tjt ^1 B^0 +) ^1 B^tjt ^1 )A^0 +
change in consecutive periods:matrix: ^t+1jt=^tjt  1. We can solve for the stationary
This is adiscrete time algebraic Riccati equationX=AXA^0  AXB^0 (BXB^0 +) .^1 BXA^0 +

The matrix Kt:=^tjt  1 B (^0) (B^tjt  1 B (^0) +)  1
is called the optimal Kalman gain. The equations become^tjt=[I KtB]^tjt  1 (2.26)
^x^tt+1+1x^tjjjttt=(==AAI^x ^ttjKjttAtB^0 +)x^tjt ^1 +Ktyt (2.27)(2.28)(2.29)


```
2.4.2. Kalman Filter ExamplesExample 2.1: [Muth, 1960]:
xytt+1+1==xxtt+1++t+1t+1 (2.30)(2.31)
```
The stationary^^ 2 t+1^t (^4) +1jtis given by the solution to the Riccati equation:jt
t+1jt+K^2 ==^^2 t (^2) +1)^t (^2) j+1t^+j^2 tt+1 2 jt=^12 ^2 (1 +p(2)^2 + 1)
where we have introduced the parameterx^t+1jt=(1 K)^xtjt ^1 +Kyt
Loosely, this is a noise-to-signal ratio. It is high when the measurement error:=
is high compared to the typical change of the state per period. Forformula simplies:K' 1 =(+ 1).  1 the
Example 2.2: (AR(1) model): In this model, the state equation isx^tjt=1 +x^tjt ^1 +1 +^1 yt
xt+1=b+axt+t (2.32)


To have a mean-reverting process, introduce a long-term mean valuea relaxation constant > 0 , and set  > 0 and
ab:=1:=  (2.33)(2.34)
Equation(2.32)becomesxt+1=xt (xt ) +t+1

The state reverts to valuestationary distribution of=p 2   (^2). xtwhen it is away from this equilibrium value. Theis Gaussian, with meanand standard deviation
Dene: ut:=xt  (2.35)
We rewrite the equation as vt:=yt  (2.36)
xt+1uu tt+1+1==~=xxatt~x + (t+a+ ( t+11)a ut1)(+xt t+1) +t+1


The state space equations areut+1=aut+t+1
The Riccati equation is vt+1=ut+1+t+1

(1 a^2 )^t^2 +1jt+^ (^2) ta+1)^2 ^jtt^4 +1^+t (^2) +1jt (^2) jt== 12 ^2 (a (^2)  1) (^2) + 2
=^12 +q(a^2 (a ^2  1)1)^2 +^4 +^2 ^4 + 2(a^2 + 1)^2 ^2 
=^12 +q^2 [((aa^22   1)1)^22 + 1+^2 ]^2 + 4^2 ^2 
K=^ (^2) t+1^24 ^^2 t1 +j+1t+jts 2 1 +(a^2  ^2 1)^2 + 1^235
Now replaceu;vusing Equations (2.35) and (2.36):u^t+1jt=(1 K)^utjt ^1 +Kvt
Fora= 1the formula is identical to that of Example 2.1; and it is straight-)^xt+1jt=(1 K)^xtjt ^1 +Kyt
forward to verify that^t^2 +1jtis decreasing in 69 a, and consequently alsoK is


decreasing in1.The EWMA is still an optimal estimator for a mean-reverting model ofvolatility.a. There are two insights to be drawn from this:
2.equal. We discount the past less, because mean-reversion causes volatilityto be more concentrated. When the volatility is changing less from periodIn the presence of mean reversion,K decreases, everything else being
Example 2.3:to period, past observations become more informative.[Harvey and Shephard, 1996]: The generating process for gross
returnsRt=Pt=Pt  1 is assumed to beRt=e +exp(ht=2)t
whereut= exp( is a known constant, andht=2)t. Squareutand take the logarithm to linearize the equation:tN(0;1). Deneut=logRt . Then
logu^2 t==hhtt+ log+t+t^2 

where:=E(logt^2 )'  1 :y (^2703) t= log, andu (^2) t tis a zero-mean random variable. Dene
so that we get an observation equation:=2 logjlogRt ^ j 
yt= 70 ht+t


Now, we posit an evolution equation forht+1=b+haht:t+t
This is the same model as AR(1), from which we obtain an estimateis given by = 1, then the formulas take a simple form:ut'rtand the volatility estimate^ht. If
^t'exp"Xs^1 =0(1 K) s(logjlogRt  1 j )#
2.5. ExercisesExercise 2.1: (15) Prove thatQTt=1(1 +r(t)) 1 =T  1 T  1 PTt=1r(t).
Exercise 2.2:uncorrelated but dependent.(20) Provide an example of two random variables that are
Exercise 2.3:rationale for the lack of correlation from the rst one.(25) Provide a second example, employing an entirely dierent

Exercise 2.4:Exercise 2.5: (15) Derive the formula for(10) Prove that ifE(h (^21) ) is nite, i.e.E(h^21 ) from Equation ( 1 + 1 <??1, then a).
stationary distribution exists, i.e.inequality) E[log( 1 + 1 ^20 )]<0. (Hint: use Jensen's


1. Security returns exhibit heavy tails, low autocorrelation but highThe Takeaways
2. autocorrelation in absolute value or square, and they are approach-ing log-normal returns over longer time intervals.GARCH models capture most properties of returns, and can beused to estimate volatility.
3.4. The GARCH volatility estimates are exponential weighted averagesof non-iid squared returns.State-space models can be used to model a variety of stochasticlinear dynamical systems.
5. They will appear in factor models.


# Chapter 3Linear Models of Returns

## 1. What do we intend for linear models of returns?The Questions

## 2. How do we interpret them?3. What are their applications?

## 
exible, interpretable, perform well in applications, and are supported by theory.Furthermore, they t like a glove with mean-variance optimization and can beLinear models of asset returns are a cornerstone of this book. They are

## also used as a basis for a number of important tasks, like risk management andperformance analysis. It is possible that you, the reader, will nd this classof models inadequate in some way, at some point. But just because you have

## outgrown them, does not mean that you will nd them useless. They will stillenable you to reason about the entire investment process, and some of thetheory will come in handy.


We saw in Chapter 2 how to model univariate returns. A direct extension to3.1. Factor Modelsmultivariate returns would be to model each security's return as an independent
process. This would not be adequate, however, because returns are dependent.It is a natural step to model the common dependency among stocks as beinggenerated by a few common sources of randomness, and then to keep a random

source of per-security randomness that is independent of the factors. The modelfor stock returns is called afactor model (^1) and takes the form:
where: rt=^ +Bft+t (3.1)
 t (^) rt (^2) is anis a random vector ofNdenotes time;n-dimensional vector;nasset returns minus the risk-free rate (see Section
 2.1.2);fBtis the random vector ofis anmloadings matrix;mfactor returns;
If the random vector tis the random vector ofthad a generic distribution, we would have gained nothingnidiosyncratic (or specic) returns.
Recent textbooks treatment on the subject are Rencher and Christensen [2012], Johnson andWichern [2007]. In nance, factor models were rst introduce by Sharpe [1964], Sharpe [1965],and Sharpe [1966] for the one-factor case, which was extended to multiple factors by Ross^1 Factor models go back to the birth of psychometrics at the turn of the XIX Century.
[Ross, 1976]. Good introductions to factor models in nance are the survey papers by Connorand Korajczyk [2010], Fan et al. [2016] and the books Connor et al. [2010] and Connor andKorajczyk [2010], MacKinlay [1995].


in tractability. Instead, we assume that i) The vectorfrom the factor returns (^) ;t:=var(t) be diagonal, or at least sparse in some sense. Often, modelsfsfor alls; ii)E[t] = 0; iii) the covariance matrixtis be independent
componentwith a diagonal covariance matrix are calledcovariance matrix are calledof returns. approximate. The vectorstrictand models with a sparsetis theidiosyncratic
We assume that the pair (at least with a slowly-varying distribution, and thatWe usually refer to the termft;Bft) be identically distributed across periods ortas thesystematic component of asset returnsftandtbe independent.
for each (^)  2 Rntn. I denote covariance matrices ofrespectively. With this notation, the covariance matrix of assets isftandtwith (^) f 2 Rmm and 2
This decomposition is at the core of volatility modeling with linear returns and^ r=B
fB^0 +^  (3.2)
the subject of Chapters 6 and 7.FAQ 3.1:Why is the covariance matrix (^) r=B
fB (^0) + (^) ?
The covariance matrixThe factor term is a linear transformation ofthe termstorwith covarianceBftandtare independent, so that (^) ,rcovdoes not depend on the intercept(B) =B
B (^0) , because [ft. For any random vec- (^) r =covcov(Bf(Bt (^) ) +)], andi;j (^) =.
cov(Pk[B]i;kk;P`[B]j;``) =Pk;`[B]i;k[ (^) ]k;`[B]j;`= [B
B^0 ]i;j.
2 In this chapter we set aside the very important issue of estimating theIf this formula is not familiar to you, derive it, maybe using a single-factor model rst.


interpretationsparameters of Equation (3.1) from data, and focus instead on its usage andinterpretation. Here is the plan for the next few sections. First, we review theof Equation (3.1), of which there are three:

1. as a graphical model;2. as the superposition of low-dimensional cross-sectional return vectors;3. as the overlap of the factor return vector with the asset loadings vector.
Secondly, we review theThere are three of those too:1. Rotations; transformationsthat can be operated on factor models.
These mathematical operations are versatile tools in the hand of the quantitative2. Projections;3. Push-outs.
manager to reformulate, simplify or extend a model.Lastly, we describe the uses of factor models. There are quite a few:1. Forecast andDecomposevolatility, so that we can separate wanted vs
2. Be a fundamental input to3. unwanted risk;Understandperformance and separate skill from luck;Portfolio Construction;
4. Serve as a foundation foralpha research.
3.2. Interpretations of Factor ModelsBefore we start interpreting, let us make factor model more concrete withan example. In Figure 3.1 you see a \typical" loading matrix used in a risk


```
-2.39-1.520.12-1.91-3.00... .........
... ... ...
```
```
010 001 100 .........
...^0 ...^0 ...^0 ......
```
```
001 100 000 010 .........
... ... ... ......
```
style country industry

Figure 3.1:factor (sometimes termed \country" factor). The loadings are all ones, and theintercept factor contribution to total returns is the same for all assets. The other styleloadings often are standardized. The country and industry loadings take values equalA typical loadings matrix. The style loadings comprise an \intercept"

to 1 if the asset belongs to the country or industry.model. A few columns containstyleloadings (^3). Other columns consisting of
"biotechnology company", and so on. A stock will have a \1" loading if itdummy variables indicating whether the stock belongs to a particular industry.There may be a column for \energy explorers and producers", a column for
belongs to the industry, 0, otherwise. Finally there are columns consisting ofdummy variables denoting country classication, similarly to industry. Whenthe factor return for a country or an industry is high, it will move all the stocks
in the industry. The factor structure captures comovement among stocks withcertain obvious commonalities, as well as less obvious ones.Even though Equation (3.1) is older than modern Statistics (having really
styles.^3 The use of the term \style" will be clear later, when we associate to loadings investment 77


originated in the unpublished work of Gauss), it is surprisingly rich in meaning,and possibly even richer when used in nancial applications. First, let's reviewsome interpretations of the equation.

3.2.1. Graphical ModelThe rst one is as a graphical modelequation holds (^5) : (^4). Sincer  =Bf, for each assetithis
Each of the many asset returns is dependent on all, or some of, the few factorE(ri ^ ijf) =Xj [B]i;jfj
Asset Returns
LoadingsFactor Returns
Figure 3.2:returns. In a typical regional risk model (say, America, Asia, or Europe) weFactor models as graphical models.
Learning [Bishop, 2006, Murphy, 2012], and survey papers [Models, 2004].ofB^45 Graphical models are covered in monographies [Lauritzen, 1996], books on MachineHere, and in the rest of the book, we use these notational conventions: [on theith row andjth column; [B]i;and [B];jvectors corresponding to theB]i;jis elementith row
andjth columns ofBrespectively. 78


have up to 10,000 assets and up to 100 factors. In Figure 3.2 we show therelationship visually. A few factors (in green) determine the expected assetreturns in excess of (in yellow), though the link provided by loadingsB(in
grey). When the matrixBis sparse, the corresponding graph is sparse.
3.2.2. Superposition of EectsThe second interpretation is as an overlap of in
uences on asset returns. a modelfor the cross-section of returns, i.e., the vector of returns at a given point in
time. Let [as B];jbe thejth column of the matrixB. We rewriteE(r  ) =Bf
The expected excess return vector is the overlap of a small number of vectors (theE(r ^ jf) =Xj [B];jfj
loadings [clear that the factor component of the cross-section lives in a low-dimensionalspace. This is shown in Figure 3.3.B]:;jfor a specic factor), weighted by the factor return. This makes
3.2.3. Single-Asset ProductThe last interpretation applies to single assets. The expected return of an assetgiven the factor returns is equal to the scalar product of the asset loadings and

the vector of factor returns.E(ri  (^) ijf) =h[B]i;;fi


```
B・, 2
B・, 1
```
```
Asset Returns
= B・, 1f・, 1+ B・, 2f・, 2
```
While this formula is rarely used at the asset level, it does show up all the timeFigure 3.3:Factor models as superposition of weighted factor loadings.

when we apply it to portfolios. Consider a portfolionet notional valuethe number of shares held long or short. The expected PnL of the portfolio is (^6) invested in asseti; for stocks, this is the stock price timesw 2 Rn, wherewiis the
E w^0 r^ f) ==EXi^ [X ii+wihr[iB^ f]i;!fi]wi
We can explain the factor PnL of a portfolio in terms of a scalar product; withinthe scalar product identify the largest contributor, the degree of dispersion ofPnL among the factors, and so on. This is the jump-o point forperformance
attribution(numeraire). (^6) Net Notional Value is the amount invested in the security in the reference currency, which we'll cover extensively later in the book.


B 1,・

B 3,・
B 2,・
〈f, B 2,・〉〈f, B 3,・〉 〈f, B 1,f・〉
Figure 3.4:3.3. Alpha Spanned and Alpha Orthog-Factor models as scalar products of per-stock loadings and factor returns.

Consider the factor equationonal
whereftare iid with nite mean and variance, andrt=^ +Bft+t tare iid (independent on

fthe orthogonal complement:t) with zero unconditional mean and nite variance.Decompose as the sum of its projection on the column subspace of =B+ (^) ?. By construction it isB (^0) ?= 0. SoBand
we haveis an indeterminacy in the factor model. You can rewrite the model asrt= (^) ?+B(+ft) +t. In this relationship, you can see that there
The \alpha" spanned by the columns ofrt=^ ?+B[+E(ftB)] +is indistinguishable from the expectedB[ft E(ft)] +t


returns of the factors. However, the termhow you split the contribution of the two. In the following, we setsetf:=E[ft]. (^) k:=B[+E(ft)] is independent of= 0 and
alpha position themselvesNow, for a little prestige: if you choose as a portfolio proportional to the
its payo is w=k^ ??k
w^0 rt==kk (^1) ??kk (^) +^0 ?kr t (^0) ??kt
The expected return and variance of this portfolio areE(w (^0) rt) =k (^) ?k
There is an upper bound for the variance, given by the operator norm:var(w^0 rt) =^ k^0?^ ?k^2?
So that^ k^0?^ ?k^2 ?k^ k^22
In the case of a diagonal matrix,kSR (^) k^22 is the largest asset idiosyncratic variance.kk^ ?kk^2
Assume that it is upper bounded for all 82 n. This has interesting implications.


Consider the case, for example, where the average absolute orthogonal returnper asset is positive:use the simple inequality between 1-norm and Euclidean norm:Pij[ (^) ?]ij=n= >0 or, equivalently,k (^) k?xkk 11 npn. Nowkxk 2.
Hencestrategy, and we have a lower bound on the Sharpe Ratio:k (^) ?k 2 pn. Apply this to the Sharpe Ratio of the alpha orthogonal
Let's summarize the assumptions we made so far, besides the fact that theSR(w)kk^ ?kk^2 pnk^ k^2 (3.3)
factor model is correct. We assumed that:1. the largest idiosyncratic varianceassets. (^7) is uniformly bounded in the number of
If that is the case, we have a lower bound on the Sharpe Strategy of a portfolio.2. the average absolute value of the coordinate of.^ ?is bounded below by
And if these bounds are uniform for increasing valuessequence of Sharpe Ratios going to innity! This is highly unlikely in real life,so one of the assumptions we made { factor model, bound on idio variances,^8 ofn, then we have a
that the factor model is correctbound on orthogonal expected returns { must not hold.variances holds in practice. This leaves us with the fact that the idio orthogonal, it appears that the assumption of nite idioUnder the assumption
expected returns are vanishing in (^78) Or, more generally, the largest eigenvalue of the sparse matrixEconomists reason in terms of \increasing" economies as a function of the tradable assets.n. Let us summarize this result in concrete (^) r.
I believe there is not much to gain from this level of abstraction, so I keep the exposition andthe inequalities in nite dimensions.


terms:\spanned" or \orthogonal".If a linear model is a good approximation of returns, then alpha is either
 \Alpha orthogonal" is extremely valuable: if you have positive expectedalpha at the asset level, then your Sharpe increases at the raterate that arises when you can diversify risk without giving up on returns.pn, a typical
 But Sharpe does not approach innity in the real world, so you can expectthe orthogonal alpha of an asset to be small.There are excess returns, but they are more likely to come from \alpha
spanned". This alpha as we will see in the next chapter comes with risk thatdoes not diversify away with a large number of assets.
3.4. Transformations3.4.1. Rotations
A factor model is not uniquely identied. Letand dene Cbe anmminvertible matrix,
B~~f==BCCf ^1
the columns ofB~ span the same subspace as the columns ofr= +B~~f+ B. The model


indeterminacyhas the same returns as the original model. This is usually termedThe covariance matrix of the transformed factors isof the factor model. ~f=C
fCrotational (^0). There
will be several applications of rotational indeterminacy in the book. Rotationsenable us to provide nal users with dierentplore the impact on factor returns of factor transformations for three instructiveviewsof the same model. We ex-
examples: unit factor covariance, orthonormal loadings and z-scored loadings. Identity factor covariance matrix. Sometimes, users of a model would like to
see uncorrelated factors returns with unit variances. Under this perspective,exposures of the portfolio can be interpreted directly as factor volatilities,and factor risk of a portfolio is the sum of the squared exposures, without
covariance terms.This risk model perspective can be obtained by taking the Singular ValueDecomposition (SVD) of (^) f=USU (^0) and then settingC:=S  1 = (^2) U (^0). It
follows that ~f=C
fC (^0) =S  1 = (^2) U (^0) USU (^0) US  1 = (^2) =I
(but not unit variance, since the column may have non-zero mean), and isOrthonormal loadingsorthonormalB~ (^0) B~=I. We can also choose a rotation so that the loadings arem. This means that each column ofB~ has unit norm
 orthogonal to the other. In this case the transformation iswhereZ-scored loadingsVandScome from the SVD of. The z-scoring of factor loadings is a common procedure. ItB=USV^0. We getB~C= ^1 U:=. VS ^1 ,
consists of a linear rescaling of the loadings of one or more factors, so that 85


the new loadings have zero mean and unit variance (since they are zero-mean,they have also unit squared norm). The benet of the transformation is thatit makes the loadings easier to interpret. Is the stock more exposed than
the average to the factor, and by how much? What is the average portfolioexposure to the factor on a standardized basis? Is such a linear transforma-
FAQ 3.2:Z-scoring the loadings of a model will result in a model that makes thesame predictions as the original model with raw loadings only if theIs z-scoring factor loadings changing a factor model?
\country" factor (or \intercept" factor) is among the original factors. Ifunit vector (1loadings vectors of the original model. A special case is the one where thethat is not the case, z-scoring factors will result in a model that produces;^1 ;:::;1) can be expressed as a linear combination of the
dierent risk forecasts and performance attributions.
tion resulting in an equivalent factor model? It is possible to multiply theloadings of factorwhich is always invertible. However, in general it is not possible to center theiby constanti: just considerC:=diag   11 ;:::; m 1 ,

loadings (You can try to nd a counterexample in Exercise 3.3). However,assume that the unit vector is in the subspace spanned by the loadingscolumns, i.e., there is a vectora 2 Rm such that (^9) e=Ba. In this case,
the centering is possible. If we want to add constantsthentransformation isB~=B+ediag ()=B+Badiag ()=B(Im+adiag (ito the loadings,)), hence our
(^9) We use the notatione:= (1; 1 C;:::; ^1 1).=Im+adiag () (3.4)


This assumption is veried in two common cases. The rst one is the use ofa \market" factor, to which all assets are identically exposed. The loadingsvector is theneby construction. The second case is when there are country
or industry loadings, such that for each asset the sum of the loadings acrossindustries is exactly one. In this casepositions corresponding to the industry factors, and zero otherwise.e=Bafor a vectorathat has ones in
3.4.2. ProjectionsOn occasion, we may want to use a risk model withto the original one. At rst glance, this operation may seem unjustied. If wefewerfactors compared
trust that our risk model is the most accurate, why would we want to replaceit with a dierent one? The reasons are many. For example, it may be the casethat in practice the loadings of one or more factors are changing so fast as to
make portfolio management and hedging dicult. Another reason is that weare using a vendor-provided model, and that we believe that the model is notperfect, i.e., some factors do not quite belong to the model. A third reason
may be that we want to give to a nal user a \simplied" risk model that is asaccurate as possible, while retaining the full model for other uses. For thesereasons and more, we face to nd a dierent risk model that is close, in some

sense, to the original one.B
We have a modelfB (^0) + (^) , but we want to employ a dierent exposure matrixr= +Bf+and associated covariance matrixA, in which the (^) r=
range ofthe covariance matrix would beresulting in the best approximation to our original model? Let the distanceAis contained in the range of (^) r=B. If we model returns asA
gA (^0) + (^) . What is the valuer= +Ag+ g,


between the original factor returnskwhereBf HAg:= (k (^2). The distance-minimizing approximate factor returns areA (^0) A)  (^1) A (^0) B. The corresponding value offand the approximate factor returns (^) gis g=gHfbe,
The factor component of asset returns is^ g:=H
BffH. We solve^0
from whichg= (A^0 A) ^1 A^0 Bfmin=gHfkBf. The corresponding covariance matrix is Agk^2
(^) aregWe call these transformations projections because, like projections, they=idempotentH
fH^0 .. An idempotent linear operatoris such that (^2) x=x.
The geometric intuition is that, once you have projected a vector on a plane,projecting the resulting vector again on the same plane does not result in anothervector, since the input vector is already on the plane. Similarly, consider the
\projection" of the model using the matrixAbecomes (. If you project once again using the same matrixA (^0) A)  (^1) A (^0) A, i.e., the identity. The transformed covariance matrix isA. The new loadings matrix is nowA, the transformationH
unchanged.
3.4.3. Push-OutsIn the previous two sections we introduced a transformation that preserves thenumber of factors and a transformation that reduces it. The last section focuses
on a transformation thatincreases the number of factors. We therefore lift 88


```
the loadings matrix into a new one, whose column space contains the columnspace of the old one. Why could this be of interest? A possible scenario thatoccurs in practice is that that our factor model may have been developed on
historical data that are not representative of the current regime. As a result,the idiosyncratic returns show some structure, in the sense that they themselvesare amenable to be formulated as a dierent factor model:
withA 2 Rnp,ga rv taking values in=AgRp+and a rv taking values inRn. The
```
new model becomes r= (^) ?+Bf+Ag+ (3.5)
Withthatmodied. Assume thatA (^0) Buncorrelated from= 0. If not, the factor returns of the original model would have to beB (^0) Af;g 6 = 0. Then we can decompose the columns of. In the specication of the model (3.5), we requireAinto
the sum of parallel and orthogonal components. In matrix terms,for someasr=B(Cf+ 2 RCgm) +p. It follows that the modelHg+. r=Bf+Ag+can be writtenA=BC+H,
^0 (Bf+Ag^00 AgBf) = 0= 0= 0 (original model orthogonality condition)(residual model orthogonality condition)(nal model orthogonality condition)
From the second and the third equality it follows thatequality can be rewritten as 0 = (g (^0) A (^0) + (^0) )Bf=g (^0) A (^0) Bffor all realization of^0 Bf = 0; the rst


```
frisk model in a characteristic-model framework.;g, henceA^0 B= 0. In the estimation chapter we will see how to augment a
3.5. Applications3.5.1. Performance Attribution
```
What is the PnL of a portfolio at time(portfolio PnLt)=wt (^0) rt t?
==wb (^0) tt^0 fBft+t+w (^0) tw( 0 t(? (^) +?+t)t) (bt:=B (^0) wt)
The vectorterm [by the portfolio holdings; keep in mind that the characteristics and the weightsbt]iis the sum of the characteristics of factorbt 2 Rmare thefactor exposuresof the portfolio at timeiof each stock, weightedt. The
can both be negative. The termthe term is the idiosyncratic PnL. Summing up over a time interval [1the PnL of a strategy is b^0 tftis the factor PnL in time interval;:::;Tt, while],
PnL = Factor PnL + Residual PnL


We can also distribute the sum dierently:PnL =XT

=Xtt=1=1T (Factor PnLXjm=1[bt]j[ft]j+t)Xt+=1T(Residual PnLXi=1n[wt]i( (^) ?;i+ [t) t]i)
And then, of course, one can partition factors and stocks in groups, to highlight,=Xjm=1(FactorjPnL)+Xi=1n (StockiResidual PnL)
for example the performance arising from style factors, from industry factors,or from a specic group of stocks.
3.5.2. Risk Management: Forecast and Decom-position
If we have a covariance matrix (not specically from a factor model), thevariance of a portfolioPi;jwivar(ri;rj)wj=ww 0 is easy to compute: (^) rw. We can apply this to formula to a covariancevar(r (^0) w) =Pi;jvar(riwi;rjwj) =
matrix associated to a factor model:var(r (^0) w) =w (^0) (B
fB (^0) + (^) )w
The formula has two applications. The rst one is an estimate of a portfolio's=b^0 fb+w^0 w ex
antefor risk managers, since they monitor volatility and allocate risk based on thismeasure. The second application is the decomposition of variance in factorvolatility at any point in time. This is an important piece for information


and idiosyncratic components. Like in the attribution case, the formula is ajumping-o point. For example, a commonly quoted statistic for a strategy is thepercentage of idio variance, dened as 100*(dollar idio variance)/(total variance);
the percentage of idio variance and factor variance sum to 100, of course. Thefactor variance can be decomposed further by making factor partitions. Themost detailed one has each factor being a singleton, but very common choices are
(style group)/(industry group)/(country group), or (subsectors group)/(stylegroup)/(country group). This measure, and the associated sensitivities, arecommonly used to monitor strategies. Every partition, either of factors or of
assets, induces a covariance matrixbetween partition groupexposureb, and we partition the factors into groups 1iandj. For example, say that a portfolio has factor 
2 Rppwhere [ ]i;j;:::;pis the covariance, with group
iexposures where all the terms not incovariance matrix of the sets' returns:containing the subset of elementsSS(i() are set equal to zero. Denei). DenebS(i) as a vector of factor as the

=^266664 bb^0 S (^0) S(1)(p)^ :::ffbbSS(1)(1) ::::::::: bb^0 S (^0) S(1)(p)^ :::ffbbSS((pp))^377775
Then the total factor variance isgroup'sivariance isv (^2) i:=b (^0) S(i) (^) fvbTOT^2 S(i).:=e^0 
e, wheree:= (1 :::1)^0. The


 Fraction of total variancepi:=(variance of groupfor group(portfolio variance)i+ half of covariance contributions)iis

==Pcov(vj (^2) TOT[^ vrTOT 2 i];i;jrTOT)
So thatP=ip^ ii= 1. The percentage of variance of a groupS(i) (again, this
 includes single factors and single assets{perhaps the most commonly usedpartition!) is simply the beta of returns of the group to the overall portfolio.Marginal contribution to risk(MCR) of a groupS(i) is dened as
mi:==(portfolio@(x@ivi)px$ 0 vol change when we buy
x (^) x=e $1M $1M vol of setS(i))
==viiv^1 TOTXj [ ]i;j
 Sharpe Ratio sensitivity=vTOTvi pi. It is also useful to compute the sensitivity of the
Sharpe Ratio to changes in volatility of a group. The Total Portfolio'sSharpe


```
Ratio Sensitivity@x@ivol(E(PnLPnL))with respect to volatility increase of group=vol(PnL)@iE(PnLvar() PnL@ivol() PnL)Ei(is given byPnL)
==vol(SRvTOTTOTPnL)SRSR@TOTiEi (PnL mvar()i PnLmi)SRTOTvol(PnL)
The contribution to total Sharpe Ratio is positive if the Sharpe Ratio of agroup exceeds a threshold, which is its marginal contribution to risk.
```
When we rotate a factor model, we transform the factor loadings andFAQ 3.3:factor covariance matrix asDo model rotations aect risk decompositions?B~ =BC  (^1) and ~f=C
fC (^0) respectively.
(The total factor variance is unchanged. The total (and single-asset) idiovariance is unchanged too, as it does not depend on rotations. However,In the rotated model, the factor exposures of portfolioC^0 ) ^1 b, and the factor risk is~b^0 ~fb~=b^0 C ^1 (C
fC^0 )(wCare^0 ) ^1 b~b==B~b^00 w (^) f=b.
the single-factor risk variance is aected by rotations. Rather than beinga drawback, this is a plus. It aords us the 
exibility to attribute riskto factor groups that are more meaningful (e.g., more intuitive) thanothers.
3.5.3. Portfolio ManagementFactor models are useful for portfolio management in more than one way. Therst one is adjacent to risk management: volatility is the common language
spoken by risk managers and portfolio managers, and it is oftentimes generatedby a factor model. The second one is the inverse of the covariance matrix


FAQ 3.4:preliminary question. Given a time series of returnsBefore delving in the details of factor model estimation, we address aWhy not use the empirical covariance matrix?rtwith population

covariance matrix 
r, its simplest estimator is the empirical covariance ^r=T 1 Xt=1T rtr (^0) t
we can writeor, if we denotethat the estimate maximizes log likelihood (for a normal multivariatedistribution), is asymptotically consistent, and a Central Limit Theorem ^r=RT^2  ^1 RRRnT^0. It is well known (and easy to establish)the matrix of returns wherert = R;t,
is available for it [Anderson, 1963]. Why not use this as our estimate forour covariance matrix? The reason is that, whenis very inadequate for volatility estimation and portfolio optimizationpurposes. The covariance matrix has at most rankTT. letwni, the estimator;i= 1;:::;T 
volatility. The situation is even worse in portfolio optimization. Thenthese vectors as portfolios. The volatility of portfolioT a basis for the null space of^1 kR^0 wik = 0. So, a majority of independent portfolios has zeroR^0 , i.e.,R^0 wi = 0. We can interpretiiswi^0 ^rwi=
wsolution of the mean-variance problemundened. Choosing an alpha close to the null space yields an arbitrarilylarge portfolio, and an arbitrarily large Sharpe Ratio.=  r^1. In this case, if is in the null space, the portfolio ismaxw[^0  (2) ^1 w^0 ^rw] is


also known asoptimization. As discussed in FAQ 3.4, the empirical covariance matrix isusually not invertible. The factor structure makes possible to estimate bothprecision matrix. This matrix plays a central role in portfolio (^) r
andterms:classes of expected returns. This makes sense intuitively, since the factor-based  r 1. The third is the model of the expected asset returns as the sum of twoandB (^0) E(f). These two terms give rise to two qualitatively dierent
returns come with some variability and risk, which is itself captured by thefactor covariance matrixno risk. How to manage these sources of returns is the concern of Portfolio (^) f. The alpha term, instead, comes with apparently
Management. Lastly, a factor model isproduces factor exposures, risk and performance decompositions, as discussedabove. This makes the job of the portfolio managers easier, since it enableslegible: when applied to a portfolio, it
(after the trade) their strategies.them to plan (before the trade), monitor (during the trade) and understand
3.5.4. Alpha ResearchAs volatility is theso alpha is what a signal researcher and a portfolio manager both understand.lingua francaspoken by risk managers and portfolio managers,
At the cost of excessive generalization, one could say that the signal researchercares abouttrading costs and tries to combine all these terms into a protable strategy. In , the risk manager cares aboutBfand the portfolio manager adds
reality, there is \risky" alpha worth trading inloosely for the time being, with the goal of tightening it in coming chapters.Furthermore, sometimes these people are one and the same, although the rolesBf{again, I use the language
are increasingly separated in suciently large and complex strategies. Alpha 96


research is improved by factor models in two ways. First,and for a certain class of investors it is the only thing that mattersresearchers focusing on , the factor-based approach helps separate the twoBfis important, (^10). For
source of expected returns: priced factors and unpriced factors.
(3.1)3.6. Factor Models TypesThe fundamental model we use from here on is the factor model of Equation. We have taken the model for granted. But where the data and parameters
of the model come from? In the case of factor models, the answer is especiallyimportant, because the meaning attached to the various symbols matters.Practitioners use three broad approaches to identify the all the parameters in
the equation: Characteristic Modelthe model are the time series: this is the most common approach. The input data tor
estimated from these data. We deneavailable (^11) at the beginning of the interval [tandBBt. Factor and idiosyncratic returns aretas a matrix oft  1 ;t]. The intuition is thatasset characteristics
 these characteristics are partially responsible for the stock return. I coverthis in Chapter 6.Statistical Model: in this model, the only primitive isrt, andBt,ftandt
 10 are all estimated. I cover this in Chapter 7.Macroeconomic Model: in this approach, the primitives arertandft, andBt
that the the time index for the loadings is not o by one. Most vendors use the timestampfor data available at the end of the interval [^11 A marketing term used for this investment style isImportant: when using commercial data, always check the data specication to make suret  1 ;t]. smart beta. t


The relevant methodological issues the modeler must address are:andseries.tare estimated.ftusually represents a vector of macroeconomic time

1. What are the best loss functions to rank a model?2. Once we have estimates (or primitive data) about factor and idiosyncraticreturns, how do we estimate the covariance matrices from cross-sectional
3. What is the best approach within each framework?4. estimates?How do we select the best model, without optimizing for noise, or data
    mining?
3.7.3.7.1. Linear Regression?Appendix

Linear models are by far the most important class of models in Statistics.There are more books on the subject than citizens of the sovereign state of theVatican (^12). In fact, one could argue there is so much material on linear models,
that two humans on planet Earth may have completely interpretations of them.In order to have some common ground, I will describe the salient aspects someless-well know aspects which will be needed later. Our setting is as follows. We
are given a pair (a random vector taking values in 12 y;x), whereyis a random variable taking values inRm.yandx;yandxare in general dependentRandxis
the \Probability and Statistics" section with \regression" in their title or subject, the vastmajority of them covering linear models.Not a joke: as of October 2017, the Vatican has 842 citizens; Amazon lists 1,392 books in


random variables: knowing the value of a realization ofabout the values ofwe want to provide a forecast ofyand this makes the problem innitely interesting. Say thaty, which we denote^y(xx). One way to selecttells us something
such forecast is to try to minimize a loss function; we should pay a price forbeing wrong. One natural choice of loss is the quadratic loss: it is nonnegative;it is symmetric; it is dierentiable; and it penalizes more for large errors. The

problem we face is miny^ E[(^y(x) y) (^2) jx] (3.6)
One basic result in statisticsfunction that minimizes this expectation is the conditional expectation ofgivenx. We introduce a new variable^13 and in control theory is that, if: E(y^2 )< 1 , they
It follows thatE() =E(y) yE(=EE(y(jyxj)) =x) +E(y) E(y) = 0. Then use the(3.7)
chain the following chain:E[(^y(x) y) (^2) jx] =E[(^y(x) E(yjx) +E(yjx) y) (^2) jx]
==EEE[[[^222 jjjxxx] +] +] EE[(^[(^yy  EE((yyjjxx))^22 jjxx]]  2 E[jx](y E(yjx))
detail, Wasserman [2004], Hastie et al. [2008], Johnson and Wichern [2007], Harrell [2015],Gelman et al. [2022], Hansen [2022].^13 Linear regression is an inexhaustible topic. Some useful references are, in order of increasing


The equality holds only if ^E[ (^2) jx] 2 E(y (^2) ) + 2y=E[EE((yyjjxx). The term) (^2) ] E[^2 jx] is nite, because
=4< 21 EE((yy^22 ) + 2) E[E(y^2 jx)] (Iterated Expectation)(Jensen)
In applications, we haveythe^=gempirical(x;) wheresquared lossis a nite- or innite-dimensional vector. We then minimizensamples (n  1 Pi(yyii;x i) and we choose a functional form forg(x;)) (^2). The simplest form ofgis
linear:g(x; ) =Pi (^) ixi. In matrix form, Equation (3.7) becomesy=X + (3.8)
whereof observations, and the \features". we want to estimate the parametersestimates fory 2 Rn,XX. We then minimize the empirical loss 2 Rnm, 2 Rm. The integersnandmdenote the number , and
which is equal to the unweighted sum of squared errors (min^ ky X^ k^2 Ordinary Least Squares(3.9),
or OLS) (to posit that the true model is Equation (3.8), and to further assume thatN(0;yi 2  InP). If we xj[X]i;j (^) j)^2. A dierent way to arrive at the same problem is, we have=y X ; and since we know the
distribution ofchoose the parameterproblem as Equation (3.9). The choice of maximizing the likelihood is called, we can associate to a choice of to maximize the likelihood, we end up solving the same alikelihood f(j ). If we


the Maximum Likelihood Principlecan interpret the setFinally there is a geometrical interpretation for the regression problem. YouS:=fX j 214 R.mgas a subspace ofRn. The columns of
Xpointof a projection ofare a (generally non-orthonormal) basis of the subspace. We are then given ay 2 Rand nd the pointyonS. The projection is a linear operator. The minimumy^ 2 Sthat is closest toy. This is the denition 15

is attained at ^= (X (^0) X)  (^1) X (^0) y (3.10)
and the estimatesy^:=E(yj (^) ^y) are=X ^
The matrixH=X(X^0 X) ^1 X^0 =is called theX(X^0 X) ^1 Xhat matrix^0 y orprojection matrix(3.11).
The estimated residuals are
Intuitively, the optimal estimates should not change if we change the base of^= (I H)y
the subspace. To see this rigorously, transformis non-singular. The transformed set of predictors spans the same subspace as 14 XintoXQ, whereQ 2 Rmm
independent. In Chapter 6 we will encounter cases of rank-decient matrices.^15 For a detailed discussion of the MLP, see Robert [2007].The minimum is unique if the rank ofXism, i.e., if all the columns ofXare linearly


X. Then ^y=XQ((XQ) (^0) XQ)  (^1) (XQ) (^0) y
===XQXQQX(X(Q (^0) X ^01 X)( X^01 xQX (^0) X 0 )y)  ^11 Q(Q^0 X (^0) )^0  y (^1) Q (^0) X (^0) y (3.12)
henceprocess on the estimateAnother property of the estimateyis independent of base representation.^y, we obtain again^yis that, if we iterate the estimationy^. This also has geometric interpre-
tation. Once a point has been projected on a hyperplane, the projection of theprojection is unchanged. In algebraic terms,Here is another facet of linear regression tying geometric and algebraicHy^=H (^2) y=Hy=y^.
interpretations of linear regression. DecomposeUis an orthonormal basis for the column subspace ofxusing the SVD:x. Then x=UV^0.
^y==UVUU (^0) y^0 (VU^0 UV^0 ) ^1 VU^0 y
SoyReplace Equation (3.8) in beta estimation formula (3.10) to obtainis projected on the column space ofU.
^=(= X+ (^0 XX)  (^01) XX)^0  (X (^1) X (^0) +:)
The estimate of beta is unbiased, because 102 E[(X^0 X) ^1 X^0 ] = 0; and the covari-


ance matrix of ^is var( ^) = (^2) (X (^0) X)  (^1) (3.13)
Similarly, var(^y) = (^2) X(X (^0) X)  (^1) X 0
We can write these formulas using the SVD:var( ^) = (^2) V  (^2) V (^0) (3.14)
The variance of the estimatesvar(var^y) =( ^) becomes larger as the columns of^2 UU^0 (3.15)X
become more collinear. In our interpretation of the matrixwe include factors that overlap heavily with pre-existing factors.The estimation formulas extend directly to the case ofheteroskedastic noiseX, this occurs when.
In this case we assume thatsymmetric matrix. The estimates forfrom the previous formulas, by left-multiplying by N(0 ^;, (^) y^and), wherevar (  ^ 1
 ) can be derived directly= 2 both sides of Equationis a positive denite
(3.8):   1 = (^2) y=   1 = (^2) X +   1 = (^2) 
Notice that theso that the noise is homoskedastic; and we apply the OLS results to obtain  ^1 =^2 is distributed according to a standard normal (exercise),


Weighted Least Squares(WLS) formulas: ^=(X 0
   (^1) X)  (^1) X 0
   (^1) y (3.16)
var( ^^y) =(=XX(^0 X 
0   
1  X 1 )X )^1   (^1) X 0
   (^1) y (3.17)(3.18)
Exercise 3.1:there is a unit-norm vector1. Show that(15) If a matrixu (^0) (X (^0) X)u=uhsuch that. X 2 RknXumkhas near collinear columns, then (^2) =hfor some small positiveh.
2. Let3. From this, show thatibe the eigenvalues ofPivar(X ^^0 iX) 2. Show that minmaxi i (^2)  1 i=h^2 i=khXu. k  (^2).
3.7.2. Linear Regression DecompositionSplit Equation (3.8) into two parts:
where we have partitioned the predictorsy=X^1 X^2 ^264 X^ into two blocks. Equation^12375 + (3.19)(3.10)
can be rewritten by using block matrices forfor the inverse of block matrices, in order to obtainthat the coecient ^ 2 can be estimated by a two-step process. First, regressX^0 Xand ^ 1 X, ^^0 y 2 , and the formula. It can be shown
the columns ofThe matrixare orthogonal to the columns ofX~ 2 Xcontains the components of the column vectors of 2 on those ofX 1 :XX 12 (we say that=X 1
 +X~ 2 , where (X~ 2 is the projection on theX 2  X 1
 )X^0 X~ 22 that= 0.
orthogonal complementof the subspace spanned 104 X 1 ). The subspace spanned by


[prove it). Therefore, the estimatesSecond, regressX 1 jX~ 2 ] is the same as the subspace spanned by [yonX~ 2 : y^and^in EquationX 1 jX 2 ] (if you do not see it,(3.19)are unchanged.
It can be proven (see, e.g., Hansen [2022], Ch. 2.23; or prove it yourself as any=X~^23 +
exercise) that least-squared coecient of this regression is the same as ^ 3 = ^ 2. ^ 2 , i.e.
3.7.3. The Frisch-Waugh-Lovell TheoremLet us continue along the line of reasoning of the previous section, where wecharacterized groups of regressors, as in Equation(3.19). As we did above, we
remove from the columns ofand denote the resulting matrixHowever, this transformation enables us to perform regressions in consecutiveX 2 the component collinear to the columns ofX~ 2. X 1
stages, where each stage solves a stand-alone linear estimation problem. Thisinsight is formalized in the following theorem.
Theorem 3.1(Frisch-Waugh-Lovell)y=X 11 +:X~ 2 Denote the reference model 2 + (3.20)
whose estimated parameters areEstimate the system in stages. The rst stage model is ^ 1 ; ^ 2 ;^.
y=X 1
1 + 1 (3.21)


The second-stage model usesfrom which we get estimates^ ^^^11 ;from the rst stage:^^1.
from which we get estimates ^ 2 ^;^1 ^ 2 =. The following identities hold:X~^2
2 +^2 (3.22)

^^^ 122 === (^) ^^^ (^12)
is a projection, i.e.,the solutions forProof. We use the hat matrix of ^ 1 ;H ^ 22. We use the property that=Hand (InX ^1 H,H)^2 ==XIn^1  (XXH^0101 X. First, we characterizeX~^12 ) =^1 XX^0101. The operator(In H)X 2 =
(X X)X 2 = 0. y=X 1 X~ 2  (^2641)
(^264) ^^ 1 2 375 +
(^2) ^^^37512 ==(=(^264 XX~ 0102 XX~XX~^0102 XX 12 ))^11    (^11) XX~XX~ (^01020102) yyXX~~^22375  ^1264 XX~^0102375 y


Now, let us write the outputs ^^ 11 ;X=(~ (^2) Iof the rst stage:n H)y
Those are used to generate ^ 1 X;~^ 
22. We show that they are identical to=(In H)X^2 ^ 1 ; ^ 2.
^ (^) ^ 
12 =(==( ^XX~ 10102 XX~ 12 ))  ^11 XX~^0102 y^ 1
=(=(= ^XX~ 20202 (X~In 2 )   1 HX~) (^022) yX 2 ) ^1 X^02 (In H)y
The equality ofthe section with two remarks. In Section 3.7.2 we showed that Equation^ 2 and^follows from Equations (3.20, 3.21, 3.22). We close(3.22)yields the same estimate as
the regression on the total returns, i.e. that the coecient estimated usingmeans that, after orthogonalizing the independent variable, we have the^ 1 =X~ 2
2 + 2 andr=X~ 23 +give identical estimates:^ 
2 = ^ 3. This
 option of regressing directly on the total return. However, the estimatedresidualsThe formulas above hold for the case of identical idiosyncratic volatilities.^^2 and^will be dierent.
For the general case, the formula forX~ 2 = (In X 1 (X 01
 X~  (^21) Xbecomes 1 )  (^1) X 1
   (^1) )X 2


Proving this is left as an exercise (whiten the returns by premultiplying by   1 = (^2) , use the results above, and transform back).
Procedure 3.1:1. Estimate the modelStagewise Linear Regression

2. to obtain estimatesRegress the columns ofregression. DeneZ~^ ^as a matrix whose, andZy^on=. XX^ and take the residuals of each^1 +ith column is the residual(3.23)
3. Estimate the modelvector of [Z]ionX.^=Z~ 2 +
3.7.4. The Singular Value DecompositionThe Singular Value Decomposition (SVD) is a fundamental factorization innumerical linear algebra. It powers many numerical computations, as Golub
and Van Loan [2012] beautifully explains. In addition, it is extremely insightfulin theoretical analysis. Much of this book relies on it. Since it is not alwayscovered in linear algebra courses, this appendix provides a crash course on the
subject. For gentler introductions, see Trefethen and Bau [1997], Horn andJohnson [2012], Strang [2019], and the aforementioned classic book by Goluband Van Loan.
Abe thethat is symmetric and positive semidenite (We start by recalling a basic fact of algebra. We are given a square matrixith eigenvalue and eigenvector ofA, i.e.,xAxAv^0 i=0 for allivi, wherex). Letvii;arevi


unit-norm vectors. Then, the eigenvalues are real, positive, and the eigenvectorsare orthonormal, i.e.,matricesA 2 Rmn? A possible generalization is to relax the condition thatv (^0) ivj=i;j. What can be said about generic rectangular
vthe form:requirement thatiappear on both sides of the eigenvalue equation. We posit an equation ofAvi=vsiiUbe orthonormal and similarly fori, withvi 2 RnandUi 2 Rm. However, we keep theUi. Letrminfm;ng
be the norm ofindependent vectorsthere arem rindependent vectorsA. The image subspace ofxisuchAxi 6 = 0. The kernel subspace has dimensionyisuch thatAhas dimensionAyi= 0. We partitionr: there arenv iinrr:
image and kernel vectors:Avi=siUi 1 ir (3.24)
We can write these equations in matrix form:Avi=0 r < im (3.25)
Av 1 ::: vn =U 1 ::: Um 
(^2666666)
666666664 s^00001 ::: ::: ::: :::s^0002 ::: ::: :::::: ::: :::::: ::: :::::: sr :::^00000
0 ::: ::: ::: ::: 0
(^3777777)
(^777777775)
Here, in addition to the vectorsU 1 ;:::;Ur, we have completed this orthonormal(3.26)
basis withcan be written asUr+1;:::;AVUm=so that it spansUS, whereUR;mV. In compact form, Equation (3.26)are orthonormal matrices, i.e.,


Uthe main diagonal. Finally, we rewrite the equation after right-multiplying byV 00 Uas=ImandV^0 V=In; andS 2 Rmnmay have non-zero elements only on

We show the decomposition visually in Figure 3.5.A=USV^0 (3.27)
A = U x S x V'

Figure 3.5:We prove Equations (3.24), (3.25) by noting thatSingular Value Decomposition, full form. A (^0) Ais a symmetric
((3.24). We prove that thepositive semidenite matrix of rankA^0 A)vi=ivi. DenesiU:=ipare orthonormal:iandr, so that there areUi:= (Avi)=si. These satisfy Equationrpairs (vi;i) satisfying
becausev 1 ;:::;vrare orthonormal. Now we complete the basis inU^0 iUj=v^0 i(Asi^0 sAvj j)=ssjivivj=i;j Rnby adding(3.28)
orthonormal vectorsnullspace ofcomplete the basis inA. Correspondingly, we add orthonormal vectorsvRr+1m. A few observations (among many) on the SVD:;:::;vn, whereAvi= 0. These make a basis for theUr+1;:::;Umto

1. If all the singular values are distinct, the rstare uniquely determined. However, they are not in the case of identical 110 rcolumns ofUandV


2. Equation (3.27) can be rewritten assingular values.
    The SVD decomposes a matrix into a sum of rank-one matrices.A=Xi=1r siUiv^0 i (3.29)

3. For allir, A (^0) Avi=s (^2) ivi (3.30)
In other terms,AAA^0 A^0 Uandi=AAA(A^00 have the same eigenvalues.Avi)=si=siAvi=s^2 iUi (3.31)

4. The SVD decomposes the operations on an element ina rescaling of the axes turning a ball into an ellipsoid, followed by anotherrotation. The net result is that any operatorAmaps a point on a ballRninto a rotation,
    into a point on a rotated ellipsoid. Figure 3.6 illustrates the steps of theSVD.
3.8. ExercisesExercise 3.2(Portfolio Covariances):

1.2. (5)Prove that, ifnet return portfolio(10)Generalize this result. LetR wehas varianceis Gaussian with covariance matrixxbe a random vector taking values inw (^0) rw. (^) r, then theRn
with covariance matrixcovariance matrix of the random vector. LetAbe anAxmisnA
Amatrix. Prove that the (^0).


x V'x SV'x USV'x

Ax x

Figure 3.6:rotation. Singular Value Decomposition as a sequence of steps: rotation, scaling,

3. (10) Say that a random vectorwith covariance matrixUU (^0) , and dene. Let the Singular Value Decomposition ofxfollows a multivariate normal distribution be

1 =^2 =U^266666664 ::: ::: ::: :::^1100 =^2 ^1200 =^200 ::::::::: ^0001 n= 2 377777775 U^0
Let 
1 = 2 a gaussian distribution with unit covariance matrix. Prove thathas covariance.
Exercise 3.3:center the loadings with a rotation. Hint: use a one-factor model.(27) Provide a counterexample in which it is not possible to
Exercise 3.4: (30) Find conditions under which matrix (3.4) is invertible. 112


Exercise 3.5of our factor model we have considered a linear model of returns. Assumeinstead that we have a linear model for the vector of log returns. Denote this(Factor Model of log returns): In the original formulation

vectormatrices of log returns and of returns1. (10) Prove that the covariance matrix of returns is such thatr~. The net return of assetiisri;t ~=r,exp (^) r(respectively.~ri;t) 1. Denote the covariance

2. (5) Show that the rst-order approximation for the exact equation above[^ r]i;j= exp^12 [^ ~r]i;i+^12 [^ ~r]j;jexph[^ ~r]i;j ^1 i (3.32)

is [ (^) r]i;j'[ ~r]i;j1 + 12 [ ~r]i;i+ [ ~r]j;j+ [ ~r]i;j (3.33)
Exercise 3.6Prove that [(Excess Returns)^ r]i;j[^ ~r]i;j.: (25) It is commonly assumed that among
the investable assets there is an asset that has returnrthe standard factor model (3.1) models thefreechanges over time, but is known in each period. In the academic literatureexcessreturns, dened as (rfreewith probability 1.rt)i rfree,
as per Section 2.1.2 On the other side, practitioners think in terms of returns,not excess returns. When in portfolio management is incorrect to reason in term of excess
returns? When it is not?by adding a factor.Show that a model of excess returns could be recasts as a model of returns
 Can you extend the modeling to incorporate sensitivities to interest rates? 113


1. Factor Models are intuitive and tractable.The Takeaways
    (a)(b)Intuitive, because they model additive sources of returns, eachone with interpretable characteristics;Tractable, because linear models can scale in complexity andbreadth of covered securities.
2. They can be used for risk estimation, portfolio construction, signalresearch, and performance attribution. You can:(a) Separate risk into factor and and idiosyncratic, and managethem according to your investment philosophy;
    (b)(c) Optimize a portfolio having full visibility into the type of riskyou want to tolerate;Understand prot and loss in terms of factor and idiosyncraticterms.
3. They are 
exible, i.e., they can be modied, simplied, or extendedto suit a specic need.(a) Simplify a model, by projecting it on a lower-dimensionalspace;
    (b) Transform a model, by changing its factor representation;(c) Extend a model, by adding factors.


# Chapter 4Evaluating Excess Returns

## The task of estimating factor models and testing alphas for systematic strategiesusually involves reusing the same historical data. This is somewhat unintuitive.One of the dening features of the past 40 year has been the increased recording

## of new data sets and its dissemination. Investment rms have budgets of tensof billions of dollars allocated to the purchase of market and alternative data,and to the bespoke collection of data (e.g., via web scrapes). And yet, the

## characteristics of traded assets, and specically of companies, do not change ona minute-by-minute basis; and investment strategies with relatively long holdingtimes { of the order of a day or longer { do not necessarily employ tick-by-tick

data. If we record prices for a broad local investment universe at ve-minuteintervals, we collect 60 millions numeric data pointsidentier and a time stamp, the required storage is of the order of gigabytes. (^1) ; including a security

## History is not replaceable, and sometimes is not deep. Not replaceable, in thesense that it is not easy to produce a simulated version of the past that provablyreproduces all of its features. Not deep, in the sense that we do not live in a

## stationary world. The pace at which the real world outside of nance changesis breathtaking and accelerating; and markets are a timid re
ection of it. Noteven taking such change in to account, the introduction of new technology,

(^1) Assuming 6.5 trading hours, 252 trading days and 3,000 stocks. 115


of new market microstructure designs, of new regulations, and the ongoingcollective learning process of all market participants make the investing worldof ve years ago very dierent from today's. The fact that we have to rely on
historical data poses a major challenge. We cannot design experiments. Ourstudies are observational and repeated. Financial practitioners do not have ashared protocol for experimental analysis. Even if we had one, it is far from
obvious that it is the correct one. Well-established disciplines like Medicine andPsychology had shared experimental practices accompanied by experimentaldesign, and yet they have undergone a reevaluation when their practitioners
found that most of their results are not replicable [Ioannidis, 2005, Open ScienceCollaboration, 2015].This poses a few challenges for us modelers. We have a very large number of
signals types, which themselves depend on continuous tuning parameters. Thisis similar to the situation faced by biostatisticians, who are faced with tens ofthousands of simultaneous tests in the form of responses from DNA microarray
\response variable" for a DNA microarray is usually discrete (\polytomous"),Dudoit et al. [2003], Huang et al. [2009]. The details are quite dierent. Theand responses are uncorrelated or weakly correlated. In quantitative nance, the
response variable (be it return or Sharpe) is continuous, and signal correlationplays a decisive role.This chapter has four sections. First, we list some basic best practices for
data preparation and usage. Second, we describe some common backtestingpractices and critique them. The third section summarize some importanthypothesis testing approaches. The last section is entirely devoted to describing
a new backtesting protocol, which oers several advantages over the previousones: it gives nite-sample uniform probabilistic bounds on the Sharpe Ratio


of a large set of strategies.
We review a few best practices for backtesting. They do not originate from some4.1. Backtesting Best Practicescomprehensive theory for them. Unlike Athena, who was born fully formed
from the mind of Zeus, it is an ever-incomplete, occasional shallow body ofknowledge that has formed by experimentation. Some references covering theapproximately the same ground are Arnott et al. [2019], Wang et al. [2014],
Lopez de Prado [2020].Data Sourcing. High-quality data are essential to backtesting, and the search
for better data is a never-ending task for a researcher. There are four broadareas of concern. The rst one is data sourcing. There are multiple vendorsoering similar data. When comparing them, ask the following questions:
mean?Denition and Interpretationnot only in data sourcing, but in quantitative investing, isWhat is the exact denition of the data collected? What are their. Perhaps the rst and most important question,what do the data
physical units? If the dataset is money-related, it should be unambiguouswhat is the reference currency (or currencies, for exchange rates). If thedata is 
ow-related (i.e., measuring rates over time), the time unit should be
 dened. A surprising number of mistakes happens because of unit conversionerrors.Provenance. Where are the data coming from? Does the vendor collect the
data themselves (e.g., via web scraping, or internet trac); more often thevendor serves as an intermediary between a data originator and the client. In 117


the former case, what is the collection criterion? Does the vendor sample dataor collects the data exhaustively? Is the population sampling methodologysound? In the latter case, who is originating the data? Are they trustworthy?
 Completenessdata that are obviously missing from the data set such as, for example,intermittently missing prices? Are there data that are non-obviously missing,. This leads to the second question: completeness. Are there
such, as for example, unrecorded consumer credit card transactions? Someof these questions can be answered by performing exploratory analysis onthe data themselves, others need to be addressed with the vendor.
 Quality Assuranceor collects are consistently of good quality? Does it have checks for changepoints in the data characteristics?. How does the provider ensure that the data it receives
 Point-in-time vs. Restated Dataa certain date, without changing them at a later date, based on correctionsand company updates? This is an instance of data leakage, which we will. Does the provider oer data collected as of
 cover this in more detail later.Transformationssome instances. Examples are: imputation of missing data; winsorization. Data are almost always transformed by the vendor in
and censoring of outliers; end-of-period price calculations (last transaction,mid bid-ask price, weighted average). These transformations should be docu-mented, evaluated, and if possible veried by the research analyst.
 Exploring Alternatives and complementssense questions: can we obtain better data, in three dimensions. First, arethere providers oering larger coverage for the same data set (more securities. Always ask the following common-
at any point in time, deeper history, more frequent data)? Second, are thereproviders with better data? For example, if data are collected from broker-


dealers, the alternative provider has an agreement with a larger number ofparticipating contributors. Third, can we obtain complementary data? Theseare data sets that used jointly with the original data set, greatly increase its
original value. For example, we may obtain transactional data that help usestimate short-term revenues of a company, in addition to data that give usa good estimate of their costs.
Research Processis part of their competitive advantage; it's indeed partthoughts and learned lessons accumulated over a lifetime of experiences and. Every researcher has their own research process. Thisof what they are, of

of studying. It would be futile to superimpose the author's overall researchphilosophy to that of the readersteps that are uncontroversial, and are part of basic hygiene. Consider these as (^2) , just in a few pages.However, there are a few
the precept to never leave home without wearing underwear. Data Leakagedenition of data leakage is the presence in the training data, the data. The rst recommendation is to avoiddata leakage. The
available up to timeperiodsa certain date that we are not able to use in production today. Detecting datat+ 1 and later. The reference rule is to never use data in a backtest ont, of information contained in the target, i.e., returns in
leakage is more art than science, and it requires both a deep knowledge ofthe data (see above) and of the problem at hand. Below are a few examples.{ Survivorship bias. If we backtest the performance of a strategy over an
2 extended period of time, considering only the stocks that have continuouslytraded during this period, i.e., the surviving stocks at the end of the
Point taken, to an extent. I am providing some building blocks, and you are reshaping andassembling them into something sensible.Although, you may argue, this whole book is an exposition of my investment philosophy.


backtest, we are subject to survivorship bias. Stocks are most often delistedbecause they experience large losses, trade at low unit prices, becomeilliquid and do not meet the criteria for being listed on exchange. Removing
them biases the investment sample toward outperformers with dierentcharacteristics from the broader investment universe at a point in time.For example, the Survivors' liquidity, momentum, and size are larger
than the universe. This is the simplest and most impactful instance ofdata leakage. The remedy to this issue is to: a) employ an objectivemethodology for inclusion that is applicable at any point in time; b)
specify a realistic and conservative rule in the backtest for the event ofa delisting. For example, one could assume that the entire investment iswritten o. Note that the methodology in a) should be speciedbefore
backtests are initiated. Changing the inclusion rules based on the resultof backtest is also an instance of data leakage, and it should be avoided.Criteria for inclusion are indeed not straightforward to specify. A common
recommendation is to use a prespecied investment universe representedby a benchmark, like Russell 1000, Russell 3000, MSCI benchmarks, orcommercial factor models investment universes. Note that benchmark
components are always announced before (\announcement date") theeective addition date (\reconstitution date"), and the returns of thestocks are aected by the announcement an the inclusion. In your backtest,
you may want to capture this information, in order to assess how muchof the performance of your quantitative strategies is aected by recentchanges in the investment universe.
{ Financial Statementsor year should be included in the backtesting data on the day (or the day. Financial statement information for a given quarter


```
{ after) of their public release, not on the last quarter to which the datarefer, or a xed number after the reference quarter.Point-in-Time Data. Financial data used in the backtest on a given date
(a quarterly nancial report) is restated because of material error, theshould always be the most current data availablebacktest should not re
ect that. The strategy must be tested by allowingas of that date. If a 10Q
{ the presence of error in its input data.Price Adjustmentsshares. The price of the split share is adjusted accordingly. This occurs. Shares are regularly split (or reverse-split) into multiple
when the stock appreciates to the point one share becomes so expensivethat it prevents investors from being able to buy it. In order to computehistorical returns across long time series, prices and dividend are usually
split-adjusted. This introduces a complication. A low stock price in thedistant past indicates that the shares have been split several times in thefuture, likely because of high returns. The price becomes informative of
{ future performance. The recommended remedy is to use adjusted pricesonly for return calculation. For feature generation, use as-of-date prices.Missingness. In certain cases (mostly unstructured data instances), data
points are missing either because they were not made available as-of-dateor because they contain sensitive information and were redacted. In thelatter case, missingness may be suering from look-ahead bias and is
```
{ informative of future returns.Avoidable Mistakesperienced, eective researchers make never ceases to amaze. The amount of silly mistakes (in hindsight) that ex- (^3). For example,
and that authors of investing books are even dumber than investors.^3 One of the implicit themes of this book is that investors are stupider than they think, 121


(see the previous bullet point). As another example, an erroneousa stock characteristic available in a data set had high Information Coef-cient. Upon further investigation, it was a stock split conversion factortvs.
 Strategy Developmentta three-month momentum factor denition, also causing a false positive.+ 1 convention error caused a research to include the next-day return in. There are some qualitative recommendations that,
while missing a solid foundation, are hard to argue against.{ Have a theory (if you can)anomaly, and if we pre-registered the predictions of the theory before. It is preferable to have a theory for every
the backtest. For example, in their paper on quality, Asness et al. [2019]propose a theory guiding the development of the factor; so do Frazziniand Pedersen [2014] when they analyze the beta anomaly. With a theory
as a guide, it is easier to choose a security characteristic among many,therefore reducing the number of strategies being tested; it is possible tointerpret the result and believe in it more, and it is possible to critique
{ and revise the characteristic, which is maybe not desirable (it would benice if we got it right the rst time) but necessary.Enforce reproducibility. Document all your strategies and make sure you
{ can reproduce and rerun them at any time.Use as much as possible the same setting in backtesting and in productionBy this we mean that we should use the same point-in-time data, but also.
{ the same optimization formulations, the same market impact model, andthe same codebase.Calibrate the market impact model. When we perform a backtest the
market impact model has a \descriptive" role. It estimates the lossesin eciency from actual trading. It is not possible, however, to verify 122


the realized market impact on historical data. In order to align backtestperformance to live one, it is important not to take a market impact modelat face value, especially one provided by a vendor or a partner. Instead,
calibrate its parameters against live performance of the current version ofyour strategy, so that realized and backtested PnL of your current strategyoverlap as much as possible.
{ Include Borrow Costssimulated PnL, one should take into account borrow costs for shortedsecurities, since they can have a material impact on the protability of. As part of the eort to align production and
the short side. This has challenges. Historical borrow rates are not readilyavailable historically. The researcher may have to approximate them, orpredict them on the basis of security characteristics. Another complication,
albeit less impactful, is the tax treatment of dividends. When they arereceived by the investor, they are subject to taxation. When the investoris short the security, the treatment of dividends is more complex. In
practice, tax dividend treatment is complex, and does not make a materialdierence in backtests, so it is not modeled. Be aware of it, in case yousee discrepancies between accounting and simulated PnL.
{ Dene beforehand the backtesting protocol.sequence of actions and decisions that lead to assessing the performance ofa strategy. It is the subject of the next section. For the sake of this list ofA backtesting protocol is the
folk wisdom precepts, it is sucient to say that the backtesting protocolshould be changed a) rarely, b) for a good reason, and c) if it changes, youshould rerun and re-evaluate all your strategies under the new protocol.
{ Dene beforehand the dataset being usedpart of the backtesting protocol, the heuristic follows from the previous. If dataset selection is seen as


```
point. The dierence however is that new data become available everyday, both in the form of live data, and extensions to historical dataset.Researchers may be prone to include datasets that conrm their ndings,
and ignore those that do not. Ignoring new data would be suboptimal,and including them selectively may lead to the wrong conclusions. Useyour judgement and research integrity, which no theorems can help.
```
4.2. The Backtesting Protocol4.2.1. Cross-Validation and Walk Forward
Evaluating trading strategies bears similarities with statistical model selection[Hastie et al., 2008]. We have a family of strategies (in Statistics, a familyof models), and a performance measure, such as Sharpe Ratio or return on
GMV. The strategies themselves may depend on several parameters. Twoevaluation schemes are most common. The rst one is cross-validation (Hastieet al. [2008], Ch. 7, and Mohri et al. [2018], Ch. 4). The available data is
split into abased on the estimated time-dependence in the time series, the training andholdout samples are separated by a \buer" dataset. The cross-validation istraining datasetand aholdout (or validation) dataset. Sometimes,
split intotraining and holdout datasets, we may want to separate the folds by a shortbuer (for equities, just one or two days) to eliminate dependencies betweenKequal-sized samples (\folds"). Similarly to the buer between
folds. This eliminates a possible source of look-ahead bias. Then we performKthe possible combinations ofestimation-evaluation exercises The parameters are estimated on each ofK 1 folds, and the performance of the model


```
Fold 1 [train]FoldFold 1 [test] 1 [train] Fold 2 [train]FoldFold 2 [test] 2 [train] Fold 3 [train]Fold 3 [train]Fold 3 [test] FoldFold 4 [train]Fold^4 4 [train] [train] Fold 5 [train]Fold 5 [train]Fold 5 [train]
Fold 1 [train]Fold 1 [train] FoldFold 2 [train] 2 [train] Fold 3 [train]Fold 3 [train] Fold 4 [train]Fold 4 [test] Fold 5 [train]Fold 5 [test]
```
Run 1Run 2 Training Dataset Buffer Holdout Dataset time
Run 3Run 4Run 5
Figure 4.1:folds, while lighter boxes are training folds.A scheme of the cross-validation procedure. Darker boxes are validation
is evaluated of the remaining fold using the optimized parameter; see Figure4.1. Then estimate the cross-validation performance as the average of the

Cross-ValidationBest Parameters Training DatasetFinal Training Data Holdout Dataset

Figure 4.2:A scheme of the cross-validation procedure. Data are split into two sets.Final Validation
Cross-validation is performed on the rst one (training dataset), to estimate theexpected performance of a strategy. The model is then optimized on the entiretraining dataset, and validated on the second one (validation dataset).
single-run performances. Finally, performance is checked against the holdoutsample; a scheme is shown in Figure 4.2. There are several contraindications 125


to using cross-validation for nancial applications. First, the samples are notindependent. The time dependence is re
ected in the returns themselves. Weknow that serial dependence of return is weak and has short memory, while
volatility dependence is strong and has long memory. For certain time series, itis possible to remedy this by keeping the order intact in the training folds andthe errors are serially uncorrelated Bergmeir et al. [2018], Cerqueira et al. [2023].
This is not the only issue faced in nancial applications, however. For example,consider the inclusion of security momentum as a predictor. This characteristicuses past returns. Now, if the validation fold precedes temporally the training
fold, these past return are in the validation fold and we are incurring in atypical instance of data leakage: the predictors directly contain informationabout the target. This is just an obvious example; there are subtle ones as
well. For example, we could use forward earnings forecast as a predictor. Butforward earnings are usually produced by analysts, who base their judgementon past returns. Like momentum, we may have leaked target data into the
training set. Besides the temporal dependencies, there is another practicalobjection to[2008] (Section 7.10.2) make a forceful case that the model shouldK-fold cross-validation. In their in
uential book, Hastie et al.entirelybe
selected by cross-validation. Predictive variables (be they alphas or factors,in our framework) should not be screened in advance. This is not never donein practice. The predictiveness of signals or fully-
edged strategies is tested
separately. Perform cross-validation enough times on dierent classes of models,and you will inevitably obtain favorable results. The holdout dataset is meantto serve as a nal check against this \shing expedition" [Cochrane, 2005].
And yet, when the number of raw signals runs in the millions, it is inevitableto cycle through several renements and model revisions, so that the holdout


Frequency (^020) −0.5 sharpe0.0 0.5
4060
Frequency (^0102030) −1.5 −1.0 −0.5 0.0sharpe0.5 1.0 1.5 2.0
40506070
Figure 4.3:Cross-validated Sharpe for (a) Scenario 1, (b) Scenario 2.(a) (b)
sample performance becomes just another variable to be optimized, instead ofa performance check to be run only once.An example may help illustrate the perils of cross-validation. We have
Nrandom: [= 0= 1000 assets. We simulate iid asset returns with:01. We introduceB]i;jN(0;1). These random features are by design not predictiveprandom asset characteristics, also iid drawn atrt;i N(0;^2 ), with
of returns. The backtest consists in a 5-fold cross-validation, to estimate theperformance of the predictors. In each run, we select the best performing factor,based on in-sample IC, and then compute the IC on the test fold. Then we
report the average cross-validated IC. We repeat the process on 1000 simulateddata sets. Below are the results for two scenarios:1. The rst one is the \many periods, few predictors" case: we setT= 5000
2.(twenty years of daily data) andhave felt too lonely.The second one is the \not many periods, more predictors" case: we setp= 2; two predictors because one would
Twe meet in practice.= 1250 (ve years of daily data) andp= 500; not nearly as many as


The frequency histograms of the simulations are shown in Figure 4.3. Somesummary statistics of the simulations are shown in Tableare close to zero in both case, with a much larger standard deviation for??. The averages

the many factor-case. The percentage of samples whose Sharpe Ratio passesthe 1% signicant level is shown in the last column of the tablehistograms for the two simulated scenarios; the conversion IC to Sharpe Ratio (^4). Frequency
is SR = ICT p p (^252) Mean(SR) Stdev (SR) % passingN
5000 21250 500 0.040.07 0.61.4 1.2 19
backtestingand target returns for periodA remedy to the data leakage issues arising in cross-validation is[Pardo, 2007]. In this scheme, we use historical data up to periodt+ 1. The scheme is as close as possible to thewalk-forwardt
{ serial dependence and risk of data leakage { and it also augments naturallyproduction process. It addresses two drawbacks of cross-validation for time-seriesthe data set with the arrival of new data. Finally, it is naturally adaptive:
it ne-tunes parameters as the environment changes. These advantages arecomplementary to cross-validation. As a result, it is often the case that signals,or simplied strategies, are rst tested using cross-validation, and then tested
\out of sample" in a walk-forward test. This is not ideal, however, since it hasWalk-forward has an additional important drawback: it uses less training dataan opportunity cost caused by the delay in running the strategy in production.
than cross-validation. When the set of models and parameters is very large, this 2 : 34 pThis is the percentage of simulation samples for which the condition(1 + SR (^2) =2)=T SR >


```
Training SetTraining SetTest Set Test Set Test Set
Training Set Training Set Test Set
```
```
time
Training SetTraining SetTest Set Test Set Test Set
Training SetTraining Set Test Set
```
time

Figure 4.4:training data, thus preserving the estimation procedure. The bottom one uses all theavailable data up to certain epoch, possibly weighting data dierently based on theinterval from the decision epoch.Two common walk-forward schemes. The top one uses xed-length
limitation could be very severe. On the other side, when the model has beenidentied, and only a few parameters need to be optimized, then this drawbackbecomes negligible. Two additional trading settings in which walk-forward does
not suer from data limitations are when a) data are plenty. This is the caseof high-frequency trading; b) data are very non-stationary. This is the case,to some extent, of every trading strategy, and this very fact suggests that
walk-forward backtesting is, in any event, a necessary step in the validation ofa strategy, and in its preparation for production.Summing up, neither cross-sectional nor walk-forward schemes are without

aws. Ideally, we would like a protocol with the following features.1.2. non-anticipative/immune from data leakagetaking into account serial dependency; ;


3.4.5. using all dataallowing for multiple testing of a very large number of signalsProviding a rigorous decision rule;. ;
Walk forward meets the rst two requirements; cross-validation meets the third.Neither meet the last two. The next section introduces a novel backtestingprotocol, theRademacher Anti-Serum (RAS) (in short, RAS), which meets
these requirements.
4.3. The Rademacher Anti-Serum4.3.1. Setup
We will be concerned with testing the performance of strategies and signals.The former is simply the time series of the walk-forward simulated returnsz-scored by their predicted volatility, so that their average equals the empirical

sharpe ratio for strategyprotocol is similar to walk-forward. When we test signals, we instead considerthe Information Coecient for the signaln, which we denote bynat timet. The denitions are belowxt;n. In this respect, the (^5) :
xxt;nt;n:=:=qk w (^) t;nw (^0) t;n (^0) t;nkk^0 t;n (^) trtttwkt;n (Information Coecient)(Sharpe Ratio)
We also denotecontext. In either case, the primitive dataset needed for the analysis is a 5 xt;nboth instances; the interpretation will be clear from the
For denitions and uses of , see Sections 3.3 and 8.4. 130


Tcolumns denote strategies, whose set we denotethetNth row ofmatrixXXis denoted by. Rows denote observations as of a certain timestamp andxt, and thenth columnS. For notational simplicity,xn. In the following we
make the important assumption that the random vectorsvariable, drawn from a common probability distributiontwo ground. The rst one is empirical. Serial dependence is small for returnsP. We justify this onxtare iid random
observed at daily frequencies or lowercan be extended to the case of time-dependent returns, at a price of weaker,asymptotic results. We recommend to plot the autocorrelation plot of the^6 The second one is that our framework
univariate plot of the seriesthen replace the original time series withaverages of blocks (x1+ks;n;:::;xxn. If there is sizable autocorrelation up to lag(k+1)s;n). We employ the following notation.bN=scnon-overlapping, contiguouss,
We let the joint distribution ofdistribution on the space ofindependent, identically distributed (iid) rows, each drawn fromTxtbeNPmatrices in which the element. LetD=NNi=1Pbe the joint probabilityPx.tPhas
Pof the data matrix(We also dene a \bootstrap distribution", i.e., a probability distributionX). An elementXY. For notational simplicity we drop the subscriptis drawn fromDby sampling with replacementXTsincerows
we only deal with only one data matrix.of strategy/signal performances. DeneThe expected value ofxtis denoted by^(X) 22 RRNN. This is the true vectoras the vector of column
averages ofX: ^(X) =T 1 XT

(^6) See Chapter 2 and references therein, for example Cont [2001] and Taylor [2007].t=1xt (4.1)


which is the expected value of the row ofbution.Let aRademacher random vectorbe a beXaccording to the bootstrap distri-T-dimensional random vectors
Rademacher Complexitywhose elements are iid and take values in 1 or -1 with probability 1/2. TheofXis dened as:
Before stating a rigorous result linking this quantity to a bound on performance,R^=Esupn j^0 Txnj
we focus our attention on its interpretation. Specically, we can interpretat least three ways. As the covariance to random noise: Consideras a random covariate.R^in
We can interpretperformance measure of a strategy to random noise. If, on average, for everyset of +/-1 indicators, there is at least a strategy that covaries with it, thenR^as the expected value of the highest covariance of the
\we can do no wrong": for every realization of a random series, there's astrategy that would do well matching it. If we interpret thefor epocht, then this means that for every sequence of eventsxt;nas predictionstwe have a
 strategy that predicts them well.As generalized 2-way cross-validationof positive elements intconcentrates around size: For suciently largeT=2. We denoteT, the setsS+the
set ofinside the sup asT=2 periods wheret= 1, andS the other periods. Rewrite the term

j^0 Txnj= (^12) T (^2) s 2 XS+ 1 xs;n+T (^2) sX 2 S xs;n^ = (^12) j^+n ^ nj


For strategyon two equal-sized random subsets of the observations. By taking the supacross strategies, we are estimating the worst case: we estimate performancen, this is the discrepancy in average performance measured
on a subset, and get a very dierent result on the remaining subset! Andif the discrepancy is high for each random subset, this will indicate thatperformance is not consistent: there's always at least a strategy that performs
comparatively wellassociatedperformance.R^is high, and means that the set of strategies has unreliablesomewhereand poorly in the remaining periods. The
\random direction" chosen at random inAs measure of span over possible performancesequal topT. In the case where the performance measure is the standardizedRT. The vector has Euclidean norm: We interpretas a
return,this value. The empirical RademacherE(kxnk) is also equal topT, and is strongly concentrated aroundR^is then approximately equal to
This can be interpreted in the following way. We have a set ofEsupn^ kkk^0 xxnnk^  N vectors
xthe maximum collinearity (expressed as the cosine distance) of this randomdirection to our vectors. The expected value of this collinearity measures^1 ;:::;xN. We pick a random direction in the ambient space, and observe
how much our set of strategy vectors spancopies of the same vector, the answer is: not very well. If conversely thesevectors are all orthogonal, we have maximum collinearity. The RademacherRT. If we havenvectors that are
One interesting characteristic of the Rademacher complexity is that it takes intocomplexity if a geometric measure of how much the vectorsxn\span"RT.


account dependence among strategies. If for example we had a billion strategiesto our set of candidate strategies, but they are all identical (hence perfectlycorrelated) we are not increasing the Rademacher complexity. However, if the
strategies are uncorrelated from each other, then the Rademacher complexityis high, indicating higher likelihood of overtting.
4.3.2. Main result and InterpretationThe thrust of our protocol is to provide a uniform additive haircut to theperformance statistic. In other terms, for each strategynwe have an empirical
performanceempirical Sharpe Ratio. Then, we can establish a probabilistic guarantee on thetrue Sharpe Ratio: with high probability, say, greater than 1^n, by Equation(4.1). In the case of z-scored returns, this is the , the Sharpe
Ratio of the strategy is greater thanfunction of the Rademacher complexity, the number of samplesparameter. ^n \haircut", where the haircut is aT, and the
We start with signals. In this case, we havecorrelation. ForHere, we describe the steps that establish a lower bound for performance.allsignals, the true performance metricjxt;nj1, because the value is anis bounded below
1 by the empirical performance minus a haircut, with probability greater than :
The result is described in Procedure 4.1.n>^n (data snooping)|{z}^2 R^  (estimation error)^2 |rlog(2{zT=)} (4.2)
Now, consider the case for Sharpe analysis. The formula is similar, but with 134


Procedure 4.1:1. Backtest all the strategies using a walk-forward procedure. LetRademacher Anti-Serum for Signals

2. Compute3. ComputeXnat time^2 RTNRt^^.(be the matrix with Information Coecients of strategy(XX), as dened in Equation (4.1).).
4. For alln 21 ;:::;Nn>^n  2 R^  2 rlog(2T=)
    with probability greater than 1 .
a dierent estimaation error.

The proofs are in the Appendix, Subsection 4.4, Theorems 4.3 and 4.4.n ^n (data snooping)|{z}^2 R^  ^3 |r2 log(2T(estimation error)=) {zr2 log(2TN=)} (4.3)
lower bounds on IC and Sharpe hold. Moreover the statement holds for any niteWe focus on the interpretation of the claim. The theorem states that thesimultaneouslyT; no asymptotic approximation isat least with probability 1 
involved. The true expected performance diers from the empirical performancebecause of two nonnegative terms: The rst is the term 2R^. This is thedata snooping term. The larger the
number of strategies, the higher thethe set of strategies. Moreover, as we discussed, the higher the dependencyamong strategies, the lowerR^. In the limit case where we test multipleR^, because sup is strictly increasing in


Procedure 4.2:1. Backtest all the strategies using a walk-forward procedure. LetRademacher Anti-Serum for Sharpe

2. Compute3. ComputeXtime^2 Rt.TNR^^(be the matrix with Information Ratio of strategy(XX), as dened in Equation (4.1).). nat

4. For alln (^2) n  1 ;:::;N^n  2 R^  3 r2 log(2T =) r2 log(2TN=)
with probability greater than 1 .
 replicas of the same strategyinnity, 2The second is theR^does not go to zero.estimation termR^is zero. If the number of periods goes to. It is the unavoidable For some intuition,
consider the case ofunit variance. Their averagedistribution with standard deviation 1T iid normal random variables^is approximately distributed as a normal=pT. What is thetwith mean 0 and-quantile of the
distribution? There is no closed-formula for it, but we can approximate itusing Equationdeviation 1=pT(2.4), and Cumulative Distribution Function. For a normal distribution with zero mean and standardF,
This is similar, save for constants, to the estimation errors in EquationsF ^1 () s2 log[1=T(p^2 )] (4.2)
andapproaches 0.(4.3). In the limitT! 1, The estimation error in both procedures


The procedure is operationally simple: simulate all possible strategies in a walk-forward manner. There should be no look-ahead bias. The strategies should beformulated without looking at the entire data set and their parameters should
be tuned based on past history only. As we mentioned in the \best practices"section, all strategies should be documented and should run in parallel to theproduction strategy. Then, estimate the Rademacher complexity of matrixXby
the expectation in the denition of that statistic. The Rademacher complexityis easy to compute for tens of millions (or more) of strategies, and can becomputed for even larger sets of strategies using tools from numerical analysis.
 The SAR procedure for signals uses the worst casehowever, it is extremely unlikely to observe ICs close to one; and IC greaterA few more practical remarks are in order, for the application of the formulas:jxt;nj 1. In practice,
than 0.1 is extremely unlikely. If we assumeTheorem 4.3, the estimation term becomes smaller, by a factorjxt;nj   <1, and apply:
Consider some realistic parameters:\estimation error" = 2= 0:02,rlog(2= 0T:=01 and) T= 2500. Then
 the estimation error is about 0.002.In the SAR procedure for strategies, the formula for the estimation error isa rather simple bound and the constant factor could be probably improved.
For realistic parameters, the error is quite large. For exampleTan annualized estimation error of 5.1. This seems a loose bound, compared= 2500, andN = 1E6, the estimation error is 0.31, corresponding to = 0:01,
to the standard formula for the standard error of the Sharpe Ratio [Lo,2002]: for a strategy with Sharpe Ratio equal to 3, the estimation error


is\estimation error" = F()p(1 +SR^2 =2)=Tp252 = 1:7.
4.4.4.4.1. Proofs for RAS?Appendix
We use some essential inequalities in the proofs. Standard references areBoucheron et al. [2013] and Vershinin [2018].
random variables, andTheorem 4.1(McDiarmid's inequality)f:Rn!R, such that, for each: LetX^1 ;:::;Xi, nbe independent
Then, for allxsupi >;x^0 ijf 0 (,x^1 ;:::;xi;:::;xn) f(x^1 ;:::;x^0 i;:::;xn)jci
Specically, ifci=c, and with probability greater thanP(jf Efj> )exp P^2 i^2 c^2 i 1  = 2 ,
A mean-zero sub-gaussian random variablef < Ef rnc^22 log(=X2)is one for which a positive

constantfor all positiveexists, such that the inequality. The parameter (^2) is the proxy variance.P(jXj> ) 2 exp( ^2 =(2^2 )) holds
i.i.d. random variables with nite sub-gaussian norms and proxy. Then, for allTheorem 4.2(Generalized Hoeding's inequality): LetX^1 ;:::;Xnbe


 > 0 , P (^) n 1 Xi=1n Xi EX > !exp  2 n 22  (4.4)
thatTheorem 4.3jxtnjafor all(Bounds for Bounded Performance Metrics)n= 1;:::;N;t= 1;:::;T. For alln 21 ;:::;N: Assume
Proof. The straightforward inequality holds for alln^n ^2 R^ ^3 ar2 log(2T =)n= 1;:::;N:n (4.5)^n
 supnj^n nj. Dene  := supn j^n nj (4.6)
We claim that with probability greater than 1ED +ar2 log(2T ==) (^2) (4.7)
This allows one to deal withinequality, note that, for allxEt;iD;xsup (^0) t;i 2 nj[^ na;a ];tnj, which is easier. To prove the= 1;:::;T;i= 1;:::;N,
From which it follows thatj^n(:::;xt;i;:::) ^n(:::;x^0 t;i;:::)j^2 Ta (4.8)
We apply McDiarmid's inequality to  to obtain the result.xt;n;xsup^0 t;n^2 RTj(:::;xt;n;:::) (:::;x^0 t;n;:::)j^2 Ta


In order to obtain a lower bound onthe equalities below, we introduce a probability measureindependent from,D. nwe need an upper bound onD (^0) identical to, andED. In
E=DEsupDnsup^ n^n  ^n(n!^ ) ED 0 ^n(! (^0) ) (^)
=EEDDEsupnD 0 supEnD 0 ^^nn((!!))  E^nD( (^0) !^ 0 n)(!^0 )^ (conditioning)(Jensen)
= (T^1 )EDED 0 supn^ Xt (xt;n(!) xt;n(!^0 ))^
We introduce an additional source of noise (thelose a constant of 2, but gain in tractability. We can change the signs of eachsummand by multiplying by some arbitrary factorRademacher vector) and weyt2 f+1;  1 g, since the
terms are exchangeable.() =T (^1) EDED (^0) supn (^) Xt yt(xt;n(!) xt;n(! (^0) )) (^)
=TT^11 EEDDEEDD 00 EEsupsupnn^ XXtt tt((xxt;nt;n((!!))  +xEt;nD(E!D^0 )) 0 E^ supn (^) Xt txt;n(! (^0) ) (^)
==TT^12 EEDDER^supn^ Xt txt;n(!)^ +T^1 EDEsupn^ Xt txt;n(!)^
= 2R 140


Where we denedthe distribution of performance realizations.We now use McDiarmid again: for allRas the expected value of the Rademacher complexity overxt;i;x (^0) t;i,
Hence, with probability greater than 1jR^(:::;xt;i;:::) R^( :::;x= 20 t;i;:::)j^2 Ta
Now we employ the union bound on inequalities (4.7) and (4.9) to obtain theRR^+ar2 log(2T =) (4.9)
claim.Eexp(A random variable)( (^2)  (^2) =2), or if equivalently, is -sub-gaussianP(jjif there is a> a)<2 exp( > a (^2) =0 such that 2  (^2) ).
Then, for allsume thatTheorem 4.4P(jxn(Bounds for Sub-Gaussian Performance Metrics)t;n 2 j 1 > ;:::;N)^2 e ^2 =^2 for all >^0 , for alln= 1;:::;N;t= 1;:::;T: As-.
Proof. Letna > ^0. We splitn ^2 R^ ^3 nr 2 log(2^nTinto the sum of two terms:=) r2 log(2TN=) n ^n=


g(xn;a) +hn(x n;a^n), where=g(xn;a) +h(xn;a)
g(xi;a) := E[Tsup^1 nXt=1Tjg(xxt;in;a 1 (j)xj t;ijsupnaj)]h( xnT;a^1 Xt)=1Tj xt;i 1 (jxt;ija)
We boundh(Px(supi;a) :=ijhE(x[iT^1 ;aXt)=1Tjxvt;i). By symmetrization^1 (jxt;ij> a)] T^1 Xt=1T xt;i^1 (jxt;ij> a)
The random variableEjhj(txxit;i;a 1 )(jjxt;i^2 jE> aXt=1T)jjis subgaussian, since it is dominatedtxt;i^1 (jxt;ij> a)j
byGeneral Hoeng inequality,jxt;ijwith probability 1, and it has the same proxy variance asjxt;ij. By the
P^ Psupi^ jjXXtt=1=1TT hh((xxt;it;i))jj> v> v!!Nexp(exp( Tv Tv^2 =2)^2 =2)
By the union bound,P^ supi jXt=1T h(xt;i)j>p2 log(2N=)=T!=^2
n ^n  2 R^  3 r2 log(2T =) r2 log(2TN=) (4.10)


# Chapter 5Evaluating Risk

## 1. A factor model serves many purposes. How do we score a model'sThe Questions

## 2. How do we evaluate the volatility forecast of a model?3. How do we measure its performance for portfolio optimization?4. What other measures should we take into account?performance? Specically?

## cial models. New model generations. New asset classes. All combinations ofgeographies. And of course, new vendors. However, there hardly any papersThere are dozens of papers and documents extolling the virtues of commer-

## laying out theoretically-motivated procedures that test risk properties of factormodels that are relevant to practitioners. Testing is hard, it is mundane, it ishumble and humbling. In the words of P.J. O'Rourke, \Everybody wants to

## save the Earth; nobody wants to help Mom do the dishes". This is a chapterabout doing dishes. It relies on two simple principles. First, the metrics that weuse should be related as much as possible to our applications. We care about

## accuracy of volatility forecasts, and realized volatility of optimized portfolios,and we strive to measure these quantities in a realistic setting. The second


principle follows from the observation that there is not a single performancemeasure on which we benchmark factor models. It follows that it is possiblethat there a single \best" model may not exist, because it is unlikely that a
single model outperforms all the other on all metrics. This should not be viewednecessarily as a curse, but as a blessing. We can concentrate our eorts on ouruse-case, or at least prioritize for it, and nd the best model for the task.
those aimed at evaluating the covariance matrix; those aimed at evaluatingthe precision matrix; and those aimed at evaluating the model usability forThe remainder of the chapter is organized around three families of metrics:
secondary tasks.
5.1. Evaluating The Covariance Matrix5.1.1. Robust Loss Functions for Volatility Esti-
A major application of a factor model is volatility estimation. The qualityof volatility predictions is one that has been at the forefront of the earlymation
(developments of risk models. If a model predicts asset volatilitiestimet  1 t;t(i.e., the volatility prediction made available at time)), then a measure of the quality of the volatility predictions is given byt 1 for time interval^iat a certain

a loss function L:=T 1 Xt=1n L(~ (^2) t;^ (^2) t)


wherevolatility metric dened previously). The loss functionequal to zero if an only if~tis an empirical estimate of the observed volatility (e.g., the realized^=~In the metric statistic above, we use a volatilityLis non-negative, and
proxyintroduce a concept ofvolatility forecasts~tinstead of the unknown true volatility^t(j), one is better than the other using an unbiased volatilityrank robustnessfor losses: if we have two alternativet. Hansen and Lunde [2006a]
proxy if and only if one is better than the other using the true volatility. I.e.,L(^(1);)L(^(2);),L(^(1);~)L(^(2);~)
Patton and Sheppard [2009] and Patton [2011] completely characterize theseloss functions and show that these two are robusts:

QLIKE(^MSE(^;r;r) :=) :=TT^11 XXit=1=1TT ^ (^2) tr^^2 t (^2) tr^ t (^22) tlog  1 r^ 22 t (^2) t  1 
QLIKE is (save for constants) the negative of the log-likelihood of the normaldistribution. These two loss functions are increasingly being used in place ofthe bias statistic.
5.1.2. Application to Multivariate ReturnsThe loss functions QLIKE and MSE apply to univariate returns, not to co-variance matrices. Below are a few ways to adapt the univariate setting to a
multivariate one.


0.00.5

```
1.01.5
0.5 r 2 1.0σ 2 1.5
```
value lossqlikemse
Figure 5.1:losses when the realized variance is greater than estimated variance.QLIKE and MSE comparison. Notice that QLIKE is skewed, with higher
Production strategiesnecessary test is to evaluate their simulated performance under dierent factormodels. QLIKE and MSE are important and should be checked jointly with. If strategies are already running, a straightforward and
metrics that are important for the portfolio manager, like Sharpe Ratio or PnL.It is important that the covariance matrix be the input to the entire productionprocess, i.e., portfolios should be generated on the basis of the factor model
themselves. If a portfolio is generated using factor model A and then tested onmodel B, the test will be marred by this asymmetry.
Average-case analysiswhere the expectation is taken on a distribution of portfolios as well as of assetreturns. For the distribution of returns, we use the empirical measure. An alternative approach is to estimate the expected loss,P^of histor-

ical returns; for the distribution of portfolios, we may choose a simple one, likeuniform on a sphere. Then we estimateEwD;rP^[L((r (^0) w) (^2) ;w (^0) ^rw)]. There


are a few drawbacks to this approach. First, there is a degree of arbitrariness inchoosing a portfolio distribution. The actual distribution of portfolio is almostcertainlynotuniform; and it is not even warranted that the distribution of
alphas is uniform. Secondly, it is computationally expensive. We are simulatingin highly dimensional spaces, withthousands. Computational issues, such as simulation schemes and convergencewranging in size from 1,000 assets to tens of
criteria, become important. An approximation is to select ai.e.,thesennportfoliosportfolios. A special case of this special case is that ofw 1 ;t;:::;wn;t, and then apply an \average"-case analysis toportfolio basiseigenportfolios,:

decomposeThe approach is computationally tractable. One important drawback is thatthis average loss is not independent of the choice of the portfolios; in fact, it (^) r=USU^0 , and set the basis portfolios equal to the columns ofU.
is quite sensitive to it. Even if we restrict our choice to an orthonormal basis,like eigenportfolios, the measured performance still depends on the basis. Sincethe choice of an appropriate basis cannot be easily justied based on principles,
the outcome is arbitrary.Procedure 5.1:Random Portfolios Average Variance Testing
1.2. Set3. InputstSet= 1wL;:::;Ttot: candidate covariance matrices= 0,N(0, loss function;nIitern),= 0.w w=Lk.wk. Chooses ^uniformly at random inr;t and returnsrt for
4. Set5. If6.^1 Output;:::;TL[(Lrtot (^0) sw.=:)L 2 L;:=wtot (^0) ^L+stotLw=n[()]r=Liter^0 swtot.)^2 ;w^0 tol^s, go to Step 3.w)]. Setniter niter+ 1


Worst-case Under/Over-Predictionworst-case loss function:. Yet another approach is to estimate the
maxs:t:EkwrkP^[L(( 1 r^0 w)^2 ;w^0 ^rw)]
This problem with this approach is that the objective function (be itorcomputationally tractable.MSE) is not convex. When the number of assets is large, the problem is notQLIKE
Procedure 5.2:1. Inputs: candidate covariance matricesWorst-Case Variance Testing ^r;t and returnsrt for

2. Set3. 1 tSet;:::;T= 1wL;:::;Ttot.= 0,N(0, loss function;nIitern),= 0.w w=Lk.wk. Choosesuniformly at random in

4. Set5. If6. OutputL[(wr (^0) sw:)wL (^2) ; :=wn (^0) ^L iterstot^1 wr=n)]w=LiterL[(tot.r^0 sw)^2 tol;w, go to Step 3.^0 ^sw)]. Setniter niter+ 1
production strategies are always being tested against alternative approaches.Average and worst-case analyses are both computationally very demanding.Neither of the options above dominates the others. Whenever available,
Moreover, in the case of average-case analysis the result depends on the as-sumption on portfolio distribution.


Leading alpha MVO portfoliosconstructed on the realized leading returns of the securities. This scheme hasthe advantage to test the predictiveness of the strategy for \relevant" portfolios. Another option is to construct portfolios that are
and is described in Procedure 5.3. Volatility prediction matters if we have alpha.If we don't, then we have other problems to be worried about. An advantage
Procedure 5.3:1. Inputs: candidate covariance matricesRealized Alpha Variance Testing ^r;t and returnsrt for

2. Set3. For eacht= 1L;:::;Ttot= 0.t= 0, loss function;T , let L,^2 N+.
    L^ tot^wt:=:=:=^ L^1 ^tot rs;t=tX^1 +^ t+^+1tLr(sr^0 tw;w^0 ^r;tw)
4. Output:L:=Ltot=(T + 1).
of this approach is that it can be easily augmented. For example, we could testthe performance on portfolios with added noise:
Distribution likelihoodw. An alternative that does not depend on the portfolio:=^ ^ r;t^1 (^ ^t+t); tN(0;^2 In)
choice is to use the log-likelihood for the zero-mean multivariate normal dis-tribution, applied to the returns of the estimation universe. Modulo constant


terms, the negative log-likelihood is proportional toQDIST =Xt r (^0) t ^ r;t (^1) rt+ logj ^r;tj+ntlog(2)
5.2. Evaluating the Precision Matrix5.2.1. Minimum-Variance Portfolios
As we saw repeatedly throughout the book, the quality of a factor model isre
ected in the accuracy of its precision matrix. We propose two methods. Therst one is using a well-known test: minimum-variance portfolios. Consider a
very simple example: construct a portfolionet market valuethe realized variance will dier. The intuition is that a \better" covariancePiwi= 1. This is thewex anteof minimum variance and with unitminimum variance portfolio;
arbitrarymatrix will result in a lower realized variance. We make this intuition rigorous,and generalize to the the case where the portfolio has a given exposure to anfactor, i.e.,Pibiwi= 1.
covariance matrix. LetLet^ ^r^2 Rnnbe a candidate covariance matrix andb 2 Rn, and solve the risk minimization problem^ r be the true
mins:t:wb (^00) w ^r= 1w (5.1)
and letvarthe one of(w( ^wr)(; (^) w^ r(r) be its solution. Denote the realized variance of the portfolio ). Then, the realized volatility of portfolior), and the two are identical if and only ifw( ^ r) is greater thanr/ ^r. This is
Theorem??in Appendix (Section??). A way to apply this result is as follows: 150


Setthe best possible Sharpe Ratio, and a natural ranking of covariance models isby the realized Sharpe Ratio for a certain strategy.b=E[r], the alpha vector. Then the correct covariance matrix results in
tests to evaluate the precision matrix. The realized variance acts as a lossfunction.We can use all the portfolio-dependent schemes introduced for volatility
5.2.2. Mahalanobis DistanceThere is another test that is portfolio-independent and that involves the precisionmatrix only. The Mahalanobis distance is dened for a multivariate zero-

mean random vectorqdistributed according to a Chi-squared distribution withr 0
  r (^1) r. For Gaussian returns and under the true covariance matrix,rand an associated covariance matrixndegrees of freedom (^) rasd(r; (^) rd) := (^2) is (^1).
One test then is t:=n (^1) tr (^0) t ^ r;t (^1) rt
The lower the value ofMSTDMSTD := stdev((r; ^r;), the better the performance of the)
precision matrix. If the standard deviation is very low (say, of the order ofppredicting perfectly. We don't primarily care about the constant in this test, 2 =n), then the inverse of the covariance matrix is, save for a constant,
because a volatility test should address that issue better. A dierent way toTherefore (^1) To prove this, note that the vectorr 0
  r (^1) rPii (^2)  (^2) n. rcan be generated byr:= (^1) r= (^2) , whereN( 0 ;In).


interpret the result is the following: if returns are Gaussian, then they aredistributed ashas meanntand standard deviation (^1) r=;t (^2) t, witha multivariate standard normal rv. Moreoverp 2 nt; We rewrite MSTD as  (^0) tt
MSTD :=t:=nT^11 tXr^0 tt^ ^ r;t^1 nr^1 tt^0 t (^) r;t ^ r;t^1 r;tt ^2
'=TT^11 XXtt nn^112 t (^2) th (^0) t^0 t( (^) rr;t;t ^ ^ r r;t^1 ;t 1

 rr;t;t t In)^0 ttti 22
We are testing the closeness ofleft and right by standard multivariate Gaussian random vectors. In Section9.3.2 we saw that this matrix dierence is responsible for bounding the Sharpe (^) r;t ^ r;t^1 r;t Into zero by multiplying to the
Ratio Eciency.
5.3. Ancillary TestsIn addition to performance measures on the return covariance matrixinverse, we should verify that the model performs well in tasks that are indirectly (^) rand its
related to portfolio optimization and hedging. We consider two specically.The rst one is model turnover. Changes over time in the information we haveat hand aect the transaction costs of our strategies. There are three major
drivers behind such changes. The rst one is in our day-to-day forecasts ofexcess returns, i.e., alpha turnover. We need to model such turnover explicitly,and do so in Chapter 10. The second one is due to changes in the market impact
function itself. There are exceptional periods in which trading activity changes 152


very rapidly, and so does the cost of trading. However, in practice, this is themost stable component in portfolio construction and we ignore its short-termvariation (^2). The last driver of change is the factor model, which is the subject
of the following subsection.
5.3.1. Model TurnoverTurnover is not an intrinsic property of a model; it is the property of a productiontrading strategy. However, it may make sense to nd a measure that gives us an
estimate of strategy turnover. In an ideal setting in which we ignore transactioncosts, we may want to target a constant factor exposure levelIn this setting, it is optimal to trade Factor-Mimicking Portfolios. The returnsbifor factori.
of these portfolio are the best approximation to the true factor returns of themodel. They are introduced in Section 8.3. The weights of these portfolio arethe column vectors of the matrix
Pwtt:=:= (^) Pt b;t^1 Bt(B^0 t  ;t^1 Bt) ^1
What drives portfolio turnover is the change inmeasure of turnover as the time-series average Pt. We then dene a simple
(^2) I should note that some researchers do model time variation of execution costs, e.g., byturnoverF:=T^1 Xt=1T kPt Pt ^1 kF
forecasting trading volume. But these approaches are out of the scope of this book.


whereof being simple and intuitive. It is possible to rene it, at the cost of losinggenerality. If we have an indication of the target exposureskkFis the Frobenius norm of a matrix. This denition has the advantagebof our strategy,
and we have a trading cost functionmeasure of turnover would be TC:Rn!R+, then a more accurate
turnoverTC:=T^1 Xt=1T TC[(Pt Pt  1 )b]
5.3.2. Testing BetasA practical application of risk models is to produce predicted beta of investorportfolios to some benchmark. A simple instance is to generate the beta to a
market portfolio. A slightly less simple example is to generate the beta to afactor-mimicking portfolio. An even less obvious example is that of beta to athematic portfolio: a bank has generated a thematic portfolio that describes an
industrial or consumption trend that is relevant at that point in time. We wantto measure the beta of our portfolio is to this thematic portfolio. In all of theseinstances, we want to make sure that the predicted beta is accurate, in the sense
that it exhibits low discrepancy to the realized beta. Therefore, as part of theevaluation of the risk model, we want to include tests on betas. For simplicity,consider the case of a single reference portfoliow(a factor-mimicking portfolio,
or a thematic portfolio). The vector of predicted betas of each asset to thisreference portfolio is

(^) t(w) =w^0 r;trw;tw


```
The realized return covariance matrix ^r;t:= 11   ee  1 T== ^rX;tTand realized beta vector is given by
^t(w) :=w^ ^ 0
 ^r;trw;tw s=1e s=rt sr^0 t s
```
We measure the beta accuracy asBETAERR(w) =Xt (^) t  ^t (^2)
and employ BETAERR as an ancillary measure of accuracy.
5.3.3. Coecient of Determination?A very popular way to summarize the performance of a factor model is byreporting the average coecient of determination (orR (^2) ) of the weighted cross-
sectional regression. It is dened as 1 minus the ratio of the weighted residualsum of squares and the total sum of squares.
Since the idiosyncratic covariance matrixR^2 =1 PTt=1P^ Tt^ ^=1 ;t^1 =^ ^^2 ( r;tis not known in advance, a proxy^1 t= ^2 rBt^ t^2 ^ft)^2
is used in its place, as described in Chapters 6 and 7. The estimated factorreturnscoecient of determination is interpreted as a positive attribute of the model^ftare the coecients of the cross-sectional regression in periodt. A high


specication, similarly to the case of linear regressiondierences, however. First, there is no \out-of-sample" estimate ofcannot possibly estimate the performance of the model on a holdout sample^3. There are importantR (^2). We
because the estimated coecients, the factor returns, must be estimated inevery period. This makes the metric amenable to data mining. Even if we keepconstant the complexity of the model (the number of factors), it is easy to
increaseBloadings) to an existing model, although more rened metrics, like AIC and BIC,t. The naveR^2 by successive manipulations and adjustments to the loading matricesR (^2) is always improved by adding factors (even with random
penalize more for the number of factors are a possible answer to this objection.Another objection to the use ofthe problem at hand. To illustrate the problem, consider an articial example.R (^2) is that it ignores the rotational invariance of
Asset returns follow a simple static factor modelanda new factor model. Let (^) =In. The estimated factor returns areCt 2 Rmmbe a sequence of iid random matricesr^ftt==BfBt (^0) r+t. Now, let us buildt, withB^0 B=Im
dened as follows:
Ct=^266666664 ^1000 ;t ^0200 ;t ^0030 ;t :::::::::::: m;t^000377777775
whereCt 3 C (^0) t=i;tImtake the values 1 or -1 with equal probability. Note that. After some rote calculations, we nd that the estimated factorC^0 tCt=
(BIC) (see, e.g., Hastie et al. [2008]), since the main points made in this apply to them as well.quality of t, like Akaike Information Criterion (AIC) and Bayesian Information CriterionWe ignore corrections ofR^2 for the \degrees of freedom", and alternative measures of


returns from this model areof determination is unchanged:~ft= (B~^0 tB~t) ^1 B~^0 trt=C^0 tB^0 rt=Ct^ft. The coecient

R^2 ((B~t)Tt=1) =1=1  PPTtTt=1=1Pkk((IITtP=1nn Tt =1krBCBBtkkr 2 tt 0 k)C (^2) rt^0 tBk 20 )rtk^2
However, the estimated factor covariance matrix of the rotated model is=R^2 (B)
[ ~f]i;j!=T (^8) >>< ^1 Xt=1T f^i;tf^j;ti;tj;t
Wheni=j, the average isT ^1 P>>:Tt=1[^0 ~ff^i;t]^2 i;j, i.e., it is identical to the variance ofififii=^6 =jj
the original non-rotated model. Whencause of the independence ofE[fifj]E[i]E[j] = 0. The rotationsf^i;tf^j;t,i;tiC 6 =andtjhave had the eect of decorrelating, the sum approaches 0 in the limit be-j;t:limT!1T  1 PTt=1f^i;tf^j;ti;tj;t=
the estimated factor returns. In summary, we have two models: one is the truemodel, the other is a rotated model with random rotations in every period.The two models are indistinguishable with respect to their coecient of de-
termination since it is identical for both model. It is straightforward to showthat AIC and BIC are also identical. However the second model has a verydierent{and incorrect{covariance matrix. Expert modelers are aware of the
shortcomings ofeectiveness of the cross-sectional regression. One such heuristic is to check theR^2 for factor modeling, and resort to heuristics to conrm the


percentage of periods in which a specic factor's returns meet a signicancecriterion, i.e., the regression coecient corresponding of a factor has an absolutet-score greater than two. Another natural check is on the realized Sharpe Ratios

of each factor returns. These tests conrm thatmodel selectionearlier in this chapter for risk model performance, and on Chapter 4 for testing (^4). The recommendation is to rely on the tests we presentedR^2 is inadequate for factor
risk-adjusted performance.
et al. [2010].^4 For another critical perspective onR^2 used as a metric for time-series model, see Lewellen 158


# Chapter 6Fundamental Factor Models

Fundamental (or characteristic-based) factor models estimate Equation (3.1)using as inputsfactor and idiosyncratic returnsrtandBt. The outputs of the models are estimates of theft;t, as well as their covariance matrices (^) f,
(^) practitioners. Reasons for their popularity are:Good Performance. Fundamental factors models are perhaps the most popular ones among. Commercial models are the outcome of a long process

##  of renement. The rst models date back to the mid 1970s. Consequently,some important factors have been identied.Interpretability. Firm characteristics provide a summary description of indi-

##  vidual rms, and exposures based on these characteristics give a summary ofa portfolio;Connections to Academic Research. In the asset pricing literature, multi-

## 1976], and the reference model used by academic researchers to identifyfactor models originate with the Arbitrage Pricing Theory of Ross [Ross,pricing anomalies is the three-factor model by Fama and French [1993].

##  Alpha Researchbecause they allow the portfolio manager to incorporate almost any datasource, to analyze very large data sets, to interpret the outcome of the. Fundamental models are the workhorse of alpha research,

## analysis, and to feed the outcome to a portfolio construction system. 159


```
6.1. The Inputs and the ProcessThere are ve major steps needed to identify a factor model. Some of themrequire sound quantitative methods; others are more art than science. Before
we even begin to describe the steps, we should focus on the inputs.
6.1.1. The InputsFundamental model inputs are:
```
1. a set of returns per asset/date, i.e., the2. a set ofthese inputs we generate theraw characteristicsper asset/date/characteristic identier; fromBt. rtpart;
Asset returnsThese intervals determine the periodicity of the model. Daily returns maybe based on close-to-close prices. Intraday returns may be based on the last. Returns are usually reported over intervals of equal duration.
transaction price observed in that intraday interval. The interval can rangefrom thirty minutes to a sub-minute interval. It would seem that returns areunambiguously dened, but this isnotthe case. The answer to the question
\what is the nal price in a time period" is not easy nor unique. Ultimatelymodels of returns should help the portfolio manager develop a protable real-lifestrategy. If prices are such that we could not have executed transactions reliably
at their quoted values, then the factor model will not be reliable, and neitherwill be the strategy built on the model. Consider the closing price. Where doesit come from? In many stock exchanges, at the end of the day the Limit-Order
Book (LOB) is replaced by a Closing Auction (CA). Without delving in thedetails of a CA, suces to know that a CA is a very liquid event, in which


stockabout 10% of the daily volume of a stock is traded. Consequentlyportfolio manager, at a non-negligible size. Now, compare this scenario to onethe closing price is meaningful, in the sense that it is exploitable by afor a liquid
in which we are interested in modeling a small-cap stock that is a component ofthe Russell 2000 index. Such a stock would likely qualify to be a member of therisk model estimation universe. However, it could trade at very low volumes. In
addition, if we model intraday returns, then we must pay additional care. Whatdoes it mean that the price at the end of a 10-minute interval was $6.93? Maybethe stock did not even transact in that interval, and the period return is zero.
Or maybe there were only a handful of trades. What is the correct price, then?The transaction price? That is not obvious. Maybe the transaction happenedat the ask, but the transaction just before happened at the bid, just because of
random circumstances. Or, should we use the mid price between the bid andthe ask? Could our strategy reliably transact at either of these prices in reallife? These are just some of the many questions one should ask when developing
models based on intra-day return models, but not only. For many asset classes,determining good closing daily closing prices is a very challenging, importantand thankless task. The details are too asset- and data-vendor-specic to be
covered in detail; moreover, this is an area where traders accumulate Intel-lectual Property that is very material to their success. A few heuristic rulesshould help. First, the shorter the interval, the harder the problem. We saw
(bid, ask, mid); whether to explicitly model the noise in price observations;this already in Section 2.2.4. You have to model what price is appropriatewhether time-of-day non-stationarity matters; whether to model close-to-open
returns and intraday returns separately. The second recommendation is to thinkexplicitly about the relationship between asset liquidity and model periodicity.


```
Liquidity, for our purposes, could be proxied by trading volume in a xedinterval. Usually average daily trading volume is available. Liquidity is relatedto price discovery. The price of a very liquid stock is less prone to observation
errors, and it is more transactable, than that of an illiquid stocks. Therefore, thechoice of model universe and model periodicity are related. Unless you want tomodel market microstructure explicitly, and want to rely on closing per-period
```
Raw characteristic dataprices, then a shorter period will imply that your model universe will be smaller.. This is the \art", or better, \dark art" part of the mod-
eling task. \Raw data" can mean almost anything. A possible classication ofraw data is in structured and unstructured. The former include numerical dataand categorical data that can be associated to a security and to an estimation
period.have an ordering relationship. Examples are the country and sector of a stock.A slightly less common example is the credit rating of a company, which doesCategoricaldata take only a nite set of values, which do not necessarily
admit an order. Unstructured data include any data that do not come directlyin such a tabular form. Examples are the earnings transcripts of a company, orits regulatory lings (Forms 10-K, 10-Q, 8-Q); or the web scraping of a rm
with information about its products; or the consumer credit card transactionswith a rm; or, even more, location data of customers visiting the store of arm. These few examples give just a taste of the immensity of possible inputs
to a model. For asset return modeling purposes, we extract from these vasttroves of alternative data some representative statistics that can be interpretedas structured data. For example, from transactional data, we can extract levels
(dollars transacted in a quarter by a consumer rm's web portal) and trends(quarterly changes in such level); or we can extract measures of geographical


dispersion. Moreover, some of these operations can be automated, or require theuse of machine learning tasks like classication and clustering. One importantfeature of all these operations, though, is that they entail some form of human
expertise. In fact, the task of extracting structured data from unstructuredinformation is perhaps the one that requires the highest amount of humanintelligence. A great amount of papers have been published on characteristic
data. Maybe in the future we will be able to feed such disparate sources ofinformation into a black box and directly predict prices, or even recommendtrades. In that event, I'll gladly write a second edition to this book.
6.1.2. The ProcessThe estimation steps of a characteristic model are:

1. Data ingestionchecking their integrity and performing essential data checks. Amongthem:. This step encompasses receiving data sets from vendors,
     Ensure that data are of the correct type and not corrupt. This happenswith positive probability.Ensure that the set of securities is not substantially dierent from the
     previous period.Ensure that the fraction of missing data per asset and characteristic isnot substantially dierent.
2. Estimation universe selectionin the chapter. The criteria for inclusions are: Identify and report data outliers.. I introduced issues related to this set earlier
     Tradability. The assets must be suciently liquid, because factor- 163


```
 mimicking portfolios include them all.Data qualityfor a dierent goal. We need securities for which prices are. This is closely related to the liquidity of the assets, butdiscovered,
 i.e., close to their economic fundamental value, since we are using thoseprices for return calculations and model estimation.Relevance to investments. The estimation universe should be overlap-
ping to some extent with the investment universe of the strategy. Thisis more of an art. There is not (to my knowledge) a rigorous treatmentof this problem.
3.4. Winsorizationwinsorize them.Loadings Generation. Identify outliers in returns of the estimation universe and. Generate characteristics by transformations and
```
5. combinations.Cross-Sectional Regressionsectional regression of asset returns. For eachrttagainst the loadings= 1;:::;T, perform a cross- (^1) Bt. The

6. outputs of this step are the vectorsTime-Series Estimationmate:. Using the time series from the rst step, esti-^ftand^t.
    (b) the idiosyncratic covariance matrix(a) the factor covariance matrix(c) the risk-adjusted performance of factors returns.^ ^f;t; ^;t;
the research process. 1 Whereas step 3 is relatively straightforward, the last step is at the core of
end of periodA reminder: as explained in Section 3.6, we denote byt 1. Btthe loadings available at the


Procedure 6.1:1. Winsorize the returnsSteps in Fundamental Factor Modeling

2. Transform the loadings3. Select the estimation universe4. Regress returns against loadings5. Estimate volatilities and performances
and covariance estimation. Winsorization comes next. Finally, the process ofidentifying the characteristics receives its own nal, long section.The next two sections cover the essentials of factor models: regression
6.2. Cross-Sectional RegressionThe rst step is cross-sectional regression
where the parameters to be estimated arert=Btft+t; tftand^2 Nt. This is a case ofrandom(6.1)
designfrom a common distribution. We observe (Several regression approaches are possible. One may minimize the square: the tuple (rt;Bt;ft;t) can be viewed as independent samples drawnrt;Bt), and we estimate (ft;t).
loss1.krThe matrixcondition for this is thatt Btftk^2. The assumptions behind this step are:Bt 2 Rnmmhas full rank. A necessary but not sucientn.
2. Residual returnst;ihave zero-mean, are homoskedastic (i.e., have the 165


3. Factor returns and residual returns are independent of each other.4. same variance) and are independent of each other.Factor and residual returns are \well-behaved", in the sense of having at
These assumptions can be relaxed. If the matrix is rank-decient, the solutionto the minimum-norm problem exists but is not unique, and factor returnsleast nite fourth moments.
are not identied. Later in this section we will introduce ways to deal withrank-decient matrices, in order to have a unique solution. Homoskedasticityis also not a necessary assumption. If residuals have dierent variances for
dierent assets, we can weight the losses for each assets dierently. The intuitionis that, if the residual return of an asset has a large variance, we should weightthe loss for that asset less, so that this single term does not dominate the sum
of losses, and unduly aects the parameters' estimation.R+:We estimate Model (6.1) by minimizing the sum of a loss functionL:Rn!

In this section, we choose to minimize the weighted sum of the residuals. WeminL(rt Btft)
know a diagonal, positive matrixas weights assigned to observation (i.e., asset)W, whose diagonal terms can be interpretedi. We then ndfthat minimizes
There are good reasons for this choice. If we assume that Model (6.1) is theL(rt Btft) := (rt Btft)^0 W(rt Btft) (6.2)
true model of returns, then Least Squares gives us the lowest-varianceestimate among all the linear models [Hansen, 2022]. The lack of bias matters 166 unbiased


for performance attribution and alpha identication. Even a small bias in factorreturn estimation (and, consequently, in residual returns) would accumulateover the course of a multi-period performance attribution, thus distorting the
results and the insights from the analysis. An additional benet of WeightedLeast Squares regression is that its estimates have a natural interpretation interms offactor-mimicking portfolios. We will cover these in details later. For
now, it should suce to say these are investable portfolios whose returns track aswell as possible the true{but unobservable{factor returns. Our recommendationtherefore is to use this loss function at least as a starting point, and to run

thorough diagnostics to identify its possible shortcomings. To x ideas, wemake the assumption that the model istN(0; (^) ). The two crucial assumptions here are:rt=Bft+t, withftN(0; (^) f) and
1. Residual returns are assumed to be heteroskedastic. We can address theissue of heteroscedasticity by premultiplying both sides of the equationrt=Btft+tby matrix   1 = (^2). Now idiosyncratic returns are homoskedas-
tic. We use the Ordinary Least Squares loss functionwhich is equivalent to the loss function in EquationmatrixW=   (^1). (6.2)^  , with a weight^1 =^2 (rt Bft)^ ,

2. Factor loadings are assumed to be constant over time. This simplies theformulas below, but can be relaxed by simply regressing the returns onthe time-varying loadings.

GivenB, (^) Y, the Gaussian likelihood is given byT
If we denote the matrix of returnst=1(2)n=^21 j^ j^1 =^2 expR ^122 (Rrtn TBf, the log-likelihood is equivalentt)^0  ^1 (rt Bft)


to jjR BFjj^2   1. We write the optimization problem asmin (^)   1 = (^2) (R BF) (^2)
We consider rst the case of a single period. In this cases:t:F^2 RmT R and F are
(column vectors. The solution is the ordinary least squares solution:of the single-period problems:B^0  ^1 B) ^1 B^0  ^1 R. In the case of multiple periods, the problem is the sumF =
Each term can be minimized independently. Hence we havekR BFk^2  ^1 =Xt^  ^1 =^2 (rt Bft)^2
As a direct extension of the previous formula in matrix form, the problem of^ft= (B^0  ^1 B) ^1 B^0  ^1 rt (6.3)
minimizingkA BXarg minkhas a closed-form solution:X kA BXk (^2) F= (B (^0) B)  (^1) B (^0) A (6.4)
6.2.1. Rank-Decient Loadings MatricesIn some cases the loadings matrix is rank-decient: even if there arethe number of independent columns isp < m. As concrete (and very common!)mfactors,
examples, consider the following two: There is a factor with loadings for each asset equal to 1. This is sometimes


called a \country", \region" or \universe" factor, since all assets are iden-tically aected by changes in this factor. The interpretation is that this isan \intercept" term in the regression. However, the same loadings matrix
contains at the very least industry loadings, which can be interpreted asnon-negative weights summing to one. For simplicity, assume that the rstfactor is the country, and the nextm 1 are industries. Then the vector
 vIn most multi-country models there are industry as well as country loadings.Say the rst= (1; ^1 ; m^1 ;:::;indare industy loadings, followed by 1)^0 is such thatBv= 0. The matrix is rank-decient.mctrycountry loadings.
We generalize this to the case where areThe vectorand the remainingv= (1;m^1 ;:::;ctryare negative ones, also annihilates^1 ; ^1 ; ^1 ;:::;m 1) ^0 , where the rstpindependent vectorsBm. indare onesvisuch
thatpossible to estimateaddress such an issue.Bvi= 0. Because of this deciency,^fusing Equation(6.1)B. There are at least three ways to^0 Bis not invertible and it is not
 The rst one is to remove the redundancy. For example, remove one industryand/or a country and/or a country factor. The benet is that we can reuse afamiliar formula. The drawback is that the original loadings matrix is easier
to interpret. We would like to know a portfolio exposure to the countryto all industries. The country exposure is telling us whether the portfoliois long or short, an information which the individual industries exposuresand
don't immediately convey. And, of course, all countries are useful. Just askthe portfolio manager whose main covered industry was removed from themodel.

 The second one is to add a small quadratic penalty term tokfk (^2). This removes the degeneracy. The factor estimates are no longer 169 kr Bfk^2 , i.e.,


```
 unbiased in the linear model, so a careful analysis would be needed beforeusing this method.Finally, we can addm pside constraints of the formC^0 f=a[Heston and
Rouwenhorst, 1994, 1995] and solve a constrained linear regression problem.This adds some (minor) complexity to the estimation process, but maintainsor even enhances the interpretability of factor returns. For example, we may
```
require that the market-weighted sum of industry factor returns be zero.This would be written asof industry factors,findis the subset industry factor returns,w (^0) Bindfind= 0, whereBindis the column subsetwis a weight
vector of asset market caps per asset. The constraint says \the sum acrossassets of market-weighted industry returns must be 0". Ifbe the weights of a benchmark portfolio, this can be read as \the benchmarkware chosen to
portfolio must have no industry returns".
6.2.2.Before we move on, we address two issues related to estimation. You won'tencounter these issues except in pathological cases. First, what are the valid?Conditions for Constrained Identication
constraintsof the constraint resulting in dierent risk models?Start with the problemC^0 f=athat remove the degeneracy? Second, are dierent choicesminfkr Bfk (^2) , whose First-Order Necessary Con-
dition (FONC) is (is given bygis in the null space off+g, whereB^0 B)fBf=, i.e.,is the minimum-normB^0 r. WhenBg= 0. We can represents all elements of thisBis rank-decient, the set of solutionsfthat solves the FONC, and


```
space as a linear combination of theV 2 vRimdened above, so(m p) g=Vx, where
BVx=0^2 Rm p
```
When we impose a constraintC (^0) f=a C^0 Vf=a, we x the values ofg:
)f)+gg==(VI(mC ^0 VV) (C^1 (^0 aV ) C^1 C^0 f^0 ))f+V(C^0 V) ^1 a
This has a unique solution as long asis a necessary condition for the constraint.Whena 6 = 0, the expected value of the factor is changed by the osetC^0 V 2 R(m p)(m p)is non-singular. This
V(C^0 V) ^1 a. This oset is irrelevant for investment purposes becauseB(V(C (^0) V)  (^1) a) = 0
and is irrelevant for covariance estimation purposes because it is constant.Factor returns are also modied by the matrixHhas the property thatBH=B. The empirical factor covariance matrixH:= (Im V(C (^0) V)  (^1) C (^0) ).
dependent on the constraintdierence is not relevant because, from direct calculation, the factor volatilityfor any portfolio is unchanged:Cis This is a dierent covariance matrix. But the
w^0 B^[ ]f+gB^0 w=w^0 BH 171
 ^fH^0 B^0 w=w^0 B ^fB^0 w


```
because of the equationBV= 0.
6.3. Estimating The Factor CovarianceMatrix
```
We have a random vector of factor returns (^) statistical model estimation, we cannot assume thatf. We assume that theft;ihave fourth moments, but unlike in the chapter on^ft, from which we want to estimate (^) fhas a special structure.
By construction, we do not expect the matrix to be spiked. The number ofsamples over which we estimate the covariance matrix is can be larger than thenumber of factors; for example, we could estimate a model with 10 factors and
500 days of estimation. The assumptionsalmost surely. Both eigenvalues and eigenvectors converge to the covarianceLet empT :=T  1 PTt=1^ft^ft (^0). By the Law of Large Numbers,mconstant,T!1seem appropriate. empT! (^) f
(also denotedmatrix. See SectionThe principal components of the factor covariance matrix also converge to theirpopulation??in the Appendix. Factor volatilities converge to the true) volatilities, and the relative standard error isp 2 =T.
population counterparts, so long as the volatilities of factors are all sucientlyseparated. This seems to settle the issue of covariance estimation: just take theempirical covariance matrix. There are several problems, though:
 Oftentimes, though, the number of factors is not much smaller than thenumber of observations. In this case, shrinkage may improve the quality ofthe estimate.
 We will see that factor return estimates are in
ated by the estimation process.This is another argument in favor of shrinkage. 172


 Factor returns are nonstationary, sometimes dramatically so at the onset ofa crisis. We need to take this into account.Factor returns are mildly autocorrelated. We need to correct for that.
6.3.1. Factor Covariance Matrix ShrinkageThe rst issue lies in the fact that the factor return estimatesestimates. They are the outcome of WLS linear regression estimates, Equation^ftare just that:
(3.16)that. The covariance matrix^2 of the estimates^ftis (B^0  ^1 B) ^1. This implies

var(^ft) = (^) f+ (B^0  ^1 B) ^1 (6.5)
ShrinkageAn alternative lens to interpret EquationInsight 6.1:Factor-Mimicking Portfolio Interpretation of Factor Covariance(6.5)is via factor-mimicking
The covariance of the returns of FMPportfolios. The return of factor-mimicking portfoliocovsuggests that we should shrink the empirical covariance matrix in order(f^i;f^j) =cov(fi;fj) + [(B 0
   (^1) B)  1 i]i;jand, which is Equationj, using Equationwiisf^i=(6.5)f(8.12)i+. This^0 , iswi.
to obtain an unbiased estimate: ^f= var(^ft) (B 0
   (^1) B)  (^1) (6.6)
2 How big is the correction? In the simpler but instructive caseSee Equation (3.17). B^0 B=Im,


(^) B (^0) ^=rBIn, and therefore, the estimated factor returns are^ft=B^0 rt, andvar(^ft) =T ^1 Pt^ft^ft^0 =
In applications the number of factors ranges between 1 and 100 and the number^ ^f=B^0 ^rB Im (6.7)
of periods ranges between 126 (six months, for daily returns) and 500 (twoyears of daily returns); therefore we are not always in the regimeand the asymptotics of Section??do not apply; neither do results for spikedp T
Wolf Shrinkage [Ledoit and Wolf, 2003a,b, 2004]. It has the advantage of beingcovariance matrix. A popular shrinkage applied to covariance matrix is Ledoit-simple to implement and to optimize, and with good performance. The shrinked
covariance matrix is
which we combine with Equation (6.6):^ f;shrink() = (1 )^ ^f+tracem^ ^fIm
(^) wheref;shrink( 2 ) = (1(0;1) is a tunable parameter. )[var(^ft) (B^0  ^1 B) ^1 ] +trace^ ^f (mB^0  ^1 B) ^1 Im
6.3.2. Dynamic Conditional CorrelationAn alternative and common approach to estimating the empirical covariancematrixvar(^ft) is to model the factor volatilities and correlations separately.


Namely, we decompose the population covariance matrix in the product of acorrelation matrixCand a diagonal matrixV containing the factor volatilities:
Bollerslev [1990] modeled the volatilities as time-varying and the correlation^ f=VCV
matrix as constant. Practitioners estimate the empirical correlation matrixand the volatility vector using exponential weighted averages with dierenthalf-lives.

diag VC^2 t:==VCXXss=0T=0T ee  s=s=VCV^ft  t s (^1) s^ft^f t ss^ft (^0)  sV t  (^1) s
whereanddaily returns, the half lives are set between three months (for exceptionallyV;C> Care normalizing constants. In many equity models estimated usingV are half-lives for factor correlations and variances respectively,
responsive variance estimations) and two years.
6.3.3. Short-Term Factor UpdatingEstimated factor returns often exhibit large, unanticipated values. Anecdotally,their volatility does not vary smoothly but discontinuously, with regimes of high
volatility, followed by a quick transition to low-volatility regimes. This poses twochallenges for the modeler. First, a simple exponential weighted estimator willreact too slowly to sudden increases in volatility. The very concrete eect of this
is that the investors will severely underestimate systemic risk at the time when 175


they need accurate estimates the most. Secondly, the estimates react too slowlytodecay no faster than exponentially, with half lives of several months. Severalreductionsin volatility. By the nature of the weighting scheme, volatilities
approaches have been proposed to address this issue. We mention one thatperforms well and is simple to implement: Short-Term Factor Updating (STFU).First, we model the multivariate factor returns so that they are modulated by

a latent state variablext: ft=ext= (^2) VtC (^1) t= (^2) t (6.8)
xt+1t=Nx(t^0 +;Im
)t
In the degenerate case wherethe factor covariance matrix isDeneut:=C t 1 = (^2) V t (^1) ft. Thenxt = 0 for allf.xt=logtk, the model reduces to one whereutk (^2)  logktk (^2). This is a linear
state-space model. Dene =:E(logktk (^2) )
xyttt=: log:=:= logt kkuttkk^22   
The state-space equation is: yt=xt+t
xt+1= 176 xt+
t


and the estimate of the state takes the formex^t= (^2) = exp" 1  e 2   1 = 0 Xs (^1) =0e s=^30 logkut sk (^2)  #
From the rst equation in modeladjusted by multiplying by the factorSome implementations use the linear approximation of this formula and the(6.8)e, the factor covariance matrix is then^xt.
approximate equalitya.s. form!1. =log(m)+Elog(ktk^2 =m)'logmsincektk^2 =m! 1
e^xt=^2 ''expexp""(1(1  ee  ^11 ==^00 ))Xs 1 =0Xs (^1) =0e es= s=^0  0 kkuupptt m msskk!   1  1 ##
The interpretation of the formula is clearest in the special case of uncorrelated'(1 e ^1 =^0 )Xs^1 =0e s=^0 kupt msk
factor returns. In this case,have unit variance. If we view the random variablesrandom variable, the termuktuis the vector of z-scored returns. Ift sk=pmgives us an estimate of its standarduias iid samples of axt= 1, they
deviation, and if this estimate exceeds one, then our original estimates for thestandard deviations of the factor need to be revised upward. That is what themodel does. The half-life 0 is typically between 10 and 20 days for daily risk
models, in order to incorporate the rapid onset of a shock. (^3) See Section 2.4.2.


6.3.4. Correcting for Autocorrelation in FactorReturns
Daily factor and asset returns usually exhibit mild, but non-zero, short-termautocorrelation. When the factor covariance matrix is estimated on shortertime intervals, the autocorrelation may be more pronounced. In these cases,
adjusting for autocorrelation improves the model's performance. Cohen et al.[1983] build on previous work by Scholes and Williams [1977] and assumethat the observed returns follow an autoregressive process of orderlmaxthat is
function of underlying uncorrelated returns. The coecients in theequation are random, but sum to 1. Let the lagged covariance matrixdened as AR(Clmaxlbe)

Then the autocorrelation-consistent estimator is given by[Cl]i;j:=cov(ft;i;ft l;j)
An alternative approach, which is asymptotically consistent in the limit^ ^f=C^0 +^12 lXlmax=1(Cl+C^0 l) T!1
is Newey and West's estimator [Newey and West, 1987]: ^f=C 0 +lXmax
l=1^1  1 +llmax(Cl+C^0 l)


6.4. Estimating the Idiosyncratic Covari-ance Matrix

Next, we need to estimate the covariance matrixestimated idiosyncratic returns^t. (^)  based on the period
6.4.1. Bootstrapping the Idiosyncratic Covari-ance Matrix
6.4.2. Exponential WeightingAs in the case of factor volatility, we use exponential weighting for idiosyncraticvolatility estimation. LetE 2 RnTbe the matrix of estimated idiosyncratic
returns, with [common choice for the diagonal terms is that of exponential weights [. The weighting matrix is a diagonal positive denite matrixE]i;t:=i;t. The exponential weighting parameter is the half-lifeW 2 RWT]Tt;t. A=
Wempirical idiosyncratic covariance matrix is thenexp:=( diagt= ); the positive constante ^1 =;:::;e T=, andis such that the diagonal terms sum tois a normalizing constant. The EWMA ^:=EWE (^0). T.
6.4.3. Visual InspectionThis matrix should be diagonal, or at least sparse. The sample covariancematrix based on estimated returns does not satisfy these requirements. The
We (the modelers) could set all the non-diagonal terms to zero, which eectivelysample covariance matrix^ ^is neither sparse nor positive denite, since 179 T < n.


amounts to a radical shrinkage of the idiosyncratic correlation matrix. Thisstep, however, is not warranted. As a sanity check it is always recommended toperform a visual inspection of the empirical covariance matrix. Oftentimes, there
are striking patterns that can be interpreted as factors that should be added tothe model. For example, some Chinese securities are listed both in MainlandChina (A and B Shares) and in Hong Kong (H shares). These securities have
highly correlated but not identical returns, and the correlations will show upin the idiosyncratic covariance matrix. In such a case, rather that assumingthat A, B, H shares are identical (they are not), it is more appropriate to add
a \share class" factor to the model.
6.4.4. Short-Term Idio UpdateIdiosyncratic returns, like factor returns, are subject to sudden changes involatility that are not captured well by exponential weighting with long half-
lifesthe shocks may occur over ten trading days. As a remedy, we reuse the SFTUmachinery, but with one minor but important modication. We use as an. A very responsive daily return model has= 126 trading days, and
example the case of equities, even though the technique is easily applicableto other asset classes. Stocks are likely to receive large shocks in proximity ofearnings, either because new information is released before or on earnings date,
or because such information becomes fully priced in the following days. Weintroduce tent-shaped variablesbe a time horizon during which earnings information is received. Dene theai;t. LetTearn;ibe the earning date, andearn
function as


ai;tranges from zero to one, whenai;t=^8 >><>>:^10  jt Tearn;ij=earntis withinifotherwisejt Tearnearn;ijnumber of days fromearn
the earnings datethose stocks within the earnings announcement window. The SFTU model issomewhat simplied by the fact that the correlation matrix is approximatelyti;earn. We use Model(6.8), but restricting our updates to
diagonal. We restrict our attention to the linear approximation: the correctiveterm is
and applies only to the assets aected by earnings.e^xt=^2 =^0 Xs^1 =0e s=^0 sPiai;tP(ii;tai;t=^i;t)^2
^i;t^2 h(1 ai;t) +ai;te^xti^^2 i;t
6.4.5. O-Diagonal ClusteringFinally, we need to identify those assets whose idiosyncratic returns are highlycorrelated. Two instances are important. The rst one is the case of dierent
securities that refer to the same underlying asset. For example, some stocksare listed as dierent share classes; for example, Berkshire Hathaway tradesunder BRK.A and BRK.B, with dierent fractional values. The liquidity of
the two securities diers; yet, their returns are highly correlated. Whetherto include the two securities in a factor model or not depends on the nature


of the trading strategy employing the model itself. If the strategy intends toexploit the temporary small mispricing between two assets, then we shouldinclude both assets. If instead we only intend to invest in the company based on
fundamental information, then we should only include a security representativeof the underlying asset; typically we choose the most liquid asset. The secondinstance instead has to do with stocks whose dependencies are not described by
factors. In order to be identiable, factors must be pervasive. A factor in
uencingonly a handful of assets is not a factor, and cannot be identied in a largecross-section of assets. The dependency among these stocks is still detectable in
the correlation between their idiosyncratic returns. To identify them, we resorttosimple clipping operator:correlation thresholdingthres. We transform the correlation elements by applying a(i;j) :=i;j 1 fji;jj> g. The optimal threshold
instructive to explore the clusters emerging for dierent values of the threshold.For some value ofisKplogn=T, for some positive constant, the clusters are a) stable, in the sense that they do notK. In practice, however, it is more
change much for perturbed values of the threshold; b) interpretable, in the sensethat they are comprised of \similar" stocks, in the sense that they belong to thesame sector or industry, and sometimes they have similar style factor loadings
as wellcorrelation matrix is positive denite (and well-conditioned). As an example, weuse the residual returns from a commercial factor model (Axioma US V.4, Short^4. It is important to check that, for every level of the threshold, the
Horizon, AXUS4SH). We use the residual returns for year 2010. We computethe equal-weighted correlations for continuous constituents of the Russell 3000 4
factor loadings, and given this similarity measure, propose a more systematic thresholdingprocedure, but it would fall beyond the scope of the book.We could characterize more rigorously this within-cluster similarity as a distance in among


index, and threshold their absolute values at 0.55. Graph 6.1 shows the resultingclusters. The number of stocks is small: less than 90, out of a set of nearly 2,900stocks; about 3%. Table 6.1 lists tickers and associated names. The pairs are
quite intuitive: Visa and MasterCard; Wynn and Lass Vegas Sands; PeabodyEnergy and Alpha Natural Resources; and a mining cluster composed of HL,NEM, CDE, RGLD.


DSW

```
FMR NALHMA
XCO ALY
BTH
```
```
AMLN
MA
```
```
AVNR
ALTR
```
WL

```
LVS
ARQL
AAI
```
HL

```
GCA
NEM
FTO KG
```
MNTA

```
SVR
ANR RCL
```
```
MTG PMI
RGLD
MDVN
HOT RVI
```
```
MWW CYH
MFE
```
```
DYN
CASY
```
```
ALKS
V XLNX
```
```
ATSG SUR WYNN
ACV
```
CMTL

HOC ACTI

QLGC

```
NCI
BTU CCL
```
```
RDN
CDE
NOVLMAR
```
Figure 6.1:correlation; red links (lighter) negative correlation.Clusters for idiosyncratic matrix. Blue links (darker) denote positive


Table 6.1:TickerAAIACTIACVALKS NameAIRTRAN HOLDINGSACTIVIDENTITY CORPALBERTO CULVER CO NEWALKERMES INCTicker and company names of cluster components in Figure 6.1.TickerHOTKGLVSMA NameSTRW HTL RES WRLWDKING PHARMCUTCLLAS VEGAS SANDSMASTERCARD INC
ALTRALYAMLN AMYLIN PHARMACEUTICALS INCANRARQL ARQULEATSGAVNR AVANIR PHARMACEUTICALS INCALTERA CORPALLIS CHALMERS ENERGY INCALPHA NATURAL RESAIR TRANSPORT SERVICES GRP I MARMDVN MEDIVATION INCMFEMNTA MOMENTA PHARMACEUTICALS INCMTGMWW MONSTER WORLDWIDE INCNAL MARRIOTT INTL INC NEWMCAFEE INCMGIC INVT CORP WISNEWALLIANCE BANCSHARES INC
BTHBTUCASYCCLCDERCLCMTL COMTECH TELECOMMUNICATIONS CP RGLDBLYTH INCPEABODY ENERGYCASEYS GEN STORES INCCARNIVAL CORPCOEUR D ALENE MINES CORP IDAHOROYAL CARIBBEAN CRUISES LTD NCINEMNOVLPMIQLGC QLOGIC CORPRDN NAVIGANT CONSULTING INCNEWMONT MINING CORPNOVELL INCPMI GROUP INCRADIAN GROUP INCROYAL GOLD INC
CYHDSWDYNFMRFTOGCAHL COMMUNITY HEALTH SYS INC NEWCO RVIDSW-ADYNEGY INC DELFIRST MERCURY FINFRONTIER OIL CORPGCA HLDGSHECLA MNG CO SURSVRVWLWYNN WYNN RESORTSXCO RETAIL VENTURES INCCNA SURETY CORPSYNIVERSE HLDGS INCVISA INCWILMINGTON TRUST CORPEXCO RESOURCES INC

6.4.6. Idiosyncratic Covariance Matrix Shrink-HMAHOC HEALTH MGMT ASSOC INC NEWHOLLY CORP XLNX XILINX INC
Analogously to the shrinkage of factor covariance shrinkage of Section 6.3.1 ,we recommend to shrink the idiosyncratic variances toward the identity matrix:age
For a diagonal idiosyncratic covariance matrix, this is analogous to shrinking^ ;shrink() = (1 )^ ^+tracem^ ^In
the idiosyncratic variances toward the empirical average of the variances.


6.5. Winsorization of ReturnsThe issue of outlier detection is, if not central, at least very important both forrisk modeling and alpha research. There are many instances of outliers in return
data, each one of them responsible for ruining the career of a nance researcher.Before proposing some remedial measures to improve the research processand save a few careers, let us discuss where they come from, and the impact
that they may have. The sources of outliers are primarily two. First, the dataprovider may be providing generally low-quality data. This is, unfortunately,quite common, and good researchers spend a large proportion of their time
evaluating and comparing data and questioning providers on the data collectionmethodology and their applicability. The sources of error are too many to list.In the worst case, prices are not correctly adjusted for stock splits or reverse
splits. Data collection may not be synchronous; the ultimate source of thereturns may be a broker located in a farming village in New Zealand, and evenmore unlikely instances. Bad providers are the perfect breeding ground for

outliers. Secondly: authentic outliers do exist. Instances are: There are rare stray transactions for a liquid stockVery illiquid stocks exhibit higher volatility, and occasionally large returns, (^5).
 even intraday.Stocks in the process of being delisted, or entering/exiting bankruptcy, usuallytrading over the counter (OTC) also exhibit very large returns.
2000. One day, at the closing auction, Enron's stock price jumped from $90 after vibratingaround $86 all day. And peopleshort Enron now?". The stock fell back to mid-80s the day after. Lesson: if traders want to^5 If I can self-indulge in a personal recollection: I was working for Enron in the summer ofon Enron's trading 
oorwere openly wondering \should we
short themselves, then it's a likely outlier of some kind. 186


 There are genuinely large jumps re
ecting new information in the market:surprises in earnings and forward guidance, announcement of market entryby a competitor, merger announcements and news of merger break, accidents

Of these instances, the rst one can be dealt with by inspecting price dataor likely new and unforeseen liabilities, and macro-economic drivers having alarge impact on the security's price.
carefully; i.e., by not only taking the last price of a ve-minute interval, butby inspecting the entire price trace. The second and third can be avoided bychoosing the estimation and investment universe carefully. Microcap stocks
that are very illiquid should be excluded. The last class of outliers, howeverlarge they may be, shouldmain rationale is that this exclusion will make the output of the analysis muchnotbe excluded from the estimation process. The
less reliable. If we winsorize a large absolute return, we aect the estimatedfactor returns from the cross-sectional regression. A factor's return is the returnof its mimicking portfolio, and by winsorizing returns in the cross-sectional
regression, it is eectively the portfolio return using winsorized data. The trueportfolio return unfortunately is based on historical returns. This aects theevaluation of the factor returns, as well as of the idiosyncratic returns. Two
easy qualitative recommendations that follow from all of this is are:1. whatever winsorization method you use, make sure to report all theinstances of winsorized data in a a backtest or in production, and examine

2. them one by one.make sure that your investment universe comprises only liquid, tradableassets.


For the remaining assets, use a robust outlier detection strategy. There is noideal and completely justied method. A method that works well enough is tocompute at the security level, the robust z-score of return:

and to winsorize returns exceeding a thresholddi;t=median(jlog(1 +jrlog(1 +i;t ^1 )j;:::;ri;td)maxjjlog(1 +. The threshold depends onri;t T))j
asset class, region and other attributes, and is set by trial-and-error between 5and 10.


6.6. Selecting Factors: the Large Num-ber of Predictor Case
Status: This is too speculative/advanced to make it in the book.Oftentimes, we encounter the case of large number of predictors.
standardize to have unit norm and zero mean, from which we want to deriveloadings matricesThe primitive is a set of matricesBt 2 Rnm. The matricesAt^2 ARntwon't do as loadings, since thep, withpn, with columns
cross-sectional regressions are undetermined, and, even in the caseresult in poor performance. One natural approach is to determine factors asa linear combination of predictors. As a special case of their approach, we setp.n, would
Bsolve the estimation problem,t=AtC, whereC 2 Rpmis time-invariant.Cneeds to be identied. We
mins:t:CXt 2 kRrtp mAtCftk^2
We solve this problem by considering a simpler instance, and then generalizingft^2 Rm

it. We solve a single-factor estimation problem:minXt krt Atcftk (^2) (6.9)
s:t:cft 22 RRp (6.10)(6.11)


(This can be solved alternating by alternating Least Squares, minimizing overf 1 ;:::;fT) 2 RTandc 2 Rp.

Procedure 6.2:1. Seti= 0 and initializeas c(0)such that (^) c(0) (^) = 1, tol>0.
2. Estimate ft(i)=((c(ir)) (^0) t 0 AAt (^0) tcA(i)tc(i))
3. Set4. Set5. If6. Return (^) cxc((i:=i)) =cc=Px(=i ctk((1)ixf) t(kandi.)>)^2 tol, setAft^0 tA=tft+(ii) (^) .Pit+ 1 and go to 2.ft(i)A^0 trt.
guarantee that the matrixhas rankNote that we use the Moore-Penrose pseudoinverse, because there is non, and the sum ofPTtAmatrices has rank at most^0 tAt 2 Rppis invertible. Each matrixn+T, which is inA^0 tAt
general smaller thanmatricesAt: p. Once the solution has been found, we orthogonalize the
And then we iterate Procedure[A~t];i:= [At];i [kA[At]^0 t;i]A;ikt^2 cAtc (6.12)


6.7.6.7.1. Linking Models?Advanced Model Topics
In some applications, you will have an investment universe consisting of securitiesbelonging to dierent countries. Large hedge funds, for example, invest at leastin North America, Europe, and Asia. In other applications, the universe will
consist of securities belonging to dierent asset classes. An example is US equityand corporate credit, but the possibilities are endless. Since the mathematicaltreatment that will follow is somewhat dry and arduous, it is perhaps worth
asking the question: why? What are the uses of an integrated model? Rathersubjectively, I think there are two major uses. The rst one, and the mostcommon, is for rm-wide (or large business-wide) risk management. Weneedas
accurate a measure of rm-wide of volatility as possible. Being wrong by 50%in excess or defect on the rm vol is either damaging returns because we believewe have deployed more volatility than we actually have, or it is deadly, because
we are running a great deal of unwanted volatility and unwanted risk of a largedrawdown. The second use case is {but of course! { that we have a strategy thatfundamentally exploits joint properties of heterogenous investment universes.
We need a factor model for alpha research and portfolio optimization. In mypersonal experience, linking models is the last of your problems, except when itis youronlyproblem.
classes and geographies; Figure 6.2 shows simplied instances of geography andasset-class models. In practice, though, the modeler is faced with three options.In principle, it is possible to build a \model of everything", across asset
The boundaries between them are not perfectly demarcated, the descriptionwill target only the idealized cases.


Covariance MatrixEquity Factor

```
Covariance MatrixCredit Factor Credit-Equity Covariances
Equity-Credit Covariances Covariance MatrixUS Equity Factor
```
```
Covariance MatrixEU Equity Factor EU-US Equity Covariances
US-EU Equity Covariances
Figure 6.2:factor covariance matrix.Left: credit-equity linked factor covariance matrix. Right: country-linked
```
1. You may want to jointly model all the assets. This is not any dierent fromjointly modeling assets belonging to dierent sectors in equity models.You could include country factors in the models, and do business as usual.
2. You may develop separate models (which we callassets belonging to dierent geographies and then combine the modelsin a second stage. The distinguishing feature of this approach is that welocal models) for, say,
    want to make sure that the integrated model, when is applied to portfolioscontained in each local model's universe, should be identical to that ofthe local model.
3. You may model the assets jointly in a rst stage, and then in a secondstage model the residual returns obtained from the rst stage in separatemodels.
We discuss the three approaches, their benets and drawbacks, below.1. Integrated Modeling. This approach is conceptual straightforward, and


has the advantage of giving the model a greatest deal of 
exibility whenmodeling the relationships between securities in the model. For example,in an equity-corporate credit model we may want to create a factor de-
scribing Investment Grade vs High-Yield classication. This factor couldaect both IG bonds and stocks of companies issuing IG bonds. Suchspecicity and domain knowledge is best incorporated in an integrated
model. Moreover, if the model is used for trading, alphas and factor-mimicking portfolios should be developed and tested for the combinedinvestment universe. There are some complication. One is the asynchrone-
ity in returns due to dierent time zones, when securities are in multiplecountries. Another complexity is in the misaligned trading calendar. Trad-ing holidays dier by country, so we have to deal with pairwise incomplete
observations in cross-sectional regression, which result in missing factorestimates for country factors on certain days. These, in turn, can resultin non-positive denite factor covariance matrices. There are possible
strategies to address some of these issues, which we outline below. One way to address asynchroneity for daily models is by aggregatingreturns over multiple days, ranging from two to ve. This way, returns
become largely overlapping. The number of observations within atime window is reduced accordingly, and the idio volatility scalesapproximately as sqrt(aggregation window).
 Asynchroneity induces cross-autocorrelation in factor returns. Oneway to partially address the problem is by applying the Newey-WestEstimator to the covariance matrix.
 Finally, one can address asynchroneity by explicitly modeling returnsin a state-space framework. Such a treatment falls beyond the scope of


```
 this book. For an instance of this approach, see Burns et al. [1998].Regarding missing returns, one possible approach is to estimate thecovariance matrix on complete observations across all local models.
The availability of data for all local models on the same dates willinsure that the factor covariance matrix is positive-denite. It is alsopossible to estimate factor returns (for, e.g., performance attribution)
on incomplete observations. This approach has the drawback thatfactor-mimicking portfolios have potentially high turnover on dayswhen the estimation universe changes due to missing returns for certain
local models. Yet another approach is to not to drop local models ondates when their are not available but instead to impute returns fortheir assets. We won't cover it here 6
 Regarding missing returns, it is also possible (although slightly unholy)to estimate factor returns on all dates, and then estimate individualfactor covariances using pairwise complete observations. The factor
covariance matrix will not be necessarily positive denite, but it mayturned into a positive denite matrix by shrinking the o-diagonalcovariances between two local models. We are in uncharted territory.
```
2. Separate Modelingtegrated modeling can be both powerful and dangerous. In the nextHic sunt leones.. From the previous item, we know that detailed in-
6 approach, we seek to keep most of the benets of the integrate approach,while keeping all the benets that come with preserving local models. In
involved in imputation of missing data is high, and the return on the eort in this case iscomparatively low.As a justication for opting not to cover this subject, I note that the technical sophistication


the analysis below, we have as primitive data local models. We denotethe local factor covariance modelsintegrated model, whose factor covariance ^(1)f ;:::; ^(f(fIq)). In addition, we have an(\I" is for "Integrated")
estimated using the joint factor returnsmatrices so thatof marketi, andVVi;ii;jis the estimated covariance matrix for the universeis the matrix of covariances between securities inf(1);:::;f(q). We partition its sub-
marketiand marketj. The idiosyncratic matrix is block-diagonal.
^(fI)=^266664 VV::: ::: :::^1 q;;^11 :::::: VV^1 q;q;q^377775 ^(I)=^266664 ^::: ::: ::: 0 (1) :::::: ^^0 (q)^377775

Here is the form of the integrated model: (^266)
666664 rrr:::(1)(2)(q)^377777775 =^266666664 B::: ::: ::: ::: 00 (1) B^00 (2) ::::::::: B^00 (q)^377777775266666664 fff:::(1)(2)(q)^377777775 +^266666664 :::(1)(2)(q)^377777775 (6.13)
The integrated model's covariance matrix is ^(rI)=B(I) ^(fI)(B(I)) (^0) + ^(I)
Let us go back to our challenge. The local models are valuable, becausethey are estimated using all the information (e.g., all the trading dates foreach market) and all the factor-specic information at our disposal. Yet,
the cross-market covariances are valuable too to quantify joint risk; thatis the point of having a linked model. The idea is to develop a \minimal


rotation\block covariances are the local model covariancesto require the rotation to be block-diagonalCthat transforms ^(fI)into a matrix where the main diagonalC:= ^(fidiag). It will be sucient C(1);:::;C(q),
with (this is the clever bit)be close to the identity, because we expectsimilar. Let us write the rotation down (the \IR" superscript stands forC(i)=V i;i^1 =^2 ( ^(fi))^1 V=^2 i;i. Note thatand ^(fi)Cto be very(i)should
\Integrated Rotated"):
^(fIR)=^266664 C::: ::: 001 ;^1 :::::: C^00 q;q^377775266666664 VVV::: ::: :::^12 q;;;^111 ::::::::: VVV^12 q;q;q;q^377777775266666664 C::: ::: :::^001 ;^1 ::::::::: C^00 q;q^377777775
=^266666664 VV^~~::: ::: :::(1)f^2 q;;^11 ::::::::: VV ~~^(f^12 q;q;q)^377777775

Here,by post-multiplying it byloadings, and as a result we would not preserve the local market model.V~i;j:= (C(i))^0 Vi;jCC(j ). Note that we are not transforming (^1). Doing so would change the local marketB(I)
In other words, we are not actually rotating the entire model; we are onlyperturbing the factor covariance matrix by a small amount, for alignmentpurposes. The error induced in theV~i;jis small and should be tolerable.
Finally, a step that is often performed in this procedure is block shrinkage,so that, for some parameter >0, the nal covariance matrix takes the


```
form (the \IRS" superscript stands for \Integrated Rotated Shrinked"):
^(fIRS)=^266666664 ^ ^VV::: ::: :::~~(1)f^2 q;;^11 ::: ::: ::: VV^~~(f^12 q;q;q)^377777775
```
3. Multistage Modelinga both \global" and \local" factors. The global factors describe the co-movements among securities across all local markets. The local factors. There are use cases in which we would like to have
    are instead aecting only the securities in their markets. The appeal tothis approach is that the global factors describe all the dependenciesacross markets, so that, given the knowledge of these factor returns,
    the local markets are independent of each other. We describe a way toobtain such a model. As a primitive, we need an integrated modelor and integrated and rotated model ^(fIR). In addition, we need global ^(fI),
    characteristicscharacteristics are: a global \country" factor (all loadings equal to one);B(G) 2 RnmG(\G" is for \Global"). Examples of these
    In the rst step, we perform cross-sectional regressions on the integrated a global market factor;global style factors, namely momentum, volatility, and value.


universe: (^2666)
66664 rrr:::(1)t(2)t(tq)^377777775 =B(G)gt
and as an output we obtain global, factor returnsglobal factor returns into a matrixIn the second step, we regress the local factors agains the global factors:G 2 RmGT, whose columns aregt. We arrange thegt.
The solution to this regression is given byft(i)=C(i)gt+~f^7 t(Equation (6.4):i)
The matrix is the output of the Weighted Least Squared Regression, andC(i)= (G^0 G) ^1 G^0 F(i)
is equal to. In the third step, we replace these formulas in the IntegratedFactor Model Equation (6.13): 2
66666664 rr:::(1)(2)
r(q)
(^3777777)
75 =
(^2666666)
64 BBB(1)(2)(q:::)CCC(1)(2)(q)
(^3777777)
75 g+
(^2666666)
64 B::: ::: ::: :::^00 (1) B^00 (2) ::::::::: B^00 (q)
(^3777777)
(^75)
(^2666666)
64 ~f~f~f:::(1)(2)(q)
(^3777777)
75 +
(^2666666)
64 :::(1)(2)(q)
(^3777777)
(^75)
is generally not the case. However, it is possible to further rene the model in order to allowfor heteroskedasticity. Turtles all the way down.^7 Note that we are assuming here that the local factor returnsft;j(i)are homoskedastic. This


```
We must check that the returns vectorsapproximately uncorrelated. In this case, the factor covariance matrix isgt;ft(1);:::;ft(q) are pairwise
If that is not the case, then we have three options. First, nd \better"diagcov(gt);cov(ft(1));:::;cov(ft(1))
global factors while keepingorder to achieve our goal. Lastly, give up nance altogether.mGconstant. Second, add global factors in
6.7.2. Currency RebasingIn a multi-country factor model the return of an asset is usually expressed in adierent currency than the one in which the asset is traded. Consider the case of
a US-based manager trading a security denominated in Euro. The Dollar/Europair is apurchase the currency in which the security is traded (the Euro), also calledcurrency pair. In order to purchase a Euro-denominated security, we
```
therate is the dollar amount needed to buy one Euro. More details on usage: whenreferring to a currency pair, the ordering is base-quoted. In this case: EURUSDbasecurrency, and sell dollars, thequotecurrency. The direct exchange (^8).
exchange rateLet us denote thereciprocal of the direct exchange rate. The exchange rate return is dened asis the exchange rate of the reversed pair, and it is equal to thedirect exchange ratein periodtbypEURUSD(t). Theindirect
the return received by holding the base currency in one period, and is equal torcEURUSD 8 (t) = [pEURUSD(t) pEURUSD(t 1)]=pEURUSD(t 1). We dene the
EUR, GBP (UK pounds), AUD (Australian dollars), CAD (Canadian dollars), CNY (YuanRenmibi), JPY (Yen).The currency codes are identied by three letters. The most common currencies are USD,


currency returntion, in which we buy and sell the currency on consecutive days. We denoteLet us analyze rst the realized return of holding EUR in a simple transac-rci;iwhen the base and quote are the same to be zero.
byepochs for the two currencies. On day 0, we borrow $1 and and purchase 1rfUSD,rfEURthe risk-free return in the interval between the two transaction=p
 On day 1 the EUR holding is worth (1 +dollars at the pricepEURUSD(1). The dollar amount we are left with isrfEUREURUSD)=pEURUSD(0) EUR.(0). We buy back
(1 += (1 +rfEURrEURf)pUSDEUR)(1 +rEURUSD(1)=pEURUSD) (0)
We then pay our USD loan for an amount(1 +rEURf )(1 +rEURUSD )  1   1  rfUSDrfUSD. We are left with
Let us extend this result. Instead of holding the EUR in a cash account, we'rcEURUSD+rfEUR rUSDf
invest it in a security withcalculations, the return islocalreturn (in EUR) equal tor. Following the same

```
rre:=:==rrrle ++rrrfEURcEURUSDcfEURUSD rfUSD
gEURUSD:=rcEURUSD+rEURf  rUSDf
```

The return is the sum of two components: rst, the local excess returnrrisk-free rates. rEURf. Second, the currency returngEURUSD, adjusted by the dierence inre:=
three (or more) currencies. Let us denote the currencies by an indexA no-arbitrage argument implies thatThere is yet another identity of interest. This links the currency returns ofpk;i(t) =pk;j(t)pj;i(t), and from thisi2f 1 ; 2 ; 3 g.
relationship and the linear approximation we obtainwhich the identity holds: rck;i=rk;jc +rj;ic, from
Now we consider the problem of changing numeraire. For example, we want togk;j:=gk;i gj;i
change the numeraire from USD to GBP.re+gEURGBP=re+gEURUSD gGBPUSD (6.14)
Let us say that our factor model contains securities traded inassets total return can be decomposed into the sum of a local return and anexchange rate return: qcurrencies. The

The matrixC 2 rR=n(local factor structure)qis binary, with [Bf| {z+} C+]i;j(currency factor structure)= 1 if assetCg|{zk^0 }ihas reference currency

jquoted currencytransforming the currency returns. Letand 0 otherwise. The returnk 0 We rebase from currencygik^0 is the return of the base currencyA 2 Rqqk (^0) a matrix whose elements areto currencyk 1 by way ofi, with


all zeros with the exception of [gk (^1) =(IqA ];kA (^1) )= 1.gk 0
We close this section with several comments related to modeling extensions)r=Bf++C(Iq A) ^1 gk^1
and practical implementation: We have ignored the question of modeling the joint distribution of the spotcurrency returns.gk (^0). One natural avenue is to model those using a factor
We need to model the relationship only with respect to one quote currency.model, either fundamental or statistical, so that we can expressFor simplicity, we have also ignored the correlations betweenfgkand^0 =Hg. The+.
model is r= (^264) B Cf;g
 Currency risk depends heavily on institutional arrangement. For example,Cg;g C^375264 fgk^0375 +
an investment rm may have a xed capital housed in a dierent country,and trade using only this capital as collateral. The net exposure is xed Inthis case the foreign currency exposure is given by the capital level, which is
usually hedged by currency forward contracts.
6.8. A Tour of FactorsThis chapter would not be complete without at least a cursory description offundamental factors. Because factors should explain cross-sectional returns,


they feature prominently in the nancial literature exploring return anomaliesand extensions to the CAPM or the standard Fama-French three-factor model.The literature on these factors is very large; see Harvey et al. [2016], Green
et al. [2013], Ilmanen [2011] for surveys. Marketthe vector. By far the most pervasive factor in the model, it is usually eithereor a vector of regression coecients of the asset total return
to a \market" factor return (e.g., SPX or RUA in the US). In the rst case,the interpretation is that every return is identically aected by the market,and it is left to other factors to capture the dependence on.
 Countries and Industriesvariables summing to 1 for each asset. We consider these factors as homo-geneous not only because the information is coded in the same way in the. Countries and Industries are represented as 0/1
factor loadings, but also because the relative importance of the two has beena subject of intense study both for nancial economist and macroeconomists.Aside from the papers by Heston and Rouwenhorst cited above, see also
 Brooks and Del Negro [2005], Cavaglia et al. [2000], Berben and Jansen[2005], Puchkov et al. [2005], Miralles Marcelo et al. [2013].Momentum. Stocks that have outperformed (underperformed) their peer over
the three to twelve month previous to a given date outperform (underperform)their peers in the future. Jegadeesh and Titman document this anomaly inthe academic literature Jegadeesh and Titman [1993]. They review 20 years
 of literature in Jegadeesh and Titman [2011]; a more recent survey is Wiest[2023].value
 low beta/low vol 203


6.9. Further ReadingFactor zoo: Bender et al. [2013], Bryzgalova et al. [2022], Jacobs [2015], Harveyand Liu [2020], Freyberger et al. [2020]
What Factors Matters? Harvey et al. [2016], Kagan and Tian [2017], Feng et al.[2020], Chen and Velikov [2019], Jacobs [2015] Covariance Thresholding: BickelAlternative Data: Kolanovic and Krishnamachari [2017]
and Levina [2008], El Karoui [2008], Cai et al. [2016]


# Chapter 7Statistical Factor Models

## In the statistical model framework we assume that we don't know neither thefactor returns nor the exposures; we estimate both. The estimation relies ofPrincipal Component Analysis. Starting with Chamberlain [1983], this approach

## has been motivated using an asymptotic argument: if the number of factors isnite, saythen when the number of assets is large, there is a clear separation betweenm, and if the specic risk stays bounded over bounded portfolios,

## theconstitutes then a good approximation and, in the limit, the PCA solutionconverges to the true model. In applications, one may question the merit ofmlargest eigenvalues and the remaining eigenvalues. The PCA solution

## an approach that, unlike the fundamental and macroeconomic ones, ignoresadditional information about the rm characteristics or the macroeconomicenvironment. Developing a statistical model is useful for several reasons:

##  Complementarityof each individual model. We can project an existing model on the statisticalmodel, or augment it with statistical factors.. Using several models helps understand the shortcomings

##  Optimizationcompare solutions in which we have bounded the total factor variance usingdierent models; or, we could include. In a portfolio optimization problem, it is often benecial tobothconstraints;

##  Data. In certain asset classes, rm characteristics or relevant macroeconomic 205


 factors may not be available. In the case of joint return estimation Whenonly returns are available, statistical models are the only option;Availability at Short Time Scales. At certain time scales, such as one- or-ve-
The main disadvantage of statistical models is that its loadings are less inter- minute intervals, fundamental factors may not be as relevant;Performance. A statistical model may just outperform the alternatives.
pretable than in the case of alternatives estimation methods. The rst factor isusually easy to interpret as the market. The second and third onesinterpretation. For example, Litterman and Scheinkman [1991] interpret threecannd an
statistical factors as level, steepness and curvature of the bond yield curve.The situation is not helpless; in Section 7.4 I describe approaches to interpretstatistical models. In the words of Johnson and Wichern [2007], \Analyses of
principal components are more of a means to an end rather than an end inthemselves because they frequently serve as intermediate steps in much largerinvestigations". This is perhaps true of all factor models, but is certainly more
true with regards to statistical models, because of the possible challenges ininterpretation.This chapter starts with a minimal description of the approach. Then, we
take a detour in the real world.
7.1. Statistical Models: The Basics7.1.1. Best Low-Rank Approximation and PCA
Letof returns in periodR 2 RnTthe matrix of observed returns, whoset; the matricesB 2062 RnmandF 2 tth column is the vectorRmTdenote a matrix


of loadings and of factor returns respectively. If we wanted to nd the loadingsand factor returns that minimized the total \unexplained" variation of returns,summed across periods and assets, then we would solve the problem
wherekkF is the Frobenius norm. A matrix of the formminB;FkR BFkF BFabove has rank(7.1)
less than or equal tomcan be decomposed asm. Conversely, every matrix with rank less or equal thanBF(Exercise 7.1). The problem can be restated as
Here, we have not specied whether the norm is Frobenius. It could be Frobenius,rank(minR^)m^ R R^^2 (7.2)
but it could be also any unitarily invariant norm[1936] and generalized by Mirsky [1960]. We use theThis minimization problem was formulated and solved by Eckart and Young^1. Singular Value Decompo-
sitionSingular ValuesT respectively, and^2 ofR=USV) on the main diagonal (i.e., [S^0 , witha matrix of sizeU,Vsquare orthonormal matrices of sizenT, which has positive values (calledS]i;i) and zero values elsewhere.nand

The solution to Problemsingular values after the[Golub and Van Loan, 2012] in compact form asm(7.2)th one set to zero. The solution can also be writtenis given byR^ =RUS^ =mVUm^0 SwheremV (^0) m, whereSmhas theUm
andmatrices: (^1) These are matrix norms that are invariant for left- and right-multiplication by orthonormalVmkare the matrices obtained taking the rstAk=kUAV (^0) k. Spectral, Frobenius and nuclear norms are unitarily invariant.mcolumns ofUandV, and
Bau [1997].^2 This is referred to as the Full SVD, as opposed to the reduced SVD; see Trefethen and


SThen, the original Problem (7.1) is solved by settingmis the square matrix obtained taking the rstmcolumns andmrows ofS.

BF==USmmV (^0) m (7.3)(7.4)
As noted in earlier chapters, there are equivalent \rotated" solutions, of theformthis is also a solution:B~ =BC,F~=C  (^1) F, for some non-singularC 2 Rmm. For example,
BF==UVm (^0) mSm (7.5)(7.6)
Component AnalysisA related problem, with which many readers are acquainted, isOur goal is to generate a linear combination of the original vectors. In this setting, we start with a covariance matrixr^Principal (^1) ;:::; 2 RnrTn,.
i.e.,have unit Euclidean norm. We want these random observationsthe greatest possible variance. With a little work (which we did in previousw^0 r^1 ,:::,w^0 rT; the vectorw 2 Rnis a vector of weights, normalized tow (^0) rito have
chapters; or do Exercise 7.4), you can show that this variance is equal toThe problem than can be stated as w^0 w^.
maxs:t:wjjw^0 w^jj 1 (7.7)
The vectorProblem(7.7)wis called theas a nancial problem too: nd a maximum-variance portfolio,rst principal componentof^. You can interpret


where the sum of the squared net notional positions is less or equal than 1.The connection between PCA and eigenvalue problems is well known, but itstill useful to highlight it. The Lagrangian of Problem(7.7)isrw(w (^0) w^ ) +
the Lagrangian be zero. This is equal to the eigenvalue equationFrom this equation it follows thatrw(1 kwk^2 ) = 2w^   2 w; a necessary condition for the maximum is that=v (^0) v^. Therefore, the solution is thev^ =v.
eigenvector with the highest associated eigenvalue.process and nd another maximum-variance portfolio that is orthogonal toOnce this maximum-variance portfoliow(1)has been found, we repeat the
w(1): maxw (^0) w^ (7.8)
s:t:jjww (^0) wjj(1) (^1) = 0
To see the relationship between PCA and SVD, we write the uncenteredcovariance matrix using the SVD decomposition:
Replace this decomposition of^=^T^1 in the optimization problem, Equation (7.7),RR^0 =T^1 US^2 U^0 (7.9)
and notice thatjjUwjj=jjwjjbecause the matrixUis orthonormal. We are


left to solve maxv (^0) S (^2) v (7.10)
s:t:jjwvw 2 =jjRUvn 1
The solution is straightforward:column ofthat the columns ofU. If we were to nd the rstUmsolve our problem. These columns, however, are notv= (1m; (^0) principal components, we would nd;:::;0)^0 , andwequal to the rst
uniquely identied when two or more eigenvalues are equal. For example shouldverify for yourself that, ifv 12 +v (^22) = 1, is indeed a solution. Figure 7.1 gives a geometrical interpretation 1 = 2 , then any vectorv= (v 1 ;v 2 ; 0 ;:::;0), with
of this fact.andWe call these vectors interchangeablyEigenfactors. The variances of the components are the squared singularPrincipal Components,Eigenvectors,
values of the SVD. R¼
R½R®½ R¾ R®¾
Figure 7.1:identied. The eigenvectors associated to identical eigenvalues are not uniquely 210


the case ofFinally, we note that the optimization problemmeigenvectors: (7.7)can be extended to

max traces:t:WW (^0) W 2 RW=nI^0 mWm^  (7.11)
7.1.2. Maximum Likelihood Estimation and PCAThe statistical model was introduced as a norm-minimization problem, but isnot directly related to a factor model formulation
In fact, if we approximated the covariance matrix with a principal compo-r=Bf+ (7.12)
nent approximation using the topcovariance matrix, which is highly undesirable.The goal of this section is to establish a rst connection between spectralmeigenvalues, we would obtain a singular
methods and the standard factor model. We consider the model above as astarting point. We assume for simplicity thatvolatilities, are all equal to. Furthermore we assume, without loss of generality, 1 ;:::;n, the asset idiosyncratic
thatchoice of covariance matrix.Under the assumptionsf=Im. This is allowed, because rotational invariance aords us thisfN(0;Im) andN(0; (^2) In) the return covari-
ance matrix isare greater thanThe log-likelihood function for a zero-mean multivariate normal distribution isBB 20 +(Exercise 7.5). Let^2 In. The rstmeigenvalues of the covariance matrixrbe the empirical covariance matrix.


[Johnson and Wichern, 2007, Bishop, 2006]L(^r) = T 2 hlog (^) ^r (^) +h^ r (^1) ;ri+nlog(2)i (7.13)
where we denote the scalar product of two matricesparametersB;can be estimated via maximum likelihood:hA;Bi:=trace (A^0 B). The
maxs:t: ^rlog=B^ ^^B^r^0 + ^ h^ (^2) I rn^1 ;ri (7.14)(7.15)
Bishop, 1999]. DecomposeThe solution to this problem is especially simple and intuitive [Tipping andr=USU^0. Then
^B^^2 ==Um(S^2 m ^^2 In)^1 =^2 (7.16)
whererotation of this risk model is:is the average of the lastn meigenvalues ofr. An alternative
Bf==(=USIm^2 mn  In) (7.17)(7.18)(7.19)
The model oers several insights. First, it links a probabilistic model of returnsto the PCA of the empirical covariance matrix. Second, in the model rotationabove, the factor covariance matrix is diagonal and the factor variances are
equal to the shrinked empirical variances obtained by PCA. Indeed, the PCA 212


solution can be obtained as an asymptotic result. consider the limitthis scenario, the idiosyncratic risks are much smaller than the factor risk. Inthe limit, the formula then simplies to ^#0. In
Bf===0US^2 mm (7.20)(7.21)(7.22)
which is the Principal Component Analysis solution.T= 250,We show how PPCA works in a simulated instance. We choosenequal to 1000 and 3000 assets,m= 10 and factor volatilities equal= 1
(a), (b) show the true (population) factor variances on the x axes. On the y-axesto 1we plot the sample factor variances (circles) and the shrinked factor variances;^2 ;:::;10. For each set of parameters, we run 50 simulations. Figures 7.2
(triangles). You can see that, when the ratio between number of assets andnumber of period is greater, the upward bias of the sample eigenvalues{i.e., of thesample factor variances{ is higher. Shrinkage eliminates such bias. However, the
shrinked eigenvalues are now biased downwards and, in addition, this downwardbias is not constant, which suggests that the optimal shrinkage should not be aconstant oset. There are three take-aways from these simulations, which could
be conrmed empirically for other choices of the parameters: Sample factor eigenvalues are higher than their population counterparts;Shrinkage helps, but optimal shrinkage may be more complex than a constant
 oset;Maximum likelihood estimation, which we could solve analytically in thisspecial case, will give in general bias estimates on the factor volatilities.


(^250)
5075
100125
(^025) eigenvalue (population) 50 75 100 125
eigenvalue (sample)
(^250)
5075
100125
(^025) eigenvalue (population) 50 75 100 125
eigenvalue (sample)
Figure 7.2:volatilities 1;(a): Probabilistic PCA for a universe of 1000 assets, with 10 factors with 2 ;:::;10. Circle-shaped points are the sample factor variances against(a) (b)
the true variances; triangle-shaped are the shrinked factor variances against the truevariances. (b): All parameters are unchanged, with the exception of the number ofassets, here equal to 3000.
7.1.3. Cross-Sectional and Time-Series Regres-sions via SVD
A popular approach to PCA is to take the rstthe PCA as factors loadings, and then estimate the factor returns via cross-sectional regression. What are these factor returns? Start by settingmprincipal components ofB=Um.
The estimated factor returns are the result ofcan write the relation as follows: T cross-sectional regressions. We
R=U 214 mF^+E (7.23)


The least-squares estimate isF^= (U (^0) mUm)  (^1) U (^0) mR (7.24)
or, sinceUis orthonormal,F^=U (^0) mR=U (^0) mUSV (^0) =SmV (^0) m (7.25)
Behold, these are the same factor estimates we computed from the SVD inEquationof the SVD itself allow us to recover them from cross-sectional regressions.(7.4). If we throw away the factor returns of an SVD, the loadings
Similarly, you can easily prove (Exercise 7.9) that, if we only know the estimatedfactor returnstime-series regression of asset returns against these factor returns, and obtainF^from Equation(7.25), then we can estimate the loadings using
as a resultthe returns matrix such that the loadings are the time-series betas of the assetreturns to the factor returns, and the factor returns are the cross-sectional betasB^ =Um. Indeed, the SVD decomposition is theonlyfactorization of
of the asset returns to the loadingsalso has several applications. It is a useful relationship when we estimate factorloadings for assets with incomplete return data; it helps explain discrepancies^3. This is a computational simplication, but
in time-series and cross-sectional performance attribution in fundamental factormodels; and establishes a connection between statistical and fundamental factormodels.
Section 7.6.^3 You can prove this! Solve Exercise 7.8. You will also nd additional reading sources in


7.2. Beyond the BasicsIt is important to understand the behavior of PCA in nite samples, and insettings that are relevant to practitioners. There are a few parameters that
intuitively should matter to the portfolio manager. The rst two are trivial: thenumber of assetsSVD on a rolling window of observations of widthnand the number of factorsm. In addition, we will performT (Figure 7.3). This width
is chosen so that the data can be considered broadly homogeneous (i.e., thecross-section of returns are drawn from the same distribution), but also sothat the data has a suciently high number of observations to estimate the
parameters. Finally, another important quantity is the gap between themth

Figure 7.3:T. We estimate the risk model parameters using data in an interval of widtht-T+1 t-T+1 t-1 t
and the (smallest variance of a factor and the largest idiosyncratic variance. How do thesequantities interact? This question has been at the center of intense researchm+ 1)the eigenvalues, corresponding to the separation between the
in the past twenty-ve years. PCA, a 120-year old technique, has witnesseda theory renaissance, which is still far from being concluded. This chapterattempts to give some intuition about the analytical approach; to summarize
the state-of-the-art results; to compare them to simulated scenarios; and nallyto administer some practical advice in using PCA.


7.2.1. The Spiked Covariance ModelLetmatrixT;i, withi= 1;:::;n, be the sorted eigenvalues of the empirical covariance

The spiked covariance model posits the following: there is 0^ ~r:=T ^1 Xt=1T rtr^0 t < m < n(7.26)and a
positive constantCsuch that asi:= lim T!1
There is a spectral gap between the largestT!1T;i^8 >><>>:= 1Cn mfor allfor alleigenvalues and the remainingi > mim (7.27)
ones. How does this relate to factor models? Consider the original modelspecied by Equation= 1, a formulation (7.4)and choose, like we did in Section(7.1.2), and with

Why should the eigenvaluesBBigrow at least linearly in^0 +In n? The rst(7.28)m

eigenvalues ofSVD decomposition ofBB (^0) =US (^2) U 0 BBand^0 Bare the same as those of (^0) BB==VSUSV (^2) V (^0). The two products have the same rst (^0) and consider the two matrix productsB^0 B. To see this, write them
eigenvalues and dierent eigenvectors. Instead of analyzing the properties ofBBA reasonable assumption for (^0) , we will work onB (^0) B. Bis that its rowsbi, representing the loadings
of a single stock to the factors, are iid samples from a probability distribution 217 D,


so thatFor large values ofED(b (^0) bb). We denoteiP(Rm). We can then writenthe terms in parentheses converges to an expectationithe eigenvalues of this matrix. The eigenvalues ofB^0 B=Pni=1b^0 ibi=n(n ^1 Pni=1bB^0 ib 0 iB).
are then in the limitarelargest eigenvalues eigenvalues: for large stock universes, the pervasive (orni+ 1. This heuristic argument justies the scaling assumption for then! 1equal toni, and the eigenvalues ofBB^0 spike+In)
eigenvalues separate for the rest (orsize of the stock universe.Letibe the eigenvalues ofBB (^0). The spectrum of the covariance matrixbulk), and the gap grows linearly in the
(so thatis then given bycovariance matrix. We can see how these condition translate into practice. Recall (^) =In) and rotation (so that^1 + 1;:::;m+ 1;^1 ;:::; 1, so a factor model, after rescalingf =Im), has an associated spiked
from Section 8.3 That theConsider the risk decomposition: The factor variance iswith factor-mimicking portfolio 0 iiswi=B(B^0 B) ^1 ei.
 The idiosyncratic variance ism  (^1) kV (^0) k (^2) keik (^2)  1 =(Cni(), since the norm of an orthonormal matrixBBw^00 i)wwii==ee^0 i(^0 ieBi^0 = 1.B) ^1 ei=e^0 iVS ^2 V^0 eim ^1 kVVis^0 eik^2 
Therefore for large asset universes, i.e.,have a vanishing small percentage idiosyncratic variance. They \mimick" theone. n! 1, factor-mimicking portfolios
true factor returns whell. A dierent way to state the approximation propertyis that the idiosyncratic risk \diversies away" as the number of assets becomeslarger; and that there are \factor portfolios" with factor risk that is well above
their idiosyncratic risk.


7.2.2. Spectral Limit Behavior of the Spiked Co-variance Model
The rst asymptotic limits for PCA were concerned with large samples:andand eigenvectors converge to their population counterparts (see Appendixnconstant. In this case, Anderson [1963] showed that the sample eigenvaluesT!1??.
For modern application, the case were bothrelevant, withbecause the number of observations is often of the same order of magnitude as :=n=T 2 [0; 1 ). This limit is interesting in applications,T andngo to innity is more
the number of variables.1. The elements ofHere,rtis a sequence of iid rv taking values inrthas nite fourth moments;Rn. Assume that:

2. There aren;T!1mconstantsci, with 0< c 1 < c 2 < ::: < cm, such that as
3. The remainingn meigenvalues are equal to one.^ i!ci; i= 1;:::;m (7.29)
1. WhenThen the following holds [Shen et al., 2016, Johnstone and Paul, 2018]:i>1 +p :
     Let^ibe the sample eigenvector. Then^i!i:=i(1 +ci) a.s. (7.30)


12

34

5

(^12) eigenvalue 3 4 5
empirical eigenvalue
Figure 7.4:Because of Equation (7.29), in the limitIn
ation of sample eigenvalues, Equation (7.30), forn;p!1, this the same as = 0:2.
The empirical eigenvalues are asymptotically unbiased for large values^i!i1 +^ i; i= 1;:::;m (7.31)
 ofletalmost surely,u; see Figure 7.4.ithe population eigenvector andU^ithe sample eigenvector. Then,

2. Wheni1 +p : jhui;U^iij!^8 >><>>:Op1+(1^1 =cip^ ) ii > mm (7.32)
     ^i! 1 +p ^2 in probability; 220


Even if this strong result only applies to a single spiked model, it oers afew insights that can be veried experimentally. In addition, there are similar jhui;u^iij!0 a.s.
results that extend to the multiple spiked eigenvalue case, albeit with moreassumptions. First, let us review the insights: Under the spiked model assumptions, the spiked empirical eigenvalues are
asymptotically upwardly biased. The bias is higher ifground eigenvalues; it becomes smaller whenintuitive sense. When 1 is close to one, then the probability that the largest 1 gets bigger. This makes 1 is closer to the
 empirical eigenvalue is a \noisy" ground eigenvalue becomes non-negligible.This brings us to the second insight.There is a critical threshold at 1 +p. For eigenvalues larger than 1 +p , it
is possible to separate the largest eigenvalue from the spectrum. Indeed, thelargest sample eigenvalue is further biased upward. The sample eigenvectoris collinear with the population eigenvector. The larger the rst eigenvalue,
 the better the eigenvector's collinearity.Below the threshold, the largest eigenvalue, even if it is larger than 1, cannotbe easily be identied from data. The associated eigenvector contains no
interval (10information about the population eigenvector.In practice, for many applications, the number of asset in a model is in the^3 ; 104 ), and the number of observations ranges between 250 and
1,000, so that 1 +reason about thresholding eigenvalues, and their associated eigenvector.p ranges between 2 and 7. This is a useful starting point to


We know that the empirical eigenvalues are biased. This means that, should7.2.3. Optimal Shrinkage of Eigenvalueswe evaluate portfolios in the subspace spanned (^4) by the spike eigenvectors,
the predicted volatility of the portfolios will be biased upward bya^w (^22) =Ram (^0) a^be a unit-norm vector, and let the portfolio be=Pmi=1^ia (^2) i=Pmi=1ia (^2) i+ = (^2) w+. If the portfolio is in the (^5) w=Uma. Then. Let
subspace orthogonal to the eigenfactors, then the portfolio variance estimateis also biased. We can repeat the calculations and use the BBP theorem toobtain^ (^2) w=w (^2) + 2p +. A possible solution to the problem of eigenvalue
estimation error is to apply a function to the sample eigenvalues. For example,from Equation (7.30), one could invertifrom^iby applying the function
For large values of, this shrinkage function is an oset of the empirical`() = 
; 1 +p^ (7.33)
eigenvalues, like the one we rst saw in PPCA, Equationthis to a diagonal matrix`(S), which returns a diagonal matrix with the corresponding diagonal termsV ECSlled with eigenvalues, we use the notation(7.18). When we apply
shrinked using EquationThe choice of the loss function matters. Donoho et al. [2018] characterize theoptimalshrinkingof eigenvalues for a large number of loss types. Based on(7.33). However, this is not necessarily the best choice.
what we learned in Chapter 6, we focus only on a few: the operator normas a linear combination of (^4) The subspace spanned by vectorsvi. The column subspace of a matrixv 1 ;:::;vmis the set of vectors that can be expressedA 2 Rnmis the subspace
spanned by its column vectors, i.e., the set (^5) As in Subsection 7.1.1,Umis the submatrix off 222 Ax:xU (^2) obtained by taking the rstRmg. mcolumns.


ktwo losses, the shrinkage formula Eq.this formula simplies toA Bkand the operator norm on precision matrix`()'+ 1 (7.33). We subtract a constant oset fromis optimal. For large values of^ A ^1  B ^1. For these,
each eigenvalue. Large eigenvalues are shrunk proportionally less than the smallones. This result is connected to what is perhaps the best-known covarianceshrinkage method among practitioners: the Ledoit-Wolf shrinkage. This method
starts with nding a matrix of the form^r= 1 ~r^+rof the form 2 In (7.34)
and they identifyFrobenius norm from  1 andr: 2 so that^rminimizes the distance induced by the
mins.t.^ ^r^r=  1 ~rr^ F+ 2 In (7.35)

The space oftrace (just a special case of the well-known problem of minimum distance of a subspaceAB (^0) ). The induced normnnmatrices is a Hilbert space with scalar productphA;Aiis the Frobenius norm. This is thenhA;Bi:=
from a point in a Hilbert space (Luenberger [1969], Sec 3.3). They assume iidreturns, nite fourth moments, and an asymptotic regime in whichandT!1. They nd that the optimal solution is of the form nis constant
This solution has many interpretations, aside from the geometric one that^r=^1  T~r+TIn (7.36)
follows from the solution to Problem 223 (7.35). While these interpretations may


```
be of independent interest, I will devote some time to justify why this approachisis using the Frobenius-induced distance is generally not helping to identify thenotrecommended to estimate returns with a spiked covariance. A rst issue
structure of the model, as shown in the previous chapter. Secondly, becausethe regimeornT. Thirdly, because the condition that the estimate lie in the subspacenxed,T diverging is not relevant to applications in whichn > T
```
spanned byof of the target matrix are of the formeigenvalues, this shrinkage does not match the optimal asymptotic shrinkage of~randInmay be overly restrictive. Lastly, because the eigenvaluesi T  (^1) (i 1). For the leading
the spiked covariance model.
We now compare these theoretical results to simulations. We use the same7.2.4. Eigenvalues: Experiments Vs. Theoryparameters we used for the Probabilistic PCA in Section 7.1.2: 10 factors
with standard deviations ranging between 1 and 10, uniformly spaced; unitidiosyncratic standard deviations; 250 periods, and either 1000 or 3000 assets.In addition to the case of normal returns, I also consider the case of heavy-
tailed returns. Specically both factor returns and idiosyncratic returns aret-distributed with ve degrees of freedom. This choice is mean to simulatereturns that have four nite moments, which is a reasonable assumption for
daily asset returns.the rst ten empirical top eigenvalues, and we shrink them using FormulaWe simulate 50 instances of each factor model. For each model, we compute(7.33)
fornormally distributed returns, but not for heavy-tailed returns. In this case,`(^). The simulation shows that the shrinkage function`works well for


3060

90

(^2550) eigenvalue (theory) 75 100
eigenvalue (sample)^10050
150
(^2550) eigenvalue (theory) 75 100
eigenvalue (sample)
(a) (b)
3060
90
(^3060) eigenvalue (theory) 90
eigenvalue (sample)^10015050
200
(^3060) eigenvalue (theory) 90
eigenvalue (sample)
Figure 7.5:t-distributed returns; (c): 3000 assets, normally distributed returns; (d) 3000 assets,(a): 1000 assets, normally distributed returns; (b) 1000 assets,(c) (d)
t-distributed returns. Thedenotes the shrinked empirical eigenvalues. The dashed line is the linex-axis denotes the population eigenvalues, while they=x. y-axis
it appears that a better shrinkage approach is to scale the eigenvalues by acommon factor. This is a dierent shrinkage than the one of Equationsand(7.33), which consistent in a constant osetting term. Combining the(7.18)
empirical observations from simulated data, and theoretical results, it seems at 225


least reasonable to consider a linear shrinkage`() = 1   2 (7.37)
 21  2 (0min;1) (7.38)(7.39)
when identifying a model.
7.2.5. Choosing the Number of FactorsIn the example above, we assumed that the number of factors was known inadvance. This is not the case in applications. An important component of the
model denition procedure is the determination of the number of factors. Thereare some criteria motivated by theoretical models, and others that are theoutcome of experiments and trial-and-error by generations of practitioners. The
theory-based models themselves prescribe dierent numbers of factors, so weshould premise this section with a few considerations. First, nding thefactors matters more than nding their exact right number. By \right", I meanright
of course the factor loadings with the best \performance", and by performance,I mean one of many metrics introduced in chapter 6. Because there are manymetrics, many of which not even considered in the theoretical treatments on the
number of factors, there is no one-size-ts-all criterion. Second consideration:telling the exact number of factor in practice is either very easy or hopelesslyhard. Under the assumptions of pervasive factors, you won't need complex
criteria: there is a wide gap between the smallest factor eigenvalue and thelargest idiosyncratic one. When the assumption does not hold, eigenvalues will


decrease gradually, and a hard rule is unlikely to choose the exact threshold.A nal consideration, which is both grounded in theory and in practice isthat, one should err on the side of selecting more factors, rather then fewer.
The cost of selecting too few factors is that, in portfolio optimization, we willchoose portfolios that underestimate their true risk, which can result in steepdegradation of the Sharpe Ratio. This is covered in depth in Chapter 9. The
cost of choosing too many factors is a slight decrease in the Sharpe Ratio. Threshold-based methodsAfter these qualications, let us review the most common methods.. For matrices with ground eigenvalues equal
to 1, the results of Section 7.2.2 suggest that we should select as factoreigenvalues those that exceed the threshold 1 +p , i.e.
An older method is thescree plotm= maxf. This is the best-known method. It con-kj^k1 +p^ g (7.40)
sists of plotting the eigenvalues against their rank. The largest eigenvaluesdominate and decrease rapidly, to a value where the eigenvalue are small anddecrease gradually, usually almost linearly. The method consists of choosing
 the last eigenvalue preceding this group. A variant of this method plots thelogarithm of the eigenvalues.Maximum Change Points. Associated to these two methods, are two
additional ones that select the number of factors based on the largest gapbetween consecutive factor eigenvalues, or consecutive log(eigenvalues):
mm== 22 maxmaxkkkkmaxmax^logk ^k^ k log 1 ^k  1  (7.41)


```
WherePenalty-Based Methodsminimizing the square residual error, Equationkmaxis a threshold chosen iteratively [Onatski, 2010].. We began the chapter with the problem of(7.2). We can select the
number of factors by adding a penalty term, and by makingvariable ma decision
k;frank((n;TminR^) =)k^ nRnT+ TRlog^^2 +nnTkf+(Tn;T ) (7.42)(7.43)
```
We now explore a real-life data set with the goal of comparing the observed7.3. Real-Life Stylized Behavior of PCAbehavior of principal components and eigenvalues to the ideal spiked covariance
model. We employ daily stock total returns belonging to the Russell 3000index for the period 2007-2017. Assets that are included in this index mustsatisfy some essential requirements. As of 2022, on a designated day in May

(\rank day"), Russell evaluates eligibility for inclusion in its indices based onseveral criteria. Among them, the company must be U.S.-based (no ADR/GDRsallowed (^6) ); the stock price must exceed $1; the market capitalization must exceed
$30mm; and the percentage of 
oat (shares traded on exchange) must exceed5% of the total shares issued. In addition, some governance requirements andcorporate structure must be met; for example ETFs, trusts, closed-end funds
(GDR) is similar to an ADR, but is oered on exchanges in more than one country outside ofstock exchange, which also oers shares in U.S. exchanges. A Global Depositary Receiptthe primary market.^6 An American Depositary Receipt (ADR) is a foreign company that is listed on a foreign


investment companies and REITs are excluded. Out of this eligible set, Russellassigns to R3000 the rst 3,000 assets by market cap, and eectively changesthe composition of the index on the fourth Friday of June. These criteria
ensure that the asset characteristics are suciently homogeneous (based ongeography, revenue source and corporate governance) and that the returns canbe reliably computed based on daily closing prices (based on stock price and
market capitalization^7 ).
7.3.1. Concentration of EigenvaluesFor our exploration we consider Principal Components based on three types ofreturns. First, stock total returns. This is the simplest approach. Secondly, we
normalize returns by dividing them by their predicted idiosyncratic volatilities.The benet of this approach is that it should make the spectrum closer to theassumptions we made in the previous sections: the idiosyncratic volatilities
of the normalized empirical covariance matrix are all equal to one, and thespike volatilities should be greater than one. Lastly, we normalize returns bytheir predicted total volatilities. The rationale for this choice is that we study
the properties of the empiricalto hypothesize that the correlation matrix has dierent properties than thecovariance matrix. Correlations may be more stable than covariances; forcorrelationmatrix. It is at least reasonable
example, this is the modeling assumption made in Bollerslev [1990], and inBarra's and Axioma's U.S. statistical models. Our procedure is relatively simple. 7
the smaller-capitalization companies in R3000 and R2000 may not be suciently liquid to betraded in large sizes.Note, however, that Russell does not screen stocks based on trading volume, and that


We use one full year of return data, for eight non-overlapping years. When wenormalize by idiosyncratic volatilities, we use the data provided by Axioma'sUS model AXUS Short Horizon. I take this shortcut for one simple reason: I
introduce a self-contained idio vol estimation process later in the chapter, butdid not wait any further to show some empirical data. I will show later thatthe statistical model idio vols are indeed quite close to those of a commercial
model, so that this illustrative example is in fact quite close to a self-containedanalysis. The raw returns are winsorized at daily returns of (-90%, +100%), andthe z-scored returns at returns of (-10, +10), i.e., plus or minus ten standard
deviations. Figure 7.6 shows the variances of the rst forty factors, normalizedby the variance of the rst factor (to make them comparable). Two features areconspicuous. The rst on is that there is no obvious gap between variances. The
second is that there is a consistent ranking between the spectra of the threecovariance matrices. The plot shows the ratio of the variance of lower-orderfactors to that of the rst factor, and this value is smallest for the return/idio
vol covariance matrix, followed by the return/total vol covariance matrix, andlastly by the covariance matrix of total returns. This suggests that the rstfew eigenfactors explain a larger percentage of total variance of the associated
covariance matrix. This is conrmed by Figure 7.7. For example, say that wewould like to have a number of factors sucient to capture 50% of the varianceof asset returns. For the period ending on July 1, 2008, we need 30 factors for the
raw covariance matrix, 20 factors for the z-scored returns, using total volatility,and only 10 factors for the z-scored returns, using idiosyncratic volatility. Thisin itself doesnotmean that this choice is preferable, because the performance
of a risk model has no direct relationship with this metric. Nonetheless, itsuggests that, in this specic instance, a model built on a transformed sequence


2012−06−29 2013−07−03 2014−07−03 2015−07−06

```
2008−07−01 2009−07−01 2010−07−01 2011−06−30
0 10 20 30 400 10 20 30 40 0 10 20 30 40 0 10 20 30 40
```
```
0.010.101.00
0.010.10
```
```
1.00
n.factor
```
Variance (normalized)

Figure 7.6:eigenfactor) for the rst forty factors. Note that the scale of theVariances of the eigenfactors (normalized to the variance of the rstreturn type Return Return/Total Vol Return/Specific Volyaxis is logarithmic.
of returns is more parsimonious.

2012−06−29 2013−07−03 2014−07−03 2015−07−06

2008−07−01 2009−07−01 2010−07−01 2011−06−30

0 10 20 30 400 10 20 30 40 0 10 20 30 40 0 10 20 30 40

0.000.250.500.75

```
1.00
0.000.250.500.75
```
```
1.00
n.factor
```
Perc. Total Variance

Figure 7.7:dierence covariance matrices.Cumulative percentage of variance described by the rstreturn type Return Return/Total Vol Return/Specific Volnfactors, for


7.3.2. Controlling the Turnover of EigenvectorsSo far, we have focused on the properties of the eigenvalues. Eigenfactors exhibita distinctive behaviour as well. One important property of eigenfactors is their
turnover. The turnover for two consecutive portfoliosmeasured as the gross market value traded, as a percentage of the gross marketvalue of the portfolio:turnover 1 (v(t)) := (Pijvi(t) viv(t(t );1)v(j)t=+ 1) is usuallyPjjvj(t 1)j.

An alternative is to use the denition uses the square of the gross notional:turnover 2 (v(t)) :=Pi(vPi(tj)v  (^2) j(vti (t1) 1)) (^2) (7.44)
There are good reasons for this. The rst one is that the squared GMV isa fairly good approximation to the transaction costs associated to tradingthe factor portfolio. A second one is analytical tractability and a associated
geometric intuition. For eigenportfolios, recall thatthe numeratorquadratic turnover is therefore related to the cosine similarity which we denedkv(t) v(t 11)k (^2) can be rewritten as 2(1kv(t)k = 1, and that thatv (^0) (t)v(t 1)). The
earlier in this chapter. Low-turnover eigenportfolios have high cosine similarity.turnover 2 (v(t)) = 2[1 jSC(v(t);v(t 1))j] (7.45)
In the equation above we use the absolute value ofare identied modulo the sign of the vector. In other terms, if0, we can always 
ip the sign ofv(t) in order to have a lower-turnover pair ofSCbecause the eigenfactorsSC(v(t);v(t 1))<
eigenfactors. In Figure 7.9 we show the absolute values of the cosine distancesover time for the rst eight eigenfactors of our three sequences of covariancematrices computed on raw total returns (panel (a)), raw returns normalized
by total volatilities (panel (b)), and raw returns normalized by idio volatilities 232


(panel (c)). The covariance matrix on a given date is computed using thetrailing 252 trading days of returns. The number of assets from one day to thenext can change slightly as well, because the universe is not xed. The charts
have qualitatively similar behavior. The rst eigenfactor, is associated to aneigenvalue that has a large gap from the second largest eigenvalue (see Figure7.6). As a result, the PCA procedure has no issue in identifying it and its
\market" portfolio. The turnover has a more interesting structure for higher-orderweights are very stable throughout the estimation period. This is essentially aeigenportfolio. Consider the second eigenportfolio of the (non-normalized) total
returns. There are occasional spikes; for example there are large spikes occurringon October 9, 2009 and November 20, 2009. The second one is so big that theeigenfactors on consecutive dates have a turnover of almost 200%. What is even
more puzzling is that immediately before and immediately after the portfoliodoesn't turn over at all: it changes dramatically on a single day, to stabilizeshortly afterwards. And this behavior qualitatively repeats across covariance
matrices and eigenfactors: higher-order eigenfactors transition more often andwith larger spikes, but transitions are still relatively rare: Even eigenfactor 8has a cosine similarity below 1/2 only in 6% of the cases. Another qualitative
phenomenon is that, as for the case of eigenvalues, standardizing returns seemsto reduce turnover incidence and severity; more so for idio vol normalization. Forexample, in the latter case, eigenfactor 8 has a cosine similarity below 1/2 only
in 1.5% of the cases. How to explain this phenomenon? The cause of the jumpsis a direct consequence of the lack of eigenvalue separation. When eigenvaluesare close, the addition and removal of an observation of cross-sectional returns,
as well as the addition or removal of one or two assets in the estimation universe,is sucient to aect the numerical solution of the PCA. The distance between


the eigenvalues (i.e., variances of the eigenfactors) is within the change of thesesame eigenvalues from one period to the next due to data updates. Even if theeigenfactors change, the subspace spanned by these eigenfactors may be in fact
stable. Below, we show the subspace distance for the three cases abovethe column subspaces in consecutive periods. The distances are very small (thelargest being just 1E-5, for total return factors), and are smaller for idio vol^8 between
z-scored returns. This does conrm yet again that statistical models built onnormalized returns sequence are more stable, suggesting that the eigenvalues ofsuch models are better separated from each other.
we are faced with an inescapable issue in statistical models. Except for a fewhigh-order factors and variances, most factors in statistical models suer from aAside from the quality of the PCA for dierent choices of covariance matrices,
kind of indeterminacy. In consecutive periods, PCA may give us very dierentloadings, even though the subspaces spanned by these factors are very closeto each other. Is this a matter of concern? For most applications, it is not.

The reason is that, even if loadings can change a lot from one period to thenext, the covariance matrix does not changevolatility prediction does not depend on the orientation of the factor loadings, (^9). This means that a portfolio's
and therefore that any portfolio optimization problem is also not aected by thechoice of loadings, so long as its formulation includes constraints or objective-function penalty terms on the portfolio volatility, or combined factor volatility
of the degenerate factors (i.e., factors with identical volatilities). In integratedfundamental/statistical models, a topic we will cover in a later chapter, the 8
solve Exercise 7.13.^9 For a denition of subspace similarity, see Exercise 7.11.If you are not convinced, or this statement does not seem obvious, this is a good time to


indeterminacy of loadings is not aecting the nal result, namely the volatilitypredictions and the performance characteristics of the fundamental factors. InTable 7.1 I summarize the relevance to specic applications.
Table 7.1:UseVolatility EstimationSummary of Impact of High Factor Turnover.Impact of High Factor TurnoverNot important
Portfolio Optimization/Hedging Not importantIntegrated Stat./Fund. ModelsPerformance Attribution Not ImportantVery High
by eigenvalue quasi-degeneracy. However, single-factor attribution depends onfactor turnover. Since model prediction is unaected by rotations, we can alwaysEssentially only single-factor Performance Attribution is made irrelevant
perform a rotation that minimize distance between loadings in consecutiveperiods; this is a zero-cost operation. In other words, if we have a sequenceof loading matricesBt, we aim for new \rotated" loadingsB~tthat have low

turnover^10 : B~t+1= arg minkBt Yk (^2) F (7.46)
s:t:YXX 0 =X 2 RB=mt+1ImmX
First, we prove that the objective is equivalent to maximizing (^10) Historical note: this problem is closely related toWahba's Problem[Wahba, 1965].hA;X^0 i, with


A:=B^0 tBktB+1t. This follows from the sequence of identities Bt+1Xk (^2) F = (^) B (^0) t (Bt+1X) (^0

2) F
=trace=trace trace  (BB (^0) t B^0 tB t (^0) tB(+ traceBt+1t+1XX ) ^0 ()(traceBBt+1t X XB) 00 t(B+1B (^0) tXt+1+1)BXt)
The last equality follows from the orthonormality of2(m trace (AX)) Bt;Bt+1. Let the SVD ofA
We replace these expressions in the objective function:beandAX==USVVYU^0. We prove that a solution is given by^0 for someY. From orthonormality ofXX?follows directly=VUmax trace (^0. letAY=AX^0 YUSV)==I^0.
max trace (equal to ones and orthogonal eigenvectorsY=PiaiaSY (^0) iand the objective function is). Now for the last step: unitary matrices have all eigenvaluestrace (ai. The eigendecomposition ofSY)=Pisi[aia (^0) i]i;i, but thisYis
is maximized whenai=ei, andY=I, so that the solution isX=VU^0.


7.4. Interpreting Principal ComponentsOne criticism that is often leveled against Principal Component Analysis is thatits loadings are hard to interpret. The goal of this chapter is to partially dispel
this myth. The output of a PCA can be interpreted, and in fact sometimes itprovides additional non-trivial perspectives for the user.
7.4.1. The Clustering ViewThe rst avenue to interpretation is to do no transformation at all. The principalcomponents are uniquely determined up to a change of sign: ifuis an eigenvector
associated to eigenvalueinterpreted as amake the connection between clustering and PCA, we rst introduce theclustering membership index, so is u. We show that their loadings can be[Ding and He, 2004]. In order toK-
means approach. We partition ourby a set membershipcluster is set in advance. The cluster membership is found by minimizing theCkand centroidsnassets intomk:=PKi 2 clusters, each characterizedCkri=jCkj. The number of
sum of squared distances from the centroids:minXK
s:t:mk=1k:=iX^2 CikX 2 (Crik ri=mjCkk)j^2 (7.47)(7.48)
C[ii\CCi=j=f 1 ?;:::;N;i 6 =jg (7.49)(7.50)


The objective function can be rewritten asX
We could represent cluster membership algebraically. LetThe rst sum is a constant and does not aect the optimization problem.i ri XkK=1jCkj ^1 j;`X^2 Ck(rj)^0 r` hk 2 Rnand dene(7.51)
[needs to belong to exactly one cluster, there is a constraint on the vectors:Phkk]ip= 1jCk=jhpkjC=k 1 j, whereif asset 1 i 2 is in clusterRnis a vector of ones. DeneCk, zero otherwise. Because an assetH= (h 1 ;:::;hK) 2
Rto precisely one cluster can be expressed asKn-clustering problem, we need to solveK. Letg= (pjC 1 j;:::;pjCKj). The condition that each asset belongsHg= 1. Therefore to solve a
max traces:t:[H]i;k  2 Hn^0 R 00 ;RjC^0 Hkj  1 = 2 o (7.52)(7.53)
Notice that the columns ofnatural to relax the discrete requirements onHhave unit norm and are orthogonal. Then it isHand to solve

max traceH (^0) H =HI^0 KRR^0 H (7.54)(7.55)
This is the same formulation as the optimization version of the uncenteredPCAcluster membership. The simplest case is when we cluster on the rst principal(7.11). The interpretation of the loadings then can be one of approximate
component. We can separate the two clusters based on some clustering methodon the loadings; oftentimes, a simple inspection of the loadings distribution will


suggest an appropriate cut-o point. When inspecting multiple eigenvectors, amultivariate clustering algorithm will help identify groups.
7.4.2. The Regression ViewAnother way to interpret the loadings of a statistical model is to representthem as sums of vectors, whose weights are intuitive. Qualitatively, we proceed
We denote the matrix of characteristicsas follows. First, assemble meaningful stock characteristics for a given date.is a columngj of the matrixG. We denoteG 2 RBnthe matrix of loadings fromp, where each characteristic
the statistical model. Now, regressregression coecientsvector orthogonal to the column subspace of i 2 Rp. In formulas,Bion the columns ofBGi. If we are not using a very wide=G i+, whereG, and denote the 2 Rnis a
set of characteristics, then the regression weights help interpret the statisticalloadings. The approach is, of course, not restricted to statistical models: wecould apply this regression approach to any pair of risk models, to interpret
one based on information contained in the other.returns normalized by idio vols, for the date of July 6, 2017. In order to gainAs a (very simplied) example, we consider a model built on US asset
intuition aboout the eigenfactors, we regress them against style loadings only;we use Axioma AXUS4 as source of these loadings. In Tables 7.2 and 7.3, wereport only the most signicant loadings.
factor, i.e., the factor of identical loadings all equal to ones. This is usually thecase in statistical models. Regarding the second factor, the most importantThe rst principal component is overwhelmingly explained by the market
explanatory variables are a value factor (Dividend Yield), Size, and (with 239


Table 7.2:termMarket InterceptVolatility Regression coecients for the rst principal component.estimate std.error t-statistic-2.6E-031.7E-02 1.6E-041.9E-04 -1.4E+011.1E+02 0.0E+008.1E-43p value
Table 7.3:Short-Term MomentumEarnings YieldRegression coecients for the second principal component.1.2E-037.7E-04 1.6E-041.9E-04 7.6E+004.1E+00 2.8E-143.4E-05
termDividend YieldShort-Term MomentumSize estimate std.error t-statistic-3.4E-034.2E-033.3E-03 3.3E-043.3E-043.3E-04 -1.0E+01 1.1E-241.3E+01 8.7E-361.0E+01 1.2E-23p value
negative coecient) Short-Term Momentum. The opposite signs for valueand momentum are consistent with experience, since the returns of thesefactors are usually negatively correlated. Size and Dividend Yield loadings are
usuallyhigher dividends{or dividends at all{than small caps. For this specic date, thecorrelation is 0.32. The rst factor can be interpreted as a \risk-on" factor,positivelycorrelated, the reason being that large caps are likely to pay
whereas the second factor can be interpreted as a defensive, or \risk-o" factor.
7.5. Statistical Model Estimation in Prac-tice
So far we have only presented the theory of statistical factor models. Thenext two sections discuss the issues related to its implementation. PrincipalComponent Analysis is usually applied to matrices (orpanels) that do not


have a time dimension. In contrast, we deal with temporal data; and we cannotassume that these data are drawn in each period from the same probabilitydistribution. We will employ the PCA and SVDlocally, i.e., on intervals in
which the data can be presumed to be approximately stationary. We present twoapproaches that are used by practitioners. Without any aspiration to establisha winner, we compare their performance on historical US equity data.
7.5.1. Weighted and Two-Stage PCAA recurring theme in factor estimation is that weighting observations dierentlyhelps. Observations in the distant past are less informative than recent ones;
observed returns of stocks with high idiosyncratic risk should be downweighted,compared to those of low-idio stocks. There are therefore two basic transfor-mations that we can apply to the raw return matrix. The rst one is in the
time dimension. We replace the empirical covariance matrix in Equation (7.9)with a weighted one. Letnal elements. The diagonal terms could be, for example, exponential weightsW 2 RTTa diagonal matrix with positive diago-
[sum toW]t;t=T. Then the time-weighted empirical uncentered covariance matrix isexp( t=); the positive constantis such that the diagonal terms
This is the same as rst transforming the returns^=T^1 RW^2 R^0 R~=RW, and then computing(7.56)
the empirical covariance matrix, Eq.practice, we would not compute the covariance matrix and then perform thePCA, but rather perform the SVD onR~(7.9), which would be computationally less, on the transformed returns. In
expensive and give us the same results. 241


fundamental factor models chapter we saw that it is optimal to scale returnsby the idiosyncratic volatility, or at least a proxy. Similarly to Boivin andA dierent type of transformation is cross-sectional reweighting. In the

Ng [2006], I propose a two-step procedure. First, perform an SVD (possibly,time-weighted) on the returns;p= 5) and compute the idiosyncratic returnsR=USV (^0). Take the rstE=R UpSppVcomponents (say, (^0) p; a case we also
consider iscovariance matrix isi (^2) =Pi[Ep] (^2) i;i= 0, in which case, andW :=diagR. Dene the proxy idiosyncratic volatilities:   11 ;:::; n 1 . The asset-level reweighted
One can perform then a second-stage PCA and a factor model on the reweighted^=WRR^0 W (7.57)
covariance matrix:idiosyncratic weighting matricesWe employ the steps above in the following process. We use two time-series^UmS^2 mU^0 mW+.I. Finally, pre- and post-multiply by the
reweightings: one with half-lifeAn empirical insight in asset return data is that volatilities and correlationschange over dierent timescales. Volatilities change rapidly; in fact the mayf (f is for \fast") ands(sis for \slow").
change dramatically over the course of a few days. The ratio between thevolatility of a stock during a crisis can four times as large as the volatility of thesame asset during a quiet period. On the other side, pairwise correlations are
quite stable. Even in the presence of major market stresses, these correlationsmarginally increase in absolute value. This suggests that we separate volatilitiesand correlations. Therefore, in the rst stage, we use a short half-life to capture
adequately changes in volatility. In the second stage, we use a longer-half lifeto estimate the factor structure of correlations. 242


Procedure 7.1:1. Inputs:RStatistical Model Estimation 2 RnT,sf>0,p 2 N,m >0.

2. Time-Series ReweightingWRf~:==RWdiag (exp(f : T=f);:::;exp(  1 =f))

3.4. First stage PCAIdio Proxy EstimationE=R~ :U~R~p~S:=pV~:U~ (^0) pS~V~^0 (truncated SVD)

5. Idio ReweightingW^2 i:= diag=Xt [E :]^2 i;t ^11 ;:::; n^1  (idio vol proxies)
6. Second Stage PCAWR^s:=:=Wdiag (exp(:RWR^ :=sU^ S^T=V^ s);:::;exp( ^1 =s))

7. Second-Stage Factor Modelwhere:fNN(0  (^0) ;;diagIn:)^r =`(sU^ (^21) )m;:::;`f+^(s (^2) m)

8. Output: Final Factor Model=n ^1 mi=X:mnr+1:=s^2 iBf+

where:Bf=WNN(0   (^01) ;;U^diagWm^   2 `)(s (^21) );:::;`(s (^2) m)
This procedure is 
exible enough to include several PCA-related procedures 243


as special cases, and to serve as a basis for further experimentation. Someexamples: Whenp= 0, then idio reweighting becomes a z-scoring, so that the second-
 stage PCA is eectively applied to the correlation matrix.The special case of equal-weighted observations in time is obtained in thelimit!1.
 It is straightforward to use dierent shrinkage methods in the second-stagefactor model step.In the second-stage factor model step, we use the Probabilistic PCA results
of Section 7.1.2. The idio reweighting steps approximately \whitens\ theidiosyncratic returns, i.e., it makes them unit-variance, so that PPCA ap-plies. However, we could replace this a dierent estimation procedure, like
Maximum Likelihood.
7.5.2. Implementing Statistical Models in Pro-duction
dynamicIt is not sucient to have a procedure that estimates the loadings and thecovariance matrix at a point in time. In our applications, factor models are. At timet, we have an estimation universe of stocks, and we use return
data up todata between loadingsTBmaxt periods in the past. We apply the two-stage PCA using returnsTmax+ 1 andt, to obtain:
t. This is the output loadings matrix.


 factor returns and idio returns estimate at time^ft=(B (^0) t  1 W;t (^2)   1 Bt  1 )  (^1) B (^0) t  1 Wt: (^2) ;t  1 rt (7.58)
^t=[=rU^t m]B^0 tWt^ftrt (7.59)(7.60)
We need to address some outstanding problems:1. Sign indeterminacy of eigenvectors;2. Time-changing estimation universe;

3. Imputation of loadings for non-estimation universe assets;4. Imputation of missing values for new or temporarily non-traded assets.5. Adjustment for corporate events.
We tackle them in this order.Sign indeterminacy of eigenvectors. Let us begin with a simple observation.
In a statistical model, eigenvectors are identied modulo a sign change, i.e., ifis an eigenvector of matrixwe compute the SVD for adjacent periods, we add and remove observations,and associated eigenvalue, then so is u. Whenu

which may lead to a sign 
ip in the loadings. It is important therefore that load-ings be collinear, in the sense that the cosine anglein adjacent periods be positive. Aside from the straightforward realignment ex- (^11) as between eigenvectors
ercise, the turnover of eigenvectors is important in two respects. First, because,if we observe that 11 SC(ui(t);ui(t+ 1))'0, then it is dicult to determine
(u^0 vThe cosine angle (or cosine similarity) between two vectors)=(kukkvk). u;vis dened asSC(u;v) :=


the sign of consecutive eigenvalues. As a result, it is dicult to determinethe sign of the factor returnsiderations, high-turnover statistical factors cannot employed for performancefi(t) over time. Aside from any statistical con-
attribution. The second consideration is that a very high-turnover factor resultsin factor-mimicking portfolios with very high turnover as well, and is thereforea factor that is very dicult to trade, either for hedging or speculation purposes.
Time-changing estimation universetistical models are estimated on a predetermined set of assets. The rationale forthe choice of such universe is the same as for fundamental models. Estimation. Similarly to fundamental models, sta-
universe assets may be representative of the investment universe of the tradingstrategy; may be suciently liquid to be considered tradeable; and, relatedly,may be suciently traded to ensure good price discovery and therefore reliable
return calculations. Assets enter and leave the universe over time. We havea dilemma. We cannot use the latest universe composition, because the pastreturns of recent additions to the index may be unreliable because the asset
was illiquid, or be missing altogether. We can still opt to keep these recentadditions, provided that their returns are well dened; or alternatively we canuse the assets at the intersection of all the universes over the time interval used
for estimation. If the time interval used for model estimation is not too long,and if the universe turnover is not too high, we will still have a sucientlybroad panel of assets. It is preferable to employ an estimation universe that has
the lowest possible turnover, and it is important to use a consistent procedureto select the assets to include inR.
Imputing loadings for non-estimation universe assets 246. There are assets


that are not in the estimation universe, but that have complete returns. Theydo not have loadings. We can impute loadings by performing a time-seriesregression of asset returns against the factor returns. This approach is justied
by the results in Subsection 7.1.3: we can recover loadings from time seriesregression, provided that the factor returns we obtained using the estimationuniverse are close to the true factor returns. Below is a simple numerical example.
We use one year of returns, and a universe corresponding approximately to theRussell 3000. We rst perform a two-stage PCA on the entire universe, andestimateBandF. To test that estimated asset loadings can we recovered, we
perform the same analysis, but this time on a universe of 2000 assets chosen atrandom. We now take the estimated factor returns, and estimated the loadingsusing a time-series regression for the assets we held out. Finally, we compare
the loadings from the rst PCA, the \population" loadings, to those from timeseries regression, the \imputed" loadings.[*** TABLE AND CHARTS HERE***]
Imputation of missing values for new or temporarily non-traded as-setsexamples are newly-listed assets (IPOs, ADRs), or assets that were either. Some assets do not have sucient return history to regress their loadings;
delisted for a long period of time, or had trading volumes considered too low toresult in reliable returns. A possible solution is to use additional characteristicsof the asset to impute its loadings. The approach is similar to the one we
presented in Section 7.4.2 on the interpretation of loadings using regression. Inthis case, however, we usually are not aorded the luxury to know many ofthe asset's style characteristics like momentum, beta, liquidity, or protability.
All we have is knowledge of the industry and country of the asset. We regress 247


observed loadings against these two characteristics, and predict the missingloadings. It is common practice to shrink predicted loadings toward zero. Wewill cover a rationale for this practice in later sections devoted to hedging.

7.6. Further ReadingStandard references for PCA are Jollie [2010], Jollie and Cadima [2016],Johnson and Wichern [2007], Pourahmadi [2013], Yao et al. [2015]; PCA is also
covered in any popular graduate-level textbook on Statistical Learning, e.g.Hastie et al. [2008], Murphy [2012], Bishop [2006]. Skillicorn [2007] is devotedto the interpretation of SVD, PCA, Non-negative Matrix Factorization and its
applications.[2001]. In a seminal paper, Chamberlain and Rothschild [1983] impose similarIn the statistical literature, the analysis of this model begins with Johnstone
conditions, but in an asymptotic setting, by considering an increasing sequenceof asset universes (withgoes to zero. n!1) and risk models in which the diversiable risk
in Section 7.2.2, to give a taste of what happens and give a basis for heuristics.Several papers have characterized the behavior the model. The rst and seminalWe have only touched brie
y on the asymptotic limit of the spiked model
result is by Baik, Ben Arous and Peche [Baik et al., 2005], and the theorem isnamed BBP theorem after their initials. Several authors have generalized theseresults: Baik and Silverstein [2006], Paul [2017], Bai and Yao [2008], Mestre
[2008], El Karoui [2008], Benaych-Georges and Nadakuditi [2011], Shen et al.[2016], Wang and Fan [2017]; a survey is Johnstone and Paul [2018]. Generalsurveys on Random Matrix Theory, with a eye toward nance are Bun et al.


[2017] and Bouchaud and Potters [2020]. The line of research concerned withproperties of the spectrum in the regime \Johnstone [2001]. From the very rst result on biased asymptotic estimators, ap=n1" begins (^12) perhaps with
reader may wonder about shrinkage methods. There is an extensive literatureon factor model shrinkage. Standard references are Ledoit and Wolf [2003b,a,2004] on linear shrinkage, and more recent work on nonlinear shrinkage by the
same authors [Ledoit and Wolf, 2012, 2015, 2020]. The paper by Donoho et al.[2018] covers optimal shrinkage functions for a large set of loss functions.For a relatively old survey on methods to select the number of factors, see
Ferre [1995]; a more recent survey is in Fan et al. [2020]. The scree plot methodis due to Cattel [1966], and its logarithmic version by Farmer [1971]. The screeis the debris that form at the base of a cli.
static factor models and dynamic factor models. For the former, see the surveyby Bai and Ng [2008]; for the latter, Stock and Watson [2016].In the econometric literature, there are at least two strands of research:
Boivin and Ng [2006] reweights using idio volatilities, and Bollerslev [1990]using total volatilities.The two-step procedure for reweighting the PCA is relatively common;
by Ding and He [2004].The connection between PCA and clustering was made in the seminal paper
7.7. ExercisesN.B.: the solution sketches will be grouped at the end of the book.
observations with^12 The academic literature denotes the number of variables withn. 249 pand the number of


Exercise 7.1of ranktwo matricesmminB(Low-rank factorization) 2 fn;TRngmif and only if it can be decomposed in the product ofandC 2 RmT. : Prove that a matrixA 2 RnTis
(7.7)Exercise 7.2kw?kand= 1.(7.10)(PCA solution)is unique and that constraint: Prove that the solutionkwk^2 1 is always binding, i.e.,w? in Problems
Exercise 7.3tionas nding iteratively(7.11)gives the same solution as nding the rst(Alternative PCA formulation)kunit-norm vectorsw 1 ;:::;:wkProve that the optimiza-m, witheigenvectors ofwkorthogonal to^, and
the rstExercise 7.4k 1 vectors(Covariance Matrix of a Linear Transformation)wk, that maximizew^0 kw^ k. : Prove

that if the random vectorif 2 Rmn, then the random vectorsrtaking values inx=Arhas covariance matrixRnhas covariance matrixAA, and (^0).
Exercise 7.5matrix. Prove that the rst(A Simple Spiked Matrix)meigenvalues of:BBLet (^0) +B (^22) InRare greater thannm be anm-rank (^2).
Exercise 7.6:Exercise 7.7(The Power Method)Solve the optimization problem, Eq. (7.16).: A simple (the simplest?) algorithm for

1. start with a unit-normcomputing the largest eigenvalue of a symmetric p.d. matrixa standard normal distribution, then normalize it); 2. iterate:x 0 chosen at random (say, sample the coordinates fromxi+1is the following:=xi=kxik;

3. after the vector converges (sayxi+11.approximates the top eigenvector, andProve the convergence and correctness of the power method. (Hint:kxi+1 x 1 kx (^0) iis smaller than some tolerance),xithe top eigenvalue. xi=


2. Let3. How would you extend it to nd all the eigenvalues ofix^0 i=^ 
(log(1ix^0 .)=)=). Prove thatx^0 ixi(1 ) 1. ?
Exercise 7.8plest?) algorithm for computing the largest singular value of a matrixis the following: 1. start with(Iterated Projections for the SVD)x 02 RT chosen at random (say, sample the coor-: A simple (the sim-R 2 RnT
dinates from a standard normal distribution), 2. iterate:yi+1=Rxi (7.61)

3. after the vectors convergexi+1xi+1approximates the highest left eigenvector,=R^0 yi+1 (7.62)
yi+11.the higher right eigenvector, andProve the convergence and correctness of the algorithm (hint: powermethod); y^0 i+1Rxi+1the top singular value.
    2. How would you extend it to nd the SVD ofof the power method). R? (Hint: not the same may

Exercise 7.9and setith factor return. Prove that the least-squares regression coecient of the timeF^:=S(Time Series Regression from the SVD)mV (^0) m. The vector^fi, theith row ofF^, is the time series of the: LetR=USV^0 ,
seriesExercise 7.10ri= (^) i;j^fj(Oja's Iterative Algorithm)+, is (^) i;j= [U]i;j. : Letrt;t= 1;:::;Tbe a time
series of returns drawn from a common distribution onmatrixof :. Prove that the following algorithm converges to the rst eigenvectorRnwith covariance


1. Set2. Choose column3. Update the directioni= 0 and choose a unit-norm(i) uniformly at random between 1 andv 12 Bnuniformly at random.T.
    vvii+1+1 =vknvvii++1+1ik ^1 (1 v^0 ie)(r^0 (i)vi)r(i) (7.63)(7.64)

Solution (sketch)X4. Settakes one ofi^ i+ 1. IfT: Letvalues:Rkv 2 i+1rRinr  (^0) iTwith equal probability 1v, andikthen stop. Otherwise go to Step 2.Xa random matrix taking values in=T. One can interpretRnn.
the productT  (^1) RR (^0) is T ^1 v^0 RR^0 vas the expectationE(v^0 Xv). The rst eigenvalue of
We can apply the stochastic gradient algorithm to the maximum search. Letkmaxvk=1Evk^0 vXvk^2  (7.65)
fkv(Xk;isv) := (v^0 Xv)=kvk^2  kvk^2. The derivativervffor a unit-norm vector
Exercise 7.11(Distance Between Subspaces)2(1 v^0 e)Xv : LetA;B 2 Rnm, be or-(7.66)
thonormal matrices. If the two column subspaces are \similar", then anyunit-norm vector in the column subspace ofunit-norm vector in the column subspace ofBA. Dene similarity between theis well-approximated by some


two subspaces S(A;B) := (^12) kmaxxk 1 kminyk 1 kAx Byk (^2) (7.67)
1.2. Prove thatvalue ofProve thatA (^0) BSS.((AA;;BB) is 1) is not a distance because it does not satisfy the  1 (A^0 B), where 1 (A^0 B) is the rst singular
Exercise 7.12triangle inequality.(Angle Between Subspaces): LetA;B 2 Rnm, be or-
thonormal matrices. Let the least cosine distance between subspaces be thecosine of the smallest achievable angle between two vectors, one belonging tothe column subspace ofA, the other belonging to the column subspace ofB.
ofAProve that^0 B. SC(A;B) =n(A^0 B), wherem(A^0 B) is the last singular value
values)Exercise 7.13Bhas the form: Consider a risk model with the following structure: its loading matrix(Covariance Matrix Invariance for Degenerate Eigen-B=DU, whereD 2 Rnnis diagonal positive denite, and
Uidentity: (^2) 1.RProve that if we replacenm,fU=^0 UI=m.Im; and its factor covariance matrix is proportional to theUwith an \equivalent"U~ 2 Rmnspanning the

2. same subspace, the covariance matrix does not change.Extend the result to the case wherepvariances being greater than the rest:fis still diagonal, but with the rst 1 >  2 > ::: > p> p+1=


:::=m, and with U~;1:p=U;1:p
U~^0 ;(p+1):mU~;(p+1):m=Im p


factor 5 factor 6 factor 7 factor 8

factor 1 factor 2 factor 3 factor 4

2008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−07

0.000.250.500.75

```
1.00
0.000.250.500.75
```
```
1.00
date
```
```
abs(cos distance)
(a)
factor 5 factor 6 factor 7 factor 8
```
factor 1 factor 2 factor 3 factor 4

2008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−07

0.000.250.500.75

```
1.00
0.000.250.500.75
```
```
1.00
date
```
```
abs(cos distance)
(b)
factor 5 factor 6 factor 7 factor 8
```
factor 1 factor 2 factor 3 factor 4

2008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−07

0.000.250.500.75

```
1.00
0.000.250.500.75
```
```
1.00
date
```
abs(cos distance)

(b) total returns/total vol; (c) total returns/idio vol.Figure 7.8:Eigenfactor turnover for dierent covariance matrices. (a): total returns;^255 (c)


```
Return Return/Total Vol Return/Idio Vol
0e+003e−06 2008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−072008−07 2009−01 2009−07 2010−01 2010−07
6e−069e−06
date
```
similarity
Figure 7.9:consecutive periods. The eigenfactors are generated by PCAs on total returns, totalreturns/total vol, and total return/idio vol.Distance between column subspaces of the rst eight eigenfactors in

```
Return Return/Total Vol Return/Idio Vol
0.00.5 2010 2012 2014 2016 2010 2012 2014 2016 2010 2012 2014 2016
1.0
```
Figure 7.10:cumulative return Factor returns for the rst four eigenvactors. The eigenfactors arefactor factor 1 factor 2date factor 3 factor 4
generated by PCAs on total returns, total returns/total vol, and total return/idio vol.


0.000.25

0.500.75

1.00

(^5) n.clusters 10 15 20
between_SS / total_SS −0.050.00
0.05
0.00 0.02 loadings factor 1 0.04 0.06
loadings factor 2
Figure 7.11:rst two principal components.(a) Performance of clustering; b) Five clusters of the loadings of the(a) (b)


# During The TradePart II


# Chapter 8Portfolio Management: The

# Basics

## 1. What are the basic single-period portfolio optimization formula-The Questions

## 2. What can go wrong?3. tions? How do we interpret the results?How do we incorporate prior information in portfolio optimization?

## common theme throughout the chapter is that we limit ourselves to a single-period optimization setting. This a chapter for hedgehogs, not foxes: we set aThis chapter is devoted to the very basics of portfolio construction. The

## narrow playing eld, but dig a deep hole. The chapter requires some knowledgeof basic results optimization Please consult the Appendix, Section 8.7.1, orre-open any optimization textbook you enjoyed reading as an undergraduate or

## MS student. I give references on this subject, and other standard topics likeutility theory, in the \Further Reading" Section at the end of the chapter.


8.1. Why Mean-Variance Optimization?Investors have objectives, information, and constraints. Besides this genericstatement, there is not much in common among them. A large fraction of
investment professionals cannot { and would not { articulate a clear objectivefunction; their constraints are sometimesforced. Neither George Soros nor Warren Buett, nor others among the mostad hoc, vague, or inconsistently en-
successful investors in history, have ever known what the volatility of theirportfolios was at any point in time. At the other extreme, academics havedeveloped several normative theories for portfolio construction. In this book I

am trying to use relevance to applications as a guiding principle. In the vastmajority of applications, the optimization formulations are single-period. Thisis explainable by a combination of the following (^1) :
 Interpretabilityto formulate and, once solved, their solutions are also harder to interpret.Computational tractability. Multi-period optimization problems are vastly more complex. Single-period optimization problems are solvable
 by commercial solvers in a matter of seconds.Short-term investment horizonpartly because they heavily discount the future, partly because they do not. Investors think only about the short term,
 know how to quantify information uncertainty and rate of change.Lack of standard theoretical resultsterizing the formulations and the improvement in performance.. Few strong results are available charac-
[2005], Huang and Litzenberger [1988]. Both cover the standard cases of exponential andquadratic utilities. A number of textbooks exist covering portfolio construction. A classic isGrinold and Kahn [1999]; see also Chincarini and Kim [2022], Qian et al. [2007], Isichenko^1 On justications of the mean-variance approach to portfolio optimization, see Cochrane
[2021]. On the statistics of the Sharpe Ratio, see Lo [2002] and, for a comprehensive anddenitive reference, Pav [2023] and references therein. 260


```
The objective functionreturnsvalues under dierent realizations of the future. The expected value of ther. Economic theory interpretsV is a function of the portfolio weightsV as a utility function, taking dierentwand of the
utility function gives the investor thetaking by investing in a portfolio. We assume that the investor has initial wealthW 0 , that she knows the distribution of the random vectorex antevalue of the bet she would ber, and that she solves
```
the problem maxEV(W 0 +w (^0) r) (8.1)
The choice ofmonotonically increasing (more wealth is better than less) and concave (cor-responding to risk aversion). One approach, followed by Markowitz [1959],V is not obvious. Common properties ofV are that it is be
is to consider a polynomial local approximation of the objective function:Vwe obtain(W 0 +w (^0) r)'V(W 0 ) +V (^0) (W 0 )w (^0) r+V (^00) (W 0 )(w (^0) r) (^2) =2. Taking expectations,
EV(W 0 +w^0 r)''VVV(( 00 WW( 2 W 0 ) + 0 ) Vw^00 ( Wr (^0) w)w+ (^0 w+ (^0) ) 2 
V^00 ( 2 W^0 ) + 0 )wV 0
0 (rWw^0 )w^0 +
We maximize a quadratic objective function which is the weighted sum ofexpected return and variance; hence the namemean-variance portfolio opti-


mization[De Finetti, 1940, Markowitz, 1952]:E[V(W 0 +V 0 w(W (^0) r 0 )]) V(W 0 )'w (^0)   2 w (^0) rw
 >0 is called thecoecient of absolute risk aversion:= VV^000 ((WW^00 (CARA). The higher)) ,
the more risk-averse the investor is.The CARA for this function is constantAs examples, consider an objective function of the form=a: it is independent of the wealthV(x) = exp( ax).
Wis 0 of the investor, and so are her allocation decisions. The optimization problem
Alternatively, consider the objective functionmaxw w^0  a^2 w^0 Vrw(x) =log(x). This function is
associated to thewarrant a dedicated section to it in this chapter. Here, let us consider itsimplications for approximate portfolio optimization. The CARA isKelly criterionfor investing. It has unique properties which= 1=W 0 ,
so that we solve maxw w (^0)   2 W (^10) w (^0) rw
The wealthier the investor is, the more risk-seeking she becomes.optimization problem for the investor. This result is standard. Less knownWe have shown that a quadratic utility function implies a mean-variance
is the converse: if an investor selects an investment on the basis of meanand variance only, her utility function is necessarily quadratic [Baron, 1977,


Johnstone and Lindley, 2011]. Viewed in the context of axiomatic decision theory,portfolio mean-variance optimization is not satisfactory, because a quadraticutility implies that investors are satiated, and have even a dislike of wealth
beyond a certain threshold. As a local approximation, however, mean-varianceoptimization is appropriate. Moments of returns (and portfolios) beyond thesecond one are beyond the realm of what's possible, as seen in Chapter 2.
A portfolio manager settled a long discussion on the topic with the laconicstatement that \the rst two moments should be enough for everybody".

8.2. Mean-Variance Optimal PortfoliosA factor model gives us an asset-asset covariance matrixthis information, it is straightforward to compute the variance of a portfolio, (^) r 2 Rnn. Given
as we saw in Section 3.5.2 on risk decomposition. The other essential inputto the optimization problem is a vectorsame interval at which we have a volatility forecast. The simplest optimization 2 Rnof expected returns, over the
problem is to maximize expected PnL, subject to a constraint on the maximumtolerable volatility, denoted by >0. The problem can be stated as
maxs:t: (^) w^00 w (^) rw 2 (8.2)
This is not only the simplest optimization problem. One of the most importantmetrics used for the evaluation of strategies is thehave at least a supercial acquaintance with it; and it will be covered extensivelySharpe Ratio. Most readers
in Chapter 5. For now, it suces to say that the Sharpe Ratio of a portfolio 263


is the ratio of its expected return to its predicted volatility at a certain timehorizon, and therefore serves as a risk-adjusted measure of performance. If wehave covariance matrix and expected returns, we can formulate the Sharpe
Ratio optimization thus: maxw pw 00
 wrw
This optimization, however, is indenite because the objective functionindependent of the portfolio size, i.e., homogeneous of degree 0:for allt >0. We can address this issue by bounding the denominator. ThisSR(tw) =SRSR(w() isw)
means xing the portfolio size. The upper bound constraint on the denominatoris always binding:
maxsw:t:ppww^000 wrrww

equivalent to maxequivalent to maxsw:t:w^  00 w (^) rw 2
sw:t:^ w^00 w (^) rw^2


Which is optimization problem(FONC) for this problem are: (8.2). The First-Order Necessary Conditions

rw( 0 w ww^0
0 rwrw) ==0 (^)  2 + 2 (^) rw
(w^0 rw ^2 ) =0^0
The solution to these equations isw?=q 0    1
?=q^02 r r^1  r^1 (8.3)(8.4)
The expected return and the Sharpe Ratio of the portfolio areE(r (^0) w?) =q 0
  r (^1)
A way to interpret (and derive quickly) the solution is to recall that the optimalSR?=q^0  r^1 (8.5)
portfolio is proportional tothat the variance constraint is met. The optimal portfolio is proportional to thevolatility budget: the higher the budget, the bigger the portfolio. However, the  r^1 , and then to nd the proportionality factor so
portfolio is independent of the magnitude of the alpha vector (it is homogeneousof degree zero in alpha): replacing with gives the same solution. This


is interesting. The parameterInsight 8.1:Miscalibration of alpha size is not catastrophic?also merits special consideration. It is the
relativeIf you have a volatility constraint, a good volatility model, and youralphas does not matter.alphas are accurate then the error in theabsolutesize of the
shadow pricethe variance budget by one unit, the expected return increases byterms, the shadow price of the variance constraint is the derivative of the(or Lagrange multiplier) of the volatility constraint. If we increase?. In other
objective function with respect to the variance. While this relationship is notvery useful in this specic case, it will come in handy for other constraints.In its simplicity, the solution contains the essential data of the problem: the
inverse of the covariance matrix (also called theof expected return. In the next few pages I would like to interpret, eviscerate,extend this simple formula; and nally, as you start believing it is useful, toprecision matrix) and the vector
caution you against its use. Like all the good things in life, mean-varianceoptimization is at its most pleasant when it is accompanied by precautionarymeasures. First of all, we can derive the same solution when we solve an

unconstrained problem: max 0 w w (^0) rw (8.6)
We have added the constraint to the objective function in the form of a penaltys:t:w^2 Rn (8.7)
term; the informal term for this operation is 266 pricing outthe constraint. The


objective function is convex, and the solution is given byw?= 21   r (^1)
which gives the same solution as the vol-constrained problem when=q (^02)  r (^1)
The larger the volatility budget, the smaller the penalty coecient.formulation. This is not a coincidence. We obtain the same solution when weNotice that this penalty value is the same as the shadow price in the previous
price out the constraint and we give the a unit price equal to the shadow priceof that constraint.A third equivalent formulation is the one where we minimize volatility,
subject to a return constraint: minw (^0) rw (8.8)
The solution is s:t:^0 w (8.9)
There is yet another formulation that is equivalent to the previous ones. Often-w?=^0  r^1  r^1
times, we think of portfolio positions not in terms on net market value, butof volatility. We do not invest $10M in AAPL. The annualized volatility ofAAPL is 20%, and therefore we have a $2M volatility position in the stock.


This conveys the position size in terms of its range of dollar movement overthe course of a year. Now, we can express the Sharpe-Optimal portfolio interms of volatility in the following way. Let the stock volatilities be 1 ;:::;n,
and deneDenote the asset correlation matrix withbe written Vra diagonal matrix with these volatilities on the main diagonal.=VCV. Now let's rewrite the solution to the MVO problem:C. Then, the covariance matrix can

Vww??==^2211 (CVCV ^1 (V)  ^11 )
SRv??==p^21 sC^0 C  ^11 ss (8.10)(8.11)
In the formula above,vector of asset-level Sharpe Ratios. Therefore, the optimal dollar volatilities areproportional to the Sharpe Ratios, multiplied by the inverse of the correlationv?:=Vw?is the vector of dollar volatilities, andsis the
matrix. This is interesting, because dollar vols, correlations, and asset SharpeRatios are more intuitive quantities than covariances and returns. A directimplication of this result is that, when assets are uncorrelated, the optimal
dollar vol allocation is proportional to the asset Sharpe Ratios.


Insight 8.2:Is there a way to interpret further the relationshipoptimal position of asset?Reading the entries of the precision matrixiis a weighted sum of alphas. The 
w?/  r r (^11) ]? Thei;jare
proportional to minus theafter controlling for the other asset returns. The interpretation of partialcorrelation is that it captures collinearity between two random variables,after removing the collinearity of these variables with a set of controllingpartial correlationsof the returns ofiandj
variables. In practice, one follows this procedure: 1. regress the returns ofThe formula for the optimal portfolio isassetbetween the residuals from the two regressions, which we denoteiandjon the returns of the other assets; 2. compute the correlationi;j.
The diagonal terms of the precision matrix are always positive. Theinterpretation of this rather convoluted formula is that, whenever thewi/[
 r^1 ]i;i^0 @^ i Xj^6 =ii;j[
 r^1 ]j;j^ j^1 A
returns of two assets are positively correlated after removing the jointeect of correlations with other variables, the size of the portfolio isreduced, because the collinearity makes the alpha common to both assetiandj.


8.3. Trading in Factor Space8.3.1. Factor-Mimicking Portfolios
We have a factor model, and we estimate the expected factor returnsthat we want to generate a portfolio which has the closest possible return toone of the factors. For example, we want to generate a \momentum factor". Say
(FMP) should be as close as possible to those of the portfolio: the variance ofportfolio. What would it be? The returns of thethe dierence of the two returns should be minimized. A portfoliofactor-mimicking portfoliowhas an

associated factor exposurevarianceminimized when (^2) betweenbi fi1 = 0,andrbb (^0) wj. Its returns are= 0 forisE[((jbi 6 = i, and the portfolio's idio variance is1)fri^0 +wP=jb 6 =^0 ifbj+fjw+^0 w. The tracking (^0) ) (^2) ]. This is
minimized. The optimization formulation isminw (^0) w
(^2) We ignore the term (^) ?, both out of simplicity and because it is very small.s:t:B^0 w=ei


```
The solution isare the factor-mimicking portfolios is (vi=  ^1 B(B^0  ^1 B) P^1 eiis for \portfolios"). The matrix whose column vectors
P:=^266664 vj jj j 1 v 2 ::::::::: vjjm^377775 (8.12)
==   ^11 BB((BB^00   ^11 BB))  ^11266664 ej jj j 1 e 2 ::::::::: ejjm^377775
```
We now have factor portfolios as tradable instruments. The expected return ofa factor portfolio is (1. generate the FPMs compositions over time; (^0) ?+ (^0) B (^0) )vi=i. In practice, we:

2. compute their per-period PnL;3. compute their empirical average PnL;4. apply a haircut to the average PnL;
returns and FPM composition. In the Appendix (Theorem 8.8), we prove that if5. optimize in factor space.We now prove that FMPs emerge naturally from certain assumptions about
alpha spanned is zero and if the idiosyncratic variance of the factor-mimickingportfolios is small, then the mean-variance optimization problem reduces to onein which we only trade FMPs. First, we solve the low-dimensional optimization


problem max (^0) u  21
 u (^0) fu
Say that the solution isv?. The optimal portfolio is the weighted sum of thes:t:u^2 Rm
FMPs In factor space, the dimensionality of the problem collapses, but we stillhave an MVO problem, which is usually more interpretable. The possiblew?=Pv?. A few remarks on the appeal and limitations result:
 drawbacks of mean-variance optimization still hold, but so do the possibleremedies, which we present in Chapter 9.Factor-mimicking portfolio make their appearance as the necessary syn-
thetic instruments for trading in factor space. In synthesis, if you performmean-variance optimization and factors are suciently \pure" (having lowidiosyncratic risk), then younecessarilytrade FMPs. It is an economical,
 beautiful result.Keep in mind that FMPs are associated to the loadings matrixthat there are many loadings matrices resulting in equivalent factor modelsB, and
(see Section 3.4.1). Think of FMPs as a vector basis in a nite-dimensionalsubspace. There are innitely many such bases, and they don't need to beorthogonal. The subspace, however, is uniquely identied.
 The assumption of small factor idiosyncratic variance can be expressed as (^) book{in an ideal world, we would like it to be small, in the real world, it is(B 0
   (^1) B)  (^1) 1. The matrix inside the norm appears repeatedly in this
not. The ideal-world solution works well as a sketch of the real world. It tellsus the broad shape of the portfolio. When trading, we should include the


```
 idiosyncratic variance of the portfolio and not solve for the limit case.In conjunction with the previous point, we have also ignored execution costs.They should not be ignored in applications. Chapter 10 is devoted to the
subject.
8.3.2. Adding, Estimating, and Trading a NewFactor
```
Let us consider a simple example, and let us work through the individual steps.In a way, all the steps are implicitly contained in the theory developed so far. Thestarting point is a factor model withmfactors, with parametersB; (^) f; (^) . We
assume that they are constant through time for notational simplicity; extendingthe example to time-varying parameters is straighforward. The factors haveexpected returns. We are exploring a new asset characteristic vectora 2 Rn.
We can add the new factor to the existing model without reestimating the entiremodel by pushing out the model. We add a factor to the model, but do not needto reestimate model because we can take advantage of Frisch-Vaugh-Lovell's
theorem1. Orthogonalizationfactors. The orthogonalized factoris given by standard linear regression^3.. First we orthogonalize the new factor to the existing
formulas^4 by bm+1= (In B(B 0
   (^1) B)  (^1) B 0
   (^1) )a
(^34) See Section 3.7.3.See Section 3.7.1.


2. Estimationexisting model against the orthogonalized factor by using Frisch-Vaugh-Lovel theorem:. Next, we regress in every period the residual returns from the

)f^m+1;tt:==bbm (^0) mb+1+1^0 m+1f ^m^  +1 1  b;t^1 m+t+1^t (8.13)(8.14)
^^mm+1+1:=:=T^1 TX 1 tXft^mf+1^m 2 ;t+1;t! (8.15)(8.16)
In the Appendix (Theorem 8.9), we show that the approximate varianceSR =c ^^mm+1+1 (8.17)

3. of the new factor is ^Risk updatingcovariance matrix including the new factor is given by. We show in Section 8.7.6 that the approximate factorm^2 +1= (b^0 m+1^  ^1 bm+1) ^1.

```
This result holds only for constant parameters and well-diversied factor^ ~f'^264
0 f (b^0 m+1^  ^01 bm+1) ^1375
portfolios. For time-varying models, we need to resort to numerical esti-mates for the factor covariance matrix. The analytical results provide auseful approximation.
```
4. Trading. The Factor-Mimicking Portfolio of the new factor isvm+1=b (^0) m (^) +1  
1 b m (^1) b+1m+1


This follows from the denition of FPMs, Equationis via the factor return estimation above. The factor return estimate isthe same whether we regress using residual returns or total returns(8.12). A faster route (^5) :
f^m+1;t==bb (^0) m (^0) mbb+1+1^0 m (^0) m+1+1   (^)   11   bb^11 mm^rtt+1+1
Let~= (j^m+1). Finally, we solve the optimization problem=v^0 m+1rt
maxs:t:u~^0 u 2  Rm (^21) +1 u^0 ~fu
whose solution is simple, because of the block structure of the factorcovariance matrix
So, our investment in the preexisting factors is unchanged, but we addu?=^264 (b^0 m+1^  ^1  fb^1 m+1)^m+1^375
a position in the new factor, proportional to the expected factor returndivided by its variance.
(^5) See Sections 3.7.2 and 3.7.3. 275


Procedure 8.1:1. Inputs: a factor model (Adding a New Factor to a Model and Trading Itbt; (^) f;t; (^) ;t;t), with expected factor
2. Orthogonalize the factor:returns; raw loadings for the new factorbm+1;t= (In bt(b (^0) t   (^1) bt)  1 abt (^0) t.   (^1) )at
3. Compute the Factor-Mimicking Portfolio:vm+1;t:=b (^0) m+1  ;t;t (^1) b m;t 1 +1bm;t+1;t

4. Compute new factor covariance matrix^m+1:=T^1 Xt vm^0 +1;trt
5. Compute new weights for FMPs:^ ~f'^0 f;t (b^0 m+1;t^  ^0 ;t^1 bm+1;t) ^1 
    and trade portfoliou?t=^ "(b^0 m+1^  ;t^1 b f;tm^1 +1;t)^m+1;t #

wt=^24 vj j (^1) j j;t v 2 ;t ::::::::: vmjj+1;t^35 u?t


8.3.3. Factor Portfolios from SortsA very popular way to form factor portfolios is to sort securities by a givencharacteristic, and then form a portfolio in which the long positions are top
xxthe portfolio is dollar-neutral. For example, we consider book value-to-price-quantile positions (say, the top 25% positions) and the shorts are the bottom-quantile positions. The Net Market Value of each position is identical, so that
(BtP) as the characteristic for a US investment universe of 2000 stocks, and golong $1000 the 500 stocks with the highest value of the ratio, and short $1000the 500 stocks with the lowest value of the ratio. This approach originates with
the paper by Fama and MacBeth [1973], who introduced them to alleviatethe problem of estimation error of time-series betas of single securities, byestimating portfolio betas instead. The resulting portfolios are sometimes called
portfolios from sortsThey are widely used by practitioners to convert a metric that describes apotential mispricing into an investable portfolio. What are the drawbacks oforcharacteristic portfolios(CPs ; Daniel et al. [2020]).
this approach? There are at least four.1. The characteristic portfolios will have unwanted exposures to other factors.As a result, you may be betting on the characteristic of interest as well
as on some other source of systematic risk and return. The unwantedexposures may both increase the overall portfolio risk and reduce thereturn of the portfolio.
2.3. The securities in the characteristic portfolio are equal weighted. This isinecient, since more volatile securities should have a lower weight.Being equal-weighted, the sizes in the characteristic portfolio do not re
ect
the magnitude of the characteristic. For example, if asset A has twice theBtP of asset B, and they both are in top 277 x-quantile of the distribution,


(see, e.g., Harrell [2015]).they receive the same weight. This is the same as dichotomizing thecharacteristic. Dichotomization of data is usually a poor modeling strategy

4. Over time, characteristics change, and certain securities may be droppedfrom/added to the portfolio abruptly (from a target weight to zero). Thismakes trading more expensive and require some adjustment over the
    nave weights.
Portfolios from sortsFAQ 8.1:portfolios which consist of equal-weighted long positions for securitiesWhat About Factor Portfolios from Sorts?(orcharacteristic portfolios) are dollar-neutral
having the highest values of a certain characteristic, and equal-weightedshort positions for an equal number of securities with the lowest valueof a characteristic. They hold the intuitive appeal of being a simpleimplementation of a dollar-neutral portfolio. However they have many
weighting, unwanted exposures to other factors, and high turnover duedrawbacks: non-optimal volatility weighting, non-optimal characteristicto abrupt inclusions/exclusions in the portfolio. FMPs are designed tobe the most ecient (i.e., lowest risk) portfolios with unit exposure to a
characteristic of interest.


8.4. Trading in Idio SpaceIn Section 3.3 we introduced the concepts of alpha spanned and alpha orthogonal.Alpha spanned are asset expected excess returns attributable to non-zero factor
expected returns; alpha orthogonal are non explainable by factor returns.Because of Equationthis, alpha orthogonal is the golden currency in investing. How does one build a(3.3), Sharpe Ratio scales at least likepn. Because of
portfolio that exploits only this alpha? By requiring that the optimal portfoliohave no exposures, and therefore no returns, to factors. There are many waysto achieve this, and they are encountered in practice. The rst one is to build a
portfolio that has an upper bound on volatility, maximizes expected returns,and has no factor exposures. By construction, the portfolio contains \purealpha" and no factor-related PnL. The formulation is:

maxs:t: (^) Bw^0? (^00) w w= 0w 2 (8.18)
whose solution^6 is ^?:=(In B(B 0
   (^1) B)  (^1) B 0
   (^1) ) (^)?
In Section 8.3.2, we built an FMP for a new factor through two steps: rst,w?=q^ ^^0?^  ^1 ^?^  ^1 ^?
orthogonalization; second, inverse variance weighting. The portfolio construction (^6) Derive it as an exercise, or see Section 8.7.4.


for an alpha orthogonal portfolio is indeed, identical: orthogonalization andinverse variance weighting. If all the asset idiosyncratic volatilities are identical, (^) is proportional to the identity, and the orthogonalization step is super
uous:
^?= (^) ?.
8.5. Drivers of Information Ratio: Infor-mation Coecient and Diversica-
What makes a good strategy? Before we are trading (i.e.,the dream, i.e. Equation (8.5):tion ex ante), we are living
A substantial part of this and of the next chapter is dedicated to the notionSR?=q^0  r^1
that we do not exist in the Dreamtime. Our forecasted returns and risk modelsare incorrect, and we should take this knowledge in the investment process. Arst step is to establish someex postrelationship for the Sharpe Ratio. Start
with the solution to the MVO problem, Equation (8.3):w?=q 0    1
r^  r^1


And assume that the covariance matrixassumption. The expectedrealizedreturn is (^) ris accurate; admittedly a strong
E(r^0 w?) ==qq 0   rE (^1) (rE 0
 (r r^0
1  r)^1 )
Dene theInformation Coecient^0  r^1 :qE(r^0  r^1 r)sE(r^0 n r^1 r)pn
The important thing to know is that the Information Coecient is a correlation.IC :=q^0 E r(^1 r^0 q rE^1 (r)^0  r^1 r)
To see why, we need to transform variables:~r=  r 1 = (^2) r (8.19)
So that the Information Coecient can be rewritten in a more succinct form^ ^=^  r^1 =^2
which can be interpreted as a cross-sectional uncentered correlation.IC(^ ^;~r) :=p^ ^^0 E^ ^(p~r^0 E^)(~r^0 ~r)
vector 7 We can simplify things further by proving thatrhas the same covariance matrix^7 as (^1) rE=^2 (r^0 , where^  r^1 r) =nis a standard. The random
Prove this step-by-step in Exercise 3.2.


multivariate normal. E(r 0
  r (^1) r) =E( (^0
1) r= (^2)  r (^1
1) r= (^2) )
==nXi=1n E(i^2 )
Putting everything together, theSR =IC(E(r^0 ^w;?~r);= (^) ris)pn
who named itby practitioners. In practice, users of the formula do not whiten returns andThis relationship goes back to Grinold [1989] and Grinold and Kahn [1999],The Fundamental Law of Active Management^8. It is often invoked
alphas in Equationof a portfolio, so thatIC becomes the cross-sectional correlation between the standardized alphas(8.19) (^) r. Instead, they apply the law to the active componentis replaced by the diagonal (^) and by (^) ?. Then,
(expected excess returns in units of volatility) and the standardized idio returns(so that they have unit variance).The Fundamental Law has several important implications. The rst, and
most obvious one, is that performance is driven by two factors. The rst one isa measure of skill: the Information Coecient. It is a strength of the predictivestrength of the signal. If we have the ability to extend our forecast to a larger
panel of stocks without degrading its predictive power, we should do so! This istitle at the time. I can imagine Grinold playing air guitar and singing to an Iron Maiden tune (^8) Quite an important name for a \law"! And why not? Nobody had thought of using this
as he was drafting the original 1989 paper. 282


Insight 8.3:Being a correlation, the IC is also naturally related to the predictivestrength of our alphas, as measured by a cross-sectional regression. AsInformation Coecient and Predictive Regression
weighted-least squares regression of residual returns against alpha. Wean important step in exploring alphas, we perform a cross-sectionalestimate a coecientxthat solves the following minimization problem:

The solution is given byisk~rk (^2)  (~r (^0) ^) (^2) =minkb ^kX 2 i, while the total sum of squares isb?(r=i ~r^0 ^2 ^;ii=b)k^2 ^= mink^2 and the residual sum of squaresb k~r ^ ^bk^2 k~rk (^2). The
Coecient of Determination (\R squared") is, in expectation, equal to:R (^2) =k ^(~rk (^02) ^k)~r (^2) k 2 = (IC) 2
And we can link the coecient of determination in predictive regressionsto the Information Ratio: IR =pR (^2) n
If there arehas a convenient form as a function of per-period cross-sectional Rsquared Tinvestment periods in a year, the annualized InformationIR =pR (^2) nT= ICpnT
in a yearOtherwise stated, the annualized Information Ratio is equal to theInformation Coecient times theaFor the relationship between Coecient of Determinnation and Information Ratio,a. independent number of return forecasts
see Chincarini and Kim [2007, 2022].


never the case in real life. Many investors also have a notion of \idea velocity",expressed as the number of forecastsin principle, the Information Ratio. It is really dicult, however, to increaseTper year. A higher idea velocity increases,

(the IC) that is interpretable as a correlation, which can be related to a specialeectively the frequency ofThe Fundamental Law also connects Information Ratio to anindependentforecasts. ex postmeasure
kind of regression (as per Insight 8.3).
8.6. Investment Performance MetricsA discretionary portfolio manager satisces, a quantitative portfolio manageroptimizes. Maybe this is not entirely fair to discretionary portfolio managers:
they optimize too, the way tiger sharks optimize for food intake or migratingwarblers minimize traveling distance to Cuba. On the other side, this describesaccurately what a quant does. A quantitative manager has an objective, con-
straints, and information. Investment objectives are not the only ones enteringthe manager's process. For example, the estimation process of a factor modelrequires a loss function to minimize. This chapter introduces and justies the
investment metrics that will appear in later chapters. In some cases, the metricsenter the optimization problem as objectives; in others, as constraints. The roleplayed by objectives and constraints is, to some extent, interchangeable.
 The expected return of the strategy;The volatility of the strategy;The performance metrics of a portfolio manager are, by and large, three:
 The Sharpe Ratio;The Information Ratio; 284


 Capacity.
(PnL) to Assets Under Management. With the possible exception of Mother8.6.1. Expected ReturnTheexpected returnof the strategy is dened as the ratio of prot and loss
Teresa, investors prefer more money to less, and returns are an adequate way todescribe this. Returns are preferred to actual money because the normalizationmakes the measurestationary, i.e., having (approximately) the same distribution
across dierent investment periods, andindependent of the amount invested. This allows for better comparison acrossperiods and across funds. Returns can be optimized either over the course ofintensive(as opposed to extensive), i.e.,
an investment period or over the lifetime of the strategy. In practice, the twoproblems are separable: we solve a sequence of single-period problems, whichwe embed in a larger multi-period problem.

We introduced the8.6.2. Volatilityis also dened as the standard deviation of the its returns. The use of volatilityvolatilityof returns in Chapter 2. The volatility of a strategy
in investing is ubiquitous. From a descriptive point of view, one may stop here.From a normative point of view, volatility may be justied by making additionalassumptions. Say that the investor solves a one-period utility optimization prob-
lem of the formof the investor and is increasing and concave. Then, one can justify the use ofvolatility using three assumptions. The rst, is by assuming that the utilitymaxwE[u(w^0 R)]; the utility function describes the preference
function is well approximated by a second-order Taylor expansion centered 285


at the expected payo, so thatsecond justication comes from assuming a quadratic utilityarbitrarily distributed returns; then the portfolio has also normally distributedu'aE(w^0 R) bE[(w^0 R 9  uE=(wax^0 R ))bx^2 ]. The (^2) and
payo, and taking expectations we can express utility as a function of meanand variance. Lastly, one can assume arbitrary utility and normally distributedreturns. Since mean and variance identify a normal distribution, we can express
the expected utility as a function of these two parameters, albeit not necessarilyadditive. All the approaches above require that the second moment of returnsbe nite. As we discussed in Chapter 2, there is agreement that returns of
many securities have nite variance, and that over longer time scales log returnsresemble Gaussian returns. The assumption that the can approximate utilitywith a quadratic function is not unrealistic, since the optimization horizon in
quantitative investing is short and the payos are small. Globally, utility isnot quadratic, and this can be described by the parameters used in the utilityapproximation formula. A higher value of the ratiob=acan be interpreted as
penalizing more the uncertainty of payos relatively to their expected values,i.e., in being more risk-averse. I am not discussing this further, since the topicis covered extensively in textbooks (see Section??for references), and is not
essential to the remainder of this book.
8.6.3. Sharpe RatioTheits volatility. It combines the previous two quantities by measuring returns inSharpe Ratiois dened as the ratio of expected returns of a strategy to
(^9) This is not an increasing utility, and this assumption is unrealistic anyway.


units of volatility over a certain period of time. If we assume that the returnsof a strategy identically distributed and independent, the Sharpe Ratio is thesame as the t-statistic of the mean of the return distribution. In nance, the^10
Sharpe Ratio is named after William F. Sharpe, one of the authors for theCapital Asset Pricing Model (CAPM). The Sharpe Ratio has drawbacks andadvantages. Its drawbacks are two. First, it is not quite justiable as a metric
that ranks uncertain outcomes. Aside from decision-theoretic considerationsthe Sharpe Ratio of a portfolio with negative expected return of -5% andvolatility 5% ishigherthan the Sharpe Ratio with the same negative return,^11
and volatility 10%. This is unintuitive at best and wrong at worst. Secondly,it inherits the limitation of volatility as a measure of risk. It is possible toreplace the denominator with one's favorite risk measure, of which there is a
near-innite supplyis intuitive: return in units of \risk". Second, it comes with a rich arsenal oftheoretical results. We have condence intervals and characterizations of its^12. There are advantages, however. First, the Sharpe Ratio
empirical properties, theoretical results, like relationship between cross-sectionalregressions and Sharpe Ratio. The Sharpe Ratio also implies a bound on theprobability of incurring a certain loss. This follows from Cantelli's inequality.

For a random variablerisk-free rate, often the three-month Treasury yield. This is the return of holding a self-nanced (^10) Or, more commonly, thewith meanexcess returns, i.e., the returns of a strategy in excess of theand standard deviation, this inequality
security: we borrow one dollar in the rst period at the risk-free rate, and buy one dollar ofthe security. In the second period, we receive the security return, and pay o the loan. Seealso Section (^1112) For these, see Huang and Litzenberger [1988].??, where excess returns enter naturally.
heuristic.See, for example, Bacon [2005] for a list of risk metrics, both theoretically justied and


states thatP( <  ) 2 + (^2)  2 orP( < ) (^2) + ( (^2) +) 2 (8.20)
Ifof the strategy, and the loss is expressed as a multiple of standard deviations Lis the annual return of a strategy, and SR is the annualized Sharpe Ratio, as practitioners often do, then the inequality is
This holds foranydistribution of returns with Sharpe Ratio SR. For example,P( < L)1 + (L^1 + SR)^2 (8.21)
consider an annualized Sharpe Ratio of 3 and an annualized volatility of $50M.The probability of a $100M loss is no greater than two standard deviations isnot greater than 3.8%. This a much higher value than we would obtain under
the assumption of normal returns. In that case, the probability of a loss wouldbe 2.9E-7.
Whereas the return and Sharpe Ratio are well known and dened, the8.6.4. Capacityof a strategy is not unequivocally dened. An informal denition of capacitycapacity
is \the highest expected PnL that a strategy is able to produce over a certainhorizon". You may ask, \but isn't expected PnL just equal to Sharpe Ratiotimes dollar volatility? Capacity is essentially the maximum volatility at which
we can run a strategy". This would be true is Sharpe Ratio were independentof volatility, and in that case, why not run a strategy to innity volatility, orat least to the proverbial 11? Sharpe, however, is almost always a decreasing


```
which they are measured. Daily returnFAQ 8.2:Return, volatility and Sharpe Ratio depend on the time horizon overWhat are the dimensions of the Sharpe Ratio?ris daily PnL on capital; an-
(10%/nualized return, where we assume the same daily PnL overdays in a year, isexample: a strategy has a return of 10%/(1 year) = 10%/(T)/days. Provided that returns are serially uncorrelated (seerT. We say that returns have dimension [time]TT tradingdays)= ^1. An
```
Subsection 2.1.5), variance is also linear in time, because the vari-ance of returns over a year is the sum ofdimension ishas the dimension of[time]  (^1) [time]. Volatility is the square root of variance and  1 = (^2). The Sharpe Ratio has the dimensionT daily variances, so its
[return]/[volatility]=the horizon of a Sharpe Ratio for an equity strategy from a daily horizonto a monthly one, we multiply the daily Sharpe Ratio byis the number of trading days in a month. The conversion factor to an[time] ^1 =[time] ^1 =^2 =[time] ^1 =^2. When convertingp 21 , where 21
annualized Sharpe Ratio in the US isp252.
function of volatility. For a large enough volatility, the Sharpe Ratio becomeszero, and beyond this threshold the strategy is unprotable. The capacity of astrategy can be dened as the maximum PnL that can be attained, subject to
a constraint that the Sharpe Ratio exceed an acceptable level. Alternatively,we could require a minimum bound on the expected return on capital. Denedthis way, the capacity is an important parameter for hedge fund managers and
portfolio managers alike. A strategy may have attractive return and SharpeRatio when run at low volatility. If it can yield only a model PnL, it will beeconomically unattractive.


FAQ 8.3:Suppose you observeSharpe Ratio from these data. What is the condence interval of thisWhat is the condence interval for the Sharpe Ratio?T consecutive returns (or PnL), and estimate the
estimator? First, the Sharpe Ratio estimator is^:=T 1 Xt=1T rt ^:=vuutT 1 Xt=1T (rt ^) 2
For excess returnsis normally distributed in the limitrtthat are iid and with nite variance, the estimatorSR :=c T^^!1, with standard error
Compare this to the case in which we knew in advance the standarddeviation of the returns. The Sharpe Ratio is thenSE(SR) =c s1 + SRT^2 =^2 SRc:==^ , and the
values ofSE isIn the case of autocorrelated returns withRatio estimator and the asymptotic condence interval are, for smallp^1 =Tjj,. cor(rs;rt) =jt sj, the Sharpe
SR :=c ^^r^1 1 + '^^r^1 1 + '^^(1 )


8.7.8.7.1. Convex Optimization?Appendix
This appendix collects some basic facts about optimization of convex functionsthat are used in the book. Extensive treatments of convex optimization are inBoyd and Vandenberghe [2004], Luenberger and Ye [2008] and Bazaraa et al.
[2006]. Convexity plays a central role in our treatment. Fig. 8.1 illustrates theconcept.

Figure 8.1:A convex set (left) and a non-convex set (right).
Denition 8.1:t 2 [0;1],tx+ (1 At)yconvex set2D. Dis a set such that for anyx;y2 D and
Denition 8.2:Dbe a convex set infisconvexRnandis its graph is convex, i.e., for any pairf:D !R. x;y 2 S,
fstrict.(tx+ (1 t)y)tf(x) + (1 t)f(y). It is strictly convex if the inequality is
convex, closed and bounded.We assume below thatfis convex and dierentiable, and that the setSis


convex set.Theorem 8.1: The intersection of an arbitrary number of convex sets is a
set.Theorem 8.2: Letfbe a convex function. The setfxjf(x)^0 gis a convex
Denition 8.3:1. AIt is strict if the inequality is strict.global minimumx?2Dis a point such thatf(x?)f(x) for allx2D.

2. Afcentered at(xlocal minimum?)f(xx) for all?. It is strict if the inequality is strict.x?x 22 SSis a point such that there is\B(x?), whereB(x?) is a ball of radius >0 such that
Theorem 8.3:1. A global minimum for2. Ifx?is a local minimum, then it is a global minimum.f exists.
3.In this book, we are interested in characterizing the solutions of the problemiffis strictly convex, then it is the only global minimum and it is strict.

mins:t:gfbi( (^0) j(xxx))=acji i= 1j= 1;:::;m;:::p (8.22)
whereconvex, e.g., 13 f:Rnf!(xR) =is dierentiable and convex, e.g., 0 x+x (^0) 
x.giare dierentiable convex functionsf(x) =  0 xor strictly (^13).
You may observe that the formulation is redundant. We can do away with the linear 292


Their sublevel setsbproblem (also calledi 2 Rn,ai 2 R, is also convex,. The set of feasible points for the optimizationfxfeasible regionjgi(x) ci (^0) ) is the intersection of convex sets and isgare convex. The setfxjb^0 ix=aigwhere
therefore convex. The maximization of a concave function is equivalent to themaximization of a convex function. Therefore the conditions of Th. 8.3 apply.Denote the optimal value of the objective functionp?.
8.7.2. DualityDenition 8.4:RmRp!R. TheLagrangianof the problem 8.22 is a functionL:Rn
The variablesL(x;,;) :=are thef(x) +Lagrange multipliersXim=1i(gi(x) ci) +of Problem (8.22).Xj=1p j(b^0 jx aj)
can see the optimal solutionandThe Lagrangian can be interpreted as a penalized objective function. Ifare sucient large and, in the case ofx?LofL approach the optimal solution, has the correct sign, youx? of
Problem (8.22), because these large values \discourage" constraint infraction.The theorems below identify the limits of the intuition: minimizingan intermediate step toward solving the problem is a seemingly dierent way.Lis indeed
equalities and replace them with two inequality constraintsconstraints are frequently found in practice, and the formulation we present simplies theinterpretation of solutions in the presence of linear constraints.b^0 jxaj, b^0 jx aj. Linear


Denition 8.5: Thedual functiong(;) = infxis dened as2DL(x;;)
Theorem 8.4(Weak Duality):g(For each;)p? 0 , 2 Rp
closed set, the sup is attained on the feasible set. Denote (point.We can take the sup ofg; since it is bounded above and?;;?take value in a) the optimum
q?:= maxs:t:g(; 0 )
qproblem is convex, the equality does not always hold. An additional conditionis needed, called?p?. When does the inequality become an equality? Even when the originalconstraint qualication. More than a single condition, it is
a family of requirements for the constraints that, when satised, ensure thatweak duality becomes strong. Roughly speaking, these conditions ensure thatconstraints are not redundant. A common constraint qualication isSlater's
Conditioninequality constraints are strictly satised:: there existsxin the feasible region of Prob. (8.22) for which all thegi(x)<0 for alli= 1;:::;m.
Theorem 8.5(Strong Duality): If Slater's condition holds, thenq?=p?.


From strong duality, it follows thatf(x?) =q?=p?=f(x?) +Xi=1n i(gi(x?) ci) +Xj=1p j(b (^0) jx? ai)
))Xim=1i(gi(ix(g?i)( x?c)i) = 0 ci) = 0i= 1;:::;m
where the last term comes from the fact that each term is non-positive. Thiscondition is termedWe collect the necessary conditions for optimality of the point (complementary slackness conditions. x?;?;?):
rxf(x) +Xim=1irxgi(x) +Xj=1pgi(jxbj)=0ci i= 1;:::;m (8.23)(8.24)
i(gi(x) bc^0 jixi) =0=a^0 j iij= 1= 1= 1;:::;m;:::;m;:::;p (8.25)(8.26)(8.27)
The rst equation is the rst-order necessary condition for the maximum ofthe Lagrangian. The second and the third equations are the primal feasibilityconditions. The fourth equation is the dual feasibility condition. The last one is
the complementary slackness condition. Considered together, Eqs. (8.23-8.27)are referred to as thecentral result in optimization theory is that these conditions are also sucient.Karush-Kuhn-Tucker conditions, or KKT conditions. A
then it is an optimal point for pb. (8.22).Theorem 8.6(KKT conditions): If a pointx?satises the KKT condition,


treatment I recommend Boyd and Vandenberghe Boyd and Vandenberghe[2004]. There are several interpretations and uses for the values (There are many interpretations of the dual, and for an extensive, clear?;?). We
Equivalent Penalized Problemmention two.. Say we solve the unconstrained problem
where?;?solve the KKT conditions. Then the solution satises 8.23. Henceminx L(x;?;?)
the optimum is reached atan unconstrained penalized optimization problem is equivalent to a constrainedone. x?.?;?are the penalization constants such that
8.7.3. Local AnalysisIt is possible to fully characterize the sensitivity of the solution of Problem 8.22to changes in the input parameters without having to solve the problem anew.
Envelope Theoremof generality, we omit the linear equality constraints:. Consider a variant of Pb. (8.22) in which, without loss
V() := mins:t:gfxi(( 2 xx;;Rn)) 0 i= 1;:::;m (8.28)(8.29)
Both 2 Rfp. Fixand the functions?and letx?;gi?are dierentiable functions of a parameter vectorthe optimum point and Lagrangian multipliers. 296


Theorem 8.7:dV(dx?i;) (^) =?= @f(@x?i;) (^) =?+Xim=1?i @gi(@x?i;) (^) =?: (8.30)
dierentiable.Proof. By the Implicit Function Theorem, the functionx?();?() are
@V@i==@@f@fi+Xkn=1@x@fk@x@ki+Xjm=1?j@g@ji+Xjm=1Xkn=1@@xk?j@x@kigj
@=i@@f+iXjm=1+Xjm=1?j@g@?jji@g@+jiXk @x@ki@x@k^0 @f+Xj ?jgj^1 A
the last equality holds because of Eq. (8.23).the Lagrange multipliers can be interpreted as a measure of the impact that aconstraint exerts on the solution. A large multiplier corresponds to high penaltyShadow Prices. The magnitude of
associated to the constraint. If we removed the constraint, the solution wouldlikely be improved. A constraint that is not binding has no impact on the nalsolution; by complementary slackness, the associated Lagrange multiplier must
be zero. There is a well-established quantitative relationship between Lagrangemultipliers and marginal impact of the constraint. In Problembe the solution, which we parametrize as function ofa;c; and correspondingly,(8.22), letV(a;c)
let(a;c);(a;c) be the Lagrange multipliers. It is a direct corollary of the


Envelope Function Theorem that@V@ai=j i= 1;:::;p (8.31)
We can interpret the RHS parameters as upper bounds on quantities. For@V@cj =j j= 1;:::;m (8.32)
example, a linear constraint may be an upper bound on total exposure of aportfolio to a certain factor. The Lagrange multiplier is then theexposure: if we relaxed the exposure by one unit, we would experience anpriceof that
improvement in the overall performance equal to the Lagrange multiplier. Forthis reason, Lagrange multipliers are also termedshadow prices.
Local Change of optimal pointchanges in the optimal pointanalysis only to the unconstrained case andx. A related question is that of expressing the?() as the parameter 2 R, as it is the one needed inchanges. We limit our
this book; the multivariate and constrained one follows along the same lines.The rst-order conditions are
DeneH 2 Rnnandg 2 @fRn(x@xas?(i);)= 0 for all (8.33)
(H)giji:=:=@xdxd@j?i^2 @xfk(x?();) (8.34)(8.35)
b:=@@rxf(x?();) (8.36)


Then 0 =dd@f(x@x?(i);)= 0 (8.37)
)g(?) = H ^1 (?)b(?=)Xk Hjkgk+b= 0 (8.38)(8.39)
Parametrized Optimization Problemsto optimize a functionparametermay model an input to the model, but may also be used tof(x;), which depends on a parameter. Consider now the case in which we want 2 R. The
describe a family of functions. Letthe case in which we solve the problem forestimate of an input parameter; or to a functional form which we are able tox?() :=arg min 0. This may correspond to our bestff(x;) :x 2 Rng. Consider
solve exactly. Letfunction atof the objective function when the parameter isx?( 0 )when the value of the parameter is( 0 ;) be the dierence between the value of the objective 1 : , and the optimal value
This can be interpreted as an \optimization" error when the parameter choice is() :=f(x?(^0 );) f(x?();) (8.40)
not correct. From the denition offor the upper bound of. x?,0. We would like to have an estimate

dd==@f@ hr(x?x(f( (^0) x);?()) hr;);dxdxf?(x(?)(i););ddx?()i @f@(x?( 0 );) (8.41)(8.42)


Sinceby hrxf(x?( 0 ); 0 ) = 0,d=dat 0 is zero. The second derivative is given

dd^2  2 ==g hr (^0) Hgxf(x?(););dxd?(x?( 0 );)i (8.43)(8.44)
 h hr@@xrf(xxf?((x?)(;));;dd) 2 ;xdx 2 d?(?()i)i (8.45)(8.46)
at= 0 the gradient in the third term is zero, and we usedd (^2)  2 =b (^0) H  (^1) b hb; H  (^1) b)i= 2b (^0) H  (^1) b (8.47)
As an application of the formula above, we estimate the optimization errorwhen we approximate convex dierentiablehsuch that, for some point x 0 ,g(x 0 ) =gghfunction with a quadratic function(x 0 ),rxg(x 0 ) = rxh(x 0 ) and
We optimize the quadratic function, corresponding toHpoint beg(x^0 ) =xH?. The vectorh(x^0 ). The parametrized function isbis f(x;) = 0 = 0. Let the optimalg(x) + (1 )h(x).
which we can approximate, sinceb=rx(rg(xx(g?)(x ?)h (xh?))(x?))' rx(g(x 0 ) h(x(8.48) 0 )) +
Hthat, to a rst approximation,g h(x 0 )(x? x 0 ) =Hg h(x (^0) d)( 2 x=d?  2 x= 0. The error is cubic in 0 ) = 0 sinceHg h(x 0 ) = 0. It follows.


8.7.4. Solutions to Specic Optimization Prob-lems
equalitiesMaximize expected return subject to a vol constraint and linear homogeneous.

maxs.t. (^) Bw^000 ww
w= 0 2 (8.49)
The solutionw?to this problem is given by:=In B(B 0
   (^1) B)  (^1) B 0
   1
w^ ~?:==p^ ~ 0
   (^1) ~  ^1 ~
 Minimum-variance portfolio subject to linear equalitiesminw (^0) 
w. (8.50)
The solution isw?=  ^1 B(B^0 s.t.  B^1 B^0 w) =^1 bb. Of special interest is the case(8.51)
whereww (^0)? (^) =w. The rst term is constant, so the objective is  1 =B(B
B 0
 f B (^10) B+)  (^1) b. In this case the objective is equal to=Pb, wherePis the matrix whose columns arew (^0) w, and theb^0 fb+
the Factor-Mimicking Portfolios associated to the factor model. These areintroduced in Section 8.3. 301


We have a standard MVO problem, but the available data are the SharpeMaximize expected returns using Sharpe Ratio and Asset Correlation MatrixRatios of the assets and their correlations. The solution can be expressed as.

an intuitive function of these data. The MVO portfolio is proportional tothe portfoliocontaining asset volatilities, and  r (^1). We write (^) rC=VCVis the correlation matrix. The SharpewhereVis the diagonal matrix
Ratio of assetiissi:= (^) i=i.w?=(VCV)  (^1)
)Vw?===VVC   ^111 CCs  ^11 (sV ^1 )
The Sharpe Ratio of the MVO-optimal portfolio isoptimal dollar volatility is a function of correlation and sharpe only. Foruncorrelated assets, the optimal dollar volatility is proportional to the Sharpeps^0 C ^1 s. Hence the
Ratio.
We now prove that FMPs emerge naturally from certain assumptions about8.7.5. Optimality of FMPsreturns and FPM composition, which we use in Section 8.3.
Theorem 8.8:1. Alpha orthogonal is zero, so thatConsider a sequence of models =B, for some(B; (^) f; (i)) 2. Assume thatRm.


2. Idiosyncratic variance converges to zero in norm:ilim!1 (^) (B (^0) ( (i))  (^1) B)  (^1) = 0
Then in the limit Sharpe-optimizing portfolio is a weighted sum of the FMPs,and the weights themselves solve a MVO in factor space
wherewu??== arg max=Pu ? f (^1)  fu 2 Rmj^0 u (1= 2
 )u^0 fug
for someq 0
  f (^1) 
 >. 0. The Sharpe Ratio of the optimal portfolio is equal toSR?=
It is easy to check that the term inside the norm ismatrix of the idiosyncratic PnL of the FMPs. The condition states that theThe second condition on idiosyncratic variance has a simple interpretation.P^0 (i)P, i.e., the covariance
idiosyncratic variance of the FMPs goes to zero.Sharpe-optimizing portfolio problem, Equation (8.6): Proof. Start with the
)wwmax^2 ?R=n^0 w r^1  B^2 ^1 w^0 rw
The second identity is Woodbury-Sherman-Morrison Lemma.=^ [(^ (i)) ^1  (^ (i)) ^1 B(^  f^1 +B^0 (^ (i)) ^1 B) ^1 B^0 (^ (i)) ^1 ]B


Now we perform a rst-order expansion: Notice that (^)  f (^1) (B (^0) ( (i))  (^1) B)  (^1)  (^)  f (^1) (B (^0) ( (i))  (^1) B)^14   (^1)! 0 ; i!1
So we perform a rst-order approximation of the inverse(  f (^1) +B (^0) ( (i))  (^1) B)  (^1) =[(  f (^1) (B (^0) ( (i))  (^1) B)  (^1) +Im^15 )(:B (^0) ( (i))  (^1) B)]  1
Replace the expression in the solution of'(B^0 (^ (i)) ^1 Bw) ?:^1 [Im ^  f^1 (B^0 (^ (i)) ^1 B) ^1 ]
w?=== ((( (((iii))))))   ^111 [[BBB(B   (^0) (BB ((BB(i)^00 )((  

1 ((Bii)))))    111
 BB)) f   (^111) [[IBm (^0) (  ( (^) i) f)B^1 (B ^0 ( (^)  f( 1 i)]]) ^1 B) ^1 ]B^0 ( (i))B]
The expected PnL of the optimal solution is=Pu? ^0  f^1 . The factor exposure of
the optimal solution iscratic variance is  f^1 . The factor variance is 
2 ^0  f^1 . The idiosyn-
(w?)^0 (i)w?==(P u(^0 ?B) (^00) ((PB 
0 ((i (^) )) (i) 1 )B ) (^1)  B 1 )  k (^1) uu??k 2
holds.^1415 Given two square matricesThe rst-order expansion (from Neumann's series) is (A;B, the inequality on spectral normsI+A)  (^1) 'I kAAB.k  kAkkBk


and is zero in the limit, per the second assumption. The Sharpe Ratio isq 0
  f (^1) .
8.7.6. Single-Factor Covariance Matrix Updat-ing
Here we prove a basic result on the updated factor covariance matrix whenadding a new factor. The analysis assumes that the parametersthe factor model are constant, and so is the vectoraor characteristics that weB; (^) f; (^) of
using to augment the factor model. As in Section 8.3.2.Theorem 8.9: Let the loadings, factor covariance matrix and idiosyncratic
of a factor model beDene bBm+1; (^) = (f; (^) In, and let B(B 0
 a  (^21) BR) n 1 be a vector of characteristic.B 0
   (^1) )a
The factor covariance matrix associated to the model with loadingsgiven by [Bjbm+1]is
Proof. Let the factor return of the new factor be^ ~f'^264
0 f ^^2 m^0 +1^375
f^m+1;t==v^ m 0 b+1 (^0) mbr+1t^0 m +1 ^1 b m^1 +1!rt


as in Equationimpact on the idiosyncratic returns in the sense thatthat (^) is approximately unchanged by the addition of the new factor. Then(8.14). We assume that the new factor does not have a bigjbm+1;if^m+1;tjjt;ij, so
the volatility of the new factor is ^f^m (^2) +1;t=E(bm (^0) m(b+1+1 (^0) m (^) +1= (  
1 b ^0 mt 1 b+1 (^0) t (^) m (^)  +1  (^1) b)^12 bmm+1+1)) ^1 =^2.
)^m^2 +1==(bb^0 m( (^0) m+1b+1 (^0) m^ +1    
11
  b (^1) m^ b+1m ^1 +1) b 1 m) 2 +1
We show thatcolumn vector of the rstf^m+1is approximately uncorrelated to the rstmfactor returns isP (^0) rt. mfactors. The
E(ff^m+1) ==^=^Emm 22 (P+1+1^0 rPPtr (^00) (^0 tB
vrm +1 fB 1 )b 0 m++1 (^) )   (^1) bm+1
=^=Pm^20 +1(v (^) mf+1(B^0  ^1 bm+1) +P^0  ^1 bm+1)
The last equality follows from the orthogonality ofbetween FMPs is given by the idiosyncratic component of their returns, whichshould be small if the factors are diversied. bm+1. The correlation


# Chapter 9Beyond Simple

# Mean-Variance

## 9.1. Shortcomings of Nave MVOBefore introducing more complex optimizations, let's work through a simpleexample{maybe the simplest instance of the simplest optimization problem{to

## illustrate the implications of MVO. We have just two assets, with non-negativeSharpe Ratioscovariance matrix iss 1 ;s 2. Their returns have correlation. The inverse of the

## So by Equation (8.10), the optimal volatility allocation isC ^1 =^1  ^1 ^2264  ^1   ^1375

## vv 12 ??== 11    22 ((ss 12   ss 21 ))

## Whereon maximum portfolio risk. If >0 is a parameter determined by the risk tolerance or by the constraints 2 =s 1 < , then we short asset 2. Consider rst


the case whereAsset 2 acts asexpected return); b) it reduces the volatility of the portfolio, since it is positivelyhedges 2 = 0 and. Shorting it is benecial because a) it has no cost (zero >0. In this case, we always short the asset.
correlated to asset 1. When the Sharpe Ratio of asset 2 is positive, then thereis a cost to shorting, and for the hedge to be benecial, the correlation mustexceed a thresholds 2 =s 1.
is explainable, it is probably at odds with the intuition of many readers. Iftwo assets are very correlated, wouldn't it be preferable to go long both, thusEven though the recommendation to short an asset with positive returns
averaging out the signal error? We can make this reasoning more rigorous by as-sessing the impact of estimation error on expected returns and on the correlation.
RatiosRatios is bounded:Impact of errors in forecasted Sharpe Ratios~si, and assume that the error between the true and forecasted Sharpek~s sk. The realized expected return is. We denote thetrueSharpe
E(PnL) = 1   2 [(s 1  s 2 )~s 1 + (s 2  s 1 )~s 2 ]

Insight 9.1:Leta;x 02 RA Simple Linear-Quadratic Problemn. The problem minfha;xijkx x 0 k (^2)  (^2) ghas solution
hhaa;;xx? 0 ii x?1 ==x ^0  hak;kaxaak 0 ki
In the worst case, we solve the problem 308 minfE(PnL)jk~s skg. I leave


s 1

```
s^2 0.51.01.52.02.50.5 1.0 1.5 2.0 2.5
s 1
```
```
s^2 0.51.01.52.02.50.5 1.0 1.5 2.0 2.5
s 1
```
s^2 0.51.01.52.02.50.5 1.0 1.5 2.0 2.5
Figure 9.1:Sharpe Ratio of two assets, assuming a maximum errorParameters:Level plots of the loss of PnL (and Sharpe Ratio) as a function of the= 0:5; Correlation: (a)= 0:1, (b)= 0:5, (c)in the Sharpe Ratio norm.= 0:9.
the solution as an exercise (also, see Insight 9.1); the relative reduction in PnLis
This is also the relative loss in Sharpe, since the volatility of the portfolio is p(s^1 (s ^1  ss^2 )s^21 )^2 + (+ (s^2 s^2   ss^1 )^1 s)^22 
unaected by return forecast error. Figure 9.1 shows numerical results for twoassets, assuming an errorof 0.5 is perhaps conservative; actual dierences in forecasted versus realized= 0:5 and varying levels of correlation. An error
Sharpe Ratios are higher. Notice that high correlation makes things worse. Inall scenarios, the percentage in eciency is signicant. It is of course lower forhigher Sharpes (because the relative forecasting error is smaller); and is higher
for higher correlations. In all cases it exceeds 10% and can be as high as 50%.lationImpact of errors in correlation among assets~and assume that the estimation error is bounded:. We denote the true corre-j~ j . The

error in estimated correlation aects the volatility. We solve the problemmaxf(V?) (^0) C~  (^1) V?j j~ j g. In this case the worst-case realized relative


s 1

```
s^2 0.51.01.52.02.50.5 1.0 1.5 2.0 2.5
s 1
```
```
s^2 0.51.01.52.02.50.5 1.0 1.5 2.0 2.5
s 1
```
s^2 0.51.01.52.02.50.5 1.0 1.5 2.0 2.5
Figure 9.2:Sharpe Ratio of two assets, assuming a maximum errorParameters:Level plots of the loss of PnL (and Sharpe Ratio) as a function of the= 0:1; Correlation: (a)= 0:1, (a)= 0:5, (c)in the correlation.= 0:9.
volatility increase (exercise!) is
I am showing the impact of the error in Figure 9.2, for a reasonable error in p(V?)^0 C^2  j(^1 sV^1  ?+ 2s^2 j()(ss^12   ss^21 )()js^2  s^1 )j
(albeit not dramatically so). In Figure 9.3 I show the impact of correlation errorcorrelation estimate of 0.1. However, in periods of crisis, the error can be largeron Sharpe.
When we use Nave MVO optimization, the degradation in Sharpe RatioInsight 9.2:arising from forecasted (Degradation in Performance due to Forecasting Errorex ante) parameters for volatilities and returns
vs realized values (ex post) can easily range in the 10-50%.


0.000.050.100.150.00 0.05 0.10 0.15 0.20 0.25 0.30

```
0.200.250.300.35
ε
```
SR change
Figure 9.3:and 2, return correlationfraction loss in Sharpe Ratio for two strategies with Sharpe Ratios of 3= 0:3, and errorranging from 0 to 0.3.
9.2. Constraints and Modied ObjectivesEquationThey re
ect the detailed preferences of the investors, short-term concerns,(8.2)is the starting point for more complex optimization problems.
regulatory constraints, and implementation considerations. In applications,optimization formulations dier widely because they address a wide range ofconcerns:
 Investor's preferencesequal to zero."Tactical considerations: \Keep medium-term momentum exposure exactly: \Don't trade this stock because it could be acquired
 tomorrow" or "liquidate this stock because it could be acquired tomorrow";both are valid, if incompatible, concerns.Regulatory considerations: \The portfolio must be long only".
 Fiduciary considerationsdierence in returns between the portfolio's returns and the benchmark'scannot exceed a certaintracking volatility: \The portfolio must". tracka benchmark, i.e., the


From a modeling viewpoint, constraints can take several forms. We introduce Implementation considerationstrading costs." : \The objective function must include the
those rst, and then we map them to the applications at hand. The \mapping"part will be either instructive if you have never been exposed to it, or terminallyboring if you have worked in portfolio management for a few years. Rejoice
with the former group, and commiserate with the latter.
9.2.1. Types of ConstraintsAlthough one can imagine innite types of constraints, some of them are muchmore common than others. We review them below.

 Linear constraintsA (^0) w. These can be inequality or equality constraints:c (Inequality constraints) (9.1)
These are perhaps the most common constraints in nancial optimization,A^0 w=c (Equality constraints)
because they are used to address several of the concerns listed at the beginningof the section. For example, some strategies are required to beThe constraint is simply long-only.
Extending this to a bound on maximum short and long size for a singlew^0 (Long-Only constraint)
position is only a small step. The rationales for suchThere are natural limits due to maximum institutional ownership of a stock 312 box constraintsare many.


(say, no more than 5% of the outstanding stocks); or to the maximum riskconcentration in a stock: the idiosyncratic variance of a stock may not exceeda certain percentage of the total idiosyncratic variance, which translates to a
linear constraint. Further still, we may impose a maximum liquidation costrequirement on all stocks; which also becomes a constraint on single positionsize.
A slightly more complex constraint, which does not seem linear at rst sight,is on Gross Market Value:limits on nancial leverage that the fund wants to apply to its managed assets.Pijwij G. This constraint may originate on
The constraint may be turned into a linear onevariables representing the long and short side of a position, and additionalconstraints:^1 by introducing ancillary
wxy=^00 x y(GMV constraint) (9.2)(9.3)(9.4)
A similar constraint is on the long vs short ratioXi (xi+yi)G^2. If we want the long/short(9.5)
ratio to be equal to a certain value, then the constraint isThis constraint is the same as the GMV constraint, with the exception of 1 Piwi+=KPiwi .
the modeling of the GMV constraint, so that you just have to specify it.net-long portfolios, with a 30% of Net Market Value invested in shorts and 130 % invested in 2 Before rediscovering the wheel, know that some nancial optimization packages abstractFor example a few years ago,130/30 portfolioswere popular. These strategies managed
longs


Equation (9.5), which we replace withXi xi=KXi yi (Long/Short ratio constraint)

Yet another class of constraint is that on factor model exposures, and onexposures to other asset characteristics not in the model. An example is theconstraint on historical market betas (^) i. The constraint then isPi (^) iwi=b 0.
The general form of factor exposure isA constraint on maximum portfolio turnover takes a similar form to theprevious constraints that use absolute values. I am leaving it as an exerciseverbatimthat of Equations (9.1).
to the reader. The turnover constraint may be either (poorly) justied tocontrol costs, or by duciary requirements on portfolio turnover. A betterway to model costs takes us in the domain of non-linear constraints.
 Non-linear constraintsTrading occurs over many periods, and one approach to control excessivetrading is to limit the traded capital, possibly weighted to account for asset-. A constraint of a dierent nature is trading-related.
specic trading cost, in each portfolio rebalancing. This is equivalent toassuming linear transaction costs. We generalize this at little cost, and modeltrading costs as superlinear in traded amount but growing at a quadratic
rate or less:Xciijciwjwiji^  , wherewstarti j (^)  (^2) C[1;2]. The constraint takes the form:(Trading cost constraint)
Quadratic constraintswhereis convex, so that the portfolio optimization problem has a unique solution.wstartis the portfolio held at the beginning of the period. The constraintappear naturally when we want to control risk at a ner
resolution than that on total variance. For example , let 314 stylef be the principal


submatrix in the factor covariance matrix, and letthe vector of style factor exposures. Then a constraint on the maximumstyle-factor risk becomes bstyle= (Bstyle)^0 wbe
(bstyle)^0 stylef bbstylestyle=(B^2 stylestyle)^0 w(Style factor vol constraint)
Risk constraints are often not only applied to the positions of a portfolio,but to thelong-only portfolio with a GMV of $1B, and letactivepositions of the portfolio itself. For example, consider awbenchbe the positions of
a portfolio with the same GMV, with weights proportional to those of theSP500 benchmark. Theis the volatility of the active portfolio, and is a measure of the freedom theactive holdingsarewa=w wbench.tracking error
portfolio manager has in selecting stocks. A constraint on the tracking erroris
 Non-convex constraints(wa)^0 rw. Finally, there are a few constraint types that lead toa^2 a (tracking error constraint)
a non-convex feasible region. Finding a global optimum is in general NP-hard.Convex solvers may either not accept such constraints, or may not converge.I would argue that, in most cases, these constraints shouldnotbe used on
grounds of sensible modeling. I am presenting them both for completenessand as a cautionary tale.The rst constraint type is on the maximum numberNmaxof assets in the
portfolio. This is usually implemented by introducing 0/1 variables 315 xi, and by


setting a maximum (large) absolute position sizejwijMxi i= 1;:::;n (Max number of positions)M. The constraint becomes(9.6)
Xi=1n xxii2fN 0 max; 1 g i= 1;:::;n (9.7)(9.8)
The rationale for this constraint is that a very broad portfolio may betoo burdensome to trade or manage. This combinatorial constraint can behandled by some commercial solvers for realistic problem instances with
thousands of assets. However, its utility is limited. It is usually preferable tomodel trading costs directly, and either not include a constraint at all, orhave a threshold for trading below which the trades of the optimal solution
are set to zero. This usually has a negligible impact on optimality.A very dierent type of constraint is on percentage of idio variance. We havementioned this metric in Section 3.5.2. It is tempting to include a constraint

of the form w (^0) wpidiow (^0) rw (9.9)
or, equivalently, w (^0) [pidioB
fB (^0)  (1 pidio) (^) ]w 0 (9.10)
The problem is that the matrixpositive denite, and therefore the constraint is not convex (exercise: proveit). pidioB
fB^0  (1 pidio) (^) is in general not


A constraint type with a similar objective is to require a minimum id-iosyncratic dollar volatility:constraint, and its proponents should be excommunicated from the Orthodoxw (^0) w (^2) idio. This is obviously a non-convex
Church of Optimization. A sensible approach is to simply upper bound thefactor variance, or impose bounds of factor exposures, and test the impactof the bound on the portfolio's performance.
Yet another excommunicable oense is imposing a lower bound on totalvolatility. I would not mention it, had I not witnessed actual humans proposingit.
In the same spirit, i.e., the goal of ensuring that the portfolio meets aminimum size, is a lower bound on Gross Market Value. The answer tothese constraints is that they are usually ill-conceived. If, after accounting
for excess return forecasts, trading costs, and risk constraints, the optimalportfolio is small, then maybe it should stay small. And if one really wantsto make it bigger (again, not advisable), one could loosen the upper bounds
on risk or underestimate the transaction costs.
9.2.2. Do Constraints Improve or Worsen Per-formance?
The nave answer to the title of this section is that{of course!{they worsenperformance. If you reduce the feasible region of your optimization problemby adding a constraint, you will not get a better optimum. Specically, if
we maximize the Sharpe Ratio, adding constraints will degrade the Sharpe


Ratioexpected returns, are estimated correctly. If we take estimation error intoaccount, however, constraints may help. The next section interprets constraints^3 This is true if the data in the problem, i.e. covariance matrix and
as regularization terms for parameters entering in the optimization^4.
9.2.3. Constraints as PenaltiesOne alternative way to interpret a constraint in portfolio optimization is as apenalty term added to the objective function: given a problem
maxs:t:gf((xx))a
with optimal solutionx?(a), there is amaxf(x) ?(?a(a))>g(0 such thatx)
has the same solutionchapter. The parameterconstraint's right-hand side parameterx?(?a(a). We used this result at the beginning of the) can also be interpreted as a sensitivity to thea. The variableis the marginal change
in the optimum when we increase (or \relax")commercial solver returns bothat zero additional cost. This results also opens up a dierent modeling approach.x?and?, this means that we get sensitivitiesa:df(x?(a))=da=(a). Since a
for an early contribution to the analysis of long-only constraints; The work by DeMiguel et al.[2009a,b] on trading penalties; Fan et al. [2012] on GMV constraints and Ceria et al. [2012],^34 For example, see Clarke et al. [2002].The academic literature on this subject is not very large. See Jagannathan and Ma [2003]
Saxena and Stubbs [2013] on penalties on the factor covariance matrix. 318


What if we converted constraints into penalties? We now know that the outcome,for the appropriate penalizing coecient, is the same. Does this mean that theapproaches are equivalent? The answer is no, and the remainder of this section
is devoted to illustrating the dierence.There are constraints that are commensurable with the objective, and that areFirst, let us focus our attention on the meaning of constraints and penalties.
naturally expressed as penalties. For example, you could put a constraint onmaximum trading costs. However, costs and expected PnL in the objective havethe same unit (dollar) and it makes more sense to express the objective function
What about risk? If we x the time interval, the variance constraint has theas the dierence of PnL and trading cost. The penalty parameter is simply one.dimension of dollar squared, and is therefore not commensurable to PnL in the

objective. What we could add to the objective function ispossible in some optimization packagesvalue 0 of nal volatility, we can choose a penalty parameter such that the (^5) However, if we know the approximatepw^0 rw. This is
adding a volatility term or a variance one gives a similar result. We do so bylinearizing in the region of the optimum portfolio:
 q^20 + (w^0 rw ^20 ~)' = 0   0 (w~w^0
0 rwrw  02 )
The constant term is irrelevant to the optimization problem, and the volatility:=^0
is locally approximated by a variance.than a variance constraint or penalty. (^5) A volatility constraint or penalty is in practice computationally more burdensome to solve


we add the constraint on GMV as a penalty? Or long-only constraints? Theanswer, somewhat surprisingly, is that adding those constraints as penalty mayA second class of constraints does not have an obvious interpretation. Should
actually help the performance of the optimized portfolio, when the parametersin the model are not accurately estimated.Let us start with an augmented version of Problem (8.6):

maxs:t: (^) kw^0 wk 2  w
G rw (9.11)
whose penalized version ismax 0 w w
rw kwk (^2) (9.12)
This problem can interpreted in many dierent ways. The rst one is a simplerewriting of the quadratic terms asproblem then is a MVO problem with a modied covariance matrix. Thew (^0) ( (^) r+ (=)In)w =:w (^0) ~rw. The
correlations of the original covariance matrix have been reduced by a factor=other; in the limit(+). The asset variances have been increased, and are more similar to each! 1they are identical. The norm constraint therefore
has a \regularizing" eect on the solution. There are dierent optimizationformulations that leads to the same solution of the optimization problemUncertain Alpha. Let us start with the assumption that the vector (9.12)is not.
known with accuracy. We we have instead is the knowledge that the vector isdistributed according to a multivariate Gaussian: N( 0 ; (^2) In). We still


solve a MVO, taking into account alpha uncertainty:var(r (^0) w) = var( 0 w) + var(r  ) (^0) w) =w (^0) ( (^2) In+ (^) r)w
The MVO formulation is again the same as that of Equationmodied covariance matrix. As in the case of Equationare made more equal, and correlations are shrinked toward zero.(9.12)(8.6), the variances, but with a
that we know their distribution, we model their error deterministically, andadversarially: we know that the true alphas are within a certain distanceRobust Alpha. Instead modelling alphas' imperfect estimation by assumingdfrom
our estimate and, as we did at the beginning of the chapter, we look at theworst case, i.e., the realized alpha is worst possible one among the admissiblerealizations. In formulas, we solve
maxs:t:aa^0 w= arg min wx^0 frxw (^0) wjjjx  jjdg (9.13)(9.14)
We know what the solution to the nested problemequal toa=  dw=kwk. Hence we solve (9.14): from Insight 9.1, it is
This is similar, but not identical, to Equationmax^0 w w^0 rw (9.12)dkwk: the norm penalty term(9.15)
is not squared. The same argument can be made to show that the norm andthe norm squared are interchangeable, once the penalty constantdkwk'(d=kw 0 k)kwk (^2) , for akw 0 kclose tokwkof the nal solution.dis rescaled:
Robust Factors. We consider another instance of constrained optimization. 321


```
A recurrent theme in this book is model misspecication. Factor models can bemisspecied (both in their factor structure and in their expected returns), butthey also oer remedies. Consider the case of an omitted factor. As a special
case of misspecication, its eect is to worsen the Sharpe Ratio of the MVOportfolio. In order to reduce the impact, let us consider again an adversarialapproach. Assume that there is a hidden factor, whose loadings we do not know,
but whose volatilityimportance of the omitted factor.The new factor model an additional factor loadingis given. We use this as a parameter to quantify thevorthogonal toB. The
```
covariance matrix is ~r= (^) r+ (^2) vv 0
We solve maxw kminvk 10 w w (^0) ( (^) r+ (^2) vv (^0) )w
maxmaxww 00 ww  ww^00 (( (^) rr++k 2 wI^2 kn) (^2) www^0 )w
So, yet again, we are solving an optimization problem with a penalized covariancematrix.Robust Asset correlations. Another case of adversarial modeling that is
expressed as a penalization term. Assume that we estimate the asset correlationmatrix terms with some error independent of the asset pair, so that the dierencebetween estimated correlation between and true correlation is at mostji;j 
^i;jjd. The adversarial model looks for a solution to the MVO problem, where 322


Nature chooses the covariance matrix with the highest variance compatiblewith the error bound:

maxs:t:a^02 w= arg max ^2  w (^0) ( (^) r+)wj[]i;jjd (^2) [ ]i;i[ ]j;j;i;j= 1;:::;n(9.16)(9.17)
The objective of the nested problem is equivalent tow (^0) w=Xi;jwiwj[ ]i;i[ ]j;ji;j (9.18)
Every term is maximized whenvalue is i;j=d^2 sgn (wiwj), and the objective function
(w?)^0 w?==dd^22 (XXi;ji jjwwiiwj[j j[] (^) i;i])i;i 2 [ ]j;j (9.19)(9.20)
Whereis a diagonal covariance matrix whose=d^2 kwk^21 ith diagonal term is the variance(9.21)
of asseti. Let us plug this back in the original problem:maxa (^0) w w (^0) rw d (^2) kwk (^21) (9.22)
And we have yet again a penalization term, which is, in this case, the squareof an L1 norm of the portfolio weights. The functionthe optimization problem is tractable. I am summarizing the penalizationkwk (^21) is convex, so


```
approaches in the table below:robust covariance optimization. We assume that the adversary has a budget forRobust Covariance Matrix. Consider a dierent starting point to model
the maximum cumulative squared error of the asset covariances:This is the same as a bound on the Frobenius norm of the error,robust problem formulation is similar to the previous one: Pi;jk[]k^2 i;jF. Thed^2.
```
maxs:t:a^02 w= arg max w^0 rwnw  (^0) w^2 jkk (^2) Fd 2 o
The strategy to solve this problem is similar to previous cases: the adversarymaximizes a linear objective function with a norm constraint; see Insight 9.1 forthe solution. In this case, (?) (^2) =d (^2) kwk (^2) , yet again, and the problem becomes
an MVO with a quadratic penalization term.ApproachUncertain Alpha Penalty (^2) kwk 2 Parameter Interpretationstd.error of ^
Robust AlphaRobust FactorRobust CorrelationsRobust Covariance dddkw (^22) kkkkwwwkkk 2221 max distancevolatility of a missing factormax distancemax distancekjjj (^) i;jr    ^^ ^ki;jrjjj
(9.12)Exercise 9.1:interpretations of this penalty, and discuss their applicability to real-worldto this norm. Read [Olivares-Nadal and DeMiguel, 2018] for additional(30) Dene the normkxk;p:=^  ^1 x^ p. Extend Problem
settings.


Although they can yield the same optimal portfolio, the constrained andInsight 9.3:penalty version dier in two important ways. The rst one is that theThe Distinction Between Constraints and Penalties
shadow price of the constraint is not known before the optimization isrun. This means that the solution can be very sensitive to the choiceof the right-hand side of the constraint: we don't know the trade-obetween constraint limit and optimum value. This is not the case with
a penalty: weinterpretation (like the price for risk). In successive optimizations, thisprice is unchanged making comparisons easier. When the interpretation isclear, penalties are preferable. The second dierence is almost a corollarysetthe price, and the price has often a straightforward
which is always feasible.of the rst one: in the constrained formulation, we may have no feasiblesolution, which is, in a loose sense, like saying that the price of theconstraint is innite. This is never the case with a penalized formulation,
9.3. How Does Estimation Error AectSharpe Ratio?

An investor starts with estimates of expected returns and of the covariancematrixproportional to (^6). We denote them with ^ r (^1) ^; the proportionality constant is irrelevant for the Sharpe ^ and ^rrespectively. The MVO portfolio is
Ratio. The realized Sharpe Ratio, however, is a function of the true expectedreturns and covariance matrix ; (^) r:
(^6) The third leg of the trading stool is a model for trading cost. We will cover this in laterSR(^ ^;^ ^r) =q(^ ^ r^10 ^(^ ^)^0  r^1 r^ ^(^ )^ r^1 ^)
chapters 325


We compare the realized Sharpe Ratio to the best Sharpe ratio, based on thetrue values of and (^) r, given by Equation (8.5):
We call this theSharpe Ratio EciencySR(SR(^ ^;;^ ^(SRE). It is important to study thisrr))
quantity, because we want to know, at all times, whether we are losing a greatdeal of performance from inaccurate parameter estimation or large transactioncosts. We will ask a few qualitative and quantitative questions, and see how far
can the analysis take usworsen performance.The rst fact is intuitive, but still needs to be proved. Incorrect estimates^7.
it equal to one if and only ifTheorem 9.1: The Sharpe Ratio Eciency is less or equal than one, and if  r^1 =^2 and (^1) r=^2 ^ r^1 ^ are collinear.
Proof. The SRE isSR(SR( ^;; ^rr))=q 0
 ^ r (^1) ^
Let^8 ^^0 ^ r^1 r^ ^ r^1 ^q^01  r^1 (9.23)
ba:=:=^  r^1 r=^12 = 
2 ^^  r^1 ^ (9.24)(9.25)
error, are Michaud [1989], Shephard [2009], Chopra and W.Ziemba [1993].Decomposition. Dene^78 Early papers on model estimation error, and the relative impact of alpha and estimationLetHbe a symmetric positive denite matrix and letH 1 = (^2) :=V 1 = (^2) V (^0). ThenH 1 = (^2) H 1 = (^2) =HVVand (^0) be its Singular ValueH 1 = (^2


2) op=kHkop.


so that SR(SR( ^;; ^rr))=kaakk (^0) bbk
The Sharpe Ratio eciency is always less than one because of Cauchy-Schwartzinequality (^9) , unless  r 1 = (^2) and (^1) r= (^2) ^ r (^1) ^are collinear.
9.3.1. The Impact of Alpha ErrorIt is more useful is to derive lower bounds on performance ineciency, basedon the estimation error of either expected returns of covariance.
dened as the operator norm. Dene the relative alpha error asWe need to introduce a few basic results. Let the norm of a matrix be (^)
In the Appendix (Section 9.5.1) I prove the following result:^ k^ k k^ ^^k^ alpha
SR(SR( ^;; ^rr)) 1  ^  r (^1

2) k (^) rk 2 alpha 2
9.3.2. The Impact of Risk ErrorTheorem 9.2(Misspecication of Risk): If there is > 0 such that
(^9) Which can be found in almost any linear algebra book. If^1 r=^2 ^ r^1
1 r=^2  I^2  x;y 2 Rn, thenj(9.26)a (^0) bj 
pa (^0) apb (^0) b, with the equality holding only if 327 a=b.


Then SR(SR( ^;; ^rr)) 1   (^2) + (9.27)
is interesting about this result is how weak it is. Let us consider a few specialcases. We deneThis formula follows directly from the EquationH:= (^1) r= (^2) ^ r (^1
1) r= (^2). (9.23). At rst sight, what
1. If the estimated covariance matrix is biased, but uniformly so, i.e.,from the previous chapter. What happens in practice is that we would (^) r, thenH=  (^1) I, and there is no eciency loss. We knew this already ^r=

2. deploy a portfolio with the highest Sharpe Ratio, but incorrect volatility.Say, however, that weso thatH6/I. It can still happen that we have a SRE of one! Thisreallyestimate the covariance matrix incorrectly,
    (9.23)will happen ifeigenvalue. Say the associated eigenvalue is^ ^ is proportional to an eigenvector of^. Then, use directly EquationHwith a positive
       Even more pathologically, though, this also implies that if ourSRE =^ ^k^0 (^ ^^ k^ ^^2 )s^ ^k^0 (^ ^^ k^22 ^)= sgn (^ ) ^ is
       proportional to an eigenvector withRatio Eciency is -1. Incidentally,positive denite, so a negative eigenvalue is indeed a possibility.Hnegativeis neither necessarily symmetric noreigenvalue, then the Sharpe

3. But, you may argue, this is an exceptional circumstance. Consider a sim-pler but instructive case. We make the assumption thateigenvectors as (^) r. In other words, the Singular Value Decompositions ^rhas the same


only dier because of the Singular Values. (^) r=UU 0
so thatH=U^1 =^2 U^0 U^ ^1 U^ ^^0 Ur=U^1 =^2 U^U^00 =U^ ^1 U^0 ; a great simpli-
cation. Denote the eigenvalue ratioon the SRE in this case? We solve fori:=:i=^i. What is the lower bound
:= min= min^ qUmax(i ^( i^1   ) 2 I)U^0


2
For?= (maxii+min=i^12 i(max)=2. We use these values in Equationi i mini i) (9.27)to
obtain SRE 1  maximaxi imini ii=maxminiiii
Hence the loss in eciency arises from the fact that we estimate unevenlythe volatilities of the eigenvectors of the asset covariance matrix. If weunderestimate them (or overestimate them) by the same constant, then
we lose nothing, as noted in the rst point above. Let us think of anadverse case. Say we estimate all volatilities exactly (one, which we underestimate by 50%. Then the worst-case loss in Sharpei= 1) except for
Ratio can be in 50%.


turns)9.4. Trading Sharpe For CapacityExercise 9.2: (30) Consider the problem(The trade-o between sharpe ratio and absolute re-

V(r) := mins:t:Aw 000 ww (^) rwrc (9.28)
and dene the associated Sharpe Ratioization of the dual of the original unconstrained problemSR(r) :=r=pV(r). This is a general-
V~(r ) : min (^0) wrw^0 rw
One special instance is the problemV(r) := minw (^0) rw
s:t: X 0 iwjwirj 1
In this instance,portfolio and1. Prove thatpVrV(is a minimum required return on Gross Market Value of ther() is the smallest achievable volatility.r)V~(r) for allr 2 R;

2. Prove that3. Prove that4. Prove thatpqSRVV~(((rrr) is non-increasing and trivially bounded by) is increasing and convex;) is linear and increasing; SR.f


This exercise shows that a high Sharpe Ratio can be traded o for higher payos,included higher returns on GMV. For example, while the MVO portfolio mayhave a high Sharpe but low return on GMV, a constrained version can achieve
higher return, but at the cost of a lower risk-adjusted performance.
9.5.9.5.1. Theorems on Sharpe Eciency Loss?Appendix
These theorems are informally introduced in Section 9.3.We recall that
and^ H ^1  ^21 kxkkHxkkHk^2 kxk
so that kHykkHxk+kH(y x)kkHxk+kHk^2 kx yk
jkHxk kHykjkHk 2 kx yk


Also, use the cosine rule: (^) kaak kbbk (^2) =2 1  kaakk (^0) bbk
)SR(SR(^ ^;;^ ^rr))==1ka akk^0 b 12 b kkaak kbbk (^2)
whereLemma 9.1:a;bare dened by Equations (9.24) and (9.25).LetHbe symmetric positive-denite,x;y 2 Rn, and
(^) kxxk kyyk (^) 
Then (^) kHxHxk kHyHyk (^) 2 minfkHk 2

 H  (^1

2) ; 1 g


Proof. (^) kLetHaHaak; b (^2) kHbHbRn.k (^) = (^) kHbkkHaHakk kHbHakkHb (^)
=k^ Hak 1 Hbkk(kHH((aa  kbbHa))k kk+(kjkHbHaHak kkk kHbHbk)kjHb)^
kkHaHa^11 kk((kkHH(ka 2 k (ab) kb+)kkH+kk (^2) Hkak 2  kabk )bk)
(a:=kxxk;b:=kyyk) k^ HaH^2 k^2 kxxkkH^ kkH^2 kk( 2 a^  kxxbk)k kyyk^
This bound is tight, up to a constant. For an example, consider the case of^2 kHk^2 H ^1

2 
diagonalhave^10 H:=diag ( 1 ;:::; n),x:=e 1 +en,y:=en, withn= 1. We
(^10) We use the notatione 1 ;:::;^ kexxnkfor the standard basis in kyyk^ r^32 =:Rn.


(^) kHxHxk kHyHyk (^) =^ pnen (^2) n++ (^21) e 211  en^
=vuuts 2  p (^2) n( (^2) n+^2 n (^12) n= (^2) + (n (^21) ) (^2)  =2 + ( 11 )! 22 + 1 ) (^2) n 2 (+^1 ) (^22)  (^21)
sp 12  (^2) n( (^1) n+ (^1 )^21 ) 2
Theorem 9.3(Misspecication of alpha)=p^13 kHk^2 H ^1 :^2 If
(^) k (^) k k ^^k (^) 
Then SR(SR( ^;; ^rr)) 1   2

  r (^1

2) k (^) rk  21  2
Proof. From Lemma 9.1: (^)  r 1 = (^2)
 r^1 =^2  ^  r r^11 ==^22 ^^^ = 2^2 q^   

1
 =^2  r^12




2 k^1 =^2 r^ k^22 


Then SR(SR( ^;; ^rr))=1  12







  r 1 = (^2)
 1  ^  r^1  r 21 k= (^2) rk^2  ^2  r r^11 ==^22 ^^^2
Theorem 9.4(Misspecication of Risk) (^1) r= (^2) ^ r (^1
1) r= (^2)  I:n If there is 2   > 0 such that(9.29)
Then SR(SR( ^;; ^rr)) 1   (^2) + (9.30)
the SRE Equation (9.23) and condition (9.29) areProof. LetH:=^1 r=^2 ^ r^1
1 r=^2 and let^ ^:=^  r^1 =^2. Using this notation,
kSR(SR(H ^ ;;I^ ^nrrk)) 2 =^ ^k^0 ^Hk^2 ^s^ ^k^0 H^k^22 ^
Letequivalent to 1  (^2) ji :::jneigenvalues offor alli= 1;:::;nH. The condition. kH Ink 2  is
^^ k^k^0 H^^0 ^Hkk^222 ^^ n (^21) ( +) 2
)^ ^k^0 ^Hk^2 ^s ^k (^0) H^k (^22) ^ 335  += 1 ^2 +


covariance matrix isthe left-hand side of Inequality (9.29) whenThe population covariance matrix is not known. A one-period proxy for therr^0. The next lemma presents a closed-form expression of (^) ris replaced by this proxy.


# Chapter 10Market-Impact-Aware

# Portfolio Management

## 1. importance of tcosts. Ref: WHAT HAPPENED TO THE REST? APRINCIPLEDAPPROACH TO CLEAN-UP COSTS INALGORITHMICTRADING

## 2. pre-trade in this chapter; post-trade in the after the trade part3. implementation shortfall or slippage. Denition: signed dierence betweenthe arrival price and average execution price of the order. Buy order and

## 4. positive slippage implies a loss; the opposite for a sell order.some orders do not get executed in time. This implies a loss, calledclean-up costs

## 5.6. order types: VWAP, TWAP, PWPthere is a trade-o between implementation shortfall and clean-up. Themore aggressive the order, the higher the former and the lower the latter.

## 7.8. liquidity suppliersLiquidity: depth, breadth and resiliency. Depth: large inventory; breadth:many participants. Resiliency: return to equilibrium

## 10.9. liquidity demanders


```
execute a trade, we incur costs of all sorts: nancing costs when we leverageour portfolio; borrowing costs when we short securities; commission costs toTrading canpossiblymake money, but itsurely costs money. When we
exchanges and other counterparties. In addition to all of the above, we pay anindirect cost: our actions move prices. It appeals to our intuition that, when wepurchase a security, we somewhat push its price upward, which in turn makes
the additional purchase of a security more expensive. What is less intuitive,however, is that this \price impact" can turn a strategy that is potentiallyprotable into a very unprotable one. We are then faced with two important
questions. The rst one is to adequately describe the laws governing priceimpact dynamics. The second is to use these laws to optimize the performanceof our trading strategy. These two questions inform the organization of the
chapter: in the next section, we provide a quick description of market impactmodels. Then we delve into optimal execution.
```
\Market impact is the cumulative market-wide response of the arrival of new10.1. Market ImpactA synthetic denition of market impact is the following [Velu et al., 2020]:
order 
ow". The underlying process is complex, and results from the jointcontribution of several factors: First, there is a direct reduction in inventory of the securities being bought
 or sold, causing a price movement.Secondly, there is an informational eect: initiating a transaction may revealprivate beliefs about the future price of that security, as well be informative
of future transactions in the near future. 338


 Third, there is a mimetic eect, where participants, in the absence of in-formation, imitate each other's behavior, leading to temporary run-ups ordraw-downs.
 Finally, there is a strategic aspect. Even in the absence of information leakage,participants trade so as to exploit potential arbitrages arising from priceimpact.
Each one of these phenomena is complex, and hard to model. The total trans-action cost associated to a trade is usually decomposed into three components:
Expected Transaction Cost =(spread cost)(temporary market impact)(permanent market impact)+ +
Themarket order \crosses" the spread, i.e. is executed at the best price oeredby the counterparty. This order reduces the available inventory available forspread costsre
ect the dierence between the bid and the ask price. A
transactions, and thus removes liquidity. On the other side, a limit order hasan associated execution price and adds liquidity. The average cost incurredin a trade is modeled as a fraction of the bid-ask spread, and assumed to be
independent from other transactions.has been executed.Thepermanent impactis the price change that persists long after the order
occurs during order execution and immediately afterwards, until price reachesequilibrium.Thetemporary impact (also called \slippage" is the price change that
In the rest of the chapter, we focus on temporary impact, and eectively 339


```
ignore both spread costs and permanent impact, although these are bothinteresting areas of research. The rationales for this choice are modeling prioritiesand brevity. From the vantage point of a modeler specically concerned with
portfolio optimization, as opposed to one interested in understanding themechanisms underlying price impact, temporary impact is by far the mostimportant concern because of its magnitude compared to the other two terms.
Secondly, even our discussion of temporary impact is kept as short as possible,but not shorter. The interested reader can consult the reference in the \FurtherReading" section at the end of the chapter.
```
We want to submit a large order, usually called a10.1.1. Temporary Market ImpactDepending on the asset class, we have dierent options for execution. Forparent orderor ameta-order.
example, we could split the parent order into smaller \child" orders and executethem on exchange. In other cases, Over-the-counter or alternate trading systemsare available. It is remarkable that, despite the broad array of trading venues
and matching mechanism, the expected market impact is described well by acommon formula, which we describe below. At time 0 we start trading, and wedenote byx(t) the cumulative number of shares traded up to timet, and with
We now introduce two functions: the instantaneous market impactxand the propagator_(t) the trading rate, i.e., the number of shares traded per unit time, at timeG:R+!R+. We also have a positive constant termf:R!R+t,,.
which is a function of the security characteristics. The expected temporary


T

E(PT)
P 0
Figure 10.1:t^0 Market Impact over time for a single trade executed at timet^0 t 0. The
decay aftermarket impact is given by the formulat 0 is proportional toG.

For an interpretation, consider the case of a marketable orderE(PT) P^0 =Z^0 Tf( _xt)G(T t)dt^1 single buy(10.1)
trade, a short \pulse" occurring at timeis proportional toand is followed by a \relaxation" back to an equilibrium level. The functionG(T t 0 ): an instantaneous price change occurs at timet 0. Then the market impact forTtt 00 ,,
Gan equilibrium level (see Figure 10.1) The functionmonotone increasing: the higher the trading rate, the higher the instantaneousis monotonically decreasing, thus re
ecting the long-term convergence tofshould be intuitively be
by a counterparty, and that therefore removes inventory.^1 A marketable order is one that executes immediately at the best available price oered 341


impact. The interpretation of Equationof pulse trades, each of one having an impact that relaxes back to equilibriumover time. The big question is then what is the functional form of(10.1)is then as a linear superpositionf andG.
Below are a few alternatives: [Almgren et al., 2005] The functions are
fG( _(xt) =) =(t)xv_^
where:per unit interval' andcentered at the origin). The trading cost is  0 :6,is the security's volatility;() is Dirac's delta function (a \pulse" function withvis the number of shares traded
C[x] ==v ZZ 00 TTdtdtx_x_t1+tZ 0 tdsx_vs^ (t s)
As an important example, we trade share quantity[0V;T=] and the total traded volume in the market in the same period isvT. The ratioQ=V is usually referred to as theQparticipation rateat constant rate inor
POVcosts are(\Percentage Of Volume"). From the formula above, the total and unit
Cc==QVQV^ Q


The unit cost is decreasing in the execution time. By replacinghaveThere is an argument made on the basis of physical dimension that suggestsc/T  (^). V=vT, we
thatof the Almgren Market Impact. They assume that there are only threequantities that matter: = 1=2. Pohl et al. [2017] propose an argument for the universality
{{ QVthe same period., which we interpret as the dollar value traded during a period., which we interpret as the dollar value traded by all participants during
{The transaction costphysical unit of the inverse square root of time., the security's volatility during the same period. Volatility has thecis dimensionless and invariant in the units chosen for
currency and time. If the argument is a polynomial of the input quantitiesabove, we write
c(Q;;V;T[number] =) =F([currency]Va[time]Qbc)a[currency]b[time] (^11) = 2 c
From which 0 =aF(=V   11 == 2 2. It follows that the cost is a function ofQ 1 = (^2) ). a+band a c=2 = 0. Set, without loss of generality,V  1 = (^2) Q 1 = (^2) :c(Q;;V) =
 [Kyle, 1985, Huberman and Stanzl, 2004] This model is a special case ofAlmgren-Chriss's model and precedes it historically. The functions are
fG( _(xt) =) =(t)xv_


 The model is interesting in the sense that it is[Obizhaeva and Wang, 2013] The functions are:
fG( _(xt) =) =exv_ t=
The trading cost is C[x] =Z 0 Tdtx_te t=Z 0 tdsx_vses=
Consider, again the constant-rate trade ofThe trading cost is Qshares over an interval [0;T].

C==QTQT^221 v (^1) vZ[ (^0) TT dte (1t= Ze (^0)  tT=dse)]s=
Consider the two cases where timescales of execution and relaxation separate:c=h^1  T(1 e T=)iQV (10.2)
\slow" executionTand \fast" executionc' (^8) >>>< T:
For the slow execution case, the unit cost is inversely proportional to execution>>>:T^2 QVQV ififTT
time, whereas it is independent oftime series is shown in Figure 10.2. The Obizhaeva and Wang model (O-WTwhenT. The overall market impact


henceforth) has a dynamic formulation. Lettraded notional, andq:=Q_. The O-W market impact is modeled asQ: [0;T]+!Rthe cumulative
With an initial condition I(0) = 0, and with constant rate of executionI_t=vqt ^1 It
q=QT=T, this dierential equation has a simple solution:It=vq(1 e t=)
and the trading cost is given byC=Z 0 TdtItq
==Tvh 1 q ^2 [1T (1T (1e  T=e )T=i)]QVTQT
 The formula of[Gatheral, 2016] The functions arec=C=QTis the same form as Equation (10.2).
fG( _(xt) =) =p 1 txv_^1 =^2

The trading cost is Z 0 Tdtx_tZ 0 tdsx_vs 1 = (^2) pt (^1)  s


time

P 0 Impact

```
Ptend
t 0 tend
Figure 10.2:impact. The solid line is the sum of temporary and permanent market impacts.Market Impact over time. The dashed line is the permanent market
```
The constant-rate trade ofQCshare over an interval [0= (^43) rQTV Q ;T] is
The unit execution cost isc/c=p^43 Q=vr, and independent ofQTV T.
We now introduce a multiperiod optimization model. We rst focus on the10.2. Multiperiod Optimizationspecial case of a single asset. While interesting in its own right, this simple case
can be extended to more general cases. Its extensions and uses in application 346


will be the subject of Section The assumptions underlying the model are:1. The alpha signal follows an AR(1) process:2. The asset has volatility. (^) t=t  1 +t  1.
3. The market impact follows an Obizhaeva-Wang model.4. The optimization asks to solve a discounted mean-variance problem, wherePnL is inclusive of transaction costs:P (^1) t=0 t[E(PnLt) var(PnLt)]
The autocorrelation function of the alpha istime scale of alpha decay iswhere^ is a positive constant smaller than one. = (log)  (^1). cor( (^) t+s;t) =s, so that the
We need a few denitions.10.3. Baldacci-Benveniste-Ritter
hxkx;yk 2 i:=:=Ehx;xZ (^0) i^1 x^0 sysds
(Kx)t:=Z 0 txsds


The adjoint operator ofhx;Kyi=EKZis such that 01 x (^0) s(Z 0 sytdthK)dsx;yi=hx;Kyi. In formulas:
==EE[[ZZ 0011 (Zxtt 1 dtxZ (^0) t (^01) dty (^0) )sy^0 tdsdt^0 ] Z 01 (Z 0 t^0 xtdt)yt^0 dt^0 ]
)(Kx)t==EE[tZZ^0 t^11 Exuu(duZu^1 xu^0 du^0 )yudu]
Objective: maxx EZ 01 [ (^0) txt  (^12) x_ (^0) tCx_t  (^12) x (^0) t
xt]dt (10.3)
maxu EZ 01 [^0 t(Ku)t ^12 u^0 tCut ^12 (Ku)^0 t (xK:=u)Kt]dtu (10.4)(10.5)
FONC on functionalsF[u] :=h;KrFui =K^12 hu; CuKCui  =^12 KChx_K+ uKK;^ uK= 0
xui (10.6)(10.7)(10.8)
This is a linear system. Some denitions. EFor somes(x) :=Ex,(xtjFs). The tower property of expectation isEsEt=Es^t.
0 t, letxt 0 ;t:=Esxt. From the denitionxt 0 ;t,Etxt=xt(!).


ApplyEt 0 to Equation (10.8).Et 0 EtZt (^1) t 0 dt (^0) =CdtdEt 0 xt+EsZt (^1) 
xt
dtdEsZtE^1 t^0 Ztt^01 dt^0 d= 2 t^0 dt ^0 E=sCtdt=dECt^0 dtdx^22 tE+sx^ t Et^0 ZEt^1 t^0 xxtt
this is a linear ODE inEt 0 xtdt, which we can solve analytically. First, dene^2 xt^0 ;t= C ^1 t^0 ;t+C ^1 
xt^0 ;t
b t:=(:=ZtC^1  e^1  ^ (t) ^1 s=)^2 C ^1 Etsds (10.10)(10.9)
The solution that satisesxt 0 ;t=e  (t t 0 )xt 0 ;t 0 +x 12 tC 0 ;t  01 =Ztx 0 ttdse 0 ;t (^0)  and lim (t s)Zts!1 (^1) dzext (^0)  ;t = 0 is(z s)t 0 ;z (10.11)
From which it follows directlydtdxt 0 ;t (^) t=t 0 =  xt 0 ;t 0 +bt 0 (10.12)
Finally, frompolicy follows:dxt 0 ;t=dt=x_t 0 , andxt 0 ;t 0 =xt 0 , the law for the optimal trading
fx_?t==E Z x 01 t[+^0 tbxtt ^12 x_^0 tCx_t ^12 x^0 t
xt]dt (10.13)(10.14)


The discretized version of the optimal trading policy is :bt:=Xs (^1) =ttet (t s)C  (^1) Et(s) (10.15)
xt+1=(I t )xt+tbt (10.16)
Procedure 10.1:1. Input: Optimal Trading Policy
(a) symmetric positive denite cost matrix(b)(c) expected return processsymmetric positive denite return covariance matrixRnn ttaking values inC (^2) RRnnn 2
2. Dene(d) initial portfolio x:=(^02 CRn  (^1) ) 1 = 2

3. Output:(a) Optimal trading policy:bt:=Zt^1 e (t s)C ^1 Etsds
    (b) Optimum:x_t=  xt+bt)xt=e  tx^0 +Z^0 te sbsds


10.3.1. Comparison to Single-Period Optimiza-tion

Let us solve the single-period problem. Denemax(Ett+1) (^0) xt+1  (^12) (xt+1 xt) (^0) C(xt+1 xt)  (^12) xt+1
xt+1 (10.17)
max(Ett+1+Cxt)^0 xt+1 ^12 xt+1( +C)xt+1 (10.18)
In the casext+1^ = (C I^1 + ^ C ^1 1, we can approximate:^ ) ^1 xt+ (I+C ^1 ) ^1 C ^1 Ett+1 (10.19)
The solution is similar to multiperiod, in that it is a combination of the existing'(I C ^1 )xt+ (I C ^1 )C ^1 Ett+1 (10.20)
portfolio and an alpha-related term. If we assume thatand assuming againand the multiperiod solution is (^) C  (^1) 1, we approximate the rst term only ofEts= 0 fors > t+ 1,bt
The two are identical, except that a square root term appears in the multiperiodxt+1'(I t(C ^1 )^1 =^2 )xt+ (I t(C ^1 )^1 =^2 )C ^1 Ett+1 (10.21)
approximation.


When10.3.2. The No-Market-Impact LimitConsider the case of vanishing market impact. We setk k1, from Equation (10.15) we have C:=C^0 , and let#0.
bt:='ZZt 011 ee  (st  Cs) C 1  ^1 tEdstsds (10.22)(10.23)

=='       1  C ^11  e( 1  e s tsC   ^11 )tC^1 s=0  (^1) t (10.24)(10.25)(10.26)
and x_t=  xt+bt (10.27)
In the limit=# 0, a solution exists if^1 =^2 h (C ^01 )^1 =^2 xt+ (C ^01 ) ^1 =^2 C ^01 ti (10.28)
xt=(= C 1
   (^01)   (^1) ) t^1 C  01 t
This is the solution to the single-period MVO problem in the absence oftransaction costs. The optimal solution is to rebalance instantaneously to theMVO allocation, depending on the instantaneous alpha prediction. We have
recovered the result from conventional single-period optimization.


10.3.3. Optimal LiquidationSuppose that we hold a portfolio(t) = 0 a.s. fort0. What is the optimal trading policy? In this case,x(0), and have no forward-looking alpha:bt= 0
and the optimal trade-out policy is the solution to the equationi.e.,rate of liquidation depending on the matrixx(t) =e t x(0). We reduce the positions at an exponential rate, with the . The larger the coecient of riskx_t=  xt,
aversionslower the liquidation.and the volatility, the faster the liquidation. The higher the cost, the
10.3.4. Deterministic AlphaSay that the future returns are a deterministic functionis also deterministic and given by the integral(10.10). The solution to thet. The functionbt

ordinary dierential equation (10.13) isbt=Zt (^1) e (t s)C  (^1) sds
xt==ee    ttxx 00 ++ZZ 00 ttee  ssbsZdss 1 e (s u)C  (^1) ududs
It is useful to present an indicative case of a \spiked" alpha:In this case the functionbttakes a simple form: t:= 0 (t t 0 ).
bt= 1 (t 0  t)e (t t^0 )C ^1  0


Fortt 0 , xt 0 =e  tx 0 +Z 0 te 2  se  t (^0) C  (^1)  0 ds
In the formula above, we have introduced a direct extension of the hyperbolic=e  t x^0 +  ^1 e tcosh( t)e  t^0 C ^1 ^0 
cosine to squared matrices, i.e., sinh(Whent=t 0 the optimal portfolio position isX) := (eX e X)=2.
Fort > t 0 , the portfolio is liquidated in the absence of alpha:xt^0 =e  t^0  x^0 +  ^1 cosh( t^0 )C ^1 ^0 
In Figure xx we show the behavior of the complete function.xt=e  t x^0 +  ^1 cosh( t^0 )C ^1 ^0 
10.3.5. AR(1) SignalLet us consider rst the case of autoregressive signals.
t+1rt==t+t+tt (10.29)(10.30)
where  is a diagonal matrix with []i;i 2 (0;1)
tN(0;^ ), with;^ diagonal and positive denite 354


Usually we make the assumption that ^ tt,Ntindependent of each other(0;^ )^

The long-term volatility oftis (^2) (1 (I ^2 ) ^12 =)^2  . Since^1 k^ k.
Ettt++ss==ts+t^ sXi =0^1 s it+i (10.31)(10.32)
The long-term covariance matrix is := [C  (^1) ( (^)  (^) + + (^2)  (^) (I^2  (I  2 ) ^21 ))] ^11 =. Let 2
It follows that bt=Xi (^1) =0e i C  (^1) it (10.33)
Let us make the assumption that 
invest in idio space. Theith element ofis diagonal. This is reasonable when webtis
b^ t;ii==qct;iicexp( i^1 exp([ 
2 ;ii)^ + i)^2 i;i(1 ^2 i) ^1 ] (10.34)(10.35)
And the trading policy isxt+1;i= (1  (^) i)xt;i+ct;ii exp(exp( (^) i) (^)  i)i


(^264) xtt+1+1 (^375) = (^2641)   0
 i c (^1) iexp(exp( (^) ii) (^)  i)i (^375264) xtt (^375) + (^264) i (^0) t (^375)
10.3.6. Mixing Signals(ti+1) =(i)(ti)+(ti) (10.36)
rtt==Xti+(tit) (10.37)(10.38)
The calculation isEtt+s=Xj wj(j)s(tj)
bt==XX 1 j wjXi^1 =0e i C ^1 (j)i(tj)
10.3.7. Essential Statistics for AR(1) Processesi=0e i C ^10 @Xj wj(j)i(tj)^1 A
The process is described by the equation:xt+1=+xt+At (10.39)


```
Stationary Distributionstationary conditions are. Let the stationary distribution beN(x;x). The
x=(=I x)^0 +xAA^0
Ifuse the identity vec(I is invertible, thenABC) = (x= (C 0
 I A) vec() ^1 B. Regarding the second equation,).
```
vec(vec(xx) = vec() =(= vec(I vec( x) vec(^0 ) + vec()) x 1 ) + vec(AAvec(^0 AA) AA (^0) ) (^0) )
Turnover. The turnover of the process is dened as the vectorTi=E(xt+1Ex;i  (^2) t;ixt;i) 2 T. (10.40)
under the stationary distribution. The denominator is trivial. The numerator isharder. Note thatI)x( I) (^0) +AAxt 0 +1).  xt=+ ( I)xt+AtN(+ ( I)x;( 
Combining ProcessesTi=[+ (. Consider the existence of multiple processes I)x]^2 i+ [([x]^2 i+ [ I)x]xi;i( I)^0 +AA^0 ]i;i (10.41)
The weighted average of the signals with weightsx(ti+1) =(i)+(i)x(ti)+A(iw)i(tiis)xt:=Pix(ti). (10.42)


x(ti+1) =(i)+(i)x(ti)+A(i)(ti) (10.43)
10.4. Further ReadingPapers: [Kolm and Westray, 2021], [Amihud et al., 2012], Velu et al. [2020],Gueant [2016], Webster [2023], Bouchaud et al. [2018], Bacidore [2020] Dimen-
sional analysis: [Bluman and Kumei, 1989, Barenblatt, 2003, Gibbins, 2011,Mahajan, 2014]


# Chapter 11Hedging

## Hedging is the process of reducing the risk of a portfolio by means of aug-menting the portfolio with additional investments, whose returns are negativelycorrelated to the existing portfolio. The most common forms of hedging are

## market hedging and currency hedging, but there are at least three additionalcases of practical relevance to portfolio managers. The rst is hedging to factor-mimicking portfolios obtained from a fundamental factor model. The second one

## is hedging to a future or liquid asset capturing non-equity risk. This includesenergy and interest rate futures, and liquid ETFs and ETN describing sector orstyle risk. The last application of interest is the production of thematic tradable

## baskets by banks. One can buy these baskets to hedge or speculate on politicalrisk (e.g., elections) or thematic risks (e.g., Citi has a global thematic enginewith 80+ industry trends).

## vanilla hedging. There are no villains in this story{no transaction costs, noparameter uncertainty, and a single period. Yet, such a simple model is stillThe chapter is broadly organized in three parts. The rst one is covers

## widely used in a wide range of applications. In the second section we explorethe impact of parameter error and how it aects optimal hedging. Lastly, welook at multi-period hedging in the presence of execution costs.


```
11.1. Toy StoryIn its simplest form, we have the following ingredients:
We make investment decisions atWe have two decision epochsWe have two assets, which we denotet 0 ;tt 10 , and one realized return between them., and observe realized returns atcoreandhedgewith expected returnst 1.
```
We decide the size of the hedging instrument in order to maximize the SharpeThe rst asset is the core portfolio , the second one is the hedging portfolio.c;h= 0, volatilitiesc;h, and return correlation between the two is.
Ratio of the combined portfolio. You already see how similar this problem isto the two-asset Mean-Variance Optimization instance we saw in Section 9.1.In that problem, we decided the optimal positions of both assets; not a major

dierence. The MVO optimization problemxmaxh 2 Rcxc  2 ( (^2) cx (^2) c+ (^2) hx (^2) h+ 2hcxcxh)
has solution x?h= chxc (11.1)
The ratiojx?h=xcjis theoptimal hedge ratioxx?hc= hc= ^ and is equal to the beta of the core(rh;rc) (11.2)
portfolio's return to the hedging portfolio's return.The unhedged variance is (^2) cx (^2) c; after the hedge it is (1  (^2) ) (^2) cx (^2) c. The


improvement in Sharpe Ratio is equal to the improvement in volatility:SR(hedged)SR(native) =p 11   2 (11.3)
The parameter beta is estimated either via time-series regression or by usinga return covariance matrix, such as one supplied by a factor model. Denewc;whthe core and hedge portfolios; the model beta is
From that, formula(11.2)gives the relative size of the hedge, and formula^ (rc;rh) =ww^0 h^0 c^ rrwwhh (11.4)
(11.3) the improvement in Sharpe Ratio from hedging.application involves the use of a single hedging instrument that is very liquidIn their simplicity, Equations (11.1, 11.2, 11.3) are applied widely. A typical
and inexpensive to trade, and whose expected return is negligible comparedto that of the native portfolio. We perform intraday or end-of-day hedging inorder to remove the associated risk.
Procedure 11.1:1. Inputs: core portfolio NMVSimple Single-Asset Hedgingxcwith returnsrc. Hedging asset with

2. returnregression, or of an asset covariance matrix.Outputrh: Hedge NMV. Parameter^ x(?hrh=;r c), obtained by means of time-series (rh;rc)xc.
sumptions:Hedging in this specic instance rests on several implicit and explicit as-


 We assume that the beta of the core portfolio to the hedging instrument canbe estimated accurately;We assume that there is a single trading instrument;

In the remainder of this chapter we reexamine these hypotheses and relax them. We assume that the trading costs are negligible;We assume that the hedging instrument has negligible expected return.
11.2. Factor Hedging11.2.1. The General Case
Factor models have made their appearance repeatedly in this book, and unsur-prisingly they matter for hedging as well. In principle, portfolio constructionshould take into account predicted risk arising from factor exposures and from
idiosyncratic bets, and generate a portfolio that meets our investment goals.In practice, there are situations in which this is not possible. An example isthe one in which the core portfolio is the outcome of a portfolio construction
process outside of our control. For example, we may have several groups ofindependent discretionary portfolio managers trading stocks based on theirfundamental outlook. The sum of their individual portfolios constitutes a core
portfolio that is not optimized, and that exhibits undesired systematic risk. Inthis case, the hedging process takesunwanted risk from factor exposures 1 w. We dened factor-mimicking portfolioscas an input, and seeks to reduce the

in Chapter 8, Equationnegligible (^1) We are assuming, again, that the returns of the factors we want to hedge are zero, or(8.12): they are the columns of matrixP, and have


unit exposure to factorWe have achieved zero factor exposure. The solution is simple, elegant, andi. One way to do so would be Procedure 11.2.

Procedure 11.2:1. Compute the core portfolio factor exposureA Simple Factor Hedging Procedurebc=B (^0) wc.

2. \Trade out" the core exposure by buying an amount of factorexposure bc. We do this by buying a hedge portfolio Pbc.
unfortunately unrealistic. We have ignored two essential aspects of the hedgingproblem. First, factors have non-zero expected returns. Second, trading factoris expensive. However, we can change the formulation to include these mod-
eling concerns. Let us begin with accounting the non-zero expected return ofthe hedging portfolio. To this end, we need to go back to Section 3.3, whichintroduced the denition of alpha orthogonal and alpha spanned. In formulas:

the expected return of a portfolioexecution costs, we can include them in the optimization formulation, using asquare root impact model, or a quadratic model, as seen in Chapter 10. Wewis equal to ( (^0) ?+^0 B^0 )w. Regarding the
denote the expected trading cost of a portfoliowbyf(w). In a single-period


setting, we can then write the problem asmax (^0) ?(wc+wh) + (^0) b  (^12) (f (^2) +i (^2) ) f(wh wh; 0 ) (11.5)
s:t:bfi 22 === (Bbw^0 ( 0
 wcf+cb+wwh)h 0
 )(wc+wh)
I leave it as an exercise to prove that if execution costs are zero, orthogonalwh^2 Rn
and spanned alphas are zero, and factor portfolio have zero idiosyncraticvariance, thenassumption holds, and it's worth spending some time commenting on them.of coursewe would hedge out exposure. Not a single one of these
 Some of the factors do have zero expected returnsthem can in fact be counterproductive because the gain in Sharpe Ratio arecountered by expected PnL losses.^2 , some don't. Hedging
 The hedging portfolio may also have non-zero alpha orthogonal exposure.This must be taken into account, especially when alpha orthogonal is indeedwhat the protability of the strategy depends on it, more than on alpha
 spanned.Even if we traded the pure factor-mimicking portfolios of Procedure 11.2, wewould add idiosyncratic risk to our core portfolio. This additional idiosyncratic
risk reduces the benets of factor risk reduction. The optimization formulationtakes this into account. In fact, the following Exercise asks you to work out 2
holding their associated risk.Sometimes these are referred to asunpriced factors, because we receive no reward for


the details and to show that the optimal hedging is not equal toExercise 11.1: (35) Assume that:  bc.

1. factor portfolios have zero expected returns;2. we hedge only using factor portfolios;3. we have no transaction costs.

Prove that the optimal hedging policy isx?= ( (^) f+ (B 0
   (^1) B)  (^1) )  (^1) (B 0
   (^1) B)  (^1) bc
Under what condition is the optimal hedging smaller than perfect factor= [I+ (B^0  ^1 B)^ f] ^1 bc
neutralization of Procedure 11.2?The solution is the Appendix. Meanwhile, here is a much easier problem to
get you started:Exercise 11.2: (10) For simplicity, consider the case where asset returns
are described by one-factor model, and that there is a hedging portfolio thathas exposure to that factor. Starting with Equationoptimal not to hedge entirely the exposure of the core portfolio to that factor.(11.4), show that it is
 In the simplistic hedging procedures of the rst part of this chapter, wecould ignore our investment objective, because volatility reduction was azero-cost improvement: no execution concerns, no expected factor returns, no
idiosyncratic volatility increase. But reality is complicated. The parameterquanties our risk tolerance and determines where do we want to be on thecurve trading o volatility for expected costs.This is a good thing. In practice,


```
 we should explore this trade-o and determine the optimal operating point.In the special case of quadratic costs, Optimization Problembe rewritten as a multi-period optimization problem and solved using the(11.5)can
techniques presented in Chapter 10 and specically in Procedure 10.1. Thisis the subject of the following...
Exercise 11.3:multiperiod setting. Discuss implementation complexity and propose somesimplifying assumptions.(35) Extend Problem Optimization Problem(11.5)to the
```
11.3. Hedging Tradable Factors with Time-Series Betas
A relatively common use case for hedging is the following. We have somenon-equity tradable and liquid instrument that is associated to macroeconomicmovements; for example, energy or metal commodity futures; or xed income
futures. Because of their ability to capture broad macroeconomic themes andof their liquidity, we would like to use these instruments for hedging. To x ourideas further, consider the case of a portfolio composed of energy stocks, and of
gas and crude future contracts, which are among the most liquid in the world.It stands to reason that the energy portfolio is correlated to energy prices, andat the same time that the portfolio manager or the trading algorithm does not

have a view on the future price energy movements. A possible approach is toestimate time-series betasusing Procedure 11.1. Would this approach work? Surprisingly, in more than ^i:= (ri;rh), and then hedge the exposure ^ (^0) wc
one instance, the realized risk of thehedged 366 portfolio is worse than the realized


risk of the core portfolio? This is somewhat counterintuitive. In this section,we try to shed some light on hedging for this particular scenario.As in the previous sections, we denote the return of the tradable instrument

rwithwithh, with variance the random vector of estimation error with covariance matrixthe vector of true betas. In order to see what could go wrong, let ush^2. We model the estimated betas as ^i= (^) i+i. We denote (^) , and
hedge with the \optimal" hedge ratioaugmented with the hedging instrument, is: 0 x?h =  ^^0 w. The covariance matrix,
B@^2 h r 0 ^2 h (^2) h^1 CA
var(r^0 w+rhxh)^2 ===EEw 0
 Ewrw( 0
 r ^0 wrw(+ hr h 20 xw?h (^2) h)) 22 wj+(]  (^2) h w 0  ) (^0) ww+ (h(  ) (^0) w) 2 
The variance of the hedged portfolio exceeds the unhedged variance whenwerror of the portfolio's beta. The right-hand side is the portfolio beta-related (^0) w>( 0 w) (^2). The left-hand side of the inequality is the squared estimation
variance.hedging level that improves on both. We consider the case where we apply aBetween the non-hedged and the fully-hedged portfolio, maybe there is a
positiveestimate the variance of (hedging shrinkage factorr (^0) w+xyhhrhto the optimal hedging:) (^2) , and then we minimize it with respectxh= yh ^^0 w. We


toE(yr 0. The calculation is similar to the one we performed above:w+rhxh) (^2) =EE(r (^0) w+rhx?h) (^2) j]=w (^0) rw yh( 0 w) (^2)  (^2) h+y (^2) hh (^2) w (^0) w
From which y?h=1 w(w (^0
0) ^)w 2 (11.6)
Let's sense-check this formula:x?h= ^ ^^0 w+ww^0
0 ^w (11.7)
 The shrinkage factormeasure the portfolio in cents or in dollar, we get the same value ofOtherwise stated: if we hedge a portfolio 10 times the size of our current one,y?his independent of the units of the portfolio. If weyh?.
 the fraction is unchanged, and the best hedge is 10 times the hedge of theoriginal portfolio.If there are no estimation errors in the betas, then (^) = 0 andy?h= 1: we
 use the optimal hedge ratio.The numerator is a weighted sum of the estimation errors. The larger theerror, the smaller the shrinkage factor.
 The ratio in Equationaggregate noise-to-signal ratio of the betas. The higher the ratio, the smallerthe scaling factor. (11.6)can be loosely interpreted as the square of the
 Consider the edge case where the true betas are all zero and errors areindependent. Then 3 ^=and the expected value (^3) of the denominator is
small, so that the expected value is a good proxy for (Informally, if the number of assets is large, we should expect the variance of ( 368 w^0 ^ )^2. w^0 ^)^2 to be


Eandaction.[(wy^0 h (^) ?^)= 1. On average, we do not hedge, which is the correct course of^2 ] =w^0 w. In expectation, numerator and denominator are equal,
In practice, we recommend the following steps:1. Estimate the time-seriesdiagonal matrix whoseith term is ^iand its standard errori (^2). i. Dene (^) as the
2. Compute3. Buyat zero is meant to avoid the situation where we hedge in the oppositex?h=y ?h(using Formula (11.6).y?h)+( ^ (^0) w) of the hedging instrument. The lower bound

4. (optional). It is dicult to estimate the correlations between estimationdirection.errors, especially in periods of market stress. You can simulate their impact
    by assuming constant correlations between them and then dening

(^) =^0 BBBBBBB@::: ::: ::: :::::: ::: ::: ^012 ^022 ::: :::::: :::n 2 1 CCCCCCCA^0 BBBBBBB@::: ::: ::: :::^1  ::: ::: ::: ^1 :::  1 1 CCCCCCCA^0 BBBBBBB@::: ::: ::: :::::: ::: ::: ^012 ^022 ::: :::::: :::n 2 1 CCCCCCCA

5. and testing the sensitivity for dierent values ofdecreases linearly as(simplifying Formulas (11.6, 11.7)). Assume that the termsincreases. . The hedging ratiow^2 i are uncor-


related withw (^0) wi^2 =. ThenXi w^42 ii 2
==k^1 nwXki (^2) Ew^(^2 iX 2 i)i^2 +ncov((w^21 ;:::;w^2 n);( 12 ;:::;n^2 ))
An analogous simplication occurs for the denominator. Then the formulafor the optimal hedge ratio becomes
Higher standard errorsiyimply greater shrinkage. Lower dollar exposure?= 1 E^((^ ^^20 )wk)w^2 k^2 (11.8)
to the tradable factor also means greater shrinkage. Finally, to simplifythings dramatically, consider the case where allportfolio is long only. The shrinkage factor simplies further: ^iare identical, and the
The ratioHy?h(w= 1) := k(squared noise-to-signal)wk^22 |^= k^2 wE{z^k(^21 is a measure of portfolio concentration^2 }) (portfolio concentration)H|{z(w})^5.
A portfolio that has maximum diversication hasNMV, and hashas all NMV concentrated in a single stock, so thatH(w) = 1=n, while a maximally concentrated portfolionpositions with identicalH(w) = 1. The
sum to one:xi:=^45 For a vectorThe Herndahl Index is usually dened for a set ofjyij=PjHjy:=jxj, deneand applying the original denition..Pix^2 i. It can be extended to arbitrary sets of numbersE^(x) the average of the valuesx^1 n;:::;xnonnegative numbersn. yi, by deningxithat


interpretation here is that the shrinkage factor is small when the portfoliois more concentrated. The intuition is that the estimation error of thebeta averages out more in diversied portfolios.

11.4. Factor-Mimicking Portfolios of TimeSeries
A problem related to hedging a portfolio using a tradable security is that oftrading a portfolio that is close to aabound in real life. A quantitative portfolio manager may be interested innon-tradablesecurity. Such time series
trading them for a few reasons. First, the time series may show high correlationto the securities in her investment universe; and therefore the time series couldserve as a useful hedging instrument. Another use case is that of the macro-
economic systematic investortheme. Developing a tradable portfolio that \tracks" the time has real valuefor her. Lastly, just verifying how well can we track a time series is interesting^6 who has some well-informed reason to trade a
in itself. It shows us whether the time series is of concrete use. Only that thatcan be traded exists. The occasional analysts that hawk non-tradable themesare full of sound and fury, usually signifying sell-side research fees.
haveoriginal subscript, since subscripts should not be multiplied beyond necessity.We introduce the ingredients for our problem earlier in the chapters. Wenassets with returnsri, and a time-series with returnrh; we keep the

In its simplest form, we have the following ingredients:its members in the wild. (^6) A species who I have ignored in this book, because I have not been lucky enough to meet


 We have two periods and one realized return. Investment decisions are madein period one, prots are realized in period two.There arenassets with returnsri, with covariance matrix (^) r.
The problem asks to minimize the tracking error between the time series and There areE(i^2 ) =i^2 n. We denoteloadings^ ^i= ^ := diagi+iwhere ^12 ;:::;iis the estimation error ofn^2 .^ i, with
a portfolio:chapter. minwE[(r^0 w rh)^2 ]. We condition on, as we did earlier in the
E[(r^0 w rh)^2 ] ==EE+w[EE 0 [(( [(rr (^) w^0 w    2 )rh (^2) hh)](+ 2 + var( ) (^0) w) (^0) w r^0 wr+h)] h 22 r]h)j]
==w^2 h 0 (( (^0) rw+ 1) (^2) h ^2 ++ (^2) h^2 h w^0  w (^0) )w+ w2(^0  (^2) hrw+  (^2) h (^2) ) ^2 h (^0) w (^0) +w+ (^2) h+h^2  (^2) h
And the rst-order condition on this unconstrained problem gives the optimalportfolio, which we transform by means of the Woodbury-Sherman-Morrisonlemma of the inverse matrix; see Equation (??):
w?=(=(^2 h (^2) h++hh^22 )() (^) 1 +r+ h^2 h  (^2) ++ (^0) (  0 r^2 h( (^) +r^0 +) (^2) h  ^1 ) (^2) h   (^1) )  1 !( (^) r+ (^2) h )  (^1)
Having done most of the heavy listing, we close with a few remarks: The beta estimation errorThe larger the expected returns, the higher the important of the regularization serves as a regularizer for the covariance matrix.
term. 372


 Whenportfolio isvariance portfolio. A minor point: it seems that the scaling factor in = 0 (no estimation error), andw?= (^2) h  r (^1) , which is, up to a scaling factor, the minimum-h= 0 (zero return), the optimal (^2) h,
 which would make no sense. The covariance matrix does containso that dependency is eectively linear.Whenjhj!1, the optimal portfolio approaches, up to a constant,h, though,  ^1.
 Once we have the optimal portfoliosense that we can employ Equation(11.4)w?, hedging is straightforward, in theto reduce the core portfolio's risk.
(or a FMP of a time series) on top of equity FMPs for a preexisting model(Hint: orthogonalization).Exercise 11.4: 15 Describe how you would hedge to a time-series factor
Proof.11.5.the denition of[Proof of Exercise 11.1] We replace the decision variable?AppendixP, it follows thatB (^0) Px=x, andx (^0) P (^0) Px=xw (^0) (hB= 0
 Px  (^1) B. From)  (^1) x.
It follows that the optimization problem (11.5) can be rewrittenmax (^0) ?(wc+wh)  (^12) ( (^2) f+ (^2) i) f(wh wh; 0 )
s:t:b (^2) f (^2) i===bxc (^02) + (^) ;cfx+xx (^0) (B 0
   (^1) B)  (^1) x+b (^0) c(B 0
   (^1) B)  (^1) x+w (^0) c (^) y
Assume thatwyh= 0,^2 Rn= 0 and transaction costs equal to 0. The objective


function becomes (^0) ?wc  (^12) (x (^0) fx+ (^2) ;c+x (^0) (B 0
   (^1) B)  (^1) x+b (^0) c(B 0
   (^1) B)  (^1) x)
which is minimized at ^12 [x^0 (^ f+ (B^0  ^1 B) ^1 )x+b^0 c(B^0  ^1 B) ^1 x]
x?==  ([I (^) + (f+ (B 0 B 
0   
1  B^1 )B )f ]^1  ) 1  b^1 c(B^0  ^1 B) ^1 bc


# After the TradePart III



# Chapter 12Dynamic Risk Allocation

## So far we have focused exclusively on single-period portfolio optimization.This may be appropriate for one-o investment decisions, but is inadequatefor long-term investment strategies. There is a rich academic literature on

## inter-temporal choice theory, which aims at modeling the interplay betweenconsumption and investment in the long run, both at the level of the individualconsumer and at the aggregate level. Much of the literature has been ignored by

## asset managers for their investment decisions, for reasons we conjecture below.First, these models require the specication of a principled utility function andof an inter-temporal tradeo (in the form of a discount factor for future utility),

## something that no investment manager would or could specify. If quadraticutility had been the main justication of mean-variance optimization, it wouldprobably have never been adopted. Secondly, these models don't capture well

## the institutional setting of asset managers. \Consumption" for asset managerscorresponds to out
ows, and asset managers don't receive any utility from it.Moreover, out
ows do not bear a direct relationship to the principals' utilities

## (i.e., those who provide the investment capital to the managers). The reasonfor this is that in
ows and out
ows occur at low rates (they are \sticky"), dueto inertia of the principals (who resist changing their asset allocations) and

## to contractual obligations with the asset managers (who require long advance 377


notice for capital withdrawal).driving their Ferraris (don't read and drive), they still have to make decisionsEven if hedge fund managers do not read the academic literature while
about the risk they want to take the next day, week, and month. There isone line of research, initiated by electrical engineers and mostly developedby researchers not employed by Economics departments, that is relevant to
investors. It is broadly known asGrowth Investing. It has both descriptive power, since it is followed by manysuccessful investors, and prescriptive value, in that it is based on rst principlesKelly Criterion, Kelly Investing, or Optimal
and has attractive properties. The rest of this chapter is devoted to presentingthe basics of the theory. We start with a description and motivation of theKelly Criterion. Then we link it to the familiar concepts of Mean-Variance
Optimization and Sharpe Ratio. The way that vodka is not suitable as a dinnerdrink, \Pure" Kelly is not suitable for investing.what Chardonnay is to Vodka: more sustainable, better tasting, and ultimatelyFractional Kellyis to Kelly
more fun. Finally, we introduce a time-varying of Fractional Kelly, which helpsmanage the occurrence of drawdowns.
12.1. The Kelly CriterionOne line of research in multi-period investing has been relevant to practitioners.It takes various names: Kelly gambling, Optimal Growth Portfolios, or Universal
Portfolios. To introduce the concept, we consider rst a very simple example.You have one risky asset in which to invest, which returns +100% or -50% withequal probability. The single-period expected return of the asset is 5=4, and its
volatility is 3=4. You have to decide how to invest your initial capital in this 378


asset. Consider two alternatives:1. (Constant Capital Allocation)of capital to the risky asset. This approach is consistent with solving aEvery day you allocate the same amount
mean-variance optimization problem in each period. The problem facedin every period is
wherewis the net amount allocated to the risky asset and is independentmaxw^54 w ^2169 w^2 )w=^920  (12.1)

2. of the period.(Static Allocation)the risky asset, and then you let it run. This is consistent with solving aOn day 0, you allocate a fractionxof your capital to
3.on that daymean-variance optimization in period 0, and letting it run.(Dynamic Allocation)to the risky asset. We have no motivation for this (yet). TheEvery day, you allocate a fractionxof your capital
    intuition however is it seems reasonable to have a volatility proportionalto the available capital in each period. The ratio of the strategy's volatilityto capital in each period is equal to 3x=4 and is indeed constant in this
The chart below shows the cumulative returns under the three approaches. Theconstant capital allocation shows low growth. Independently ofapproach. x, the static allo-
cation has poor performance, even though the risky asset has positive expectedreturn. Conversely, the dynamic allocation exhibits a variety of behaviors. Itsgrowth rate (equal to the slope of the curve) is not monotonically increasing
withreturns are low. The most protable strategy corresponds tox. Risk-adjusted performance is good for low values ofx, but the averagex= 1=2. Higher


```
constant capital dynamic static
1e+01 0 500 1000 1500 2000 0 500 1000 1500 2000 0 500 1000 1500 2000
1e+161e+31
```
```
1e+46
Day
```
Cumulative Return

fraction (^0) 0.10.20.30.40.5
0.60.70.80.9 1
Figure 12.1:curves are based on the same realization of returns of the risky asset. The returns areplotted on a logarithmic scale.Cumulative returns under the dynamic and static policies. All the same
values detract from performance.Ratio is identical and equal to 1What is remarkable is that, for each strategy, and for each period, the Sharpe=3, because in each period the portfolio, being
the combination of a free-risk asset and a risky asset, is mean-variance ecient.This numerical example should warn about the subtleties of using the SharpeRatio as a performance measure. We have been able to compute the Sharpe
Ratio exactly, thus abstracting away any complication due to performancemeasurement; and we obtained the same value for all the strategies in ourexample. Yet, the behavior of the cumulative returns diers wildly among the
strategies! We can interpret this as follows: the single-period Sharpe Ratio,dened as expected mean return/standard deviation in a single period, is ameasure ofinvestor skill, but not ofstrategy performance. Averaging the Sharpe
Ratio over the life of a strategy can give us a better estimate of skill, but isnot telling us much about the risk-adjusted performance of the strategy over


its lifetime. If we chose the cumulative returns over the strategy lifetime as ametric { and ignored any drawdown concern { then the dynamic strategy withx= 1=2 would be the clear favorite.
high-Sharpe portfolio in any given period, is necessary but not sucient to bea successful investor. The size of the overall portfolio over time plays a majorA second observation is that skill alone, dened as the ability to select a
role in the long term. Yet, this topic does not receive much attention amongacademics nor practitioners.To understand where the valuex= 1=2 comes from, letrt(x) be the random

return of the dynamic allocation strategy in period1 +rt(x) = (^8) >>< t. It is
The total return of the strategy isQ>>:1 +^1 Tt=1 rx px=t(x^2 ). The average growth rate of thep= 1= 1==^22 (12.2)
strategygT(x) is such thatYT
wheret=1gTrt((xx) :=) = exp(T^1 XtT=1Tglog(1 +T(x)) rt(x))
For a xed number of periodsgrowth rate of the strategy, we would solve the problemT! 1, because returns are iid rvs, by the law of large numbers,T, if we wanted to maximize the expectedmaxxgTg(Tx(). Forx)!
E[log(1 +r 1 (x))] a.s. The solution to the problemmaxx E[log(1 +r 1 (x))] (12.3)


```
is asymptotically equivalent to maximizing the expectation(12.3). The objective
−0.040.00
```
```
0.04
0.00 0.25 0.50 x 0.75 1.00 1.25
```
E(log(r)]
Figure 12.2:maximized atxExpected value of the log of the single-period growth, which is?= 1=2.
12.2).function is maximized when the investment fractionFrom Fig. 12.1, it appears that this strategy performs decidedly worsexis equal to 1=2 (see Figure
than other strategies with lower investment fractions. By simulation (or fromFigure 12.2) one can see that strategy in whichcorresponds to borrowing money to invest in the risky asset. Summing up, itx >1 performs even worse; this
appears that long-term returns are maximized not by maximizing the expectedreturns, but by maximizing the expected growth rate, which is mathematicallyequivalent to maximizing an expected utility, with a logarithmic utility function.
These strategies go under dierent names: Kelly strategies, optimal growthstrategies, Kelly strategies, and universal strategies.Let's work out in detail an important example.


```
only two assets: a risk-free asset and a risky asset. Let the excess return of therisky asset beExample 12.1r. One way to interpret this asset in real-world application is as a(The Kelly allocation to a single security): We have
the expected growth of the portfolio, then we would solve the problemportfolio manager to which we need to allocate capital. If we were to maximize
In addition to an exact numerical solution, we also produce an approximatemaxx g(x) := maxx E[log (1 +rx)] (12.4)
```
solution based on the quadratic approximation of the logarithm:log(1 +x) =x x 22 +o(x (^3) ) (12.5)
Then a quadratic approximation ismaxx E[log (1 +rx)]'maxx x  (^12) ( (^2) + (^2) )x (^2) (12.6)
and a further approximation, in which we assumemaxx E[log (1 +rx)]'maxx x  12  2 x, is (^2) (12.7)


from which (exact result): (^8) >><
(quadratic approximation):>>:^8 >><xg(?x= arg max?) =E[log (1 +xE[log (1 +rx?)] rx)] (12.8)
(assuming that):>>:^8 >><xg(?^1 x'?^1 )'^2 +^12 SRSR^22 +1^2 (12.9)
This approximate result is reliable when the typical 
uctuations of>>:xg(?^2 x'?^2 )SR'^12 SR^2 (12.10)xrare
smaller than 1. A heuristic is to require that the volatility ofthan 1:Let us consider in some more detail the accuracy of the approximationsjxj1, i.e.,jSRj1. xrbe smallerx? 1 ;x? 2.
We consider daily Gaussian returns. The approximationerrorRatio of 4). The approximationjx? 1  x?j=x?2%) for daily Sharpe Ratios up to 0x? 2 is accurate (relative errorx:24 (annualized Sharpe? 1 is accurate (relativejx? 2  x?j=x?2%)
for daily Sharpe Ratios up to 0The crucial assumption in these calculations is the rebalancing interval. If werebalance at shorter horizons, the volatility of returns in that horizon is smaller,:15 (annualized Sharpe Ratios up to 2.4).
and the quadratic approximation is more accurate. If we rebalanced capital atshorter horizons than daily, the approximation would hold for higher values ofthe annualized Sharpe Ratio.
volatility and capital is equal to the Sharpe RatioAnother way to read this result is thatthe optimal ration between dollar. The capital deployed isW 0 x?.


Hence the (dollar volatility)/(capital) ratio is(dollar volatility)(capital) =(WW 0 x 0? 2 )= SR (12.11)
Note that the formulas above hold for volatilities and Sharpe Ratio measuredat the same timescale. For example: if we deploy $1B of capital, and have anannualized Sharpe Ratio of 2, then we should deploy approximately $2B of
dollar volatility to run a Kelly-optimal strategy.expected return isAnother observation: according to Equation(12.11), the Kelly-optimal
(expected strategy return)= SR(dollar volatility)(capital) = SR^2
1e−021e+001e+02

1e+04

Cumulative Return (^19401960) Date 1980 2000 2020
fraction invested0.40.81.21.6 (^2) 2.42.83.2
(^1000200030000)
40005000
Figure 12.3:(a): Time series of cumulative returns for dierent fractions of the(a) Cumulative Return^01 (b)Fraction^234
capital invested in the US market benchmark (cap-weighted average of NYSE, AMEXand NASDAQ-listed companies). Monthly excess returns of the benchmark for theperiod February 1926-March 2018 are from Ken French's data library site. (b):Cumulative returns as a function of the fraction invested in the US market benchmark.
The optimal Kelly fraction under the two approximations (Equations (12.9, 12.10)) isx? 1 = 1:88 andx? 2 = 2:2.
Example 12.2(The Kelly allocation to the US market) 385 : We can spe-


US market benchmark. This asset is available to retail investors in the formcialize the analysis above to the important case in which the risky asset is theof low-management fees mutual funds and ETFs, both of which track the US

market accurately. Futures for the US markets are also available to sophisticatedinvestors. The Sharpe Ratio computed on the returns of the SP500 in excess of3-month Treasury bills is a function of starting and ending dates (^1). We assume a
Sharpe Ratio of 0.42 and an annualized volatility of 19%. Based on the observedrealization of the historical returns, the optimal the total returns are maximizedatx? 1 = 1: 88 (Equation (12.9) andx? 2 = 2: 2 (Equation (12.10). A chart of the
returnsgoal was to maximize our long-term returns, then it would be optimal to leverageour capital. In practice, there are borrowing constraints and the live behavior of^2 of the SP500 is shown in Figure 12.6. This example suggests that, if our
a Kelly strategy has drawbacks: the historical plot shows how a larger fractioninvested results in much more volatile PnL and in larger drawdowns. However,this example illustrates of the invested fraction can have a very dramatic impact
on capital appreciation.The SP500 example shows the attractive features, but also the drawbacks
of Kelly strategies.Example 12.3(Sizing a Bet): We extend the example with which we opened
the chapter. Consider a bet with a binary outcome: if we investpayo equal to 1 rw> 0 with probabilitypand rl< 0 with probability$1, we receive aq= 1 p.
sury returns.SP90 index. 2 A. Damoradan maintains a page (Before January 1957, the SP500 had 90 components. The returns for 1926-1956 use thishttps://tinyurl.com/spdamor) with SP500 and Trea-


The optimization problem ismaxx plog(1 +xrw) +qlog(1 xrl)
)x1 +?pr=xw?rprll  rq^1 w qrxl?rl= 0 (rst-order condition)

Introduce the win-loss ratiox?=rpl 1  (win-loss ratio)p=q, and the winning skew (^1) (winning skew) 1 rw=rl.
The higher the win-loss ratio and the winning-skew, the higher the size of thebet. If both win-loss ratio and winning skew are smaller than one, the optimalsize cannot be positive.
properties of Kelly strategies.The next section is devoted to describing the attractive mathematical
We limit our attention to the case in which we can choose in each period among12.2. Mathematical propertiesa set of strategies , and the associated returnsrt() are independent ofrt (^0) (),
for alland Savage [1965], but some of them have also been established for dependentrandom variables; see Algoet and Cover [1988].t^0 < t. These results were proved rst by Breiman [1961] and Dubins
alternative strategy with lower expected growth rate.1.LetThe rst property is that the Kelly strategy grows faster, than anyXt;Yt be the cumulative returns of the Kelly strategy, and of an


strategy with lower expected growth rate. Letreturns of the Kelly strategy and alternative strategy respectively. Then,with probability 1, Xt;Yt the cumulative

2. The second property characterizes the long-term growth of a strategytlim!1XYtt=^1 (12.12)
    based on the expected value of its log returns. LetX(a)tthe associated cumulative return process. Then, with probability 1g > 0 )Xt!1 g:=E[log(1 +r 1 )] and
3. The expected time to reach capital level(b)(c) g <g= 0^0 ))Xlim supt! 1tXt=^1 ;lim inftXCt=is equal to 1. logC=gin the limit
features. In the long run, it beats almost surely any other strategy that hasWhat these result say is that a Kelly strategy has many very desirableC!1, and it is shortest for the Kelly strategy.
a dierent expected growth rate. It also reaches a certain cumulative returnfaster than any other strategy; and the approximate time needed to reach thisreturn can be expressed as a function ofg. Finally, a positive expected growth

rate is a necessary and sucient condition for any strategy to have a growingcumulative return over timeWhat the resultsdon't say (^3). is that a Kelly Strategy is maximizing the
Sharpe Ratio, even if we were able to compute it exactly from knowledge ofand Part IV of the book MacLean et al. [2010b] for a diversity of views. (^3) There are other properties of the Kelly Strategy. See MacLean et al. [2010a] for a review,


The Kelly criterion for sizing has several intuitive and attractive features:Insight 12.1: Goal: The allocation strategy achieves the highest long-term capitalThe Intuition Behind Kelly Strategies
 growth.Simplicityfraction of total capital to the risky strategy.Lower and Upper Bound on risky allocation: The optimal strategy is simple, since it allocates a constant: the fraction of capital
 allocated to a risky strategy should be high enough to ensure growthg >Sharpe-proportionalcapital invested is proportional to the Sharpe Ratio of the strategy.0, and at most equal to: to a rst approximation, the optimal fraction ofx?.
(capital allocated to strategy)(capital)(dollar volatility)(capital) == SRSR
(expected strategy return)= SR^2
the true expected return and volatility of the strategy. Nor does it guaranteeany lower bound on the maximum drawdowns, which can be severe, as seen inthe simulations above. In example 12.2, the fractionxinvested increases from
0 to the growth-maximizing leveldrawdowns increase withof the returns is therefore proportional to the drawdown percentage. Abovex. The scale of the y axis is logarithmic. The excursionx, both the growth rate and the size of the
the optimal level, the growth rate diminishes (as expected) and the drawdownsincrease further. For fractions of the invested wealth lower thantrade-o between expected log returns and volatility of the log returns: we getx, there is a
lower returns, in exchange for lower risk. We explore this trade-o next.


12.3. The Fractional Kelly StrategyTherta fractionfractional Kelly strategyx?fracof the available capital smaller thanconsists of investing in a strategy with iid returnx?, but still such that
E[log(1 +Combination of risk-free asset and full Kellytion of two investments: a risk-free asset, and the full Kelly strategy. Ther 1 x?frac)]>1. If can be interpreted in several ways:. Fractional Kelly is combina-
percentage volatility of the strategy ispursued by MacLean et al. [1992]. They show [MacLean et al., 2004, 2010a]that the fractional Kelly strategy does indeed trade o growth for security.x?frac. This is the line of analysis
Assume, for example, that in each period we cannot tolerate a percentagevolatility greater than some valuedrawdown per period that we can accept. From Equationp. This threshold is related to the maximum(12.11),xp.
We choose the minimum of theExample 12.4: We deploy$1B of capital, and have a Sharpe Ratio of 2.x?= minfp=;SRg.
The strategy has a percentage volatility of 5%. We can lose at most 1% of ourcapital in a week. Say thati.e., 3 (weekly dollar volatility)= 0: 01 (capital),
So thatp== 0: 11 p. This is smaller than the weekly Sharpe Ratio=(weekly dollar volatility)(capital) = 0:^01 =^32 =p 52 u
^0 Higher risk aversion:^27 , which corresponds to the optimal Kelly fraction.. We start from Equation(12.6), which approximates the
log objective function with a linear-quadratic one. We modify the approximate


objective function by overweighting the quadratic penalty:maxx x  2 ( (^2) + (^2) )x (^2) ;  > 1
The optimization point is x?frac=x?
 Fractional Kelly is then a modied Kelly strategy for investors who are morerisk-averse than logarithmic utility would suggestParameter uncertainty. Thorp [2006] makes the case that uncertainty about^4.
the properties of returns should result in fractional Kelly. Indeed, being wrongcan have terrible consequences. Imagine, for example, that we have a strategywith a volatility of 19%, and an estimate of Sharpe Ratio equal to 0.84 the
realized Sharpe Ratio is 0.42. The Kelly fraction is 4.4. We over-leverage thestrategy and go bankrupt (see Figure 12.6, bottom panel, for a historicalsimulation based on the returns of the Market).
We have introduced parameter uncertainty already in Section 9.2.2, in thecontext of mean-variance optimization. An argument for this approach is thefollowing. We model parameter uncertainty as follows. Per-period returns
aresample in the probability space 
random parameter taking values in a set , with probability measurert=r(!t;t), wherertis a function of two iid random variablest, with probability measureP!) and!t(thetP(a).
u(xThe interpretation is that in every period we have a noisy estimate of the^4 )The relationship between this mean-variance approximation and power utility function/u^ , for
 >0, is explored by Pulley [1981].


```
true parameter:=gTE(x) :=(t).The log total return isT 1 XT
g(x) := lim=ET!1!;t=1[log(1 +glog(1 +T(x) xrxr(!;(!t;))]t)) a:s:
The expectation is taken with respect to the random variablesP. We want to maximizeg(x). The rst-order condition is!g 0 (xP) = 0:!and
g(x?uncertg^0 (x) =) =0E!E1 +r(xr!;(!;) )
As a function ofr, the functionh(r) :=r=(1 +xr) is strictly convex. By
```
Figure 12.4:always smaller than the optimal size when parameters are known.The optimal Kelly size in the presence of parameter uncertainty is
Jensen's inequality, E1 +r(xr!;(!;) )<1 +r(xr!;(!;))


And therefore, taking expectations overg (^0) (x) =E!E1 +r(xr!;(!;) )< E!!,1 +r(xr!;(!;))=:g 0 (x)
The function on the left-hand side is the derivative of the expected log returnin the presence of parameter uncertainty. The function on the right-hand sideis the derivative of the expected log return when the parameter is known. It
Let us consider two examples that have some general application: uncertaintyfollows thattwo solutions.x?uncertx?. Figure 12.4 visually illustrates the location of the
about a strategy's expected return and about its variance.Example 12.5(Strategy with uncertain expected return): Letr=+
E(, where) =and varis a rv with zero mean and unit variance, and() = (^2). We assume thatandare independent.is random, with
so that the Kelly fraction isE[log(1 +rx)]'x ^12 (^2 +^2 +^2 )x^2
Let us use the SP500 rough market estimates from previous examples:x?^1 '^2 +^2 +^2
of 1.88 in the absence of estimation error.= 0:^19 ,= 0:^08 , and a= 0:^04. We getx?^1 = 1:^81 , compared to an estimate
whereExample 12.6 > 0 and(Strategy with uncertain volatility);are rvs mean zero and unit variance. We assume that 393 : Letr=+(+),


andare independent.E[log(1 +rx)]'x  (^12) [ (^2) +E((+) (^2)  (^2) )]x 2
so that the Kelly fraction is again=x ^12 (^2 +^2 +^2 )x^2
Let us use the SP500 rough market estimates from previous examples:x?^1 '^2 +^2 +^2
compared to an estimate of 1.52 in the absence of estimation error.= 0:^19 ,= 0:^08 , and= 0:^1 for the market return. We getx?^1 = 1:^81 ,
All reasonable investors allocate capital to a risky strategy so that thevolatility/capital ratio is constant, or slowly varying. This is in line withInsight 12.2:All Reasonable Investors use Fractional Kelly, Without Knowing
(Part VI of MacLean et al. [2010b] collects the contributions on thiswords, they want to allocated as much capital as it's possible, compatiblywith the drawdowns that their investors can bear. In a series of papersthe rst justication we gave to fractional Kelly strategies. In other
subject) Ziemba and coauthors provide anecdotal evidence that successfulinvestors follow Kelly allocations. The likely reason is not that investorsare aware of the Kelly criterion, but rather that they use the simpleconstant vol/capital heuristic, which turns out to be equal to Fractional
Kelly.


```
12.4. Fractional Kelly and Drawdown Con-trol
In an in
uential paper, Grossman and Zhou [1993] address a question related tothat of identifying a growth-optimal strategy and of constrained growth-optimaloptimization. In the optimization problem, the constraint was on the volatility
of log returns, and implicitly on the probability of drawdown; in the Grossman-Zhou formualtion, the investor wants to maximize the long-term growth andwith probability one avoid reaching a drawdown threshold. As formulated in
```
high watermarktheir original paper, the model only consider a risk-free asset and a risky onewith meanand volatilityasMt=max. In order to formulate the policy we dene thefWs:t 2 [0;t]g. Letdtthe current percentage
drawdown from the high watermarkdrawdown berisky asset and is given byD. The optimal policy gives the optimal fraction invested in thedt= 1 Wt=Mt. Let the maximum allowed
This policy is elegant and intuitive. For some intuition, x rst,ft=^2 ^1  ^11   Ddt D= 1; i.e.,(12.13)

we can tolerate innite drawdown. Then the strategy is the one we identiedin Eq.12.6: invest a xed fractionstrategy is to invest a fractionxDxwhen we are at the high watermark== (^2). If 0< D <1, then the optimaldt= 0.
This means that we are more prudent than in the simple Kelly scenario, andwe are more prudent if our threshold is conservative. Moreover, we decrease theinvested fraction as we approach the drawdown threshold, and we liquidate the
risky asset Figure 12.5 shows the optimal fraction as a function of the threshold. 395


05

1015

20

% of ideal Kelly investing fraction (^05) drawdown 10 15 20
D (^246810)
(^1214161820)
Figure 12.5:The reduction rate is nearly constant over the range of allowed drawdowns.Reduction factor 1 (1 D)=(1 dt), for various values ofDanddt.
To understand the trade-os between optimizing for variance control andoptimizing for drawdown control, it is useful to compare the Grossman-Zhouand Fractional Kelly strategies in a numerical examples. Specically, we consider
the case of a risky asset with independent identically distributed returns. Itsexpected daily return is 0.08% and its daily volatility is 1%, corresponding to aSharpe Ratio of 1.27. The two strategies are parametrized by the Kelly fraction
and the drawdown threshold respectively, i.e.ft(p) =p (^2) (Fractional Kelly) (12.14)
withp 2 (0ft;(D1);D) = 22 (0;^1 1). I then simulate the performance of the two strategies ^11   Ddt (Grossman-Zhou) (12.15)
over a 100-year period (i.e., 25,200 days) and compare the realized volatility andthe maximum drawdown for strategies having the same expected log-return. Fig.


12.6 shows the results. As expected, the fractional Kelly strategy has a betterprole than the Grossman-Zhou in the mean-volatility plane, and a worse onein the mean-maximum drawdown one. In this numerical example, the reduction
in drawdown of Grossman-Zhou seems more more marked than the associatedincrease in volatility. For example, consider a max tolerated drawdown of 30%.Grossman-Zhou achieves an average daily return of approximately 0.09%, while
fractional Kelly achieves an average daily return of 0.075%, a 20% increase.More importantly, Grossman-Zhu controls the maximum drawdownwith probability one and independently of misspecication of the problem. Inex ante,
the mean-variance approach, we can only provide a probabilistic bound onthe drawdown; moreover, if the parameters in the optimization problem areincorrect, this bound will be incorrect as well. These considerations suggest that
the Grossman-Zhou strategy may be preferable. There are a few qualicationsto this statements. First, we have ignored the role played by transaction costs.In Grossman-Zhou, the amount invested 
uctuates heavily over time, since we
may force a complete liquidation of the risky asset when we reach the threshold.This in turn may aect the protability of the strategy and make the approachless attractive. It is beyond the scope of this chapter to extend the analysis to
the case of transaction costs which, in the absence of analytical results, may onlybe tractable with numerical experiments. A second issue with the Grossman-Zhou strategy is that it does not give us the same modeling 
exibility of an
optimization formulation. This book makes the case that additional penaltyterms and constraints are justied by concern with regulatory requirements,duciary mandates, model mis-estimation and many other considerations; all
of which t naturally in the fractional Kelly framework, which can be derivedas the outcome of an optimization. The same constraints and penalties in the


0.000.01

```
0.020.03
0.0000 0.0005E[log(1+r)]0.0010 0.0015
```
std dev[log(r)] strategyFractionalGrossman−Zhou (^2040600)
80
maximum drawdown (%)0.0000 0.0005E[log(1+r)]0.0010 0.0015
strategyFractionalGrossman−Zhou
Figure 12.6:strategies' performance measures are estimated over the same sequence of 25,200Comparison of fractional Kelly and Grossman-Zhou strategies. Both(a) (b)
returns, but with dierent parameterslog-returns vs mean log-return. (b) Maximum drawdown.p,D. (a) Standard Deviation of daily
Grossman-Zhou dynamic problem poses formidable challenges. These objectionsnotwithstanding, Grossman-Zhou is a useful heuristic that can be used as anoverlay to a Kelly-like strategy.


# Chapter 13Ex Post Performance

# Attribution

\After the rain has fallen, we return/ To a plain sense of things". So begins afamous poemthe \rain" is the realized performance of our strategy, and the plain sense of (^1) which describes well the spirit of this chapter. Out of metaphor,

## things is our ability to understand what happened after the fact, namely: Is our performance due to luck or skill?How did we make or lose money? What is the contribution of factor PnL

##  and idiosyncratic PnL?In idiosyncratic space, what drove our PnL? Asset selection or sizing? Therst is being on the right side of a bet; the second one is the ability to size

##  appropriately asset bets that yield higher returns.How can we explain factor PnL concisely and insightfully, i.e., using onlyfactors that are of interest to us?

## Performance attribution oers numerous advantages. First, it provides theportfolio manager with a much-needed reality check. If she lost money, maybeshe can explain the source of the loss, and identify countermeasures to apply

going forward; sometimes the remedies are straightforward and contained in (^1) W. Stevens, \The Plain Sense of Things" in Stevens [1990].


the output of the performance attribution itself. If she made money, maybe shedid so as the result of unintended bets on factors that were not included in thestrategy scope. \The rst principle is that you must not fool yourself{and you
are the easiest person to fool." This statement, made by Richard Feynman inhis 1974 CalTech commencement address, holds true for scientists and tradersalike. Secondly, performance attribution empowers the enables theprincipalto
reward an agent appropriately. The principal may be the hedge fund managerand the agent the portfolio manager, or, descending one step down in thedecision-making hierarchy, the principal may be the portfolio manager, and
the agent may be the analyst who works in the portfolio manager's team.There are other benets. A portfolio manager is bound to use a specic factormodel forex anteportfolio construction. Noex postlimitation exists after the
trade, though: she can look at her performance under the magnifying glass ofdierent risk models. For example, a global risk model, sometimes unsuited forcountry-specic investing, could reveal cross-country exposures. We can use
statistical models in addition to fundamental models.remainder of this chapter is broadly organized in two part. First, we introducePerformance attribution is conceptually simple but it is not trivial. The
time-series performance attributionbased(also known asholdings-based, and review the concept of) dd characteristics-


```
13.1. Performance Attribution: The Ba-sics
Recall the short introduction to performance attribution in Section 3.5.1: thePnL can be decomposed into the sum of factor and idiosyncratic components.The performance decompositionprocessis slightly more involved. Trading time
is not discrete, whereas performance attribution occurs in discrete time. Toreconcile the two views, The time axis is partitioned in intervals delimited byepochsi. Denote thePnLithe PnL in interval [i  1 ;i], andri,fi, andithe
```
total returns, factor returns and idiosyncratic returns respectively. Also, dene,as we have done previously,with the decomposition: bi:=B (^0) wi. Then we can isolate thetrading PnL
PnL ==XX|tt (PnL(PnL{ztt  rrttwwtt}) +) rtwt
The sum of factor and idiosyncratic PnL is sometimes referred to astrading PnL +factor PnL|X|t{zb^0 tf}tposition PnL+idiosyncratic PnL{zX|t{z^0 tw}t } position
PnLwith no transaction costs, so that the PnL is resulting from the application tothe portfolio of the interval's total returns. To x ideas on the interpretation of. This is the PnL we would experience if we could instantaneously trade,
the trading PnL, it is helpful to consider the case of an idealized high-frequencytrader (HFT). Let the epochs be the close of trading days. The high-frequency


trader ends the day 
atPnL is not. It originates from three terms: intraday alpha, i.e. \price discovery";compensation for providing liquidity by submitting limit orders and receiving^2 :wt= 0. The accounting PnL is zero, but the trading
a fraction of the bid-ask spread; and costs incurred by taking liquidity bysubmitting market orders.The factor PnL can be decomposed in separate time series for the contribu-

tion of each factor: Factor PnL =Xjm=1 (^) Xt=1T[bt]j[ft]j! (13.1)
This could be the end of a simple story: take portfolio snapshots at eachepoch, decompose PnL into three terms, and then dive into the contributionof individual factors and of individual securities to idiosyncratic PnL. Reality,
however, is more complex. First, we need to unveil the illusion of certainty thatcomes with the simple decomposition of Equation (13.1).
13.2. Performance Attribution with Er-rors
13.2.1. Two ParadoxesTo motivate the importance of having a more nuanced view of factor-basedperformance attribution we introduce two paradoxical facts about performance
and/or partially hedge it.^2 Non-idealized HFTs do not necessarily close the day 
at, but instead rebalance the book


attribution, both related to factor-mimicking portfolios: (Factor-Mimicking Portfolios have idiosyncratic risk but not PnL.)factor-mimicking portfoliov Each

ancecratic PnL whatsoever. This can be seen intuitively by the fact that the^2 vi:=v^0 i (^) vi. However, the factor-mimicking portfolio has no idiosyn-ihas by necessity a non-zero idiosyncratic vari-
return of the factor is the return of the portfolio itself. More rigorously, letbe the matrix whose columns are the factor-mimicking portfolios, as denedin Equation (8.12). Then their idio PnL is P
and therefore the idio PnL is null. This holds forP^0 =B(B^0  ^1 B) ^1 B^0  ^1 (In B(B^0 all ^1 factor portfolios, includingB) ^1 B^0  ^1 )r= 0
those have an idiosyncratic variance percentage close to 50%, and for allperiods. This is especially concerning given that factor model performance isoften evaluated on factor portfolios.
 (Factor-Neutral Portfolios)factor exposures, i.e.,volatility (^2) w:=w 0
 Bw (^0) w. Now, consider the portfolio= 0. Hence, its entire volatility is its idiosyncraticOn the other side, consider a portfoliow+v, wherewwith novis
a factor-mimicking portfolio andportfolio is the same for any value ofthe idiosyncratic volatility ofw+v (^2) depends on, sinceR. The idiosyncratic PnL of thisvhas no idio PnL. However,, and is equal to (^2) w+
We can make the realized idiosyncratic volatility of the portfolio arbitrarilygenerated by a continuum of portfolios with possibly very dierent volatilities.^2 v^2 + 2w^0 v. Hence we haveexactlythe same sequence of residual PnL
dierent than the predicted idiovol, thus greatly undermining the credibilityof the model. How can this be?


```
One could object that in practice, factor portfolios do not have zero idiosyncraticPnL. This is due primarily to the nonstationarity of the process, so that factorportfolios as of timetare slightly stale when applied to timet+ 1. This criticism
doesn't address the concerns exemplied by the paradoxes for two reasons.First, because even in the ideal case in which the model is stationary, and wehave accurately estimated its parameters, we do have these paradoxes. Secondly,
because the idiosyncratic PnL would be in any event much smaller than whatwould be compatible with the idiosyncratic volatility predicted by the model.In the next three sections I present a possible solution to these paradoxes.
```
The overall take-away in the analysis is that the returns of the factor-mimickingportfolios areportfolios have, according toestimates of the true factor returns from the model. Factorany (^3) factor model, non-zero idiosyncratic volatility,
and they have idiosyncratic returns in addition to their true factor returns. Oncewe account rigorously for the estimation error, the factor PnL and idiosyncraticPnL can be characterized as random variables whose rst and second moments
We then give explanations for the paradoxes.can be obtained from model and portfolio data. The next section lays out somebasic facts about model estimation; the last section derives the main formulas.
13.2.2. Estimating Attribution ErrorsLet us rewrite the attribution equations, but paying attention to the fact thatwe are using factor and idiosyncratic return estimates^ft;^t. We consider the
case of a time-independent factor model, but Recall from Section 6.3.1 that thea dense low-rank matrix and a sparse full-rank one. (^3) By \any", we mean that the return covariance matrix can be decomposed into the sum of


factor returns can be written as^ft=ft+t tN(0;(B 0
   (^1) B)  (^1) )
Analogously, for the idiosyncratic returns, we have^t=rt B^ft
=t Bt BtN(0;B(B^0  ^1 B) ^1 B^0 )
(estimated idiosyncratic PnL)(estimated factor PnL)tt===ww(true factor PnL)^0 t^0 tB^t^ft t+w^0 tBt
w^0 tBt=N(true idiosyncratic PnL)(0;b^0 t(B^0  ^1 B) ^1 bt) t w^0 tBt
When we attribute the PnL over multiple periods, we have(true factor PnL)=(estimated factor PnL) Xt w (^0) tBt
(true idiosyncratic PnL)=(estimated idiosyncratic PnL)+Xt w^0 tBt


```
Finally, this gives us two useful results. First, it provides condence intervalsaround the attributed PnL:
(true idiosyncratic PnL)(true factor PnL)NN((XXtt bw^0 tt^0 ^f^t;t;XXttbb^0 t(^0 t(BB^0
0   ^11 BB))  ^11 bbt)t)
If, for example, we observe a negative idiosyncratic PnL over a given timeinterval, we can determine whether $0 falls inside the 95% condence interval ornot. The same applies to factor PnL. An additional result is that the time series
```
of factor and idiosyncratic PnL are in general negatively correlated. Take thecase of a constant portfolio, and constant factor exposuresbetween factor and idiosyncratic PnL is given by b (^0) (B 0
 b . The covariance (^1) B)  (^1) b. This is
sometimes observed in practice.
We rst discuss the paradoxes introduced in the rst section, both analytically13.2.3. Paradox Resolutionand numerical examples.
 (Factor Portfolios)where the 1 is in theFactor portfolioith position, soihas exposure vectorkbtk= 1. Thereforebi= (0;:::; 0 ; 1 ; 0 ;:::;0),
(true idiosyncratic PnL)(true factor PnL)NN^   0 Xt;T=1T[(f^Bt;i^0 ;T  [(^1 BB^0 )^   ^1 ]^1 i;iB) ^1 ]i;i!
So the factor portfolio has a random zero-mean idiosyncratic PnL whosevariance grows linearly inT. 406


 (Factor-Neutral Portfolios)i.e.,portfolio) has exposureB (^0) w= 0. The portfoliobi= (0Letw+w;:::;;:::;a portfolio with no exposure to any factor,vi(where0). The factor and idiosyncraticviis the rst factor-mimicking
PnL are:(true factor PnL)N (^) XtT=1f^t;i; (^2) T[(B 0
   (^1) B)  (^1) ]i;i!
The idiosyncratic PnL is no longer independent of the hedgeIPN^ Xt=1T w^0 ^t;^2 T[(B^0  ^1 B) ^1 ]i;iv!i. A greater
hedge makes the idiosyncratic attribution more uncertain, and the uncertaintyis linear in the hedge.
(either graphically, or in tabular form), the standard errors of the factorWhen reporting factor-based performance attributions, always includeInsight 13.1:Reporting Standard Errors for Attributions
and idiosyncratic PnL:(true factor PnL)N(Xt b (^0) t^ft;Xt b (^0) t(B 0
   (^1) B)  (^1) bt)
This will help the portfolio manager better understand the uncertaintyassociated with her attributed performance.(true idiosyncratic PnL)N(Xt wt^0 ^t;Xt b^0 t(B^0  ^1 B) ^1 bt)
Summing up, the current factor-based attribution methodology universallyassigns a numeric factor and idiosyncratic PnL to a strategy; these are deter-ministic functions of the portfolios over time, the stock returns, and additional
available data, such as asset characteristics. Ignoring the estimation error of 407


```
these attributions leads to inconsistencies. These inconsistencies are not edgecases. Attributing performance of factor portfolios and of hedged portfolios iscentral to the practice of risk management and to understanding the perfor-
mance of a strategy. As a simple resolution to these paradoxes, we saw that,even if are employing the the true factor model, the returns of the factor-mimicking portfolios are unbiased estimates of the actual factor returns, and
that we can characterize the estimation error. Given this characterization, onecan propagate its impact in the performance attribution process, and view thefactor and idiosyncratic PnL as random variables for which we have the full
distributions (under the assumption of normality of returns) and the condenceintervals.
13.3. Maximal Performance AttributionA dierent way to summarize the previous section is: do performance attribution,but use caution. The coming section admits a similarly concise summary: do
```
goodperformance attribution, but trying to reduce confusion. If had to attempt aparallel to real life, performance attribution is like falling in love: fundamentally, but certainly dangerous, and potentially confusing. Where does the
confusion come from? Consider the following scenario. A portfolio manager haspositive momentum exposure and loses a large sum due to a negative momentumreturn. He then cuts momentum exposure to zero, as a defensive measure. The
expectedday after, the factor has a very large negative return. We ask: is the portfoliosthat the relationship between asset performance and factor returns is mediatedPnL equal to zero? The answer is no. Another way to state this fact is
by betas, not exposures. The beta of a portfolio to momentum is given by the 408


covariance between portfolio returns and the factor's returns, divided by thefactor's variance. In formulas (^4) :
The beta is in general non zero even if^ (w^0 r;fi)b'i= 0, becauseb^0 i^2 fei =Pk 6 =0k;ibk(k=i).
Factors other than momentum, but that are correlated to it, are responsiblefor the transmission of the shock.
country factor (whose loadings are all ones) and a historical beta factor. Youhave the option of z-scoring the historical beta loadings. The choice to z-scoreLet us go through another example. You are developing a risk model with a
does not aect the performance of the risk model, i.e., z-scoring is a modelrotation if a country factor is present, and aggregated factor risk does notchange if you z-score or not; nor does the aggregate performance attribution.
However, PnL attributions of the individual beta and country factor change.Z-scoring makes attribution in the beta factor much smaller. What is the \right"choice? What criteria should we use? This is relevant forex postanalysis. If a
portfolio has a large factor drawdown, it is possible that the PnL be spreadacross multiple factors and that no factor stands out. It is also possible that allthese factor losses may be correlated. For example, losses in many industries
could be \explained" as Momentum losses, or crowding losses. The problemis not only associated with performance analysis. Thewith a factor depends on the representation of the factor itself in the risk model.ex anterisk associated
also assume that the factor portfolio has negligible idiosyncratic variance.^4 We use the notationeifor the vector having a 1 in theith position: (0;:::;^1 ;:::;0). We


By this, we mean that the information contained in a given set of factors canbe represented in dierent ways. The same factor may have zero correlation toother factors in one representation, and positive correlation in another. The
central question is then: pick away to assign performance attribution and risk to this subset, such that itexplains the PnL and the risk of the portfolio as much as possible?subsetof factors. Is there a single, non-ambiguous
maximum risk and PnL to a subset of factors. There are four dierent ways toformulate and model the problem, all yielding the same result.The answer is in the armative: there is a procedure to assign unequivocally
We introduce some notation. Denote the setsU:=f 1 ;:::;mg

SS:=:=ff (^1) p;:::;p+ 1;:::;mg g
so we write1. Maximal Cross-Sectional Return Explanation.describing the asset returns as function of the returns of factorfSinstead off(p+1):mor (^) U;Sinstead of (^) Consider the problem of1:p;(p+1):m. uas well
as possible, i.e., r= fS+ (13.2)
wherethe maximum amount of returns we can attribute to factorswe identify beta, the return attributed to the factors is 2 Rnpandis independent offS. By construction, this is 0 fS, which is inU. Once


general dierent thanBS;UfminS. We solve the problemEkk (^2) (13.3)
s:t:rr == 2 Bf (^) RfnS++p
This is equivalent to min EkBf  fSk 2
which is solved bySis given by =B
U;S  S;^1 S. Then the attribution using factor set
w^0 wf^0 Sr===wbb^00 S^0 UfSS;S;S+  S(Pnl independent of S;^1 S; (^1) SffSS+b (^0) S (^) S;S  S; (^1) SffSS)
The termw^0 fSis the=maximalb^0 SfS+battribution to factors in^0 S^ S;S^  S;^1 SfS S. When factors(13.4)
inblockwise structure, withperformance attribution and maximal attribution are the same. But inuare uncorrelated to factors in (^) S;U= 0, and thenS, the factor covariance matrix has a =B;S, so that standard
general, the factors inattribution shifts the PnL attributable to factors infactors. Sand inSare correlated and (^) SS;Ufrom the other 6 = 0. Maximal

2. Conditional Expectation. There is another way to interpret these formulas, 411


```
based on conditional distribution of the multivariate Gaussian distribution.Given returnsknown analytically and are given by the vectorfS, the conditional expected returns of factors inSare
The formula for the normal performance attribution isE(fSjfS) =^ S;S^  S;^1 SfS (13.5)
and this is identical to the maximal attribution term in Equationb^0 SfS+b^0 SE(fSjfS) =b^0 SfS+b^0 S^ S;S^  S;^1 SfS (13.4).
```
3. Maximal Portfolio PnL Explanation.portfolioby means of the returns of factors in setw (^0) , with factor exposureb. Try to explain as much of this PnLStart with the factor PnL of theS. In formulas, we solve the
problem~bmin 2 RpE (^) b (^0) f b~ (^0) fS (^2) = minb~ 2 Rpb (^0) U;Ub+x (^0) S;Sx  2 b (^0) U;Sb~
and the PnL attribution is~b^0 fS =b^0 U;S  S;^1 S)fS~b, which is, again, we=^  S;^1 S^ S;Ub
obtain Equation (13.4).This suggests an interpretation of the vectorof the portfolio to factors in setS. b~as theadjusted-dollar betas

4. Uncorrelated Factor Rotationmodels are not uniquely determined. One can transform the loadingsmatrix by right-multiplying it by a non-singular square matrix. We have seen in Section 3.4.1 that factorC, and
    correspondingly transform the factor returns by left-multiplying them by 412


CIt makes the same predictions as the original risk model, in the sense thatthe factor variance predicted by the two models is identical, and so is the ^1. The resulting risk model has factor covariance matrixC ^1 (C ^1 )^0.

total factor PnL attribution. However, the PnL attributed to the individualfactors will change. [whether there is an equivalent model that yields the above \maximalw (^0) B]ifiis not the same as [w (^0) BC]i[C  (^1) f]i. We ask
attribution" for the rstanswer to the rst question is simple, given the previous derivations. Weneed to ndCsuch thatpfactors, and what is its interpretation. The
Xi2S[b (^0) C]i[C  (^1) f]i=b (^0) U;S  S; (^1) SfS (13.6)
dene the matrixA:= (^) U;S (^) C S:=^1 ;S (^0) B@and the rotation matrixIS;S 0 Cas
) C ^1 =^0 B@I ASA I;S ISS^0 ;;SS^1 CA^1 CA
Direct calculation shows that[b (^0) C]S=b (^0) S+b (^0) S (^) U;S  S; (^1) S=b (^0) U;S  S; (^1) SfS (13.7)
which is the same as Equation (13.3).


In the rotated risk model the covariance matrix isC  (^1) (C  (^1) ) (^0) = (^0) B@IS;S 0
=^0 B@^ AS 0 ;S I S;SS;S^1 CA ^0 B@ (^) S^0 ;SSS ;;SS S; (^1) S^ SSS;;SS;S^1 CA^1 CA^0 B@I SA I;S S^0 ;S(13.8)^1 CA
The interpretation of the transformation is that it makes the rstfactors independent from the remaining ones. The returns and volatilitiesof the rstpfactors are unchanged, and the volatilities of the remainingp
ones are reduced. This is unintuitive at rst sight, but has a simpleinterpretations: we have orthogonalized the factors in the setpushed the explanatory power in the rstpones. The dollar exposures ofS, and
a portfolio for the rsttoattributable to them is increasing as well.C (^0) b, as per Equationp(13.7)factors, on the other side, areso that the volatility and the performancechangingfromb
(top). We select as maximal factors the market, momentum, and crowding fac-Let us go through an example. We have a sector strategy for which we per-formance daily factor performance attribution, which is shown in Figure 13.1
tors. After rotating the remaining factors, the performance attribution changessignicantly and is shown in Figure 13.1 (bottom). Market is responsible fora higher loss; crowding is \
atter" than in the regular attribution, whereas
momentum changes sign: it had a cumulative PnL of $2.6M in the regularattribution, but it has $-5M in the maximal attribution.We close this section with two observations. First, we focused on the
\maximal attribution" factors. Alternatively, we could focus on the factors in 414


Procedure 13.1:1. Inputs: Factor covariance matrixMaximal Attribution 
2 Rmm; loadings matrix

2. SetBportfolio^2 Rnwp, factor universe. b:=BU (^0) w:=f^1 ;:::;mg; setsS,S:=U=S;
AC:=:= (^) U;ISSA (^) ;S S;^1 SIS (^0) ;S
3. OutputPer-factor maximal PnL: PnLRotated Factor covariance matrix:: k= [b ~ (^0) A:=]kfCk, for all  (^1) (C k (^1) )2S 0.
Procedure 13.2:1. Inputs: Factor covariance matrixNested Maximal Attribution 
2 Rmm;U:=f 1 ;:::;mg;

2. Forset partition(a)iPerform Maximal Attribution (Procedure 13.1) onS= 1i,w;:::;p. S^1 :;:::;SpofU; portfoliow. ,B,U,
3. Return PnL(b) Set(ik), for:= 0
 kSi2U;Si,, and the rotated risk modelU U=Si,B^ B;U,^ ~U;U.
    BBBB@::: ::: ::: ::: ::: 000 (1) ::: :::::: :::^0 (2) :::::: (p^000  1) 
000 1 CCCCA


size growth industry

volatility dividend yield value

market momentum crowding

0 25 50 75 0 25 50 75 0 25 50 75

```
−20−10^0
−20−10^0
−20−10^0 period
```
PnL

size growth industry

volatility dividend yield value

market momentum crowding

0 25 50 75 0 25 50 75 0 25 50 75

```
−20−10^0
−20−10^0
−20−10^0 period
```
PnL

Figure 13.1:attribution on three factors: market, momentum, and crowding.Top: PnL base factor performance attribution. Bottom: Maximal
the setidentied \minimal attribution" factors. The model has been rotated so thatthe portfolio performance has been described by a smaller dimensional space.S. If the performance attributable to these factor is small, then we have


```
of having a \maximal attribution" set and a \minimal attribution" set, weextend the approach to a partition of the factor setSecondly, we can perform anestedmaximal performance attribution. Insteadf 1 ;:::;mgby factor setsSi.
Factor setof the remaining PnL; and so on. The most granular instance is that whereSi=fig, so that we orthogonalize the model sequentially one factor at a time.S 1 gets the maximal attribution; setS 2 gets the maximal attribution
```
\market factor" set composed of country, market and volatility factors; then aIn practice, however, it may be more sensible to create a coarser partition,every element of which describes a common theme. For example, we may have a
\value factor" set composed of earnings yield, earning variation, dividend yield,book-to-price, and quality; a \sentiment factor" set, an \industry set", and soon. The steps involved in simple maximal attribution and nested attribution
are described in Procedures 13.1 and 13.2.
13.4. Selection vs. Sizing AttributionIn factor-based attribution, the idiosyncratic prot and loss (PnL) of a strategyis the most crucial performance term, representing the PnL that cannot be
explained by factor exposure. While factor-based attribution identies the non-idiosyncratic portion of the PnL, it fails to explain the source of idiosyncraticperformance. Portfolio managers often consider asset selection and sizing as the
primary sources of their skills. Selection skill refers to the ability to be long onstocks with positive returns and short on those with negative returns. Sizingskill means being more protable when right than when wrong. These skills
have practical implications for portfolio construction and can lead to improvedrisk-adjusted performance. Quantitative analysts have developed \hitting" and


\slugging" metrics to quantify selection and sizing. Hitting is the percentageof protable single-asset investments, while slugging is the ratio between theaverage PnL of protable and unprotable investments. Despite their intuitive
appeal, these measures have two drawbacks: they lack a direct relationshipwith protability measures like Information Ratio, and do not provide clearguidance for portfolio managers.
sizing decomposition achieves three objectives:1.This section aims to address these problems. We show how a new selection-It links through an analytical, interpretable formula the Information Ratio
2.(IR) of a strategy to selection, sizing and breadth of a portfolio;It provides guidance for portfolio managers, both in the case that thestrategy has positive sizing skill and that it has negative sizing skill.
deviation. If we restrict our attention to a single period, an estimate of the IRis The IR is the expected value of the idiosyncratic PnL divided by its standard
An estimate for the IR that employs the available time series of portfolios inIRct=(Idio PnL)(Idio Vol)tt
epochs 1; 2 ;:::;Tis IR =c T 1 XT
The IR can be expressed as a simple combination of intuitive terms. Thet=1cIRt


decomposition isIR =c T 1 XT
The terms in the identity are:t=1[(selection)t(diversication)t+(sizing)t]

 Aselectionskill. (selection)t:= (^1) nXi=1n ~t;isgn (wt;i):
We z-score the idiosyncratic returnand multiply it by the sign of that asset's holding. If holding and return havethe same sign, the portfolio manager was on the right side of a security bett;iof an asset to obtain~t;i:=t;i=i
in a specic period and the contribution to selection is positive. Z-scoringputs assets with dierent volatility on the same scale, so that selection doesnot reward the magnitude of the return.
 Diversicationwe use the dollar volatility of each position, dened aswe dene. Instead of reasoning about the notional value of positions,w~t;i:=iwt;i. Then
When all the dollar volatilities are identical, then the portfolio diversication(diversication)t:=kkww~~ttkk^12
1 andisportfolio diversication is 1. The diversication squared ranges betweenpn. At the other end, if the portfolio has a single position, then then, and can be interpreted as the eective number of assets. This
diversication term has a well-known connection to the Herndahl Index,which is a measure of concentration. To be more specic, dene weights 419


xrelationship is thendiversication and portfolio construction was rst explored by Bouchaudi:=jw~t;ij=Pjjw~t;jj. The Herndahl Index is dened as(diversication)t= 1=pH. The relationship betweenH:=Pix^2 i. The
 et al. [1997].The last term iswhere we treated the quantities associated to individual assets as empiricalsizing. It is equal to here,covcis a cross-sectional covariance,
observationsbetween being on the right side of a betSizing is positive if, when the portfolio manager is right about the^5. The interpretation of sizing is that it measures the correlation~t;isgn (wt;i), and the bet sizesidejiwof at;ij.
position, they are right about itsIn formulas, we rst we dene sizeby having a relatively large position.
This equation can be used in several ways. To achieve a higher IR, a portfolio(sizing)t:=kw~ntkcov(c (right-side index)~|tsgn ({z w~t});(bet size)j|{z}w~tj )
manager has the following three options: Increase diversicationonly free lunch in investing. This equation shows that benets from diversi-. Markowitz famously said that diversication is the
cation are accrued via selection skill, i.e., selection is the marginal benetobtained by increasing diversication. This reasoning is not entirely correct,however. Managers can increase diversication in two ways. The rst one is
by making portfolio positions more equal. This does not require additionaleort 5 6. Alternatively, the portfolio manager could add stocks to the invest-
reasonable approximation for small portfolios. A more comprehensive model is possible, but^6 More rigorously, for two vectorsThe analysis presented here does not take into account transaction costs. This is ax;y^2 Rn,dcov(x;y) :=n ^1 Pixiyi n ^2 PjxjPkyk.


ment universe. This operation is not costless, since it would involve spendingless time on each stock, and possibly cover less desirable stocks not in theprimary universe. When increasing diversication, the manager may want to
 consider the impact on stock selection from this decision.Improve selection skillmeasure, which makes use of the entire dataset at a manager's disposal:. The decomposition helps by providing a simple
daily positions, PnL, and idiosyncratic risk of the individual positions. Onceselection can be measured, several actions are possible. For example, theportfolio manager can track selection skill at the sub-industry or at the
thematic level; or the portfolio manager can compare performance duringearnings versus outside earnings. Improving portfolio selection is not easy,but is possible.
 Improve sizing skilltheir sizing skill relative to selection; most portfolio managers overestimatetheir sizing skill, and nd the low sizing skill, or even the absence thereof,. There is value already in having portfolio managers assess
instructive. If their sizing skill isnot dierentiate positions according to size. In doing so, they will eliminatethe drag from negative sizing and magnify the benet of stock selection, bynegative, the portfolio manager should
maximizing breadth. If there iscan optimize the size of the high-conviction positions to maximize the IR.This is the subject of the next subsection.positivesizing skill, the portfolio manager
outside of this article's scope.


13.4.1. Connection to the Fundamental Law ofActive Management
This formula bears some resemblance to Grinold and Kahn's Fundamental Lawof Active Management [Grinold and Kahn, 1999]. That formula stated that theIR is the product of the Information Coecient and the breadth of the portfolio
ptreats not all positions as equal. For example, a portfolio of 100 stocks with agross notional of $1 million in each of them does not have the same breadthn. This formula uses a dierent portfolio breadth {the eective breadth{which
of a portfolio of 100 stocks where one position is $999,901 in one stock and $1in the remaining 99. In their seminal article, Bouchaud et al. [1997] present amodied mean-variance portfolio formulation that puts a lower bound on our
denition of diversication. This results in using a shrinked covariance matrix.The same approach has been advocated using robust portfolio constructionmodels [Stubbs and Vance, 2005, V. et al., 2013, Pedersen et al., 2021] and
penalized covariance estimation methodologies [Ledoit and Wolf, 2003a].
13.4.2. Long-Short Performance AttributionThe selection component of our performance attribution is linear, and thereforelends itself naturally to be further partitioned in dierent performance sub-
classes. A natural partition is long versus short; that is, the fraction of selectionskill that arises from being on the right side of returns when positions are long,versus when positions are short. The decomposition follows from the chain of
equalities below.


Factor PnL Total PnL Information Idio PnLRatio

Factor(1) PnL Diversification (Long Selection)**...** _q_ longFactor(m) Diversification ✕PnL SelectionDiversification (Short Selection)✕ (^) _q_ short ✕ Sizing
Figure 13.2:A Taxonomy of Performance Attribution.
(selection)t==nn^1 longni:wXt;in>long 10 ~t;ii:sgn (wXt;i>w 0 ~t;it;i) +sgn (n^1 wi:t;iwXt;i) +< (^0) n~t;ishortnsgn (nshortw 1 t;i)i:wXt;i< 0 ~t;isgn (wt;i)
wherenlong;n=shortqlongare the number of long and short positions, and(selection)L;t+qshort(selection)S;t qlong;qshortare
the fraction of the total portfolio positions that are long and short, respectively.sition terms.Summing up, in Figure 13.2 we show the dependency tree of the decompo-


13.5. Appendix13.5.1. Proof of the Selection vs. Sizing Decom-?
iid idiosyncratic returnsTheorem 13.1:positionConsider a portfolio sequencettaking values inRn, withwt^2 covRn(, and a sequence oft) =. Dene the
Empirical Information Ratio:IRc=T 1 XT
Then the identity holds t=1(Idio PnL)(Idio Vol)tt
where the terms in the equation above are dened as follows:cIR=T^1 XtT=1[(selection)t(diversication)t+(sizing)t] (13.9)

w~~utt:=:= (^) p^1 n=^2 kwww~~tttk
(diversication)(selection)~ttt:=:=:=^ Ep^( n~^1 Et^=^2 (jusgn~ttj)(u~t))
(sizing)t:==pkkww~~nttcovckk^12 (~tsgn(u~t);ju~tj)
=kwn 424 tkcovc(~tsgn(w~t);jw~tj)


byProof. In periodt, the risk-adjusted PnL of the portfolio at timetis given
Setw~t:= 
1 =^2 wt, and~t:= IRc ^1 t=^2 =t. The vectorpww^0 t^0 t
wt t w~thas a familiar interpreta-
tion. It is a portfolio whose positions are not expressed as NMV but rather asdollar volatilities in each asset. The return vectorreturns. Its covariance matrix is the identity. With these transformations, the~tcontains the z-scored asset

sample IR takes a simpler form:IRct=kw~w~ (^0) t~tkt
This follows from the fact that the numerator iswt (^0) t=Xi wt;it;i=Xi (iwt;i)(t;i=i)
and the denominator is =Xi w~t;i~t;i
q(w (^0) t 
1 = (^2) )( 
1 = (^2) wt) =jj 
1 = (^2) wtjj=kw~tk
We can further simplify the formula by considering a breadth-rescaled


percentage of the total dollar volatility:IRct=Xi ~ikww~~ik
==Xpinn~ 1 isgn ( ~Xi ~wisgn ( ~i)kjww~~wikji)pknw~jw~kij
where we set =pnn^1 Xi ~isgn (~ui)j~uij
We denote thecross-sectional empirical averageu~t:=pnkww~~ttkand thecross sectional empirical
covariance E^(x) :=n  1 Xi xi

```
The formula becomes:cov(c x;y) :=E^[(x E^x)^2 (y E^y)^2 ]
where we have used the notation `cIRt=pnE^' to the denote the element-wise (Hadamard)(~tsgn (u~t)ju~tj)
product of two vectors, i.e.: (identityE^(xy) =covc(x;y) +xyE^)(ix:=)E^x(yiy) withi. Finally, in the last step we use thex=~tsgn (~ut)andy=ju~tj.
```

It follows thatIRct=pnhE^(~tsgn (u~t))E^(ju~tj) +cov(c ~tsgn (u~t);ju~tj)i

1 IR over a single observation, or period. An estimate of the IR over the period;:::;TA possible interpretation of the above formula is as a sample of the realizedis then given by its time-series average:
IR =c=pT^1 nXt=1T"T 1 kw~wX~T^0 t~ttk
This is equal to Equation (13.9) once we denet=1E^(~tsgn (u~t))E^(ju~tj) +T^1 Xt=1T cov(c ~tsgn (u~t);ju~tj)#
(diversication)(selection)tt===Epq^P(n~niEt^=1(jjsgn (u~w~tjt;i)ju~t))
(sizing)t=pnPcov(cni=1~wt~^2 t;isgn (u~t);ju~tj)

=qPnin=1w~ (^2) t;icov(c ~tsgn (w~t);jw~tj)



# Bibliography

## V. Agarwal and N. Y. Naik. Risks and portfolio decisions involving hedge funds.Y. At-Sahalia, P. A. Mykland, and L. Zhang. How often to sample a continuous-The Review of Financial Studies, 17(1):63{98, 2004.

## P. H. Algoet and T. M. Cover. Asymptotic optimality and asymptotic equipar-Financial Studiestime process in the presence of market microstructure noise., 18(2):351{416, 2005. Review of

## R. Almgren, C. Thum, H. L. Hauptmann, and H. Li. Equity market impact.tition properties of log-optimum investment.876{898, 1988. Annals of Probability, 16(2):

## Y. Amihud, H. Mendelson, and L. H. Pedersen.RiskUniversity Press, 2012., pages 57{62, July 2005. Market liquidity. Cambridge

## T. G. Andersen and L. Benzoni. Realized volatility. In T. G. Andersen, R. A.SeriesDavis, J.-P. Kreiss, and T. Mikosch, editors,, pages 555{575. Springer, 2009. Handbook of Financial Time

## T. G. Andersen, T. Bollerslev, P. F. Christoersen, and F. X. Diebold. Volatilityand correlation forecasting. In G. Elliott, C. W. J. Granger, and A. Tim-mermann, editors,Handbook of Economic Forecasting, volume 1, chapter 15,

## pages 777{878. Elsevier, 2006. 429


T. G. Andersen, R. A. Davis, J.-P. Kreiss, and T. Mikosch, editors.T. G. Andersen, T. Bollerslev, P. F. Christoersen, and F. X. Diebold. Financialof Financial Time Series. Springer, 2009. Handbook
risk measurement for nancial risk management. In G. M. Constantinides,M. Harris, and R. M. Stulz, editors,volume 2, part B, chapter 17, pages 1127{1220. Elsevier, 2013.Handbook of the Economics of Finance,
T. W. Anderson. Theory for principal component analysis.R. Arnott, C. R. Harvey, and H. Markowitz. A backtesting protocol in theMathematical Statistics, 34(1):122{148, 1963. The Annals of

C. S. Asness, A. Frazzini, and L. H. Pedersen. Quality minus junk.era of machine learning.2019. The Journal of Financial Data Science, 1(1):64{74,Review of
J. M. Bacidore.Accounting StudiesAlgorithmic Trading: A Practitioner's Guide, 24(34-112), 2019.. TBG Press, 2020.
C. R. Bacon.Z. Bai and S. Ng. Large dimensional factor analysis.Wiley, 2005.Practical Portfolio Performance Measurement and AttributionFoundations and Trends.
Z. Bai and J. Yao. Central limit theorems for eigenvalues in a spiked populationin Econometricsmodel.Annales de l'Institut Henri Poincare, 3(2):447{474, 2008. , 44(3):447{474, 2008.
J. Baik and J. W. Silverstein. Eigenvalues of large sample covariance matricesof spiked population models.2006. Journal of Multivariate Analysis, 97:1382{1408,


J. Baik, G. Ben Arous, and S. Peche. Phase transition of the largest eigenvalue(5):1643{1697, 2005.for nonnull complex sample covariance matrices.Annals of Probability, 33
B. M. Barber and T. Odean.2(B), chapter The Behavior of Individual Investors, pages 1533{1570. Elsevier,2013. Handbook of the Economics of Finance, volume
G. I. Barenblatt.O. E. Barndor-Nielsen and N. Shephard. Estimating quadratic variation usingrealized variance.ScalingJournal of Applied Econometrics. Cambridge University Press, 2003., 17(5):457{477, 2002.
O. E. Barndor-Nielsen, P. R. Hansen, A. Lunde, and N. Shephard. Designingrealized kernels to measure the ex post variation of equity prices in thepresence of noise.Econometrica, 76(6):1481{1536, 2008.
O. E. Barndor-Nielsen, P. R. Hansen, A. Lunde, and N. Shephard. Realizedkernels in practice: trades and quotes.2009. Econometrics Journal, 12:C1{C32,
D. P. Baron. On the utility theoretic foundations of mean-variance analysis.M. S. Bazaraa, H. D. Sherali, and C. M. Shetty.Journal of Finance, 32(5):1683{1697, 1977. Nonlinear programming: theory
F. Benaych-Georges and R. R. Nadakuditi. The eigenvalues and eigenvectorsand algorithmsof nite, low rank perturbations of large random matrices.. Wiley, 3rd edition, 2006. Advances in
Mathematics, 227(1):494{521, 2011.


Jennifer Bender, Remy Briand, Dimitris Melas, and Raman Aylur Subramanian.Foundations of factor investing. Technical report, MSCI Research Insight,2013.
R.-P. Berben and W. J. Jansen. Comovement in international equity markets:A sectoral view.2005. Journal of International Money and Finance, 24(5):832{857,
C. Bergmeir, R. J. Hyndman, and B. Koo. A note on the validity of cross-Statistics & Data Analysisvalidation for evaluating autoregressive time series prediction., (70-83), 2018. Computational
P. J. Bickel and E. Levina. Covariance regularization by thresholding.C. M. Bishop.of Statistics, 36(6):2577{2604, 2008.Pattern Recognition and Machine Learning. Springer, 2006.Annals
G. W. Bluman and S. Kumei.J. Boivin and S. Ng. Are more data always better for factor analysis?1989. Symmetries and Dierential Equations. Springer,Journal
T. Bollerslev. Modelling the coherence in short-run nominal exchange rates: Aof Econometricsmultivariate generalized arch model., 132(1):169{194, 2006.The Review of Economics and Statistics,
J.-P. Bouchaud and M. Potters.72(3):498{505, 1990.Cambridge University Press, 2020.A First Course in Random Matrix Theory.
J.-P. Bouchaud, M. Potters, and J.-P. Aguilar. Missing information and assetallocation. cond-mat/9707042, 1997. 432


J.-P. Bouchaud, J. Bonart, J. Donier, and M. Gould.S. Boucheron, G. Lugosi, and P. Massart.Cambridge University Press, 2018. Concentration Inequalities: ATrades, Quotes and Prices.
S. Boyd and L. Vandenberghe.Nonasymptotic Theory of IndependencePress, 2004. Convex Optimization. Oxford University Press, 2013.. Cambridge University
L. Breiman. Optimal gambling systems for favorable games. In J. Neyman,editor,pages 65{78. University of California Press, 1961.Fourth Berkeley Symposium on Mathematical Statistics and Probability,
R. Brooks and M. Del Negro. Country versus region eects in internationalC. Brownlees, B. Engle, and B. Kelly. A practical guide to volatility forecastingstock returns.Journal of Portfolio Management, 31(4):67{72, 2005.
Svetlana Bryzgalova, Jiantao Huang, and Christian Julliard. Bayesian solutionsthrough calm and storm.for the factor zoo: We just ran two quadrillion models.Journal of Risk, 14(2):3{22, 2011.The Journal of
J. Bun, J.-P. Bouchaud, and M. Potters. Cleaning large correlation matrices:FinanceTools from random matrix theory., 78(1), 2022. Physics Reports, 666:1{109, 2017.
D. Buraczewski, E. Damek, and T. Mikosch.P. Burns, P. Engle, and J. Mezrich. Correlations and volatilities of asynchronoustails. Springer, 2016. Stochastic models with power-law
data. University of California, San Diego, discussion paper 97-30R, 1998. 433


T. T. Cai, Z. Ren, and H. H. Zhou. Estimating structured high-dimensionalElectronic Journal of Statisticscovariance and precision matrices: optimal rates and adaptive estimation., 10:1{59, 2016.
I. Calvino.R. B. Cattel. The scree test for the number of factors.1999. Six Memos for the Next Millennium. Harvard University Press,Multivariate Behavioral
S. Cavaglia, C. Brightman, and M. Aked. The increasing importance of industryResearchfactors.Financial Analysts Journal, 1(2):245{276, 1966. , 56(5):41{54, 2000.
S. Ceria, A. Saxena, and R. A. Stubbs. Factor alignment problems and quanti-tative portfolio management.2012. Journal of Portfolio Management, 28(2):29{43,
V. Cerqueira, L. Torgo, and C. Soares. Model selection for time series forecasting10073{10091, 2023.an empirical analysis of multiple estimators.Neural Processing Letters, 55:
G. Chamberlain. A characterization of the distributions that imply mean-G. Chamberlain and M. Rothschild. Arbitrage, factor structure, and mean-variance utility functions.Journal of Economic Theory, 29:184{201, 1983.

A. Y. Chen and M. Velikov. Accounting for the anomaly zoo: a trading cost1983.variance analysis of large asset markets. Econometrica, 51(5):1281{1305,
perspective.working paper, 2019.


L. B. Chincarini and D. Kim. Another look at the information ratio.L. B. Chincarini and D. Kim.of Asset Management, 8(5):284{295, 2007.Quantitative Equity Portfolio ManagementJournal.
A. Chinco and M. Sammon.McGraw Hill, 2nd edition, 2022.ble what you think it is, 2023.The passive-ownership share is dou-URL https://www.alexchinco.com/
V. K. Chopra and W.Ziemba. The eect of errors in means, variances, anddouble-what-you-think-it-is.pdf.covariances on optimal portfolio choice.Journal of Portfolio Management,
P. Cizek, W. K. Hardle, and R. Weron.19(2):6{11, 1993.Insurance. Springer, 2nd edition, 2011. Statistical Tools for Finance and
R. Clarke, H. de Silva, and S. Thorley. Portfolio constraints and the fundamentalA. Clauset, C. R. Shalizi, and M. E. J. Newman. Power-law distributions inlaw of active management.Financial Analysts Journal, 58(5):48{66, 2002.
J. H. Cochrane.empirical data.Asset PricingSIAM Review. Princeton University Press, 2005., 51(4):661{703, 2009.
J. H. Cochrane. The dog that did not bark: a defense of stock return pre-K. J. Cohen, G. A. Hawawini, S. F. Maier, R. A. Schwartz, and D. K. Whitcomb.dictability.The Review of Financial Studies, 21(4):1533{1575, 2008.
of Financial EconomicsFriction in the trading process and the estimation of systematic risk., 12:263{278, 1983. Journal


G. Connor and R. A. Korajczyk. Factor models of asset returns. In R. Cont,G. Connor, L. R. Goldberg, and R. A. Korajczyk.editor,Encyclopedia of Quantitative Finance. Wiley, 2010.Portfolio risk analysis.
R. Cont. Empirical properties of asset returns: stylized facts and statisticalPrinceton University Press, 2010.issues.Quantitative Finance, 1:223{236, 2001.
K. Daniel, L. Mota, S. Rottke, and T. Santos. The cross-section of risk andR. A. Davis and T. Mikosch. Extreme value theory forreturns.The Review of Financial Studies, 33(5):1927{1979, 2020.GARCHprocesses. In

B. De Finetti. Il problema dei pieni.of Financial Time SeriesT. G. Andersen, R. A. Davis, J.-P. Kreiss, and T. Mikosch, editors,, pages 187{200. Springer, 2009.Giornale dell'Istituto Italiano degli AttuariHandbook,
M. H. DeGroot and M. J. Schervish.11:1{88, 1940.4th edition, 2012. Probability and Statistics. Addison-Wesley,
V. DeMiguel, L. Garlappi, F. J. Nogales, and R. Uppal. A generalized approachto portfolio optimization: improving performance by constraining portfolionorms.Management Science, 55(5):798{812, 2009a.
V. DeMiguel, L. Garlappi, and R. Uppal. Optimal versus naive diversication:(5):1915{1953, 2009b.How inecient is the 1/n portfolio strategy?Review of Financial Studies, 22
P. Diaconis and D. Freedman. Iterated random functions.45{76, 1999. 436 SIAM Review, 41(1):


C. Ding and X. He. K-means clustering via principal component analysis. InProceedings of the twenty-rst international conference on Machine learning2004. ,
J. Ding and N. Meade. Forecasting accuracy of stochastic volatility, garchEconomicsand ewma models under dierent volatility scenarios., (10):1742{1778, 2010. Applied Financial
D. L. Donoho, M. Gavish, and I. M. Johnstone. Optimal shrinkage of eigenvaluesL. Dubins and L. J. Savage.in the spiked covariance model.How to gamble if you must: inequalities forAnnals of Statistics, 46(4):1742{1778, 2018.
S. Dudoit, J. Popper Shaer, and J. C. Boldrick. Multiple hypothesis testingstochastic processesin microarray experiments.. McGraw-Hill, 1965.Statistical Science, 18(1):71{103, 2003.
G. Eckart and G. Young. The approximation of one matrix by another of lowerN. El Karoui. Spectrum estimation for large dimensional covariance matricesrank.Psychometrika, 1(3):211{218, 1936.
R. F. Engle. Autoregressive conditional heteroscedasticity with estimates ofusing random matrix theory.the variance of united kingdom in
ation.Annals of StatisticsEconometrica, 36(6):2757{2790, 2008., 50(987-1007), 1982.
R. F. Engle and T. Bollerslev. Modelling the persistence of conditional variances.E. F. Fama and K. R. French. The cross-section of expected stock returns.Econometric Reviews, 5(1):1{50, 1986.
Journal of Finance, 47(2):427{465, 1993. 437


E. F. Fama and J. D. MacBeth. Risk, return, and equilibrium: Empirical tests.J. Fan, J. Zhang, and K. Yu. Vast portfolio selection with gross-exposureJournal of Political Economy, 81(3):607{636, 1973.

J. Fan, Y. Liao, and H. Liu. An overview of the estimation of large covarianceconstraints.606, 2012. Journal of the American Statistical Association, 107(498):592{
J. Fan, R. Li, C.-H. Zhang, and H. Zou.and precision matrices.CRC Press, 2020. The Econometrics JournalStatistical Foundations of Data Science, 16:C1{C32, 2016..
S.A. Farmer. An investigation into the results of principal component analysisG. Feng, S. Giglio, and D.Xiu. Taming the factor zoo: A test of new factors.of data derived from random numbers.Statistician, 20(4):63{72, 1971.
L. Ferre. Selection of components in principal component analysis: A comparisonJournal of Financeof methods.Computational Statistics & Data Analysis, 2020. , 19(19):669{682, 1995.
A. Frazzini and L. H. Pedersen. Betting against beta.K. R. French, G. W. Schwert, and R. F. Stambaugh. Expected stock returnsEconomics, 111(1):1{25, 2014. Journal of Financial
J. Freyberger, A. Neuhierl, and M. Weber. Dissecting characteristics nonpara-and volatility.metrically.Review of Financial StudiesJournal of Financial Economics, 33(5):2326{2377, 2020., 19(1):3{29, 1987.
G. Galilei.Il Saggiatore. 1623. 438


J. Gatheral. Three models of market impact. 2016.A. Gelman, J. Hill, and A. Vehtari.University Press, 2022. Regression and Other Stories. Cambridge
J. Gerakos and J. T. Linnainmaa. Asset managers: Institutional performanceJ. C. Gibbins.and factor exposures.Dimensional AnalysisJournal of Finance. Springer, 2011., 76(4):2035{2075, 2021.
DetlefviewURL Glow.{ relative Mondayhttps://lipperalpha.renitiv.com/reports/2024/01/performancemorningequitymemo:fundsPerformance2023, 2023.re-
G. H. Golub and C. F. Van Loan.monday-morning-memo-performance-review-relative-performance-equity-funds-2023/.University Press, 4th edition, 2012.Matrix Computations. Johns Hopkins
B. Graham.C. W. J. Granger and Z. Ding. Some properties of absolute return: an alternativemeasure of risk.The Intelligent InvestorAnnales d' 'Economie et de Statistique. Harper Business, 2006., (40):67{91, 1995.
J. Green, J. R. M. Hand, and X. F. Zhang. The supraview of return predictiveR. C. Grinold. The fundamental law of active management.signals.Review of Accounting Studies, 18:692{730, 2013.Journal of Portfolio
R. C. Grinold and R. N. Kahn.ManagementEducation, 2nd edition, 1999., 15(3):30{37, 1989.Active Portfolio Management. McGraw-Hill
S. J. Grossman and Z. Zhou. Optimal investment strategies for controllingdrawdowns.Mathematical Finance, 3(3):241{276, 1993. 439


O. Gueant.B. Hansen.Hall/CRC, 2016.EconometricsThe Financial Mathematics of Market Liquidity. Princeton University Press, 2022.. Chapman &
L. P. Hansen and T. J. Sargent.P. R. Hansen and A. Lunde. A forecast comparison of volatility models: doesanything beat agarch(1;1).Journal of Applied EconometricsRobustness. Princeton University Press, 2008., 20(7):873{889,
P. R. Hansen and A. Lunde. Consistent ranking of volatility models.of Econometrics2005. , 131(1-2):97{121, 2006a. Journal
P. R. Hansen and A. Lunde. Realized variance and market microstructure noise.P. R. Hansen, A. Lunde, and J. M. Nason. The model condence set.Journal of Business and Economic Statistics, 24(2):127{161, 2006b. Econo-
P. R. Hansen, Z. Huang, and H. H. Shek. Realized GARCH: a joint model formetricareturns and realized measures of volatility., 79(2):453{497, 2011. Journal of Applied Econometrics,
F. E. Harrell.27(6):877{906, 2012.Regression Modeling Strategies. Springer, 2nd edition, 2015.
L. Harris.A. C. Harvey.Filter. Cambridge University Press, 1990.Trading and ExchangesForecasting, Structural Time Series Models and the Kalman. Oxford University Press, 2003.
A. C. Harvey and N. Shephard. Estimation of an asymmetric stochastic volatilitymodel for asset returns.429{424, 1996. Journal of Business & Economic Statistics, 14(4):


C. H. Harvey and Y. Liu. A census of the factor zoo.C. R. Harvey, Y. Liu, and H. Zhu. ... and the cross-section of expected returns.The Review of Financial Studies, 29(1):5{61, 2016. preprint, 2020.
J. Hasbrouck.T. Hastie, R. Tibshirani, and J. Friedman.Springer, 2nd edition, 2008.Empirical Market MicrostructureThe Elements of Statistical Learning. Oxford University Press, 2007..
C. He and T. Terasvirta. Fourth moment structure of theS. L. Heston and K. G. Rouwenhorst. Does industrial structure explain theEconometric Theory, 15(6):824{846, 1999. GARCH(p;q) process.

S. L. Heston and K. G. Rouwenhorst. Industry and country eects in inter-benets of industrial diversication?3{27, 1994. Journal of Financial Economics, 36:
R. A. Horn and C.R. Johnson.1995.national stock returns.The Journal of Portfolio ManagementMatrix Analysis. Cambridge University Press,, 21(3):53{58,
C.-F. Huang and R. H. Litzenberger.2nd edition, 2012.Prentice-Hall, 1988. Foundations for nancial economics.
D. W. Huang, B. T. Sherman, and R. A. Lempicki. Bioinformatics enrichmentNucleic Acids Researchtools: paths toward the comprehensive functional analysis of large gene lists., 37(1):1{13, 2009.
G. Huberman and W. Stanzl. Price manipulation and quasi-arbitrage.metrica, 74(4):1247{1276, 2004. 441 Econo-


R. Hyndman, A. B. Koehler, J. K. Ord, and R. D. Snyder.A. Ilmanen.Exponential Smoothing: The State Space ApproachExpected Returns. Wiley, 2011.. Springer, 2008.Forecasting with
J.P.A. Ioannidis. Why most published research ndings are false.M. Isichenko.Medicine, 2(8):696{701, 2005.Quantitative Portfolio Management. Wiley, 2021. PLOS
H. Jacobs. What explains the dynamics of 100 anomalies?R. Jagannathan and T. Ma. Risk reduction in large portfolios: Why imposingand Finance, 57:65{85, 2015. Journal of Banking
N. Jegadeesh and S. Titman. Returns to buying winners and selling losers:the wrong constraints helps.implications for stock market eciency.Journal of FinanceJournal of Finance, 58(4):1651{1683, 2003., 48(1):65{91,
N. Jegadeesh and S. Titman. Momentum.1993.nomics, 3(1):493{509, 2011. Annual Review of Financial Eco-
R. A. Johnson and D. W. Wichern.D. J. Johnstone and D. V. Lindley. Elementary proof that mean{variancePearson, 6th edition, 2007. Applied Multivariate Statistical Analysis.
I. M. Johnstone. On the distribution of the largest eigenvalue in principalimplies quadratic utility.components analysis.Annals of StatisticsTheory and Decision, 29:295{327, 2001., 70(2):149{155, 2011.
I. M. Johnstone and D. Paul. PCA in high dimensions: An orientation.ceedings of the IEEE, 106(8):1277{1292, 2018. 442 Pro-


I. T. Jollie.I.T. Jollie and J. Cadima. Principal component analysis: a review and recentdevelopments.Principal Component AnalysisPhilosophical Transactions of the Royal Society A. Springer, 2nd edition, 2010., 374(2065):
L. Kagan and M. Tian. Firm characteristics and empirical factor models: a20150202, 2016.data-mining experiment, 2017.
R. E. Kalman. A new approach to linear ltering and prediction problems.R. E. Kalman and R. S. Bucy. New results in linear ltering and predictionJournal of Basic Engineering, 82(1):35{45, 1960.
R. L. Kelley.theory.Journal of Basic EngineeringGeneral Topology. Van Nostrand, 1955., 83(1):95{108, 1961.
H. Kesten. Random dierence equations and renewal theory for products ofM. Kolanovic and R. T. Krishnamachari. Big data and ai strategies: Machinerandom matrices.Acta Mathematica, 131(207-248), 1973.

P. Kolm and N. Westray. A principled approach to clean-up costs in algolearning and alternative data approach to investing. Technical report, J. P.Morgan, 2017.
A. S. Kyle. Continuous auctions and insider trading.1315{1335, 1985.trading.Risk Magazine, 2021. Econometrica, 54(6):
S. L. Lauritzen.Graphical Models. Oxford Science Publications, 1996.


O. Ledoit and M. Wolf. Improved estimation of the covariance matrix of stockFinancereturns with an application to portfolio selection., 10:603{621, 2003a. Journal of Empirical
O. Ledoit and M. Wolf. Honey, I shrunk the sample covariance matrix: Problemsin mean-variance optimization.2003b. Journal of Portfolio Management, 30:110{119,
O. Ledoit and M. Wolf. A well-conditioned estimator for large-dimensionalO. Ledoit and M. Wolf. Nonlinear shrinkage estimation of large-dimensionalcovariance matrices.Journal of Multivariate Analysis, 88:365{411, 2004.
O. Ledoit and M. Wolf. Spectrum estimation: A unied framework for covariancecovariance matrices.matrix estimation and PCA in large dimensions.Annals of Statistics, 40(2):1024{1060, 2012.Journal of Multivariate
O. Ledoit and M. Wolf. Analytical nonlinear shrinkage of large-dimensionalAnalysiscovariance matrices., 139:360{384, 2015.Annals of Statistics, 48(5):3043{3065, 2020.
J. Lewellen, S. Nagel, and J. Shanken. A skeptical appraisal of asset pricingS. Li. Should passive investors actively manage their trades?, 2021. URLtests.Journal of Financial Economics, 96:175{194, 2010.
A. M. Lindner. Stationarity, mixing, distributional properties and momentshttps://papers.ssrn.com/sol3/papers.cfm?abstractof garch(p, q)-processes. In T. G. Andersen, R. A. Davis, J.-P. Kreiss,id=3967799.
and T. Mikosch, editors,Springer, 2009. Handbook of Financial Time Series, pages 43{70.


R. Litterman and J. Scheinkman. Common factors aecting bond returns.L. Y. Liu, A. J. Patton, and K. Sheppard. Does anything beat 5-minute rv?Journal of Fixed Income, 1(1):54{61, 1991. The

A. W. Lo. The statistics of sharpe ratios.Econometricsa comparison of realized measures across multiple asset classes., 187(1):293{311, 2015. Financial Analysts JournalJournal of, 58(4):
M. Lopez de Prado.36{52, 2002.University Press, 2020.Machine Learning for Asset Managers. Cambridge
D. G. Luenberger.D. G. Luenberger and Y. Ye.3rd edition, 2008.Optimization by vector space methodsLinear and Nonlinear Programming. Wiley, 1969.. Springer,
H. Lutkepohl.A. C. MacKinlay. Multifactor models do not explain deviations from capm.2005. New introduction to multiple time series analysis. Springer,
L. C. MacLean, W. T. Ziemba, and G. Blazenko. Growth versus security inJournal of Financial Economicsdynamic investment analysis.Management Science, 38(1):3{28, 1995., 38(11):1562{85, 1992.
L. C. MacLean, R. Sanegre, Y Zhao, and W. T. Ziemba. Capital growth withL. C. MacLean, E. O. Thorp, and W. T. Ziemba. Good and bad propertiessecurity.Journal of Economic Dynamics and Control, 28:937{954, 2004.
of the Kelly criterion. In L. C. MacLean, E. O. Thorp, and W. T. Ziemba, 445


L. C. MacLean, E. O. Thorp, and W. T. Ziemba, editors.World Scientic, 2010a.editors,The Kelly Capital Growth Investment CriterionThe Kelly Capital, pages 563{574.
S. Mahajan.Growth Investment CriterionThe Art of Insight in Science and Engineering. World Scientic, 2010b.. MIT Press, 2014.
B. Malkiel.C. Mancini. Non-parametric threshold estimation for models with stochasticMarket Hypothesis, pages 1{7. Palgrave MacMillan, 1987.The New Palgrave Dictionary of Economics, chapter Ecient

C. Mancini. The speed of convergence of the threshold estimator of integrateddiusion coecient and jumps.270{296, 2009. Scandinavian Journal of Statistics, 36(2):
H. M. Markowitz. Portfolio selection.variance.Stochastic Processes and their ApplicationsJournal of Finance, 121(4):845{855, 2011., 7(1):77{91, 1952.
H. M. Markowitz.X. Mestre. Improved estimation of eigenvalues and eigenvectors of covarianceBasil Blackwell, 2nd edition, 1959.Portfolio Selection: Ecient Diversication of Investments.

R. O. Michaud. The markowitz optimization enigma: Is `optimized' optimal?Theorymatrices using their sample estimates., 54(11):5113{5129, 2008. IEEE Transactions on Information
T. Mikosch and C. Starica. Limit theory for the sample autocorrelations andFinancial Analysts Journalextremes of a garch(1, 1) process., 45(1):31{42, 1989.Annals of Statistics, 28(5):1427{1451, 2000.


J. L. Miralles Marcelo, J. L. Miralles Quiros, and J. L. Martins. The role ofFinancial Markets, Institutions and Moneycountry and industry factors during volatile times., 26:273{290, 2013.Journal of International
L. Mirsky. Symmetric gauge functions and unitarily invariant norms.Graphical Models. M. i. jordan.Quarterly Journal of MathematicsStatistical Science, 11(1):50{59, 1960., 19(1):140{155, 2004.The
M. Mohri, A. Rostamizadeh, and A. Talwalkar.K. P. Murphy.Learning. The MIT Press, 2nd edition, 2018.Machine Learning. MIT Press, 2012.Foundations of Machine
J. F. Muth. Optimal properties of exponentially weighted forecasts.R. K. Narang.the American Statistical AssociationInside the Black Box. Wiley, 3nd edition, 2024., 55(290):299{306, 1960. Journal of
D. R. Nelson. Stationarity and persistence in theW. K. Newey and K. D. West. A simple, positive semi-denite, heteroskedasticitymetric Theory, 6:318{334, 1990. GARCH(1;1) model.Econo-

B.and autocorrelation consistent covariance matrix.708, 1987.Novick. Index investing supportsEconometricavibrant, 55(3):703{capital
//www.blackrock.com/corporate/literature/whitepaper/markets.viewpoint-index-investing-supports-vibrant-capital-markets-oct-2017.pdf.Blackrock Viewpoint, 2017. URL https:
A. A. Obizhaeva and J. Wang. Optimal trading strategy and supply/demanddynamics.Journal of Financial Markets 447 , 16(1):1{32, 2013.


A. V. Olivares-Nadal and V. DeMiguel. Technical note|a robust perspectiveon transaction costs in portfolio optimization.733{739, 2018. Operations Research, 66(3):
A. Onatski. Determining the number of factors from empirical distribution ofOpen Science Collaboration. Estimating the reproducibility of psychologicaleigenvalues.Review of Economics and Statistics, 92(4):1004{1016, 2010.
R. Pardo.science.edition, 2007.The Evaluation and Optimization of Trading StrategiesScience, 349(6251):aac4716, 2015.. Wiley, 2nd
A. J. Patton. Volatility forecast comparison using imperfect volatility proxies.A. J. Patton and K. Sheppard. Evaluating volatility and correlation forecasts. InJournal of Econometrics, 160:246{256, 2011.

D. Paul. Asymptotics of sample eigenstructure for a large dimensional spikedof Financial Time SeriesT. G. Andersen, R. A. Davis, J.-P. Kreiss, and T. Mikosch, editors,, pages 801{838. Springer, 2009. Handbook
S. E. Pav.covariance model.The Sharpe RatioStatistica Sinica. Chapman & Hall/CRC, 2023., 17(1617-1642), 2017.
L. H. Pedersen.L. H. Pedersen, A. Babu, and A. Levine. Enhanced portfolio optimization.Prices are DeterminedEciently Inecient: How Smart Money Invests and Market. Princeton University Press, 2015.
M. Podolskij and M. Vetter. Bipower-type estimation in a noisy diusionFinancial Analysts Journalsetting.Stochastic Processes and their Applications, 77(2):124{151, 2021. , 119(9):2803{2831, 2009.


M. Pohl, A. Ristig, and W. Schachmayer. The amazing power of dimensional(4):1850004, 2017.analysis: quantifying market impact.Market Microstructure and Liquidity, 3
M. Pourahmadi.A. V. Puchkov, D. Stefek, and M. Davis. Sources of return in global investing.Journal of Portfolio ManagementHigh-Dimensional Covariance Estimation, 31(2):12{21, 2005.. Wiley, 2013.
L.B. Pulley. A general mean-variance approximation to expected utility for16(3):361{363, 1981.short holding periods.The Journal of Financial and Quantitative Analysis,
E. E. Qian, R. H. Hua, and E. H. Sorensen.Ethan Ratli-Crain, Colin M. Van Oort, James Bagrow, Matthew T. K. Koehler,Management. Chapman & Hall/CRC, 2007. Quantitative Equity Portfolio

A. C. Rencher and W. F. Christensen.and Brian F. Tivnan. Revisiting stylized facts for modern stock markets,2023. Methods of multivariate analysis. Wiley,
C. P. Robert.2012. The Bayesian Choice. Springer, 2nd edition, 2007.
R. Roll. A simple implicit measure of the eective bid-ask spread in an ecientJ. P. Romano and M. Wolf. Stepwise multiple testing as formalized datamarket.Journal of Finance, 39(4):1127{39, 1984.
S. A. Ross. The arbitrage theory of capital asset pricing.Theorysnooping., 13(3):341{360, 1976.Econometrica, 73(4):1237{1282, 2005. Journal of Economic


S. M. Ross.D. Ruppert and D. S. Matteson.2023. Introduction to Probability ModelsStatistics and Data Analysis for Financial. Academic Press, 13th edition,
A. Saxena and R. A. Stubbs. The alpha alignment factor: a solution to theEngineeringunderestimation of risk for optimized active portfolios.. Springer, 2nd edition, 2015. Journal of Risk, 15
M. Scholes and J. Williams. Estimating beta from nonsynchronous data.(3):3{37, 2013.of Financial Economics, 5(3):309{327, 1977. Journal
W. F. Sharpe. Capital asset prices: A theory of market equilibrium underW. F. Sharpe. The valuation of risk assets and the selection of risky investmentsconditions of risk.Journal of Finance, 19(3):425{442, 1964.

W. F. Sharpe. Equilibrium in a capital asset market.in stock portfolios and capital budgets.47(1):13{37, 1965. Review of Economics and StatisticsEconometrica, 34(4):,
D. Shen, H. Shen, H. Zhu, and J. S. Marron. The statistics and mathematics of768{783, 1966.high dimension low sample size asymptotics.Statistica Sinica, 26:1747{1770,
Peter G. Shephard. Second order risk, 2009.2016.
R. H. Shumway and D. S. Stoer.Springer, 2011. Time Series Analysis and Its Applications.


D. Simon.D. Skillicorn.Wiley, 2006.Optimal State Estimation: Kalman,Understanding Complex Datasets: Data Mining with MatrixH 1 , and Nonlinear Approaches.
W. Stevens.DecompositionsThe Collected Poems. Chapman & Hall/CRC, 2007.. Vintage, 1990.
J. H. Stock and W. M. Watson.Vector Autoregressions, and Structural Vector Autoregressions in Macroeco-nomics, volume 2A, chapter 8, pages 415{525. 2016.Dynamic Factor Models, Factor-Augmented
G. Strang.R. A. Stubbs and P. Vance. Computing return estimation error matrices forPress, 2019.Linear Algebra and Learning from Data. Wellesley - Cambridge
S. Suzuki.robust optimization. Technical Report 1, Axioma Research Paper, 2005.Zen Mind, Beginner's Mind. Weatherhill, 1970.
S. J. Taylor.S. J. Taylor.University Press, 2007.Modelling Financial Time SeriesAsset Price Dynamics, Volatility, and Prediction. Wiley, 1986.. Princeton
T. Terasvirta. An introduction to univariateTime SeriesR. A. Davis, J.-P. Kreiss, and T. Mikosch, editors,, pages 17{42. Springer, 2009a.GARCHmodels. In T. G. Andersen,Handbook of Financial
T. Terasvirta. MultivariateJ.-P. Kreiss, and T. Mikosch, editors,Springer, 2009b. GARCHmodels. In T. G. Andersen, R. A. Davis,Handbook of Financial Time Series.


E. O. Thorp. The kelly criterion in blackjack sports betting, and the stockliability managementmarket. In S.A. Zenios and W. Ziemba, editors,, volume 1. Elsevier, 2006. Handbook of asset and
M. E. Tipping and C. M. Bishop. Probabilistic principal component analysis.L. Trefethen and D. Bau.Journal of the Royal Statistical Society Series BNumerical linear algebra, 61(3):611{622, 1999.. SIAM, 1997.
R. S. Tsay.A. DeMiguel V., Martin-Utrera, and F.J. Nogales. Size matters: Optimalcalibration of shrinkage estimators for portfolio selection.Analysis of nancial time series. Wiley, 3rd edition, 2010.Journal of Banking
N. Vause. Counterparty risk and contract volumes in the credit default swapand Financemarket.BIS Quarterly Review, 37(8):3018{3034, 2013., 2010.
R. Velu, M. Hardy, and D. Nehren.R. Vershinin.Strategies. CRC Press, 2020.High-dimensional probabilityAlgorithmic Trading and Quantitative. Cambridge University Press, 2018.
G. Wahba. A least squares estimate of satellite attitude.S. Wang, Y. Luo, M.-A Alvarez, J. Jussa, A. Wang, and G. Rohal. Seven sins384, 1965. SIAM Review, 7(3):
W. Wang and J. Fan. Asymptotics of empirical eigenstructure for high dimen-of quantitative investing. Technical report, Deutsche Bank, 2014.sional spiked covariance.Annals of Statistics, 45(3):1342{1374, 2017.
L. Wasserman.All of Statistics. Springer, 2004. 452


K. T. Webster.P. Whittle.2023. Optimal Control. Basics and BeyondHandbook of Price Impact Modeling. Wiley, 1996.. Chapman & Hall/CRC,
T. Wiest. Momentum: what do we know 30 years after jegadeesh and titman'sseminal paper?2023. Financial Markets and Portfolio Management, 37:95{114,
J. Yao, S. Zheng, and Z. Bai.L. Zhang, P. A. Mykland, and Y. At-Sahalia. A tale of two time scales:Dimensional Data Analysis. Cambridge University Press, 2015.Large Sample Covariance Matrices and High-

E. Zivot. Practical issues in the analysis of univariate garch models. In T. G.the American Statistical Associationdetermining integrated volatility with noisy high-frequency data., 100(472):1394{1411, 2005. Journal of
E. Zivot and J. Wang.Financial Time SeriesAndersen, R. A. Davis, J.-P. Kreiss, and T. Mikosch, editors,Modeling Financial Time Series with S-Plus, pages 113{155. Springer, 2009. Handbook of. Springer,
2003.


IndexR (^2) ,seeCoecient of Determination
Active Managers, 16Aggregational Gaussianity, 39Akaike Information Criterion (AIC), 156Alpha, 76, 96Intraday, 402Orthogonal, 82, 279, 363
Alternate Trading System, 340American Depositary Receipt (ADR), 228Arbitrageurs, 18Asset Allocators, 17Assets Under Management, 27Spanned, 81, 271, 279, 363
AUM,AutocorrelationBacktestingAbsolute univariate returns, 39Univariate Returns, 37seeAssets Under Management
Cross-Validation, 130Protocol, 123Rademacher Anti-Serum (against back-Walk Forward, 130Walk-Foward, 128testing bites), 130
Bayesian Information Criterion, 156Beginner's Mind, xixBeta, 93BetasBid-Ask Spread, 34Adjusted-Dollar, 412
Bloomberg, 12Bonds, 7Book-to-Price Ratio, 277Broker-Dealers, 15Brokers, 12, 13Buy Side, 11, 15
CA,Cantelli's inequality, 287Capital Asset Pricing Model, 287CAPM,Cash Equivalents, 17CDS,seeseeseeClosing AuctionCredit Default SwapsCapital Asset Pricing Model
Characteristics, 24Child Order, 340CHM,Clearing, 13Closing Auction, 160seeelsConditional Heteroscedastic Mod-
Clustering
Coecient of Determination, 155, 283Complementary slackness conditions, 295Conditional Heteroscedastic Models, 41Constrained Regression, 170ConstraintK-Means, 237
constraintLong-Only, 312Market Beta, 314on Volatility, 263Portfolio Turnover, 314Tracking Error, 315
Constraint Qualication, 294ConstraintsConsumer Price Index, 24CorrelationPricing Out, 266Quadratic, 314
Cosine Similarity, 232, 245Covariance Matrix, 2Credit Default Swaps, 8Thresholding, 182Autocorrelation Correction, 178Empirical, 95
Cross-Sectional Empirical Average, 426Cross-Sectional Empirical Covariance, 426Cross-Validation, 124CurrencyBase, 199Quote, 199
Dark Pools, 11DataData Leakage, 118, 119Categorical, 162Structured, 25Unstructured, 25
DatasetDealers, 11Dealerweb, 12Training, 124Validation, 124Inventory, 12
Degrees of Freedom, 156Deleveraging Spirals, 21Diversication, 419Dividend, 31Dual Traders,Duality seeBroker-Dealers
454 Strong, 294Weak, 294


Ecient Market, 19Eigenfactors, 210EigenvaluesBulk, 218Concentration, 229Spike, 218
Eigenvectors, 210Equities, 7Estimation Universe, 161Estimation universe, 163ETF,EWMA,seeseeExchange-Traded FundsExponentially Weighted Mov-
Exchange Rate, 199Exchange-Traded Funds, 7Exchanges, 9Exponentially Weighted Moving Average,Indirect, 199ing Average
ExposureFactorto Factors, 90to Systematic Risk, 26^55
Country, 86Intercept, 86Mimicking-Portfolios, 302Orthogonalized, 273Returns, 74Unpriced, 364
Factor Model, 74Approximate, 75as a superposition of loadings, 79Characteristic, 97, 159Currency Rebasing, 199Denition, 74
Graphical Model, 78Idiosyncratic Component, 75Interpretations, 76Linking Local Models, 191Local, 192Macroeconomic, 97
Projections, 87Pushout, 88, 273Rotation, 84, 208Rotational Indeterminacy, 85Statistical, 97, 205Strict, 75
Feasible region, 293First Order Necessary Conditions, 265Systematic Component, 75Transformations, 76Types, 97Uses, 76
Flow predictability, 21FONC,Fractional Kelly Strategy, 390, 394tionsseeFirst Order Necessary Condi-

```
Frisch-Vaugh Lovell, 274Frisch-Waugh-Lovell Theorem, 105, 273Front-Running, 15, 22Fundamental Law of Active Management,Futures, 7 282
GARCH models, 41{43, 46General Autoregressive Conditional Het-Global Depositary Receipt (GDR), 228GMV,Graphical model, 76see alsoeroskedastic,Gross Market ValueseeGARCH models
Gross Market Value, 27Hat Matrix, 101, 106Heavy tails, 37Hedge Funds, 17Hedging, 26
Herndahl Index, 370, 420Heteroskedastic noise, 103HFT,High-Frequency Trader, 401Shrinkage Factor, 367see alsoHigh-Frequency Trader
Idempotent Operator, 88iid rv, 3IndexIndex Huggers, 17Rebalancing, 22Reconstition, 22
Information Coecient, 127, 130, 281Information Ratio, 283, 284, 418, 425Information Set, 19Interest Rate Swaps, 8IR,Empirical, 424seeInformation Ratio
IRS,Kalman Filter, 36, 56, 62Karush-Kuhn-Tucker conditions, 295Kelly Criterion, 262, 378Optimal Gain, 66seeInterest Rate Swaps
Kolmogorov-Smirnov distance, 46Lagrange multiplier, 266Lagrange multipliers, 293Lagrangian, 293Ledoit-Wolfe Shrinkage, 174, 185
Leverage, 27Leverage Eect, 39Likelihood, 100Limit-Order Book, 9, 34, 160Linear Regression, 98, 273As Projection, 101
455 Decomposition, 104Features, 100Frisch-Waugh-Lovell Theorem, 105
```

Linear State-Space Models, 30, 56, 60Liquidity, 8, 20LoadingsRandom Design, 165Denition, 74Orthonormal, 85
LOB,Mahalanobis distance, 151Market Eciency, 19Z-scored, 85Z-scoring, 85seeLimit-Order Book
Market Impact, 25, 338Market Makers, 12Market orders, 12Marketable Order, 341Maximum Likelihood Estimator, 47, 51Mean-Variance Optimization, 272
Meta-Order,MIFID II, 14MLE,Moore-Penrose Pseudoinvers, 2MSE, 145seeMaximum Likelihood Estimatorsee alsoParent Order
Net Market Value, 32Newey-West Estimator, 178, 193NMV,NormpFrobenius, 207-Norm, 2seeNet Market Value
Numeraire, 30, 80OptimizationOperator, 3, 327Unitarily Invariant, 207Mean-Variance, 262, 391
Orthogonal Complement, 104OTC,Over-the-Counter, 10, 340Parent Order, 340Partial Correlation, 269seeOver-the-Counter
Participation Rate, 342Passive Investing, 22Payment for Order Flow, 15, 19PCApd, 3K-Means, 237
Performance AttribitionPerformance AttributionMaximalMaximal, 408Portfolio-Based, 412As Conditional Expectation, 411
Selection-Sizing, 417As Model Rotation, 412Cross-Sectional, 410Nested, 417

```
Permanent Market Impact, 339PFOF,PnL, 26, 31Time Series, 400Position, 401Trading, 401seePayment for Order Flow
Portfolio, 31basis, 147Characteristic, 277Construction, 76Eigenportfolios, 147Factor-Mimicking, 153, 154, 167, 173,
Portfolio Management, 94From Sorts, 277Market, 154Production, 146Thematic, 154270, 271, 279, 301, 302, 362, 403
POV,Precision Matrix, 96, 266PricePrice Discovery, 18, 402Ask, 12Bid, 12seeParticipation Rate
Principal Component, 208, 210Principal Component Analysis, 208, 248Principal Trading Firms, 17ProductScalar, 3Hadamard, 3, 426
Projection, 101Projection Matrix, 101Projections, 88Publicly Available Information, 20QLIKE, 145
Quasi-Likelihood,R Squared,Rademacher Complexity, 132Random Recursive Equations, 46, 47tionseeCoecient of Determina-seeQLIKE
Random VariablesRegression, 239Heavy-Tailed, 40, 41, 44iid, 41, 43, 46, 47, 50, 53, 55, 58Cross-Sectional, 165Ordinary Least Squares, 100
Return, 31Returns, 30, 285Weighted Least Squares, 104, 166, 173Dividend-Adjusted, 31Excess, 113Compounding, 33
Excess, 31Idiosyncratic, 74, 75, 89, 97Logarithmic, 33Risk-Free, 31, 74
```

Riccati EquationRisk, 20, 25Stylized Facts, 37Discrete Time Algebraic, 66Recursion Formula, 66Marginal Contribution, 93
Risk ModelRisk-Free Rate, 31RREs,rv, 3Integrated, 234seeRandom Recursive Equations
Scalar Product, 212Scree plot, 227Secured Overnight Financing Rate, 32Secured Overnight Lending Rate, 14Securities, 7Sell Side, 11
Settlement, 13Shadow Price, 266, 318Sharpe Ratio, 50, 263{265, 268, 284, 286,Condence Interval, 290Dimensions, 289 384
Short-Term Factor Updating, 180Short-Term Idio Updating, 180Shrinkage, 196, 222Signal, 26Eciency (SRE), 326Sensitivity, 94
Singular Value Decomposition, 85, 108,Singular Values, 207SkillSkill vs. Luck, 76Selection, 419112, 207, 248, 326
Slippage,Smart Beta, 97SOFR,Spiked Covariance Model, 217Spread, 12RateseeseeSecured Overnight FinancingTemporary Market Impact
Spread Cost, 339STFU, seealso Short-Term Factor Updat-Strategy130/30, 313Capacity, 288ing176
Studentization,Subsampling, 51SubspaceLong-Only, 312Column, 239Similarity Between Two Subspaces, 234seeZ-scoring
SVD,TailSpanned by eigenvectors, 222seeSingular Value Decomposition

```
Temporary Market Impact, 339Time series, 24Tracking Error, 315tracking volatility, 311GARCH(1, 1) processes, 44Gaussian, 40
TradingTrading CostInformational Eect, 338Mimetic Eect, 339Strategy, 339Single-Period, 314
Turnover, 152Eigenvectors, 232Linear, 232Model, 153Quadratic, 232
Vanilla Options, 8Volatility, 285Unintended Bets, 400Utility Theory, 261Ex Ante, 91
Wahba's Problem, 235Win-Loss Ratio, 387Winning Skew, 387Realized (RV), 49Short-Term Factor Updating, 175
Wirehouses,Woodbury-Sherman-Morrison Lemma, 303, 372 seeBroker-Dealers
```


IndexR (^2) ,seeCoecient of Determination
Active Managers, 16Aggregational Gaussianity, 39Akaike Information Criterion (AIC), 156Alpha, 76, 96Intraday, 402Orthogonal, 82, 279, 363
Alternate Trading System, 340American Depositary Receipt (ADR), 228Arbitrageurs, 18Asset Allocators, 17Assets Under Management, 27Spanned, 81, 271, 279, 363
AUM,AutocorrelationBacktestingAbsolute univariate returns, 39Univariate Returns, 37seeAssets Under Management
Cross-Validation, 130Protocol, 123Rademacher Anti-Serum (against back-Walk Forward, 130Walk-Foward, 128testing bites), 130
Bayesian Information Criterion, 156Beginner's Mind, xixBeta, 93BetasBid-Ask Spread, 34Adjusted-Dollar, 412
Bloomberg, 12Bonds, 7Book-to-Price Ratio, 277Broker-Dealers, 15Brokers, 12, 13Buy Side, 11, 15
CA,Cantelli's inequality, 287Capital Asset Pricing Model, 287CAPM,Cash Equivalents, 17CDS,seeseeseeClosing AuctionCredit Default SwapsCapital Asset Pricing Model
Characteristics, 24Child Order, 340CHM,Clearing, 13Closing Auction, 160seeelsConditional Heteroscedastic Mod-
Clustering
Coecient of Determination, 155, 283Complementary slackness conditions, 295Conditional Heteroscedastic Models, 41Constrained Regression, 170ConstraintK-Means, 237
constraintLong-Only, 312Market Beta, 314on Volatility, 263Portfolio Turnover, 314Tracking Error, 315
Constraint Qualication, 294ConstraintsConsumer Price Index, 24CorrelationPricing Out, 266Quadratic, 314
Cosine Similarity, 232, 245Covariance Matrix, 2Credit Default Swaps, 8Thresholding, 182Autocorrelation Correction, 178Empirical, 95
Cross-Sectional Empirical Average, 426Cross-Sectional Empirical Covariance, 426Cross-Validation, 124CurrencyBase, 199Quote, 199
Dark Pools, 11DataData Leakage, 118, 119Categorical, 162Structured, 25Unstructured, 25
DatasetDealers, 11Dealerweb, 12Training, 124Validation, 124Inventory, 12
Degrees of Freedom, 156Deleveraging Spirals, 21Diversication, 419Dividend, 31Dual Traders,Duality seeBroker-Dealers
459 Strong, 294Weak, 294


Ecient Market, 19Eigenfactors, 210EigenvaluesBulk, 218Concentration, 229Spike, 218
Eigenvectors, 210Equities, 7Estimation Universe, 161Estimation universe, 163ETF,EWMA,seeseeExchange-Traded FundsExponentially Weighted Mov-
Exchange Rate, 199Exchange-Traded Funds, 7Exchanges, 9Exponentially Weighted Moving Average,Indirect, 199ing Average
ExposureFactorto Factors, 90to Systematic Risk, 26^55
Country, 86Intercept, 86Mimicking-Portfolios, 302Orthogonalized, 273Returns, 74Unpriced, 364
Factor Model, 74Approximate, 75as a superposition of loadings, 79Characteristic, 97, 159Currency Rebasing, 199Denition, 74
Graphical Model, 78Idiosyncratic Component, 75Interpretations, 76Linking Local Models, 191Local, 192Macroeconomic, 97
Projections, 87Pushout, 88, 273Rotation, 84, 208Rotational Indeterminacy, 85Statistical, 97, 205Strict, 75
Feasible region, 293First Order Necessary Conditions, 265Systematic Component, 75Transformations, 76Types, 97Uses, 76
Flow predictability, 21FONC,Fractional Kelly Strategy, 390, 394tionsseeFirst Order Necessary Condi-

```
Frisch-Vaugh Lovell, 274Frisch-Waugh-Lovell Theorem, 105, 273Front-Running, 15, 22Fundamental Law of Active Management,Futures, 7 282
GARCH models, 41{43, 46General Autoregressive Conditional Het-Global Depositary Receipt (GDR), 228GMV,Graphical model, 76see alsoeroskedastic,Gross Market ValueseeGARCH models
Gross Market Value, 27Hat Matrix, 101, 106Heavy tails, 37Hedge Funds, 17Hedging, 26
Herndahl Index, 370, 420Heteroskedastic noise, 103HFT,High-Frequency Trader, 401Shrinkage Factor, 367see alsoHigh-Frequency Trader
Idempotent Operator, 88iid rv, 3IndexIndex Huggers, 17Rebalancing, 22Reconstition, 22
Information Coecient, 127, 130, 281Information Ratio, 283, 284, 418, 425Information Set, 19Interest Rate Swaps, 8IR,Empirical, 424seeInformation Ratio
IRS,Kalman Filter, 36, 56, 62Karush-Kuhn-Tucker conditions, 295Kelly Criterion, 262, 378Optimal Gain, 66seeInterest Rate Swaps
Kolmogorov-Smirnov distance, 46Lagrange multiplier, 266Lagrange multipliers, 293Lagrangian, 293Ledoit-Wolfe Shrinkage, 174, 185
Leverage, 27Leverage Eect, 39Likelihood, 100Limit-Order Book, 9, 34, 160Linear Regression, 98, 273As Projection, 101
460 Decomposition, 104Features, 100Frisch-Waugh-Lovell Theorem, 105
```

Linear State-Space Models, 30, 56, 60Liquidity, 8, 20LoadingsRandom Design, 165Denition, 74Orthonormal, 85
LOB,Mahalanobis distance, 151Market Eciency, 19Z-scored, 85Z-scoring, 85seeLimit-Order Book
Market Impact, 25, 338Market Makers, 12Market orders, 12Marketable Order, 341Maximum Likelihood Estimator, 47, 51Mean-Variance Optimization, 272
Meta-Order,MIFID II, 14MLE,Moore-Penrose Pseudoinvers, 2MSE, 145seeMaximum Likelihood Estimatorsee alsoParent Order
Net Market Value, 32Newey-West Estimator, 178, 193NMV,NormpFrobenius, 207-Norm, 2seeNet Market Value
Numeraire, 30, 80OptimizationOperator, 3, 327Unitarily Invariant, 207Mean-Variance, 262, 391
Orthogonal Complement, 104OTC,Over-the-Counter, 10, 340Parent Order, 340Partial Correlation, 269seeOver-the-Counter
Participation Rate, 342Passive Investing, 22Payment for Order Flow, 15, 19PCApd, 3K-Means, 237
Performance AttribitionPerformance AttributionMaximalMaximal, 408Portfolio-Based, 412As Conditional Expectation, 411
Selection-Sizing, 417As Model Rotation, 412Cross-Sectional, 410Nested, 417

```
Permanent Market Impact, 339PFOF,PnL, 26, 31Time Series, 400Position, 401Trading, 401seePayment for Order Flow
Portfolio, 31basis, 147Characteristic, 277Construction, 76Eigenportfolios, 147Factor-Mimicking, 153, 154, 167, 173,
Portfolio Management, 94From Sorts, 277Market, 154Production, 146Thematic, 154270, 271, 279, 301, 302, 362, 403
POV,Precision Matrix, 96, 266PricePrice Discovery, 18, 402Ask, 12Bid, 12seeParticipation Rate
Principal Component, 208, 210Principal Component Analysis, 208, 248Principal Trading Firms, 17ProductScalar, 3Hadamard, 3, 426
Projection, 101Projection Matrix, 101Projections, 88Publicly Available Information, 20QLIKE, 145
Quasi-Likelihood,R Squared,Rademacher Complexity, 132Random Recursive Equations, 46, 47tionseeCoecient of Determina-seeQLIKE
Random VariablesRegression, 239Heavy-Tailed, 40, 41, 44iid, 41, 43, 46, 47, 50, 53, 55, 58Cross-Sectional, 165Ordinary Least Squares, 100
Return, 31Returns, 30, 285Weighted Least Squares, 104, 166, 173Dividend-Adjusted, 31Excess, 113Compounding, 33
Excess, 31Idiosyncratic, 74, 75, 89, 97Logarithmic, 33Risk-Free, 31, 74
```

Riccati EquationRisk, 20, 25Stylized Facts, 37Discrete Time Algebraic, 66Recursion Formula, 66Marginal Contribution, 93
Risk ModelRisk-Free Rate, 31RREs,rv, 3Integrated, 234seeRandom Recursive Equations
Scalar Product, 212Scree plot, 227Secured Overnight Financing Rate, 32Secured Overnight Lending Rate, 14Securities, 7Sell Side, 11
Settlement, 13Shadow Price, 266, 318Sharpe Ratio, 50, 263{265, 268, 284, 286,Condence Interval, 290Dimensions, 289 384
Short-Term Factor Updating, 180Short-Term Idio Updating, 180Shrinkage, 196, 222Signal, 26Eciency (SRE), 326Sensitivity, 94
Singular Value Decomposition, 85, 108,Singular Values, 207SkillSkill vs. Luck, 76Selection, 419112, 207, 248, 326
Slippage,Smart Beta, 97SOFR,Spiked Covariance Model, 217Spread, 12RateseeseeSecured Overnight FinancingTemporary Market Impact
Spread Cost, 339STFU, seealso Short-Term Factor Updat-Strategy130/30, 313Capacity, 288ing176
Studentization,Subsampling, 51SubspaceLong-Only, 312Column, 239Similarity Between Two Subspaces, 234seeZ-scoring
SVD,TailSpanned by eigenvectors, 222seeSingular Value Decomposition

```
Temporary Market Impact, 339Time series, 24Tracking Error, 315tracking volatility, 311GARCH(1, 1) processes, 44Gaussian, 40
TradingTrading CostInformational Eect, 338Mimetic Eect, 339Strategy, 339Single-Period, 314
Turnover, 152Eigenvectors, 232Linear, 232Model, 153Quadratic, 232
Vanilla Options, 8Volatility, 285Unintended Bets, 400Utility Theory, 261Ex Ante, 91
Wahba's Problem, 235Win-Loss Ratio, 387Winning Skew, 387Realized (RV), 49Short-Term Factor Updating, 175
Wirehouses,Woodbury-Sherman-Morrison Lemma, 303, 372 seeBroker-Dealers
```

