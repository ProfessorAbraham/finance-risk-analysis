# visualize.py

import matplotlib.pyplot as plt

def plot_prices(df):
    plt.figure(figsize=(14,6))
    plt.plot(df['Price'], color='blue')
    plt.title("Brent Oil Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.show()

def plot_log_returns(df, change_point=None, events=None):
    plt.figure(figsize=(14,6))
    plt.plot(df['log_return'], color='green')
    if change_point:
        plt.axvline(change_point, color='red', linestyle='--', label='Change Point')
    if events is not None:
        for _, row in events.iterrows():
            plt.axvline(row['date'], color='orange', alpha=0.5)
    plt.title("Brent Oil Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.legend()
    plt.show()
