# -*- coding: utf-8 -*-
import numpy as np
import scipy.stats as ss
from sklearn.metrics import mutual_info_score

def numBins(nObs, corr=None):
    if corr is None:
        z = (8 + 324 * nObs + 12 * (36 * nObs + 729 * nObs ** 2) ** .5) ** (1 / 3.)
        b = round(z / 6. + 2. / (3 * z) + 1. / 3)
    else:
        b = round(2 ** -.5 * (1 + (1 + 24 * nObs / (1. - corr ** 2)) ** .5) ** .5)
    
    return int(b)

def varInfo(x, y, bins, norm=False):
    bXY = numBins(x.shape[0], corr=np.corrcoef(x, y)[0, 1])
    bins = bXY
    cXY = np.histogram2d(x, y, bins)[0]
    hX = ss.entropy(np.histogram(x, bins)[0])
    hY = ss.entropy(np.histogram(y, bins)[0])
    iXY = mutual_info_score(None, None, contingency=cXY)
    vXY = hX + hY - 2 * iXY
    if norm:
        hXY = hX + hY - iXY
        vXY = vXY / hXY
        
    return vXY

def mutualInfor(x, y, norm=False):
    bXY = numBins(x.shape[0], corr=np.corrcoef(x, y)[0, 1])
    cXY = np.histogram2d(x, y, bXY)[0]
    iXY = mutual_info_score(None, None, contingency=cXY)
    if norm:
        hX = ss.entropy(np.histogram(x, bXY)[0])
        hY = ss.entropy(np.histogram(y, bXY)[0])
        iXY /= min(hX, hY)

    return iXY

if __name__ == '__main__':
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(0, 1, 1000)
    bins = 10

    cXY = np.histogram2d(x, y, bins)[0]
    hX = ss.entropy(np.histogram(x, bins)[0])
    hY = ss.entropy(np.histogram(y, bins)[0])
    iXY = mutual_info_score(None, None, contingency=cXY)
    iXYn = iXY / min(hX, hY)
    hXY = hX + hY - iXY
    hX_Y = hXY - hY
    hY_X = hXY - hX
    
    size, seed = 5000, 0
    np.random.seed(seed)
    x = np.random.normal(size=size)
    e = np.random.normal(size=size)
    y = 0 * x + e
    nmi = mutualInfor(x, y, True)
    corr = np.corrcoef(x, y)[0, 1]