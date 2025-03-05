import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os
import math
import matplotlib.pylab as plt
import matplotlib

from Machine_Learning_for_Asset_Managers import ch2_fitKDE_find_best_bandwidth as best_bandwidth
from Machine_Learning_for_Asset_Managers import ch2_marcenko_pastur_pdf as mp
from Machine_Learning_for_Asset_Managers import ch2_monte_carlo_experiment as mc
from Machine_Learning_for_Asset_Managers import ch4_optimal_clustering as oc
import onc as onc
from Machine_Learning_for_Asset_Managers import ch5_financial_labels as fl
from Machine_Learning_for_Asset_Managers import ch7_portfolio_construction as pc


def get_OL_tickers_close(T=936, N=234):
    ol = pd.read_csv('csv/ol_ticker.csv', sep='\t', header=None)
    ticker_names = ol[0]
    closePrice = np.empty([T, N])
    covariance_matrix = np.empty([T, N])
    portfolio_name = [[None] for x in range(N)]
    ticker_adder = 0
    for i in range(0, len(ticker_names)):
        ticker = ticker_names[i]
        print(ticker)
        ol_ticker = ticker + '.ol'
        df = yf.Ticker(ol_ticker)
        try:
            ticker_df = df.history(period="7y")
            if ticker_df.shape[0] > T and ticker != 'EMAS' and ticker != 'AVM':
                closePrice[:, ticker_adder] = ticker_df['Close'][-T:].values
                portfolio_name[ticker_adder] = ol_ticker
                ticker_adder += 1
            else:
                print("no data for ticker:" + ol_ticker)
        except ValueError:
            print("no history:"+ol_ticker)
    return closePrice, portfolio_name


def denoise_OL(S, do_plot=True):
    np.argwhere(np.isnan(S))
    cor = np.corrcoef(S, rowvar=0)
    eVal0, eVec0 = mp.getPCA(cor)
    print(np.argwhere(np.isnan(np.diag(eVal0))))
    T = float(S.shape[0])
    N = S.shape[1]
    q = float(S.shape[0])/S.shape[1]
    eMax0, var0 = mp.findMaxEval(np.diag(eVal0), q, bWidth=.01)
    nFacts0 = eVal0.shape[0]-np.diag(eVal0)[::-1].searchsorted(eMax0)
    if do_plot:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.hist(np.diag(eVal0), density=True, bins=100)
        pdf0 = mp.mpPDF(var0, q=S.shape[0]/float(S.shape[1]), pts=N)
        plt.plot(pdf0.keys(), pdf0, color='r')
        plt.show()
    corr1 = mp.denoisedCorr(eVal0, eVec0, nFacts0)
    eVal1, eVec1 = mp.getPCA(corr1)
    return eVal0, eVec0, eVal1, eVec1, corr1, var0


def calculate_returns(S, percentageAsProduct=False):
    ret = np.zeros((S.shape[0]-1, S.shape[1]))
    cum_sums = np.zeros(S.shape[1])
    for j in range(0, S.shape[1]):
        cum_return = 0
        S_ret = np.zeros(S.shape[0]-1)
        for i in range(0, S.shape[0]-1):
            if percentageAsProduct == True:
                S_ret[i] = 1+((S[i+1, j]-S[i, j])/S[i, j])
            else:
                S_ret[i] = ((S[i+1, j]-S[i, j])/S[i, j])
        cum_return = np.prod(S_ret)-1
        cum_sums[j] = cum_return
        ret[:, j] = S_ret
    return ret, cum_sums


def getVolatility(S):
    return [np.std(S[:, i]) for i in range(0, S.shape[1])]


def test_exception_in_plotting_efficient_frontier(S_value):
    mvo = MeanVarianceOptimisation()
    pdPrice = pd.DataFrame(S_value)
    pdPrice.index = pd.RangeIndex(start=0, stop=6, step=1)
    dates = ['2019-01-01', '2019-02-01', '2019-03-01',
             '2019-04-01', '2019-05-01', '2019-06-01']
    pdPrice['Datetime'] = pd.to_datetime(dates)
    pdPrice.set_index('Datetime')
    expected_returns = ReturnsEstimators().calculate_mean_historical_returns(
        asset_prices=pdPrice, resample_by=None)
    covariance = ReturnsEstimators().calculate_returns(
        asset_prices=pdPrice, resample_by=None).cov()
    plot = mvo.plot_efficient_frontier(
        covariance=covariance, max_return=1.0, expected_asset_returns=expected_returns)
    assert len(plot._A) == 41
    plot.savefig('books_read.png')
    print("read books")


