import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Function to get data (replace with actual data fetching logic)
def get_gold_data():
    # Placeholder for actual data fetching logic
    current_value = 75  # Example value
    sentiment = "Strong Buy"  # Example sentiment
    return current_value, sentiment

# Get data
current_value, sentiment = get_gold_data()

# Gauge creation logic
quadrant_text = ["Strong Sell", "Sell", "Neutral", "Buy", "Strong Buy"]
quadrant_colors = ["#f25829", "#f2a529", "#eff229", "#85e043", "#2bad4e"]
n_quadrants = len(quadrant_colors)
min_value = 0
max_value = 100

# Calculate hand angle for the gauge
hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))

# Create the gauge figure
fig = go.Figure(
    data=[
        go.Pie(
            values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),
            rotation=90,
            hole=0.5,
            marker_colors=["#fff"] + quadrant_colors,
            text=quadrant_text,
            textinfo="text",
            hoverinfo="skip",
            showlegend=False
        ),
    ],
    layout=go.Layout(
        showlegend=False,
        margin=dict(b=0, t=0, l=0, r=0),
        width=300,
        height=150,
        paper_bgcolor="white",
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
                x0=0.5, x1=0.5 + 0.4 * np.cos(hand_angle),
                y0=0.5, y1=0.5 + 0.4 * np.sin(hand_angle),
                line=dict(color="#333", width=4)
            )
        ]
    )
)

# Display gauge and indicator
st.markdown('<div class="gauge-container">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown(f'<div class="indicator">{sentiment}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Timeframe options (improved with hover effect)
st.markdown('<div class="timeframe-options">', unsafe_allow_html=True)
timeframe_options = ["يومي", "اسبوعي", "شهري"]
for option in timeframe_options:
    if st.button(option):
        st.markdown(f'<div class="timeframe-option selected">{option}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="timeframe-option">{option}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Explore link
st.markdown('<div class="explore"><a href="https://sa.investing.com/commodities/gold-technical" target="_blank">استكشف</a></div>', unsafe_allow_html=True)

# Adding some CSS for styling
st.markdown("""
<style>
    .gauge-container {
        width: 300px;
        margin: auto;
        text-align: center;
    }
    .gauge-title {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .indicator {
        margin-top: -20px;
        font-size: 20px;
        font-weight: bold;
        color: #181C21;
    }
    .timeframe-options {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .timeframe-options div {
        padding: 10px;
        cursor: pointer;
        color: #232526;
        font-weight: bold;
    }
    .timeframe-options div:hover {
        color: #1256A0;
        text-decoration: underline;
    }
    .timeframe-options .selected {
        color: #1256A0;
        text-decoration: underline;
    }
    .explore {
        margin-top: 20px;
        color: #1256A0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)
