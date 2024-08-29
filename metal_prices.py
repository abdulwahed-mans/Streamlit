import streamlit as st
import requests

# Streamlit app title
st.title("Live Metal Prices")

# API details
url = "https://live-metal-prices.p.rapidapi.com/v1/latest/XAU,XAG,PA,PL,GBP,EUR/EUR"

headers = {
	"x-rapidapi-key": "38a0e16be7msh19903c78b8d710fp1fb6f9jsnd2cc4efd5140",
	"x-rapidapi-host": "live-metal-prices.p.rapidapi.com"
}

# Fetch the data
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Display the raw JSON data
    st.subheader("Raw JSON Response")
    st.json(data)
    
    # Extract and display metal prices
    st.subheader("Metal Prices (in EUR)")
    if 'prices' in data:
        for metal, details in data['prices'].items():
            st.write(f"**{metal}**: {details['price']} EUR")
    else:
        st.warning("No metal prices found in the response.")
else:
    st.error(f"Failed to retrieve data. Status code: {response.status_code}")
