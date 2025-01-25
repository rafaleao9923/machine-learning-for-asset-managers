# Machine Learning for Asset Managers

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Code Style](https://img.shields.io/badge/code%20style-black-black)]()

This repository contains implementations of code snippets and exercises from the book **"Machine Learning for Asset Managers"** by Prof. Marcos López de Prado. The project focuses on applying machine learning techniques to asset management, including portfolio optimization, risk management, and trading strategies.

## 🚀 Features

- **Denoising and Detoning**: Techniques to clean and enhance financial data.
- **Distance Metrics**: Implementation of various distance metrics for financial data analysis.
- **Optimal Clustering**: Algorithms for clustering financial instruments based on correlation.
- **Financial Labels**: Methods for labeling financial data, including trend-scanning and triple-barrier methods.
- **Feature Importance Analysis**: Tools for analyzing the importance of features in financial models.
- **Portfolio Construction**: Implementation of modern portfolio theory and hierarchical risk parity (HRP).
- **Testing Set Overfitting**: Techniques to measure and mitigate overfitting in backtesting.

## 🛠 Tech Stack

- **Python 3.8+**
- **NumPy**: For numerical computations.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For machine learning models and utilities.
- **Matplotlib/Seaborn**: For data visualization.

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

### Denoising and Detoning
```python
from ml_asset_managers.ch2_denoising import denoise_matrix

# Example usage
S_value = np.random.rand(100, 10)  # Replace with actual financial data
denoised_matrix = denoise_matrix(S_value)
```

### Optimal Clustering
```python
from ml_asset_managers.ch4_clustering import optimal_clustering

# Example usage
correlation_matrix = np.random.rand(10, 10)  # Replace with actual correlation matrix
clusters = optimal_clustering(correlation_matrix)
```

### Portfolio Construction
```python
from ml_asset_managers.ch7_portfolio import hierarchical_risk_parity

# Example usage
returns_matrix = np.random.rand(100, 10)  # Replace with actual returns data
weights = hierarchical_risk_parity(returns_matrix)
```

## 📁 Project Structure

```
machine-learning-for-asset-managers/
├── ch2_denoising/               # Denoising and detoning techniques
├── ch3_distance_metrics/        # Distance metrics for financial data
├── ch4_clustering/              # Optimal clustering algorithms
├── ch5_financial_labels/        # Financial labeling methods
├── ch6_feature_importance/      # Feature importance analysis
├── ch7_portfolio/               # Portfolio construction techniques
├── ch8_overfitting/             # Testing set overfitting analysis
├── data/                        # Sample data for testing
├── tests/                       # Unit tests for each module
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