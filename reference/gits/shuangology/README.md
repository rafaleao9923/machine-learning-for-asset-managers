# Machine-Learning-for-Asset-Managers
Implementation of code snippets and exercises in the book *Machine Learning for Asset Managers* written by Prof. Marcos López de Prado.

## 2_Denoising_and_Detoning.ipynb
This notebook focuses on techniques for denoising and detoning empirical covariance matrices, which are critical for improving the quality of financial data used in portfolio optimization and risk management. Key topics covered include:

1. **Marcenko-Pastur Theorem**: Theoretical foundation for understanding the distribution of eigenvalues in random matrices.
2. **Denoising Techniques**:
   - Constant Residual Eigenvalue Method: Replaces noise-related eigenvalues with a constant value.
   - Targeted Shrinkage: Adjusts the contribution of noise-related eigenvectors using a shrinkage parameter.
3. **Covariance Matrix Simulation**: Generates synthetic covariance matrices with embedded signal and noise.
4. **Empirical Results**: Demonstrates the impact of denoising on minimum variance portfolio optimization.
5. **Exercises**:
   - Downloads historical S&P 500 stock data.
   - Computes log returns and covariance matrices.
   - Constructs efficient frontiers using Monte Carlo simulations.
   - Applies denoising techniques to real-world financial data.

The notebook provides practical implementations of the concepts discussed in Chapter 2 of the book, along with visualizations and performance metrics.
