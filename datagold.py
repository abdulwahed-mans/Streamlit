# fetch historical data for gold (in this example, GLD ETF as a proxy for gold) and save it to a CSV file
# datagold.py
import yfinance as yf
import pandas as pd

# Fetch historical data for gold (in this example, GLD ETF as a proxy for gold)
data = yf.download('GLD', start='2010-01-01', end='2023-01-01')

# Save to CSV
data.to_csv('gold_prices.csv')

# Display the first few rows
print(data.head())
