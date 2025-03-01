## Contents

- 1 Introduction
- 2 Denoising and Detoning
- 3 Distance Metrics
- 4 Optimal Clustering
- 5 Financial Labels
- 6 Feature Importance Analysis
- 7 Portfolio Construction
- 8 Testing Set Overfitting
   - Appendix A: Testing on Synthetic Data
   - Appendix B: Proof of the“False Strategy”Theorem
   - Bibliography
   - References


## 1 Introduction

## 1.1 Motivation

To a greater extent than other mathematical disciplines, statistics is a product
of its time. If Francis Galton, Karl Pearson, Ronald Fisher, and Jerzy Neyman
had had access to computers, they may have created an entirely different
field. Classical statistics relies on simplistic assumptions (linearity, indepen-
dence), in-sample analysis, analytical solutions, and asymptotic properties
partly because its founders had access to limited computing power. Today,
many of these legacy methods continue to be taught at university courses and
in professional certification programs, even though computational methods,
such as cross-validation, ensemble estimators, regularization, bootstrapping,
and Monte Carlo, deliver demonstrably better solutions. In the words of
Efron and Hastie (2016,53),

```
two words explain the classic preference for parametric models: mathema-
tical tractability. In a world of sliderules and slow mechanical arithmetic,
mathematical formulation, by necessity, becomes the computational tool of
choice. Our new computation-rich environment has unplugged the mathe-
matical bottleneck, giving us a more realistic,flexible, and far-reaching body
of statistical techniques.
```
Financial problems pose a particular challenge to those legacy methods,
because economic systems exhibit a degree of complexity that is beyond the
grasp of classical statistical tools (López de Prado 2019b). As a consequence,
machine learning (ML) plays an increasingly important role infinance. Only a
few years ago, it was rare tofind ML applications outside short-term price
prediction, trade execution, and setting of credit ratings. Today, it is hard tofind
a use case where ML is not being deployed in some form. This trend is unlikely
to change, as larger data sets, greater computing power, and more efficient
algorithms all conspire to unleash a golden age offinancial ML. The ML
revolution creates opportunities for dynamicfirms and challenges for anti-
quated asset managers. Firms that resist this revolution will likely share
Kodak’s fate. One motivation of this Element is to demonstrate how modern
statistical tools help address many of the deficiencies of classical techniques in
the context of asset management.
Most ML algorithms were originally devised for cross-sectional data sets. This
limits their direct applicability tofinancial problems, where modeling the time
series properties of data sets is essential. My previous book,Advances in Financial
Machine Learning(AFML;López de Prado 2018a), addressed the challenge of
modeling the time series properties offinancial data sets with ML algorithms, from
the perspective of an academic who also happens to be a practitioner.

```
Elements in Quantitative Finance 1
```

Machine Learning for Asset Managersis concerned with answering a differ-
ent challenge: how can we use ML to build betterfinancial theories? This is not
a philosophical or rhetorical question. Whatever edge you aspire to gain in
finance, it can only be justified in terms of someone else making a systematic
mistake from which you benefit.^1 Without a testable theory that explains your
edge, the odds are that you do not have an edge at all. A historical simulation of
an investment strategy’s performance (backtest) is not a theory; it is a (likely
unrealistic) simulation of a past that never happened (you did not deploy that
strategy years ago; that is why you are backtesting it!). Only a theory can pin
down the clear cause–effect mechanism that allows you to extract profits against
the collective wisdom of the crowds–a testable theory that explains factual
evidence as well as counterfactual cases (ximpliesy, and the absence ofy
implies the absence ofx). Asset managers should focus their efforts on research-
ing theories, not backtesting trading rules. ML is a powerful tool for building
financial theories, and the main goal of this Element is to introduce you to
essential techniques that you will need in your endeavor.

## 1.2 Theory Matters

A black swan is typically defined as an extreme event that has not been observed
before. Someone once told me that quantitative investment strategies are use-
less. Puzzled, I asked why. He replied,“Because the future isfilled with black
swans, and since historical data sets by definition cannot contain never-seen-
before events, ML algorithms cannot be trained to predict them.”I counter-
argued that, in many cases, black swans have been predicted.
Let me explain this apparent paradox with an anecdote. Back in the year
2010, I was head of high-frequency futures at a large US hedge fund. On May 6,
we were running our liquidity provision algorithms as usual, when around 12:
ET, many of them started toflatten their positions automatically. We did not
interfere or override the systems, so within minutes, our market exposure
became very small. This system behavior had never happened to us before.
My team and I were conducting a forensic analysis of what had caused the
systems to shut themselves down when, at around 14:30 ET, we saw the S&P
500 plunge, within minutes, almost 10% relative to the open. Shortly after, the
systems started to buy aggressively, profiting from a 5% rally into the market
close. The press dubbed this black swan the“flash crash.”We were twice
surprised by this episode:first, we could not understand how our systems

(^1) This is also true in the context of factor investing, where the systematic mistake can be explained
in terms of behavioral bias, mismatched investment horizons, risk tolerance, regulatory con-
straints, and other variables informing investors’decisions.
2 Machine Learning for Asset Managers


predicted an event that we, the developers, did not anticipate; second, we could
not understand why our systems started to buy shortly after the market bottomed.
Aboutfive months later, an official investigation found that the crash was
likely caused by an order to sell 75,000 E-mini S&P 500 futures contracts at a
high participation rate (CFTC 2010). That large order contributed to a persistent
imbalance in the orderflow, making it very difficult for market makers toflip
their inventory without incurring losses. This toxic orderflow triggered stop-out
limits across market makers, who ceased to provide liquidity. Market makers
became aggressive liquidity takers, and without anyone remaining on the bid,
the market inevitably collapsed (Easley et al. 2011).
We could not have forecasted theflash crash by watching CNBC or reading the
Wall Street Journal. To most observers, theflash crash was indeed an unpredictable
black swan. However, the underlying causes of theflash crash are very common.
Orderflow is almost never perfectly balanced. In fact, imbalanced orderflow is the
norm, with various degrees of persistency (e.g., measured in terms of serial correla-
tion). Our systems had been trained to reduce positions under extreme conditions of
orderflow imbalance. In doing so, they were trained to avoid the conditions that
shortly after caused the black swan. Once the market collapsed, our systems
recognized that the opportunity to buy at a 10% discount offset previous concerns
from extreme orderflow imbalance, and they took long positions until the close. This
experience illustrates the two most important lessons contained in this Element.

```
1.2.1 Lesson 1: You Need a Theory
```
Contrary to popular belief, backtesting is not a research tool. Backtests can never
prove that a strategy is a true positive, and they may only provide evidence that a
strategy is a false positive. Never develop a strategy solely through backtests.
Strategies must be supported by theory, not historical simulations. Your theories
must be general enough to explain particular cases, even if those cases are black
swans. The existence of black holes was predicted by the theory of general relativity
more thanfive decades before thefirst black hole was observed. In the above story,
our market microstructure theory (which later on became known as the VPIN
theory; seeEasley et al. 2011b) helped us predict and profit from a black swan. Not
only that, but our theoretical work also contributed to the market’s bounce back (my
colleagues used to joke that we helped put the“flash”into the“flash crash”). This
Element contains some of the tools you need to discover your own theories.

```
1.2.2 Lesson 2: ML Helps Discover Theories
```
Consider the following approach to discovering newfinancial theories. First,
you apply ML tools to uncover the hidden variables involved in a complex

```
Elements in Quantitative Finance 3
```

phenomenon. These are the ingredients that the theory must incorporate in
order to make successful forecasts. The ML tools have identified these
ingredients; however, they do not directly inform you about the exact equation
that binds the ingredients together. Second, we formulate a theory that con-
nects these ingredients through a structural statement. This structural
statement is essentially a system of equations that hypothesizes a particular
cause–effect mechanism. Third, the theory has a wide range of testable
implications that go beyond the observations predicted by the ML tools in
the first step.^2 A successful theory will predict events out-of-sample.
Moreover, it will explain not only positives (xcausesy) but also negatives
(the absence ofyis due to the absence ofx).
In the above discovery process, ML plays the key role of decoupling the
search for variables from the search for specification. Economic theories are
often criticized for being based on“facts with unknown truth value”(Romer
2016) and“generally phony” assumptions (Solow 2010). Considering the
complexity of modernfinancial systems, it is unlikely that a researcher will be
able to uncover the ingredients of a theory by visual inspection of the data or by
running a few regressions. Classical statistical methods do not allow this
decoupling of the two searches.
Once the theory has been tested, it stands on its own feet. In this way, the
theory, not the ML algorithm, makes the predictions. In the above anecdote, the
theory, not an online forecast produced by an autonomous ML algorithm, shut
the position down. The forecast was theoretically sound, and it was not based on
some undefined pattern. It is true that the theory could not have been discovered
without the help of ML techniques, but once the theory was discovered, the ML
algorithm played no role in the decision to close the positions two hours prior to
theflash crash. The most insightful use of ML infinance is for discovering
theories. You may use ML successfully for makingfinancial forecasts; however,
that is not necessarily the best scientific use of this technology (particularly if
your goal is to develop high-capacity investment strategies).

## 1.3 How Scientists Use ML

An ML algorithm learns complex patterns in a high-dimensional space with
little human guidance on model specification. That ML models need not be
specified by the researcher has led many to, erroneously, conclude that ML must

(^2) A theory can be tested with more powerful tools than backtests. For instance, we could investigate
which market makers lost money during theflash crash. Did they monitor for orderflow
imbalance? Did market makers that monitor for orderflow imbalance fare better? Can wefind
evidence of their earlier retreat in the FIX messages of that day? A historical simulation of a
trading rule cannot give us this level of insight.
4 Machine Learning for Asset Managers


be a black box. In that view, ML is merely an“oracle,”^3 a prediction machine
from which no understanding can be extracted. The black box view of ML is a
misconception. It is fueled by popular industrial applications of ML, where the
search for better predictions outweighs the need for theoretical understanding.
A review of recent scientific breakthroughs reveals radically different uses of
ML in science, including the following:

1 Existence:ML has been deployed to evaluate the plausibility of a theory
across all scientificfields, even beyond the empirical sciences. Notably, ML
algorithms have helped make mathematical discoveries. ML algorithms
cannot prove a theorem, however they can point to the existence of an
undiscovered theorem, which can then be conjectured and eventually proved.
In other words, if something can be predicted, there is hope that a mechanism
can be uncovered (Gryak et al., forthcoming).
2 Importance:ML algorithms can determine the relative informational con-
tent of explanatory variables (features, in ML parlance) for explanatory and/
or predictive purposes (Liu 2004). For example, the mean-decrease accuracy
(MDA) method follows these steps: (1) Fit a ML algorithm on a particular
data set; (2) derive the out-of-sample cross-validated accuracy; (3) repeat
step (2) after shuffling the time series of individual features or combinations
of features; (4) compute the decay in accuracy between (2) and (3). Shuffling
the time series of an important feature will cause a significant decay in
accuracy. Thus, although MDA does not uncover the underlying mechanism,
it discovers the variables that should be part of the theory.
3 Causation:ML algorithms are often utilized to evaluate causal inference
following these steps: (1) Fit a ML algorithm on historical data to predict
outcomes, absent of an effect. This model is nontheoretical, and it is purely
driven by data (like an oracle); (2) collect observations of outcomes under the
presence of the effect; (3) use the ML algorithmfit in (1) to predict the
observation collected in (2). The prediction error can be largely attributed to
the effect, and a theory of causation can be proposed (Varian 2014; Athey
2015 ).
4 Reductionist:ML techniques are essential for the visualization of large,
high-dimensional, complex data sets. For example, manifold learning algo-
rithms can cluster a large number of observations into a reduced subset of
peer groups, whose differentiating properties can then be analyzed (Schlecht
et al. 2008).

(^3) Here we use a common definition of oracle in complexity theory: a black box that is able to
produce a solution for any instance of a given computational problem.
Elements in Quantitative Finance 5


5 Retriever:ML is used to scan through big data in search of patterns that
humans failed to recognize. For instance, every night ML algorithms are fed
millions of images in search of supernovae. Once theyfind one image with a
high probability of containing a supernova, expensive telescopes can be
pointed to a particular region in the universe, where humans will scrutinize
the data (Lochner et al. 2016). A second example is outlier detection. Finding
outliers is a prediction problem rather than an explanation problem. A ML
algorithm can detect an anomalous observation, based on the complex
structure it has found in the data, even if that structure is not explained to
us ( Hodge and Austin 2004).

Rather than replacing theories, ML plays the critical role of helping scientists
form theories based on rich empirical evidence. Likewise, ML opens the
opportunity for economists to apply powerful data science tools toward the
development of sound theories.

## 1.4 Two Types of Overfitting

The dark side of ML’sflexibility is that, in inexperienced hands, these algo-
rithms can easily overfit the data. The primary symptom of overfitting is a
divergence between a model’s in-sample and out-of-sample performance
(known as the generalization error). We can distinguish between two types of
overfitting: the overfitting that occurs on the train set, and the overfitting that
occurs on the test set.Figure 1.1summarizes how ML deals with both kinds of
overfitting.

```
1.4.1 Train Set Overfitting
```
Train set overfitting results from choosing a specification that is soflexible that
it explains not only the signal, but also the noise. The problem with confounding
signal with noise is that noise is, by definition, unpredictable. An overfit model
will produce wrong predictions with an unwarranted confidence, which in turn
will lead to poor performance out-of-sample (or even in a pseudo-out-of-
sample, like in a backtest).
ML researchers are keenly aware of this problem, which they address in three
complementary ways. Thefirst approach to correct for train set overfitting is
evaluating the generalization error, through resampling techniques (such as
cross-validation) and Monte Carlo methods. Appendix A describes these
techniques and methods in greater detail. The second approach to reduce train
set overfitting is regularization methods, which prevent model complexity
unless it can be justified in terms of greater explanatory power. Model

6 Machine Learning for Asset Managers


**Overfitting**

```
Training set
```
```
Generalization
```
```
error
```
```
(synthetic dataset)
```
```
Ensemblemethods
```
```
Regularization
```
```
Testing set (backtestoverfitting)
```
```
Generalization
```
```
error
```
```
(synthetic dataset)
```
```
Report all trials
```
```
(number,variance)
```
```
Resampling
```
```
(...)
```
```
Monte Carlo
```
```
(...)
```
```
Number ofvariables (LASSO)
```
```
Structure
(early stopping,
```
```
drop-out)
```
```
DeflatedSharpe
Ratio / FWER
```
```
Resampling
```
```
(CPCV)
```
```
Monte Carlo
```
```
Figure
```
#### 1.

```
Solutions
```
```
to
```
```
two
```
```
kinds
```
```
of
```
```
over
```
```
fitting.
```

parsimonycan be enforcedby limitingthe numberof parameters(e.g.,LASSO)
or restrictingthe model’s structure(e.g.,earlystopping).The thirdapproachto
addresstrainset overfittingis ensembletechniques,whichreducethe variance
of the errorby combiningthe forecastsof a collectionof estimators.For
example,we can controlthe risk of overfittinga randomforeston a trainset
in at leastthreeways:(1) cross-validatingthe forecasts;(2) limitingthe depthof
eachtree;and (3) addingmoretrees.
In summary,a backtestmayhint at the occurrenceof trainset overfitting,
whichcan be remediedusingthe aboveapproaches.Unfortunately,backtests
are powerlessagainstthe secondtype of overfitting,as explainednext.

```
1.4.2Test Set Overfitting
```
Imaginethat a friendclaimsto havea techniqueto predictthe winningticketat
the nextlottery.His techniqueis not exact,so he mustbuy morethanone
ticket.Of course,if he buysall of the tickets,it is no surprisethat he will win.
Howmanyticketswouldyou allowhim to buy beforeconcludingthat his
methodis useless?To evaluatethe accuracyof his technique,you should
adjustfor the fact that he has boughtmultipletickets.Likewise,researchers
runningmultiplestatisticaltestson the samedata set are morelikelyto makea
falsediscovery.By applyingthe sametest on the samedata set multipletimes,
it is guaranteedthat eventuallya researcherwill makea falsediscovery.This
selectionbias comesfromfittingthe modelto performwell on the test set, not
the trainset.
Anotherexampleof test set overfittingoccurswhena researcherbacktestsa
strategyand she tweaksit untilthe outputachievesa targetperformance.That
backtest–tweak–backtestcycleis a futileexercisethat will inevitablyend with
an overfit strategy(a falsepositive).Instead,the researchershouldhavespent
her timeinvestigatinghowthe researchprocessmisledher into backtestinga
falsestrategy.In otherwords,a poorlyperformingbacktestis an opportunityto
fix the researchprocess, not an opportunitytofix a particularinvestment
strategy.
Mostpublisheddiscoveriesinfinanceare likelyfalse,due to test set over-
fitting.ML did not causethe currentcrisisinfinancialresearch(Harveyet al.
2016). Thatcrisiswas causedby the widespreadmisuseof classicalstatistical
methodsinfinance,andp-hackingin particular.ML can helpdealwiththe
problemof test set overfitting,in threeways.First,we can keeptrackof how
manyindependenttestsa researcherhas run, to evaluatethe probabilitythat at
leastone of the outcomesis a falsediscovery(knownas familywiseerrorrate, or
FWER).The deflated Sharperatio(Baileyand Lópezde Prado 2014 ) follows

8 MachineLearningfor AssetManagers


a similar approach in the context of backtesting, as explained inSection 8.It
is the equivalent to controlling for the number of lottery tickets that your
friend bought. Second, while it is easy to overfitamodeltoonetestset,itis
hard to overfit a model to thousands of test sets for each security. Those
thousands of test sets can be generated by resampling combinatorial splits of
train and test sets. This is the approached followed by the combinatorial
purged cross-validation method, or CPCV (AFML, chapter 12). Third, we
can use historical series to estimate the underlying data-generating process,
and sample synthetic data sets that match the statistical properties observed in
history. Monte Carlo methods are particularly powerful at producing syn-
thetic data sets that match the statistical properties of a historical series. The
conclusions from these tests are conditional to the representativeness of the
estimated data-generating process (AFML, chapter 13). The main advantage
of this approach is that those conclusions are not connected to a particular
(observed) realization of the data-generating process but to an entire distri-
bution of random realizations. Following with our example, this is equivalent
to replicating the lottery game and repeating it many times, so that we can rule
luck out.
In summary, there are multiple practical solutions to the problem of train set and
test set overfitting. These solutions are neither infallible nor incompatible, and my
advice is that you apply all of them. At the same time, I must insist that no backtest
can replace a theory, for at least two reasons: (1) backtests cannot simulate black
swans–only theories have the breadth and depth needed to consider the never-
before-seen occurrences; (2) backtests may insinuate that a strategy is profitable,
but they do not tell us why. They are not a controlled experiment. Only a theory
can state the cause–effect mechanism, and formulate a wide range of predictions
and implications that can be independently tested for facts and counterfacts. Some
of these implications may even be testable outside the realm of investing. For
example, the VPIN theory predicted that market makers would suffer stop-outs
under persistent orderflow imbalance. Beyond testing whether orderflow imbal-
ance causes a reduction in liquidity, researchers can also test whether market
makers suffered losses during theflash crash (hint: they did). This latter test can be
conducted by reviewingfinancial statements, independently from the evidence
contained in exchange records of prices and quotes.

## 1.5 Outline

This Element offers asset managers a step-by-step guide to buildingfinancial
theories with the help of ML methods. To that objective, each section uses what
we have learned in the previous ones. Each section (except for this introduction)

```
Elements in Quantitative Finance 9
```

contains an empirical analysis, where the methods explained are put to the test
in Monte Carlo experiments.
Thefirst step in building a theory is to collect data that illustrate how some
variables relate to each other. Infinancial settings, those data often take the
form of a covariance matrix. We use covariance matrices to run regressions,
optimize portfolios, manage risks, search for linkages, etc. However,financial
covariance matrices are notoriously noisy. A relatively small percentage of
the information they contain is signal, which is systematically suppressed by
arbitrage forces.Section 2explains how to denoise a covariance matrix
without giving up the little signal it contains. Most of the discussion centers
on random matrix theory, but at the core of the solution sits an ML technique:
the kernel density estimator.
Many research questions involve the notion of similarity or distance.
For example, we may be interested in understanding howcloselyrelated
two variables are. Denoised covariance matrices can be very useful
for deriving distance metrics from linear relationships. Modeling nonlinear
relationships requires more advanced concepts.Section 3provides an infor-
mation-theoretic framework for extracting complex signals from noisy data.
In particular, it allows us to define distance metrics with minimal assumptions
regarding the underlying variables that characterize the metric space. These
distance metrics can be thought of as a nonlinear generalization of the notion
of correlation.
One of the applications of distance matrices is to study whether some
variables are more closely related among themselves than to the rest, hence
forming clusters. Clustering has a wide range of applications acrossfinance,
like in asset class taxonomy, portfolio construction, dimensionality reduction,
or modeling networks of agents. A general problem in clustering isfinding
the optimal number of clusters.Section 4introduces the ONC algorithm,
which provides a general solution to this problem. Various use cases for this
algorithm are presented throughout this Element.
Clustering is an unsupervised learning problem. Before we can delve into
supervised learning problems, we need to assess ways of labelingfinancial data.
The effectiveness of a supervised ML algorithm greatly depends on the kind of
problem we attempt to solve. For example, it may be harder to forecast
tomorrow’s S&P 500 return than the sign of its next 5% move. Different
features are appropriate for different types of labels. Researchers should
consider carefully what labeling method they apply on their data.Section 5
discusses the merits of various alternatives.
AFML warned readers that backtesting is not a research tool. Feature impor-
tance is. A backtest cannot help us develop an economic orfinancial theory.

10 Machine Learning for Asset Managers


In order to do that, we need a deeper understanding of what variables are
involved in a phenomenon.Section 6studies ML tools for evaluating the
importance of explanatory variables, and explains how these tools defeat
many of the caveats of classical methods, such as thep-value. A particular
concern is how to overcomep-value’s lack of robustness under multicollinear-
ity. To tackle this problem, we must apply what we learned in all prior sections,
including denoising (Section 2), distance metrics (Section 3), clustering
(Section 4), and labeling (Section 5).
Once you have afinancial theory, you can use your discovery to develop an
investment strategy. Designing that strategy will require making some invest-
ment decisions under uncertainty. To that purpose, mean-variance portfolio
optimization methods are universally known and used, even though they are
notorious for their instability. Historically, this instability has been addressed in
a number of ways, such as introducing strong constraints, adding priors, shrink-
ing the covariance matrix, and other robust optimization techniques. Many asset
managers are familiar with instability caused by noise in the covariance matrix.
Fewer asset managers realize that certain data structures (types of signal) are
also a source of instability for mean-variance solutions.Section 7explains why
signal can be a source of instability, and how ML methods can help correct it.
Finally, afinancial ML book would not be complete without a detailed
treatment of how to evaluate the probability that your discovery is false, as a
result of test set overfitting.Section 8explains the dangers of backtest over-
fitting, and provides several practical solutions to the problem of selection bias
under multiple testing.

## 1.6 Audience

If, like most asset managers, you routinely compute covariance matrices, use
correlations, search for low-dimensional representations of high-dimensional
spaces, build predictive models, computep-values, solve mean-variance opti-
mizations, or apply the same test multiple times on a given data set, you need to
read this Element. In it, you will learn thatfinancial covariance matrices are
noisy and that they need to be cleaned before running regressions or computing
optimal portfolios (Section 2). You will learn that correlations measure a very
narrow definition of codependency and that various information-theoretic
metrics are more insightful (Section 3). You will learn intuitive ways of redu-
cing the dimensionality of a space, which do not involve a change of basis.
Unlike PCA, ML-based dimensionality reduction methods provide intuitive
results (Section 4). Rather than aiming for implausiblefixed-horizon predic-
tions, you will learn alternative ways of posingfinancial prediction problems
that can be solved with higher accuracy (Section 5). You will learn modern

```
Elements in Quantitative Finance 11
```

alternatives to the classicalp-values (Section 6). You will learn how to
address the instability problem that plagues mean-variance investment port-
folios (Section 7). And you will learn how to evaluate the probability that
your discovery is false as a result of multiple testing (Section 8). If you work
in the asset management industry or in academicfinance, this Element is
for you.

## 1.7 Five Popular Misconceptions about Financial ML

Financial ML is a new technology. As it is often the case with new technologies,
its introduction has inspired a number of misconceptions. Below is a selection
of the most popular.

```
1.7.1 ML Is the Holy Grail versus ML Is Useless
```
The amount of hype and counterhype surrounding ML defies logic. Hype
creates a set of expectations that may not be fulfilled for the foreseeable future.
Counterhype attempts to convince audiences that there is nothing special about
ML and that classical statistical methods already produce the results that ML-
enthusiasts claim.
ML critics sometimes argue that“caveat X in linear regression is no big
deal,”where X can either mean model misspecification, multicollinearity,
missing regressors, nonlinear interaction effects, etc. In reality, any of these
violations of classical assumptions will lead to accepting uninformed vari-
ables (a false positive) and/or rejecting informative variables (a false nega-
tive). For an example, seeSection 6.
Another common error is to believe that the central limit theorem some-
how justifies the use of linear regression models everywhere. The argument
goes like this: with enough observations, Normality prevails, and linear
models provide a good fit to the asymptotic correlation structure. This
“CLT Hail Mary pass”is an undergrad fantasy: yes, thesample meancon-
verges in distribution to a Gaussian, but not the sample itself! And that
converge only occurs if the observations are independent and identically
distributed. It takes a few lines of code to demonstrate that a misspecified
regression will perform poorly, whether we feed it thousands or billions of
observations.
Both extremes (hype and counterhype) prevent investors from recognizing
the real and differentiated value that ML delivers today. ML is modern statistics,
and it helps overcome many of the caveats of classical techniques that have
preoccupied asset managers for decades. SeeLópez de Prado (2019c)for
multiple examples of current applications of ML infinance.

12 Machine Learning for Asset Managers


```
1.7.2 ML Is a Black Box
```
This is perhaps the most widespread myth surrounding ML. Every research
laboratory in the world uses ML to some extent, so clearly ML is compatible
with the scientific method. Not only is ML not a black box, but asSection 6
explains, ML-based research tools can be more insightful than traditional
statistical methods (including econometrics). ML models can be interpreted
through a number of procedures, such as PDP, ICE, ALE, Friedman’s H-stat,
MDI, MDA, global surrogate, LIME, and Shapley values, among others. See
Molnar (2019)for a detailed treatment of ML interpretability.
Whether someone applies ML as a black box or as a white-box is a matter of
personal choice. The same is true of many other technical subjects. I personally
do not care much about how my car works, and I must confess that I have never
lifted the hood to take a peek at the engine (my thing is math, not mechanics).
So, my car remains a black box to me. I do not blame the engineers who
designed my car for my lack of curiosity, and I am aware that the mechanics
who work at my garage see my car as a white box. Likewise, the assertion that
ML is a black box reveals how some people have chosen to apply ML, and it is
not a universal truth.

```
1.7.3 Finance Has Insufficient Data for ML
```
It is true that a few ML algorithms, particularly in the context of price predic-
tion, require a lot of data. That is why a researcher must choose the right
algorithm for a particular job. On the other hand, ML critics who wield this
argument seem to ignore that many ML applications infinance do not require
any historical data at all. Examples include risk analysis, portfolio construction,
outlier detection, feature importance, and bet-sizing methods. Each section in
this Element demonstrates the mathematical properties of ML without relying
on any historical series. For instance,Section 7evaluates the accuracy of an
ML-based portfolio construction algorithm via Monte Carlo experiments.
Conclusions drawn from millions of Monte Carlo simulations teach us some-
thing about the general mathematical properties of a particular approach. The
anecdotal evidence derived from a handful of historical simulations is no match
to evaluating a wide range of scenarios.
Otherfinancial ML applications, like sentiment analysis, deep hedging, credit
ratings, execution, and private commercial data sets, enjoy an abundance of
data. Finally, in some settings, researchers can conduct randomized controlled
experiments, where they can generate their own data and establish precise
cause–effect mechanisms. For example, we may reword a news article and
compare ML’s sentiment extraction with a human’s conclusion, controlling for

```
Elements in Quantitative Finance 13
```

various changes. Likewise, we may experiment with the market’s reaction to
alternative implementations of an execution algorithm under comparable
conditions.

```
1.7.4 The Signal-to-Noise Ratio Is Too Low in Finance
```
There is no question thatfinancial data sets exhibit lower signal-to-noise ratio
than those used by other ML applications (a point that we will demonstrate in
Section 2). Because the signal-to-noise ratio is so low infinance, data alone are
not good enough for relying on black box predictions. That does not mean that
ML cannot be used infinance. It means that we must use ML differently, hence
the notion offinancial ML as a distinct subject of study. Financial ML is not the
mere application of standard ML tofinancial data sets. Financial ML comprises
ML techniques specially designed to tackle the specific challenges faced by
financial researchers, just as econometrics is not merely the application of
standard statistical techniques to economic data sets.
The goal offinancial ML ought to be to assist researchers in the discovery of
new economic theories. The theories so discovered, and not the ML algorithms,
will produce forecasts. This is no different than the way scientists utilize ML
across allfields of research.

```
1.7.5 The Risk of Overfitting Is Too High in Finance
```
Section 1.4 debunked this myth. In knowledgeable hands, ML algorithms
overfit less than classical methods. I concede, however, that in nonexpert
hands ML algorithms can cause more harm than good.

## 1.8 The Future of Financial Research

The International Data Corporation has estimated that 80% of all available data
are unstructured (IDC 2014). Many of the new data sets available to researchers
are high-dimensional, sparse, or nonnumeric. As a result of the complexities of
these new data sets, there is a limit to how much researchers can learn using
regression models and other linear algebraic or geometric approaches. Even
with older data sets, traditional quantitative techniques may fail to capture
potentially complex (e.g., nonlinear and interactive) associations among vari-
ables, and these techniques are extremely sensitive to the multicollinearity
problem that pervadesfinancial data sets (López de Prado 2019b).
Economics andfinance have much to benefit from the adoption of ML
methods. As of November 26, 2018, the Web of Science^4 lists 13,772 journal

