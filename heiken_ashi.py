import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# إنشاء DataFrame مع قيم بسيطة ومباشرة
data = {
    'Day': [1, 2, 3, 4, 5],
    'Open': [100, 105, 102, 110, 115],
    'High': [110, 112, 108, 115, 120],
    'Low': [95, 100, 98, 105, 110],
    'Close': [105, 107, 103, 113, 118]
}
df = pd.DataFrame(data)

# حساب قيم Heiken-Ashi باستخدام الأرقام الصحيحة
df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
df['HA_Open'] = np.zeros(len(df))
df['HA_Open'][0] = df['Open'][0]

for i in range(1, len(df)):
    df['HA_Open'][i] = (df['HA_Open'][i-1] + df['HA_Close'][i-1]) / 2

df['HA_High'] = df[['High', 'HA_Open', 'HA_Close']].max(axis=1)
df['HA_Low'] = df[['Low', 'HA_Open', 'HA_Close']].min(axis=1)

# إعداد تطبيق Streamlit
st.title('Heiken-Ashi vs Traditional Close')

# رسم البيانات
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Day'], df['Close'], marker='o', label='Traditional Close', linestyle='--')
ax.plot(df['Day'], df['HA_Close'], marker='o', label='Heiken-Ashi Close', color='blue')
ax.fill_between(df['Day'], df['HA_Low'], df['HA_High'], color='lightblue', alpha=0.3)

ax.set_xlabel('Day')
ax.set_ylabel('Price')
ax.set_title('Heiken-Ashi vs Traditional Close')
ax.legend()
ax.grid(True)

# عرض الرسم البياني في Streamlit
st.pyplot(fig)
