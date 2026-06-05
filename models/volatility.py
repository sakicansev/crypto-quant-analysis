from load_data import load_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run(df):
    pivot = df.pivot_table(
        index='timestamp',
        columns='coin_id',
        values='price_usd'
    )
    log_returns = np.log(pivot / pivot.shift(1))
    rolling_vol = log_returns.rolling(window=20).std()
    rolling_vol['bitcoin'].dropna().plot(
        title='Bitcoin Rolling Volatility (20-period)',
        figsize=(12, 5)
    )
    plt.ylabel('Volatility (std of log returns)')
    plt.tight_layout()
    plt.savefig('bitcoin_volatility.png')
    return rolling_vol