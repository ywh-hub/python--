print("矩形九九表：")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j:2}", end=" ")
    print()

print("\n下三角九九表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j:2}", end=" ")
    print()

print("\n上三角九九表：")
for i in range(1, 10):
    print(" " * (7 * (i - 1)), end="")
    for j in range(i, 10):
        print(f"{i}*{j}={i*j:2}", end=" ")
    print()