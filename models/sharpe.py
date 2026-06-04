from load_data import load_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = load_prices()

cutoff = pd.Timestamp('2026-05-31 22:21:00', tz='UTC')
clean = df[df['timestamp'] > cutoff]

pivot = clean.pivot_table(
    index='timestamp',
    columns='coin_id',
    values='price_usd'
)
log_returns = np.log(pivot / pivot.shift(1))

# mean() gives average return per period, std() gives volatility.
sharpe = log_returns.mean() / log_returns.std()
print(sharpe.sort_values(ascending=False))