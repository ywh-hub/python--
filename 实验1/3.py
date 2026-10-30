ok = True

for n in range(4, 100001, 2):
    found = False

    for i in range(2, n // 2 + 1):
        # 判断 i 是不是素数
        i_is_prime = True
        k = 2
        while k * k <= i:
            if i % k == 0:
                i_is_prime = False
                break
            k = k + 1

        if i_is_prime == False:
            continue

        j = n - i

        # 判断 j 是不是素数
        j_is_prime = True
        if j < 2:
            j_is_prime = False
        else:
            k = 2
            while k * k <= j:
                if j % k == 0:
                    j_is_prime = False
                    break
                k = k + 1

        if j_is_prime == True:
            found = True
            break

    if found == False:
        print("发现不满足的偶数：", n)
        ok = False
        break

if ok == True:
    print("4到100000范围内的偶数都满足哥德巴赫猜想")