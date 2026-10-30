score = [
    ['Angle', '0121701100106', 99],
    ['Jack', '0121701100107', 86],
    ['Tom', '0121701100109', 77],
    ['Smith', '0121701100111', 100],
    ['Bob', '0121701100115', 77],
    ['Lily', '0121701100117', 59]
]

print("按姓名升序：")
for row in sorted(score, key=lambda x: x[0]):
    print(row)

print("\n按学号升序：")
for row in sorted(score, key=lambda x: x[1]):
    print(row)

print("\n按成绩升序，成绩相同按姓名升序：")
for row in sorted(score, key=lambda x: (x[2], x[0])):
    print(row)