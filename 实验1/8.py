fib = [1, 1]

for i in range(2, 100):
    next_num = fib[i - 1] + fib[i - 2]
    fib.append(next_num)

for i in range(100):
    print("第", i + 1, "项是：", fib[i])