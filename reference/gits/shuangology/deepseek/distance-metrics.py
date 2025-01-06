import numpy as np
import scipy.stats as ss
# from sklearn.metrics import mutual_info_score

def calculate_entropy(x, bins):
    hist, _ = np.histogram(x, bins=bins, density=True)
    hist = hist[hist > 0]  # Remove zero entries to avoid log(0)
    return -np.sum(hist * np.log(hist))

def calculate_mutual_info(x, y, bins, norm=False):
    cXY, _, _ = np.histogram2d(x, y, bins=bins, density=True)
    cXY = cXY[cXY > 0]  # Remove zero entries
    iXY = np.sum(cXY * np.log(cXY / np.outer(cXY.sum(axis=1), cXY.sum(axis=0)).flatten()))
    if norm:
        hX = calculate_entropy(x, bins)
        hY = calculate_entropy(y, bins)
        iXY /= min(hX, hY)  # Normalized mutual information
    return iXY

def calculate_joint_entropy(x, y, bins):
    cXY, _, _ = np.histogram2d(x, y, bins=bins, density=True)
    cXY = cXY[cXY > 0]  # Remove zero entries
    return -np.sum(cXY * np.log(cXY))

def calculate_conditional_entropy(x, y, bins):
    hXY = calculate_joint_entropy(x, y, bins)
    hY = calculate_entropy(y, bins)
    return hXY - hY

def calculate_variation_of_info(x, y, bins, norm=False):
    hX = calculate_entropy(x, bins)
    hY = calculate_entropy(y, bins)
    iXY = calculate_mutual_info(x, y, bins)
    vXY = hX + hY - 2 * iXY  # Variation of information
    if norm:
        hXY = calculate_joint_entropy(x, y, bins)
        vXY /= hXY  # Normalized variation of information
    return vXY

def num_bins(nObs, corr=None):
    if corr is None:  # Univariate case
        z = (8 + 324 * nObs + 12 * (36 * nObs + 729 * nObs**2)**0.5)**(1/3.)
        b = int(np.ceil(z / 6 + 2 / (3 * z) + 1 / 3))
    else:  # Bivariate case
        if np.isclose(1. - corr**2, 0):
            corr = np.sign(corr) * (np.abs(corr) - 1e-5)
        b = int(np.ceil(2**-0.5 * (1 + (1 + 24 * nObs / (1. - corr**2))**0.5)**0.5))
    return max(1, b)

def calculate_mutual_info_opt_bins(x, y, norm=False):
    bXY = num_bins(len(x), corr=np.corrcoef(x, y)[0, 1])
    return calculate_mutual_info(x, y, bXY, norm)

def calculate_variation_of_info_opt_bins(x, y, norm=False):
    bXY = num_bins(len(x), corr=np.corrcoef(x, y)[0, 1])
    return calculate_variation_of_info(x, y, bXY, norm)
