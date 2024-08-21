import streamlit as st
import pandas as pd

# Sample data extracted from the PDF
data = [
    {"Name": "Shadi Abo Shabab", "ID": "1412622987", "Bus": 1},
    {"Name": "Iman Saad", "ID": "2802198788", "Bus": 1},
    {"Name": "Aya Saad", "ID": "3804511939", "Bus": 1},
    {"Name": "Mohammad Abu Barkah", "ID": "4405805276", "Bus": 1},
    {"Name": "Samiha Abu Barkah", "ID": "5974334526", "Bus": 1},
    {"Name": "Ghada Qishta", "ID": "6800379414", "Bus": 1},
    # Add more entries as needed...
    {"Name": "Ahmed Zidan", "ID": "1101954848", "Bus": 3},
    {"Name": "Sara Ayman", "ID": "1101954849", "Bus": 3},
    {"Name": "Khaled Mahmoud", "ID": "1101954850", "Bus": 3},
    {"Name": "Layla Tamer", "ID": "1101954851", "Bus": 2},
]

df = pd.DataFrame(data)

# Streamlit app
st.title('Passenger List for Rafah Crossing')

# Filter by bus number
bus_number = st.selectbox('Select Bus Number:', options=sorted(df['Bus'].unique()))

# Filter the data based on the selected bus
filtered_df = df[df['Bus'] == bus_number]

# Search by name or ID
search_term = st.text_input('Search by Name or ID:')

# Apply search filter
if search_term:
    filtered_df = filtered_df[
        filtered_df['Name'].str.contains(search_term, case=False) | 
        filtered_df['ID'].str.contains(search_term)
    ]

# Display the filtered data
st.write(f"Showing results for Bus {bus_number}:")
st.table(filtered_df)