def testNCO():
    N = 5
    T = 5
    S_value = np.array([[1., 2, 3,  4, 5],
                        [1.1, 3, 2,  3, 5],
                        [1.2, 4, 1.3, 4, 5],
                        [1.3, 5, 1,  3, 5],
                        [1.4, 6, 1,  4, 5.5],
                        [1.5, 7, 1,  3, 5.5]])
    S_value[:, 1] = 1
    S_value[5, 1] = 1.1
    S, _ = calculate_returns(S_value)
    _, instrument_returns = calculate_returns(
        S_value, percentageAsProduct=True)
    np.testing.assert_almost_equal(S, pd.DataFrame(
        S_value).pct_change().dropna(how="all"))
    mu1 = None
    cov1_d = np.cov(S, rowvar=0, ddof=1)
    corr1 = mp.cov2corr(cov1_d)
    a, b, c = nco.NCO()._cluster_kmeans_base(pd.DataFrame(corr1))
    d, e, f = oc.clusterKMeansBase(pd.DataFrame(corr1))
    min_var_markowitz = mc.optPort(cov1_d, mu1).flatten()
    min_var_NCO = pc.optPort_nco(cov1_d, mu1, max(
        int(cov1_d.shape[0]/2), 2)).flatten()
    mlfinlab_NCO = nco.NCO().allocate_nco(
        cov1_d, mu1, max(int(cov1_d.shape[0]/2), 2)).flatten()
    cov1_d = np.cov(S, rowvar=0, ddof=1)
    mlfinlab_NCO = nco.NCO().allocate_nco(
        cov1_d, mu1, int(cov1_d.shape[0]/2)).flatten()
    expected_return_markowitz = [
        min_var_markowitz[i]*instrument_returns[i] for i in range(0, cov1_d.shape[0])]
    e_m = sum(expected_return_markowitz)
    expected_return_NCO = [min_var_NCO[i]*instrument_returns[i]
                           for i in range(0, cov1_d.shape[0])]
    e_NCO = sum(expected_return_markowitz)
    vol = getVolatility(S_value)
    m_minVol = [min_var_markowitz[i]*vol[i] for i in range(0, cov1_d.shape[0])]
    NCO_minVol = [mlfinlab_NCO[i]*vol[i] for i in range(0, cov1_d.shape[0])]


