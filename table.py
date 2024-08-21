import streamlit as st
import pandas as pd

# Load a sample dataset
@st.cache
def load_data():
    data = pd.DataFrame({
        'Name': ['John', 'Alice', 'Bob', 'Jane', 'Charlie'],
        'Age': [23, 35, 45, 25, 33],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Job': ['Engineer', 'Doctor', 'Artist', 'Teacher', 'Lawyer']
    })
    return data

data = load_data()

# Display the dataset in a table
st.title('Sample Data Table with Filters')
st.write('Below is a table of sample data. Use the filters to refine the data displayed.')

# Add filters
name_filter = st.multiselect('Filter by Name', options=data['Name'].unique(), default=data['Name'].unique())
city_filter = st.multiselect('Filter by City', options=data['City'].unique(), default=data['City'].unique())
job_filter = st.multiselect('Filter by Job', options=data['Job'].unique(), default=data['Job'].unique())

# Apply filters to the dataset
filtered_data = data[(data['Name'].isin(name_filter)) & (data['City'].isin(city_filter)) & (data['Job'].isin(job_filter))]

# Display filtered data
st.write('Filtered Data:')
st.table(filtered_data)
