clc,clear;
f = [-3;-2;-1]; %目标函数中变量的系数矩阵
intcon = 3; %整数变量的地址
a = ones(1,3); %小于等于的约束条件
b = 7; %小于等于的约束条件
aeq = [4 2 1]; %等于的约束条件
beq = 12; %等于的约束条件
lb = zeros(3,1); %变量的约束条件
ub = [inf;inf;1]; %变量的约束条件

%标准形式：[x,fval]=intlinprog(f,intcon,A,b,aeq,beq,lb,ub)
[x,y] = intlinprog(f,intcon,a,b,aeq,beq,lb,ub);
disp(strcat('x:',num2str(x)))
disp(strcat('y:',num2str(y)))