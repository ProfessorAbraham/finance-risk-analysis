import pandas as pd

def rolling_volatility(df, window=30):
    """Compute rolling volatility of log returns"""
    df['volatility_30d'] = df['log_return'].rolling(window=window).std()
    return df
