import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from sklearn.linear_model import LinearRegression
from prophet import Prophet
import numpy as np
import statsmodels.api as sm
import itertools

""" 预测下一天的价值 """

# 填补缺失的数据
def fill_missing_data(df):
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
    df.set_index('Date', inplace=True)
    df = df.asfreq('D')
    df['USD (PM)'].fillna(df['USD (PM)'].rolling(window=7, min_periods=1).mean(), inplace=True)
    return df

# 使用线性回归进行预测
def linear_regression_predict(training_data, steps):
    training_data['Timestamp'] = training_data.index.map(pd.Timestamp.timestamp)  # 转换时间戳为秒数
    X = training_data['Timestamp'].values.reshape(-1, 1)
    y = training_data['USD (PM)'].values

    model = LinearRegression()
    model.fit(X, y)

    predictions = []
    for step in range(1, steps + 1):
        next_timestamp = (training_data.index[-1].timestamp()) + 86400 * step  # 下一个日期的时间戳（秒数）
        predicted_value = model.predict([[next_timestamp]])
        predictions.append(predicted_value[0])

    return predictions

# 使用 ARIMA 模型进行预测
def arima_predict(training_data, steps, which=0):
    # 使用 auto_arima 来自动确定 p, d, q 参数
    if which==0:
        p, d, q = 2, 1, 0  # 这里可以使用自动确定的参数，或根据实际情况设置
    else:
        p, d, q = 4, 1, 0
    # 拟合 ARIMA 模型
    model = ARIMA(training_data['USD (PM)'], order=(p, d, q))
    model_fit = model.fit()

    # 预测目标日期的价格
    forecast = model_fit.forecast(steps=steps)
    predicted_values = forecast.tolist()

    return predicted_values

# 使用 Prophet 模型进行预测
def prophet_predict(training_data, steps):
    training_data.reset_index(inplace=True)
    training_data.rename(columns={'Date': 'ds', 'USD (PM)': 'y'}, inplace=True)

    model = Prophet(
        seasonality_mode='multiplicative',  # 使用乘法季节性
        yearly_seasonality=True,             # 启用年度季节性
        weekly_seasonality=True,             # 启用周季节性
        daily_seasonality=False,             # 关闭日季节性
        changepoint_prior_scale=0.5,         # 调整变化点的灵敏度
        seasonality_prior_scale=10.0         # 调整季节性先验参数
    )
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)  # 添加月度季节性

    model.fit(training_data)

    future = model.make_future_dataframe(periods=steps)
    forecast = model.predict(future)

    predicted_values = forecast['yhat'].iloc[-steps:].values
    return predicted_values

# 主预测函数
def predict_price(target_date, csv_file='Python/数模/data/LBMA-GOLD.csv', steps=7, threshold_arima=30, threshold_prophet=2000):
    df = pd.read_csv(csv_file, names=['Date', 'USD (PM)'], header=0)
    df = fill_missing_data(df)
    
    target_date = pd.to_datetime(target_date, format='%m/%d/%y')
    training_data = df[df.index <= target_date]

    # 确保没有 NaN 值
    training_data = training_data.dropna()

    which=0
    if csv_file=='Python/数模/data/BCHAIN-MKPRU.csv':
        which=1

    if len(training_data) < threshold_arima:
        # 数据量较小时使用线性回归模型
        predicted_values = linear_regression_predict(training_data, steps)
    else: #len(training_data) < threshold_prophet:
        # 数据量适中时使用 ARIMA 模型
        predicted_values = arima_predict(training_data, steps, which)
    """ else:
        # 数据量较大时使用 Prophet 模型
        predicted_values = prophet_predict(training_data, steps) """

    average_value = np.mean(predicted_values)

    return average_value

# 示例调用
predicted_average_value = predict_price('09/11/20', 'Python/数模/data/BCHAIN-MKPRU.csv')
print(f"Predicted average value for the next 7 days: {predicted_average_value}")
