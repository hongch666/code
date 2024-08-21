import pandas as pd
from pylab import *
import statsmodels.api as sm
from datetime import datetime
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.stats.diagnostic import acorr_ljungbox
 
 
def adf_test(timeseries):
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)
 
 
def kpss_test(timeseries):
    print('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c')
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key, value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print(kpss_output)
 
 
dataGOLD = pd.read_csv("Python/数模/data/LBMA-GOLD.csv")
dataMKPRU = pd.read_csv("Python/数模/data/BCHAIN-MKPRU.csv")
dataGOLD['Date'] = pd.to_datetime(dataGOLD.Date)
dataMKPRU['Date'] = pd.to_datetime(dataMKPRU.Date)
dataGOLD = dataGOLD[dataGOLD['Date'] >= datetime.strptime('2016-9-11', "%Y-%m-%d")]
dataMKPRU = dataMKPRU[dataMKPRU['Date'] >= datetime.strptime('2016-9-11', "%Y-%m-%d")]
dataGOLD = dataGOLD[dataGOLD['Date'] <= datetime.strptime('2021-9-10', "%Y-%m-%d")]
dataMKPRU = dataMKPRU[dataMKPRU['Date'] <= datetime.strptime('2021-9-10', "%Y-%m-%d")]
dataGOLD = dataGOLD.sort_values('Date').reset_index(drop=True)
dataMKPRU = dataMKPRU.sort_values('Date').reset_index(drop=True)
 
adf_test(dataGOLD['Value'])
kpss_test(dataGOLD['Value'])
 
diffGOLD = dataGOLD['Value'].diff(1).dropna()
diffMKPRU = dataMKPRU['Value'].diff(1).dropna()
 
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
sm.graphics.tsa.plot_acf(diffMKPRU, ax=ax1)
ax1.xaxis.set_ticks_position('top')
ax2 = fig.add_subplot(212)
sm.graphics.tsa.plot_pacf(diffMKPRU, ax=ax2)
ax2.xaxis.set_ticks_position('bottom')
fig.tight_layout()
plt.show()
 
fig = plt.figure(figsize=(12, 8))
ax11 = fig.add_subplot(211)
sm.graphics.tsa.plot_acf(diffGOLD, ax=ax11)
ax11.xaxis.set_ticks_position('top')
ax22 = fig.add_subplot(212)
sm.graphics.tsa.plot_pacf(diffGOLD, ax=ax22)
ax22.xaxis.set_ticks_position('bottom')
fig.tight_layout()
plt.show()
 
p_value = acorr_ljungbox(dataGOLD['Value'])
print(p_value)
 
results = sm.tsa.arma_order_select_ic(dataMKPRU['Value'], ic=['aic', 'bic'], trend='nc', max_ar=5, max_ma=5)
print('AIC', results.aic_min_order)
print('BIC', results.bic_min_order)
 
n_sample = dataGOLD['Value'].shape[0]
n_train = int(n_sample * 0.95) + 1
n_forecast = n_sample - n_train
 
ts_train = dataGOLD.iloc[:n_train]['Value']
ts_test = dataGOLD.iloc[n_train:]['Value']
 
arima = sm.tsa.SARIMAX(ts_train, order=(2, 1, 0))
model_results = arima.fit()
model_results.plot_diagnostics(figsize=(16, 12))
plt.show()
print(model_results.summary())
 
plt.title("Bitcoin price image after first-order difference")
plt.plot(dataMKPRU['Date'], dataMKPRU['Value'].diff(1))
plt.show()
 
plt.title("Gold price image after first-order difference")
plt.plot(dataGOLD['Date'], dataGOLD['Value'].diff(1))
plt.show()
 
 