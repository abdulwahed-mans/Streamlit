import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# بيانات تشبه تلك الموجودة في الصورة
data = {
    'Current Price': 2539.70,
    'Low Price': 2536.15,
    'High Price': 2551.35,
    'Target Price': 2547.5,  # يمكن تعديل هذه القيمة بناءً على التحليل الفني أو الاستراتيجية المتبعة
    'Previous Close': 2547.5,
    'Sentiment': 'Strong Buy',
    'Change': -7.80,  # التغيير اليومي في السعر
    'Change Percentage': -0.31  # نسبة التغيير اليومي
}

# عرض البيانات في جدول مع توضيح التغيير ونسبة التغيير
gold_data = pd.DataFrame([data])

st.subheader("Gold Price Data")
st.dataframe(gold_data)

# إنشاء المؤشر الدائري (Gauge) مع تحسين الألوان والمعلومات المعروضة
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=data['Current Price'],
    delta={
        'reference': data['Previous Close'],
        'position': "top",
        'relative': True,
        'valueformat': ".2f",
        'increasing': {'color': "green"},
        'decreasing': {'color': "red"}
    },
    gauge={
        'axis': {'range': [data['Low Price'], data['High Price']], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': 'darkblue'},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [data['Low Price'], (data['Low Price'] + data['High Price']) / 2], 'color': 'lightgray'},
            {'range': [(data['Low Price'] + data['High Price']) / 2, data['High Price']], 'color': 'lightgreen'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': data['Target Price']
        },
    },
    title={'text': "Gold Price Sentiment", 'font': {'size': 24}},
    number={'prefix': "$"}
))

# إضافة مشاعر السوق (Sentiment) كنص إضافي مع تحسين العرض
fig.update_layout(
    height=400,
    margin={'t': 50, 'b': 0, 'l': 25, 'r': 25},
    annotations=[
        dict(
            x=0.5, y=0, showarrow=False,
            text=f"Sentiment: {data['Sentiment']}",
            font=dict(size=20),
            align="center"
        ),
        dict(
            x=0.5, y=0.15, showarrow=False,
            text=f"Change: {data['Change']} ({data['Change Percentage']}%)",
            font=dict(size=14),
            align="center"
        )
    ]
)

st.plotly_chart(fig)

# تخصيص مظهر التطبيق باستخدام CSS
st.markdown("""
<style>
    .stApp {
        font-family: Arial, sans-serif;
    }
    .stButton button {
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
