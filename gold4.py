import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st


# تحميل بيانات الذهب
ticker = "GC=F"  # رمز الذهب في بورصة نيويورك
df = yf.download(ticker, period="max")

# حساب المتوسط المتحرك
df['MA50'] = df['Close'].rolling(window=50).mean()

# إنشاء واجهة المستخدم
st.title("مستشار تداول أسهم الذهب")

# عرض الرسم البياني
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='إغلاق السعر')
plt.plot(df['MA50'], label='المتوسط المتحرك (50 يوم)')
plt.xlabel('التاريخ')
plt.ylabel('السعر')
plt.legend()
st.pyplot(plt)

# منطق التداول (مثال مبسط)
if df['Close'].iloc[-1] > df['MA50'].iloc[-1]:
    st.write("توصية: الشراء")
else:
    st.write("توصية: البيع أو الانتظار")

# إعدادات إضافية (اختياري)
st.subheader("إعدادات")
timeframe_options = ['يومي', 'اسبوعي', 'شهري']
selected_timeframe = st.selectbox('إطار زمني', timeframe_options)