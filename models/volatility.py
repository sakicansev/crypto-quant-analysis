from load_data import load_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = load_prices()
pivot = df.pivot_table(
    index='timestamp', 
    columns='coin_id', 
    values='price_usd'
)
# today/yesterday, then log
log_returns = np.log(pivot / pivot.shift(1))
#std over 20 periods
rolling_vol = log_returns.rolling(window=20).std()
# plot bitcoin only, drop NaN rows
rolling_vol['bitcoin'].dropna().plot(
    title='Bitcoin Rolling Volatility (20-period)',
    figsize=(12, 5)
)
plt.ylabel('Volatility (std of log returns)')
plt.tight_layout()
plt.savefig('bitcoin_volatility.png')
print("Chart saved.")

# filter only bitcoin rows
btc = df[df['coin_id'] == 'bitcoin'].copy()

# sort by time
btc = btc.sort_values('timestamp')

# time between each snapshot
btc['time_diff'] = btc['timestamp'].diff()

#summary statistics
print(btc['time_diff'].describe())

# shows gaps > 1 hour
print(btc[btc['time_diff'] > pd.Timedelta(minutes=2)][['timestamp', 'time_diff']])