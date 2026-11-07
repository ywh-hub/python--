def yanghui(t):
    # 第一行是 [1]
    row = [1]
    for i in range(t):
        # 打印当前这一行（用空格隔开）
        for num in row:
            print(num, end=" ")
        print()  # 换行

        # 计算下一行
        new_row = [1]  # 每行开头是 1
        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])  # 中间元素 = 上一行相邻两数之和
        new_row.append(1)  # 每行结尾是 1
        row = new_row


if __name__ == "__main__":
    t = int(input("请输入要打印的行数 t："))
    yanghui(t)