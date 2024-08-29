import streamlit as st
import plotly.graph_objects as go
import time
import random

# Function to create a gauge meter
def create_gauge(value, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 100], 'color': "gray"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90}}))

    return fig

# Streamlit app layout
st.title("Digital-Analog Gauge Meter")
st.subheader("Dynamic Data Simulation")

placeholder = st.empty()

# Simulate dynamic data update
while True:
    value = random.randint(0, 100)
    
    with placeholder.container():
        gauge_fig = create_gauge(value, "Speedometer")
        st.plotly_chart(gauge_fig)
    
    time.sleep(1)  # Update every second
