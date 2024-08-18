import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
import openai
import os

# تحميل مفتاح الـ API من متغير البيئة
openai.api_key = os.getenv("OPENAI_API_KEY")

# تحميل بيانات السهم
def get_stock_data(ticker):
    try:
        data = yf.download(ticker, period='1mo', interval='1d')
        if data.empty:
            st.error("No data found for the given ticker symbol.")
            return None
        return data
    except Exception as e:
        st.error(f"Error downloading data: {e}")
        return None

# حساب المؤشرات الفنية
def calculate_indicators(data):
    try:
        data['SMA'] = data['Close'].rolling(window=3).mean()
        data['EMA'] = data['Close'].ewm(span=12, adjust=False).mean()

        delta = data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss

        data['RSI'] = 100 - (100 / (1 + rs))

        ema12 = data['Close'].ewm(span=12, adjust=False).mean()
        ema26 = data['Close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = ema12 - ema26
        data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

        data['Upper Band'] = data['Close'].rolling(window=20).mean() + data['Close'].rolling(window=20).std() * 2
        data['Lower Band'] = data['Close'].rolling(window=20).mean() - data['Close'].rolling(window=20).std() * 2

        return data
    except Exception as e:
        st.error(f"Error calculating indicators: {e}")
        return None

# تحليل البيانات باستخدام ChatGPT
def analyze_with_chatgpt(data):
    prompt = f"""Given the following technical indicators for the stock:
    RSI: {data['RSI'].iloc[-1]},
    MACD: {data['MACD'].iloc[-1]},
    Signal Line: {data['Signal'].iloc[-1]},
    Upper Bollinger Band: {data['Upper Band'].iloc[-1]},
    Lower Bollinger Band: {data['Lower Band'].iloc[-1]},
    Close Price: {data['Close'].iloc[-1]}

    What should be the trading decision?"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial advisor."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        st.error(f"Error communicating with OpenAI API: {e}")
        return "Could not determine a trading decision."

# عرض البيانات والقرارات
def display_data(data):
    st.write(data.tail())
    st.line_chart(data[['Close', 'SMA', 'EMA']])
    st.line_chart(data[['MACD', 'Signal']])
    st.write(f"RSI: {data['RSI'].iloc[-1]:.2f}")
    st.write(f"Bollinger Bands: Upper Band = {data['Upper Band'].iloc[-1]:.2f}, Lower Band = {data['Lower Band'].iloc[-1]:.2f}")

# تطبيق Streamlit
def main():
    st.title('تطبيق تحليل فني لأسهم الذهب')
    ticker = st.text_input('أدخل رمز السهم (مثل GOLD):', 'GOLD')
    if st.button('تحليل'):
        data = get_stock_data(ticker)
        if data is not None:
            data = calculate_indicators(data)
            if data is not None:
                decision = analyze_with_chatgpt(data)
                st.write(f"قرار التداول: {decision}")
                display_data(data)

if __name__ == "__main__":
    main()
