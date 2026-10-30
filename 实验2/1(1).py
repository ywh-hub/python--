lst1 = [1, 2, 1, 2, 1, 1, 1]
# 倒着删除，避免正着删时下标错乱
for i in range(len(lst1) - 1, -1, -1):
    if lst1[i] == 1:
        del lst1[i]
print("del删除后：", lst1)