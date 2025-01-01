# Machine Learning for Asset Managers

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Code Style](https://img.shields.io/badge/code%20style-black-black)]()

This repository is an advanced-level implementation of machine learning techniques for asset management, based on the book **"Machine Learning for Asset Managers"** by Prof. Marcos López de Prado. Designed for real-world applications, this project provides robust tools for portfolio optimization, risk management, and trading strategies that can generate significant monetary value.

## 🚀 Key Features

- **Data Preprocessing**: Advanced techniques to clean and enhance financial data, ensuring more accurate predictions.
- **Clustering and Correlation Analysis**: Unsupervised learning algorithms to group financial instruments based on correlation, improving portfolio diversification.
- **Strategy Development**: Sophisticated labeling methods like trend-scanning and triple-barrier for precise strategy development.
- **Feature Importance Analysis**: Tools to identify and prioritize the most impactful features in financial models.
- **Portfolio Optimization**: Implementation of modern portfolio theory and hierarchical risk parity (HRP) for optimized asset allocation.
- **Backtesting and Validation**: Techniques to measure and mitigate overfitting, ensuring robust backtesting results.

## 🛠 Tech Stack

- **Python 3.8+**
- **NumPy**: For high-performance numerical computations.
- **Pandas**: For efficient data manipulation and analysis.
- **Scikit-learn**: For machine learning models and utilities.
- **Matplotlib/Seaborn**: For comprehensive data visualization.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/machine-learning-for-asset-managers.git
   cd machine-learning-for-asset-managers
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚦 Quick Start

### Data Preprocessing
```python
from src.data_preprocessing import denoise_matrix

# Example usage
S_value = np.random.rand(100, 10)  # Replace with actual financial data
denoised_matrix = denoise_matrix(S_value)
```

### Clustering and Correlation Analysis
```python
from src.clustering import optimal_clustering

# Example usage
correlation_matrix = np.random.rand(10, 10)  # Replace with actual correlation matrix
clusters = optimal_clustering(correlation_matrix)
```

### Portfolio Optimization
```python
from src.portfolio_optimization import hierarchical_risk_parity

# Example usage
returns_matrix = np.random.rand(100, 10)  # Replace with actual returns data
weights = hierarchical_risk_parity(returns_matrix)
```

## 📁 Project Structure

```
machine-learning-for-asset-managers/
├── src/                         # Source code for the project
│   ├── data_preprocessing/      # Data cleaning and enhancement techniques
│   ├── clustering/              # Clustering algorithms for portfolio diversification
│   ├── strategy_development/    # Strategy development and labeling methods
│   ├── feature_importance/      # Feature importance analysis for model optimization
│   ├── portfolio_optimization/  # Portfolio construction and optimization techniques
│   ├── backtesting/             # Backtesting and validation methods
│   └── utils/                   # Utility functions and helpers
├── data/                        # Sample data for testing and validation
│   ├── raw/                     # Raw data files
│   ├── processed/               # Processed data files
│   └── results/                 # Results from analysis and backtesting
├── tests/                       # Comprehensive unit tests for each module
├── docs/                        # Documentation and project guides
├── notebooks/                   # Jupyter notebooks for exploratory analysis
├── config/                      # Configuration files for the project
├── logs/                        # Log files for debugging and monitoring
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
```

## 🧪 Testing

To run the unit tests, use the following command:
```bash
python -m unittest discover tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📚 References

- López de Prado, M. (2020). **Machine Learning for Asset Managers**. Cambridge University Press.
- [Hudson & Thames Quantitative Research](https://hudsonthames.org/)

## 📧 Contact

For any questions or feedback, please reach out to [your-email@example.com](mailto:your-email@example.com).

---

**Disclaimer**: This project is for educational purposes only. The techniques and strategies discussed should not be considered financial advice. Always conduct your own research and consult with a financial advisor before making investment decisions.