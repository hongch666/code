% 假设已有时间序列数据 y
y = [10, 12, 14, 16, 18, 20, 22]; % 示例数据

% 确保 y 是列向量
y = y(:);

% 拟合 ARMA 模型
model = arima(2, 0, 1); % 参数依次表示 p, d, q
fitModel = estimate(model, y);

% 预测未来的值
numSteps = 3; % 预测未来 3 个时间步长的值
forecastedValues = forecast(fitModel, numSteps);

% 打印结果
disp('预测的未来值：');
disp(forecastedValues);
