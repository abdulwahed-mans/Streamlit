import streamlit as st
import plotly.graph_objects as go
import random
import time

# Function to create a more aesthetically pleasing gauge
def create_gauge(value, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title, 'font': {'size': 24}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "black", 'thickness': 0.2},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': '#A3E4D7'},  # Light Green
                {'range': [50, 75], 'color': '#F9E79F'},  # Light Yellow
                {'range': [75, 100], 'color': '#F1948A'}  # Light Red
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90},
        }
    ))

    fig.update_layout(
        font={'color': "darkblue", 'family': "Arial"},
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="white",
    )

    return fig

# Streamlit app layout
st.title("Enhanced Digital-Analog Gauge Meter")
st.subheader("Dynamic Data Simulation")

placeholder = st.empty()

# Simulate dynamic data update
while True:
    value = random.randint(0, 100)
    
    with placeholder.container():
        gauge_fig = create_gauge(value, "Speedometer")
        st.plotly_chart(gauge_fig)
    
    time.sleep(1)  # Update every second
