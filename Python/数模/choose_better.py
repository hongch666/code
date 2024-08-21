import matplotlib.pyplot as plt
#from main import *

""" 选择求最终金额的参数 """

# 示例数据
highs = [90, 91, 92, 93, 94, 95]
lows = [28, 29, 30, 31, 32, 33]
#下面数据为代码执行过一次所得的结果，为快速生成图片故直接写进代码中，计算部分已注释
values1 = [12307.02451550002, 12306.484515500018, 12319.50451550002, 12277.114515500021, 12277.114515500021, 12273.674515500019]
values2 = [12319.50451550002, 12319.50451550002, 12319.50451550002, 12319.50451550002, 12319.50451550002, 12319.50451550002]
values3 = [2096.153887499987, 11940.084515500037, 12319.50451550002, 13752.06738250001, 13221.382490000016, 13128.142490000015]
values4 = [9022.947379500041, 12102.348265500035, 12319.50451550002, 94120.28826550009, 139232.34826550004, 94643.6990955]

""" for i in highs:
    h_g=get_my_money(1,2,i,30,92,30)
    values2.append(h_g)
    h_b=get_my_money(1,2,92,30,i,30)
    values4.append(h_b)

for i in lows:
    l_g=get_my_money(1,2,92,i,92,30)
    values1.append(l_g)
    l_b=get_my_money(1,2,92,30,92,i)
    values3.append(l_b) """

print("Low Gold:")
print(values1)
print("High Gold:")
print(values2)
print("Low Bitcon:")
print(values3)
print("High Bitcon:")
print(values4)

# 绘制条形图
fig, ax = plt.subplots(2, 2, figsize=(10, 10))  # 创建2行2列的子图

# 绘制子图1
bars1 = ax[0, 0].bar(lows, values1, capsize=2, color='b')
for bar in bars1:
    yval = bar.get_height()
    ax[0, 0].text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8)

# 添加标题和标签
ax[0, 0].set_title('Gold Low Choose')
ax[0, 0].set_xlabel('Choose')
ax[0, 0].set_ylabel('MaxValues')

# 绘制子图2
bars2 = ax[0, 1].bar(highs, values2, capsize=2, color='b')
for bar in bars2:
    yval = bar.get_height()
    ax[0, 1].text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8)

# 添加标题和标签
ax[0, 1].set_title('Gold High Choose')
ax[0, 1].set_xlabel('Choose')
ax[0, 1].set_ylabel('MaxValues')

# 绘制子图3
bars3 = ax[1, 0].bar(lows, values3, capsize=2, color='b')
for bar in bars3:
    yval = bar.get_height()
    ax[1, 0].text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8)

# 添加标题和标签
ax[1, 0].set_title('Bitcoin Low Choose')
ax[1, 0].set_xlabel('Choose')
ax[1, 0].set_ylabel('MaxValues')

# 绘制子图4
bars4 = ax[1, 1].bar(highs, values4, capsize=2, color='b')
for bar in bars4:
    yval = bar.get_height()
    ax[1, 1].text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8)

# 添加标题和标签
ax[1, 1].set_title('Bitcoin High Choose')
ax[1, 1].set_xlabel('Choose')
ax[1, 1].set_ylabel('MaxValues')

# 调整子图之间的间距
plt.tight_layout()
plt.subplots_adjust(hspace=0.3)  # 增大上下图之间的间距

# 显示图表
plt.show()