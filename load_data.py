import sqlite3
import pandas as pd

DB_PATH = '/Users/sakicansev/Documents/practice/prices.db'

conn = sqlite3.connect(DB_PATH)

query = """
        SELECT s.timestamp, p.name, p.symbol, p.coin_id, p.price_usd, p.change_24h
        FROM prices p
        JOIN snapshots s ON s.id = p.snapshot_id 
        """

df = pd.read_sql_query(query, conn)

df ['timestamp'] = pd.to_datetime(df['timestamp'])

print(df.head())
print(len(df))
print(df.dtypes)
print(df['timestamp'].min(), df['timestamp'].max())

btc = df[df['coin_id'] == 'bitcoin'].copy()
btc = btc.sort_values('timestamp')
btc['time_diff'] = btc['timestamp'].diff()
print(btc['time_diff'].describe())

print(btc[btc['time_diff'] > pd.Timedelta(hours=1)][['timestamp', 'time_diff']])

pivot = df.pivot_table(index='timestamp', columns='coin_id', values='price_usd')
print(pivot.head())