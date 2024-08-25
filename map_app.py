import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

# تحميل البيانات
gdf = gpd.read_file('se-all.geo.json')

# عنوان التطبيق
st.title("خريطة تفاعلية لسويد")

# اختيار العمود
column = st.selectbox("اختر عمودًا لعرضه:", gdf.columns)

# رسم الخريطة
fig, ax = plt.subplots()
gdf.plot(column=column, legend=True, ax=ax)
st.pyplot(fig)