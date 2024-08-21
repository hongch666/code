import pandas as pd
from predict import *
from get_no_day import *
from get_max import *
from get_rsi import *
import matplotlib.pyplot as plt

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

everyday_c={
    'Date':[],
    'Value':[]
}

everyday_h={
    'Date':[],
    'Value':[]
}

everyday_b={
    'Date':[],
    'Value':[]
}

for i in range(len(df2)):
    everyday_c['Date'].append(df2.index[i].strftime('%m/%d/%y'))
    everyday_h['Date'].append(df2.index[i].strftime('%m/%d/%y'))
    everyday_b['Date'].append(df2.index[i].strftime('%m/%d/%y'))

def get_my_money(a=1,b=2,high_g=90,low_g=30,high_b=94,low_b=31,N=15):

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

    """
    参数说明
    h：今天黄金的价格
    bt：今天比特币的价格
    h1：预测出明天黄金的价格
    bt1：预测出明天比特币的价格
    c：今天持有的现金
    x1：昨天持有的黄金的数量
    y1：昨天持有的比特币的数量
    a：黄金交易的成本
    b ：比特币交易的成本
    rsi_gold：黄金的RSI值
    rsi_bt：比特币的RSI值
    """
    h=0
    bt=float(df2.iloc[0]['Value'])
    h1=0
    bt1=predict_price(df2.index[0].strftime('%m/%d/%y'), 'Python/数模/data/BCHAIN-MKPRU.csv')
    c=1000
    x1=0
    y1=0
    x=0
    y=0
    rsi_gold=0
    rsi_bt=0
    
    x_list=[]
    y_list=[]
    all_money=[]
    for i in range(len(df2)):
        print(i)
        everyday_c['Value'].append(c)
        everyday_h['Value'].append(x)
        everyday_b['Value'].append(y)
        if i>=N:
            rsi_gold=get_rsi(df1.index[i].strftime('%m/%d/%y'),0,N)
            rsi_bt=get_rsi(df2.index[i].strftime('%m/%d/%y'),1,N)
        else:
            rsi_gold=50
            rsi_bt=50
        if(i==len(df2)-1):
            break
        # print(df2.index[i])
        if not is_open(df2.index[i].strftime('%m/%d/%y')):
            bt1=predict_price(df2.index[i].strftime('%m/%d/%y'), 'Python/数模/data/BCHAIN-MKPRU.csv')
            bt=float(df2.iloc[i]['Value'])

            now_money=x*h+y*bt+c
            print("第"+str(i+1)+"天的资产："+str(now_money))
            all_money.append(now_money)
            if high_b<=rsi_bt<=100:
                y=0
                c=c-bt*(y-y1)-b/100*abs(y-y1)
                x_list.append(x1)
                y_list.append(y)
                y1=y
            elif 0<=rsi_bt<=low_b:
                y=(c+y*bt)//bt
                c=c-bt*(y-y1)-b/100*abs(y-y1)
                x_list.append(x1)
                y_list.append(y)
                y1=y
            else:
                """ result=solve_lp_no_gold(bt,bt1,c,x1,y1,b)
                y=result['y'] """
                y=y1
                c=c-bt*(y-y1)-b/100*abs(y-y1)
                x_list.append(x1)
                y_list.append(y)
                # y1=y
            
        else:
            h=float(df1.iloc[i]['USD (PM)'])
            bt=float(df2.iloc[i]['Value'])
            h1=predict_price(df1.index[i].strftime('%m/%d/%y'))
            bt1=predict_price(df2.index[i].strftime('%m/%d/%y'), 'Python/数模/data/BCHAIN-MKPRU.csv')
            
            now_money=x*h+y*bt+c
            print("第"+str(i+1)+"天的资产："+str(now_money))
            all_money.append(now_money)

            if high_g<=rsi_gold<=100 and high_b<=rsi_bt<=100:
                #全部卖出
                x=0
                y=0
                c=c-h*(x-x1)-bt*(y-y1)-a/100*abs(x-x1)-b/100*abs(y-y1)
                x_list.append(x)
                y_list.append(y)
                x1=x
                y1=y
            elif 0<=rsi_gold<=low_g and 0<=rsi_bt<=low_b:
                #全部买入，优先比特币，剩下的再买黄金
                y=(c+y*bt+x*h)//bt
                # c=c-bt*(y-y1)-b/100*abs(y-y1)
                x=(c+h*x1+bt*y1-bt*y)//h
                c=c-h*(x-x1)-bt*(y-y1)-a/100*abs(x-x1)-b/100*abs(y-y1)
                x_list.append(x)
                y_list.append(y)
                y1=y
                x1=x
            elif 0<=rsi_gold<=low_g  and high_b<=rsi_bt<=100:
                #卖出全部比特币，买入全部黄金
                y=0
                c=c-bt*(y-y1)-b/100*abs(y-y1)
                x=(c+x*h)//h
                c=c-h*(x-x1)-a/100*abs(x-x1)
                x_list.append(x)
                y_list.append(y)
                x1=x
                y1=y
            elif high_g<=rsi_gold<=100 and 0<=rsi_bt<=low_b:
                #卖出全部黄金，买入全部比特币
                x=0
                c=c-h*(x-x1)-a/100*abs(x-x1)
                y=(c+y*h)//h
                c=c-bt*(y-y1)-b/100*abs(y-y1)
                x_list.append(x)
                y_list.append(y)
                x1=x
                y1=y
            elif low_g<rsi_gold<high_g and low_b<rsi_bt<high_b:
                #使用预测模型
                """ result=solve_lp(h,bt,h1,bt1,c,x1,y1,a,b)
                x=result['x']
                y=result['y']
                c=c-h*(x-x1)-bt*(y-y1)-a/100*abs(x-x1)-b/100*abs(y-y1)
                x_list.append(x)
                y_list.append(y)
                x1=x
                y1=y """
                result=solve_lp_only_gold(h,h1,c,x1,y1,a)
                x=result['x']
                y=y1
                c=c-h*(x-x1)-bt*(y-y1)-a/100*abs(x-x1)-b/100*abs(y-y1)
                x_list.append(x)
                y_list.append(y)
                x1=x
                
            elif low_g<rsi_gold<high_g and 0<=rsi_bt<=low_b:
                #现金全部购入比特币，但剩下的钱不处理黄金
                y=(c+y*bt)//bt
                c=c-bt*(y-y1)-b/100*abs(y-y1)
                x=x1
                x_list.append(x)
                y_list.append(y)
                y1=y
            elif low_g<rsi_gold<high_g and high_b<=rsi_bt<=100:
                #全部卖出比特币，但剩下的钱不处理黄金
                y=0
                c=c-bt*(y-y1)-b/100*abs(y-y1)
                x=x1
                x_list.append(x)
                y_list.append(y)
                y1=y
            elif 0<=rsi_gold<=low_g and low_b<rsi_bt<high_b:
                #现金全部购入黄金，但剩下的钱不处理比特币
                x=(c+x*h)//h
                c=c-h*(x-x1)-a/100*abs(x-x1)
                y=y1
                x_list.append(x)
                y_list.append(y)
                x1=x
            elif low_g<=rsi_gold<high_g and low_b<rsi_bt<high_b:
                #全部卖出黄金，但剩下的钱不处理比特币
                x=0
                c=c-h*(x-x1)-a/100*abs(x-x1)
                y=y1
                x_list.append(x)
                y_list.append(y)
                x1=x
            
    money=x_list[len(x_list)-1]*df1.iloc[len(df1)-1]['USD (PM)']+y_list[len(y_list)-1]*df2.iloc[len(df2)-1]['Value']+c
    all_money.append(money)
    
    with open('Python/数模/money.txt', 'w', encoding='utf-8') as file:
        for item in all_money:
            file.write(str(item) + '\n')  # 写入每个元素并添加换行符

    return money

