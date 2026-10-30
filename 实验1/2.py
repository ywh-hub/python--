s = input("请输入多个实数，用空格分开：")
parts = s.split()

nums = []
for x in parts:
    nums.append(float(x))

if len(nums) == 0:
    print("没有输入数据")
else:
    total = 0
    for x in nums:
        total = total + x

    avg = total / len(nums)

    result = [avg]
    for x in nums:
        if x > avg:
            result.append(x)

    result = tuple(result)
    print(result)