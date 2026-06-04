# Crypto Quantitative Analysis

A quantitative risk analysis tool built in Python, analyzing real cryptocurrency 
price data collected from a live data pipeline.

## What This Project Does

- Calculates rolling volatility for 10 cryptocurrencies
- Builds a correlation matrix to measure how assets move together
- Calculates Historical Value at Risk (VaR) at 95% confidence
- All analysis runs on real market data — not sample or synthetic data

## Data Pipeline

Price data is collected via a separate JavaScript tracker 
(github.com/sakicansev/crypto-price-tracker) and stored in a local SQLite 
database updated every 30 seconds. The Python project reads directly from 
that database. This separation keeps data collection and analysis independent — 
a standard data engineering pattern.

## Models

- `models/volatility.py` — log returns and rolling volatility
- `models/correlation.py` — Pearson correlation matrix across all assets
- `models/var.py` — Historical Value at Risk (daily, 95% confidence)

## Tech Stack

Python, pandas, numpy, matplotlib, seaborn, SQLite

## Author

Saki Cansev — targeting junior data/blockchain analyst roles in Amsterdam fintech.