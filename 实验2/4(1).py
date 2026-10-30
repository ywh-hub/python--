# 1 到 100 中所有 7 的倍数的立方和
total = sum([x ** 3 for x in range(1, 101) if x % 7 == 0])
print("7的倍数的立方和：", total)

# 矩阵转置
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("转置后：", transpose)