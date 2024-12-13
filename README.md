# QuantForecaster

## Overview
QuantForecaster-Modeling is a machine learning project designed to tackle predictive challenges in quantitative finance, particularly in sideways market scenarios. It leverages a custom **asymmetric loss function** to prioritize domain-specific requirements, emphasizing the penalty of overpredictions. 

This project showcases:
- **Custom asymmetric loss functions** to align with financial objectives.
- **Feature selection** and engineering tailored to sideways quant data.
- **Hyperparameter optimization** using GridSearchCV.
- **Performance evaluation** using Asymmetric MSE, MSE, MAE, and \( R^2 \).

## Key Features
- **Custom Loss Function**: Optimized for asymmetric penalties to align with domain needs.
- **Feature Engineering**: Effective feature selection to boost model performance.
- **Model Tuning**: Robust hyperparameter optimization for Random Forest and XGBoost.
- **Comprehensive Metrics**: Includes Asymmetric MSE, MSE, MAE, and \( R^2 \).

## Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/QuantForecaster.git
cd QuantForecaster
pip install -r requirements.txt
