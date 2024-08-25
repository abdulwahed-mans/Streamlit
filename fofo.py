import streamlit as st
import mplfinance as mpf
import matplotlib.pyplot as plt

st.title("تحليل أنماط الشموع اليابانية لأسعار الذهب")

# تحديد الفترة الزمنية
start_date = st.date_input("تاريخ البدء", df.index.min())
end_date = st.date_input("تاريخ النهاية", df.index.max())

filtered_data = df[start_date:end_date]

# عرض مخطط الشموع اليابانية
fig, ax = plt.subplots(figsize=(12, 6))
mpf.plot(filtered_data, type='candle', style='yahoo', volume=False, ax=ax)
st.pyplot(fig)

# عرض عدد الأنماط المكتشفة
st.write(f"عدد الشموع على شكل مطرقة: {filtered_data['Hammer'].sum()}")
st.write(f"عدد الشموع على شكل شهاب: {filtered_data['Shooting_Star'].sum()}")

# عرض الجدول مع الأنماط المكتشفة
st.write(filtered_data[['Open', 'High', 'Low', 'Close', 'Hammer', 'Shooting_Star']])
