# Documentation for `ch2_marcenko_pastur_pdf.py`

## Marcenko-Pastur pdf

The Marcenko-Pastur distribution describes the asymptotic behavior of the eigenvalues of large random matrices.

### Functions

- **mpPDF(var, q, pts)**: Computes the Marcenko-Pastur probability density function.

- **getPCA(matrix)**: Performs principal component analysis on a given matrix.

- **fitKDE(obs, bWidth, kernel, x)**: Fits a kernel density estimate to a series of observations.

- **getRndCov(nCols, nFacts)**: Generates a random covariance matrix.

- **cov2corr(cov)**: Derives the correlation matrix from a covariance matrix.

- **corr2cov(corr, std)**: Converts a correlation matrix back to a covariance matrix.

- **errPDFs(var, eVal, q, bWidth, pts)**: Computes the error between the theoretical and empirical PDFs.

- **findMaxEval(eVal, q, bWidth)**: Finds the maximum eigenvalue by fitting the Marcenko-Pastur distribution.

- **denoisedCorr(eVal, eVec, nFacts)**: Denoises the correlation matrix by fixing a random eigenvalue.

- **detoned_corr(corr, eigenvalues, eigenvectors, market_component)**: De-tones the correlation matrix by removing the market component.

- **test_detone()**: Tests the detoning function with a sample covariance matrix.

### Main Execution

The script generates random data, computes correlations, and fits the Marcenko-Pastur distribution to analyze eigenvalues of random matrices.