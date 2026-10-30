vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# sum(vec, []) 的作用：把里面的子列表拼接成一个新列表
flat = sum(vec, [])
print("sum(vec, []) =", flat)

# 再求和
print("总和 =", sum(flat))

