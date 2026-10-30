text = """Sports help everyone to keep healthy, happy, and efficient. So I pay special attention to games, especially table-tennis.Table tennis is my favorite game. I play it almost every day Table-tennis is an ideal game for us because it brings the whole body into action. It strengthens our muscles, expands our lungs, promotes the circulation of the blood, and causes a healthy action of the skin. Besides, it is very amusing and does not cost us much money. Table-tennis is very moderate; it is not so rough as football. It is an indoor game and can be played even on rainy days. Thus, it is my favorite kind of exercise.
One morning a fox sees a cock.He think "This is my breakfast. He comes up to the cock and says "l know you can sing very well. Can you sing for me? The cock is glad. He closes his eyes and begins to sing. The fox sees that and catches him in his mouth and carries him away. The people in the field see the fox.They cry "Look, look! The fox is carrying the cock away. The cock says to the fox "Mr Fox, do you understand? The people say you are carrying their cock away. Tell them it is yours. Not theirs. The fox opens his mouth and says "The cock is mine, not yours. Just then the cock runs away from the fox and flies into the tree."""

text = text.replace(".", " ").replace(",", " ").replace("?", " ").replace("!", " ").replace('"', " ").replace("-", "")
text = text.lower()
words = text.split()

# 统计字典
dic = {}
for w in words:
    if w in dic:
        dic[w] = dic[w] + 1
    else:
        dic[w] = 1

# 找最多和最少的
items = []
for k in dic:
    items.append((k, dic[k]))

# 冒泡排序，按照次数降序
for i in range(len(items)):
    for j in range(len(items) - 1 - i):
        if items[j][1] < items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]  # 交换

print("最多的三个：")
for i in range(3):
    print(items[i])

print("最少的三个：")
for i in range(len(items)-3, len(items)):
    print(items[i])

# 找第二多的单词
second_word = items[1][0]
print("第二多的单词是：", second_word)

# 删除单词
new_text = text.replace(second_word, "")
print("删除后的文章：", new_text)