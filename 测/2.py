def is_prime(num):
    """判断 num 是不是素数"""
    if num < 2:
        return False
    i = 2
    while i * i <= num:   # 只要试到 sqrt(num) 就够了
        if num % i == 0:
            return False
        i = i + 1
    return True


def check():
    """验证 4 到 100000 的偶数都能分解成两个素数之和"""
    even = 4
    while even <= 100000:
        ok = False
        # 从 2 开始找一个素数 p，看 even - p 是不是也是素数
        p = 2
        while p <= even // 2:
            if is_prime(p) and is_prime(even - p):
                ok = True
                break
            p = p + 1
        if not ok:
            print("验证失败：", even)
            return
        even = even + 2
    print("验证成功：4 到 100000 的偶数都能分解成两个素数之和")


check()