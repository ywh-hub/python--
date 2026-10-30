import copy

a = [[1, 2], [3, 4]]

b = a                  # 直接赋值：同一个对象
c = a.copy()           # 浅拷贝
d = copy.deepcopy(a)   # 深拷贝

print("a, b, c, d 的地址：")
print(id(a))
print(id(b))
print(id(c))
print(id(d))

print("\n内层列表地址：")
print("a[0]:", id(a[0]))
print("c[0]:", id(c[0]))
print("d[0]:", id(d[0]))

# 修改 a 里面的内层元素
a[0][0] = 999

print("\n修改 a[0][0] = 999 后：")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

# 给 a 外层追加元素
a.append([5, 6])

print("\n给 a 追加 [5, 6] 后：")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)