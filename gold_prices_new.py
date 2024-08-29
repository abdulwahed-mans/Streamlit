import yfinance as yf
import pandas as pd

# Load existing gold price data
data = pd.read_csv('gold_prices.csv', index_col='Date', parse_dates=True)

# Define the ticker symbol for gold (XAUUSD for spot gold)
ticker = 'GC=F'  # This is the ticker for Gold Futures

# Fetch data from 2023-01-01 to 2024-08-25
new_data = yf.download(ticker, start="2023-01-01", end="2024-08-25")

# Keep only the necessary columns and rename them to match your existing data
new_data = new_data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Concatenate the old data with the new data
updated_data = pd.concat([data, new_data])

# Save the updated data to a new CSV file
updated_data.to_csv('updated_gold_prices.csv')

# Display the updated data
print(updated_data.tail())
