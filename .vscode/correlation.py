from load_data import load_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = load_prices()
cutoff = pd.Timestamp('2026-05-31 22:21:00', tz='UTC')
clean = df[df['timestamp'] > cutoff]

# print('Total rows:', len(df))
# print('Clean rows:', len(clean))
# print('Dropped rows:', len(df) - len(clean))

pivot = clean.pivot_table(
    index='timestamp',
    columns='coin_id',
    values='price_usd'
)

log_returns = np.log(pivot / pivot.shift(1))
corr_matrix = log_returns.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Crypto Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation_matrix.png')

log_returns['bitcoin'].quantile(0.05)

print(corr_matrix)
print('Chart saved.')