(^4) [http://www.webofknowledge.com.](http://www.webofknowledge.com.)
14 Machine Learning for Asset Managers


articles on subjects in the intersection of “Economics” and “Statistics &
Probability.” Among those publications, only eighty-nine articles (0.65%)
contain any of the following terms: classifier, clustering, neural network, or
machine learning. To put it in perspective, out of the 40,283 articles in the
intersection of “Biology” and “Statistics & Probability,” a total of 4,049
(10.05%) contained any of those terms, and out of the 4,994 articles in the
intersection of“Chemistry, Analytical”and“Statistics & Probability,”a total of
766 (15.34%) contained any of those terms.
The econometric canon predates the dawn of digital computing. Most econo-
metric models were devised for estimation by hand and are a product of their time.
In the words of Robert Tibshirani,“people use certain methods because that is how
it all started and that’s what they are used to. It’s hard to change it.”^5 Students in the
twenty-first century should not be overexposed to legacy technologies. Moreover,
the most successful quantitative investmentfirms in history rely primarily on ML,
not econometrics, and the current predominance of econometrics in graduate
studies prepares students for academic careers, not for jobs in the industry.
This does not mean that econometrics has outlived its usability. Researchers
asked to decide between econometrics and ML are presented with a false
choice. ML and econometrics complement each other, because they have
different strengths. For example, ML can be particularly helpful at suggesting
to researchers the ingredients of a theory (seeSection 6), and econometrics can
be useful at testing a theory that is well grounded on empirical observation. In
fact, sometimes we may want to apply both paradigms at the same time, like in
semiparametric methods. For example, a regression could combine observable
explanatory variables with control variables that are contributed by an ML
algorithm (Mullainathan and Spiess 2017). Such approach would address the
bias associated with omitted regressors (Clarke 2005).

## 1.9 Frequently Asked Questions

Over the past few years, attendees at seminars have asked me all sorts of
interesting questions. In this section I have tried to provide a short answer to
some of the most common questions. I have also added a couple of questions
that I am still hoping that someone will ask one day.

```
In Simple Terms, What Is ML?
```
Broadly speaking, ML refers to the set of algorithms that learn complex patterns
in a high-dimensional space without being specifically directed. Let us break

(^5) https://qz.com/1206229/this-is-the-best-book-for-learning-modern-statistics-its-free/.
Elements in Quantitative Finance 15


that definition into its three components. First, ML learns without being speci-
fically directed, because researchers impose very little structure on the data.
Instead, the algorithm derives that structure from the data. Second, ML learns
complex patterns, because the structure identified by the algorithm may not be
representable as afinite set of equations. Third, ML learns in a high-dimensional
space, because solutions often involve a large number of variables, and the
interactions between them.
For example, we can train an ML algorithm to recognize human faces by
showing it examples. We do not define what a face is, hence the algorithm learns
without our direction. The problem is never posed in terms of equations, and in
fact the problem may not be expressible in terms of equations. And the algo-
rithm uses an extremely large number of variables to perform this task, includ-
ing the individual pixels and the interaction between the pixels.
In recent years, ML has become an increasingly useful research tool through-
out allfields of scientific research. Examples include drug development, gen-
ome research, new materials, and high-energy physics. Consumer products and
industrial services have quickly incorporated these technologies, and some of
the most valuable companies in the world produce ML-based products and
services.

```
How Is ML Different from Econometric Regressions?
```
Researchers use traditional regressions tofitapredefined functional form to
a set of variables. Regressions are extremely useful when we have a high
degree of conviction regarding that functional form and all the interaction
effects that bind the variables together. Going back to the eighteenth
century, mathematicians developed tools thatfit those functional forms
using estimators with desirable properties, subject to certain assumptions
on the data.
Starting in the 1950s, researchers realized that there was a different way to
conduct empirical analyses, with the help of computers. Rather than imposing a
functional form, particularly when that form is unknown ex ante, they would
allow algorithms tofigure out variable dependencies from the data. And rather
than making strong assumptions on the data, the algorithms would conduct
experiments that evaluate the mathematical properties of out-of-sample predic-
tions. This relaxation in terms of functional form and data assumptions, com-
bined with the use of powerful computers, opened the door to analyzing
complex data sets, including highly nonlinear, hierarchical, and noncontinuous
interaction effects.
Consider the following example: a researcher wishes to estimate the survival
probability of a passenger on theTitanic, based on a number of variables, such

16 Machine Learning for Asset Managers


as gender, ticket class, and age. A typical regression approach would be tofita
logit model to a binary variable, where 1 means survivor and 0 means
deceased, using gender, ticket class, and age as regressors. It turns out that,
even though these regressors are correct, a logit (or probit) model fails to
make good predictions. The reason is that logit models do not recognize that
this data set embeds a hierarchical (treelike) structure, with complex interac-
tions. For example, adult males in second class died at a much higher rate than
each of these attributes taken independently. In contrast, a simple“classifica-
tion tree” algorithm performs substantially better, because we allow the
algorithm tofind that hierarchical structure (and associated complex interac-
tions) for us.
As it turns out, hierarchical structures are omnipresent in economics and
finance (Simon 1962). Think of sector classifications, credit ratings, asset
classes, economic linkages, trade networks, clusters of regional economies,
etc. When confronted with these kinds of problems, ML tools can complement
and overcome the limitations of econometrics or similar traditional statistical
methods.

```
How Is ML Different from Big Data?
```
The termbig datarefers to data sets that are so large and/or complex that
traditional statistical techniques fail to extract and model the information
contained in them. It is estimated that 90% of all recorded data have been
created over the past two years, and 80% of the data is unstructured (i.e., not
directly amenable to traditional statistical techniques).
In recent years, the quantity and granularity of economic data have
improved dramatically. The good news is that the sudden explosion of admin-
istrative, private sector, and micro-level data sets offers an unparalleled
insight into the inner workings of the economy. The bad news is that these
data sets pose multiple challenges to the study of economics. (1) Some of
the most interesting data sets are unstructured. They can also be nonnumerical
and noncategorical, like news articles, voice recordings, or satellite images.
(2) These data sets are high-dimensional (e.g., credit card transactions.)
The number of variables involved often greatly exceeds the number of obser-
vations, making it very difficult to apply linear algebra solutions. (3) Many of
these data sets are extremely sparse. For instance, samples may contain a large
proportion of zeros, where standard notions such as correlation do not work
well. (4) Embedded within these data sets is critical information regarding
networks of agents, incentives, and aggregate behavior of groups of people.
ML techniques are designed for analyzing big data, which is why they are
often cited together.

```
Elements in Quantitative Finance 17
```

```
How Is the Asset Management Industry Using ML?
```
Perhaps the most popular application of ML in asset management is price
prediction. But there are plenty of equally important applications, like hedging,
portfolio construction, detection of outliers and structural breaks, credit ratings,
sentiment analysis, market making, bet sizing, securities taxonomy, and many
others. These are real-life applications that transcend the hype often associated
with expectations of price prediction.
For example, factor investingfirms use ML to redefine value. A few years
ago, price-to-earnings ratios may have provided a good ranking for value, but
that is not the case nowadays. Today, the notion of value is much more
nuanced. Modern asset managers use ML to identify the traits of value, and
how those traits interact with momentum, quality, size, etc. Meta-labeling
(Section 5.5) is another hot topic that can help asset managers size and time
their factor bets.
High-frequency trading firms have utilized ML for years to analyze
real-time exchange feeds, in search for footprints left by informed traders.
They can utilize this information to make short-term price predictions or to
make decisions on the aggressiveness or passiveness in order execution.
Credit rating agencies are also strong adopters of ML, as these algorithms
have demonstrated their ability to replicate the ratings generated by credit
analysts. Outlier detection is another important application, sincefinancial
models can be very sensitive to the presence of even a small number of
outliers. ML models can help improve investment performance byfinding
the proper size of a position, leaving the buy-or-sell decision to traditional or
fundamental models.

```
And Quantitative Investors Specifically?
```
All of the above applications, and many more, are relevant to quantitative
investors. It is a great time to be a quant. Data are more abundant than ever,
and computers arefinally delivering the power needed to make effective use of
ML. I am particularly excited about real-time prediction of macroeconomic
statistics, following the example of MIT’s Billion Prices Project (Cavallo and
Rigobon 2016). ML can be specially helpful at uncovering relationships that
until now remained hidden, even in traditional data sets. For instance, the
economic relationships between companies may not be effectively described
by traditional sector-group-industry classifications, such as GICS.^6 A network
approach, where companies are related according to a variety of factors, is likely

(^6) [http://www.msci.com/gics.](http://www.msci.com/gics.)
18 Machine Learning for Asset Managers


to offer a richer and more accurate representation of the dynamics, strengths,
and vulnerabilities of specific segments of the stock or credit markets (Cohen
and Frazzini 2008).

```
What Are Some of the Ways That ML Can Be Applied
to Investor Portfolios?
```
Portfolio construction is an extremely promising area for ML (Section 7). For
many decades, the asset management industry has relied on variations and
refinements of Markowitz’sefficient frontier to build investment portfolios. It
is known that many of these solutions are optimal in-sample, however, they can
perform poorly out-of-sample due to the computational instabilities involved in
convex optimization. Numerous classical approaches have attempted, with
mixed success, to address these computational instabilities. ML algorithms
have shown the potential to produce robust portfolios that perform well out-
of-sample, thanks to their ability to recognize sparse hierarchical relationships
that traditional methods miss (López de Prado 2016).

```
What Are the Risks? Is There Anything That Investors Should
Be Aware of or Look Out For?
```
Finance is not a plug-and-play subject as it relates to ML. Modelingfinancial
series is harder than driving cars or recognizing faces. The reason is, the signal-
to-noise ratio infinancial data is extremely low, as a result of arbitrage forces
and nonstationary systems. The computational power and functionalflexibility
of ML ensures that it will alwaysfind a pattern in the data, even if that pattern is
afluke rather than the result of a persistent phenomenon. An“oracle”approach
tofinancial ML, where algorithms are developed to form predictions divorced
from all economic theory, is likely to yield false discoveries. I have never heard
a scientist say“Forget about theory, I have this oracle that can answer anything,
so let’s all stop thinking, and let’s just believe blindly whatever comes out.”
It is important for investors to recognize that ML is not a substitute for
economic theory, but rather a powerful tool for building modern economic
theories. We need ML to develop betterfinancial theories, and we needfinancial
theories to restrict ML’s propensity to overfit. Without this theory–ML inter-
play, investors are placing their trust on high-tech horoscopes.

```
How Do You Expect ML to Impact the Asset Management
Industry in the Next Decade?
```
Today, the amount of ML used by farmers is staggering: self-driving tractors,
drones scanning for irregular patches of land, sensors feeding cattle and

```
Elements in Quantitative Finance 19
```

administering nutrients as needed, genetically engineered crops, satellite images
for estimating yields, etc. Similarly, I think in ten years we will look back, and ML
will be an important aspect of asset management. And just like in the farming
industry, although this transformation may not happen overnight, it is clear that
there is only one direction forward.
Economic data sets will only get bigger, and computers will only get more
powerful. Most asset managers will fail either by not evolving or by rushing into
the unknown without fully recognizing the dangers involved in the“oracle”
approach. Only a few asset managers will succeed by evolving in a thoughtful
and responsible manner.

```
How Do You Expect ML to Impact Financial Academia
in the Next Decade?
```
Imagine if physicists had to produce theories in a universe where the
fundamental laws of nature are in a constant flux; where publications
have an impact on the very phenomenon under study; where experimen-
tation is virtually impossible; where data are costly, the signal is dim, and
the system under study is incredibly complex...I feel utmost admiration
for how muchfinancial academics have achieved in the face of paramount
adversity.
ML has a lot to offer to the academic profession. First, ML provides the
power andflexibility needed tofind dim signals in the sea of noise caused by
arbitrage forces. Second, ML allows academics to decouple the research
process into two stages: (1) search for important variables irrespective of
functional form, and (2) search for a functional form that binds those vari-
ables.López de Prado (2019b)demonstrates how even small specification
errors mislead researchers into rejecting important variables. It is hard to
overstate the relevance of decoupling the specification search from the vari-
ables search. Third, ML offers the possibility of conducting simulations on
synthetic data. This is as close asfinance will ever get to experimentation, in
the absence of laboratories. We live an exciting time to do academic research
onfinancial systems, and I expect tremendous breakthroughs as morefinan-
cial researchers embrace ML.

```
Isn’t Financial ML All about Price Prediction?
```
One of the greatest misunderstandings I perceive from reading the press is the
notion that ML’s main (if not only) objective is price prediction. Asset pricing is
undoubtedly a very worthy endeavor, however its importance is often over-
stated. Having an edge at price prediction is just one necessary, however entirely

20 Machine Learning for Asset Managers


insufficient, condition to be successful in today’s highly competitive market.
Other areas that are equally important are data processing, portfolio construc-
tion, risk management, monitoring for structural breaks, bet sizing, and
detection of false investment strategies, just to cite a few.
Consider the players at the World Series of Poker. The cards are shuffled
and distributed randomly. These players obviously cannot predict what cards
will be handed to players with any meaningful accuracy. And yet, the same
handful of players ends up in top positions year after year. One reason is, bet
sizing is more important than card prediction. When a player receives a good
hand, he evaluates the probability that another player may hold a strong hand
too, and bets strategically. Likewise, investors may not be able to predict
prices, however they may recognize when an out-of-the-normal price has
printed, and bet accordingly. I am not saying that bet sizing is the key to
successful investing. I am merely stating that bet sizing is at least as important
as price prediction, and that portfolio construction is arguably even more
important.

```
Why Don’t You Discuss a Wide Range of ML Algorithms?
```
The purpose of this Element is not to introduce the reader to the vast popula-
tion of ML algorithms used today infinance. There are two reasons for that.
First, there are lengthy textbooks dedicated to the systematic exposition of
those algorithms, and another one is hardly needed. Excellent references
includeJames et al. (2013), Hastie et al. (2016),andEfron and Hastie
(2016). Second,financial data sets have specific nuisances, and the success
or failure of a project rests on understanding them. Once we have engineered
the features and posed the problem correctly, choosing an algorithm plays a
relatively secondary role.
Allow me to illustrate the second point with an example. Compare an
algorithm that forecasted a change of 1, but received a realized change of 3,
with another algorithm that forecasted a change of−1, but received a realized
change of 1. In both cases, the forecast error is 2. In many industrial applica-
tions, we would be indifferent between both errors. That is not the case in
finance. In thefirst instance, an investor makes one-third of the predicted
profit, whereas in the second instance the investor suffers a loss equal to the
predicted profit. Failing to predict the size is an opportunity loss, but failing to
predict the sign is an actual loss. Investors penalize actual losses much more
than opportunity losses. Predicting the sign of an outcome is often more
important than predicting its size, and a reason for favoring classifiers over
regression methods infinance. In addition, it is common infinance tofind that
the sign and size of an outcome depend on different features, so jointly

```
Elements in Quantitative Finance 21
```

forecasting the sign and size of an outcome with a unique set of features can
lead to subpar results.^7 ML experts who transition intofinance from other
fields often make fundamental mistakes, like posing problems incorrectly, as
explained inLópez de Prado (2018b). Financial ML is a subject in its own
right, and the discussion of generic ML algorithms is not the heart of the
matter.

```
Why Don’t You Discuss a Specific Investment Strategy,
Like Many Other Books Do?
```
There are plenty of books in the market that provide recipes for
implementing someone else’s investment strategy. Those cookbooks
show us how to prepare someone else’s cake. This Element is different.
I want to show you how you can use ML to discover new economic and
financial theories that are relevant to you, on which you can base your
proprietary investment strategies. Your investment strategies are just the
particular implementation of the theories that first you must discover
independently. You cannot bake someone else’s cake and expect to retain
it for yourself.

## 1.10 Conclusions

The purpose of this Element is to introduce ML tools that are useful for
discovering economic andfinancial theories. Successful investment strategies
are specific implementations of general theories. An investment strategy that
lacks a theoretical justification is likely to be false. Hence, a researcher should
concentrate her efforts on developing a theory, rather than of backtesting
potential strategies.
ML is not a black box, and it does not necessarily overfit. ML tools
complement rather than replace the classical statistical methods. Some
of ML’s strengths include (1) Focus on out-of-sample predictability over
variance adjudication; (2) usage of computational methods to avoid
relying on (potentially unrealistic) assumptions; (3) ability to “learn”
complex specifications, including nonlinear, hierarchical, and noncontin-
uous interaction effects in a high-dimensional space; and (4) ability to
disentangle the variable search from the specification search, in a manner
robust to multicollinearity and other substitution effects.

(^7) See López de Prado (2018a)for a discussion of meta-labeling algorithms, where the sign and size
decision is made by independent algorithms.
22 Machine Learning for Asset Managers


## 1.11 Exercises

1 Can quantitative methods be used to predict events that never happened
before? How could quantitative methods predict a black swan?
2 Why is theory particularly important infinance and economics? What is the
best use of ML infinance?
3 What are popular misconceptions aboutfinancial ML? Arefinancial data sets
large enough for ML applications?
4 How does ML control for overfitting? Is the signal-to-noise ratio too low in
finance for allowing the use of ML?
5 Describe a quantitative approach infinance that combines classical and ML
methods. How is ML different from a large regression? Describefive appli-
cations offinancial ML.

```
Elements in Quantitative Finance 23
```

## 2 Denoising and Detoning

## 2.1 Motivation

Covariance matrices are ubiquitous infinance. We use them to run regressions,
estimate risks, optimize portfolios, simulate scenarios via Monte Carlo,find
clusters, reduce the dimensionality of a vector space, and so on. Empirical
covariance matrices are computed on series of observations from a random
vector, in order to estimate the linear comovement between the random variables
that constitute the random vector. Given thefinite and nondeterministic nature of
these observations, the estimate of the covariance matrix includes some amount
of noise. Empirical covariance matrices derived from estimated factors are also
numerically ill-conditioned, because those factors are also estimated fromflawed
data. Unless we treat this noise, it will impact the calculations we perform with the
covariance matrix, sometimes to the point of rendering the analysis useless.
The goal of this section is to explain a procedure for reducing the noise and
enhancing the signal included in an empirical covariance matrix. Throughout
this Element, we assume that empirical covariance and correlation matrices
have been subjected to this procedure.

## 2.2 The Marcenko–Pastur Theorem

Consider a matrix of independent and identically distributed random observa-
tionsX, of sizeTxN, where the underlying process generating the observations
has zero mean and varianceσ^2. The matrixC¼T^1 X^0 Xhas eigenvaluesλthat
asymptotically converge (asN→þ∞andT→þ∞with 1<T=N<þ∞) to the
Marcenko–Pastur probability density function (PDF),

```
f½λ¼
```
#### T

#### N

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðÞλþλðÞλλ
```
```
p
```
```
2 πλσ^2
ifλ2½λ;λþ
0ifλ2½= λ;λþ;
```
#### 8

#### ><

#### >:

where the maximum expected eigenvalue isλþ¼σ^21 þ

```
ffiffiffiffiffiffiffiffiffiffi
N=T
```
```
p 2
and the
```
minimum expected eigenvalue isλ¼σ^21 

```
ffiffiffiffiffiffiffiffiffiffi
N=T
```
```
p 2
```
. Whenσ^2 ¼1, thenC

is the correlation matrix associated withX. Code Snippet 2.1implements the
Marcenko–Pastur PDF in python.
Eigenvaluesλ2½λ;λþare consistent with random behavior, and eigenva-
luesλ2½= λ;λþare consistent with nonrandom behavior. Specifically, we
associate eigenvaluesλ2½ 0 ;λþwith noise.Figure 2.1and Code Snippet 2.2
demonstrate how closely the Marcenko–Pastur distribution explains the eigen-
values of a random matrixX.

24 Machine Learning for Asset Managers


#### SNIPPET2.1 THEMARCENKO–PASTURPDF

import numpy as np,pandas as pd
#---------------------------------------------------
def mpPDF(var,q,pts):
#Marcenko-Pastur pdf
#q=T/N
eMin,eMax=var*(1-(1./q)**.5)**2,var*(1+(1./q)**.5)**2
eVal=np.linspace(eMin,eMax,pts)
pdf=q/(2*np.pi*var*eVal)*((eMax-eVal)*(eVal-eMin))**.5
pdf=pd.Series(pdf,index=eVal)
return pdf

#### SNIPPET2.2 TESTING THEMARCENKO–PASTURTHEOREM

from sklearn.neighbors.kde import KernelDensity
#---------------------------------------------------
def getPCA(matrix):
#Get eVal,eVec from a Hermitian matrix
eVal,eVec=np.linalg.eigh(matrix)
indices=eVal.argsort()[::-1]# arguments for sorting eVal desc
eVal,eVec=eVal[indices],eVec[:,indices]
eVal=np.diagflat(eVal)
return eVal,eVec
#---------------------------------------------------
deffitKDE(obs,bWidth=.25,kernel=’gaussian’,x=None):
#Fit kernel to a series of obs, and derive the prob of obs
#x is the array of values on which thefit KDE will be evaluated
if len(obs.shape)==1:obs=obs.reshape(-1,1)
kde=KernelDensity(kernel=kernel,bandwidth=bWidth).fit(obs)
if x is None:x=np.unique(obs).reshape(-1,1)
if len(x.shape)==1:x=x.reshape(-1,1)
logProb=kde.score_samples(x)# log(density)
pdf=pd.Series(np.exp(logProb),index=x.flatten())
return pdf
#---------------------------------------------------
x=np.random.normal(size=(10000,1000))
eVal0,eVec0=getPCA(np.corrcoef(x,rowvar=0))
pdf0=mpPDF(1.,q=x.shape[0]/float(x.shape[1]),pts=1000)
pdf1=fitKDE(np.diag(eVal0),bWidth=.01)# empirical pdf

```
Elements in Quantitative Finance 25
```

## 2.3 Random Matrix with Signal

In an empirical correlation matrix, not all eigenvectors may be random.Code
Snippet 2.3builds a covariance matrix that is not perfectly random, and hence its
eigenvalues will only approximately follow the Marcenko–Pastur PDF. Out of the
nCols random variables that form the covariance matrix generated by getRndCov,
only nFact contain some signal. To further dilute the signal, we add that covariance
matrix to a purely random matrix, with a weight alpha. SeeLewandowski et al.
(2009)for alternative ways of building a random covariance matrix.

## 2.4 Fitting the Marcenko–Pastur Distribution

In this section, we follow the approach introduced byLaloux et al. (2000). Since
only part of the variance is caused by random eigenvectors, we can adjustσ^2
accordingly in the above equations. For instance, if we assume that the eigen-
vector associated with the highest eigenvalue isnotrandom, then we should
replaceσ^2 withσ^2 ðÞ 1 λþ=N in the above equations. In fact, we canfit the
functionf½λto the empirical distribution of the eigenvalues to derive the
impliedσ^2. That will give us the variance that is explained by the random
eigenvectors present in the correlation matrix, and it will determine the cutoff
levelλþ, adjusted for the presence of nonrandom eigenvectors.
Code Snippet 2.4fits the Marcenko–Pastur PDF to a random covariance
matrix that contains signal. The objective of thefitistofind the value ofσ^2 that
minimizes the sum of the squared differences between the analytical PDF and

```
0.0
0.00 0.25 0.50 0.70 1.00
```
```
prob[
```
```
λ]
```
```
λ
```
```
1.25 1.50 1.75 2.00
```
```
0.2
```
```
0.4
```
```
0.6
```
```
0.8
```
```
1.0
```
```
1.2
Marcenko-Pastur
Empirical:KDE
```
```
Figure 2.1A visualization of the Marcenko–Pastur theorem.
```
26 Machine Learning for Asset Managers


#### SNIPPET2.4 FITTING THEMARCENKO–PASTURPDF

from scipy.optimize import minimize
#---------------------------------------------------
def errPDFs(var,eVal,q,bWidth,pts=1000):
# Fit error
pdf0=mpPDF(var,q,pts)# theoretical pdf
pdf1=fitKDE(eVal,bWidth,x=pdf0.index.values)# empirical pdf
sse=np.sum((pdf1-pdf0)**2)
return sse
#---------------------------------------------------
deffindMaxEval(eVal,q,bWidth):
# Find max random eVal byfitting Marcenko’s dist
out=minimize(lambda *x:errPDFs(*x),.5,args=(eVal,q,bWidth),
bounds=((1E-5,1-1E-5),))
if out[’success’]:var=out[’x’][0]
else:var=1
eMax=var*(1+(1./q)**.5)**2
return eMax,var
#---------------------------------------------------
eMax0,var0=findMaxEval(np.diag(eVal0),q,bWidth=.01)
nFacts0=eVal0.shape[0]-np.diag(eVal0)[::-1].searchsorted(eMax0)

#### SNIPPET2.3 ADDSIGNAL TO ARANDOMCOVARIANCEMATRIX

def getRndCov(nCols,nFacts):
w=np.random.normal(size=(nCols,nFacts))
cov=np.dot(w,w.T)# random cov matrix, however not full rank
cov+=np.diag(np.random.uniform(size=nCols))# full rank cov
return cov
#---------------------------------------------------
def cov2corr(cov):
# Derive the correlation matrix from a covariance matrix
std=np.sqrt(np.diag(cov))
corr=cov/np.outer(std,std)
corr[corr<-1],corr[corr>1]=-1,1# numerical error
return corr
#---------------------------------------------------
alpha,nCols,nFact,q=.995,1000,100,10
cov=np.cov(np.random.normal(size=(nCols*q,nCols)),rowvar=0)
cov=alpha*cov+(1-alpha)*getRndCov(nCols,nFact)# noise+signal
corr0=cov2corr(cov)
eVal0,eVec0=getPCA(corr0)

```
Elements in Quantitative Finance 27
```

the kernel density estimate (KDE) of the observed eigenvalues (for references on
KDE, seeRosenblatt 1956; Parzen 1962). The valueλþis reported as eMax0, the
value ofσ^2 is stored as var0, and the number of factors is recovered as nFacts0.
Figure 2.2plots the histogram of eigenvalues and the PDF of thefitted
Marcenko–Pastur distribution. Eigenvalues to the right of the fitted
Marcenko–Pastur distribution cannot be associated with noise, thus they are
related to signal. The code returns a value of 100 for nFacts0, the same number
of factors we had injected to the covariance matrix. Despite the dim signal
present in the covariance matrix, the procedure has been able to separate the
eigenvalues associated with noise from the eigenvalues associated with signal.
The fitted distribution implies thatσ^2 ≈:6768, indicating that only about
32.32% of the variance can be attributed to signal. This is one way of measuring
the signal-to-noise ratio infinancial data sets, which is known to be low as a
result of arbitrage forces.

## 2.5 Denoising

It is common infinancial applications to shrink a numerically ill-conditioned
covariance matrix (Ledoit and Wolf 2004). By making the covariance matrix
closer to a diagonal, shrinkage reduces its condition number. However, shrink-
age accomplishes that without discriminating between noise and signal. As a
result, shrinkage can further eliminate an already weak signal.

```
λ
```
```
0123456
```
```
0.0
```
```
prob[
```
```
λ]
```
```
0.2
```
```
0.4
```
```
0.6
```
```
0.8
```
```
1.0
```
```
1.2
```
```
1.4
```
```
1.6
```
```
Marcenko-Pastur dist
Empirical dist
```
```
Figure 2.2Fitting the Marcenko–Pastur PDF on a noisy covariance matrix.
```
28 Machine Learning for Asset Managers


```
In theprevious section, we have learned how to discriminate between
eigenvalues associated with noise components and eigenvalues associated
with signal components. In this section we discuss how to use this information
for denoising the correlation matrix.
```
```
2.5.1 Constant Residual Eigenvalue Method
This approach consists in setting a constant eigenvalue for all random eigen-
vectors. Letfλngn¼ 1 ;...;Nbe the set of all eigenvalues, ordered descending, andi
be the position of the eigenvalue such thatλi>λþandλiþ 1 ≤λþ. Then we set
λj¼ 1 =ðNiÞ
```
#### PN

```
k¼iþ 1 λk,j¼iþ^1 ;...;N, hence preserving the trace of the
correlation matrix. Given the eigenvector decompositionVW¼WΛ, we form
the denoised correlation matrixC 1 as
```
```
Ce 1 ¼WΛeW^0
```
```
C 1 ¼Ce 1 diagCe 1
```
```
hi ^12
diagCe 1
```
```
hi ^120
```
#### "# 1

#### ;

whereΛeis the diagonal matrix holding the corrected eigenvalues, the apos-
trophe (') transposes a matrix, and diag[.] zeroes all non-diagonal elements of a
squared matrix. The reason for the second transformation is to rescale the matrix
Ce 1 , so that the main diagonal ofC 1 is an array of 1s.Code Snippet 2.5
implements this method.Figure 2.3compares the logarithms of the eigenvalues
before and after denoising by this method.

```
2.5.2 Targeted Shrinkage
The numerical method described earlier is preferable to shrinkage, because it
removes the noise while preserving the signal. Alternatively, we could target the
```
#### SNIPPET2.5 DENOISING BYCONSTANTRESIDUALEIGENVALUE

```
def denoisedCorr(eVal,eVec,nFacts):
# Remove noise from corr byfixing random eigenvalues
eVal_=np.diag(eVal).copy()
eVal_[nFacts:]=eVal_[nFacts:].sum()/float(eVal_.shape[0]-nFacts)
eVal_=np.diag(eVal_)
corr1=np.dot(eVec,eVal_).dot(eVec.T)
corr1=cov2corr(corr1)
return corr1
#---------------------------------------------------
corr1=denoisedCorr(eVal0,eVec0,nFacts0)
eVal1,eVec1=getPCA(corr1)
```
```
Elements in Quantitative Finance 29
```

application of the shrinkage strictly to the random eigenvectors. Consider the
correlation matrixC 1

```
C 1 ¼WLΛLWL^0 þαWRΛRWR^0 þðÞ 1 αdiag½WRΛRWR^0 ;
```
where WR and ΛR are the eigenvectors and eigenvalues associated with
njλn≤λþgf ,WLandΛLare the eigenvectors and eigenvalues associated with
njλn>λþgf , andαregulates the amount of shrinkage among the eigenvectors
and eigenvalues associated with noise (α→0 for total shrinkage).Code Snippet
2.6 implements this method.Figure 2.4compares the logarithms of the eigen-
values before and after denoising by this method.

## 2.6 Detoning

Financial correlation matrices usually incorporate a market component. The
market component is characterized by thefirst eigenvector, with loadings
Wn; 1 ≈ N^12 ,n¼ 1 ;...;N. Accordingly, a market component affects every
item of the covariance matrix. In the context of clustering applications, it is
useful to remove the market component, if it exists (a hypothesis that can be
tested statistically). The reason is, it is more difficult to cluster a correlation

```
100
Eigenvalue (log-scale)
```
```
Original eigen-function
Denoised eigen-function
```
```
0 200 400
Eigenvalue number
```
```
600 800 1,000
```
Figure 2.3A comparison of eigenvalues before and after applying the residual
eigenvalue method.

30 Machine Learning for Asset Managers


matrix with a strong market component, because the algorithm will struggle to
find dissimilaritiesacrossclusters. By removing the market component, we
allow a greater portion of the correlation to be explained by components that
affect specific subsets of the securities. It is similar to removing a loud tone that
prevents us from hearing other sounds. Detoning is the principal components
analysis analogue to computing beta-adjusted (or market-adjusted) returns in
regression analysis.

```
100
Eigenvalue (log-scale)
```
```
Original eigen-function
Denoised eigen-function
```
```
0 200 400
Eigenvalue number
```
```
600 800 1,000
```
Figure 2.4A comparison of eigenvalues before and after applying the targeted
shrinkage method.

#### SNIPPET2.6 DENOISING BYTARGETEDSHRINKAGE

```
def denoisedCorr2(eVal,eVec,nFacts,alpha=0):
# Remove noise from corr through targeted shrinkage
eValL,eVecL=eVal[:nFacts,:nFacts],eVec[:,:nFacts]
eValR,eVecR=eVal[nFacts:,nFacts:],eVec[:,nFacts:]
corr0=np.dot(eVecL,eValL).dot(eVecL.T)
corr1=np.dot(eVecR,eValR).dot(eVecR.T)
corr2=corr0+alpha*corr1+(1-alpha)*np.diag(np.diag(corr1))
return corr2
#---------------------------------------------------
corr1=denoisedCorr2(eVal0,eVec0,nFacts0,alpha=.5)
eVal1,eVec1=getPCA(corr1)
```
```
Elements in Quantitative Finance 31
```

We can remove the market component from the denoised correlation matrix,
C 1 , to form the detoned correlation matrix

```
Ce 2 ¼C 1 WMΛMWM^0 ¼WDΛDWD^0
```
```
C 2 ¼Ce 2 diagCe 2
```
hi  (^1) = 2
diagCe 2
hi  (^1) = 20  1
;
whereWMandΛMare the eigenvectors and eigenvalues associated with market
components (usually only one, but possibly more), andWDandΛDare the
eigenvectors and eigenvalues associated with nonmarket components.
The detoned correlation matrix is singular, as a result of eliminating (at least)
one eigenvector. This is not a problem for clustering applications, as most
approaches do not require the invertibility of the correlation matrix. Still, a
detoned correlation matrixC 2 cannot be used directly for mean-variance port-
folio optimization. Instead, we can optimize a portfolio on the selected (non-
zero) principal components, and map the optimal allocationsfback to the
original basis. The optimal allocations in the original basis are
ω¼Wþf;
whereWþcontains only the eigenvectors that survived the detoning process (i.e.,
with a nonnull eigenvalue), andfis the vector of optimal allocations to those
same components.

## 2.7 Experimental Results

Working with denoised and detoned covariance matrices renders substantial
benefits. Those benefits result from the mathematical properties of those treated
matrices, and can be evaluated through Monte Carlo experiments. In this section
we discuss two characteristic portfolios of the efficient frontier, namely, the
minimum variance and maximum Sharpe ratio solutions, since any member of
the unconstrained efficient frontier can be derived as a convex combination of
the two.

```
2.7.1 Minimum Variance Portfolio
```
In this section, we compute the errors associated with estimating a minimum
variance portfolio with and without denoising.Code Snippet 2.7forms a vector
of means and a covariance matrix out of ten blocks of sizefifty each, where off-
diagonal elements within each block have a correlation of 0.5. This covariance
matrix is a stylized representation of a true (nonempirical) detoned correlation
matrix of the S&P 500, where each block is associated with an economic sector.
Without loss of generality, the variances are drawn from a uniform distribution

32 Machine Learning for Asset Managers


bounded between 5% and 20%, and the vector of means is drawn from a Normal
distribution with mean and standard deviation equal to the standard deviation
from the covariance matrix. This is consistent with the notion that in an efficient
market all securities have the same expected Sharpe ratio. Wefix a seed to
facilitate the comparison of results across runs with different parameters.
Code Snippet 2.8uses the true (nonempirical) covariance matrix to draw a
random matrixXof sizeTxN, and it derives the associated empirical covariance
matrix and vector of means. Function simCovMu receives argument nObs,

#### SNIPPET2.7 GENERATING ABLOCK-DIAGONALCOVARIANCEMATRIX AND AVECTOR OF

#### MEANS

```
def formBlockMatrix(nBlocks,bSize,bCorr):
block=np.ones((bSize,bSize))*bCorr
block[range(bSize),range(bSize)]=1
corr=block_diag(*([block]*nBlocks))
return corr
#---------------------------------------------------
def formTrueMatrix(nBlocks,bSize,bCorr):
corr0=formBlockMatrix(nBlocks,bSize,bCorr)
corr0=pd.DataFrame(corr0)
cols=corr0.columns.tolist()
np.random.shuffle(cols)
corr0=corr0[cols].loc[cols].copy(deep=True)
std0=np.random.uniform(.05,.2,corr0.shape[0])
cov0=corr2cov(corr0,std0)
mu0=np.random.normal(std0,std0,cov0.shape[0]).reshape(-1,1)
return mu0,cov0
#---------------------------------------------------
from scipy.linalg import block_diag
from sklearn.covariance import LedoitWolf
nBlocks,bSize,bCorr=10,50,.5
np.random.seed(0)
mu0,cov0=formTrueMatrix(nBlocks,bSize,bCorr)
```
#### SNIPPET2.8 GENERATING THEEMPIRICALCOVARIANCEMATRIX

```
def simCovMu(mu0,cov0,nObs,shrink=False):
x=np.random.multivariate_normal(mu0.flatten(),cov0,size=nObs)
mu1=x.mean(axis=0).reshape(-1,1)
if shrink:cov1=LedoitWolf().fit(x).covariance_
else:cov1=np.cov(x,rowvar=0)
return mu1,cov1
```
```
Elements in Quantitative Finance 33
```

which sets the value ofT. When shrink=True, the function performs a Ledoit–
Wolf shrinkage of the empirical covariance matrix.
Code Snippet 2.9applies the methods explained in this section, to denoise the
empirical covariance matrix. In this particular experiment, we denoise through
the constant residual eigenvalue method.

Code Snippet 2.10runs the following Monte Carlo experiment with 1,000
iterations: (1) draw a random empirical covariance matrix (shrinkage optional)
withT¼ 1 ;000; (2) denoise the empirical covariance matrix (optional); (3)

#### SNIPPET2.9 DENOISING OF THEEMPIRICALCOVARIANCEMATRIX

```
def corr2cov(corr,std):
cov=corr*np.outer(std,std)
return cov
#---------------------------------------------------
def deNoiseCov(cov0,q,bWidth):
corr0=cov2corr(cov0)
eVal0,eVec0=getPCA(corr0)
eMax0,var0=findMaxEval(np.diag(eVal0),q,bWidth)
nFacts0=eVal0.shape[0]-np.diag(eVal0)[::-1].searchsorted(eMax0)
corr1=denoisedCorr(eVal0,eVec0,nFacts0)
cov1=corr2cov(corr1,np.diag(cov0)**.5)
return cov1
```
#### SNIPPET2.10 DENOISING OF THEEMPIRICALCOVARIANCEMATRIX

```
def optPort(cov,mu=None):
inv=np.linalg.inv(cov)
ones=np.ones(shape=(inv.shape[0],1))
if mu is None:mu=ones
w=np.dot(inv,mu)
w/=np.dot(ones.T,w)
return w
#---------------------------------------------------
nObs,nTrials,bWidth,shrink,minVarPortf=1000,1000,.01,False,True
w1=pd.DataFrame(columns=xrange(cov0.shape[0]),
index=xrange(nTrials),dtype=float)
w1_d=w1.copy(deep=True)
np.random.seed(0)
for i in range(nTrials):
mu1,cov1=simCovMu(mu0,cov0,nObs,shrink=shrink)
if minVarPortf:mu1=None
cov1_d=deNoiseCov(cov1,nObs*1./cov1.shape[1],bWidth)
w1.loc[i]=optPort(cov1,mu1).flatten()
w1_d.loc[i]=optPort(cov1_d,mu1).flatten()
```
34 Machine Learning for Asset Managers


derive the minimum variance portfolio, using the function optPort. When we
pass the argument shrink=True to function simCovMu, the covariance matrix is
shrunk. When parameter bWidth>0, the covariance matrix is denoised prior to
estimating the minimum variance portfolio.^8 A random seed is arbitrarily set, so
that we may run this Monte Carlo experiment on the same covariance matrices,
with and without denoising.
Code Snippet 2.11computes the true minimum variance portfolio, derived
from the true covariance matrix. Using those allocations as benchmark, it then
computes the root-mean-square errors (RMSE) across all weights, with and
without denoising. We can runCode Snippet 2.11with and without shrinkage,
thus obtaining the four combinations displayed inFigure 2.5. Denoising is much
more effective than shrinkage: the denoised minimum variance portfolio incurs
only 40.15% of the RMSE incurred by the minimum variance portfolio without
denoising. That is a 59.85% reduction in RMSE from denoising alone, com-
pared to a 30.22% reduction using Ledoit–Wolf shrinkage. Shrinkage adds little
benefit beyond what denoising contributes. The reduction in RMSE from
combining denoising with shrinkage is 65.63%, which is not much better than
the result from using denoising only.

## 2.7.2 Maximum Sharpe Ratio Portfolio

We can repeat the previous experiment, where on this occasion we target the
estimation of the maximum Sharpe ratio portfolio. In order to do that, we need

#### SNIPPET2.11 ROOT-MEAN-SQUAREERRORS

```
w0=optPort(cov0,None if minVarPortf else mu0)
w0=np.repeat(w0.T,w1.shape[0],axis=0)
rmsd=np.mean((w1-w0).values.flatten()**2)**.5# RMSE
rmsd_d=np.mean((w1_d-w0).values.flatten()**2)**.5# RMSE
print rmsd,rmsd_d
```
```
Not denoised Denoised
Not shrunk 4.95E– 03 1.99E– 03
Shrunk 3.45E– 03 1.70E– 03
```
```
Figure 2.5RMSE for combinations of denois-
ing and shrinkage (minimum variance portfolio).
```
(^8) As an exercise, we leave the estimation via cross-validation of the optimal value of bWidth.
Elements in Quantitative Finance 35


to set minVarPortf=True inCode Snippet 2.10. Figure 2.6shows that, once
again, denoising is much more effective than shrinkage: the denoised maximum
Sharpe ratio portfolio incurs only 0.04% of the RMSE incurred by the max-
imum Sharpe ratio portfolio without denoising. That is a 94.44% reduction in
RMSE from denoising alone, compared to a 70.77% reduction using Ledoit–
Wolf shrinkage. While shrinkage is somewhat helpful in absence of denoising,
it adds no benefit in combination with denoising. This is because shrinkage
dilutes the noise at the expense of diluting some of the signal as well.

## 2.8 Conclusions

Infinance, empirical covariance matrices are often numerically ill-conditioned, as a
result of the small number of independent observations used to estimate a large
number of parameters. Working with those matrices directly, without treatment, is
not recommended. Even if the covariance matrix is nonsingular, and therefore
invertible, the small determinant all but guarantees that the estimations error will be
greatly magnified by the inversion process. These estimation errors cause misallo-
cation of assets and substantial transaction costs due to unnecessary rebalancing.
The Marcenko–Pastur theorem gives us the distribution of the eigenvalues
associated with a random matrix. Byfitting this distribution, we can discriminate
between eigenvalues associated with signal and eigenvalues associated with noise.
The latter can be adjusted to correct the matrix’s ill-conditioning, without diluting
the signal. This random matrix theoretic approach is generally preferable to (1) the
threshold method (Jolliffe 2002, 113), which selects a number of components that
jointly explain afixed amount of variance, regardless of the true amount of variance
caused by noise; and (2) the shrinkage method (Ledoit and Wolf 2004), which can
remove some of the noise at the cost of diluting much of the signal.
Recall that the correlation matrix’s condition number is the ratio between its
maximal and minimal (by moduli) eigenvalues. Denoising reduces the condi-
tion number by increasing the lowest eigenvalue. We can further reduce the
condition number by reducing the highest eigenvalue. This makes mathematical
sense, and also intuitive sense. Removing the market components present in the

```
Not denoised Denoised
Not shrunk 9.48E– 01 5.27E– 02
Shrunk 2.77E– 01 5.17E– 02
```
```
Figure 2.6RMSE for combinations of denoising
and shrinkage (maximum Sharpe ratio portfolio).
```
36 Machine Learning for Asset Managers


correlation matrix reinforces the more subtle signals hiding under the market
“tone.”For example, if we are trying to cluster a correlation matrix of stock
returns, detoning that matrix will likely help amplify the signals associated with
other exposures, such as sector, industry, or size.
We have demonstrated the usefulness of denoising in the context of portfolio
optimization, however its applications extend to any use of the covariance
matrix. For example, denoising the matrixX^0 Xbefore inverting it should help
reduce the variance of regression estimates, and improve the power of statistical
tests of hypothesis. For the same reason, covariance matrices derived from
regressed factors (also known as factor-based covariance matrices) also require
denoising, and should not be used without numerical treatment.

## 2.9 Exercises

1 Implement in python the detoning method described inSection 2.6.
2 Using a series of matrix of stock returns:
a Compute the covariance matrix. What is the condition number of the
correlation matrix?
b Compute one hundred efficient frontiers by drawing one hundred alter-
native vectors of expected returns from a Normal distribution with mean
10% and standard deviation 10%.
c Compute the variance of the errors against the mean efficient frontier.
3 Repeat Exercise 2, where this time you denoise the covariance matrix before
computing the one hundred efficient frontiers.
a What is the value ofσ^2 implied by the Marcenko–Pastur distribution?
b How many eigenvalues are associated with random components?
c Is the variance of the errors significantly higher or lower? Why?
4 Repeat Exercise 2, where this time you apply the Ledoit–Wolf shrinkage
method (instead of denoising) on the covariance matrix before computing the
one hundred efficient frontiers. Is the variance of the errors significantly
higher or lower? Why?
5 Repeat Exercise 3, where this time you also detone the covariance matrix
before computing the one hundred efficient frontiers. Is the variance of the
errors significantly higher or lower? Why?
6 What happens if you drop the components whose eigenvalues fall below a
given threshold? Can you still compute the efficient frontiers? How?
7 Extend functionfitKDE in Code Snippet 2.2, so that it estimates through
cross-validation the optimal value of bWidth.

```
Elements in Quantitative Finance 37
```

## 3 Distance Metrics

## 3.1 Motivation

In Section 2, we have studied important numerical properties of the empirical
correlation (and by extension, covariance) matrix. Despite all of its virtues,
correlation suffers from some critical limitations as a measure of codepen-
dence. In this section, we overcome those limitations by reviewing informa-
tion theory concepts that underlie many modern marvels, such as the internet,
mobile phones,file compression, video streaming, or encryption. None of
these inventions would have been possible if researchers had not looked
beyond correlations to understand codependency.
As it turns out, information theory in general, and the concept of Shannon’s
entropy in particular, also have useful applications infinance. The key idea
behind entropy is to quantify the amount of uncertainty associated with a
random variable. Information theory is also essential to ML, because the
primary goal of many ML algorithms is to reduce the amount of uncertainty
involved in the solution to a problem. In this section, we review concepts that
are used throughout ML in a variety of settings, including (1) defining the
objective function in decision tree learning; (2) defining the loss function for
classification problems; (3) evaluating the distance between two random vari-
ables; (4) comparing clusters; and (5) feature selection.

## 3.2 A Correlation-Based Metric

Correlation is a useful measure of linear codependence. Once a correlation
matrix has been denoised and detoned, it can reveal important structural infor-
mation about a system. For example, we could use correlations to identify
clusters of highly interrelated securities. But before we can do that, we need
to address a technical problem: correlation is not a metric, because it does not
satisfy nonnegativity and triangle inequality conditions. Metrics are important
because they induce an intuitive topology on a set. Without that intuitive
topology, comparing non-metric measurements of codependence can lead to
rather incoherent outcomes. For instance, the difference between correlations
(0.9,1.0) is the same as (0.1,0.2), even though the former involves a greater
difference in terms of codependence.
Consider two random vectorsX,Yof sizeT, and a correlation estimate
ρ½X;Y, with the only requirement that σ½X;Y¼ρ½X;Yσ½Xσ½Y, where
σ½X;Yis the covariance between the two vectors andσ½:is the standard
deviation. Pearson’s correlation is one of several correlation estimates that

38 Machine Learning for Asset Managers


satisfy these requirements. Then, the measure dρ½X;Y¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 = 2 ð 1 ρ½X;YÞ
```
p
is
a metric.
To prove that statement,first consider that the Euclidean distance between the

two vectors isd½X;Y¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiP
T
t¼ 1 ðÞXtYt
```
```
2
q
```
. Second, wez-standardize those

vectors asx¼ðXXÞ=σ½X,y¼ðYYÞ=σ½Y, whereXis the mean ofX,
andYis the mean ofY. Consequently,ρ½x;y¼ρ½X;Y. Third, we derive the
Euclidean distanced½x;yas

```
d½x;y¼
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
XT
t¼ 1
```
```
ðÞxtyt^2
```
```
s
```
#### ¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
XT
t¼ 1
```
```
x^2 tþ
```
#### XT

```
t¼ 1
```
```
y^2 t 2
```
#### XT

```
t¼ 1
```
```
xtyt
```
```
vu
ut
¼
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
TþT 2 Tσ½x;y
```
```
p
```
#### ¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
```
```
2 T 1 ρ½x;y
¼ρ½X;Y
```
#### 0

#### BB

#### B@

#### 1

#### CC

#### CA

```
vu
uu
uu
ut ¼
```
```
ffiffiffiffiffiffi
4 T
```
```
p
dρ½X;Y:
```
The implication is thatdρ½X;Yis a linear multiple of the Euclidean distance
between the vectors X;Ygf after z-standardization (d½x;y), hence it inherits the
true-metric properties of the Euclidean distance.
The metricd½x;yhas the property that it is normalized,dρ½X;Y2½ 0 ; 1 ,
becauseρ½X;Y2½ 1 ; 1 . Another property is that it deems more distant two
random variables with negative correlation than two random variables with
positive correlation, regardless of their absolute value. This property makes
sense in many applications. For example, we may wish to build a long-only
portfolio, where holdings in negative-correlated securities can only offset
risk, and therefore should be treated as different for diversification purposes.
In other instances, like in long-short portfolios, we often prefer to consider
highly negatively correlated securities as similar, because the position
sign can override the sign of the correlation. For that case, we can
define an alternative normalized correlation-based distance metric,
djρj½X;Y¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 jρ½X;Yj
```
p
.
Similarly, we can prove thatdjρj½X;Ydescends to a true metric on theℤ= 2 ℤ
quotient. In order to do that, we redefiney¼ðYYÞ=σ½Ysgn½ρ½X;Y, where
sgn½:is the sign operator, so that 0≤ρ½x;y¼jρ½X;Yj. Then, following the
same argument used earlier,

# f

```
Elements in Quantitative Finance 39
```

```
d½x;y¼
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
```
```
2 T 1 ρ½x;y
¼jρ½X;Yj
```
#### 0

#### B@

#### 1

#### CA

```
vu
uu
ut ¼pffiffiffiffiffiffi 2 Tdjρj½X;Y:
```
## 3.3 Marginal and Joint Entropy

The notion of correlation presents three important caveats. First, it quantifies the
linearcodependency between two random variables. It neglects nonlinear
relationships. Second, correlation is highly influenced by outliers. Third, its
application beyond the multivariate Normal case is questionable. We may
compute the correlation between any two real variables, however that correla-
tion is typically meaningless unless the two variables follow a bivariate Normal
distribution. To overcome these caveats, we need to introduce a few informa-
tion-theoretic concepts.
LetXbe a discrete random variable that takes a valuexfrom the setSXwith
probabilityp½x. The entropy ofXis defined as

```
H½X¼
```
#### X​

```
x 2 SX
```
```
p½xlog½p½x;
```
Throughout this section, we will follow the convention that 0log½ 0 ¼0,
since limp→ 0 þplog½p¼0. The value 1=p½xmeasures how surprising an obser-
vation is, because surprising observations are characterized by their low
probability. Entropy is the expected value of those surprises, where the
log½:function prevents thatp½xcancels 1=p½xand endows entropy with
desirable mathematical properties. Accordingly, entropy can be interpreted
as the amount of uncertainty associated with X. Entropy is zero when
all probability is concentrated in a single element of SX.Entropy
reaches a maximum at log½∥SX∥ when X is distributed uniformly,
p½x¼ 1 =∥SX∥; 8 x 2 SX.
LetYbe a discrete random variable that takes a valueyfrom the setSYwith
probabilityp½y. Random variablesXandYdo not need to be defined on the
same probability space. The joint entropy ofXandYis

```
H½X;Y¼
```
#### X​

```
x;y 2 SXSY
```
```
p½x;ylog½p½x;y:
```
In particular, we have thatH½X;Y¼H½Y;X,H½X;X¼H½X,H½X;Y≥
max H½X;H½Ygf , andH½X;Y≤H½XþH½Y.

# f

40 Machine Learning for Asset Managers


It is important to recognize that Shannon’s entropy isfinite only for discrete
random variables. In the continuous case, one should use the limiting density of
discrete points (LDDP), or discretize the random variable, as explained in
Section 3.9(Jaynes 2003).

## 3.4 Conditional Entropy

The conditional entropy ofXgivenYis defined as

```
H½XjY¼H½X;YH½Y¼
```
#### X

```
y 2 SY
```
```
p½y
```
#### X

```
x 2 SX
```
```
p½xjY¼ylog½p½xjY¼y;
```
wherep½xjY¼yis the probability thatXtakes the valuexconditioned onYhaving
taken the valuey. Following this definition,H½XjYis the uncertainty we expect in
Xif we are told the value ofY. Accordingly,H½XjX¼0, andH½X≥H½XjY.

## 3.5 Kullback–Leibler Divergence

Letpandqbe two discrete probability distributions defined on the same
probability space. The Kullback–Leibler (or KL) divergence betweenpandqis

```
DKL½p∥q¼
```
#### X​

```
x 2 SX
```
```
p½xlog
q½x
p½x
```
#### 

#### ¼

#### X​

```
x 2 SX
```
```
p½xlog
p½x
q½x
```
#### 

#### ;

whereq½x¼ 0 )p½x¼0. Intuitively, this expression measures how muchp
diverges from a reference distributionq. The KL divergence isnota metric: although
it is always nonnegative (DKL½p∥q≥0), it violates the symmetry
(DKL½p∥q6¼DKL½q∥p) and triangle inequality conditions. Note the difference
with the definition of joint entropy, where the two random variables did not
necessarily exist in the same probability space. KL divergence is widely used in
variational inference.

## 3.6 Cross-Entropy

Letpandqbe two discrete probability distributions defined on the same
probability space. Cross-entropy betweenpandqis

```
HC½p∥q¼
```
#### X

```
x 2 SX
```
```
p½xlog½q½x¼H½XþDKL½pjjq:
```
Cross-entropy can be interpreted as the uncertainty associated withX, where we
evaluate its information content using a wrong distributionqrather than the true
distributionp. Cross-entropy is a popular scoring function in classification
problems, and it is particularly meaningful infinancial applications (López de
Prado 2018, section 9.4).

```
Elements in Quantitative Finance 41
```

## 3.7 Mutual Information

Mutual information is defined as the decrease in uncertainty (or informational
gain) inXthat results from knowing the value ofY:

```
I½X;Y¼H½XH½XjY¼H½XþH½YH½X;Y
```
```
¼
```
#### X

```
x 2 SX
```
#### X

```
y 2 SY
```
```
p½x;ylog p½x;y
p½xp½y
```
#### 

```
¼DKL½p½x;y∥p½xp½y¼
```
#### X​

```
y 2 SY
```
```
p½y
```
#### X​

```
x 2 SX
```
```
p½xjylog
p½xjy
p½x
```
#### 

```
¼EY½DKL½p½xjy∥p½x¼
```
#### X​

```
x 2 SX
```
```
p½x
```
#### X​

```
y 2 SY
```
```
p½yjxlog
p½yjx
p½y
```
#### 

```
¼EX½DKL½p½yjx∥p½y:
```
From the above we can see that I½X;Y≥0, I½X;Y¼I½Y;Xand that
I½X;X¼H½X. WhenX and Yare independent,p½x;y¼p½xp½y, hence
I½X;Y¼0. An upper boundary is given by I½X;Y≤min H½X;H½Ygf.
However, mutual information isnota metric, because it does not satisfy the
triangle inequality: I½X;Z≰I½X;YþI½Y;Z. An important attribute of
mutual information is its grouping property,

```
I½X;Y;Z¼I½X;YþI½ðÞX;Y;Z;
```
whereðÞX;Y represents the joint distribution ofXandY. SinceX,Y, andZcan
themselves represent joint distributions, the above property can be used to
decompose mutual information into simpler constituents. This makes mutual
information a useful similarity measure in the context of agglomerative cluster-
ing algorithms and forward feature selection.
Given two arraysxandyof equal size, which are discretized into a regular
grid with a number of partitions (bins) per dimension,Code Snippet 3.1shows
how to compute in python the marginal entropies, joint entropy, conditional
entropies, and the mutual information.

## 3.8 Variation of Information

Variation of information is defined as

```
VI½X;Y¼H½XjYþH½YjX¼H½XþH½Y 2 I½X;Y
¼ 2 H½X;YH½XH½Y¼H½X;YI½X;Y:
```
This measure can be interpreted as the uncertainty we expect in one variable if we are
told the value of other. It has a lower bound inVI½X;Y¼ 0 ⇔X¼Y, and an upper

42 Machine Learning for Asset Managers


bound inVI½X;Y≤H½X;Y. Variation of information is a metric, because it
satisfies the axioms (1) nonnegativity, VI½X;Y≥0; (2) symmetry,
VI½X;Y¼VI½Y;X; and (3) triangle inequality,VI½X;Z≤VI½X;YþVI½Y;Z.
BecauseH½X;Yis a function of the sizes ofSXandSY,VI½X;Ydoes not
have afirm upper bound. This is problematic when we wish to compare
variations of information across different population sizes. The following
quantity is a metric bounded between zero and one for all pairsðÞX;Y:

```
VIe½X;Y¼VI½X;Y
H½X;Y
```
#### ¼ 1 I½X;Y

#### H½X;Y

#### :

FollowingKraskov et al. (2008), a sharper alternative bounded metric is

```
VI
```
#### ≈

#### ½X;Y¼

```
maxfH½XjY;H½YjXg
maxfH½X;H½Yg
```
#### ¼ 1 

#### I½X;Y

```
maxfH½X;H½Yg
```
#### ;

whereVI
≈
½X;Y≤VeI½X;Yfor all pairsðÞX;Y. Following the previous exam-
ple, Code Snippet 3.2computes mutual information, variation of information,
and normalized variation of information.^9
As a summary,Figure 3.1provides a visual representation of how these
concepts are interrelated.

## 3.9 Discretization

Throughout this section, we have assumed that random variables were discrete.
For the continuous case, we can quantize (coarse-grain) the values, and apply
the same concepts on the binned observations. Consider a continuous random
variableX, with probability distribution functionsfX½x. Shannon defined its
(differential) entropy as

#### SNIPPET3.1 MARGINAL,JOINT,CONDITIONALENTROPIES,ANDMUTUALINFORMATION

```
import numpy as np,scipy.stats as ss
from sklearn.metrics import mutual_info_score
cXY=np.histogram2d(x,y,bins)[0]
hX=ss.entropy(np.histogram(x,bins)[0])# marginal
hY=ss.entropy(np.histogram(y,bins)[0])# marginal
iXY=mutual_info_score(None,None,contingency=cXY)
iXYn=iXY/min(hX,hY)# normalized mutual information
hXY=hX+hY-iXY# joint
hX_Y=hXY-hY# conditional
hY_X=hXY-hX# conditional
```
(^9) Also, seehttps://pypi.org/project/pyitlib/.
Elements in Quantitative Finance 43


#### H½X¼

```
ð∞
```
```
∞
```
```
fX½xlog½fX½xdx:
```
The entropy of a Gaussian random variableXisH½X¼ 1 =2log½ 2 πeσ^2 , thus
H½X≈ 1 :42 in the standard Normal case. One way to estimateH½Xon afinite
sample of real values is to divide the range spanning the observed values xgf
intoBXbins of equal sizeΔX,ΔX¼ðmax xgminff xgÞ=BX, giving us

#### H½X≈

#### XBX

```
i¼ 1
```
```
fX½xilog½fX½xiΔX;
```
wherefX½xirepresents the frequency of observations falling within theith bin.
Letp½xibe the probability of drawing an observation within the segmentΔX

#### SNIPPET3.2 MUTUALINFORMATION,VARIATION OFINFORMATION,ANDNORMALIZED

#### VARIATION OFINFORMATION

```
import numpy as np,scipy.stats as ss
from sklearn.metrics import mutual_info_score
#---------------------------------------------------
def varInfo(x,y,bins,norm=False):
# variation of information
cXY=np.histogram2d(x,y,bins)[0]
iXY=mutual_info_score(None,None,contingency=cXY)
hX=ss.entropy(np.histogram(x,bins)[0])# marginal
hY=ss.entropy(np.histogram(y,bins)[0])# marginal
vXY=hX+hY-2*iXY# variation of information
if norm:
hXY=hX+hY-iXY# joint
vXY/=hXY #normalized variation of information
return vXY
```
```
H [ X , Y ]
```
```
H [ X Y ] I [ X , Y ] H [ Y X ]
```
```
VI [ X, Y ]
```
```
H [ X ] H [ Y ]
```
```
Figure 3.1Correspondence between joint entropy, marginal entropies,
conditional entropies, mutual information, and variation of information.
```
44 Machine Learning for Asset Managers


corresponding to theith bin. We can approximatep½xiasp½xi≈fX½xiΔX,
which can be estimated as^p½xi¼Ni=N, whereNiis the number of observations
within theith bin,N¼

#### PBX

```
i¼ 1 Ni, and
```
#### PBX

i¼ 1 p^½xi¼1. This leads to a discretized
estimator of entropy of the form

#### H^½X¼

#### XBX

```
i¼ 1
```
```
Ni
Nlog
```
```
Ni
N
```
#### 

```
þlog½ΔX:
```
Following the same argument, the estimator of the joint entropy is

#### H^½X;Y¼

#### XBX

```
i¼ 1
```
#### XBY

```
j¼ 1
```
```
Ni;j
Nlog
```
```
Ni;j
N
```
#### 

```
þlog½ΔXΔY:
```
From the estimatorsH^½XandH^½X;Y, we can derive estimators for condi-
tional entropies, mutual information, and variation of information. As we can
see from these equations, results may be biased by our choice ofBXandBY. For
the marginal entropy case,Hacine-Gharbi et al. (2012)found that the following
binning is optimal:

```
BX¼round
ζ
6
þ
```
#### 2

```
3 ζ
þ
```
#### 1

#### 3

#### 

```
ζ¼
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
8 þ 324 Nþ 12
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
36 Nþ 729 N^2
```
```
q 3 p
:
```
For the joint entropy case,Hacine-Gharbi and Ravier (2018)found that the
optimal binning is given by

```
BX¼BY¼round
```
#### 1

```
ffiffiffi
2
```
```
p
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
```
```
1 þ
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 þ
```
#### 24 N

```
1 ^ρ^2
```
```
vu s
ut
```
#### 2

(^64)

#### 3

(^75) ;
whereρ^is the estimated correlation betweenXandY. Code Snippet 3.3modifies
the previous function varInfo, so that it now incorporates the optimal binning
derived by function numBins.

## 3.10 Distance between Two Partitions

In the previous sections, we have derived methods to evaluate the similarity
between random variables. We can extend these concepts to the problem of
comparing two partitions of the same data set, where the partitions can be
considered random to some extent (Meila 2007). A partitionPof a data setD
is an unordered set of mutually disjoint nonempty subsets:

```
Elements in Quantitative Finance 45
```

```
P¼fDkgk¼ 1 ;...;K;
∥Dk∥> 0 ; 8 k;
Dk∩Dl¼∅; 8 k6¼l;
```
```
∪
```
```
k
k¼ 1
Dk¼D:
```
Let us define the uncertainty associated withP. First, we set the probability of
picking any elementd 2 Daspe½d¼ 1 =‖D‖. Second, we define the probability
that an element d 2 D picked at random belongs to subset Dk as
p½k¼‖Dk‖=‖D‖. This second probabilityp½kis associated with a discrete
random variable that takes a valuekfromS¼ 1 ;...;Kgf. Third, the uncer-
tainty associated with this discrete random variable can be expressed in terms of
the entropy

#### H½P¼

#### XK

```
k¼ 1
```
```
p½klog½p½k:
```
#### SNIPPET3.3 VARIATION OFINFORMATION ONDISCRETIZEDCONTINUOUSRANDOM

#### VARIABLES

```
def numBins(nObs,corr=None):
# Optimal number of bins for discretization
if corr is None:# univariate case
z=(8+324*nObs+12*(36*nObs+729*nObs**2)**.5)**(1/3.)
b=round(z/6.+2./(3*z)+1./3)
else:# bivariate case
b=round(2**-.5*(1+(1+24*nObs/(1.-corr**2))**.5)**.5)
return int(b)
#---------------------------------------------------
def varInfo(x,y,norm=False):
# variation of information
bXY=numBins(x.shape[0],corr=np.corrcoef(x,y)[0,1])
cXY=np.histogram2d(x,y,bXY)[0]
iXY=mutual_info_score(None,None,contingency=cXY)
hX=ss.entropy(np.histogram(x,bXY)[0])# marginal
hY=ss.entropy(np.histogram(y,bXY)[0])# marginal
vXY=hX+hY-2*iXY# variation of information
if norm:
hXY=hX+hY-iXY# joint
vXY/=hXY# normalized variation of information
return vXY
```
46 Machine Learning for Asset Managers


From the above we can see thatH½Pdoes not depend on‖D‖, but on the relative
sizes of the subsets. Given a second partitionP^0 ¼fD^0 k 0 gk¼ 1 ;...;K, we can define a
second random variable that takes a valuek^0 fromS^0 ¼ 1 ;...;K^0 gf. The joint
probability that an elementd 2 Dpicked at random belongs to subsetDkinP
and also belongs to subsetD^0 k 0 inP^0 is

```
p½k;k^0 ¼
∥Dk∩D^0 k 0 ∥
‖D‖
```
#### :

The joint entropy is defined as

#### H½P;P^0 ¼

#### XK

```
k¼ 1
```
#### XK^0

```
k^0 ¼ 1
```
```
p½k;k^0 log½p½k;k^0 ;
```
and the conditional entropy isH½PjP^0 ¼H½P;P^0 H½P. The mutual informa-
tion is

```
I½P;P^0 ¼H½PH½PjP^0 ¼
```
#### XK

```
k¼ 1
```
#### XK^0

```
k^0 ¼ 1
```
```
p½k;k^0 log
p½k;k^0 
p½kp½k^0 
```
#### 

#### ;

and the variation of information is

```
VI½P;P^0 ¼H½PjP^0 þH½P^0 jP;
```
whereH½PjP^0 measures the amount of information aboutPthat we lose and
H½P^0 jPmeasures the amount of information aboutP^0 that we gain when going
from partitionPtoP^0. This definition of variation of information has several
properties, among which wefind that (1) it is a metric; (2) it has an absolute upper
boundary atVI½P;P^0 ≤log½‖D‖(like entropy); and (3) if the number of subsets is
bounded by a constantK, withK≤

```
ffiffiffiffiffiffiffi
‖D‖
```
p
, thenVI½P;P^0 ≤2log½K. These three
properties are important because they allow us to normalize the distance between
partitions, and compare partitioning algorithms across different data sets. In the
context of unsupervised learning, variation of information is useful for comparing
outcomes from a partitional (non-hierarchical) clustering algorithm.

## 3.11 Experimental Results

The mutual information quantifies the amount of information shared by two
random variables. The normalized mutual information takes real values within
the range½ 0 ; 1 , like the absolute value of the correlation coefficient. Also like
the correlation coefficient (or its absolute value), neither the mutual information
nor the normalized mutual information are true metrics. The mutual information
between two random standardized Gaussian variablesXandYwith correlationρ
is known to beI½X;Y¼ 1 =2log½ 1 ρ^2 .

```
Elements in Quantitative Finance 47
```

It is in this sense that we can consider the normalized mutual information as
the information-theoretic analogue to linear algebra’s correlation coefficient.
Next, we study how both statistics perform under different scenarios.

```
3.11.1 No Relationship
```
We begin by drawing two arrays, x and e, of random numbers from a standard
Gaussian distribution. Then we computey¼ 0 xþe¼e, and evaluate the
normalized mutual information as well as the correlation between x and y.
Code Snippet 3.4details these calculations.

Figure 3.2representsyagainstx, which as expected resembles a cloud.
Correlation and normalized mutual information are both approximately zero.

```
3.11.2 Linear Relationship
```
In this example, we impose a strong linear relationship between x and y, by setting
y¼ 100 xþe. Now the correlation is approximately 1, and the normalized
mutual information is also very high, approximately 0.9. Still, the normalized
mutual information is not 1, because there is some degree of uncertainty asso-
ciated with e. For instance, should we imposey¼ 104 xþe, then the normalized
mutual information would be 0.995.Figure 3.3plots this relationship.

#### SNIPPET3.4 CORRELATION ANDNORMALIZEDMUTUALINFORMATION OFTWO

#### INDEPENDENTGAUSSIANRANDOMVARIABLES

```
def mutualInfo(x,y,norm=False):
# mutual information
bXY=numBins(x.shape[0],corr=np.corrcoef(x,y)[0,1])
cXY=np.histogram2d(x,y,bXY)[0]
iXY=mutual_info_score(None,None,contingency=cXY)
if norm:
hX=ss.entropy(np.histogram(x,bXY)[0])# marginal
hY=ss.entropy(np.histogram(y,bXY)[0])# marginal
iXY/=min(hX,hY)# normalized mutual information
return iXY
#---------------------------------------------------
size,seed=5000,0
np.random.seed(seed)
x=np.random.normal(size=size)
e=np.random.normal(size=size)
y=0*x+e
nmi=mutualInfo(x,y,True)
corr=np.corrcoef(x,y)[0,1]
```
48 Machine Learning for Asset Managers


```
3.11.3 Nonlinear Relationship
```
In this example, we impose a symmetric relationship across the x-axis between
x and y, by settingy¼ 100 jxjþe. Now the correlation is approximately 0, and
the normalized mutual information is approximately 0.64. As expected, the
correlation has failed to recognize the strong relationship that exists between x

```
3
```
```
corr=0.0015
nmi=0.0068
```
```
y = 0 x + ε
```
```
2
```
```
1
```
```
0
```
```
–1
```
```
–2
```
```
–3
–4 –3 –2 –1 0 1 2 3 4
Figure 3.2Scatterplot of two independent Gaussian random variables.
```
```
200
```
```
400
300
```
```
corr=0.9999
nmi=0.8907
```
```
y = 100 x + ε
```
```
100
0
–100
–200
–300
–400
–4 –3 –2 –1 0 1 2 3 4
Figure 3.3 Scatterplot of two Gaussian random variables with a linear
relationship.
```
```
Elements in Quantitative Finance 49
```

and y, because that relationship is nonlinear. In contrast, the mutual information
recognizes that we can extract a substantial amount of information from x that is
useful to predict y, andvice versa. Figure 3.4plots this relationship.
Unlike in the linear case, raising the coefficient from 10^2 to 10^4 will not
substantially increase the normalized mutual information. In this example, the
main source of uncertainty is not e. The normalized mutual information is high,
but not 1, because knowing y does not suffice to know x. In fact, there are two
alternative values of x associated with each value of y.

## 3.12 Conclusions

Correlations are useful at quantifying the linear codependency between random
variables. This form of codependency accepts various representations as a
distance metric, such as dρ½X;Y¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
2 ðÞ^1 ρ½X;Y
```
q
,or
djρj½X;Y¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 jρ½X;Yj
```
```
p
```
. However, when variablesXandYare bound by a
nonlinear relationship, the above distance metric misjudges the similarity of
these variables. For nonlinear cases, we have argued that the normalized varia-
tion of information is a more appropriate distance metric. It allows us to answer
questions regarding the unique information contributed by a random variable,
without having to make functional assumptions. Given that many ML algo-
rithms do not impose a functional form on the data, it makes sense to use them in
conjunction with entropy-based features.

```
y = 100| x | + ε
corr=–0.008
350 nmi=0.6439
300
250
200
150
100
50
0
–4 –3 –2 –1 0 1 2 3 4
Figure 3.4Scatterplot of two Gaussian random variables with a nonlinear
relationship.
```
50 Machine Learning for Asset Managers


## 3.13 Exercises

1 Draw 1,000 observations from a bivariate Normal distribution with unit
standard deviations and a correlation coefficientρ2 1 ;: 5 ; 0 ;: 5 ; 1 gf.
a Discretize the samples, following the method described inSection 3.9.
b ComputeH½X,H½Y,H½X;Y,H½XjY,I½X;Y,VI½X;YandVIe½X;Y.
c AreH½XandH½Yaffected byρ?
d AreH½X;Y,H½XjY,I½X;Y,VI½X;Y, andVIe½X;Yaffected byρ?
2 Repeat Exercise 1, this time for 1 million observations. What variables are
impacted by the different sample size?
3 Repeat Exercise 2, where this time you use the discretization stepBXfrom
Exercise 1. How does this impact the results?
4 What is the main advantage of variation of information over mutual informa-
tion? Can you think of a use case infinance where mutual information is
more appropriate than variation of information?
5 Consider the two correlation-based distance metrics we discussed inSection
3.2. Can you think of a use case where those distance metrics would be
preferable to the normalized variation of information?
6 Code in Python a function to compute the KL divergence between two
discrete probability distributions.
7 Code in Python a function to compute the cross-entropy of two discrete
probability distributions.
8 Prove thatdρ 2 ½X;Y¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ρ½X;Y^2
```
```
q
is also a proper metric.
```
```
Elements in Quantitative Finance 51
```

## 4 Optimal Clustering

## 4.1 Motivation

A clustering problem consists of a set of objects and a set of features associated
with those objects. The goal is to separate the objects into groups (called
clusters) using the features, where intragroup similarities are maximized, and
intergroup similarities are minimized. It is a form of unsupervised learning,
because we do not provide examples to assist the algorithm in solving this task.
Clustering problems appear naturally infinance, at every step of the investment
process. For instance, analysts may look for historical analogues to current
events, a task that involves developing a numerical taxonomy of events.
Portfolio managers often cluster securities with respect to a variety of features,
to derive relative values among peers. Risk managers are keen to avoid the
concentration of risks in securities that share common traits. Traders wish to
understandflows affecting a set of securities, to determine whether a rally or
sell-off is idiosyncratic to a particular security, or affects a category shared by a
multiplicity of securities. In tackling these problems, we use the notions of
distance we studied inSection 3. This section focuses on the problem offinding
the optimal number and composition of clusters.

## 4.2 Proximity Matrix

Consider a data matrixX, of orderNbyF,whereNis the number of objects andFis
the number of features. We use theFfeatures to compute the proximity between the
Nobjects, as represented by anNxNmatrix. The proximity measure can indicate
either similarity (e.g., correlation, mutual information) or dissimilarity (e.g., a
distance metric). It is convenient but not strictly necessary that dissimilarity mea-
sures satisfy the conditions of a metric: nonnegativity, symmetry and triangle
inequality (Kraskov et al. 2008). The proximity matrix can be represented as an
undirected graph where the weights are a function of the similarity (the more similar,
the greater the weight) or dissimilarity (the more dissimilar, the smaller the weight).
Then the clustering problem is equivalent to breaking the graph into connected
components (disjoint connected subgraphs), one for each cluster. When forming the
proximity matrix, it is a good idea to standardize the input data, to prevent that one
feature’s scale dominates over the rest.

## 4.3 Types of Clustering

There are two main classes of clustering algorithms: partitional and hierarchi-
cal. Partitional techniques create a one-level (un-nested) partitioning of the
objects (each object belongs to one cluster, and to one cluster only).

52 Machine Learning for Asset Managers


Hierarchical techniques produce a nested sequence of partitions, with a single, all-
inclusive cluster at the top and singleton clusters of individual points at the
bottom. Hierarchical clustering algorithms can be divisive (top-down) or agglom-
erative (bottom-up). By restricting the growth of a hierarchical tree, we can derive
a partitional clustering from any hierarchical clustering. However, one cannot
generally derive a hierarchical clustering from a partitional one.
Depending on the definition of cluster, we can distinguish several types of
clustering algorithms, including the following:

1 Connectivity:This clustering is based on distance connectivity, like hier-
archical clustering. For an example infinance, seeLópez de Prado (2016).
2 Centroids:These algorithms perform a vector quantization, like k-means.
For an example infinance, seeLópez de Prado and Lewis (2018).
3 Distribution: Clusters are formed using statistical distributions, e.g., a
mixture of Gaussians.
4 Density:These algorithms search for connected dense regions in the data
space. Examples include DBSCAN and OPTICS.
5 Subspace:Clusters are modeled on two dimensions, featuresandobserva-
tions. An example is biclustering (also known as coclustering). For instance,
they can help identify similarities in subsets of instrumentsandtime periods
simultaneously.^10
Some algorithms expect as input a measure of similarity, and other algorithms
expect as input a measure of dissimilarity. It is important to make sure that you
pass the right input to a particular algorithm. For instance, a hierarchical
clustering algorithm typically expects distance as an input, and it will cluster
together items within a neighborhood. Centroids, distribution and density
methods expect vector-space coordinates, and they can handle distances
directly. However, biclustering directly on the distance matrix will cluster
together the most distant elements (the opposite of what say k-means would
do). One solution is to bicluster on the reciprocal of distance.
If the number of features greatly exceeds the number of observations, the curse of
dimensionality can make the clustering problematic: most of the space spanning the
observations will be empty, making it difficult to identify any groupings. One
solution is to project the data matrixXonto a low-dimensional space, similar to
how PCA reduces the number of features (Steinbach et al. 2004; Ding and He 2004).
An alternative solution is to project the proximity matrix onto a low-dimensional
space, and use it as a new X matrix. In both cases, the procedure described inSection
2 can help identify the number of dimensions associated with signal.

(^10) For an illustration, seehttps://quantdare.com/biclustering-time-series/.
Elements in Quantitative Finance 53


## 4.4 Number of Clusters

Partitioning algorithmsfind the composition of un-nested clusters, where the
researcher is responsible for providing the correct number of clusters. In practice,
researchers often do not know in advance what the number of clusters should be.
The“elbow method”is a popular technique that stops adding clusters when the
marginal percentage of variance explained does not exceed a predefined thresh-
old. In this context, the percentage of variance explained is defined as the ratio of
the between-group variance to the total variance (an F-test). One caveat of this
approach is that the threshold is often set arbitrarily (Goutte et al. 1999).
In this section we present one algorithm that recovers the number of clusters
from a shuffled block-diagonal correlation matrix.López de Prado and Lewis
(2018)denote this algorithm ONC, since it searches for theoptimal number of
clusters. ONC belongs to the broader class of algorithms that apply the silhou-
ette method (Rousseeuw 1987). Although we typically focus onfinding the
number of clusters within a correlation matrix, this algorithm can be applied to
any generic observation matrix.

```
4.4.1 Observations Matrix
```
If your problem does not involve a correlation matrix, or you already possess an
observation matrix, you may skip this section.^11 Otherwise, assume that we
haveNvariables that follow a multivariate Normal distribution characterized by
a correlation matrixρ, whereρi;jis the correlation between variablesiandj.Ifa
strong common component is present, it is advisable to remove it by applying
the detoning method explained inSection 2, because a factor exposure shared
by all variables may hide the existence of partly shared exposures.
For the purposes of correlation clustering, we can follow at least three
approaches: (a) circumvent theXmatrix, by directly defining the distance

matrix asdi;j¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
2 1 ρi;j
```
```
r
or a similar transformation (see Section 3); (b)
```
use the correlation matrix asX; (c) derive theXmatrix asXi;j¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
2 1 ρi;j
```
```
r
,
```
or a similar transformation (the distance of distances approach). The advantage
of options (b) and (c) is that the distance between two variables will be a
function of multiple correlation estimates, and not only one, which makes the
analysis more robust to the presence of outliers. The advantage of option (c) is

(^11) Ideally, your observations matrix will be based on one of the information-theoretic metrics explained
in Section 3. However, I must concede that correlation is still more prevalent infinance. ONC is
agnostic as to how the observations matrix is formed, so the purpose of this section is to explain one
way of computing this matrix for readers who feel more comfortable using correlations.
54 Machine Learning for Asset Managers


that it acknowledges that a change fromρi;j¼ 0 :9toρi;j¼ 1 :0 is greater than a
change fromρi;j¼ 0 :1toρi;j¼ 0 :2. In this Section we follow approach (c), thus

we define the observations matrix asXi;j¼

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
2 1 ρi;j
```
r
.
The clustering of correlation matrices is peculiar in the sense that the features
match the observations: we try to group observations where the observations
themselves are the features (hence the symmetry ofX). MatrixXappears to be a
distance matrix, but it is not. It is still an observations matrix, on which distances
can be evaluated.
For large matricesX, generally it is good practice to reduce its dimension via
PCA.TheideaistoreplaceXwith its standardized orthogonal projection onto a
lower-dimensional space, where the number of dimensions is given by the number
of eigenvalues inX’s correlation matrix that exceedλþ(seeSection 2). The
resulting observations matrix,Xe, of sizeNxF, has a higher signal-to-noise ratio.

```
4.4.2 Base Clustering
```
At this stage, we assume that we have a matrix that expresses our observations
in a metric space. This matrix may have been computed as described in the
previous section, or applying some other method. For example, the matrix may
be based on the variation of information between random variables, as
explained inSection 3. Next, let us discuss the base clustering algorithm. One
possibility would be to use the k-means algorithm on our observation matrix.^12
While k-means is simple and frequently effective, it does have two notable
limitations:first, the algorithm requires an user-set number of clustersK, which
is not necessarily optimal a priori; second, the initialization is random, and
hence the effectiveness of the algorithm can be similarly random.
In order to address these two concerns, we need to modify the k-means
algorithm. Thefirst modification we make is to introduce an objective function,
so that we canfind the“optimalK.”For this, we choose the silhouette score
introduced byRousseeuw (1987). As a reminder, for a given elementiand a
given clustering, the silhouette coefficientSiis defined as

```
Si¼ biai
maxfai;big
;i¼ 1 ;...;N;
```
whereaiis the average distance betweeniand all other elements in the same
cluster, andbiis the average distance betweeniand all the elements in the

(^12) Another possibility is to use a hierarchical algorithm, where the base clustering occurs at the
dendrogram’s distance that maximizes the quality of the partitions. For an example, seehttps://
ssrn.com/abstract=3512998
Elements in Quantitative Finance 55


nearest cluster of whichiis not a member. Effectively, this is a measure
comparing intracluster distance and intercluster distance. A value Si¼ 1
means that elementiis clustered well, whileSi¼1 means thatiwas clustered
poorly. For a given partition, our measure of clustering qualityqis defined as

```
q¼
Effiffiffiffiffiffiffiffiffiffiffiffiffiffiffi½Sigf
V½Sigf
```
```
p ;
```
where E½Sigfis the mean of the silhouette coefficients and V½Sigfis the
variance of the silhouette coefficients. The second modification we make
deals with k-mean’s initialization problem. At the base level, our clustering
algorithm performs the following operation:first, evaluate the observation
matrix; second, we perform a double for...loop. In thefirst loop, we try
differentk¼ 2 ;...;Non which to cluster via k-means for one given initializa-
tion, and evaluate the qualityqfor each clustering. The second loop repeats the
first loop multiple times, thereby attempting different initializations. Third, over
these two loops, we select the clustering with the highestq. Code Snippet 4.1
implements this procedure, andFigure 4.1summarizes the workflow.

#### SNIPPET4.1 BASECLUSTERING

```
import numpy as np,pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples
#---------------------------------------------------
def clusterKMeansBase(corr0,maxNumClusters=10,n_init=10):
x,silh=((1-corr0.fillna(0))/2.)**.5,pd.Series()# observations matrix
for init in range(n_init):
for i in xrange(2,maxNumClusters+1):
kmeans_=KMeans(n_clusters=i,n_jobs=1,n_init=1)
kmeans_=kmeans_.fit(x)
silh_=silhouette_samples(x,kmeans_.labels_)
stat=(silh_.mean()/silh_.std(),silh.mean()/silh.std())
if np.isnan(stat[1]) or stat[0]>stat[1]:
silh,kmeans=silh_,kmeans_
newIdx=np.argsort(kmeans.labels_)
corr1=corr0.iloc[newIdx]# reorder rows
```
```
corr1=corr1.iloc[:,newIdx]# reorder columns
clstrs={i:corr0.columns[np.where(kmeans.labels_==i)[0]].tolist() \
for i in np.unique(kmeans.labels_) }# cluster members
silh=pd.Series(silh,index=x.index)
return corr1,clstrs,silh
```
56 Machine Learning for Asset Managers


```
4.4.3 Higher-Level Clustering
```
Our third modification to k-means deals with clusters of inconsistent quality.
The base clustering may capture the more distinct clusters, while missing the
less apparent ones. To address this issue, we evaluate the qualityqkof each
clusterk¼ 1 ;...;Kgiven the clustering quality scores obtained from the base
clustering algorithm. We then take the average qualityq, andfind the set of
clusters with quality below average, qkjqk<q;k¼ 1 ;...;Kgf. Let us denote
asK 1 the number of clusters in that set,K 1 <K. If the number of clusters to
rerun isK 1 ≤1, then we return the clustering given by the base algorithm.
However, ifK 1 ≥2, we rerun the clustering of the items in thoseK 1 clusters,
while the rest are considered acceptably clustered.
We form a new (reduced) observations matrix out of the elements that
compose theK 1 clusters, and rerun the base clustering algorithm on that reduced
correlation matrix. Doing so will return a, possibly new, clustering for those
elements inK 1. To check its efficacy, we compare the average cluster quality

```
Input
correlation
matrix ρ
```
```
Base clustering algo
```
```
NO
```
```
YES
i = 1 k = k + 1
```
```
i = i + 1
```
```
k ≤ N
```
```
k = 2 and
X = sqrt[.5(1–p)]
```
```
i ≤ imax
```
```
NO
```
```
Cluster using K-means
for k clusters using X,
Evaluate quality
(t-stat of silhouette scores)
```
```
Return highest-
quality clustering
YES
```
```
YES
```
```
NO
```
```
Figure 4.1Structure of ONC’s base clustering stage.
```
```
Elements in Quantitative Finance 57
```

before and after reclustering those elements inK 1. If the average cluster quality
improves, we return the accepted clustering from the base clustering concate-
nated with the new clustering for the redone nodes. Otherwise, we return the
clustering formed by the base algorithm.Code Snippet 4.2implements this
operation in python, andFigure 4.2summarizes the workflow.

#### SNIPPET4.2 TOP-LEVEL OFCLUSTERING

```
from sklearn.metrics import silhouette_samples
#---------------------------------------------------
def makeNewOutputs(corr0,clstrs,clstrs2):
clstrsNew={}
for i in clstrs.keys():
clstrsNew[len(clstrsNew.keys())]=list(clstrs[i])
for i in clstrs2.keys():
clstrsNew[len(clstrsNew.keys())]=list(clstrs2[i])
newIdx=[j for i in clstrsNew for j in clstrsNew[i]]
corrNew=corr0.loc[newIdx,newIdx]
x=((1-corr0.fillna(0))/2.)**.5
kmeans_labels=np.zeros(len(x.columns))
for i in clstrsNew.keys():
idxs=[x.index.get_loc(k) for k in clstrsNew[i]]
kmeans_labels[idxs]=i
silhNew=pd.Series(silhouette_samples(x,kmeans_labels),
index=x.index)
return corrNew,clstrsNew,silhNew
#---------------------------------------------------
def clusterKMeansTop(corr0,maxNumClusters=None,n_init=10):
if maxNumClusters==None:maxNumClusters=corr0.shape[1]-1
corr1,clstrs,silh=clusterKMeansBase(corr0,maxNumClusters= \
min(maxNumClusters,corr0.shape[1]-1),n_init=n_init)
clusterTstats={i:np.mean(silh[clstrs[i]])/ \
np.std(silh[clstrs[i]]) for i in clstrs.keys()}
tStatMean=sum(clusterTstats.values())/len(clusterTstats)
redoClusters=[i for i in clusterTstats.keys() if \
clusterTstats[i]<tStatMean]
if len(redoClusters)<=1:
return corr1,clstrs,silh
else:
keysRedo=[j for i in redoClusters for j in clstrs[i]]
corrTmp=corr0.loc[keysRedo,keysRedo]
tStatMean=np.mean([clusterTstats[i] for i in redoClusters])
corr2,clstrs2,silh2=clusterKMeansTop(corrTmp, \
maxNumClusters=min(maxNumClusters, \
corrTmp.shape[1]-1),n_init=n_init)
```
58 Machine Learning for Asset Managers


## 4.5 Experimental Results

We now design a Monte Carlo experiment to verify the accuracy of the ONC
algorithm introduced earlier:first, we create anNxNcorrelation matrixρfrom
random draws with a predefined number of blocksK, where intrablock correla-
tion is high and across-block correlation is low; second, we shuffle that correla-
tion matrix. Third, we apply ONC, and verify that the ONC algorithm recovers
the blocks we injected.^13

## 4.5.1 Generation of Random Block Correlation Matrices

Given the tupleðÞN;M;K, we wish to create a random block correlation matrix
of sizeNxN, made up ofKblocks, each of size greater or equal thanM. Let us
describe the procedure for randomly partitioningNitems intoKdisjoint groups,
each of size at leastM. Note that this is equivalent to randomly partitioning
N^0 ¼NKMðÞ 1 items intoKgroups each of size at least 1, so we reduce
our analysis to that. Consider randomly choosingK1 distinct items, denoted
as a setB, from the setA¼ðÞ 1 ;...;N^0  1 , then addN^0 toB, so thatBis of size
K. Thus,Bcontainsi 1 ;...;iK, where 1≤i 1 <i 2 <...<iK¼N^0. GivenB,
consider theKpartition setsC 1 ¼ 0 ;...;i 1 1;C 2 ¼i 1 ;...;i 2 1;...; and
CK¼iK 1 ;...;iK1. Given thatijare distinct, each partition contains at least
one element as desired, and furthermore completely partitions the set
ðÞ 0 ;...;N^0  1. In doing so, each setCj contains ijij 1 elements for
j¼ 1 ;...;K, lettingi 0 ¼0. We can generalize again by addingM1 elements
to each block.
Let each blockk¼ 1 ;...;Khave sizexkbyxk, wherexk≥M, thus implying
x 1 þ...þxK¼N≥MK. First, for each blockk, we create a time series of
lengthTthat is drawn from independent and identically distributed (IID)

```
# Make new outputs, if necessary
corrNew,clstrsNew,silhNew=makeNewOutputs(corr0, \
{i:clstrs[i] for i in clstrs.keys() if i not in redoClusters}, \
clstrs2)
newTstatMean=np.mean([np.mean(silhNew[clstrsNew[i]])/ \
np.std(silhNew[clstrsNew[i]]) for i in clstrsNew.keys()])
if newTstatMean<=tStatMean:
return corr1,clstrs,silh
else:
return corrNew,clstrsNew,silhNew
```
(^13) I thank Michael J. Lewis for his help in carrying out this experiment.
Elements in Quantitative Finance 59


standard Gaussians, then make copies of that to each column of a matrixXof
sizeðÞT;xk. Second, we add to eachXi;ja random Gaussian noise with standard
deviationσ>0. By design, the columns ofXwill be highly correlated for small
σ, and less correlated for largeσ. Third, we evaluate the covariance matrixΣX
for the columns ofX, and addΣXas a block toΣ. Fourth, we add toΣanother
covariance matrix with one block but largerσ. Finally, we derive the correlation
matrixρassociated withΣ.

```
Input
correlation
matrix ρ
```
```
Top-level clustering algo
```
```
Cluster ρ using base clustering algo
```
```
Evaluate quality ( t - stat of silhouette
scores) of each cluster
```
```
NOYES
```
```
Keep good (high-
quality) clusters
```
```
Redo instruments in
bad (low-quality)
clusters
```
```
Return clustering from
base clustering algo
```
```
Return good + redone
clusters
```
```
New clustering
higher quality?
```
Figure 4.2Structure of ONC’s higher-level stage.
Source:López de Prado and Lewis (2018)

60 Machine Learning for Asset Managers


By construction,ρhasKblocks with high correlations inside each block, and
low correlations otherwise.Figure 4.3is an example of a correlation matrix
constructed this way.Code Snippet 4.3implements this operation in python.

#### SNIPPET4.3 RANDOMBLOCKCORRELATIONMATRIXCREATION

```
import numpy as np,pandas as pd
from scipy.linalg import block_diag
from sklearn.utils import check_random_state
#---------------------------------------------------
def getCovSub(nObs,nCols,sigma,random_state=None):
#Sub correl matrix
rng=check_random_state(random_state)
if nCols==1:return np.ones((1,1))
ar0=rng.normal(size=(nObs,1))
ar0=np.repeat(ar0,nCols,axis=1)
ar0+=rng.normal(scale=sigma,size=ar0.shape)
ar0=np.cov(ar0,rowvar=False)
return ar0
#---------------------------------------------------
def getRndBlockCov(nCols,nBlocks,minBlockSize=1,sigma=1.,
random_state=None):
#Generate a block random correlation matrix
rng=check_random_state(random_state)
parts=rng.choice(range(1,nCols-(minBlockSize-1)*nBlocks), \
nBlocks-1,replace=False)
parts.sort()
parts=np.append(parts,nCols-(minBlockSize-1)*nBlocks)
parts=np.append(parts[0],np.diff(parts))-1+minBlockSize
cov=None
for nCols_ in parts:
cov_=getCovSub(int(max(nCols_*(nCols_+1)/2.,100)), \
nCols_,sigma,random_state=rng)
if cov is None:cov=cov_.copy()
else:cov=block_diag(cov,cov_)
return cov
#---------------------------------------------------
def randomBlockCorr(nCols,nBlocks,random_state=None,
minBlockSize=1):
#Form block corr
rng=check_random_state(random_state)
```
```
cov0=getRndBlockCov(nCols,nBlocks,
minBlockSize=minBlockSize,sigma=.5,random_state=rng)
cov1=getRndBlockCov(nCols,1,minBlockSize=minBlockSize,
sigma=1.,random_state=rng)# add noise
```
```
Elements in Quantitative Finance 61
```

```
4.5.2 Number of Clusters
```
Using the above described procedure, we create random NxN correlation
matrices withKblocks of size at leastM. We shuffle the rows and columns of
each correlation matrix, so that the blocks are no longer identifiable. Then, we
test the efficacy of the ONC algorithm in recovering the number and composi-
tion of those blocks. For our simulations, we choseN¼ 20 ; 40 ; 80 ;160. As we
would expect clusters to be formed of at least two objects, we setM¼2, and
thus necessarilyK=N≤ 1 =2. For eachN, we testK¼ 3 ; 6 ;...,uptoN=2.
Finally, we test 1,000 random generations for each of these parameter sets.
Figure 4.4displays various boxplots for these simulations. In particular, for
K=Nin a given bucket, we display the boxplot of the ratio ofKpredicted by the
clustering (denoted E½KÞto the actualKtested. Ideally, this ratio should be near

1. Results indicate that ONC frequently recovers the correct number of clusters,
with some small errors.
    As a reminder, in a boxplot, the central box has the bottom set to the 25th
percentile of the data (Q1), while the top is set to the 75th percentile (Q3). The

```
cov0+=cov1
corr0=cov2corr(cov0)
corr0=pd.DataFrame(corr0)
return corr0
```
```
0.3
```
```
0.4
```
```
0.5
```
```
0.6
```
```
0.7
```
```
0.8
```
```
0.9
```
```
1.0
```
Figure 4.3Example of a random block correlation matrix, before shuffling.
Source:López de Prado and Lewis (2018)

62 Machine Learning for Asset Managers


interquartile range (IQR) is set to Q3-Q1. The median is displayed as a line
inside the box. The “whiskers” extend to the largest datum less than
Q 3 þ 1 : 5 IQR, and the smallest datum greater thanQ 1 – 1 : 5 IQR. Points outside
that range are considered outliers.

## 4.6 Conclusions

In this section, we have studied the problem of determining the optimal com-
position and number of clusters by a partitioning algorithm. We have made three
modifications to the k-means algorithm: (1) we have defined an objective
function that measures the quality of the clusters; (2) we have addressed k-
mean’s initialization problem by rerunning the algorithm with alternative seeds;
and (3) an upper-level clustering looks for better partitions among the clusters
the exhibit below-average quality. Experimental results show that the algorithm
effectively recovers the number and composition of the clusters injected into a
block-diagonal matrix.
We have applied the proposed solution to random correlation matrices,
however nothing in the method prevents its application to other kinds of
matrices. The starting point of the algorithm is an observations matrix, which
can be defined in terms of correlation-based metrics, variation of information, or
some other function.

```
0.98
```
```
(–0.001, 0.1] (0.1, 0.2] (0.2, 0.3]
[ K / N deciles]
```
```
(–0.3, 0.4] (0.4, 0.5]
```
```
1.00
```
```
1.02
E
[ K
```
```
] /
```
```
K
```
```
1.04
```
```
1.06
```
```
Boxplot groupted by K / N deciles
```
Figure 4.4 Boxplots of estimatedK/actualKfor bucketedK/N.
Source:López de Prado and Lewis (2018)

```
Elements in Quantitative Finance 63
```

## 4.7 Exercises

1 What is the main difference between outputs from hierarchical and partition-
ing clustering algorithms? Why can’t the output from the latter be converted
into the output of the former?
2 Is MSCI’s GICS classification system an example of hierarchical or parti-
tioning clustering? Using the appropriate algorithm on a correlation matrix,
try to replicate the MSCI classification. To compare the clustering output
with MSCI’s, use the clustering distance introduced inSection 3.
3 ModifyCode Snippets 4.1and 4.2 to work with a spectral biclustering algorithm.
Do you get fundamentally different results? Hint: Remember that, as proximity
matrix, biclustering algorithms expect a similarity matrix, not a distance matrix.
4 Repeat the experimental analysis, where this time ONC’s base algorithm
selects the number of clusters using the“elbow method.”Do you recover the
true number of clusters consistently? Why?
5InSection 2, we used a different method for building block-diagonal correla-
tion matrices. In that method, all blocks had the same size. Repeat the
experimental analysis on regular block-diagonal correlation matrices. Do
you get better or worse results? Why?

64 Machine Learning for Asset Managers


## 5 Financial Labels

## 5.1 Motivation

Section 4discussed clustering, a technique that searches for similarities within a
data set of features (anXmatrix). Clustering is an unsupervised learning
method, in the sense that the algorithm does not learn through examples. In
contrast, a supervised learning algorithm solves a task with the help of examples
(ayarray). There are two main types of supervised learning problems: regres-
sion and classification. In regression problems, examples are drawn from an
infinite population, which can be countable (like integers) or uncountable (like
real values). In classification problems, examples are drawn from afinite set of
labels (either categorical or ordinal). When there is no intrinsic ordering
between the values, labels represent the observations from a categorical vari-
able, like male versus female. When there is intrinsic ordering between the
values, labels represent the observations from an ordinal variable, like credit
ratings. Real variables can be discretized into categorical or ordinal labels.
Researchers need to ponder very carefully how they define labels, because
labels determine the task that the algorithm is going to learn. For example, we
may train an algorithm to predict the sign of today’s return for stock XYZ, or
whether that stock’snext5%movewillbepositive(arunthatspansa
variable number of days). The features needed to solve both tasks can be
very different, as thefirst label involves a point forecast whereas the second
label relates to a path-dependent event. For example, the sign of a stock’s
daily return may be unpredictable, while a stock’s probability of rallying
(unconditional on the time frame) may be assessable. That some features
failed to predict one type of label for a particular stock does not mean that
they will fail to predict all types of labels for that same stock. Since investors
typically do not mind making money one way or another, it is worthwhile to
try alternative ways of defining labels. In this section, we discuss four
important labeling strategies.

## 5.2 Fixed-Horizon Method

Virtually all academic studies infinancial ML use thefixed-horizon labeling
method (see the bibliography). Consider a features matrixXwithIrows,
fXigi¼ 1 ;...;I, sampled from a series of bars with indext¼ 1 ;...;T, where
I≤T. We compute the price return over a horizonhas

```
rti; 0 ;ti; 1 ¼
pti; 1
pti; 0
```
####  1 ;

```
Elements in Quantitative Finance 65
```

where ti; 0 is the bar index associated with theith observed features and
ti; 1 ¼ti; 0 þhis the bar index after thefixed horizon ofhbars has elapsed.
This method assigns a labelyi¼ 1 ; 0 ; 1 gf to an observationXi, with

```
yi¼
```
```
1ifrti; 0 ;ti; 1 <τ;
0ifjrti; 0 ;ti; 1 j≤τ;
1ifrti; 0 ;ti; 1 >τ;
```
#### 8

#### <

#### :

whereτis a predefined constant threshold. When the bars are sampled at a regular
chronological time frequency, they are known as time bars. Time bars are also very
popular in thefinancial literature. The combination of time bars withfixed-horizon
labeling results infixed time horizons. Despite its popularity, there are several
reasons to avoid this method. First, returns computed on time bars exhibit substantial
heteroscedasticity, as a consequence of intraday seasonal activity patterns. Applying
a constant thresholdτin conjunction with heteroskedastic returnsfrti; 0 ;ti; 1 gi¼ 1 ;...;I
will transfer that seasonality to the labels, thus the distribution of labels will not
be stationary. For instance, obtaining a 0 label at the open or the close is more
informative (in the sense of unexpected) than obtaining a 0 label around noon,
or during the night. One solution is to apply thefixed-horizon method on tick,
volume or dollar bars (seeLópez de Prado 2018a). Another solution is to label
based on standardized returnszti; 0 ;ti; 1 , adjusted for the volatility predicted over
the interval of bars½ti; 0 ;ti; 1 ,

```
yi¼
```
```
1ifzti; 0 ;ti; 1 <τ;
0ifjzti; 0 ;ti; 1 j≤τ;
1ifzti; 0 ;ti; 1 >τ:
```
#### 8

#### <

#### :

A second concern of thefixed horizon method is that it dismisses all information
regarding the intermediate returns within the interval½ti; 0 ;ti; 1 . This is problematic,
because positions are typically managed according to profit taking and stop-loss
levels. In the particular case of stop losses, those levels may be self-imposed by the
portfolio manager, or enforced by the risk department. Accordingly,fixed-horizon
labels may not be representative of the outcome of a real investment.
A third concern of thefixed-horizon method is that investors are rarely
interested in forecasting whether a return will exceed a thresholdτat a precise
point in timeti; 0 þh. It would be more practical to predict the side of the next
absolute return that exceeds a thresholdτwithin a maximum horizonh. The
following method deals with these three concerns.

## 5.3 Triple-Barrier Method

Infinancial applications, a more realistic method is to make labels reflect the
success or failure of a position. A typical trading rule adopted by portfolio

66 Machine Learning for Asset Managers


managers is to hold a position until thefirst of three possible outcomes occurs:
(1) the unrealized profit target is achieved, and the position is closed with
success; (2) the unrealized loss limit is reached, and the position is closed
with failure; (3) the position is held beyond a maximum number of bars, and
the position is closed without neither failure nor success. In a time plot of
position performance, thefirst two conditions define two horizontal barriers,
and the third condition defines a vertical barrier. The index of the bar associated
with thefirst touched barrier is recorded asti; 1. When the profit-taking barrier is
touchedfirst, we label the observation asyi¼1. When the stop-loss barrier is
touchedfirst, we label the observation asyi¼1. When the vertical barrier is
touchedfirst, we have two options: we can either label ityi¼0, or we can label
ityi¼sgn½rti; 0 ;ti; 1 . SeeLópez de Prado (2018a)for code snippets that implement
the triple-barrier method in python.
Setting profit taking and stop-loss barriers requires knowledge of the position
sideassociated with theith observation. When the position side is unknown, we can
still set horizontal barriers as a function of the volatility predicted over the interval
of bars½ti; 0 ;ti; 0 þh,wherehis the number of bars until the vertical barrier is
touched. In this case, the barriers will be symmetric, because without side informa-
tion we cannot know which barrier means profit and which barrier means loss.
A key advantage of the triple-barrier method over thefixed-horizon method is
that the former incorporates information about the path spanning the interval of
bars½ti; 0 ;ti; 0 þh. In practice, the maximum holding period of an investment
opportunity can be defined naturally, and the value ofhis not subjective. One
disadvantage is that touching a barrier is a discrete event, which may or may not
occur by a thin margin. This caveat is addressed by the following method.

## 5.4 Trend-Scanning Method

In this section we introduce a new labeling method that does not require
defininghor profit-taking or stop-loss barriers. The general idea is to identify
trends and let them run for as long and as far as they may persist, without setting
any barriers.^14 In order to accomplish that,first we need to define what con-
stitutes a trend.
Consider a series of observationsfxtgt¼ 1 ;...;T, wherextmay represent the
price of a security we aim to predict. We wish to assign a labelyt2 1 ; 0 ; 1 gf to
every observation inxt, based on whetherxtis part of a downtrend, no-trend, or
an uptrend. One possibility is to compute thet-value (^t^β 1 ) associated with the
estimated regressor coefficient (^β 1 ) in a linear time-trend model,

(^14) The idea of trend scanning is the fruit of joint work with my colleagues Lee Cohn, Michael Lock,
and Yaxiong Zeng.
Elements in Quantitative Finance 67


```
xtþl¼β 0 þβ 1 lþεtþl
```
```
^t^β 1 ¼
β^ 1
^σβ^ 1
```
#### ;

where^σ^β 1 is the standard error of^β 1 , andl¼ 0 ;...;L1, andLsets the look-
forward period.Code Snippet 5.1computes thist-value on the sample deter-
mined byL.

Different values ofLlead to differentt-values. To solve this indetermination,
we can try a set of alternative values forL, and pick the value ofLthat maximizes
j^tβ 1 j. In this way, we labelxtaccording to the most statistically significant trend
observed in the future, out of multiple possible look-forward periods.Code
Snippet 5.2implements this procedure in python. The arguments are molecule,
which is the index of observations we wish to label; close, which is the time
series of xtgf ; and span, which is the set of values ofLthat the algorithm will

#### SNIPPET5.1T-VALUE OF ALINEARTREND

```
import statsmodels.api as sm1
#---------------------------------------------------
def tValLinR(close):
# tValue from a linear trend
x=np.ones((close.shape[0],2))
x[:,1]=np.arange(close.shape[0])
ols=sm1.OLS(close,x).fit()
return ols.tvalues[1]
```
#### SNIPPET5.2 IMPLEMENTATION OF THETREND-SCANNINGMETHOD

```
def getBinsFromTrend(molecule,close,span):
’’’
Derive labels from the sign of t-value of linear trend
Output includes:
```
- t1: End time for the identified trend
- tVal: t-value associated with the estimated trend coefficient
- bin: Sign of the trend
’’’
out=pd.DataFrame(index=molecule,columns=[’t1’,’tVal’,’bin’])
hrzns=xrange(*span)
for dt0 in molecule:
    df0=pd.Series()
    iloc0=close.index.get_loc(dt0)
    if iloc0+max(hrzns)>close.shape[0]:continue

68 Machine Learning for Asset Managers


evaluate, in search for the maximum absolutet-value. The output is a data frame
where the index is the timestamp of thext, column t1 reports the timestamp of
the farthest observation used tofind the most significant trend, column tVal
reports thet-value associated with the most significant linear trend among the
set of evaluated look-forward periods, and column bin is the label (yt).
Trend-scanning labels are often intuitive, and can be used in classification as well
as regression problems. We present an example in the experimental results section.

## 5.5 Meta-labeling

A common occurrence infinance is that we know whether we want to buy or sell
a particular security, however we are less certain about how much we should
bet. A model that determines a position’ssidemay not be the best one to
determine that position’ssize. Perhaps the size should be a function of the
recent performance of the model, whereas that recent performance is irrelevant
to forecast the position’s side.
Having a good bet-sizing model is extremely important. Consider an invest-
ment strategy with a precision of 60% and a recall of 90%. A 90% recall means
that the strategy predicts ninety out of one hundred true investment opportu-
nities. A 60% precision means that out of one hundred predicted opportunities,
sixty are true. Such strategy will lose money if bet sizes are small on the sixty
true positives and large on the forty false positives. As investors, we have no
(legitimate) control over prices, and the key decision we can and must make is to
size bets properly.
Meta-labeling is useful for avoiding or at least reducing an investor’s expo-
sure to false positives. It achieves that by giving up some recall in exchange for
higher precision. In the example above, adding a meta-labeling layer may result
in a recall of 70% and a precision of 70%, hence improving the model’s F1-
score (the harmonic average of precision and recall). SeeLópez de Prado
(2018a)for a python implementation of meta-labeling.

```
for hrzn in hrzns:
dt1=close.index[iloc0+hrzn-1]
df1=close.loc[dt0:dt1]
df0.loc[dt1]=tValLinR(df1.values)
dt1=df0.replace([-np.inf,np.inf,np.nan],0).abs().idxmax()
out.loc[dt0,[’t1’,’tVal’,’bin’]]=df0.index[-1],df0[dt1],
np.sign(df0[dt1])# prevent leakage
out[’t1’]=pd.to_datetime(out[’t1’])
out[’bin’]=pd.to_numeric(out[’bin’],downcast=’signed’)
return out.dropna(subset=[’bin’])
```
```
Elements in Quantitative Finance 69
```

The goal of meta-labeling is to train a secondary model on the prediction
outcomes of a primary model, where losses are labeled as“ 0 ”and gains are
labeled as“1.”Therefore, the secondary model does not predict the side.
Instead, the secondary model predicts whether the primary model will succeed
or fail at a particular prediction (a meta-prediction). The probability asso-
ciated with a“ 1 ”prediction can then be used to size the position, as explained
next.

```
5.5.1 Bet Sizing by Expected Sharpe Ratio
```
Letpbe the expected probability that the opportunity yields a profitπ, and 1p
the expected probability that the opportunity yields a profit–π(i.e., a loss), for
some symmetric payoff of magnitudeπ>0. The expected profit from the
opportunity is μ¼pπþðÞ 1 pðÞ¼π πðÞ 2 p 1. The expected variance
from the opportunity isσ^2 ¼ 4 π^2 pðÞ 1 p. The Sharpe ratio associated with
the opportunity can therefore be estimated as

```
z¼
μ
σ
```
#### ¼

```
p^12
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
pðÞ 1 p
```
```
p ;
```
withz2ðÞ∞;þ∞. Assuming that the Sharpe ratio of opportunities follows a
standard Gaussian distribution, we may derive the bet size asm¼ 2 Z½z1,
whereZ½:is the cumulative distribution function of the standard Gaussian, and
m2½ 1 ; 1 follows a uniform distribution.

```
5.5.2 Ensemble Bet Sizing
```
Considernmeta-labeling classifiers that make a binary prediction on whether an
opportunity will be profitable or not,yi¼ 0 ; 1 gf ,i¼ 1 ;...;n. The true prob-
ability of being profitable isp, and predictionsyiare drawn from a Bernoulli
distribution, so
Pn
i¼ 1 yieB½n;p, whereB½n;pis a binomial distribution ofn
trials with probabilityp. Assuming that the predictions are independent and
identically distributed, the de Moivre–Laplace theorem states that the distribu-
tion of

Pn
i¼ 1 yiconverges to a Gaussian with meannpand variancenpðÞ^1 pas
n→∞. Accordingly, limn→∞^1 n
Pn
i¼ 1 yieN½p;pðÞ^1 p=n, which is a particular case
of the Lindeberg–Lévy theorem.
Let us denote as^pthe average prediction across thenmeta-labeling classi-
fiers, ^p¼ 1 =n
Pn
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi i¼^1 yi. The standard deviation associated with ^p is
p^ðÞ 1 ^p=n

p

. Subject to the null hypothesis H 0 :p¼ 1 =2, the statistic

t¼ðp^ 1 = 2 Þ=

```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
^pðÞ 1 p^
```
```
p ffiffiffi
n
p
, with t2ðÞ∞;þ∞, follows a t-student
```
70 Machine Learning for Asset Managers


distribution withn1 degrees of freedom. We may derive the bet size as
m¼ 2 tn 1 ½t1, wheretn 1 ½:is the cumulative distribution function of the t-
student withn1 degrees of freedom, andm2½ 1 ; 1 follows a uniform
distribution.

## 5.6 Experimental Results

In this section, we demonstrate how labels can be generated using the trend-
scanning method.Code Snippet 5.3generates a Gaussian random walk, to
which we add a sine trend, to force some inflection points. In that way, we
create concave and convex segments that should make the determination of
trends more difficult. We then call the getBinsFromTrend function, to retrieve
the trend horizons,t-values, and labels.

Figure 5.1plots a Gaussian random walk with trend, where the colors differ-
entiate four clearly distinct trends, with 1 labels plotted in yellow and1 labels

#### SNIPPET5.3 TESTING THETREND-SCANNINGLABELINGALGORITHM

```
df0=pd.Series(np.random.normal(0,.1,100)).cumsum()
df0+=np.sin(np.linspace(0,10,df0.shape[0]))
df1=getBinsFromTrend(df0.index,df0,[3,10,1])
mpl.scatter(df1.index,df0.loc[df1.index].values,
c=df1[’bin’].values, cmap=’viridis’)
mpl.savefig(’fig 5.1.png’);mpl.clf();mpl.close()
mpl.scatter(df1.index,df0.loc[df1.index].values,c=c,cmap=’viridis’)
```
```
Figure 5.1Example of trend-scanning labels.
```
```
Elements in Quantitative Finance 71
```

plotted in violet. These binary labels, although appropriate for classification
problems, omit information about the strength of the trend.
To correct for that omission,Figure 5.2plots the same Gaussian random walk
with trend, where the colors indicate the magnitude of thet-value. Highly
positivet-values are plotted in yellow, and highly negativet-values are plotted
in violet. Positive values close to zero are plotted in green, and negative values
close to zero are plotted in blue. This information could be used in regression
models, or as sample weights in classification problems.

## 5.7 Conclusions

In this section, we have presented four alternative labeling methods that can be
useful infinancial applications. Thefixed-horizon method, although implemented
in mostfinancial studies, suffers from multiple limitations. Among these limita-
tions, we listed that the distribution offixed-horizon labels may not be stationary,
that these labels dismiss path information, and that it would be more practical to
predict the side of the next absolute return that exceeds a given threshold.
The triple-barrier method answers these concerns by simulating the outcome
of a trading rule. One disadvantage is that touching a barrier is a discrete event,
which may or may not occur by a thin margin. To address that, the trend-
scanning method determines the side of the strongest linear trend among
alternative look-forward periods, with its associatedp-value. Trend-scanning
labels are often intuitive, and can be used in classification as well as regression
problems. Finally, the meta-labeling method is useful in applications where the
side of a position is predetermined, and we are only interested in learning the

```
Figure 5.2Example of trend-scanningt-values.
```
72 Machine Learning for Asset Managers


size. A proper sizing method can help improve a strategy’s performance, by
giving up some of the recall in exchange for higher precision.

## 5.8 Exercises

1 Given a time series of E-mini S&P 500 futures, compute labels on one-
minute time bars using thefixed-horizon method, whereτis set at two
standard deviations of one-minute returns.
a Compute the overall distribution of the labels.
b Compute the distribution of labels across all days, for each hour of the
trading session.
c How different are the distributions in (b) relative to the distribution in (a)?
Why?
2 Repeat Exercise 1, where this time you label standardized returns (instead of
raw returns), where the standardization is based on mean and variance
estimates from a lookback of one hour. Do you reach a different conclusion?
3 Repeat Exercise 1, where this time you apply the triple-barrier method on
volume bars. The maximum holding period is the average number of bars per
day, and the horizontal barriers are set at two standard deviations of bar
returns. How do results compare to the solutions from Exercises 1 and 2?
4 Repeat Exercise 1, where this time you apply the trend-scanning method,
with look-forward periods of up to one day. How do results compare to the
solutions from Exercises 1, 2, and 3?
5 Using the labels generated in Exercise 3 (triple-barrier method):

```
a Fit a random forest classifier on those labels. Use as features estimates of
mean return, volatility, skewness, kurtosis, and various differences in
moving averages.
b Backtest those predictions using as a trading rule the same rule used to
generate the labels.
c Apply meta-labeling on the backtest results.
dRefit the random forest on meta-labels, adding as a feature the label
predicted in (a).
e Size (a) bets according to predictions in (d), and recompute the backtest.
```
```
Elements in Quantitative Finance 73
```

## 6 Feature Importance Analysis

## 6.1 Motivation

Imagine that you are given ten puzzles, each of a thousand pieces, where all of the
pieces have been shuffled into the same box. You are asked to solve one particular
puzzle out of the ten. A reasonable way to proceed is to divide your task into two
steps. In thefirst step, you try to isolate the one thousand pieces that are important to
your problem, and discard the nine thousands pieces that are irrelevant. For
example, you may notice that about one tenth of the pieces are made of plastic,
and the rest are made of paper. Regardless of the pattern shown on the pieces, you
know that discarding all paper pieces will isolate a single puzzle. In the second step,
you try tofit a structure on the one thousand pieces that you have isolated. Now you
may make a guess of what the pattern is, and organize the pieces around it.
Now consider a researcher interested in modeling a dynamic system as a
function of many different candidate explanatory variables. Only a small subset
of those candidate variables are expected to be relevant, however the researcher
does not know in advance which. The approach generally followed in the
financial literature is to try tofit a guessed algebraic function on a guessed subset
of variables, and see which variables appear to be statistically significant (subject
to that guessed algebraic function being correct, including all interaction effects
among variables). Such an approach is counterintuitive and likely to miss impor-
tant variables that would have been revealed by unexplored specifications.
Instead, researchers could follow the same steps that they would apply to the
problem of solving a puzzle:first, isolate the important variables, irrespective of
any functional form, and only then try tofit those variables to a particular
specification that is consistent with those isolated variables. ML techniques
allow us to disentangle the specification search from the variable search.
In this section, we demonstrate that ML provides intuitive and effective tools for
researchers who work on the development of theories. Our exposition runs counter
to the popular myth that supervised ML models are black-boxes. According to that
view, supervised ML algorithmsfind predictive patterns, however researchers have
no understanding of thosefindings. In other words, the algorithm has learned
something, not the researcher. This criticism is unwarranted.
Even if a supervised ML algorithm does not yield a closed-form algebraic
solution (like, for example, a regression method would do), an analysis of its
forecasts can tell us what variables are critically involved in a particular
phenomenon, what variables are redundant, what variables are useless, and
how the relevant variables interact with each other. This kind of analysis is
known as“feature importance,”and harnessing its power will require us to use
everything we have learned in the previous sections.

74 Machine Learning for Asset Managers


## 6.2p-Values

The classical regression framework makes a number of assumptions regarding
thefitted model, such as correct model specification, mutually uncorrelated
regressors, or white noise residuals. Conditional on those assumptions being
true, researchers aim to determine the importance of an explanatory variable
through a hypothesis test.^15 A popular way of expressing a variable’s signifi-
cance is through itsp-value, a concept that dates back to the 1700s (Brian and
Jaisson 2007). Thep-value quantifies the probability that, if the true coefficient
associated with that variable is zero, we could have obtained a result equal or
more extreme than the one we have estimated. It indicates how incompatible the
data are with a specified statistical model. However, ap-value does not measure
the probability that neither the null nor the alternative hypothesis is true, or that
the data are random. And ap-value does not measure the size of an effect, or the
significance of a result.^16 The misuse ofp-values is so widespread that the
American Statistical Association has discouraged their application going for-
ward as a measure of statistical significance (Wasserstein et al. 2019). This casts
a doubt over decades of empirical research in Finance. In order to search for
alternatives to thep-value,first we must understand its pitfalls.

```
6.2.1 A Few Caveats ofp-Values
```
Afirst caveat ofp-values is that they rely on the strong assumptions outlined earlier.
When those assumptions are inaccurate, ap-value could be low even though the true
value of the coefficient is zero (a false positive), and thep-value could be high even
though the true value of the coefficient is not zero (a false negative).
A second caveat ofp-values is that, for highly multicollinear (mutually correlated)
explanatory variables,p-values cannot be robustly estimated. In multicollinear
systems, traditional regression methods cannot discriminate among redundant
explanatory variables, leading to substitution effects between relatedp-values.
A third caveat ofp-values is that they evaluate a probability that is not
entirely relevant. Given a null hypothesisH 0 and an estimated coefficientβ^,
thep-value estimates the probability of obtaining a result equal or more extreme
thanβ^, subject toH 0 being true. However, researchers are often more interested
in a different probability, namely, the probability ofH 0 being true, subject to
having observed^β. This probability can be computed using Bayes theorem, alas
at the expense of making additional assumptions (Bayesian priors).^17

(^15) Some significance tests also demand that the residuals follow a Gaussian distribution.
(^16) For additional details, read the“Statement on Statistical Significance and P-Values”by the
17 American Statistical Association (2016)and Wasserstein and Lazar (2016).
We revisit this argument inSection 8.2.
Elements in Quantitative Finance 75


A fourth caveat ofp-values is that it assesses significance in-sample. The
entire sample is used to solve two tasks: estimating the coefficients and deter-
mining their significance. Accordingly,p-values may be low (i.e., significant)
for variables that have no out-of-sample explanatory (i.e., forecasting) value.
Running multiple in-sample tests on the same data set is likely to produce a false
discovery, a practice known asp-hacking.
In summary,p-values require that we make many assumptions (caveat #1) in
order to produce a noisy estimate (caveat #2) of a probability that we do not
really need (caveat #3), and that may not be generalizable out-of-sample (caveat
#4). These are not superfluous concerns. In theory, a key advantage of classical
methods is that they provide a transparent attribution of significance among
explanatory variables. But since that classical attribution has so many caveats in
practice, perhaps classical methods could use some help from modern computa-
tional techniques that overcome those caveats.

```
6.2.2 A Numerical Example
```
Consider a binary random classification problem composed of forty features,
wherefive are informative, thirty are redundant, andfive are noise.Code
Snippet 6.1implements function getTestData, which generates informative,
redundant, and noisy features. Informative features (marked with the “I_”
prefix) are those used to generate labels. Redundant features (marked with the
“R_”prefix) are those that are formed by adding Gaussian noise to a randomly
chosen informative feature (the lower the value of sigmaStd, the greater the
substitution effect). Noise features (marked with the“N_”prefix) are those that
are not used to generate labels.
Figure 6.1plots thep-values that result from a logit regression on those
features. The horizontal bars report thep-values, and the vertical dashed line
marks the 5% significance level. Only four out of the thirty-five nonnoise
features are deemed statistically significant: I_1, R_29, R_27, I_3. Noise
features are ranked as relatively important (with positions 9, 11, 14, 18, and
26). Fourteen of the features ranked as least important are not noise. In short,
thesep-values misrepresent the ground truth, for the reasons explained earlier.
Unfortunately,financial data sets tend to be highly multicollinear, as a result
of common risk factors shared by large portions of the investment universe:
market, sector, rating, value, momentum, quality, duration, etc. Under these
circumstances,financial researchers should cease to rely exclusively onp-
values. It is important forfinancial researchers to become familiar with addi-
tional methods to determine what variables contain information in a particular
phenomenon.

76 Machine Learning for Asset Managers


## 6.3 Feature Importance

In this section, we study how two of ML’s feature importance methods address
the caveats ofp-values, with minimal assumptions, using computational tech-
niques. Other examples of ML interpretability methods are accumulated local
effects (Apley 2016) and Shapley values (Štrumbelj 2014).

```
6.3.1 Mean-Decrease Impurity
```
Suppose that you have a learning sample of sizeN, composed ofFfeatures,
fXfgf¼ 1 ;...;F and one label per observation. A tree-based classification (or
regression) algorithm splits at each nodetits labels into two samples: for a
given featureXf, labels in nodetassociated with aXfbelow a thresholdτare
placed in the left sample, and the rest are placed in the right sample. For each of
these samples, we can evaluate their impurity as the entropy of the distribution
of labels, as the Gini index, or following some other criterion. Intuitively, a
sample is purest when it contains only labels of one kind, and it is most impure

#### SNIPPET6.1 GENERATING ASET OFINFORMED,REDUNDANT,ANDNOISEEXPLANATORY

#### VARIABLES

```
def getTestData(n_features=100,n_informative=25,n_redundant=25,
n_samples=10000,random_state=0,sigmaStd=.0):
#generate a random dataset for a classification problem
from sklearn.datasets import make_classification
np.random.seed(random_state)
X,y=make_classification(n_samples=n_samples,
n_features=n_features-n_redundant,
n_informative=n_informative,n_redundant=0,shuffle=False,
random_state=random_state)
cols=[‘I_’+str(i) for i in xrange(n_informative)]
cols+=[‘N_’+str(i) for i in xrange(n_features-n_informative- \
n_redundant)]
X,y=pd.DataFrame(X,columns=cols),pd.Series(y)
i=np.random.choice(xrange(n_informative),size=n_redundant)
for k,j in enumerate(i):
X[‘R_’+str(k)]=X[‘I_’+str(j)]+np.random.normal(size= \
X.shape[0])*sigmaStd
return X,y
#---------------------------------------------------
import numpy as np,pandas as pd,seaborn as sns
import statsmodels.discrete.discrete_model as sm
X,y=getTestData(40,5,30,10000,sigmaStd=.1)
ols=sm.Logit(y,X).fit()
```
```
Elements in Quantitative Finance 77
```

when its labels follow a uniform distribution. The information gain that results
from a split is measured in terms of the resulting reduction in impurity,

```
Δg½t;f¼i½t
NtðÞ^0
Nt
i½tðÞ^0 
NtðÞ^1
Nt
i½tðÞ^1 ;
```
wherei½tis the impurity of labels at nodet(before the split),i½tðÞ^0 is the
impurity of labels in the left sample, andi½tðÞ^1 is the impurity of labels in the
right sample. At each nodet, the classification algorithm evaluatesΔg½t;ffor
various features infXfgf¼ 1 ;...;F, determines the optimal thresholdτthat max-
imizesΔg½t;ffor each of them, and selects the featurefassociated with greatest
Δg½t;f. The classification algorithm continues splitting the samples further
until no additional information gains can be produced, or some early-stopping
condition is met, such as achieving an impurity below the maximum acceptable
limit.
The importance of a feature can be computed as the weighted information
gain (Δg½t;f) across all nodes where that feature was selected. This tree-based
feature importance concept, introduced byBreiman (2001), is known as mean-
decrease impurity (MDI). By construction, the MDI value associated with each
feature is bounded between 0 and 1, and all combined add up to 1. In the

```
0.0 0.2 0.4 0.6 0.8
```
```
R_29I_1
R_27I_3
I_0R_17
R_23I_2
N_1R_9
N_4R_13
R_3N_2
R_11R_8
R_28N_0
R_20I_4
R_10R_14
R_26R_18
R_24N_3
R_2R_6
R_16R_22
R_15R_25
R_19R_4
R_1R_21
R_12R_0
R_7R_5
```
```
Figure 6.1p-Values computed on a set of explanatory variables.
```
78 Machine Learning for Asset Managers


presence ofFfeatures where all are uninformative (or equally informed), each
MDI value is expected to be 1=F. For algorithms that combine ensembles of
trees, like random forests, we can further estimate the mean and variance of
MDI values for each feature across all trees. These mean and variance estimates,
along with the central limit theorem, are useful in testing the significance of a
feature against a user-defined null hypothesis.Code Snippet 6.2implements an
ensemble MDI procedure. SeeLópez de Prado (2018a)for practical advice on
how to use MDI.

Figure 6.2plots the result of applying MDI to the same random classification
problem discussed inFigure 6.1. The horizontal bars indicate the mean of MDI
values across 1,000 trees in a random forest, and the lines indicate the standard
deviation around that mean. The more trees we add to the forest, the smaller
becomes the standard deviation around the mean. MDI does a good job, in the
sense that all of the nonnoisy features (either informed or redundant) are ranked
higher than the noise features. Still, a small number of nonnoisy features appear
to be much more important than their peers. This is the kind of substitution
effects that we anticipated tofind in the presence of redundant features.Section
6.5 proposes a solution to this particular concern.

#### SNIPPET6.2 IMPLEMENTATION OF ANENSEMBLEMDI METHOD

```
def featImpMDI(fit,featNames):
#feat importance based on IS mean impurity reduction
df0={i:tree.feature_importances_ for i,tree in \
enumerate(fit.estimators_)}
df0=pd.DataFrame.from_dict(df0,orient=‘index’)
df0.columns=featNames
df0=df0.replace(0,np.nan)#because max_features=1
imp=pd.concat({‘mean’:df0.mean(),
‘std’:df0.std()*df0.shape[0]**-.5},axis=1)# CLT
imp/=imp[‘mean’].sum()
return imp
#---------------------------------------------------
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
X,y=getTestData(40,5,30,10000,sigmaStd=.1)
clf=DecisionTreeClassifier(criterion=‘entropy’,max_features=1,
class_weight=‘balanced’,min_weight_fraction_leaf=0)
clf=BaggingClassifier(base_estimator=clf,n_estimators=1000,
max_features=1.,max_samples=1.,oob_score=False)
fit=clf.fit(X,y)
imp=featImpMDI(fit,featNames=X.columns)
```
```
Elements in Quantitative Finance 79
```

Out of the four caveats ofp-values, the MDI method deals with three: (1)
MDI’s computational nature circumvents the need for strong distributional
assumptions that could be false (caveat #1)–we are not imposing a particular
tree structure or algebraic specification, or relying on stochastic or distributional
characteristics of residuals. (2) Whereas betas are estimated on a single sample,
ensemble MDIs are derived from a bootstrap of trees. Accordingly, the variance
of MDI estimates can be reduced by increasing the number of trees in ensemble
methods in general, or in a random forest in particular (caveat 2). This reduces
the probability of false positives caused by overfitting. Also, unlikep-values,
MDI’s estimation does not require the inversion of a possibly ill-conditioned
matrix. (3) The goal of the tree-based classifiers is not to estimate the coeffi-
cients of a given algebraic equation, thus estimating the probability of a
particular null hypothesis is irrelevant. In other words, MDI corrects for caveat
3byfinding the important features in general, irrespective of any particular
parametric specification.
An ensemble estimate of MDI will exhibit low variance given a sufficient
number of trees, hence reducing the concern ofp-hacking. But still, the proce-
dure itself does not involve cross-validation. Therefore, the one caveat of
p-values that MDI does not fully solve is that MDI is also computed in-sample
(caveat #4). To confront thisfinal caveat, we need to introduce the concept of
mean-decrease accuracy.

```
0.00 0.010 0.02 0.03 0.04 0.05
```
```
N_2N_3
```
```
N_0N_1
```
```
N_4R_25
```
```
R_29R_6
R_2R_3
```
```
R_22I_3
```
```
R_20R_4
R_28R_14
```
```
R_26R_10
```
```
R_17R_9
```
```
R_21R_1
```
```
R_23I_0
```
```
R_11R_8
R_0I_4
```
```
R_19R_24
```
```
R_12I_2
```
```
R_7R_15
```
```
R_27R_16
```
```
R_13I_1
R_5R_18
```
```
Figure 6.2Example of MDI results.
```
80 Machine Learning for Asset Managers


```
6.3.2 Mean-Decrease Accuracy
```
A disadvantage of bothp-values and MDI is that a variable that appears to be
significant for explanatory purposes (in-sample) may be irrelevant for forecasting
purposes (out-of-sample). To solve this problem (caveat #4),Breiman (2001)
introduced the mean-decrease accuracy (MDA) method.^18 MDAworks as follows:
first, itfits a model and computes its cross-validated performance; second, it
computes the cross-validated performance of the samefitted model, with the only
difference that it shuffles the observations associated with one of the features. That
gives us one modified cross-validated performance per feature. Third, it derives the
MDA associated with a particular feature by comparing the cross-validated perfor-
mance before and after shuffling. If the feature is important, there should be a
significant decay in performance caused by the shuffling, as long as the features
are independent. An important attribute of MDA is that, like ensemble MDIs, it is not
the result of a single estimate, but rather the average of multiple estimates (one for
each testing set in a k-fold cross-validation).
When features are not independent, MDA may underestimate the importance
of interrelated features. At the extreme, given two highly important but identical
features, MDA may conclude that both features are relatively unimportant,
because the effect of shuffling one may be partially compensated by not shuf-
fling the other. We address this concern inSection 6.5.
MDAvalues are not bounded, and shuffling a feature could potentially improve
the cross-validated performance, when the feature is uninformative to the point of
being detrimental. Because MDA involves a cross-validation step, this method
can be computationally expensive.Code Snippet 6.3implements MDA. See
López de Prado (2018a)for practical advice on how to use MDA.
Figure 6.3plots the result of applying MDA to the same random classification
problem we discussed inFigure 6.2. We can draw similar conclusions as we did
in the MDI example. First, MDA does a good job overall at separating noise
features from the rest. Noise features are ranked last. Second, noise features are
also deemed unimportant in magnitude, with MDA values of essentially zero.
Third, although substitution effects contribute to higher variances in MDA
importance, none is high enough to question the importance of the nonnoisy
features.
Despite its name, MDA does not necessarily rely on accuracy to evaluate the
cross-validated performance. MDA can be computed on other performance scores.
In fact, in the particular case offinance, accuracy is not a particularly good choice.
The reason is, accuracy scores a classifier in terms of its proportion of correct
predictions. This has the disadvantage that probabilities are not taken into account.

(^18) This is sometimes also known as permutation importance.
Elements in Quantitative Finance 81


For example, a classifier may achieve high accuracy even though it made good
predictions with low confidence and bad predictions with high confidence. In the
following section, we introduce a scoring function that addresses this concern.

## 6.4 Probability-Weighted Accuracy

Infinancial applications, a good alternative to accuracy is log-loss (also known
as cross-entropy loss). Log-loss scores a classifier in terms of the average log-
likelihood of the true labels (for a formal definition, see section 9.4 ofLópez de
Prado 2018a). One disadvantage, however, is that log-loss scores are not easy to
interpret and compare. A possible solution is to compute the negative average
likelihood of the true labels (NegAL),

#### SNIPPET6.3 IMPLEMENTATION OFMDA

```
def featImpMDA(clf,X,y,n_splits=10):
#feat importance based on OOS score reduction
from sklearn.metrics import log_loss
from sklearn.model_selection._split import KFold
cvGen=KFold(n_splits=n_splits)
scr0,scr1=pd.Series(),pd.DataFrame(columns=X.columns)
for i,(train,test) in enumerate(cvGen.split(X=X)):
X0,y0=X.iloc[train,:],y.iloc[train]
X1,y1=X.iloc[test,:],y.iloc[test]
fit=clf.fit(X=X0,y=y0)# thefit occurs here
prob=fit.predict_proba(X1)# prediction before shuffling
scr0.loc[i]=-log_loss(y1,prob,labels=clf.classes_)
for j in X.columns:
X1_=X1.copy(deep=True)
np.random.shuffle(X1_[j].values)# shuffle one column
prob=fit.predict_proba(X1_)# prediction after shuffling
scr1.loc[i,j]=-log_loss(y1,prob,labels=clf.classes_)
imp=(-1*scr1).add(scr0,axis=0)
imp=imp/(-1*scr1)
imp=pd.concat({‘mean’:imp.mean(),
‘std’:imp.std()*imp.shape[0]**-.5},axis=1)# CLT
return imp
#---------------------------------------------------
X,y=getTestData(40,5,30,10000,sigmaStd=.1)
clf=DecisionTreeClassifier(criterion=‘entropy’,max_features=1,
class_weight=‘balanced’,min_weight_fraction_leaf=0)
clf=BaggingClassifier(base_estimator=clf,n_estimators=1000,
max_features=1.,max_samples=1.,oob_score=False)
imp=featImpMDA(clf,X,y,10)
```
82 Machine Learning for Asset Managers


```
NegAL¼N^1
```
#### XN^1

```
n¼ 0
```
#### XK^1

```
k¼ 0
```
```
yn;kpn;k;
```
wherepn;kis the probability associated with predictionnof labelkandyn;kis an
indicator function, yn;k 2 0 ; 1 gf , where yn;k¼1 when observation n was
assigned labelkandyn;k¼0 otherwise. This is very similar to log-loss, with
the difference that it averages likelihoods rather than log-likelihoods, so that
NegAL still ranges between 0 and 1.
Alternatively, we can define the probability-weighted accuracy (PWA) as

#### PWA¼

#### XN^1

```
n¼ 0
```
```
ynpnK^1
```
#### 

#### ,

#### XN^1

```
n¼ 0
```
```
pnK^1
```
#### 

#### ;

wherepn¼ maxk pn;kg
andynis an indicator function,yn 2 0 ; 1 gf , where
yn¼1 when the prediction was correct, andyn¼0 otherwise.^19 This is equiva-
lent to standard accuracy when the classifier has absolute conviction in every
prediction (pn¼1 for alln). PWA punishes bad predictions made with high
confidence more severely than accuracy, but less severely than log-loss.

```
0.00
```
```
N_2 R_26
```
```
R_10R_17
```
```
R_14R_23
```
```
R_21
R_9R_1R_2
```
```
R_20R_29
```
```
R_3I_0
R_28R_6
```
```
R_22R_4
R_25I_3
```
```
R_19I_4
```
```
R_11R_8
```
```
R_18R_0
R_15R_27
```
```
R_5R_13
```
```
R_16
```
```
R_24R_7
R_12I_2
I_1
```
```
N_3N_0
N_1N_4
0.01 0.02 0.03 0.04 0.05 0.06 0.07
Figure 6.3Example of MDA results.
```
(^19) The idea of PWA is the fruit of joint work with my colleagues Lee Cohn, Michael Lock, and
Yaxiong Zeng.
Elements in Quantitative Finance 83


## 6.5 Substitution Effects

Substitution effects arise when two features share predictive information.
Substitution effects can bias the results from feature importance methods. In
the case of MDI, the importance of two identical features will be halved, as they
are randomly chosen with equal probability. In the case of MDA, two identical
features may be considered relatively unimportant, even if they are critical,
because the effect of shuffling one may be compensated by the other.

```
6.5.1 Orthogonalization
```
When features are highly codependent, their importance cannot be adjudicated
in a robust manner. Small changes in the observations may have a dramatic
impact on their estimated importance. However, this impact is not random:
given two highly codependent features, the drop in importance from one is
compensated with the raise in importance of the other. In other words, code-
pendence causes substitution effects when evaluating the importance of
features.
One solution to multicollinearity is to apply PCA on the features, derive their
orthogonal principal components, and then run MDI or MDA on those principal
components (for additional details, see chapter 8 ofLópez de Prado 2018a). Features
orthogonalized in this way may be more resilient to substitution effects, with three
caveats: (1) redundant features that result from nonlinear combinations of informa-
tive ones will still cause substitution effects; (2) the principal components may not
have an intuitive explanation; (3) the principal components are defined by eigen-
vectors that do not necessarily maximize the model’s out-of-sample performance
(Witten et al. 2013).

```
6.5.2 Cluster Feature Importance
```
A better approach, which does not require a change of basis, is to cluster similar
features and apply the feature importance analysis at the cluster level. By
construction, clusters are mutually dissimilar, hence taming the substitution
effects. Because the analysis is done on a partition of the features, without a
change of basis, results are usually intuitive.
Let us introduce one algorithm that implements this idea. The clustered
feature importance (CFI) algorithm involves two steps: (1) finding the
number and constituents of the clusters of features; (2) applying the feature
importance analysis on groups of similar features rather than on individual
features.

84 Machine Learning for Asset Managers


```
Step 1: Features Clustering
```
First, we project the observed features into a metric space, resulting in a matrix
fXfgf¼ 1 ;...;F. To form this matrix, one possibility is to follow the correlation-
based approach described inSection 4.4.1. Another possibility is to apply
information-theoretic concepts (such as variation of information; seeSection
3) to represent those features in a metric space. Information-theoretic metrics
have the advantage of recognizing redundant features that are the result of
nonlinear combinations of informative features.^20
Second, we apply a procedure to determine the optimal number and compo-
sition of clusters, such as the ONC algorithm (seeSection 4). Remember that
ONCfinds the optimal number of clusters as well as the composition of those
clusters, where each feature belongs to one and only one cluster. Features that
belong to the same cluster share a large amount of information, and features that
belong to different clusters share only a relatively small amount of information.
Some silhouette scores may be low due one feature being a combination of
multiple features across clusters. This is a problem, because ONC cannot assign
one feature to multiple clusters. In this case, the following transformation may
help reduce the multicollinearity of the system. For each clusterk¼ 1 ;...;K,
replace the features included in that cluster with residual features, where those
residual features do not contain information from featuresoutsideclusterk.To
be precise, letDkbe the subset of index featuresD¼ 1 ;...;Fgf included in
clusterk, whereDk⊂D,∥Dk∥> 0 ; 8 k;Dk∩Dl¼∅; 8 k6¼ l;UKk¼ 1 Dk¼D.
Then, for a given featureXiwherei 2 Dk, we compute the residual feature^εiby
fitting

```
Xn;i¼αiþ
```
X

j 2 ∪l<kDl

```
βi;jXn;jþεn;i
```
wheren¼ 1 ;...;Nis the index of observations per feature. If the degrees of
freedom in the above regression is too low, one option is to use as regressors linear
combinations of the features within each cluster (e.g., following a minimum var-
iance weighting scheme), so that onlyK1 betas need to be estimated. One of
the properties of OLS residuals is that they are orthogonal to the regressors.
Thus, by replacing each featureXiwith its residual equivalent^εi, we remove
from clusterkinformation that is already included in other clusters, while
preserving the information that exclusively belongs to clusterk. Again, this
transformation is not necessary if the silhouette scores clearly indicate that
features belong to their respective clusters.

(^20) For an example of features clustering with an information-theoretic distance metric, seehttps://
ssrn.com/abstract=3517595
Elements in Quantitative Finance 85


```
Step 2: Clustered Importance
```
Step 1 has identified the number and composition of the clusters of features. We
can use this information to apply MDI and MDA on groups of similar features,
rather than on individual features. In the following, we assume that a partitional
algorithm has clustered the features, however this notion of clustered feature
importance can be applied to hierarchical clusters as well.

Clustered MDI

As we saw inSection 6.3.1, the MDI of a feature is the weighted impurity
reduction across all nodes where that feature was selected. We compute the
clustered MDI as the sum of the MDI values of the features that constitute that
cluster. If there is one feature per cluster, then MDI and clustered MDI are the
same. In the case of an ensemble of trees, there is one clustered MDI for each tree,
which allows us to compute the mean clustered MDI, and standard deviation
around the mean clustered MDI, similarly to how we did for the feature MDI.
Code Snippet 6.4implements the procedure that estimates the clustered MDI.

Clustered MDA

The MDA of a feature is computed by comparing the performance of an algorithm
before and after shuffling that feature. When computing clustered MDA, instead of
shuffling one feature at a time, we shuffle all of the features that constitute a given
cluster. If there is one cluster per feature, then MDA and clustered MDA are the

#### SNIPPET6.4 CLUSTEREDMDI

```
def groupMeanStd(df0,clstrs):
out=pd.DataFrame(columns=[‘mean’,‘std’])
for i,j in clstrs.iteritems():
df1=df0[j].sum(axis=1)
out.loc[‘C_’+str(i),‘mean’]=df1.mean()
out.loc[‘C_’+str(i),‘std’]=df1.std()*df1.shape[0]**-.5
return out
#---------------------------------------------------
def featImpMDI_Clustered(fit,featNames,clstrs):
df0={i:tree.feature_importances_ for i,tree in \
enumerate(fit.estimators_)}
df0=pd.DataFrame.from_dict(df0,orient=‘index’)
df0.columns=featNames
df0=df0.replace(0,np.nan)# because max_features=1
imp=groupMeanStd(df0,clstrs)
imp/=imp[‘mean’].sum()
return imp
```
86 Machine Learning for Asset Managers


same.Code Snippet 6.5implements the procedure that estimates the clustered
MDA.

## 6.6 Experimental Results

In this experiment we are going to test the clustered MDI and MDA procedures
on the same data set we used on the nonclustered versions of MDI and MDA
(see Sections 6.3.1and 6.3.2). That data set consisted of forty features, of which
five were informative, thirty were redundant, andfive were noise. First, we
apply the ONC algorithm to the correlation matrix of those features.^21 In a
nonexperimental setting, the researcher should denoise and detone the correla-
tion matrix before clustering, as explained inSection 2. We do not do so in this
experiment as a matter of testing the robustness of the method (results are
expected to be better on a denoised and detoned correlation matrix).

#### SNIPPET6.5 CLUSTEREDMDA

```
def featImpMDA_Clustered(clf,X,y,clstrs,n_splits=10):
from sklearn.metrics import log_loss
from sklearn.model_selection._split import KFold
cvGen=KFold(n_splits=n_splits)
scr0,scr1=pd.Series(),pd.DataFrame(columns=clstrs.keys())
for i,(train,test) in enumerate(cvGen.split(X=X)):
X0,y0=X.iloc[train,:],y.iloc[train]
X1,y1=X.iloc[test,:],y.iloc[test]
fit=clf.fit(X=X0,y=y0)
prob=fit.predict_proba(X1)
scr0.loc[i]=-log_loss(y1,prob,labels=clf.classes_)
for j in scr1.columns:
X1_=X1.copy(deep=True)
for k in clstrs[j]:
np.random.shuffle(X1_[k].values)# shuffle cluster
prob=fit.predict_proba(X1_)
scr1.loc[i,j]=-log_loss(y1,prob,labels=clf.classes_)
imp=(-1*scr1).add(scr0,axis=0)
imp=imp/(-1*scr1)
imp=pd.concat({‘mean’:imp.mean(),
‘std’:imp.std()*imp.shape[0]**-.5},axis=1)
imp.index=[‘C_’+str(i) for i in imp.index]
return imp
```
(^21) As an exercise, we ask the reader to apply ONC on a metric projection of the features computed
using the normalized variation of information.
Elements in Quantitative Finance 87


Figure 6.4shows that ONC correctly recognizes that there are six relevant
clusters (one cluster for each informative feature, plus one cluster of noise features),
and it assigns the redundant features to the cluster that contains the informative
feature from which the redundant features were derived. Given the low correlation
across clusters, there is no need to replace the features with their residuals (as
proposed in Section 6.5.2.1).Code Snippet 6.6implements this example.

Next, we apply our clustered MDI method on that data set.Figure 6.5shows
the clustered MDI output, which we can compare with the unclustered output
reported inFigure 6.2. The“C_”prefix indicates the cluster, and“C_5”is the
cluster associated with the noise features. Clustered features“C_1”is the
second least important, however its importance is more than double the impor-
tance of“C_5.”This is in contrast with what we saw inFigure 6.2, where there
was a small difference in importance between the noise features and some of the
nonnoisy features. Thus, the clustered MDI method appears to work better than
the standard MDI method.Code Snippet 6.7shows how these results were
computed.

#### SNIPPET6.6 FEATURESCLUSTERINGSTEP

```
X,y=getTestData(40,5,30,10000,sigmaStd=.1)
corr0,clstrs,silh=clusterKMeansBase(X.corr(),maxNumClusters=10,
n_init=10)
sns.heatmap(corr0,cmap=‘viridis’)
```
```
N_3 –0.25
```
```
0.00
```
```
0.25
```
```
0.50
```
```
0.75
```
```
1.00
```
```
N_1
```
```
R_0
```
```
R_8
```
```
I_4
```
```
N_18
```
```
N_16
```
```
R_13
```
```
R_1
```
```
I_0
```
```
R_26
```
```
R_17
```
```
R_21
```
```
R_12
```
```
R_24
```
```
I_3
```
```
R_20
```
```
R_2
```
```
R_14
```
```
R_29
```
```
R_29R_4R_2R_20
```
```
I_3
R_24R_12R_21R_17R_26
```
```
I_0R_1
R_13R_16R_18
```
```
I_4R_8R_0N_1N_3
```
```
Figure 6.4ONC clusters together with informative and redundant features.
```
88 Machine Learning for Asset Managers


Finally, we apply our clustered MDA method on that data set.Figure 6.6shows
the clustered MDA output, which we can compare with the unclustered output
reported inFigure 6.3. Again,“C_5”is the cluster associated with the noise
features, and all other clusters are associated with informative and redundant
features. This analysis has reached two correct conclusions: (1)“C_5”has
essentially zero importance, and should be discarded as irrelevant; and (2) all
other clusters have very similar importance. This is in contrast with what we saw
in Figure 6.3, where some nonnoise features appeared to be much more important
than others, even after taking into consideration the standard derivation around
the mean values.Code Snippet 6.8shows how these results were computed.

## 6.7 Conclusions

Most researchers usep-values to evaluate the significance of explanatory vari-
ables. However, as we saw in this section,p-values suffer from four majorflaws.
ML offers feature importance methods that overcome most or all of thoseflaws.

#### SNIPPET6.7 CALLING THEFUNCTIONS FORCLUSTEREDMDI

```
clf=DecisionTreeClassifier(criterion=‘entropy’,max_features=1,
class_weight=‘balanced’,min_weight_fraction_leaf=0)
clf=BaggingClassifier(base_estimator=clf,n_estimators=1000,
max_features=1.,max_samples=1.,oob_score=False)
fit=clf.fit(X,y)
imp=featImpMDI_Clustered(fit,X.columns,clstrs)
```
```
0.00 0.05 0.10 0.15 0.20 0.25 0.30
```
```
C_5
```
```
C_1
```
```
C_0
```
```
C_4
```
```
C_2
```
```
C_3
```
```
Figure 6.5 Clustered MDI.
```
```
Elements in Quantitative Finance 89
```

The MDI and MDA methods assess the importance of features robustly and
without making strong assumptions about the distribution and structure of the
data. Unlikep-values, MDA evaluates feature importance in cross-validated
experiments. Furthermore, unlikep-values, clustered MDI and clustered MDA
estimates effectively control for substitution effects. But perhaps the most
salient advantage of MDI and MDA is that, unlike classical significance ana-
lyses, these ML techniques evaluate the importance of a feature irrespective of
any particular specification. In doing so, they provide information that is
extremely useful for the development of a theory. Once the researcher knows
the variables involved in a phenomenon, she can focus her attention onfinding
the mechanism or specification that binds them together.
The implication is that classical statistical approaches, such as regression
analysis, are not necessarily more transparent or insightful than their ML
counterparts. The perception that ML tools are black-boxes and classical tools
are white-boxes is false. Not only can ML feature importance methods be as
helpful asp-values, but in some cases they can be more insightful and accurate.

#### SNIPPET6.8 CALLING THEFUNCTIONS FORCLUSTEREDMDA

```
clf=DecisionTreeClassifier(criterion=‘entropy’,max_features=1,
class_weight=‘balanced’,min_weight_fraction_leaf=0)
clf=BaggingClassifier(base_estimator=clf,n_estimators=1000,
max_features=1.,max_samples=1.,oob_score=False)
imp=featImpMDA_Clustered(clf,X,y,clstrs,10)
```
```
0.00 0.05 0.10 0.15 0.20 0.25 0.30
```
```
C_5
```
```
C_4
```
```
C_2
```
```
C_1
```
```
C_0
```
```
C_3
```
```
Figure 6.6Clustered MDA.
```
90 Machine Learning for Asset Managers


Afinal piece of advice is to consider carefully what are we interested in
explaining or predicting. InSection 5, we reviewed various labeling methods.
The same features can yield various degrees of importance in explaining or
predicting different types of labels. Whenever possible, it makes sense to apply
these feature importance methods to all of the labeling methods discussed
earlier, and see what combination of features and labels leads to the strongest
theory. For instance, you may be indifferent between predicting the sign of the
next trend or predicting the sign of the next 5% return, because you can build
profitable strategies on either kind of prediction (as long as the feature impor-
tance analysis suggests the existence of a strong theoretical connection).

## 6.8 Exercises

1 Consider a medical test with a false positive rateα¼P½x>τjH 0 , whereH 0
is the null hypothesis (the patient is healthy),xis the observed measurement,
andτis the significance threshold. A test is run on a random patient and
comes back positive (the null hypothesis is rejected). What is the probability
that the patient truly has the condition?
a Is it 1α¼P½x≤τjH 0 (the confidence of the test)?
b Is it 1β¼P½x>τjH 1 (the power, or recall, of the test)?
c Or is it P½H 1 jx>τ(the precision of the test)?
d Of the above, what dop-values measure?
eInfinance, the analogous situation is to test whether a variable is involved
in a phenomenon. Dop-values tell us anything about the probability that
the variable is relevant, given the observed evidence?
2 Consider a medical test whereα¼:01,β¼0, and the probability of the
condition is P½H 1 ¼:001. The test has full recall and a very high confidence.
What is the probability that a positive-tested patient is actually sick? Why is it
much lower than 1αand 1β? What is the probability that a patient is
actually sick after testing positive twice on independent tests?
3 Rerun the examples inSections 6.3.1and 6.3.2, where this time you pass an
argument sigmaStd=0 to the getTestData function. How doFigures 6.2and
6.3 look now? What causes the difference, if there is one?
4 Rerun the MDA analysis inSection 6.3.2, where this time you use probability-
weighted accuracy (Section 6.4) as the scoring function. Are results materially
different? Are they more intuitive or easier to explain? Can you think of other
ways to represent MDA outputs using probability-weighted accuracy?
5 Rerun the experiment inSection 6.6, where this time the distance metric used
to cluster the features is variation of information (Section 3).

```
Elements in Quantitative Finance 91
```

## 7 Portfolio Construction

## 7.1 Motivation

The allocation of assets requires making decisions under uncertainty.
Markowitz (1952)proposed one of the most influential ideas in modernfinan-
cial history, namely, the representation of the problem of investing as a convex
optimization program. Markowitz’s Critical Line Algorithm (CLA) estimates
an“efficient frontier”of portfolios that maximize the expected return subject to
a given level of risk, where portfolio risk is measured in terms of the standard
deviation of returns. In practice, mean-variance optimal solutions tend to be
concentrated and unstable (De Miguel et al. 2009).
There are three popular approaches to reducing the instability in optimal
portfolios. First, some authors attempted to regularize the solution, by injecting
additional information regarding the mean or variance in the form of priors
(Black and Litterman 1992). Second, other authors suggested reducing the
solution’s feasibility region by incorporating additional constraints (Clarke et
al. 2002). Third, other authors proposed improving the numerical stability of the
covariance matrix’s inverse (Ledoit and Wolf 2004).
In Section 2, we discussed how to deal with the instability caused by the noise
contained in the covariance matrix. As it turns out, the signal contained in the
covariance matrix can also be a source of instability, which requires a specia-
lized treatment. In this section, we explain why certain data structures (or types
of signal) make mean-variance solutions unstable, and what we can do to
address this second source of instability.

## 7.2 Convex Portfolio Optimization

Consider a portfolio ofNholdings, where its returns in excess of the risk-free
rate have an expected valueμand an expected covarianceV. Markowitz’s
insight was to formulate the classical asset allocation problem as a quadratic
program,

```
minω
```
#### 1

#### 2

```
ω^0 Vω
```
```
s:t::ω^0 a¼ 1 ;
```
whereacharacterizes the portfolio’s constraints. This problem can be expressed
in Lagrangian form as

```
L½ω;λ¼
```
#### 1

#### 2

```
ω^0 VωλωðÞ^0 a 1
```
92 Machine Learning for Asset Managers


withfirst-order conditions

```
∂L½ω;λ
∂ω
¼Vωλa
```
```
∂L½ω;λ
∂λ
¼ω^0 a 1 :
```
Setting the first-order (necessary) conditions to zero, we obtain that
Vωλa¼ 0 )ω¼λV^1 a and ω^0 a¼a^0 ω¼ 1 )λa^0 V^1 a¼ 1 )
λ¼ 1 =a^0 V^1 a

#### 

```
, thus
```
```
ω¼
V^1 a
a^0 V^1 a
```
#### :

The second-order (sufficient) condition confirms that this solution is the mini-
mum of the Lagrangian:

```
∂L^2 ½ω;λ
∂ω^2
```
```
∂L^2 ½ω;λ
∂ω∂λ
∂L^2 ½ω;λ
∂λ∂ω
```
```
∂L^2 ½ω;λ
∂λ^2
```
(^)
(^)
(^)
(^)
(^)
(^)
(^)
(^)

#### ¼ V

(^0) a 0
a 0
(^)
(^)
¼a^0 a≥ 0 :
(^)
(^)
Let us now turn our attention to a few formulations of the characteristic
vector,a:
1 Fora¼ (^1) NandV¼σIN, whereσ 2 ℝþ,1Nis a vector of ones of sizeN, and
INis an identity matrix of sizeN, then the solution is the equal weights
portfolio (known as the“1/N”portfolio, or the“naïve”portfolio), because
ω¼ (^1) Nσ^1 =Nσ^1

#### 

¼ (^1) N=N.
2 Fora¼ (^1) NandVis a diagonal matrix with unequal entries (Vi;j¼0, for all
i6¼j), then the solution is the inverse-variance portfolio, because
ω¼PN^1
n¼ 1 Vn^1 ;n
fV^1 n;ngn¼ 1 ;...;N:
3 Fora¼ (^1) N, the solution is the minimum variance portfolio.
4 Fora¼μ, the solution maximizes the portfolio’s Sharpe ratio,ω^0 μ=
ffiffiffiffiffiffiffiffiffiffiffiffi
ω^0 Vω
p
,
and the market portfolio isV^1 μ=ð (^10) NV^1 μÞ(Grinold and Kahn 1999).

## 7.3 The Condition Number

Certain covariance structures can make the mean-variance optimization solu-
tion unstable. To understand why, we need to introduce the concept of condition
number of a covariance matrix. Consider a correlation matrix between two
securities,

```
Elements in Quantitative Finance 93
```

```
C¼^1 ρ ρ 1
```
#### 

#### ;

whereρis the correlation between their returns. MatrixCcan be diagonalized as
CW¼WΛas follows. First, we set the eigenvalue equationjCIλj¼0.
Operating,

```
1 λρ
ρ 1 λ¼^0 ) ðÞ^1 λ
```
(^2) ρ (^2) ¼ 0 :
(^)
(^)
(^)
This equation has roots inλ¼ 1 ρ, hence the diagonal elements ofΛare
Λ 1 ; 1 ¼ 1 þρ
Λ 2 ; 2 ¼ 1 ρ:
Second, the eigenvector associated with each eigenvalue is given by the solu-
tion to the system
1 Λ 1 ; 1 ρ
ρ 1 Λ 2 ; 2

#### 

#### W 1 ; 1 W 1 ; 2

#### W 2 ; 1 W 2 ; 2

#### 

#### ¼^0000

#### 

#### :

IfCis not already a diagonal matrix, thenρ6¼ 0, in which case the above system
has solutions in

#### W 1 ; 1 W 1 ; 2

#### W 2 ; 1 W 2 ; 2

#### 

#### ¼

(^1) ffiffiffi
2
p^1 ffiffiffi
2
p
(^1) ffiffiffi
2
p^1 ffiffiffi
2
p

#### 2

(^66)
4

#### 3

(^77)
5 ;
and it is easy to verify that

#### WΛW^0 ¼

#### 1

```
ffiffiffi
2
```
```
p
```
#### 1

```
ffiffiffi
2
```
```
p
1
ffiffiffi
2
```
```
p
```
#### 1

```
ffiffiffi
2
```
```
p
```
#### 2

(^66)
4

#### 3

(^77)
5
1 þρ 0
01 ρ
^1 ffiffiffi
2
p

#### 1

```
ffiffiffi
2
```
```
p
1
ffiffiffi
2
```
```
p
```
#### 1

```
ffiffiffi
2
```
```
p
```
#### 2

(^66)
4

#### 3

(^77)
5
0
¼^1 ρ ρ 1

#### 

#### ¼C:

The trace ofCistr CðÞ¼Λ 1 ; 1 þΛ 2 ; 2 ¼2, soρsets how big one eigenvalue gets
at the expense of the other. The determinant of C is given by
jCj¼Λ 1 ; 1 Λ 2 ; 2 ¼ðÞ 1 þρðÞ¼ 1 ρ 1 ρ^2. The determinant reaches its max-
imum atΛ 1 ; 1 ¼Λ 2 ; 2 ¼1, which corresponds to the uncorrelated case,ρ¼0.
The determinant reaches its minimum atΛ 1 ; 1 ¼0orΛ 2 ; 2 ¼0, which corre-
sponds to the perfectly correlated case,jρj¼1. The inverse ofCis

94 Machine Learning for Asset Managers


#### C^1 ¼WΛ^1 W^0 ¼

#### 1

```
jCj
```
```
1 ρ
ρ 1
```
#### 

#### :

The implication is that the moreρdeviates from zero, the bigger one eigenvalue
becomes relative to the other, causingjCjto approach zero, which makes the
values ofC^1 explode.
More generally, the instability caused by covariance structure can be mea-
sured in terms of the magnitude between the two extreme eigenvalues.
Accordingly, the condition number of a covariance or correlation (or normal,
thus diagonalizable) matrix is defined as the absolute value of the ratio between
its maximal and minimal (by moduli) eigenvalues. In the above example,

```
limρ→ 1 Λ^1 ;^1
Λ 2 ; 2
¼þ∞
```
```
limρ→ 1 þ
```
#### Λ 2 ; 2

#### Λ 1 ; 1

```
¼þ∞:
```
## 7.4 Markowitz’s Curse

MatrixCis just a standardized version ofV, and the conclusions we drew
onC^1 apply to theV^1 used to computeω. When securities within a portfolio
are highly correlated ( 1 <ρ≪0or0≪ρ<1),Chas a high condition
number, and the values ofV^1 explode. This is problematic in the context of
portfolio optimization, becauseωdepends onV^1 , and unlessρ≈0, we must
expect an unstable solution to the convex optimization program. In other words,
Markowitz’s solution is guaranteed to be numerically stable only ifρ≈0, which
is precisely the case when we don’t need it! The reason we needed Markowitz
was to handle theρ≉0 case, but the more we need Markowitz, the more
numerically unstable is the estimation ofω. This is Markowitz’s curse.
López de Prado (2016)introduced an ML-based asset allocation method
called hierarchical risk parity (HRP). HRP outperforms Markowitz and the
naïve allocation in out-of-sample Monte Carlo experiments. The purpose of
HRP was not to deliver an optimal allocation, but merely to demonstrate the
potential of ML approaches. In fact, HRP outperforms Markowitz out-of-
sample even though HRP is by construction suboptimal in-sample. In thenext
sectionwe analyze further why standard mean-variance optimization is rela-
tively easy to beat.

```
Elements in Quantitative Finance 95
```

## 7.5 Signal as a Source of Covariance Instability

In Section 2, we saw that the covariance instability associated with noise is
regulated by theN/Tratio, because the lower bound of the Marcenko–Pastur
distribution, λ, gets smaller asN/Tgrows,^22 while the upper bound,λþ,
increases asN/Tgrows. In this section, we are dealing with a different source
of covariance instability, caused by the structure of the data (signal). As we saw
in the 2 × 2 matrix example,ρregulates the matrix’s condition number, regard-
less and independently fromN/T. Signal-induced instability is structural, and
cannot be reduced by sampling more observations.
There is an intuitive explanation for how signal makes mean-variance opti-
mization unstable. When the correlation matrix is an identity matrix, the
eigenvalue function is a horizontal line, and the condition number is 1.
Outside that ideal case, the condition number is impacted by irregular correla-
tion structures. In the particular case offinance, when a subset of securities
exhibits greater correlation among themselves than to the rest of the investment
universe, that subset forms a cluster within the correlation matrix. Clusters
appear naturally, as a consequence of hierarchical relationships. WhenKsecu-
rities form a cluster, they are more heavily exposed to a common eigenvector,
which implies that the associated eigenvalue explains a greater amount of
variance. But because the trace of the correlation matrix is exactlyN, that
means that an eigenvalue can only increase at the expense of the otherK 1
eigenvalues in that cluster, resulting in a condition number greater than 1.
Consequently, the greater the intracluster correlation is, the higher the condition
number becomes. This source of instability is distinct and unrelated toN=T→1.
Let us illustrate this intuition with a numerical example.Code Snippet 7.1
shows how to form a block-diagonal correlation matrix of different numbers of
blocks, block sizes, and intrablock correlations.Figure 7.1plots a block-diagonal

#### SNIPPET7.1 COMPOSITION OFBLOCK-DIAGONALCORRELATIONMATRICES

```
import matplotlib.pyplot as mpl,seaborn as sns
import numpy as np
#---------------------------------------------------
corr0=formBlockMatrix(2,2,.5)
eVal,eVec=np.linalg.eigh(corr0)
print max(eVal)/min(eVal)
sns.heatmap(corr0,cmap=‘viridis’)
```
(^22) As a reminder, inSection 2, variableNdenoted the number of columns in the covariance matrix,
and variableTdenoted the number of independent observations used to compute the covariance
matrix.
96 Machine Learning for Asset Managers


matrix of size 4x4, composed of two equal-sized blocks, where the intrablock
correlation is 0.5 and the outer-block correlation is zero. Because of this block
structure, the condition number is not 1, but 3. The condition number rises if (1)
we make one block greater or (2) we increase the intrablock correlation. The
reason is, in both cases one eigenvector explains more variance than the rest. For
instance, if we increase the size of one block to three and reduce the size of the
other to 1, the condition number becomes 4. If instead we increase the intrablock
correlation to 0.75, the condition number becomes 7. A block-diagonal correla-
tion matrix of size 500x500 with two equal-sized blocks, where the intrablock
correlation is 0.5 has a condition number of 251, again as a result of having 500
eigenvectors where most of the variance is explained by only 2.
Code Snippet 7.2demonstrates that bringing down the intrablock correlation
in only one of the two blocks does not reduce the condition number. The reason
is, the extreme eigenvalues are caused by the dominant block. So even though
the high condition number may be caused by only one cluster, it impacts the
entire correlation matrix. This observation has an important implication: the
instability of Markowitz’s solution can be traced back to a few dominant

```
3
0.0
```
```
0.2
```
```
0.4
```
```
0.6
```
```
0.8
```
```
1.0
```
```
0123
```
```
2
```
```
1
```
```
0
```
```
Figure 7.1Heatmap of a block-diagonal correlation matrix.
```
#### SNIPPET7.2 BLOCK-DIAGONALCORRELATIONMATRIX WITH ADOMINANTBLOCK

```
corr0=block_diag(formBlockMatrix(1,2,.5))
corr1=formBlockMatrix(1,2,.0)
corr0=block_diag(corr0,corr1)
eVal,eVec=np.linalg.eigh(corr0)
print max(eVal)/min(eVal)
```
```
Elements in Quantitative Finance 97
```

clusters within the correlation matrix. We can contain that instability by opti-
mizing the dominant clusters separately, hence preventing that the instability
spreads throughout the entire portfolio.

## 7.6 The Nested Clustered Optimization Algorithm

The remainder of this section is dedicated to introducing a new ML-based
method, named nested clustered optimization (NCO), which tackles the
source of Markowitz’s curse. NCO belongs to a class of algorithms known
as“wrappers”: it is agnostic as to what member of the efficient frontier is
computed, or what set of constraints is imposed. NCO provides a strategy for
addressing the effect of Markowitz’s curse on an existing mean-variance
allocation method.

```
7.6.1 Correlation Clustering
```
Thefirst step of the NCO algorithm is to cluster the correlation matrix. This
operation involvesfinding the optimal number of clusters. One possibility is to
apply the ONC algorithm (Section 4), however NCO is agnostic as to what
particular algorithm is used for determining the number of clusters. For large
matrices, whereT=Nis relatively low, it is advisable to denoise the correlation
matrix prior to clustering, following the method described inSection 2. Code
Snippet 7.3implements this procedure. We compute the denoised covariance
matrix, cov1, using the deNoiseCov function introduced inSection 2.Asa
reminder, argument q informs the ratio between the number of rows and the
number of columns in the observation matrix. When bWidth=0, the covariance
matrix is not denoised. We standardize the resulting covariance matrix into
a correlation matrix using the cov2corr function. Then we cluster the
cleaned correlation matrix using the clusterKMeansBase function, which
we introduced inSection 4. The argument maxNumClusters is set to half
the number of columns in the correlation matrix. The reason is, single-item
clusters do not cause an increase in the matrix’s condition number, so we

#### SNIPPET7.3 THECORRELATIONCLUSTERINGSTEP

```
import pandas as pd
cols=cov0.columns
cov1=deNoiseCov(cov0,q,bWidth=.01)# de-noise cov
cov1=pd.DataFrame(cov1,index=cols,columns=cols)
corr1=cov2corr(cov1)
corr1,clstrs,silh=clusterKMeansBase(corr1,
maxNumClusters=corr0.shape[0]/2,n_init=10)
```
98 Machine Learning for Asset Managers


only need to consider clusters with a minimum size of two. If we expect
fewer clusters, a lower maxNumClusters may be used to accelerate
calculations.
A common question is whether we should cluster corr1 or corr1.abs(). When
all correlations are nonnegative, clustering corr1 and corr1.abs() yields the same
outcome. When some correlations are negative, the answer is more convoluted,
and depends on the numerical properties of the observed inputs. I recommend
that you try both, and see what clustering works better for your particular corr1
in Monte Carlo experiments.^23

```
7.6.2 Intracluster Weights
```
The second step of the NCO algorithm is to compute optimal intracluster
allocations, using the denoised covariance matrix, cov1.Code Snippet 7.4
implements this procedure. For simplicity purposes, we have defaulted to a
minimum variance allocation, as implemented in the minVarPort function.
However, nothing in the procedure prevents the use of alternative alloca-
tion methods. Using the estimated intracluster weights, we can derive the
reduced covariance matrix, cov2, which reports the correlations between
clusters.

```
7.6.3 Intercluster Weights
```
The third step of the NCO algorithm is to compute optimal intercluster alloca-
tions, using the reduced covariance matrix, cov2. By construction, this covar-
iance matrix is close to a diagonal matrix, and the optimization problem is close
to the ideal Markowitz case. In other words, the clustering and intracluster
optimization steps have allowed us to transform a“Markowitz-cursed”problem
(jρj≫0) into a well-behaved problem (ρ≈0).

#### SNIPPET7.4 INTRACLUSTEROPTIMALALLOCATIONS

```
wIntra=pd.DataFrame(0,index=cov1.index,columns=clstrs.keys())
for i in clstrs:
wIntra.loc[clstrs[i],i]=minVarPort(cov1.loc[clstrs[i],
clstrs[i]]).flatten()
cov2=wIntra.T.dot(np.dot(cov1,wIntra))# reduced covariance matrix
```
(^23) As a rule of thumb, corr1.abs() tends to work better in long-short portfolio optimization problems
where some correlations are negative. Intuitively, the ability to have negative weights is
equivalent toflipping the sign of the correlation, which can induce considerable instability.
Because negatively correlated variables will interact through the weights, it makes sense to
cluster those variables together, thus containing that source of instability within each cluster.
Elements in Quantitative Finance 99


Code Snippet 7.5implements this procedure. It applies the same allocation
procedure that was used in the intracluster allocation step (that is, in the case of
Code Snippet 7.4, the minVarPort function). Thefinal allocation per security is
reported by the wAll0 data frame, which results from multiplying intracluster
weights with the intercluster weights.

## 7.7 Experimental Results

In this section we subject the NCO algorithm to controlled experiments, and
compare its performance to Markowitz’s approach. Like inSection 2,we
discuss two characteristic portfolios of the efficient frontier, namely, the mini-
mum variance and maximum Sharpe ratio solutions, since any member of the
unconstrained efficient frontier can be derived as a convex combination of the
two (a result sometimes known as the“separation theorem”).
Code Snippet 7.6implements the NCO algorithm introduced earlier in this
section. When argument mu is None, function optPort_nco returns the mini-
mum variance portfolio, whereas when mu is not None, function optPort_nco
returns the maximum Sharpe ratio portfolio.

#### SNIPPET7.5 INTERCLUSTEROPTIMALALLOCATIONS

```
wInter=pd.Series(minVarPort(cov2).flatten(),index=cov2.index)
wAll0=wIntra.mul(wInter,axis=1).sum(axis=1).sort_index()
```
#### SNIPPET7.6 FUNCTIONIMPLEMENTING THENCO ALGORITHM

```
def optPort_nco(cov,mu=None,maxNumClusters=None):
cov=pd.DataFrame(cov)
if mu is not None:mu=pd.Series(mu[:,0])
corr1=cov2corr(cov)
corr1,clstrs,_=clusterKMeansBase(corr1,maxNumClusters,
n_init=10)
wIntra=pd.DataFrame(0,index=cov.index,columns=clstrs.keys())
for i in clstrs:
cov_=cov.loc[clstrs[i],clstrs[i]].values
if mu is None:mu_=None
else:mu_=mu.loc[clstrs[i]].values.reshape(-1,1)
wIntra.loc[clstrs[i],i]=optPort(cov_,mu_).flatten()
cov_=wIntra.T.dot(np.dot(cov,wIntra))# reduce covariance matrix
mu_=(None if mu is None else wIntra.T.dot(mu))
wInter=pd.Series(optPort(cov_,mu_).flatten(),index=cov_.index)
nco=wIntra.mul(wInter,axis=1).sum(axis=1).values.reshape(-1,1)
return nco
```
100 Machine Learning for Asset Managers


```
7.7.1 Minimum Variance Portfolio
```
Code Snippet 7.7creates a random vector of means and a random covariance
matrix that represent a stylized version of afifty securities portfolio, grouped in
ten blocks with intracluster correlations of 0.5. This vector and matrix char-
acterize the“true”process that generates observations.^24 We set a seed for the
purpose of reproducing and comparing results across runs with different para-
meters. Function formTrueMatrix was declared inSection 2.

Code Snippet 7.8uses function simCovMu to simulate a random empirical
vector of means and a random empirical covariance matrix based on 1,000
observations drawn from the true process (declared in Section 2). When
shrink=True, the empirical covariance matrix is subjected to Ledoit–Wolf
shrinkage. Using that empirical covariance matrix, function optPort (also
declared inSection 2) estimates the minimum variance portfolio according to
Markowitz, and function optPort_nco estimates the minimum variance portfo-
lio applying the NCO algorithm. This procedure is repeated on 1,000 different
random empirical covariance matrices. Note that, because minVarPortf=True,
the random empirical vectors of means are discarded.

#### SNIPPET7.7 DATA-GENERATINGPROCESS

```
nBlocks,bSize,bCorr =10,50,.5
np.random.seed(0)
mu0,cov0=formTrueMatrix(nBlocks,bSize,bCorr)
```
#### SNIPPET7.8 DRAWING ANEMPIRICALVECTOR OFMEANS ANDCOVARIANCEMATRIX

```
nObs,nSims,shrink,minVarPortf=1000,1000,False,True
np.random.seed(0)
for i in range(nSims):
mu1,cov1=simCovMu(mu0,cov0,nObs,shrink=shrink)
if minVarPortf:mu1=None
w1.loc[i]=optPort(cov1,mu1).flatten()
w1_d.loc[i]=optPort_nco(cov1,mu1,
int(cov1.shape[0]/2)).flatten()
```
(^24) In practical applications, we do not need to simulate μ;Vgf , as these inputs are estimated from
observed data. The reader can repeat this experiment on a pair of observed μ;Vgf and evaluate
via Monte Carlo the estimation error of alternative optimization methods on those particular
inputs, thusfinding out what method yields most robust estimates for a particular input.
Elements in Quantitative Finance 101


Code Snippet 7.9computes the true minimum variance portfolio, derived
from the true covariance matrix. Using those allocations as benchmark, it then
computes the root-mean-square errors (RMSE) across all weights. We can run
Code Snippet 7.9with and without shrinkage, thus obtaining the four combina-
tions displayed inFigure 7.2.

NCO computes the minimum variance portfolio with 52.98% of Markowitz’s
RMSE, i.e., a 47.02% reduction in the RMSE. While Ledoit–Wolf shrinkage
helps reduce the RMSE, that reduction is relatively small, around 11.81%.
Combining shrinkage and NCO yields a 15.30% reduction in RMSE, which is
better than shrinkage but worse than NCO alone.
The implication is that NCO delivers substantially lower RMSE than
Markowitz’s solution, even for a small portfolio of onlyfifty securities, and
that shrinkage adds no value. It is easy to test that NCO’s advantage widens for
larger portfolios (we leave it as an exercise).

```
7.7.2 Maximum Sharpe Ratio Portfolio
```
By setting minVarPortf=False, we can rerunCode Snippets 7.8and 7.9 to derive
the RMSE associated with the maximum Sharpe ratio portfolio.Figure 7.3
reports the results from this experiment.
NCO computes the maximum Sharpe ratio portfolio with 45.17% of
Markowitz’s RMSE, i.e., a 54.83% reduction in the RMSE. The combination
of shrinkage and NCO yields a 18.52% reduction in the RMSE of the maximum
Sharpe ratio portfolio, which is better than shrinkage but worse than NCO. Once
again, NCO delivers substantially lower RMSE than Markowitz’s solution, and
shrinkage adds no value.

#### SNIPPET7.9 ESTIMATION OFALLOCATIONERRORS

```
w0=optPort(cov0,None if minVarPortf else mu0)
w0=np.repeat(w0.T,w1.shape[0],axis=0)# true allocation
rmsd=np.mean((w1-w0).values.flatten()**2)**.5# RMSE
rmsd_d=np.mean((w1_d-w0).values.flatten()**2)**.5# RMSE
```
```
Markowitz NCO
Raw 7.95E-03 4.21E-03
Shrunk 8.89E-03 6.74E-03
```
```
Figure 7.2RMSE for the minimum variance portfolio.
```
102 Machine Learning for Asset Managers


## 7.8 Conclusions

Markowitz’s portfolio optimization framework is mathematically correct, how-
ever its practical application suffers from numerical problems. In particular,
financial covariance matrices exhibit high condition numbers due to noise and
signal. The inverse of those covariance matrices magnifies estimation errors,
which leads to unstable solutions: changing a few rows in the observations
matrix may produce entirely different allocations. Even if the allocations
estimator is unbiased, the variance associated with these unstable solutions
inexorably leads to large transaction costs than can erase much of the profit-
ability of these strategies.
In this section, we have traced back the source of Markowitz’s instability
problems to the shape of the correlation matrix’s eigenvalue function.
Horizontal eigenvalue functions are ideal for Markowitz’s framework. In
finance, where clusters of securities exhibit greater correlation among them-
selves than to the rest of the investment universe, eigenvalue functions are not
horizontal, which in turn is the cause for high condition numbers. Signal is the
cause of this type of covariance instability, not noise.
We have introduced the NCO algorithm to address this source of instability,
by splitting the optimization problem into several problems: computing one
optimization per cluster, and computing onefinal optimization across all clus-
ters. Because each security belongs to one cluster and one cluster only, thefinal
allocation is the product of the intracluster and intercluster weights.
Experimental results demonstrate that this dual clustering approach can sig-
nificantly reduce Markowitz’s estimation error. The NCO algorithm isflexible
and can be utilized in combination with any other framework, such as Black–
Litterman, shrinkage, reversed optimization, or constrained optimization
approaches. We can think of NCO as a strategy for splitting the general
optimization problem into subproblems, which can then be solved using the
researcher’s preferred method.
Like many other ML algorithms, NCO isflexible and modular. For example,
when the correlation matrix exhibits a strongly hierarchical structure, with

```
Markowitz NCO
Raw 7.02E-02 3.17E-02
Shrunk 6.54E-02 5.72E-02
```
```
Figure 7.3RMSE for the maximum Sharpe ratio portfolio.
```
```
Elements in Quantitative Finance 103
```

clusters within clusters, we can apply the NCO algorithm within each cluster
and subcluster, mimicking the matrix’s tree-like structure. The goal is to contain
the numerical instability at each level of the tree, so that the instability within a
subcluster does not extend to its parent cluster or the rest of the correlation
matrix.
We can follow the Monte Carlo approach outlined in this section to estimate
the allocation error produced by various optimization methods on a particular
set of input variables. The result is a precise determination of what method is
most robust to a particular case. Thus, rather than relying always on one
particular approach, we can apply opportunistically whatever optimization
method is best suited in a particular setting.

## 7.9 Exercises

1 Add toCode Snippet 7.3a detoning step, and repeat the experimental
analysis conducted inSection 7.7. Do you see an additional improvement
in NCO’s performance? Why?
2 RepeatSection 7.7, where this time you generate covariance matrices with-
out a cluster structure, using the function getRndCov listed inSection 2.Do
you reach a qualitatively different conclusion? Why?
3 RepeatSection 7.7, where this time you replace the minVarPort function with
the CLA class listed inBailey and López de Prado (2013).
4 RepeatSection 7.7for a covariance matrix of size ten and for a covariance
matrix of size one hundred. How do NCO’s results compare to Markowitz’s
as a function of the problem’s size?
5 RepeatSection 7.7, where you purposely mislead the clusterKMeansBase
algorithm by setting its argument maxNumClusters to a very small value, like

2. By how much does NCO’s solution worsen? How is it possible that, even
with only two clusters (instead of ten), NCO performs significantly better
than Markowitz’s solution?

104 Machine Learning for Asset Managers


## 8 Testing Set Overfitting

## 8.1 Motivation

Throughout this Element, we have studied the properties of ML solutions
through Monte Carlo experiments. Monte Carlo simulations play in mathe-
matics the analogue to a controlled experiment in the physical sciences. They
allow us to reach conclusions regarding the mathematical properties of various
estimators and procedures under controlled conditions. Having the ability to
control for the conditions of an experiment is essential to being able to make
causal inference statements.
A backtest is a historical simulation of how an investment strategy would
have performed in the past. It is not a controlled experiment, because we cannot
change the environmental variables to derive a new historical time series on
which to perform an independent backtest. As a result, backtests cannot help us
derive the precise cause–effect mechanisms that make a strategy successful.
This general inability to conduct controlled experiments on investment
strategies is more than a technical inconvenience. In the context of strategy
development, all we have is a few (relatively short, serially correlated, multi-
collinear and possibly nonstationary) historical time series. It is easy for a
researcher to overfit a backtest, by conducting multiple historical simulations,
and selecting the best performing strategy (Bailey et al. 2014). When a
researcher presents an overfit backtest as the outcome of a single trial, the
simulated performance is inflated. This form of statistical inflation is called
selection bias under multiple testing (SBuMT). SBuMT leads to false discov-
eries: strategies that are replicable in backtests, but fail when implemented.
To make matters worse, SBuMT is compounded at many asset managers, as a
consequence of sequential SBuMT at two levels: (1) each researcher runs
millions of simulations, and presents the best (overfit) ones to her boss; (2)
the company further selects a few backtests among the (already overfit) backt-
ests submitted by the researchers. We may call this backtest hyperfitting, to
differentiate it from backtest overfitting (which occurs at the researcher level).
It may take many decades to collect the future (out-of-sample) information
needed to debunk a false discovery that resulted from SBuMT. In this section, we
study how researchers can estimate the effect that SBuMT has on theirfindings.

## 8.2 Precision and Recall

Considersinvestment strategies. Some of these strategies are false discoveries,
in the sense that their expected return is not positive. We can decompose these
strategies between true (sT) and false (sF), wheres¼sTþsF. Letθbe the odds

```
Elements in Quantitative Finance 105
```

ratio of true strategies against false strategies,θ¼sT=sF.Inafield likefinancial
economics, where the signal-to-noise ratio is low, false strategies abound, hence
θis expected to be low. The number of true investment strategies is

```
sT¼s
sT
sTþsF
¼s
```
```
sT
sF
sTþsF
sF
```
```
¼s
θ
1 þθ
```
#### :

Likewise, the number of false investment strategies is

```
sF¼ssT¼s 1 
θ
1 þθ
```
#### 

```
¼s
```
#### 1

```
1 þθ
```
#### :

Given a false positive rateα(type I error), we will obtain a number of false
positives,FP¼αsF, and a number of true negatives,TN¼ðÞ 1 αsF. Let us
denote asβthe false negative rate (type II error) associated with thatα. We will
obtain a number of false negatives,FN¼βsT, and a number of true positives,
TP¼ðÞ 1 βsT. Therefore, the precision and recall of our test are

```
precision¼
```
#### TP

```
TPþFP
```
#### ¼

```
ðÞ 1 βsT
ðÞ 1 βsTþαsF
```
```
¼
```
```
ðÞ 1 βs 1 þθθ
ðÞ 1 βs 1 þθθþαs 1 þ^1 θ
```
#### ¼

```
ðÞ 1 βθ
ðÞ 1 βθþα
```
```
recall¼ TP
TPþFN
¼ ðÞ^1 βsT
ðÞ 1 βsTþβsT
¼ 1 β:
```
Before running backtests on a strategy, researchers should gather evidence
that a strategy may indeed exist. The reason is, the precision of the test is a
function of the odds ratio,θ. If the odds ratio is low, the precision will be low,
even if we get a positive with high confidence (lowp-value).^25 In particular, a
strategy is more likely false than true if 1ðÞβθ<α.
For example, suppose that the probability of a backtested strategy being
profitable is 0.01, that is, that one out of one hundred strategies is true, hence
θ¼ 1 =99. Then, at the standard thresholds ofα¼ 0 :05 andβ¼ 0 :2, researchers
are expected to get approximatelyfifty-eight positives out one thousand trials,
where approximately eight are true positives, and approximatelyfifty are false
positives. Under these circumstances, ap-value of 0.05 implies a false discov-
ery rate of 86.09% (roughly 50/58). For this reason alone, we should expect that
most discoveries infinancial econometrics are likely false.

(^25) This argument leads to the same conclusion we reached inSection 6:p-values report a rather
uninformative probability. It is possible for a statistical test to have high confidence (lowp-value)
and low precision.
106 Machine Learning for Asset Managers


## 8.3 Precision and Recall under Multiple Testing

After one trial, the probability of making a type I error isα. Suppose that we
repeat for a second time a test with false positive probabilityα. At each trial, the
probability ofnotmaking a type I error is 1ðÞα. If the two trials are
independent, the probability of not making a type I error on thefirstandsecond
tests is 1ðÞα^2. The probability of makingat least onetype I error is the
complement, 1ðÞ 1 α^2. If we conductKindependent trials, the joint prob-
ability of not making a single type I error is 1ðÞαK. Hence, the probability of
making at least one type I error is the complement,αK¼ 1 ðÞ 1 αK. This is
also known as the familywise error rate (FWER).
After one trial, the probability of making a type II error isβ. AfterK
independent trials, the probability of making a type II error on all of them is
βK¼βK. Note the difference with FWER. In the false positive case, we are
interested in the probability of makingat least oneerror. This is because a single
false alarm is a failure. However, in the false negative case, we are interested in
the probability thatallpositives are missed. AsKincreases,αKgrows andβK
shrinks.
The precision and recall adjusted for multiple testing are

```
precision¼ ðÞ^1 βKθ
ðÞ 1 βKθþαK
```
#### ¼

```
1 βK
```
#### 

```
θ
1 βK
```
#### 

```
θþ 1 ðÞ 1 αK
```
```
recall¼ 1 βK¼ 1 βK:
```
## 8.4 The Sharpe Ratio

Financial analysts do not typically assess the performance of a strategy in terms
of precision and recall. The most common measure of strategy performance is
the Sharpe ratio. In what follows, we will develop a framework for assessing the
probability that a strategy is false. The inputs are the Sharpe ratio estimate, as
well as metadata captured during the discovery process.^26
Consider an investment strategy with excess returns (or risk premia) rtgf ,
t¼ 1 ;...;T, which are independent and identically distributed (IID) Normal,

```
rteN½μ;σ^2 ;
```
(^26) Perhaps analysts should use precision and recall instead of the Sharpe ratio, but that’s beyond the
point. Financial mathematicians rarely have the luxury of framing the problems they work on,
unlike topologists, set theorists, algebraic geometers, etc.
Elements in Quantitative Finance 107


whereN½μ;σ^2 represents a Normal distribution with meanμand varianceσ^2.
FollowingSharpe (1966, 1975, 1994), the (nonannualized) Sharpe Ratio of such
strategy is defined as

```
SR¼μ
σ
```
#### :

```
Because parametersμandσare not known, SR is estimated as
```
```
SRc¼ Effiffiffiffiffiffiffiffiffiffiffiffiffiffi½rtgf
V½rtgf
```
```
p :
```
Under the assumption that returns are IID Normal,Lo (2002)derived the
asymptotic distribution ofSR asc

```
SRcSR
```
#### 

```
→aN 0 ;
1 þ^12 SR^2
T
```
#### "#

#### :

However, empirical evidence shows that hedge fund returns exhibit substan-
tial negative skewness and positive excess kurtosis (among others, seeBrooks
and Kat 2002; Ingersoll et al. 2007). Wrongly assuming that returns are IID
Normal can lead to a gross underestimation of the false positive probability.
Under the assumption that returns are drawn from IID non-Normal distribu-
tions,Mertens (2002)derived the asymptotic distribution ofSR asc

```
SRcSR
```
#### 

```
→aN 0 ;
```
```
1 þ^12 SR^2 γ 3 SRþγ^4  43 SR^2
T
```
#### "#

#### ;

whereγ 3 is the skewness of rtgf , andγ 4 is the kurtosis of rtgf (γ 3 ¼0 and
γ 4 ¼3 when returns follow a Normal distribution). Shortly after,Christie
(2005)and Opdyke (2007)discovered that, in fact, Mertens’s equation is also
valid under the more general assumption that returns are stationary and ergodic
(not necessarily IID). The key implication is thatSR^ still follows a Normal
distribution even if returns are non-Normal, however with a variance that partly
depends on the skewness and kurtosis of the returns.

## 8.5 The“False Strategy”Theorem

A researcher may carry out a large number of historical simulations
(trials), and report only the best outcome (maximum Sharpe ratio). The
distribution of the maximum Sharpe ratio is not the same as the distribu-
tion of a Sharpe ratio randomly chosen among the trials, hence giving rise
to SBuMT. When more than one trial takes place, the expected value of the

108 Machine Learning for Asset Managers


maximum Sharpe ratio is greater than the expected value of the Sharpe
ratio from a random trial. In particular, given an investment strategy with
expected Sharpe ratio zero and nonnull variance, the expected value of the
maximum Sharpe ratio is strictly positive, and a function of the number of
trials.
Given the above, the magnitude of SBuMT can be expressed in terms of the
difference between the expected maximum Sharpe ratio and the expected
Sharpe ratio from a random trial (zero, in the case of a false strategy). As it
turns out, SBuMT is a function of two variables: the number of trials, and the
variance of the Sharpe ratios across trials. The following theorem formally
states that relationship. A proof can be found in Appendix B.

Theorem: Given a sample of estimated performance statistics fSRckg,
k¼ 1 ;...;K, drawn from independent and identically distributed Gaussians,
SRck
eN½^0 ;V½
SRck, then

```
E max
k
fSRckg
```
```
 i
V
```
```
h
fSRckg
```
i (^12)
≈ðÞ 1 γZ^11 ^1
K

#### 

```
þγZ^11 ^1
Ke
```
#### 

#### ;

whereZ^1 ½:is the inverse of the standard Gaussian CDF, E½:is the expected
value, V½:is the variance,eis Euler’s number, andγis the Euler–Mascheroni
constant.

## 8.6 Experimental Results

The False Strategy theorem provides us with an approximation of the
expected maximum Sharpe ratio. An experimental analysis of this theorem
can be useful at two levels. First, it can help usfind evidence that the
theorem is not true, and in fact the proof isflawed. Of course, the converse
is not true: experimental evidence can never replace the role of a mathe-
matical proof. Still, experimental evidence can point to problems with the
proof, and give us a better understanding of what the proof should look
like. Second, the theorem does not provide a boundary for the approxima-
tion. An experimental analysis can help us estimate the distribution of the
approximation error.
The following Monte Carlo experiment evaluates the accuracy of the False
Strategy theorem. First, given a pair of valuesðK;V½fSRckgÞ, we generate a
random array of sizeðÞSxK, whereSis the number of Monte Carlo experiments.
The values contained by this random array are drawn from a Standard Normal
distribution. Second, the rows in this array are centered and scaled to match zero
mean and V½fSRckgvariance. Third, the maximum value across each row is

```
Elements in Quantitative Finance 109
```

computed, maxkfSRckg, resulting in a numberSof such maxima. Fourth, we
compute the average value across theSmaxima,^E½maxkfSRckg. Fifth, this
empirical (Monte Carlo) estimate of the expected maximum SR can then be
compared with the analytical solution provided by the False Strategy theorem,
E½maxkfSRckg. Sixth, the estimation error is defined in relative terms to the
predicted value, as

```
ε¼
```
```
^E½maxkfSRckg
E½maxkfSRckg
```
####  1 :

Seventh, we repeat the previous stepsRtimes, resulting infεrgr¼ 1 ;...;Restima-
tion errors, allowing us to compute the mean and standard deviation of the
estimation errors associated withKtrials.Code Snippet 8.1implements this
Monte Carlo experiment in python.

#### SNIPPET8.1 EXPERIMENTALVALIDATION OF THEFALSESTRATEGYTHEOREM

```
import numpy as np,pandas as pd
from scipy.stats import norm,percentileofscore
#---------------------------------------------------
def getExpectedMaxSR(nTrials,meanSR,stdSR):
# Expected max SR, controlling for SBuMT
emc=0.577215664901532860606512090082402431042159336
sr0=(1-emc)*norm.ppf(1-1./nTrials)+ /
emc*norm.ppf(1-(nTrials*np.e)**-1)
sr0=meanSR+stdSR*sr0
return sr0
#---------------------------------------------------
def getDistMaxSR(nSims,nTrials,stdSR,meanSR):
# Monte Carlo of max{SR} on nTrials, from nSims simulations
rng=np.random.RandomState()
out=pd.DataFrame()
for nTrials_ in nTrials:
#1) Simulated Sharpe ratios
sr=pd.DataFrame(rng.randn(nSims,nTrials_))
sr=sr.sub(sr.mean(axis=1),axis=0)# center
sr=sr.div(sr.std(axis=1),axis=0)# scale
sr=meanSR+sr*stdSR
#2) Store output
out_=sr.max(axis=1).to_frame(‘max{SR}’)
out_[‘nTrials’]=nTrials_
out=out.append(out_,ignore_index=True)
return out
#---------------------------------------------------
```
110 Machine Learning for Asset Managers


Figure 8.1helps us visualize the outcomes from this experiment, for a wide
range of trials (in the plot, between 2 and 1 million). For V½fSRckg¼1 and any
given number of trialsK, we simulate the maximum Sharpe ratio 10,000 times,
so that we can derive the distribution of maximum Sharpe ratios. They-axis
shows that distribution of the maximum Sharpe ratios ( maxkfSRckg) for each
number of trialsK(x-axis), when the true Sharpe ratio is zero. Results with a
higher probability receive a lighter color. For instance, if we conduct 1,000 trials,
the expected maximum Sharpe ratio (E½maxkfSRckg) is 3.26, even though the
true Sharpe ratio of the strategy is null. As expected, there is a raising hurdle that
the researcher must beat as he conducts more backtests. We can compare these
experimental results with the results predicted by the False Strategy theorem,
which are represented with a dashed line. The comparison of these two results

```
if __name__==‘__main__’:
nTrials=list(set(np.logspace(1,6,1000).astype(int)));nTrials.sort()
sr0=pd.Series({i:getExpectedMaxSR(i,meanSR=0,stdSR=1) \
for i in nTrials})
sr1=getDistMaxSR(nSims=1E3,nTrials=nTrials,meanSR=0,
stdSR=1)
```
```
1
```
```
2
```
```
3
```
```
4
```
```
5
```
```
6
```
```
7
```
```
0.0
```
```
0.5
```
```
1.0
```
```
1.5
```
```
2.0
```
```
2.5
```
```
3.0
```
```
101 102 103
Number of trials
```
```
max{SR} across uninformed strategies, for std(SR)=1
```
```
104 105 106
```
```
E [max{SR}] (prior)
```
```
E [max{SR}], max{SR}
```
```
max{SR} (observed)
```
Figure 8.1Comparison of experimental and theoretical results from the False
Strategy theorem.

```
Elements in Quantitative Finance 111
```

(experiments and theoretical) seems to indicate that the False Strategy theorem
accurately estimates the expected maximum SR for the range of trials studied.
We turn now our attention to evaluating the precision of the theorem’s
approximation. We define the approximation error as the difference between
the experimental prediction (based on 1,000 simulations) and the theorem’s
prediction, divided by the theorem’s prediction. We can then reevaluate these
estimation errors one hundred times for each number of trialsKand derive the
mean and standard deviation of the errors.Code Snippet 8.2implements a
second Monte Carlo experiment that evaluates the accuracy of the theorem.

Figure 8.2plots the results from this second experiment. The circles represent
average errors relative to predicted values (y-axis), computed for alternative
numbers of trials (x-axis). From this result, it appears that the False Strategy
theorem produces asymptotically unbiased estimates. Only at K≈50, the
theorem’s estimate exceeds the experimental value by approx. 0.7%.

#### SNIPPET8.2 MEAN ANDSTANDARDDEVIATION OF THEPREDICTIONERRORS

```
def getMeanStdError(nSims0,nSims1,nTrials,stdSR=1,meanSR=0):
# Compute standard deviation of errors per nTrial
# nTrials: [number of SR used to derive max{SR}]
# nSims0: number of max{SR} used to estimate E[max{SR}]
# nSims1: number of errors on which std is computed
sr0=pd.Series({i:getExpectedMaxSR(i,meanSR,stdSR) \
for i in nTrials})
sr0=sr0.to_frame(‘E[max{SR}]’)
sr0.index.name=‘nTrials’
err=pd.DataFrame()
for i in xrange(int(nSims1)):
sr1=getDistDSR(nSims=1E3,nTrials=nTrials,meanSR=0,
stdSR=1)
sr1=sr1.groupby(‘nTrials’).mean()
err_=sr0.join(sr1).reset_index()
err_[‘err’]=err_[‘max{SR}’]/err_[‘E[max{SR}]’]-1.
err=err.append(err_)
out={‘meanErr’:err.groupby(‘nTrials’)[‘err’].mean()}
out[‘stdErr’]=err.groupby(‘nTrials’)[‘err’].std()
out=pd.DataFrame.from_dict(out,orient=‘columns’)
return out
#---------------------------------------------------
if __name__==‘__main__’:
nTrials=list(set(np.logspace(1,6,1000).astype(int)));nTrials.sort()
stats=getMeanStdError(nSims0=1E3,nSims1=1E2,
nTrials=nTrials,stdSR=1)
```
112 Machine Learning for Asset Managers


The crosses represent the standard deviation of the errors (y-axis), derived
for different numbers of trials (x-axis). From this experiment, we can deduce
that the standard deviations are relatively small, below 0.5% of the values
forecasted by the theorem, and they become smaller as the number of trials
raises.

## 8.7 The Deflated Sharpe Ratio

The main conclusion from the False Strategy theorem is that, unless
maxkfSRckg≫E½maxkfSRckg, the discovered strategy is likely to be afalse
positive. If we can compute E½maxkfSRckg, we can use that value to set the null
hypothesis that must be rejected to conclude that the performance of the strategy
is statistically significant,H 0 ¼E½maxkfSRckg. Then, the deflated Sharpe ratio
(Bailey and López de Prado 2014) can be derived as

```
DSRd¼Z
```
```
SRcE maxkfSRckg
```
```
hi ffiffiffiffiffiffiffiffiffiffiffiffi
T 1
```
```
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ^γ 3 SRcþ^γ^44 ^1 SRc^2
```
```
q
```
#### 2

(^64)

#### 3

(^75) :
DSR can be interpreted as the probability of observing a Sharpe ratio greaterd
or equal toSR subject to the null hypothesis that the true Sharpe ratio is zero,c
while adjusting for skewness, kurtosis, sample length, and multiple testing. The
calculation ofDSR requires the estimation of Ed ½maxkfSRckg, which in turn
–0.015
–0.010
–0.005
0.000
Mean[err], std[err]
0.005
0.010
0.015
Mean[err]
Std[err]
101 102 103
Number of trials
104 105 106
Figure 8.2Statistics of the approximation errors as a function of the number of
trials.
Elements in Quantitative Finance 113


requires the estimation ofKand V½fSRckg. Here is where ML comes to our
rescue, as explained next.

```
8.7.1 Effective Number of Trials
```
The False Strategy theorem requires knowledge of the number of independent
trials within a family of tests. However, it is uncommon forfinancial researchers
to run independent trials. A more typical situation is for researchers to try
different strategies, where multiple trials are run for each strategy. Trials
associated with one strategy presumably have higher correlations to one another
than to other strategies. This relationship pattern can be visualized as a block
correlation matrix. For example,Figure 8.3plots a real example of a correlation
matrix between 6,385 backtested returns series for the same investment uni-
verse, before and after clustering (for a detailed description of this example, see
López de Prado 2019a). The ONC algorithm (Section 4) discovers the existence
of four differentiated strategies. Hence, in this example we would estimate that
E½K¼4. This is a conservative estimate, since the true numberKof indepen-
dent strategies must be smaller than the number of low-correlated strategies.

```
8.7.2 Variance across Trials
```
In this section, we follow closelyLópez de Prado and Lewis (2018). Upon
completion of the clustering above, ONC has successfully partitioned ourN
strategies intoKgroups, each of which is construed of highly correlated
strategies. We can further utilize this clustering to reduce theNstrategies to
K≪Ncluster-level strategies. Upon creation of these“cluster strategies,”we
derive our estimate of V½fSRckg, wherek¼ 1 ;...;K.
For a given clusterk, the goal is to form an aggregate cluster returns time
seriesSk;t. This necessitates choosing a weighting scheme for the aggregation. A
good candidate is the minimum variance allocation, because it prevents that
individual trials with high variance dominate the cluster’s returns. LetCkdenote
the set of strategies in clusterk,Σkthe covariance matrix restricted to strategies
inCk,ri;tthe returns series for strategyi 2 Ck, andwk;ithe weight associated
with strategyi 2 Ck. Then, we compute

```
fwk;igi 2 Ck¼
Σk^11 k
```
(^1) k^0 Σk^11 k
Sk;t¼

#### X

```
i 2 Ck
```
```
wk;iri;t;
```
114 Machine Learning for Asset Managers


```
1.00
```
```
0.75
```
```
0.50
```
```
0.25
```
```
0.00
```
```
–0.25
```
```
–0.50
```
```
–0.75
```
```
1.00
```
```
0.75
```
```
0.50
```
```
0.25
```
```
0.00
```
```
–0.25
```
```
–0.50
```
```
–0.75
```
```
(a)
```
```
(b)
```
Figure 8.3 Clustering of 6,385 trials, typical of multiple testing of a group of
strategies, before and after clustering.
Source:López de Prado (2019a)

```
Elements in Quantitative Finance 115
```

where 1kis the characteristic vector of 1s, of sizejjCkjj. A robust method of
computingwkcan be found inLópez de Prado and Lewis (2018). With the
cluster returns time seriesSk;tnow computed, we estimate each SR (SRck).
However, theseSRckare not yet comparable, as their betting frequency may
vary. To make them comparable, we mustfirst annualize each. Accordingly, we
calculate the average number of bets per year as

```
Yearsk¼
Last DatekFirst Datek
365 : 25
```
```
Frequencyk¼
Tk
Yearsk
```
#### ;

whereTkis the length of theSk;t, and First Datekand Last Datekare thefirst and
last dates of trading forSk;t, respectively. With this, we estimate the annualized
Sharpe ratio (aSR) as

```
aSRdk¼ Effiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi½fSk;tgFrequencyk
V½fSk;tgFrequencyk
```
```
p ¼SRck
```
```
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Frequencyk:
```
```
p
```
With these now comparableaSRdk, we can estimate the variance of clustered
trials as

```
E½V½fSRckg¼
V½faSRdkg
Frequencyk;
```
where Frequencyk is the frequency of the selected cluster,k. The above
equation expresses the estimated variance of clustered trials in terms of the
frequency of the selected strategy, in order to match the (nonannualized)
frequency of theSR estimate.^

## 8.8 Familywise Error Rate

This section has so far explained how to derive the probability that an invest-
ment strategy is false, using the False Strategy theorem. In this section we
discuss an alternative method, which relies on the notion of familywise error
rate.
Under the standard Neyman–Pearson hypothesis testing framework,
we reject a null hypothesisH 0 with confidence 1ðÞα when we observe
an event that, should the null hypothesis be true, could only occur with
probability α. Then, the probability of falsely rejecting the null
hypothesis (type I error) isα. This is also known as the probability of a false
positive.

116 Machine Learning for Asset Managers


WhenNeyman and Pearson (1933)proposed this framework, they did
not consider the possibility of conducting multiple tests and select the best
outcome. As we saw inSection 8.3, when a test is repeated multiple times,
the combined false positive probability increases. After a“family” ofK
independent tests, we would rejectH 0 with confidence 1ðÞαK, hence the
“family” false positive probability (or familywise error rate, FWER) is
αK¼ 1 ðÞ 1 αK. This is the probability thatat least oneof the positives is
false, which is the complement to the probability that none of the positives is
false, 1ðÞαK.

```
8.8.1Šidàk’s Correction
```
Suppose that we set a FWER over Kindependent tests atαK. Then, the
individual false positive probability can be derived from the above equation
asα¼ 1 ðÞ 1 αK^1 =K. This is known as theŠidàk correction for multiple
testing (Šidàk 1967), and it can be approximated as thefirst term of a Taylor
expansion,α≈αK=K(known as Bonferroni’s approximation).
As we did earlier, we can apply the ONC algorithm to estimate E½K. While it
is true that the E½Ktrials are not perfectly uncorrelated, they provide a con-
servative estimate of the minimum number of clusters the algorithm could not
reduce further. With this estimate E½K, we can applyŠidàk’s correction, and
compute the type I error probability under multiple testing,αK.

```
8.8.2 Type I Errors under Multiple Testing
```
Consider an investment strategy with returns time series of sizeT. We estimate
the Sharpe ratio,SR, and subject that estimate to a hypothesis test, wherec
H 0 :SR¼0 andH 1 :SR>0. We wish to determine the probability of a false
positive when this test is applied multiple times.
Bailey and López de Prado (2012)derived the probability that the true Sharpe
ratio exceeds a given threshold SR, under the general assumption that returns
are stationary and ergodic (not necessarily IID Normal). If the true Sharpe ratio
equals SR, the statistic^z½SRis asymptotically distributed as a Standard
Normal,

```
^z½SR¼
```
```
SRcSR
```
```
ffiffiffiffiffiffiffiffiffiffiffiffi
T 1
```
```
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ^γ 3 SRcþ^γ^4  41 SRc^2
```
```
q →aZ;
```
whereSR is the estimated Sharpe ratio (nonannualized),^ Tis the number of
observations,^γ 3 is the skewness of the returns, and^γ 4 is the kurtosis of the
returns. Familywise type I errors occur with probability

```
Elements in Quantitative Finance 117
```

```
P½max
k
f^z½ 0 kgk¼ 1 ;...;K>zαjH 0 ¼ 1 ðÞ 1 αK¼αK:
```
For a FWERαK,Šidàk’s correction gives us a single-trial significance level
α¼ 1 ðÞ 1 αK^1 =K. Then, the null hypothesis is rejected with confidence
ðÞ 1 αK if maxkf^z½ 0 kgk¼ 1 ;...;K>zα, wherezαis the critical value of the
Standard Normal distribution that leaves a probability α to the right,
zα¼Z^1 ½ 1 α¼Z^1 ½ðÞ 1 αK^1 =K, and Z½:is the CDF of the standard
Normal distribution.
Conversely, we can derive the type I error under multiple testing (αK)as
follows:first, apply the clustering procedure on the trials correlation matrix, to
estimate clusters’ returns series and E½K; second, estimate
^z½ 0 ¼maxkf^z½ 0 kgk¼ 1 ;...;Kon the selected cluster’s returns; third, compute
the type I error for a single test,α¼ 1 Z½^z½ 0 ; fourth, correct for multiple
testing,αK¼ 1 ðÞ 1 αK, resulting in

```
αK¼ 1 Z½^z½ 0 E½K:
```
Let us illustrate the above calculations with a numerical example.
Suppose that after conducting 1,000 trials, we identify an investment
strategy with a Sharpe ratio of 0.0791 (nonannualized), skewness of
−3, kurtosis of 10, computed on 1,250 daily observations (five years, at
250 annual observations). These levels of skewness and kurtosis are
typical of hedge fund returns sampled with daily frequency. From these
inputs we derive^z½ 0 ≈ 2 :4978 andα≈ 0 :0062. At this type I error probability,
most researchers would reject the null hypothesis, and declare that a new
investment strategy has been found. However, thisαis not adjusted for the
E½Ktrials it took tofind this strategy. We apply our ONC algorithm, and
conclude that out of the 1,000 (correlated) trials, there are E½K¼10 effectively
independent trials (again, with“effectively”independent we do not assert that
the ten clusters are strictly independent, but that the algorithm could notfind
more uncorrelated groupings). Then, the corrected FWER isαK≈ 0 :0608. Even
though the annualized Sharpe ratio is approx. 1.25, the probability that this
strategy is a false discovery is relatively high, for two reasons: (1) the number of
trials, sinceαK¼α≈ 0 :0062 if E½K¼1; (2) the non-Normality of the returns,
sinceαK≈ 0 :0261 should returns have been Normal. As expected, wrongly
assuming Normal returns leads to a gross underestimation of the type I error
probability.Code Snippet 8.3provides the python code that replicates these
results.

118 Machine Learning for Asset Managers


```
8.8.3 Type II Errors under Multiple Testing
```
Suppose that the alternative hypothesis (H 1 :SR>0) for the best strategy
is true, and SR¼SR. Then, the power of the test associated with a
FWERαKis

```
P½maxk f^z½ 0 kgk¼ 1 ;...;K>zαjSR¼SR
```
#### ¼P

```
SRcþSRSR
```
```
ffiffiffiffiffiffiffiffiffiffiffiffi
T 1
```
```
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ^γ 3 SRcþ^γ^44 ^1 SRc^2
```
```
q >zαjSR¼SR
```
#### 2

(^64)

#### 3

(^75)
¼P ^z½SR>zα

#### SR

```
ffiffiffiffiffiffiffiffiffiffiffiffi
T 1
```
```
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ^γ 3 SRcþ^γ^4  41 SRc^2
```
```
q jSR¼SR
```
#### 2

(^64)

#### 3

(^75)
¼ 1 P^z½SR<zα

#### SR

```
ffiffiffiffiffiffiffiffiffiffiffiffi
T 1
```
```
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ^γ 3 SRcþ^γ^4  41 SRc^2
```
```
q jSR¼SR
```
#### 2

(^64)

#### 3

(^75)

#### SNIPPET8.3 TYPEIERROR,WITHNUMERICALEXAMPLE

```
import scipy.stats as ss
#---------------------------------------------------
def getZStat(sr,t,sr_=0,skew=0,kurt=3):
z=(sr-sr_)*(t-1)**.5
z/=(1-skew*sr+(kurt-1)/4.*sr**2)**.5
return z
#---------------------------------------------------
def type1Err(z,k=1):
# false positive rate
alpha=ss.norm.cdf(-z)
alpha_k=1-(1-alpha)**k# multi-testing correction
return alpha_k
#---------------------------------------------------
def main0():
# Numerical example
t,skew,kurt,k,freq=1250,-3,10,10,250
sr=1.25/freq**.5;sr_=1./freq**.5
z=getZStat(sr,t,0,skew,kurt)
alpha_k=type1Err(z,k=k)
print alpha_k
return
#---------------------------------------------------
if __name__==‘__main__’:main0()
```
```
Elements in Quantitative Finance 119
```

```
¼ 1 Zzα
```
#### SR

```
ffiffiffiffiffiffiffiffiffiffiffiffi
T 1
```
```
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ^γ 3 SRcþ^γ^44 ^1 SRc^2
```
```
q
```
#### 2

(^64)

#### 3

(^75) ¼ 1 β;
wherezα¼Z^1 ½ðÞ 1 αK^1 =K. Accordingly, theindividualpower of the test
increases withSR, sample length, and skewness, however it decreases with
kurtosis. This probability 1ðÞβ is alternatively known as the true positive
rate, power, or recall.
In Section 8.3,wedefined the familywise false negative (miss) probability as
the probability thatallindividual positives are missed,βK¼βK. For a given
pairðÞαK;βK, we can derive the pairðÞα;β and imply the valueSRsuch that
P½maxkf^z½ 0 kgk¼ 1 ;...;K>zαjSR¼SR¼ 1 β. The interpretation is that, at a
FWERαK, achieving a familywise power above 1ðÞβK requires that the true
Sharpe ratio exceedsSR. In other words, the test is not powerful enough to
detect true strategies with a Sharpe ratio below that implied SR.
We can derive the Type II error under multiple testing (βK) as follows:first,
given a FWERαK, which is either set exogenously or it is estimated as
explained in theprevious section, compute the single-test critical value,zα;
second, the probability of missing a strategy with Sharpe ratio SR is
β¼Z½zαθ, where
θ¼

#### SR

```
ffiffiffiffiffiffiffiffiffiffiffiffi
T 1
```
```
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 ^γ 3 SRcþ^γ^44 ^1 SRc^2
```
```
q ;
```
third, from the individual false negative probability, we deriveβK¼βKas the
probability that all positives are missed.
Let us apply the above equations to the numerical example in theprevious
section. There, we estimated that the FWER wasαK≈ 0 :0608, which implies a
critical valuezα≈ 2 :4978. Then, the probability of missing a strategy with a true
Sharpe ratio SR≈ 0 :0632 (nonannualized) isβ≈ 0 :6913, whereθ≈ 1 :9982.
This high individual Type II error probability is understandable, because the
test is not powerful enough to detect such a weak signal (an annualized Sharpe
ratio of only 1.0) after a single trial. But because we have conducted ten trials,
βK≈ 0 :0249. The test detects more than 97.5% of the strategies with a true
Sharpe ratio SR≥ 0 :0632.Code Snippet 8.4provides the python code that
replicates these results (see Code Snippet 8.3for functions getZStat and
type1Err).

120 Machine Learning for Asset Managers


```
8.8.4 The Interaction between Type I and Type II Errors
```
Figure 8.4illustrates the interrelation betweenαandβ. The top distribution
models the probability ofSR estimates under the assumption that^ H 0 is true. The
bottom distribution (plotted upside down, to facilitate display) models the
probability ofSR estimates under the assumption that^ H 1 is true, and in
particular under the scenario where SR¼1. The sample length, skewness,
and kurtosis influence the variance of these two distributions. Given an actual
estimateSR, those variables determine the probabilitiesc αandβ, where decreas-
ing one implies increasing the other. In most journal articles, authors focus on
the“top”distribution and ignore the“bottom”distribution.
The analytic solution we derived for Type II errors makes it obvious that this
trade-off also exists betweenαKandβK, although in a not so straightforward
manner as in theK¼1 case.Figure 8.5shows that, for afixedαK,asK
increases,αdecreases,zαincreases, henceβincreases.

#### SNIPPET8.4 TYPEII ERROR,WITHNUMERICALEXAMPLE

```
def getTheta(sr,t,sr_=0,skew=0,kurt=3):
theta=sr_*(t-1)**.5
theta/=(1-skew*sr+(kurt-1)/4.*sr**2)**.5
return theta
#---------------------------------------------------
def type2Err(alpha_k,k,theta):
# false negative rate
z=ss.norm.ppf((1-alpha_k)**(1./k))# Sidak’s correction
beta=ss.norm.cdf(z-theta)
return beta
#---------------------------------------------------
def main0():
# Numerical example
t,skew,kurt,k,freq=1250,-3,10,10,250
sr=1.25/freq**.5;sr_=1./freq**.5
z=getZStat(sr,t,0,skew,kurt)
alpha_k=type1Err(z,k=k)
theta=getTheta(sr,t,sr_,skew,kurt)
beta=type2Err(alpha_k,k,theta)
beta_k=beta**k
print beta_k
return
#---------------------------------------------------
if __name__==‘__main__’:main0()
```
```
Elements in Quantitative Finance 121
```

```
–0.4
–3 –2 –1 0 1 2 3
```
```
–0.3
```
```
–0.2
```
```
–0.1
```
```
0.0
```
```
0.1
```
```
0.2
```
```
0.3
```
```
0.4
```
```
z ^[0]
```
```
H 0 : SR = 0
```
```
H 1 : SR > 0
```
```
0 zα
```
```
θ α
```
- _pdf β_ = _Z_ [ _zα_ – _θ_ ]

```
[ z
[0]|
```
```
H^1
```
```
],
pdf
```
```
[ z
[0]|
```
```
H^0
```
```
]
```
```
^
```
```
Figure 8.4Illustration of the interrelation betweenαandβ.
```
```
–0.4
–3 –2 –1 0 1 2 3
```
```
–0.3
```
```
–0.2
```
```
–0.1
```
```
0.0
```
```
0.1
```
```
0.2
```
```
0.3
```
```
0.4
```
```
z ^[0]
```
```
H 0 : SR = 0
```
```
H 1 : SR > 0
```
```
0
```
```
zα
θ αk
```
- _β_ = _Z_ [ _zα_ – _θ_ ]
_pdf_

```
[ z [0]|
```
```
H^1
```
```
],
pdf
```
```
[ z
[0]|
```
```
H^0
```
```
]
```
```
^
```
```
H 0 : SR = 0
```
```
H 1 : SR > 0
```
```
0
```
```
zα
θ αk
```
```
β = Z [ zα – θ ]
```
```
Figure 8.5The interaction betweenαKandβ.
```
122 Machine Learning for Asset Managers


Figure 8.6plotsβKasKincreases for various levels ofαK. Althoughβ
increases withK, the overall effect is to decreaseβK. For afixedαK, the equation
that determinesβKas a function ofKandθis

```
βK¼ Z½Z^1 ½ðÞ 1 αK^1 =K
```
```
i
θÞK:
```
## 8.9 Conclusions

The Sharpe ratio of an investment strategy under a single trial follows a
Gaussian distribution, even if the strategy returns are non-Normal (still, returns
must be stationary and ergodic). Researchers typically conduct a multiplicity of
trials, and selecting out of them the best performing strategy increases the
probability of selecting a false strategy. In this section, we have studied two
alternative procedures to evaluate the extent to which testing set overfitting
invalidates a discovered investment strategy.
Thefirst approach relies on the False Strategy theorem. This theorem derives
the expected value of the maximum Sharpe ratio, E½maxkfSRckg, as a function
of the number of trials,K, and the variance of the Sharpe ratios across the trials,
V½fSRckg. ML methods allow us to estimate these two variables. With this
estimate of E½maxkfSRckg, we can test whether maxkfSRckgis statistically
significant, using the deflated Sharpe ratio (Bailey and López de Prado 2014).

```
0.0
5 10 15
Number of trials ( K )
```
```
20 25
```
```
0.1
```
```
0.2
```
```
0.3
```
```
Familywise false negative probability (
```
```
βk
)
```
```
0.4
```
```
0.5
```
```
0.01
0.025
0.005
```
```
0.6
```
```
Figure 8.6βKasKincreases forθ≈ 1 :9982 andαK 2 0 : 01 ; 0 : 025 ; 0 : 05 gf.
```
```
Elements in Quantitative Finance 123
```

The second approach estimates the number of trials,K, and appliesŠidàk’s
correction to derive the familywise error rate (FWER). The FWER provides an
adjusted rejection threshold on which we can test whether maxkfSRckgis
statistically significant, using the distributions proposed byLo (2002)and
Mertens (2002). Researchers can use these analytical estimates of the family-
wise false positives probability and familywise false negatives probability when
they design their statistical tests.

## 8.10 Exercises

1 Following the approach described inSection 8.2, plot the precision and recall
associated with a test as a function ofθ2½ 0 ; 1 , whereα¼β¼ 0 :05 and
K¼1. Is this consistent with your intuition?
2 Repeat Exercise 1, plotting a surface as a function ofK¼ 1 ;...;25. What is
the overall effect of multiple testing on precision and recall?
3 Consider a strategy withfive years of daily IID Normal returns. The best trial
out of ten yields an annualized Sharpe ratio of 2, where the variance across
the annualized Sharpe ratios is 1.
a What is the expected maximum Sharpe ratio? Hint: Apply the False
Strategy theorem.
b After one trial, what is the probability of observing a maximum Sharpe
ratio equal or higher than 2? Hint: This is the probabilistic Sharpe ratio.
c After ten trials, what is the probability of observing a maximum Sharpe
ratio equal or higher than 2? Hint: This is the deflated Sharpe ratio.
4 Consider an investment strategy that buys S&P 500 futures when a price
moving average with a short lookback exceeds a price moving average with a
longer lookback.
a Generate 1,000 times series of strategy returns by applying different
combinations of
i Short lookback
ii Long lookback
iii Stop-loss
iv Profit taking
v Maximum holding period
b Compute the maximum Sharpe ratio out of the 1,000 experiments.
c Derive E½maxkfSRckg, as explained inSection 8.7.
d Compute the probability of observing a Sharpe ratio equal to or higher than
4(b).
5 Repeat Exercise 4, where this time you compute the familywise Type I and
Type II errors, where SRis the median across the 1,000 Sharpe ratios.

124 Machine Learning for Asset Managers


### Appendix A: Testing on Synthetic Data

Synthetic data sets allow researchers to test investment strategies on series
equivalent to thousands of historical years, and prevent overfitting to a parti-
cular observed data set. Generally speaking, these synthetic data sets can be
generated via two approaches: resampling and Monte Carlo.Figure A.1sum-
marizes how these approaches branch out and relate to each other.
Resampling consists of generating new (unobserved) data sets by sampling
repeatedly on the observed data set. Resampling can be deterministic or ran-
dom. Instances of deterministic resampling include jackknife (leave-one-out),
cross-validation (one-fold-out), and combinatorial cross-validation (permuta-
tion tests). For instance, one could divide the historical observations intoNfolds
and compute all testing sets that result from leavingkfolds out. This combina-
torial cross-validation yieldsNk NNk

```

complete historical paths, which are
```
harder to overfit than a single-path historical backtest (see AFML, chapter 12,
for an implementation). Instances of random resampling include subsampling
(random sampling without replacement) and bootstrap (random sampling with
replacement). Subsampling relies on weaker assumptions, however it is imprac-
tical when the observed data set has limited size. Bootstrap can generate
samples as large as the observed data set, by drawing individual observations
or blocks of them (hence preserving the serial dependence of the observations).
The effectiveness of a bootstrap depends on the independence of the random
samples, a requirement inherited from the central limit theorem. To make the
random draws as independent as possible, the sequential bootstrap adjusts
online the probability of drawing observations similar to those already sampled
(see AFML, chapter 4, for an implementation).
The second approach to generating synthetic data sets is Monte Carlo. A
Monte Carlo randomly samples new (unobserved) data sets from an estimated
population or data-generating process, rather than from an observed data set
(like a bootstrap would do). Monte Carlo experiments can be parametric or
nonparametric. An instance of a parametric Monte Carlo is a regime-switching
time series model (Hamilton 1994), where samples are drawn from alternative
processes,n¼ 1 ;...;N, and where the probabilitypt;nof drawing from process
nat timetis a function of the process from which the previous observation was
drawn (a Markov chain). Expectation-maximization algorithms can be used to
estimate the probability of transitioning from one process to another at timet
(the transition probability matrix). This parametric approach allows researchers
to match the statistical properties of the observed data set, which are then


**Synthetic dataset**

```
Resamplings
```
```
Random
```
```
Deterministic
```
```
Permutation test (all combinations) Combinatorialcross-validation
```
```
(leave k out)
```
```
Cross-validation
```
```
Jackknife (leave-one-out)(one-fold-out)
```
```
Subsample
(withoutrepetition)
```
```
Bootstap
(with repetition)
```
```
Sequential
bootstrap
```
```
(adjusts
```
```
prob online)
```
```
ParametricRegime-switchingtime series
```
```
Monte Carlo
```
```
Non-parametric
```
```
Variationalautoencoders
```
```
Generativeadversarialnetworks
```
```
Figure
```
#### A.1

```
Generation
```
```
of
```
```
synthetic
```
```
data
```
```
sets.
```

replicatedin the unobserveddata set. One caveatof parametricMonteCarlois
that the data-generatingprocessmaybe morecomplexthanafinite set of
algebraicfunctionscan replicate.Whenthat is the case,nonparametricMonte
Carloexperimentsmaybe of help,suchas variationalautoencoders,self-
organizingmaps,or generativeadversarialnetworks.Thesemethodscan be
understoodas nonparametric,nonlinearestimatorsof latentvariables(similarto
a nonlinearPCA).An autoencoderis a neuralnetworkthat learnshow to represent
high-dimensionalobservationsin a low-dimensionalspace.Variationalauto-
encodershavean additionalpropertywhichmakestheirlatentspacescontin-
uous.This allowsfor successfulrandomsamplingand interpolationand, in turn,
theiruse as a generativemodel.Oncea variationalautoencoderhas learnedthe
fundamentalstructureof the data,it can generatenew observationsthat resem-
ble the statisticalpropertiesof the originalsample,withina givendispersion
(hencethe notionof“variational”). A self-organizingmapdiffersfromauto-
encodersin that it appliescompetitivelearning(ratherthanerror-correction),
and it uses a neighborhoodfunctionto preservethe topologicalpropertiesof the
inputspace.Generativeadversarialnetworkstraintwo competingneuralnet-
works,where one network(calleda generator)is tasked withgenerating
simulatedobservationsfroma distributionfunction,and the othernetwork
(calleda discriminator)is taskedwithpredictingthe probabilitythat the simu-
latedobservationsare falsegiventhe trueobserveddata.Thetwo neural
networkscompetewitheachother,untiltheyconvergeto an equilibrium.The
originalsampleon whichthe nonparametricMonteCarlois trainedmustbe
representativeenoughto learnthe generalcharacteristicsof the data-generating
process,otherwisea parametricMonteCarloapproachshouldbe preferred(see
AFML,chapter13, for an example).

```
AppendixA: Testingon SyntheticData 127
```

### Appendix B: Proof of the“False Strategy”Theorem

It is known that the maximum value in a sample of independent random
variables following an exponential distribution converges asymptotically to a
Gumbel distribution. For a proof, seeEmbrechts et al. (2003, 138–47). As a
particular case, the Gumbel distribution covers the Maximum Domain of
Attraction of the Gaussian distribution, and therefore it can be used to estimate
the expected value of the maximum of several independent random Gaussian
variables.
To see how, suppose a sample of independent and identically distributed
Gaussian random variables,ykeN½ 0 ; 1 ,k¼ 1 ;...;K. If we apply the Fisher–
Tippet–Gnedenko theorem to the Gaussian distribution, we derive an
approximation for the sample maximum, maxk ykgf , leading to

```
lim
K→∞
prob
maxkfykgα
β
≤x
```
#### 

```
¼G½x; (1)
```
where G½x¼ee
x
is the CDF for the Standard Gumbel distribution,
α¼Z^1 ½ 1 ð 1 =KÞ,β¼Z^1 ½ 1 ð 1 =KÞe^1 α, andZ^1 corresponds to the
inverse of the Standard Normal’s CDF. SeeResnick (1987)and Embrechts et al.
(2003)for a derivation of the normalizing constantsðÞα;β.
The limit of the expectation of the normalized maxima from a distribution in
the Gumbel Maximum Domain of Attraction (see Proposition 2.1(iii) in
Resnick 1987)is

```
Klim→∞E
```
```
maxkfykgα
β
```
#### 

```
¼γ; (2)
```
whereγis the Euler–Mascheroni constant,γ≈ 0 : 5772 ...For a sufficiently large
K, the mean of the sample maximum of standard normally distributed random
variables can be approximated by

```
E½max
k
ykgf≈αþγβ¼ðÞ 1 γZ^11 
```
#### 1

#### K

#### 

```
þγZ^11 
```
#### 1

#### K

```
e^1
```
#### 

#### ; (3)

whereK£ 1 :
Now consider a set of estimated performance statisticsfSRckg,k¼ 1 ;...;K,
with independent and identically distributed GaussianSRckeN

#### 

```
0 ;V½fSRckg
```
#### 

#### .


We make use of the linearity of the expectation operator, to derive the
expression

```
E½maxk fSRckg V½fSRckg
```
```
i
Þ
```
(^1) = 2
≈ðÞ 1 γZ^11 

#### 1

#### K

#### 

```
þγZ^11 
```
#### 1

```
Ke
```
#### 

#### :

#### (4)

This concludes the proof of the theorem.

```
Appendix B: Proof of the“False Strategy”Theorem 129
```