# Generated from: 3_Distance_Metrics.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Chapter 3 Distance Metrics
#
# Look beyond correlations to understand codependency


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm


# SNIPPET 3.1 MARGINAL, JOINT, CONDITIONAL ENTROPIES, AND MUTUAL INFORMATION
import numpy as np
import scipy.stats as ss
from sklearn.metrics import mutual_info_score

x = np.random.random(100)
y = np.random.random(100)
bins = 100
# The bi-dimensional histogram of samples x and y. Values in x are histogrammed along the first dimension and values in y are histogrammed along the second dimension.
cXY = np.histogram2d(x, y, bins)[0]
hX = ss.entropy(np.histogram(x, bins)[0])  # marginal
hY = ss.entropy(np.histogram(y, bins)[0])  # marginal
iXY = mutual_info_score(None, None, contingency=cXY)
iXYn = iXY/min(hX, hY)  # normalized mutual information
hXY = hX+hY-iXY  # joint
hX_Y = hXY-hY  # conditional
hY_X = hXY-hX  # conditional

print('**'*8+'\n')
print('hX marginal entropy: {}'.format(hX))
print('hY marginal entropy: {}'.format(hY))
print('iXY mutual info score: {}'.format(iXY))
print('iXYn normalized mutual information: {}'.format(iXYn))
print('hX_Y cross entropy between x and y : {}'.format(hX_Y))
print('hY_X cross entropy between y and x : {}'.format(hY_X))


# SNIPPET 3.2 MUTUAL INFORMATION, VARIATION OF INFORMATION, AND NORMALIZED VARIATION OF INFORMATION
def varInfo(x, y, bins, norm=False):
    # variation of information
    cXY = np.histogram2d(x, y, bins)[0]
    iXY = mutual_info_score(None, None, contingency=cXY)
    hX = ss.entropy(np.histogram(x, bins)[0])  # marginal
    hY = ss.entropy(np.histogram(y, bins)[0])  # marginal
    vXY = hX+hY-2*iXY  # variation of information
    if norm:
        hXY = hX+hY-iXY  # joint
        vXY /= hXY  # normalized variation of information
    return vXY


# SNIPPET 3.3 VARIATION OF INFORMATION ON DISCRETIZED CONTINUOUS RANDOM VARIABLES
def numBins(nObs, corr=None):
    # Optimal number of bins for discretization
    if corr is None:  # univariate case
        z = (8+324*nObs+12*(36*nObs+729*nObs**2)**.5)**(1/3.)
        b = round(z/6.+2./(3*z)+1./3)
    else:  # bivariate case
        if (1.-corr**2) == 0:
            corr = np.sign(corr)*(np.abs(corr)-1e-5)
        b = round(2**-.5*(1+(1+24*nObs/(1.-corr**2))**.5)**.5)
    return int(b)
# ---------------------------------------------------


def varInfo_optBIn(x, y, norm=False):  # Discretized and with optimal bin value
    # variation of information
    bXY = numBins(x.shape[0], corr=np.corrcoef(x, y)[0, 1])
    cXY = np.histogram2d(x, y, bXY)[0]
    iXY = mutual_info_score(None, None, contingency=cXY)
    hX = ss.entropy(np.histogram(x, bXY)[0])  # marginal
    hY = ss.entropy(np.histogram(y, bXY)[0])  # marginal
    vXY = hX+hY-2*iXY  # variation of information
    if norm:
        hXY = hX+hY-iXY  # joint
        vXY /= hXY  # normalized variation of information
    return vXY


# SNIPPET 3.4 CORRELATION AND NORMALIZED MUTUAL INFORMATION OF TWO INDEPENDENT GAUSSIAN RANDOM VARIABLES
def mutualInfo(x, y, norm=False):
    # mutual information
    bXY = numBins(x.shape[0], corr=np.corrcoef(x, y)[0, 1])
    cXY = np.histogram2d(x, y, bXY)[0]
    iXY = mutual_info_score(None, None, contingency=cXY)
    if norm:
        hX = ss.entropy(np.histogram(x, bXY)[0])  # marginal
        hY = ss.entropy(np.histogram(y, bXY)[0])  # marginal
        iXY /= min(hX, hY)  # normalized mutual information
    return iXY


# ---------------------------------------------------
size, seed = 5000, 0
np.random.seed(seed)
x = np.random.normal(size=size)
e = np.random.normal(size=size)
y = 0*x+e
nmi = mutualInfo(x, y, True)
corr = np.corrcoef(x, y)[0, 1]


# Exercise 3.13.1


bins = 10

rho_list = [-1, -0.5, 0, 0.5, 1]
hX = hY = hXY = hX_Y = iXY = viXY = vi_t_XY = np.zeros(len(rho_list))
for i in tqdm(range(len(rho_list))):
    rho = rho_list[i]
    mu, sigma = 0, 1
    rr = np.random.normal(mu, sigma, size=(2, 1000))
    x, y_ = rr[0, :], rr[1, :]
    y = rho * x+np.sqrt(1-rho**2)*y_

    # The bi-dimensional histogram of samples x and y. Values in x are histogrammed along the first dimension and values in y are histogrammed along the second dimension.
    cXY = np.histogram2d(x, y, bins)[0]
    hX[i] = ss.entropy(np.histogram(x, bins)[0])  # marginal
    hY[i] = ss.entropy(np.histogram(y, bins)[0])  # marginal
    iXY[i] = mutual_info_score(None, None, contingency=cXY)
    hXY[i] = hX[i]+hY[i]-iXY[i]  # joint
    hX_Y[i] = hXY[i]-hY[i]  # conditional
    viXY[i] = varInfo(x, y, bins)
    vi_t_XY[i] = varInfo_optBIn(x, y)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(rho_list, hX, label='H[X]')
ax.plot(rho_list, hY, label='H[Y]')
# ax.plot(rho_list, hXY, label='H[X,Y]')
# ax.plot(rho_list, hX_Y, label='H[X|Y]')
# ax.plot(rho_list, iXY, label='I[X,Y]')
# ax.plot(rho_list, viXY, label='VI[X,Y]')
# ax.plot(rho_list, vi_t_XY, label=r'$\tilde{VI}$[X,Y]')
ax.legend()


cXY = np.histogram2d(x, y, bins)[0]
cXY


rr = np.random.normal(mu, sigma, size=(2, 1000))
rr[0,:].shape

