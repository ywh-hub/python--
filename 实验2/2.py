lst = [3, 1, 2]

# insert：在指定位置插入
lst.insert(1, 99)
print("insert后：", lst)

# count：统计某个元素出现次数
print("count(1)：", lst.count(1))

# index：查找元素下标
print("index(2)：", lst.index(2))

# sort：原地排序，改变原列表
lst.sort()
print("sort后：", lst)

# sorted：返回新列表，不改变原列表
print("sorted降序：", sorted(lst, reverse=True))

# reverse：列表方法，原地反转
lst.reverse()
print("reverse后：", lst)

# reversed：内置函数，返回迭代器，需要 list() 查看
print("reversed后：", list(reversed(lst)))

# zip：把多个列表对应组合
names = ["A", "B", "C"]
ages = [18, 19, 20]
print("zip：", list(zip(names, ages)))

# enumerate：同时得到下标和元素
for i, name in enumerate(names):
    print("enumerate：", i, name)