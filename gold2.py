import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# إعدادات الواجهة باستخدام Tailwind CSS
st.markdown('''
    <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css');
        body { background-color: #f9fafb; }
        .stApp { max-width: 900px; margin: auto; padding: 20px; }
        h1 { color: #1f2937; font-size: 2.5rem; }
    </style>
''', unsafe_allow_html=True)

# عنوان التطبيق
st.title('Gold Stocks Trading Advisor')

# إدخال المستخدم لرمز السهم وتواريخ التحليل
ticker = st.text_input('Enter Gold Stock Ticker:', 'GC=F')
start_date = st.date_input('Start date', pd.to_datetime('2023-01-01'))
end_date = st.date_input('End date', pd.to_datetime('today'))

# تحميل البيانات
def load_data(ticker, start, end):
    data = yf.Ticker(ticker)
    hist = data.history(start=start, end=end)
    return hist

# تحليل البيانات
def analyze_data(hist):
    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    hist['SMA_50'] = hist['Close'].rolling(window=50).mean()

    decision = "Hold"
    if hist['SMA_20'].iloc[-1] > hist['SMA_50'].iloc[-1] and hist['Close'].iloc[-1] > hist['SMA_20'].iloc[-1]:
        decision = "Buy"
    elif hist['SMA_20'].iloc[-1] < hist['SMA_50'].iloc[-1] and hist['Close'].iloc[-1] < hist['SMA_20'].iloc[-1]:
        decision = "Sell"

    return decision

# عرض الرسوم البيانية باستخدام Plotly
def plot_data(hist):
    fig = go.Figure()

    # إضافة خط السعر
    fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name='Close'))

    # إضافة المتوسطات المتحركة
    fig.add_trace(go.Scatter(x=hist.index, y=hist['SMA_20'], mode='lines', name='SMA 20'))
    fig.add_trace(go.Scatter(x=hist.index, y=hist['SMA_50'], mode='lines', name='SMA 50'))

    fig.update_layout(
        title=f"{ticker} Stock Price and Moving Averages",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

# تنفيذ التحليل والعرض
try:
    hist_data = load_data(ticker, start_date, end_date)

    if hist_data.empty:
        st.warning(f"No data found for {ticker} in the given date range.")
    else:
        decision = analyze_data(hist_data)
        st.subheader(f"Trading Recommendation: {decision}")
        st.markdown("""
        - **Buy**: Short-term bullish trend detected, consider buying.
        - **Sell**: Short-term bearish trend detected, consider selling.
        - **Hold**: Market is indecisive or showing sideways movement.
        """)

        plot_data(hist_data)

except Exception as e:
    st.error(f"Failed to retrieve data for {ticker}. Error: {e}")
