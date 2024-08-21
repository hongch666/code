# 打开文件以写入模式 ('w') 打开，如果文件不存在将会创建文件
a=[12.3,4.3,5.8,7.7]
with open('Python/数模/money.txt', 'w', encoding='utf-8') as file:
    for item in a:
        file.write(str(item) + '\n')  # 写入每个元素并添加换行符