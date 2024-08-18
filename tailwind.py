import streamlit as st

# Inject Tailwind CSS via CDN
st.markdown('''
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
''', unsafe_allow_html=True)

# Inject custom CSS for page width
st.markdown("""
    <style>
    /* Set the max-width for the main content area */
    .main {
        max-width: 1140px;
        margin-left: auto;
        margin-right: auto;
        padding: 1rem; /* Add some padding */
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app content using Tailwind CSS classes
st.markdown('''
<div class="bg-blue-500 text-white p-4 rounded-lg shadow-lg">
    <h1 class="text-4xl font-bold">Hello, Streamlit with Tailwind CSS and Bootstrap-like Container!</h1>
    <p class="text-lg mt-4">This layout has a max-width similar to Bootstrap's container.</p>
</div>

<div class="mt-6">
    <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
        Click me
    </button>
</div>
''', unsafe_allow_html=True)

# Streamlit content
st.write("This section is styled using Tailwind CSS!")
