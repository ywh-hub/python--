def gcd_euclid(a, b):
    """辗转相除法求最大公约数"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """求最小公倍数"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_euclid(a, b)


def prime_factorization(n):
    """非递归方法对正整数进行素因数分解"""
    if n < 2:
        return []

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2

    if n > 1:
        factors.append(n)

    return factors


if __name__ == "__main__":
    a, b = 36, 60
    print("最大公约数：", gcd_euclid(a, b))
    print("最小公倍数：", lcm(a, b))

    n = 360
    factors = prime_factorization(n)
    print(n, "的素因数分解：", factors)
    print("表达式：", "*".join(map(str, factors)))