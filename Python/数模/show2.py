from get_rsi import *
import matplotlib.pyplot as plt

""" 黄金/比特币的走势和对应RSI值的对比图 """

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

rsi_data1={
    'Date':[],
    'Value':[]
}

rsi_data2={
    'Date':[],
    'Value':[]
}

for i in range(16,len(df1)):
    print(i)
    rsi_data1['Date'].append(df1.index[i].strftime('%m/%d/%y'))
    rsi_data2['Date'].append(df2.index[i].strftime('%m/%d/%y'))
    rsi_data1['Value'].append(get_rsi(df1.index[i].strftime('%m/%d/%y')))
    rsi_data2['Value'].append(get_rsi(df2.index[i].strftime('%m/%d/%y'),1))

rdf1=pd.DataFrame(rsi_data1)
rdf1['Date']=pd.to_datetime(rdf1['Date'])
rdf1.set_index('Date', inplace=True)

rdf2=pd.DataFrame(rsi_data2)
rdf2['Date']=pd.to_datetime(rdf2['Date'])
rdf2.set_index('Date', inplace=True)

# 绘制折线图
fig, ax = plt.subplots(2, 2, figsize=(16, 16))  # 创建2行2列的子图

#绘制第一个子图
ax[0,0].plot(df1.index, df1['USD (PM)'], marker='o', linestyle='-', color='b', label='Real Gold', markersize=1)
ax[0,0].set_xlabel('Date')
ax[0,0].set_ylabel('Value')
ax[0,0].set_title('Gold')
ax[0,0].legend()
ax[0,0].grid(True)

#绘制第二个子图
ax[0,1].plot(df2.index, df2['Value'], marker='o', linestyle='-', color='b', label='Real Bitcoin', markersize=1)
ax[0,1].set_xlabel('Date')
ax[0,1].set_ylabel('Value')
ax[0,1].set_title('Bitcoin')
ax[0,1].legend()
ax[0,1].grid(True)

#绘制第三个子图
ax[1,0].plot(rdf1.index, rdf1['Value'], marker='o', linestyle='-', color='g', label='Gold RSI', markersize=1)
ax[1,0].set_xlabel('Date')
ax[1,0].set_ylabel('Value')
ax[1,0].set_title('Gold RSI')
ax[1,0].legend()
ax[1,0].grid(True)

#绘制第四个子图
ax[1,1].plot(rdf2.index, rdf2['Value'], marker='o', linestyle='-', color='y', label='Bitcon RSI', markersize=1)
ax[1,1].set_xlabel('Date')
ax[1,1].set_ylabel('Value')
ax[1,1].set_title('Bitcon RSI')
ax[1,1].legend()
ax[1,1].grid(True)

# 调整子图之间的间距
plt.tight_layout()
plt.subplots_adjust(hspace=0.3,top=0.9,bottom=0.1)  # 增大上下图之间的间距

# 显示图表
plt.show()