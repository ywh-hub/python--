a = [1, 2, 3]
b = a   # 直接赋值：a 和 b 指向同一块内存

print("a的地址：", id(a))
print("b的地址：", id(b))

b[0] = 100
print("修改b后，a =", a)
print("修改b后，b =", b)
