import matplotlib.pyplot as plt

def plot_prices(df):
    plt.figure(figsize=(14,6))
    plt.plot(df['Price'], label='Brent Oil Price')
    plt.title("Brent Oil Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()

def plot_log_returns(df, change_point=None, events=None):
    plt.figure(figsize=(14,6))
    plt.plot(df.index, df['log_return'], label='Log Returns', color='orange')
    if change_point:
        plt.axvline(change_point, color='red', linestyle='--', label='Change Point')
    if events is not None:
        for _, row in events.iterrows():
            plt.axvline(row['date'], color='blue', linestyle=':', alpha=0.6)
            plt.text(row['date'], df['log_return'].max()*0.8, row['event_name'], rotation=90, fontsize=8)
    plt.title("Log Returns with Change Points and Events")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.legend()
    plt.show()