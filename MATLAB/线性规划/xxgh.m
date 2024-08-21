f = [-40;-30]; %目标函数中变量的系数矩阵
a = [1,1;-1,0;0,-1;240,120]; %小于等于的约束条件
b = [6;-1;-1;1200];

%标准形式:[x,fval]=linprog(f,A,b,aeq,beq,lb,ub)
[x,y] = linprog(f,a,b);
y = -y;
disp(strcat('x:',num2str(x)))
disp(strcat('y:',num2str(y)))