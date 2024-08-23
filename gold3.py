import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st


# تحميل بيانات الذهب
ticker = "GC=F"  # رمز الذهب في بورصة نيويورك
df = yf.download(ticker, period="max")

# حساب المتوسط المتحرك
df['MA50'] = df['Close'].rolling(window=50).mean()

# إنشاء واجهة المستخدم
st.title("مستشار تداول أسهم الذهب")

# عرض الرسم البياني
st.line_chart(df[['Close', 'MA50']])

# منطق التداول (مثال مبسط)
if df['Close'].iloc[-1] > df['MA50'].iloc[-1]:
    st.write("توصية: الشراء")
else:
    st.write("توصية: البيع أو الانتظار")