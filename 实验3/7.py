import random

# --- 以下为截图中的随机数生成部分 ---
num = int(input("请输入数的个数: "))
x = [random.randint(1, 1000) for j in range(num)]
y = set(x)
z = list(y)  
# ----------------------------------

# 打印生成的列表，并确保输入 n 在列表中
print("生成的列表 z 为:", z)
n = int(input("请输入作为支点的整数 n: "))

# 判断 n 是否在列表中，防止出错
if n not in z:
    print(f"错误：支点 {n} 不在生成的列表中！")
else:
    # 列表推导式
    left = [i for i in z if i < n]   # 小于 n 的元素
    right = [i for i in z if i > n]  # 大于 n 的元素
    result = left + [n] + right      # 拼接起来
    
    print("划分后的列表为:", result)
    
   