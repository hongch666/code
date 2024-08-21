import pandas as pd

""" 用于判断当天是否为黄金开放日 """

def is_open(date_str):
    csv_file = 'Python/数模/data/LBMA-GOLD.csv'  # 替换为你的 CSV 文件路径
    df = pd.read_csv(csv_file, names=['Date', 'USD (PM)'], header=0)
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
    df.set_index('Date', inplace=True)
    df = df.asfreq('D')  # 设置频率为每天

    # 查找缺失值的日期
    missing_dates = df[df['USD (PM)'].isnull()].index

    # 检查给定日期是否在缺失日期列表中
    date_to_check = pd.to_datetime(date_str, format='%m/%d/%y')
    if date_to_check<df.index[0]:
        return False
    return date_to_check not in missing_dates

# 示例调用
date_str = '09/11/17'  # 替换为你要检查的日期
is_missing = is_open(date_str)
print(f" {date_str} 是黄金开放日吗? {is_missing}")
