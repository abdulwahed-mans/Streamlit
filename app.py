import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Simple Streamlit App')

# Slider widget
number = st.slider('Pick a number', 0, 100)

# Display the selected number
st.write(f'You selected: {number}')

# Generate some data
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

# Display the dataframe
st.write(data)

# Plot a chart
st.line_chart(data)
