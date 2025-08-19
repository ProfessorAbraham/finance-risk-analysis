# build_features.py

def rolling_volatility(df, window=30):
    """Compute rolling volatility of log returns"""
    df['volatility_30d'] = df['log_return'].rolling(window).std()
    return df
