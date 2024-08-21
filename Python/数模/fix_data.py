import pandas as pd
from datetime import datetime, timedelta

""" 使用前5/6日的平均值对黄金价格的缺失进行修复 """

# 读取CSV文件
df = pd.read_csv('Python/数模/data/LBMA-GOLD.csv', parse_dates=['Date'], dayfirst=False)

# 设置日期列为索引
df.set_index('Date', inplace=True)

# 获取所有日期范围，包括缺失的周末
full_date_range = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')

# 重新索引数据框，缺失日期将被NaN填充
df = df.reindex(full_date_range)

# 填补周末缺失的价格
for i in range(len(df)):
    if pd.isna(df.iloc[i]['USD (PM)']):
        # 检查是否是周末
        if df.index[i].weekday() in [5, 6]:  # 5是周六，6是周日
            # 计算前五天的平均值
            start_idx = max(0, i - 5)
            end_idx = i
            df.iloc[i]['USD (PM)'] = round(df.iloc[start_idx:end_idx]['USD (PM)'].mean(),2)

# 重置索引，并保存新的CSV文件
df.reset_index(inplace=True)
df.columns = ['Date', 'USD (PM)']
df.to_csv('Python/数模/data/new.csv', index=False)
