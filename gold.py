import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

# Tailwind CSS Styling
st.markdown('''
    <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css');
        body { background-color: #f9fafb; }
        .stApp { max-width: 800px; margin: auto; padding: 20px; }
        h1 { color: #1f2937; font-size: 2.5rem; }
    </style>
''', unsafe_allow_html=True)

# Title
st.title('Gold Stocks - Historical and Current Data')

# User Input for Ticker Symbol
ticker = st.text_input('Enter Gold Stock Ticker:', 'GC=F')

# Date range selection
start_date = st.date_input('Start date', pd.to_datetime('2023-01-01'))
end_date = st.date_input('End date', pd.to_datetime('today'))

# Fetching Data with Error Handling
try:
    data = yf.Ticker(ticker)
    hist = data.history(start=start_date, end=end_date)
    
    if hist.empty:
        st.warning(f"No data found for {ticker} in the given date range.")
    else:
        # Attempt to get the current price
        current_price = hist['Close'].iloc[-1] if not hist.empty else None

        if current_price:
            st.metric(label="Current Price", value=f"${current_price:.2f}")
        else:
            st.warning(f"Could not retrieve current price for {ticker}.")

        # Plotting the Data
        st.subheader(f'{ticker} Stock Price ({start_date} to {end_date})')
        chart = alt.Chart(hist.reset_index()).mark_line().encode(
            x='Date:T',
            y='Close:Q',
            tooltip=['Date:T', 'Close:Q']
        ).interactive()

        st.altair_chart(chart, use_container_width=True)
except Exception as e:
    st.error(f"Failed to retrieve data for {ticker}. Error: {e}")
