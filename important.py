import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# تحميل البيانات (افتراضًا أن البيانات في ملف CSV)
df = pd.read_csv('gold_prices.csv', index_col='Date', parse_dates=True)

# تحديد الفترة الزمنية
start_date = '2020-08-21'
end_date = '2020-08-22'

# رسم المخطط
mpf.plot(df[start_date:end_date], type='candle', style='yahoo', volume=True, 
         title='Gold Price', ylabel='Price', xlabel='Date')