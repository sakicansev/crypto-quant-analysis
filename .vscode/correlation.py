from load_data import load_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = load_prices()
cutoff = pd.Timestamp('2026-05-31 22:21:00', tz='UTC')
clean = df[df['timestamp'] > cutoff]

pivot = clean.pivot_table(
    index='timestamp',
    columns='coin_id',
    values='price_usd'
)
pivot.columns.name = None

log_returns = np.log(pivot / pivot.shift(1))
corr_matrix = log_returns.corr()

corr_matrix.columns = ['ALGO', 'AVAX', 'BTC', 'ADA', 'LINK', 'ETH', 'DOT', 'MATIC', 'SOL', 'USDC']
corr_matrix.index = ['ALGO', 'AVAX', 'BTC', 'ADA', 'LINK', 'ETH', 'DOT', 'MATIC', 'SOL', 'USDC']

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Crypto Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation_matrix.png')

print(corr_matrix)
print('Chart saved.')