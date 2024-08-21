import streamlit as st

# Inject Tailwind CSS via CDN
st.markdown('''
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
''', unsafe_allow_html=True)

# Inject custom CSS for page width adjustment and RTL text direction
st.markdown("""
    <style>
    /* Set the max-width for the main content area */
    .main {
        max-width: 1140px;
        margin-left: auto;
        margin-right: auto;
        padding: 1rem; /* Add some padding */
    }

    body {
        direction: rtl; /* تغيير اتجاه النص إلى اليمين */
        text-align: right; /* محاذاة النص إلى اليمين */
        font-family: 'sans'; /* استخدام الخط الافتراضي sans من Tailwind */
    }

    .stTextInput, .stTextArea, .stButton, .stHeader, .stMarkdown {
        font-family: 'sans'; /* استخدام نفس الخط الافتراضي sans من Tailwind */
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app content using Tailwind CSS classes
st.markdown('''
<div class="bg-blue-500 text-white p-4 rounded-lg shadow-lg">
    <h1 class="text-4xl font-bold">مرحبًا بكم في Streamlit مع Tailwind CSS!</h1>
    <p class="text-lg mt-4">هذا النص يعرض باستخدام الخط الافتراضي من Tailwind CSS ومحاذاة من اليمين إلى اليسار.</p>
</div>

<div class="mt-6">
    <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
        اضغط هنا
    </button>
</div>
''', unsafe_allow_html=True)

# Streamlit content
st.write("هذا القسم مصمم باستخدام Tailwind CSS!")

# Streamlit content using Tailwind CSS classes
st.markdown('''
<div class="mt-6">
    <h2 class="text-3xl font-bold">عنوان فرعي 1</h2>
    <p class="text-xl">هذا النص هو جزء من عنوان فرعي أول يستخدم Tailwind CSS لتنسيقه.</p>
</div>

<div class="mt-4">
    <h2 class="text-3xl font-bold">عنوان فرعي 2</h2>
    <p class="text-xl">يمكنك إضافة المزيد من المحتويات هنا، مع استخدام أسلوب Tailwind CSS.</p>
</div>
            
<div class="pt-8 text-base font-semibold leading-7">
    <p class="text-gray-900">هل تريد معرفة المزيد عن Tailwind؟</p>
    <p>
    <a href="https://tailwindcss.com/docs" class="text-sky-500 hover:text-sky-600">اقرأ الوثائق &rarr;</a>
    </p>
</div>
''', unsafe_allow_html=True)
