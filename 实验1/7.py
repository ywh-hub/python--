print("水仙花数：")

for num in range(100, 1000):
    a = num // 100
    b = num // 10 % 10
    c = num % 10

    if a * a * a + b * b * b + c * c * c == num:
        print(num)