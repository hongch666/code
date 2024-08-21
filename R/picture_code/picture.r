old_tempdir <- tempdir()  # 保存原始的临时文件路径
tempdir("D:/1code/R/test2")  # 设置一个新的临时文件路径
# 打开一个 PDF 绘图设备
pdf("plot.pdf")

# 定义x的取值范围
x <- seq(-10, 10, length.out=100)

# 计算对应的y值
y <- x^3 + 2 * x

# 绘制函数图像
plot(x, y, type="l", col="blue", xlab="x", ylab="y", main="Function Graph y=x^3")

# 关闭 PDF 绘图设备，保存绘图内容到文件
dev.off()
