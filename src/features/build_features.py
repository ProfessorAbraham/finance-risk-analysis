# src/features/build_features.py
import pandas as pd
def rolling_volatility(df, window=30):
    """Compute rolling std of log returns"""
    df['volatility_30d'] = df['log_return'].rolling(window=window).std()
    df = df.dropna(subset=['volatility_30d'])  # drop initial NaNs
    return df