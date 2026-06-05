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
    sharpe = log_returns.mean() / log_returns.std()
    ticker_map = {
        'bitcoin': 'BTC', 'ethereum': 'ETH', 'solana': 'SOL',
        'cardano': 'ADA', 'avalanche-2': 'AVAX', 'chainlink': 'LINK',
        'polkadot': 'DOT', 'algorand': 'ALGO',
        'polygon-ecosystem-token': 'MATIC', 'usd-coin': 'USDC',
    }
    sharpe.index = sharpe.index.map(ticker_map)
    sharpe.sort_values().plot(
        kind='bar',
        title='Sharpe Ratio by Coin',
        figsize=(10, 5),
        color='steelblue'
    )
    plt.axhline(y=0, color='red', linestyle='--')
    plt.xlabel('')
    plt.ylabel('Sharpe Ratio')
    plt.tight_layout()
    plt.savefig('sharpe_ratio.png')
    return sharpe