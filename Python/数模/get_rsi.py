import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from sklearn.linear_model import LinearRegression
from prophet import Prophet
import numpy as np
import statsmodels.api as sm
import itertools

# 填补缺失的数据
def fill_missing_data(df):
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
    df.set_index('Date', inplace=True)
    df = df.asfreq('D')
    df['USD (PM)'].fillna(df['USD (PM)'].rolling(window=7, min_periods=1).mean(), inplace=True)
    return df

def get_rsi(target_date, csv_file_code=0, n=15):
    csv_file='Python/数模/data/LBMA-GOLD.csv'
    if csv_file_code==1:
        csv_file='Python/数模/data/BCHAIN-MKPRU.csv'
    df = pd.read_csv(csv_file, names=['Date', 'USD (PM)'], header=0)
    df = fill_missing_data(df)
    
    target_date = pd.to_datetime(target_date, format='%m/%d/%y')
    training_data = df[df.index <= target_date]

    # 确保没有 NaN 值
    training_data = training_data.dropna()

    if len(training_data)<=n:
        print('数据不够')
        return -1
    
    # 计算每日的涨跌幅度
    delta = training_data['USD (PM)'].diff()

    # 分离涨幅和跌幅
    gain = (delta.where(delta > 0, 0)).tail(n)
    loss = (-delta.where(delta < 0, 0)).tail(n)

    # 计算平均涨幅和平均跌幅
    avg_gain = gain.mean()
    avg_loss = loss.mean()

    # 计算相对强弱（RS）
    if avg_loss == 0:
        rs = float('inf')
    else:
        rs = avg_gain / avg_loss

    # 计算 RSI
    rsi = 100 - (100 / (1 + rs))

    return rsi

# 示例调用
rsi_value = get_rsi('9/26/18', 1)
print(f"RSI value: {rsi_value}")