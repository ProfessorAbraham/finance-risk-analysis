import matplotlib.pyplot as plt

def plot_prices(df):
    plt.figure(figsize=(14,6))
    plt.plot(df.index, df['Price'], color='blue')
    plt.title("Brent Oil Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

def plot_log_returns(df, change_point=None, events=None):
    plt.figure(figsize=(14,6))
    plt.plot(df.index, df['log_return'], color='black', label='Log Returns')
    
    if change_point:
        plt.axvline(change_point, color='red', linestyle='--', label='Change Point')
    
    if events is not None:
        for _, row in events.iterrows():
            plt.axvline(row['date'], color='orange', linestyle=':', alpha=0.5)
            plt.text(row['date'], df['log_return'].min(), row['event_name'], rotation=90, fontsize=8)
    
    plt.title("Brent Oil Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.legend()
    plt.show()
