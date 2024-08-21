import random

while 1:
    l = ["三枪", "石头", "卫队", "天狗",
         "精锐", "猪猪", "亡灵群", "黄毛",
         "绿林团伙", "小电车", "骨龙", "骷髅海",
         "团伙", "ac", "骨盾", "水人",
         "蝙蝠", "炸弹人", "小王子", "火锅",
         "骨王", "婆婆", "鸟", "牢笼",
         "炮车", "黑王", "箭雨", "野猪",
         "蛮羊", "王子"]
    s = int(input("输入1继续，输入2结束"))
    if s == 2:
        break
    elif s == 1:
        i = 0
        flag = True
        while i < 8:
            a = random.randint(0, len(l) - 1)

            if l[a] == "小王子" or l[a] == "骨王":
                if flag:
                    flag = False
                else:
                    continue
            print(l.pop(a), end=" ")
            i += 1
        print('\n')
    else:
        print("请输入正确的数字")