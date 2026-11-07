def partition(x, n):
    small = []   # 存小于 n 的数
    equal = []   # 存等于 n 的数
    big = []     # 存大于 n 的数

    for num in x:
        if num < n:
            small.append(num)
        elif num == n:
            equal.append(num)
        else:
            big.append(num)

    # 把结果写回原列表
    x[:] = small + equal + big
    return x


if __name__ == "__main__":
    s = input("请输入互不相等的整数列表，用空格隔开：")
    parts = s.split()
    arr = []
    for v in parts:
        arr.append(int(v))
    n = int(input("请输入支点 n："))
    print("划分结果：", partition(arr, n))