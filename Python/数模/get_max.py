import pulp

""" 最大值求解 """

def solve_lp(h, bt, h1, bt1, c, x1, y1, a, b):
    """
    参数说明
    h：今天黄金的价格
    bt：今天比特币的价格
    h1：预测出明天黄金的价格
    bt1：预测出明天比特币的价格
    c：今天持有的现金
    x1：昨天持有的黄金的数量
    y1：昨天持有的比特币的数量
    a：黄金交易的成本
    b ：比特币交易的成本
    """
    s = c + h * x1 + bt * y1
    # 创建线性规划问题
    lp_problem = pulp.LpProblem("Maximize W", pulp.LpMaximize)

    # 定义决策变量
    x = pulp.LpVariable("x", lowBound=0,cat=pulp.LpInteger)
    y = pulp.LpVariable("y", lowBound=0,cat=pulp.LpInteger)
    abs_x_diff = pulp.LpVariable("abs_x_diff", lowBound=0)
    abs_y_diff = pulp.LpVariable("abs_y_diff", lowBound=0)

    # 定义目标函数
    lp_problem += h1 * x + bt1 * y + s - (h * x + bt * y) - (a / 100 * abs_x_diff + b / 100 * abs_y_diff), "W"

    # 添加约束条件
    lp_problem += s - (h * x + bt * y) - (a / 100 * abs_x_diff + b / 100 * abs_y_diff) >= 0, "Constraint 1"
    lp_problem += abs_x_diff >= x - x1, "Constraint 2"
    lp_problem += abs_x_diff >= -(x - x1), "Constraint 3"
    lp_problem += abs_y_diff >= y - y1, "Constraint 4"
    lp_problem += abs_y_diff >= -(y - y1), "Constraint 5"
    lp_problem += x >= 0, "Constraint 6"
    lp_problem += y >= 0, "Constraint 7"

    # 求解问题
    lp_problem.solve()

    # 返回结果
    return {
        "status": pulp.LpStatus[lp_problem.status],
        "x": pulp.value(x),
        "y": pulp.value(y),
        "Z": pulp.value(lp_problem.objective)
    }

def solve_lp_no_gold(bt, bt1, c, x1, y1, b):
    """
    参数说明
    h：今天黄金的价格
    bt：今天比特币的价格
    h1：预测出明天黄金的价格
    bt1：预测出明天比特币的价格
    c：今天持有的现金
    x1：昨天持有的黄金的数量
    y1：昨天持有的比特币的数量
    a：黄金交易的成本
    b ：比特币交易的成本
    """
    s = c + bt * y1 #这里表示能转换为现金的价值总额，因为黄金没开市，所以没有算进去
    # 创建线性规划问题
    lp_problem = pulp.LpProblem("Maximize W", pulp.LpMaximize)

    # 定义决策变量
    y = pulp.LpVariable("y", lowBound=0,cat=pulp.LpInteger)
    abs_y_diff = pulp.LpVariable("abs_y_diff", lowBound=0)

    # 定义目标函数
    lp_problem += bt1 * y + s - ( bt * y) - (b / 100 * abs_y_diff), "W"

    # 添加约束条件
    lp_problem += s - (bt * y) - (b / 100 * abs_y_diff) >= 0, "Constraint 1"
    lp_problem += abs_y_diff >= y - y1, "Constraint 4"
    lp_problem += abs_y_diff >= -(y - y1), "Constraint 5"
    lp_problem += y >= 0, "Constraint 7"

    # 求解问题
    lp_problem.solve()
    
    # 返回结果
    return {
        "status": pulp.LpStatus[lp_problem.status],
        "y": pulp.value(y),
        "Z": pulp.value(lp_problem.objective)
    }

def solve_lp_only_gold(h, h1, c, x1, y1, a):
    """
    参数说明
    h：今天黄金的价格
    bt：今天比特币的价格
    h1：预测出明天黄金的价格
    bt1：预测出明天比特币的价格
    c：今天持有的现金
    x1：昨天持有的黄金的数量
    y1：昨天持有的比特币的数量
    a：黄金交易的成本
    b ：比特币交易的成本
    """
    s = c + h * x1 #这里表示能转换为现金的价值总额，因为黄金没开市，所以没有算进去
    # 创建线性规划问题
    lp_problem = pulp.LpProblem("Maximize W", pulp.LpMaximize)

    # 定义决策变量
    x = pulp.LpVariable("x", lowBound=0,cat=pulp.LpInteger)
    abs_x_diff = pulp.LpVariable("abs_x_diff", lowBound=0)

    # 定义目标函数
    lp_problem += h1 * x + s - ( h * x) - (a / 100 * abs_x_diff), "W"

    # 添加约束条件
    lp_problem += s - (h * x) - (a / 100 * abs_x_diff) >= 0, "Constraint 1"
    lp_problem += abs_x_diff >= x - x1, "Constraint 4"
    lp_problem += abs_x_diff >= -(x - x1), "Constraint 5"
    lp_problem += x >= 0, "Constraint 7"

    # 求解问题
    lp_problem.solve()
    
    # 返回结果
    return {
        "status": pulp.LpStatus[lp_problem.status],
        "x": pulp.value(x),
        "Z": pulp.value(lp_problem.objective)
    }

result = solve_lp(324.6, 621.65, 326.65, 629.67, 1000, 0, 0, 1, 2)
for key, value in result.items():
    print(f"{key}: {value}")
