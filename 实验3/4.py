course = ["Python", "Java", "C"]
score = [98, 86, 66]

# 列表推导式 + zip
d1 = {c: s for c, s in zip(course, score)}
print(d1)

# 普通循环 + zip
d2 = {}
for c, s in zip(course, score):
    d2[c] = s
print(d2)

# 循环嵌套
d3 = {}
for c in course:
    for s in score:
        d3[c] = s
print(d3)