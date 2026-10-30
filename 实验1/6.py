print("百元百鸡方案：")

for cock in range(0, 21):
    for hen in range(0, 34):
        chick = 100 - cock - hen

        if chick >= 0:
            if 5 * cock + 3 * hen + 0.5 * chick == 100:
                print("公鸡", cock, "只，母鸡", hen, "只，小鸡", chick, "只")