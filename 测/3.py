def gcd(a, b):
    """辗转相除法求最大公约数"""
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def lcm(a, b):
    """求两个数的最小公倍数"""
    return a * b // gcd(a, b)


def lcm_many(num):
    """求多个数的最小公倍数"""
    result = num[0]
    for i in range(1, len(num)):
        result = lcm(result, num[i])
    return result


if __name__ == "__main__":
    s = input("请输入若干整数，用空格隔开：")
    parts = s.split()
    nums = []
    for v in parts:
        nums.append(int(v))
    print("最小公倍数是：", lcm_many(nums))