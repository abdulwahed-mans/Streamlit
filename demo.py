import folium
import geopandas as gpd
import shapely
import streamlit as st
from streamlit_folium import st_folium

# عنوان التطبيق
st.title("GeoJSON Styling with Folium and Streamlit")

# تحديد الموقع الافتراضي وزوم الخريطة
START_LOCATION = [37.7934347109497, -122.399077892527]
START_ZOOM = 18

# WKT يمثل المتعدد الأضلاع (Polygon)
wkt = (
    "POLYGON ((-122.399077892527 37.7934347109497, -122.398922660838 "
    "37.7934544916178, -122.398980265018 37.7937266504805, -122.399133972495 "
    "37.7937070646238, -122.399077892527 37.7934347109497))"
)

# تحميل المتعدد الأضلاع من WKT وإنشاء GeoDataFrame
polygon = shapely.wkt.loads(wkt)
gdf = gpd.GeoDataFrame(geometry=[polygon], crs="EPSG:4326")

# تخصيص النمط (style) للمتعدد الأضلاع
style_parcels = {"fillColor": "red", "fillOpacity": 0.2, "color": "blue", "weight": 2}

# إنشاء GeoJson من GeoDataFrame مع النمط المحدد
polygon_folium = folium.GeoJson(
    data=gdf, 
    style_function=lambda x: style_parcels,
)

# إنشاء خريطة Folium وتحديد الموقع الافتراضي والزوم
map = folium.Map(
    location=START_LOCATION, 
    zoom_start=START_ZOOM, 
    tiles="OpenStreetMap", 
    max_zoom=21
)

# إضافة المتعدد الأضلاع إلى مجموعة الميزات (FeatureGroup)
fg = folium.FeatureGroup(name="Parcels").add_child(polygon_folium)

# إضافة المجموعة إلى الخريطة
map.add_child(fg)

# عرض الخريطة باستخدام Streamlit
st_folium(
    map,
    width=800,
    height=450,
    feature_group_to_add=fg,
    debug=True,
)

# إضافة خيار للتحكم بالطبقات في الخريطة
folium.LayerControl().add_to(map)
