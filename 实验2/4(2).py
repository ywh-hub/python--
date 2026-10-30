import os

d_path = "D:\\"  

if os.path.exists(d_path):
    for root, dirs, files in os.walk(d_path):
        for file in files:
            print(os.path.join(root, file))
else:
    print("没有找到 D 盘")