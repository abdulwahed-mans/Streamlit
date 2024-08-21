import streamlit as st
import pandas as pd

# Sample data extracted from the PDF (with additional fields)
data = [
    {"Passenger Number": 1, "Name": "Shadi Abo Shabab", "ID": "1412622987", "Bus": 1, "Travel Date": "2023-08-21"},
    {"Passenger Number": 2, "Name": "Iman Saad", "ID": "2802198788", "Bus": 1, "Travel Date": "2023-08-21"},
    {"Passenger Number": 3, "Name": "Aya Saad", "ID": "3804511939", "Bus": 1, "Travel Date": "2023-08-21"},
    {"Passenger Number": 4, "Name": "Mohammad Abu Barkah", "ID": "4405805276", "Bus": 1, "Travel Date": "2023-08-22"},
    {"Passenger Number": 5, "Name": "Samiha Abu Barkah", "ID": "5974334526", "Bus": 1, "Travel Date": "2023-08-22"},
    {"Passenger Number": 6, "Name": "Ghada Qishta", "ID": "6800379414", "Bus": 1, "Travel Date": "2023-08-23"},
    {"Passenger Number": 7, "Name": "Ahmed Zidan", "ID": "1101954848", "Bus": 3, "Travel Date": "2023-08-23"},
    {"Passenger Number": 8, "Name": "Sara Ayman", "ID": "1101954849", "Bus": 3, "Travel Date": "2023-08-23"},
    {"Passenger Number": 9, "Name": "Khaled Mahmoud", "ID": "1101954850", "Bus": 3, "Travel Date": "2023-08-24"},
    {"Passenger Number": 10, "Name": "Layla Tamer", "ID": "1101954851", "Bus": 2, "Travel Date": "2023-08-24"},
]

df = pd.DataFrame(data)

# Convert the 'Travel Date' to datetime for better filtering
df['Travel Date'] = pd.to_datetime(df['Travel Date'])

# Format the 'Travel Date' to display as "Day-Month-Year" (e.g., "21-Aug-2023")
df['Travel Date'] = df['Travel Date'].dt.strftime('%d-%b-%Y')  # Short month name

# Streamlit app
st.title('Passenger List for Rafah Crossing')

# Filter by travel date
date_filter = st.date_input('Select Travel Date:', value=None, min_value=pd.to_datetime(df['Travel Date']).min(), max_value=pd.to_datetime(df['Travel Date']).max())

# Initialize the variable
formatted_date_filter = "All Dates"

# Filter the data based on the selected date
if date_filter:
    formatted_date_filter = date_filter.strftime('%d-%b-%Y')
    filtered_df = df[df['Travel Date'] == formatted_date_filter]
else:
    filtered_df = df.copy()

# Filter by bus number
bus_number = st.selectbox('Select Bus Number:', options=sorted(filtered_df['Bus'].unique()))

# Apply the bus filter
filtered_df = filtered_df[filtered_df['Bus'] == bus_number]

# Search by family name or ID
search_term = st.text_input('Search by Family Name or ID:')

# Apply search filter
if search_term:
    filtered_df = filtered_df[
        filtered_df['Name'].str.contains(search_term, case=False) | 
        filtered_df['ID'].str.contains(search_term)
    ]

# Display the filtered data
st.write(f"Showing results for Bus {bus_number} on {formatted_date_filter}:")
st.table(filtered_df[['Passenger Number', 'Name', 'ID', 'Bus', 'Travel Date']])
