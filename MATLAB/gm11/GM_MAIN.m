%% 输入原始数据并作出时间序列图
clear;clc
year = [24:1:29]'; %横坐标表示天
x0 = [58,37,23,33,35,36]'; %原始数据序列，写成列向量形式

%画出原始数据的时间序列图
figure(1);
plot(year,x0,'o-');
grid on;
set(gca,'xtick',year(1:1:end))
xlabel('年份');
ylabel('排污总量');

%% 判断是否适用于数据期数较短的非负时间序列
ERROR = 0; %建立一个错误指标，一旦出错就指定为1
%判断是否有负数元素
if sum(x0<0) > 0
    disp('灰色预测的时间序列中不能有负数')
    ERROR = 1; 
end
%判断数据量是否太少
n = length(x0); %原始数据长度
disp(strcat('原始数据的长度为',num2str(n)))
if n<=3
    disp('数据量太小')
    ERROR = 1;
end
%数据太多时提示可考虑使用其他方法
if n>10
    disp('考虑其他使用方法')
end
%判断数据是否为列向量，如果输入的是行向量则转置为列向量
if size(x0,1) == 1
    x0 = x0';
end
if size(year,1) == 1
    year = year';
end

%% 对一次累加后的数据进行准指数规律的检验
if ERROR == 0
    disp('----------------------------------------')
    disp('准指数规律检验')
    x1 = cumsum(x0); %累加
    rho = x0(2:end) ./ x1(1:end-1); %计算光滑度
    %画出光滑度图形和0.5的直线
    figure(2)
    plot(year(2:end),rho,'-o',[year(2),year(end)],[0.5,0.5],'-');
    grid on;
    text(year(end-1)+0.2,0.55,'临界线')
    set(gca,'xtick',year(2:1:end))
    xlabel('年份');
    ylabel('原始数据的光滑度');
    
    disp(strcat('指标1：光滑度比小于0.5的数据占比为',num2str(100*sum(rho<0.5)/(n-1)),'%'))
    disp(strcat('指标2：除去前两个周期外，光滑度比小于0.5的数据占比为',num2str(100*sum(rho(3:end)<0.5)/(n-1)),'%'))
    disp('参考标准：指标1一般要大于60%，指标2要大于90%')
    
    Judge = input('你认为可以通过准指数规律的检验吗？可以输入1，不能输入0');
    if Judge == 0
        disp('不适合')
        ERROR = 1;
    end
    disp('----------------------------------------')
end

if ERROR == 0
    if n > 7 %分训练组和试验组(n>7取后三年，n<7取后两年)
        test_num = 3;
    else
        test_num = 2;
    end
    train_x0 = x0(1:end-test_num); %训练数据
    disp('训练数据是：')
    disp(mat2str(train_x0'))
    test_x0 = x0(end-test_num+1:end); %试验数据
    disp('试验数据是：')
    disp(mat2str(test_x0'))
    disp('----------------------------------------')
    %使用GM(1,1)模型对训练数据进行训练，返回的result计算往后预测test_num的数据
    disp(' ')
    disp('***下面是GM(1,1)模型预测的详细过程***')
    result1 = gm11(train_x0,test_num);
    disp(' ')
    disp('----------------------------------------')
    %绘制对试验数据进行预测的图形
    test_year = year(end-test_num+1:end); %试验组对应年份
    figure(3)
    plot(test_year,test_x0,'-o',test_year,result1,'*-');
    grid on;
    set(gca,'xtick',year(end-test_num+1):1:year(end))
    legend('试验组的真实数据','GM(1,1)预测结果')
    xlabel('年份');
    ylabel('排污总量');
    
    predict_num = input('请输入你要往后面预测的的期数：');
    [result,x0_hat,relative_residuals,eta] = gm11(x0,predict_num);
    
    %% 输出使用最佳的模型预测出来的结果
    disp('----------------------------------------')
    disp('对原始数据的拟合结果：')
    for i =1:n
        disp(strcat(num2str(year(i)),': ',num2str(x0_hat(i))))
    end
    disp(strcat('往后预测',num2str(predict_num),'期的得到的结果：'))
    for i = 1:predict_num
        disp(strcat(num2str(year(end)+i),'：',num2str(result(i))));
    end
    
    %% 绘制相对残差和级比偏差的图形
    figure(4)
    subplot(2,1,1) %绘制子图
    plot(year(2:end),relative_residuals,'*-');
    grid on;
    legend('相等残差');
    xlabel('年份');
    set(gca,'xtick',year(2:1:end))
    disp(' ')
    disp('****下面将输出对原数据拟合的评价结果****')
    
    %% 残差检验
    average_relative_residuals = mean(relative_residuals); %计算平均残差
    disp(strcat('平均相对残差为',num2str(average_relative_residuals)))
    if average_relative_residuals<0.1
        disp('残差检验的结果表明：该模型对原始数据的拟合程度非常不错')
    elseif average_relative_residuals<0.2
        disp('残差检验的结果表明：该模型对原始数据的拟合程度达到一般要求')
    else
        disp('残差检验的结果表明：该模型对原始数据的拟合程度不太好')
    end
    
    %% 级比偏差检验
    average_eta = mean(eta); %计算平均级比偏差
    disp(strcat('平均级比偏差为',num2str(average_eta)))
    if average_eta<0.1
        disp('级比检验的结果表明：该模型对原始数据的拟合程度非常不错')
    elseif average_eta<0.2
        disp('级比检验的结果表明：该模型对原始数据的拟合程度达到一般要求')
    else
        disp('级比检验的结果表明：该模型对原始数据的拟合程度不太好，建议使用其他模型预测')
    end
    disp(' ')
    disp('----------------------------------------')
    
    %% 绘制最终的预测效果图
    figure(5);
    plot(year,x0,'-o',year,x0_hat,'-*m',year(end)+1:year(end)+predict_num,result,'-*b');
    grid on;
    hold on;
    plot([year(end),year(end)+1],[x0(end),result(1)],'-*b')
    legend('原始数据','拟合数据','预测数据')
    set(gca,'xtick',[year(1):1:year(end)+predict_num])
    xlabel('年份');
    ylabel('排污总量');
end