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

print(df.head())
print(len(df))