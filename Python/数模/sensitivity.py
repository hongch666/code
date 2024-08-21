# from main import get_my_money
import matplotlib.pyplot as plt

""" 敏感性分析 """

a=[1,1.1,1.2]
b=[2,2.2,2.4]
#下面数据为代码执行过一次所得的结果，为快速生成图片故直接写进代码中，计算部分已注释
money_a=[140883.92113250002, 140882.93513250002, 140881.94913249998]
money_b=[140883.92113250002, 140883.89113250002, 140883.86113250002]
""" for i in a:
    money_a.append(get_my_money(i,2))
for i in b:
    money_b.append(get_my_money(1,i)) """

print("a:")
print(money_a)
print("b:")
print(money_b)

a_ave=0
for i in range(1,len(money_a)):
    a_ave+=(money_a[i]-money_a[i-1])/money_a[i-1]
a_ave/=(len(money_a)-1)

b_ave=0
for i in range(1,len(money_b)):
    b_ave+=(money_b[i]-money_b[i-1])/money_b[i-1]
b_ave/=(len(money_b)-1)

print("a每增加10%，最终的金额减少{:.2g}%".format(abs(a_ave*100)))
print("b每增加10%，最终的金额减少{:.2g}%".format(abs(b_ave*100)))

a=[str(i) for i in a]
b=[str(i) for i in a]

# 绘制条形图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # 创建1行2列的子图

# 绘制子图1
bars1 = ax1.bar(a, money_a, capsize=2, color='b')
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8)

# 添加标题和标签
ax1.set_title('Sensitivity a')
ax1.set_xlabel('a')
ax1.set_ylabel('Money')
ax1.grid(True)

# 绘制子图2
bars2 = ax2.bar(b, money_b, capsize=2, color='b')
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8)

# 添加标题和标签
ax2.set_title('Sensitivity b')
ax2.set_xlabel('b')
ax2.set_ylabel('Money')
ax2.grid(True)

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()