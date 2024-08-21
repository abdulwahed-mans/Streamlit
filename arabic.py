import streamlit as st

# تحميل الخط
st.markdown('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Droid+Arabic+Kufi&display=swap">', unsafe_allow_html=True)

# تعريف أنماط CSS بشكل مركزي
st.markdown("""
<style>
body {
    font-family: 'Droid Arabic Kufi', sans-serif;
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

# Your app code here
st.title('مثال على استخدام خط درويد')
st.write('يجب أن يستخدم هذا النص خط Droid Arabic Kufi.')

# ... باقي الكود

# مثال على استخدام الأنماط بشكل أكثر كفاءة
st.write("هذا النص يستخدم الخط الافتراضي للجسم", style={'font-family': 'inherit'})
st.write("هذا النص يستخدم خط مختلف عن الافتراضي", style={'font-family': 'sans-serif'})