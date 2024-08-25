import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# تحميل البيانات
df = pd.read_csv('gold_prices.csv')

# عرض أول 5 صفوف
print(df.head())

# رسم سعر الإغلاق
plt.plot(df['Close'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Gold Price')
plt.show()