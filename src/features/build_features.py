def rolling_volatility(df, window=30):
    """Calculate rolling volatility of log returns"""
    return df['log_return'].rolling(window).std()