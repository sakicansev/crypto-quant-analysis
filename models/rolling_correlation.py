from load_data import load_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run(df):
    cutoff = pd.Timestamp('2026-05-31 22:21:00', tz='UTC')
    clean = df[df['timestamp'] > cutoff]
    pivot = clean.pivot_table(
        index='timestamp',
        columns='coin_id',
        values='price_usd'
    )
    log_returns = np.log(pivot / pivot.shift(1))
    rolling_corr = log_returns['bitcoin'].rolling(window=100).corr(log_returns['ethereum'])
    rolling_corr.dropna().plot(
        title='Rolling Correlation: BTC vs ETH (100-period)',
        figsize=(12, 5)
    )
    plt.axhline(y=0, color='red', linestyle='--')
    plt.ylabel('Correlation')
    plt.tight_layout()
    plt.savefig('rolling_correlation.png')
    return rolling_corr