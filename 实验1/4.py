n = int(input("请输入n："))

triangle = []

for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(row)

print("杨辉三角：")
for row in triangle:
    line = ""
    for x in row:
        line = line + str(x) + " "
    print(line.center(60))

print("镜像：")
for i in range(n - 2, -1, -1):
    row = triangle[i]
    line = ""
    for x in row:
        line = line + str(x) + " "
    print(line.center(60))