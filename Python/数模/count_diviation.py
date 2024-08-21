import pandas as pd
from predict import predict_price

""" 计算预测值的评价偏差量 """

# 读取CSV文件
df1 = pd.read_csv('Python/数模/data/LBMA-GOLD.csv', parse_dates=['Date'], dayfirst=False)
df2 = pd.read_csv('Python/数模/data/BCHAIN-MKPRU.csv', parse_dates=['Date'], dayfirst=False)

# 设置日期列为索引
df1.set_index('Date', inplace=True)
df2.set_index('Date', inplace=True)

# 获取所有日期范围，包括缺失的周末
full_date_range = pd.date_range(start=df2.index.min(), end=df2.index.max(), freq='D')

# 重新索引数据框，缺失日期将被NaN填充
df1 = df1.reindex(full_date_range)

# 计算偏差率
deviations_g = []
deviations_b = []
a=1
for date in df2.index:
    print(a)
    a+=1
    real_value2 = df2.loc[date, 'Value']
    predict_value2 = predict_price(date.strftime('%m/%d/%y'), csv_file='Python/数模/data/BCHAIN-MKPRU.csv')
    deviations_b.append((real_value2 - predict_value2) / real_value2)
    
    if pd.isna(df1.loc[date, 'USD (PM)']):
        continue
    
    real_value1 = df1.loc[date, 'USD (PM)']
    predict_value1 = predict_price(date.strftime('%m/%d/%y'))
    deviations_g.append((real_value1 - predict_value1) / real_value1)

# 计算平均偏差率
average_deviation_g = sum(deviations_g) / len(deviations_g) if deviations_g else 0
average_deviation_b = sum(deviations_b) / len(deviations_b) if deviations_b else 0

print(f"Gold Deviation: {average_deviation_g}")
print(f"Bitcoin Deviation: {average_deviation_b}")