print("---------------------------------------------")
print("最终的金额是："+str(get_my_money()))
final_c=everyday_c['Value'][len(everyday_c['Value'])-1]
final_g=everyday_h['Value'][len(everyday_h['Value'])-1]
final_b=everyday_b['Value'][len(everyday_b['Value'])-1]
print("最终的(c,g,b)值为({:},{:},{:})".format(final_c,final_g,final_b))

""" 结果为 """

everyday_money={
    'Date':[],
    'Value':[]
}

with open('Python/数模/money.txt','r',encoding='utf-8') as file:
    for line in file:
        everyday_money['Value'].append(float(line.strip()))

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

for i in range(len(df2)):
    everyday_money['Date'].append(df2.index[i].strftime('%m/%d/%y'))

edf1=pd.DataFrame(everyday_money)
edf1['Date'] = pd.to_datetime(edf1['Date'])
edf1.set_index('Date', inplace=True)

plt.plot(edf1.index, edf1['Value'], marker='o', linestyle='-', color='b', label='Everyday Money', markersize=1)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Everyday Money')
plt.legend()
plt.grid(True)

# 显示图表
plt.show()

edf2=pd.DataFrame(everyday_c)
edf2['Date'] = pd.to_datetime(edf2['Date'])
edf2.set_index('Date', inplace=True)

edf3=pd.DataFrame(everyday_h)
edf3['Date'] = pd.to_datetime(edf3['Date'])
edf3.set_index('Date', inplace=True)

edf4=pd.DataFrame(everyday_b)
edf4['Date'] = pd.to_datetime(edf4['Date'])
edf4.set_index('Date', inplace=True)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 15))  # 创建1行2列的子图

#绘制第一个子图
ax1.plot(edf2.index, edf2['Value'], marker='o', linestyle='-', color='b', label='c', markersize=1)
ax1.set_xlabel('Date')
ax1.set_ylabel('Value')
ax1.set_title('C')
ax1.legend()
ax1.grid(True)

#绘制第一个子图
ax2.plot(edf3.index, edf3['Value'], marker='o', linestyle='-', color='b', label='gold', markersize=1)
ax2.set_xlabel('Date')
ax2.set_ylabel('Value')
ax2.set_title('Gold')
ax2.legend()
ax2.grid(True)

#绘制第一个子图
ax3.plot(edf4.index, edf4['Value'], marker='o', linestyle='-', color='b', label='bitcon', markersize=1)
ax3.set_xlabel('Date')
ax3.set_ylabel('Value')
ax3.set_title('Bitcon')
ax3.legend()
ax3.grid(True)

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()