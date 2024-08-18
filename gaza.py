import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MousePosition

# Insert custom CSS for font styling in Streamlit
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
    }
    
    .stTextInput, .stButton, .stMarkdown {
        font-size: 16px;
        color: #333333;
        font-weight: 400;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# Sample data for Gaza (replace this with actual data loading)
data = pd.DataFrame({
    'latitude': [31.5285, 31.4989, 31.3547, 31.4450],
    'longitude': [34.4540, 34.4732, 34.3078, 34.4204],
    'category': ['food', 'medical', 'water', 'shelter'],
    'need_level': [4, 5, 3, 2]  # Need level from 1 to 5
})

# Sample GeoJSON data for Gaza regions (replace this with actual GeoJSON data)
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "North Gaza", "category": "water"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [34.500, 31.550],
                    [34.500, 31.600],
                    [34.400, 31.600],
                    [34.400, 31.550],
                    [34.500, 31.550]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": {"name": "Gaza City", "category": "food"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [34.450, 31.500],
                    [34.450, 31.550],
                    [34.350, 31.550],
                    [34.350, 31.500],
                    [34.450, 31.500]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": {"name": "Khan Younis", "category": "medical"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                [
                    34.365892942760894,
                    31.414919143086408
                ],
                [
                    34.36406834947363,
                    31.416194039088367
                ],
                [
                    34.36227796731163,
                    31.416456801759225
                ],
                [
                    34.35897089197911,
                    31.41748838142577
                ],
                [
                    34.35601733159618,
                    31.417556504212044
                ],
                [
                    34.355105034952516,
                    31.417361867548763
                ],
                [
                    34.35261902660025,
                    31.41721588978649
                ],
                [
                    34.35160409658431,
                    31.416914201690616
                ],
                [
                    34.352607622891355,
                    31.414919143086408
                ],
                [
                    34.35454625325846,
                    31.413498246210295
                ],
                [
                    34.35752262105788,
                    31.411542044755592
                ],
                [
                    34.35925598468057,
                    31.410432539235885
                ],
                [
                    34.35994020716325,
                    31.409965375092327
                ],
                [
                    34.36591575017741,
                    31.41490941098904
                ]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": {"name": "Nusirat", "category": "shelter"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            34.361406805252415,
                            31.448532322131314
                        ],
                        [
                            34.35553341949969,
                            31.44274474564935
                        ],
                        [
                            34.363958778537835,
                            31.43849956627112
                        ],
                        [
                            34.36894730923166,
                            31.445075136071964
                        ],
                        [
                            34.364869281568474,
                            31.446552114078287
                        ],
                        [
                            34.36363817887843,
                            31.446978792279594
                        ],
                        [
                            34.36139398126514,
                            31.448543262391226
                        ]
                        ]
                ]
            }
        }
    ]
}

# App title
st.title('Humanitarian Needs in Gaza')

# Sidebar filters
st.sidebar.header("Filter by:")
category_filter = st.sidebar.multiselect(
    "Select need category:",
    options=data['category'].unique(),
    default=data['category'].unique()
)

# Need level filter
need_level_filter = st.sidebar.slider(
    "Select need level range:",
    min_value=int(data['need_level'].min()),
    max_value=int(data['need_level'].max()),
    value=(int(data['need_level'].min()), int(data['need_level'].max()))
)

# Add new assistance point
st.sidebar.header("Add Assistance Point:")
new_latitude = st.sidebar.number_input("Latitude:", value=31.5)
new_longitude = st.sidebar.number_input("Longitude:", value=34.45)
new_category = st.sidebar.selectbox("Assistance Type:", options=['food', 'medical', 'water', 'shelter'])
new_need_level = st.sidebar.slider("Need Level:", min_value=1, max_value=5, value=3)

# Button to add new point
if st.sidebar.button("Add Point"):
    new_point = {'latitude': new_latitude, 'longitude': new_longitude, 'category': new_category, 'need_level': new_need_level}
    data = data.append(new_point, ignore_index=True)
    st.sidebar.success("New assistance point added successfully!")

# Filter data based on user selection
filtered_data = data[
    (data['category'].isin(category_filter)) &
    (data['need_level'].between(need_level_filter[0], need_level_filter[1]))
]

# Create the map centered on Gaza
m = folium.Map(
    location=[31.5, 34.45],  # Center the map on Gaza
    zoom_start=11
)

# Add GeoJSON regions to the map
def style_function(feature):
    category = feature['properties']['category']
    return {
        'fillColor': 'blue' if category == 'water' else 'green' if category == 'food' else 'red' if category == 'medical' else 'orange',
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5',
        'fillOpacity': 0.5,
    }

folium.GeoJson(
    geojson_data,
    name="geojson",
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['name', 'category'])
).add_to(m)

# Add points to the map
for _, row in filtered_data.iterrows():
    folium.CircleMarker(
        location=(row['latitude'], row['longitude']),
        radius=row['need_level'] * 2,
        color='blue' if row['category'] == 'water' else 'green' if row['category'] == 'food' else 'red' if row['category'] == 'medical' else 'orange',
        fill=True,
        fill_opacity=0.6,
        popup=folium.Popup(f"{row['category'].capitalize()} - Need Level: {row['need_level']}", parse_html=True),
        tooltip=f"Need: {row['category'].capitalize()} (Level {row['need_level']})"
    ).add_to(m)

# Add Mouse Position plugin to display coordinates
MousePosition().add_to(m)

# Display the map in Streamlit
folium_static(m)
