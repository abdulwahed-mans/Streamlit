import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('gold_trading_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit app
st.title('Gold Price Prediction')

st.write("""
This app predicts whether the gold price will go up or down tomorrow based on today's price and a 7-day moving average.
""")

# Input data
prev_close = st.number_input('Previous Close Price', min_value=0.0, format="%.2f")
ma7 = st.number_input('7-Day Moving Average', min_value=0.0, format="%.2f")

# Prediction
if st.button('Predict'):
    input_data = np.array([[prev_close, ma7]])
    
    # Checking for missing values and handling them
    if np.isnan(input_data).any():
        st.error("Please enter valid numerical values for both fields.")
    else:
        input_data = scaler.transform(input_data)
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success('The model predicts that the gold price will go UP tomorrow.')
        else:
            st.error('The model predicts that the gold price will go DOWN tomorrow.')

# Option to view the data
if st.checkbox("Show example data"):
    st.write("""
    Here is a sample of the data used for training the model.
    """)
    example_data = pd.DataFrame({
        'Prev_Close': [109.80, 109.70, 111.51, 110.82, 111.37],
        'MA7': [109.70, 110.14, 110.91, 111.00, 111.18],
        'Target': [1, 1, 0, 1, 0]
    })
    st.dataframe(example_data)

# Run the app: streamlit run streamlit_app.py
