# Documentation for covariance_matrix_applied.py

## Resources
- Random matrix theory: https://calculatedcontent.com/2019/12/03/towards-a-new-theory-of-learning-statistical-mechanics-of-deep-neural-networks/
- Review: [Book] Commented summary of Machine Learning for Asset Managers by Marcos Lopez de Prado
  https://gmarti.gitlab.io/qfin/2020/04/12/commented-summary-machine-learning-for-asset-managers.html
- Chapter 2: This chapter essentially describes an approach that Bouchaud and his crew from the CFM have pioneered and refined for the past 20 years. The latest iteration of this body of work is summarized in Joel Bun’s Cleaning large correlation matrices: Tools from Random Matrix Theory.
  https://www.sciencedirect.com/science/article/pii/S0370157316303337
- Condition number: https://dominus.ai/wp-content/uploads/2019/11/ML_WhitePaper_MarcoGruppo.pdf

## Exercise 2.9
1. Using a series of matrix of stock returns:
   a) Compute the covariance matrix. What is the condition number of the correlation matrix?
   b) Compute one hundredth efficient frontiers by drawing one hundred alternative vectors of expected returns from a Normal distribution with mean 10% and std 10%.
   c) Compute the variance of the errors against the mean efficient frontier.

## Function Descriptions
### `get_OL_tickers_close(T=936, N=234)`
- `N`: Number of stocks in portfolio.
- `T`: Lookback time.

### `test_exception_in_plotting_efficient_frontier(S_value)`

Test raising of exception when plotting the efficient frontier.

## Code Comments
- `# pylint: disable=invalid-name, protected-access`  
- `# Note: pnames = pnames[1:] - first element is obx`  
- `# Expected return: w.T . mu`  
- `# Expected portfolio variance: W^T.(Cov).W`  
- `# mlfinlab impl`  
- `# nan`  
- `# invert y-axis to get origo at lower left corner`  
- `# most significant t-value`  