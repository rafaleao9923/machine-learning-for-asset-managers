# -*- coding: utf-8 -*-
import statsmodels.api as sm1
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

def tValLinR(close):
    x = np.ones((close.shape[0], 2))
    x[:, 1] = np.arange(close.shape[0])
    ols = sm1.OLS(close, x).fit()
    return ols.tvalues[1]

def getBinsFromTrend(molecule, close, span):
    out = pd.DataFrame(index=molecule, columns=['t1', 'tVal', 'bin', 'windowSize'])
    hrzns = range(*span)
    maxWindow = span[1] - 1
    for idx in close.index:
        idx += maxWindow
        if idx >= len(close):
            break
        df_tval = pd.Series(dtype='float64')
        iloc0 = close.index.get_loc(idx)
        for hrzn in hrzns:
            dt1 = close.index[iloc0 - hrzn + 1]
            df1 = close.loc[dt1:idx]
            df_tval.loc[dt1] = tValLinR(df1.values)
        dt1 = df_tval.replace([-np.inf, np.inf, np.nan], 0).abs().idxmax()
        out.loc[idx, ['t1', 'tVal', 'bin', 'windowSize']] = df_tval.index[-1], df_tval[dt1], np.sign(df_tval[dt1]), abs(df_tval.values).argmax() + (span[0])
    out['t1'] = pd.to_datetime(out['t1'])
    out['bin'] = pd.to_numeric(out['bin'], downcast='signed')
    tValueVariance = out['tVal'].values.var()
    tMax = 20
    if tValueVariance < tMax:
        tMax = tValueVariance
    out.loc[out['tVal'] > tMax, 'tVal'] = tMax
    out.loc[out['tVal'] < (-1) * tMax, 'tVal'] = (-1) * tMax
    return out.dropna(subset=['bin'])

if __name__ == '__main__':
    idx_range_from = 3
    idx_range_to = 10
    df0 = pd.Series(np.random.normal(0, .1, 100)).cumsum()
    df0 += np.sin(np.linspace(0, 10, df0.shape[0]))
    df1 = getBinsFromTrend(df0.index, df0, [idx_range_from, idx_range_to, 1])
    tValues = df1['tVal'].values
    doNormalize = False
    if doNormalize:
        minusArgs = [i for i in range(len(tValues)) if tValues[i] < 0]
        tValues[minusArgs] = tValues[minusArgs] / (np.min(tValues) * (-1.0))
        plus_one = [i for i in range(len(tValues)) if tValues[i] > 0]
        tValues[plus_one] = tValues[plus_one] / np.max(tValues)
    plt.scatter(df1.index, df0.loc[df1.index].values, c=tValues, cmap='viridis')
    plt.plot(df0.index, df0.values, color='gray')
    plt.colorbar()
    plt.show()
    plt.savefig('fig5.2.png')
    plt.clf()
    plt.close()
    plt.scatter(df1.index, df0.loc[df1.index].values, c=df1['bin'].values, cmap='viridis')

    ols_tvalue = tValLinR(np.array([3.0, 3.5, 4.0]))