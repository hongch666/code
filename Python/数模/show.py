from predict import *
import matplotlib.pyplot as plt

""" 展示实际金额与预测金额的对比图 """

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

data1=[]
value1=[]
predict_data1={
    'Date':[],
    'USD (PM)':[]
}

data2=[]
value2=[]
predict_data2={
    'Date':[],
    'Value':[]
}

for i in range(16,len(df1)):
    print(i)
    predict_data1['Date'].append(df1.index[i].strftime('%m/%d/%y'))
    predict_data1['USD (PM)'].append(predict_price(df1.index[i-1].strftime('%m/%d/%y')))
    predict_data2['Date'].append(df2.index[i].strftime('%m/%d/%y'))
    predict_data2['Value'].append(predict_price(df2.index[i-1].strftime('%m/%d/%y'),'Python/数模/data/BCHAIN-MKPRU.csv'))

pdf1=pd.DataFrame(predict_data1)
pdf1['Date'] = pd.to_datetime(pdf1['Date'])
pdf1.set_index('Date', inplace=True)

pdf2=pd.DataFrame(predict_data2)
pdf2['Date'] = pd.to_datetime(pdf2['Date'])
pdf2.set_index('Date', inplace=True)

# 绘制折线图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))  # 创建1行2列的子图

#绘制第一个子图
ax1.plot(df1.index, df1['USD (PM)'], marker='o', linestyle='-', color='b', label='Real Gold', markersize=1)
ax1.plot(pdf1.index, pdf1['USD (PM)'], marker='o', linestyle='-', color='r', label='Predict Gold', markersize=1)
ax1.set_xlabel('Date')
ax1.set_ylabel('Value')
ax1.set_title('Gold')
ax1.legend()
ax1.grid(True)

#绘制第二个子图
ax2.plot(df2.index, df2['Value'], marker='o', linestyle='-', color='b', label='Real Bitcoin', markersize=1)
ax2.plot(pdf2.index, pdf2['Value'], marker='o', linestyle='-', color='r', label='Predict Bitcoin', markersize=1)
ax2.set_xlabel('Date')
ax2.set_ylabel('Value')
ax2.set_title('Bitcoin')
ax2.legend()
ax2.grid(True)

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()