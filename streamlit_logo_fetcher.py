import streamlit as st
import http.client
import json

# Define the Streamlit app
st.title("Yahoo Finance Historical Data Fetcher")

# Input for the stock symbol
stock_symbol = st.text_input("Enter Stock Symbol", "TSLA")
period = st.selectbox("Select Period", ["1d", "5d", "1mo", "6mo", "1y", "5y", "10y", "ytd", "max"])

if st.button("Get Historical Data"):
    conn = http.client.HTTPSConnection("yahoo-finance160.p.rapidapi.com")
    
    payload = json.dumps({"stock": stock_symbol, "period": period})
    
    headers = {
        'x-rapidapi-key': "38a0e16be7msh19903c78b8d710fp1fb6f9jsnd2cc4efd5140",
        'x-rapidapi-host': "yahoo-finance160.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    
    conn.request("POST", "/history", payload, headers)
    
    res = conn.getresponse()
    data = res.read()
    
    # Decode the byte response to a string
    decoded_data = data.decode("utf-8")
    
    # Try to parse the JSON data
    try:
        json_data = json.loads(decoded_data)
        
        if "message" in json_data and json_data["message"] == "You are not subscribed to this API.":
            st.error("Error: You are not subscribed to this API. Please check your subscription plan.")
        else:
            st.subheader("Raw JSON Response")
            st.json(json_data)
            
            # Display the historical data in a more readable format
            if "prices" in json_data:
                st.subheader(f"Historical Data for {stock_symbol} ({period})")
                for entry in json_data["prices"]:
                    st.write(entry)
            else:
                st.warning("Historical data not found in the response.")
    except json.JSONDecodeError:
        st.error("Failed to decode JSON from the response.")
