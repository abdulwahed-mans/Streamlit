import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

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

# إعدادات الألوان والخلفية للمؤشر الدائري
plot_bgcolor = "#def"
quadrant_colors = [plot_bgcolor, "#2bad4e", "#85e043", "#eff229", "#f2a529", "#f25829"]
quadrant_text = ["", "<b>Very Low</b>", "<b>Low</b>", "<b>Medium</b>", "<b>High</b>", "<b>Very High</b>"]
n_quadrants = len(quadrant_colors) - 1

# إعداد قيمة المؤشر
current_value = data['Current Price']
min_value = data['Low Price']
max_value = data['High Price']
hand_length = np.sqrt(2) / 4
hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))

# إنشاء المؤشر الدائري
fig = go.Figure(
    data=[
        go.Pie(
            values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),
            rotation=90,
            hole=0.5,
            marker_colors=quadrant_colors,
            text=quadrant_text,
            textinfo="text",
            hoverinfo="skip",
        ),
    ],
    layout=go.Layout(
        showlegend=False,
        margin=dict(b=0, t=10, l=10, r=10),
        width=450,
        height=450,
        paper_bgcolor=plot_bgcolor,
        annotations=[
            go.layout.Annotation(
                text=f"<b>Gold Price:</b><br>${current_value} USD",
                x=0.5, xanchor="center", xref="paper",
                y=0.25, yanchor="bottom", yref="paper",
                showarrow=False,
            )
        ],
        shapes=[
            go.layout.Shape(
                type="circle",
                x0=0.48, x1=0.52,
                y0=0.48, y1=0.52,
                fillcolor="#333",
                line_color="#333",
            ),
            go.layout.Shape(
                type="line",
                x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                line=dict(color="#333", width=4)
            )
        ]
    )
)

# عرض المؤشر الدائري في تطبيق Streamlit
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
