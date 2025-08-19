import pandas as pd
import numpy as np

def load_data(path):
    """Load dataset from CSV"""
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df.sort_values('Date', inplace=True)
    df.set_index('Date', inplace=True)
    return df

def compute_log_return(df):
    """Compute log returns"""
    df['log_return'] = np.log(df['Price']).diff()
    df = df.dropna()
    return df
