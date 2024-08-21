import matplotlib.pyplot as plt

# 定义数据
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 15, 7, 12, 9]

# 创建图
plt.figure()

# 绘制条形图
plt.bar(x, y)

# 设置标题和坐标轴标签
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 在每个柱上显示对应的数值
for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')

# 显示图
plt.show()
