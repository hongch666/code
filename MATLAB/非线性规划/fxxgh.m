clc,clear;

%标准形式：[x,fval]=fmincon(fun,x0,A,b,aeq,beq,lb,ub,nonlcon)
%fun：单独函数文件里面定义的目标函数
%x0:决策变量的初始值，不知道随便写
%A,b：线性约束的不等式变量系数矩阵和常数项矩阵（≤）
%Aeq,beq：线性约束的等式变量系数矩阵和常数项矩阵
%lb,ub：决策变量的最小取值和最大取值
%nonlcon：非线性约束，包括不等式和等式
[x,y] = fmincon('fun1',[10;0;0],[],[],[],[],[0;0;0],[],'fun2');
disp(strcat('x:',num2str(x)))
disp(strcat('y:',num2str(y)))