def f1(a):
    a = 100          # 重新绑定，不改变外部整数

def f2(lst):
    lst.append(4)    # 原地修改，改变外部列表

def f3(lst):
    lst = [1, 2]     # 重新绑定，不改变外部列表

def f4(d):
    d["x"] = 1       # 原地修改字典，改变外部字典

x = 10
f1(x)
print(x)             # 10

a = [1, 2, 3]
f2(a)
print(a)             # [1, 2, 3, 4]

b = [1, 2, 3]
f3(b)
print(b)             # [1, 2, 3]

c = {}
f4(c)
print(c)             # {'x': 1}