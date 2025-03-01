import numpy as np
# import cupy
import pandas as pd
from scipy.stats import norm
import scipy.stats as ss
import matplotlib.pylab as plt
import matplotlib as mpl
import itertools

def getExpectedMaxSR(nTrials, meanSR, stdSR):
    emc = 0.477215664901532860606512090082402431042159336
    sr0 = (1 - emc) * norm.ppf(1 - 1. / nTrials) + emc * norm.ppf(1 - (nTrials * np.e) ** -1)
    sr0 = meanSR + stdSR * sr0
    return sr0

def getDistMaxSR(nSims, nTrials, stdSR, meanSR):
    rng = np.random.RandomState()
    out = pd.DataFrame()
    for nTrials_ in nTrials:
        sr = pd.DataFrame(rng.randn(nSims, nTrials_))
        sr = sr.sub(sr.mean(axis=1), axis=0)
        sr = sr.div(sr.std(axis=1), axis=0)
        sr = meanSR + sr * stdSR
        out_ = sr.max(axis=1).to_frame('max{SR}')
        out_['nTrials'] = nTrials_
        out = out.append(out_, ignore_index=True)
    return out

def getMeanStdError(nSims0, nSims1, nTrials, stdSR=1, meanSR=0):
    sr0 = pd.Series({i: getExpectedMaxSR(i, meanSR, stdSR) for i in nTrials})
    sr0 = sr0.to_frame('E[max{SR}]')
    sr0.index.name = 'nTrials'
    err = pd.DataFrame()
    for i in range(0, int(nSims1)):
        sr1 = getDistMaxSR(nSims=1000, nTrials=nTrials, meanSR=0, stdSR=1)
        sr1 = sr1.groupby('nTrials').mean()
        err_ = sr0.join(sr1).reset_index()
        err_['err'] = err_['max{SR}'] / err_['E[max{SR}]'] - 1.
        err = err.append(err_)
    out = {'meanErr': err.groupby('nTrials')['err'].mean()}
    out['stdErr'] = err.groupby('nTrials')['err'].std()
    out = pd.DataFrame.from_dict(out, orient='columns')
    return out

def getZStat(sr, t, sr_=0, skew=0, kurt=3):
    z = (sr - sr_) * (t - 1) ** .5
    z /= (1 - skew * sr + (kurt - 1) / 4. * sr ** 2) ** .5
    return z

def type1Err(z, k=1):
    alpha = ss.norm.cdf(-z)
    alpha_k = 1 - (1 - alpha) ** k
    return alpha_k

def getTheta(sr, t, sr_=0., skew=0., kurt=3):
    theta = sr_ * (t - 1) ** .5
    theta /= (1 - skew * sr + (kurt - 1) / .4 * sr ** 2) ** .5
    return theta

def type2Err(alpha_k, k, theta):
    z = ss.norm.ppf((1 - alpha_k) ** (1. / k))
    beta = ss.norm.cdf(z - theta)
    return beta

if __name__ == '__main__':
    nTrials = list(set(np.logspace(1, 6, 100).astype(int)))
    nTrials.sort()
    sr0 = pd.Series({i: getExpectedMaxSR(i, meanSR=0, stdSR=1) for i in nTrials}, name="E[max{SR}] (prior)")
    sr1 = getDistMaxSR(nSims=100, nTrials=nTrials, meanSR=0, stdSR=1)

    nnSR0 = list(itertools.chain.from_iterable(itertools.repeat(x, 100) for x in sr0.values))
    deviationFromExpectation = abs(sr1['max{SR}'] - nnSR0)

    ax = sr1.plot.scatter(x='nTrials', y='max{SR}', label='Max{SR} (observed)', c=deviationFromExpectation, cmap=mpl.cm.viridis.reversed())
    ax.set_xscale('log')
    ax.plot(nTrials, sr0, linestyle='--', linewidth=1, label='E[max{SR}] (prior)', color='black')
    plt.legend()
    ax.figure.savefig('/gpfs/gpfs0/deep/maxSR_across_uniform_strategies_8_1.png')

    nTrials = list(set(np.logspace(1, 6, 1000).astype(int)))
    nTrials.sort()
    stats = getMeanStdError(nSims0=1000, nSims1=100, nTrials=nTrials, stdSR=1)

    ax = stats.plot()
    ax.set_xscale('log')
    ax.figure.savefig('/gpfs/gpfs0/deep/fig82.png')

    t, skew, kurt, k, freq = 1250, -3, 10, 10, 250
    sr = 1.25 / freq ** .5
    sr_ = 1. / freq ** .5
    z = getZStat(sr, t, 0, skew, kurt)
    alpha_k = type1Err(z, k=k)
    print(alpha_k)

    z = getZStat(sr, t, 0, skew, kurt)
    alpha_k = type1Err(z, k=k)
    theta = getTheta(sr, t, sr_, skew, kurt)
    beta = type2Err(alpha_k, k, theta)
    beta_k = beta ** k
    print(beta_k)