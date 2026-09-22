import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def load_business_data():
    np.random.seed(42)
    n = 150
    marketing_budget = np.random.uniform(50, 500, n)
    unit_price = np.random.uniform(20, 150, n)
    units_sold = (0.4 * marketing_budget) - (1.2 * unit_price) + np.random.normal(100, 25, n)
    units_sold = np.maximum(units_sold, 10)

    return pd.DataFrame({
        'MarketingBudget': np.round(marketing_budget, 2),
        'UnitPrice': np.round(unit_price, 2),
        'UnitsSold': np.round(units_sold, 2),
    })


def build_model():
    df = load_business_data()
    X = df[['MarketingBudget', 'UnitPrice']]
    y = df['UnitsSold']
    model = LinearRegression()
    model.fit(X, y)
    return df, model
