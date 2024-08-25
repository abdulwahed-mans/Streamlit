import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from datetime import datetime

# Load gold price data
data = pd.read_csv('gold_prices.csv', index_col='Date', parse_dates=True)

# Streamlit app layout
st.title("Gold Price Analyzer and Stock Buying Advisor")

# User input for date range analysis
start_date = st.date_input("Start Date:", min_value=data.index.min(), max_value=data.index.max(), value=data.index.min())
end_date = st.date_input("End Date:", min_value=start_date, max_value=data.index.max(), value=data.index.max())

# Filter data for selected date range
filtered_data = data.loc[start_date:end_date]

# Technical indicator calculations (replace with your preferred indicators)
# Example: Moving Average Convergence Divergence (MACD)
def calculate_macd(data):
    fast_ema = data['Close'].ewm(span=12, min_periods=12).mean()
    slow_ema = data['Close'].ewm(span=26, min_periods=26).mean()
    macd = fast_ema - slow_ema
    signal_line = macd.ewm(span=9, min_periods=9).mean()
    return macd, signal_line

macd, signal_line = calculate_macd(filtered_data)

# Create Plotly figure for candlestick chart with MACD
def create_candlestick_chart(data, macd, signal_line):
    fig = go.Figure()

    # Add candlestick chart
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick'
    ))

    # Add MACD line
    fig.add_trace(go.Scatter(
        x=data.index,
        y=macd,
        line=dict(color='blue', width=1.5),
        name='MACD'
    ))

    # Add Signal line
    fig.add_trace(go.Scatter(
        x=data.index,
        y=signal_line,
        line=dict(color='red', width=1.5),
        name='Signal Line'
    ))

    # Update layout
    fig.update_layout(
        title="Gold Price and MACD Indicator",
        yaxis_title="Price",
        xaxis_title="Date",
        xaxis_rangeslider_visible=False
    )

    return fig

# Create the candlestick chart with MACD
fig = create_candlestick_chart(filtered_data[['Open', 'High', 'Low', 'Close']], macd, signal_line)
st.plotly_chart(fig)

# Create gauge chart for MACD value using Plotly
def create_gauge_chart(macd_value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=macd_value,
        title={'text': "MACD Value"},
        gauge={
            'axis': {'range': [-5, 5]},
            'steps': [
                {'range': [-5, -1], 'color': "red"},
                {'range': [-1, 1], 'color': "yellow"},
                {'range': [1, 5], 'color': "green"}
            ],
        }
    ))

    fig.update_layout(
        height=400
    )

    return fig

# Display the gauge chart
gauge_fig = create_gauge_chart(macd.iloc[-1])
st.plotly_chart(gauge_fig)

# Add a section for trading recommendations based on MACD signals
def generate_trading_signals(macd, signal_line):
    signals = []
    for i in range(1, len(macd)):
        if macd[i] > signal_line[i] and macd[i-1] < signal_line[i-1]:
            signals.append('Buy')
        elif macd[i] < signal_line[i] and macd[i-1] > signal_line[i-1]:
            signals.append('Sell')
        else:
            signals.append('Hold')
    return signals

trading_signals = generate_trading_signals(macd, signal_line)
st.write("Trading Signals:")
st.write(trading_signals)
