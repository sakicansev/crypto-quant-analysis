from load_data import load_prices
from models import volatility, correlation, var, sharpe, rolling_correlation

df = load_prices()

print('Ronning volatility model...')
volatility.run(df)

print('Running correlation model...')
correlation.run(df)

print("Running VaR model...")
var.run(df)

print("Running Sharpe ratio model...")
sharpe.run(df)

print("Running rolling correlation model...")
rolling_correlation.run(df)

print("All models complete. Charts saved.")