if __name__ == '__main__':
    testNCO()
    N = 333
    T = 936
    S_value = np.loadtxt('csv/ol184.csv', delimiter=',')
    if S_value.shape[0] < 1 or not os.path.exists('csv/portfolio_name.csv'):
        S_value, portfolio_name = get_OL_tickers_close(T, N)
        np.savetxt('csv/ol184.csv', S_value, delimiter=',')
        np.savetxt('csv/portfolio_name.csv',
                   portfolio_name, delimiter=',', fmt='%s')
    portfolio_name = pd.read_csv(
        'csv/portfolio_name.csv', sep='\t', header=None).values
    lastIndex = 173
    S_value = S_value[:, 0:lastIndex]
    portfolio_name = portfolio_name[0:lastIndex]
    S, instrument_returns = calculate_returns(S_value)
    _, instrument_returns = calculate_returns(
        S_value, percentageAsProduct=True)
    print(np.asarray(portfolio_name)[np.argsort(instrument_returns)])
    eVal0, eVec0, denoised_eVal, denoised_eVec, denoised_corr, var0 = denoise_OL(
        S)
    detoned_corr = mp.detoned_corr(
        denoised_corr, denoised_eVal, denoised_eVec, market_component=1)
    detoned_eVal, detoned_eVec = mp.getPCA(detoned_corr)
    denoised_eigenvalue = np.diag(denoised_eVal)
    eigenvalue_prior = np.diag(eVal0)
    plt.plot(range(0, len(denoised_eigenvalue)), np.log(
        denoised_eigenvalue), color='r', label="Denoised eigen-function")
    plt.plot(range(0, len(eigenvalue_prior)), np.log(
        eigenvalue_prior), color='g', label="Original eigen-function")
    plt.xlabel("Eigenvalue number")
    plt.ylabel("Eigenvalue (log-scale)")
    plt.legend(loc="upper right")
    plt.show()
    detoned_cov = mc.corr2cov(detoned_corr, var0)
    w = mc.optPort(detoned_cov)
    print(w)
    minVarPortfolio_var = np.dot(np.dot(w.T, detoned_corr), w)
    nCols, minBlockSize = 183, 2
    print("minBlockSize"+str(minBlockSize))
    corr0 = detoned_corr
    corr1, clstrs, silh = oc.clusterKMeansTop(pd.DataFrame(detoned_corr))
    tStatMeanDepth = np.mean(
        [np.mean(silh[clstrs[i]]) / np.std(silh[clstrs[i]]) for i in clstrs.keys()])
    print("tstat at depth:")
    print(tStatMeanDepth)
    corr1, clstrs, silh = oc.clusterKMeansTop(pd.DataFrame(detoned_corr))
    tStatMeanDepth = np.mean(
        [np.mean(silh[clstrs[i]]) / np.std(silh[clstrs[i]]) for i in clstrs.keys()])
    print("tstat at depth:")
    print(tStatMeanDepth)
    # raise SystemExit

    # ------------------------------------------------------------
    # ------------------------------------------------------------

    # corr11, clstrs11, silh11 = onc.get_onc_clusters(pd.DataFrame(detoned_corr)) #test with mlfinlab impl: 1: [18, 24, 57, 81, 86, 99, 112, 120, 134, 165]

    # invert y-axis to get origo at lower left corner
    matplotlib.pyplot.matshow(corr11)
    matplotlib.pyplot.gca().xaxis.tick_bottom()
    matplotlib.pyplot.gca().invert_yaxis()
    matplotlib.pyplot.colorbar()
    matplotlib.pyplot.show()

    # Chapter 5 Financial labels
    # Lets try trend-following on PHO
    idxPHO = 118
    idxBGBIO = 29
    idxWWI = 169
    pho = S_value[:, idxBGBIO]
    df0 = pd.Series(pho[-50:])
    # [3,10,1] = range(3,10)
    df1 = fl.getBinsFromTrend(df0.index, df0, [3, 10, 1])
    tValues = df1['tVal'].values

    lastTValue = []
    for i in range(0, lastIndex):
        pho = S_value[:, i]
        df0 = pd.Series(pho[-50:])
        # [3,10,1] = range(3,10)
        df1 = fl.getBinsFromTrend(df0.index, df0, [3, 10, 1])
        tValues = df1['tVal'].values
        lastTValue.append(tValues[41])

    np.argmax(lastTValue)

    # df1['tVal'].values, cmap='viridis')
    plt.scatter(df1.index, df0.loc[df1.index].values,
                c=tValues, cmap='viridis')
    plt.colorbar()
    plt.show()

    bgbio_df = yf.Ticker("BGBIO.ol")
    bg_bio_ticker_df = bgbio_df.history(period="7y")

    bgbio = bg_bio_ticker_df['Close']
    df0 = pd.Series(bgbio[-200:])
    # [3,10,1] = range(3,10)
    df1 = fl.getBinsFromTrend(df0.index, df0, [3, 20, 1])
    tValues = df1['tVal'].values
    # df1['tVal'].values, cmap='viridis')
    plt.scatter(df1.index, df0.loc[df1.index].values,
                c=tValues, cmap='viridis')
    plt.colorbar()
    plt.show()

    S, pnames = get_OL_tickers_close()

    # get t-statistics from all instruments on OL
    S, pnames = get_OL_tickers_close(T=200, N=237)

    np.argwhere(np.isnan(S))
    S[182, 110] = S[181, 110]

    # implementing from book
    abc = [None for i in range(0, 237)]
    for i in range(0, 20):  # len(pnames)):
        instrument = S[:, i]
        df0 = pd.Series(instrument)
        print("running bins on:"+pnames[i]+" i:"+str(i))
        abc[i] = fl.getBinsFromTrend(df0.index, df0, [3, 10, 1])['tVal']

    tValLatest = [abc[i].values[-20] for i in range(0, len(abc))]
    # most significant t-value:
    np.max(tValLatest)
    pnames[np.argmax(tValLatest)]
    # END / implementing from book

    # mlfinlab impl
    S[181, 110] = S[180, 110]  # nan
    abc = [None for i in range(0, 237)]
    for i in range(0, len(abc)):
        ticker_close = pd.DataFrame(S[:, i], columns={'ticker'})
        print(i)
        t_events = ticker_close.index
        tr_scan_labels = ts.trend_scanning_labels(ticker_close, t_events, 20)
        abc[i] = tr_scan_labels['t_value']

    abc = np.asarray(abc)
    tValLatest = [abc[i, -20] for i in range(0, len(abc))]
    # most significant t-value:
    np.max(tValLatest)
    pnames[np.argmax(tValLatest)]

    plt.scatter(ticker_close.index, S[:, 78], c=abc[78], cmap='viridis')

    # Chapter 7 - apply the Nested Clustered Optimization (NCO) algorithm
    N = 234
    T = 936
    S_value = np.loadtxt('csv/ol184.csv', delimiter=',')
    S, instrument_returns = calculate_returns(S_value)
    _, instrument_returns = calculate_returns(
        S_value, percentageAsProduct=True)
    np.argsort(instrument_returns)
    # 26,  84, 167,  35,  76, 169,  31, 137,  28,  64,  36,  37,  92, 116], dtype=int64)

    eVal0, eVec0, denoised_eVal, denoised_eVec, denoised_corr, var0 = denoise_OL(
        S)
    q = float(S.shape[0])/float(S.shape[1])  # T/N
    bWidth = best_bandwidth.findOptimalBWidth(np.diag(eVal0))
    cov1_d = mc.deNoiseCov(np.cov(S, rowvar=0, ddof=1), q, bWidth['bandwidth'])

    mu1 = None
    min_var_markowitz = mc.optPort(cov1_d, mu1).flatten()
    min_var_NCO = pc.optPort_nco(cov1_d, mu1, int(cov1_d.shape[0]/2)).flatten()

    # calulate on time-series not returns
    cov1_d = np.cov(S_value, rowvar=0, ddof=1)
    min_var_markowitz = mc.optPort(cov1_d, mu1).flatten()
    min_var_NCO = pc.optPort_nco(cov1_d, mu1, int(cov1_d.shape[0]/2)).flatten()
    # note pnames = pnames[1:] - first element is obx

    ########
    T, N = 237, 235
    # x = np.random.normal(0, 1, size = (T, N))
    S, pnames = get_OL_tickers_close(T, N)
    np.argwhere(np.isnan(S))
    S[204, 109] = S[203, 109]

    cov0 = np.cov(S, rowvar=0, ddof=1)
    q = float(S.shape[0])/float(S.shape[1])  # T/N
    # eMax0, var0 = mp.findMaxEval(np.diag(eVal0), q, bWidth=.01)

    corr0 = mp.cov2corr(cov0)
    eVal0, eVec0 = mp.getPCA(corr0)
    bWidth = best_bandwidth.findOptimalBWidth(np.diag(eVal0))

    min_var_markowitz = mc.optPort(cov1_d, mu1).flatten()
    min_var_NCO = pc.optPort_nco(cov1_d, mu1, int(cov1_d.shape[0]/2)).flatten()

    ##################
    # Test if bWidth found makes sense
    pdf0 = mp.mpPDF(1., q=T/float(N), pts=N)
    # empirical pdf
    pdf1 = mp.fitKDE(np.diag(eVal0), bWidth=bWidth['bandwidth'])
    # pdf1 = mp.fitKDE(np.diag(eVal0), bWidth=0.1)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(np.diag(eVal0), density=True, bins=50)  # Histogram the eigenvalues
    plt.plot(pdf0.keys(), pdf0, color='r', label="Marcenko-Pastur pdf")
    plt.plot(pdf1.keys(), pdf1, color='g', label="Empirical:KDE")
    plt.legend(loc="upper right")
    plt.show()

    N = 1000
    T = 10000
    x = np.random.normal(0, 1, size=(T, N))
    cor = np.corrcoef(x, rowvar=0)
    eVal0, eVec0 = mp.getPCA(cor)
    bWidth = best_bandwidth.findOptimalBWidth(np.diag(eVal0))
    # {'bandwidth': 4.328761281083057}
    ###############

    bWidth = 0.1
    cov1_d = mc.deNoiseCov(cov0, q, bWidth)
    mu1 = None

    min_var_markowitz = mc.optPort(cov1_d, mu1).flatten()
    min_var_NCO = pc.optPort_nco(cov1_d, mu1, int(cov1_d.shape[0]/2)).flatten()
