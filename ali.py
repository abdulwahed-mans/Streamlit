import streamlit as st
import pandas as pd

# Sample data (replace with Mansour's actual data)
data = {
    'Monday': ['Swedish', 'Math', 'Slöjd', 'Lunch', 'Natural Sciences', 'Health and Physical Education'],
    'Tuesday': ['Swedish', 'FTH', 'Math', 'Svenska', 'Lunch', 'Health and Physical Education', 'Social Studies'],
    # ... rest of the days
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Create Streamlit app
st.title("Mansour's Weekly Schedule")

# Display the DataFrame as a table
st.table(df)

# Optionally, create a calendar view using a library like plotly_calendar
# import plotly.graph_objects as go
# fig = go.Figure(data=go.Calendar(
#     # ... configure calendar data
# ))
# st.plotly_chart(fig)