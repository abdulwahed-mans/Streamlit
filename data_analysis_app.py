import streamlit as st
import pandas as pd

# Inject Tailwind CSS via CDN
st.markdown('''
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
    /* Custom CSS for container width */
    .main {
        max-width: 1140px;
        margin-left: auto;
        margin-right: auto;
        padding: 1rem;
    }
    </style>
''', unsafe_allow_html=True)

# Title of the app
st.markdown('''
<div class="bg-blue-600 text-white p-6 rounded-lg shadow-lg">
    <h1 class="text-3xl font-bold">Data Analysis Form</h1>
    <p class="mt-2">Upload your dataset and filter the results by city or department.</p>
</div>
''', unsafe_allow_html=True)

# Form for file upload and filtering
with st.form(key='data_form'):
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    city_filter = st.selectbox("Filter by City", options=["All"])
    department_filter = st.selectbox("Filter by Department", options=["All"])
    
    submit_button = st.form_submit_button(label='Submit')

# Process the uploaded file
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Populate filters based on the file's content
    if "City" in df.columns and "Department" in df.columns:
        city_filter = st.selectbox("Filter by City", options=["All"] + df['City'].unique().tolist())
        department_filter = st.selectbox("Filter by Department", options=["All"] + df['Department'].unique().tolist())
    
        # Apply filters
        if city_filter != "All":
            df = df[df['City'] == city_filter]
        
        if department_filter != "All":
            df = df[df['Department'] == department_filter]
        
        # Display filtered data
        st.markdown('''
        <div class="bg-gray-100 p-4 rounded-lg shadow">
            <h2 class="text-2xl font-semibold">Filtered Data</h2>
        </div>
        ''', unsafe_allow_html=True)
        
        st.dataframe(df)
    else:
        st.warning("The uploaded file does not contain the required 'City' or 'Department' columns.")
else:
    st.info("Please upload a CSV file to proceed.")

# Display additional information or statistics
if uploaded_file is not None:
    st.markdown('''
    <div class="mt-4 p-4 bg-green-100 rounded-lg">
        <h3 class="text-xl font-semibold">Data Summary</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    st.write(df.describe())
