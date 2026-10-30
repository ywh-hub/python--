scores = [94, 89, 96, 88, 92, 86, 69, 95, 78, 85]

avg = sum(scores) / len(scores)

# 最高3个
top3 = sorted(scores, reverse=True)[:3]

# 最低3个
low3 = sorted(scores)[:3]

# 中位数
sorted_scores = sorted(scores)
n = len(sorted_scores)

if n % 2 == 0:
    median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
else:
    median = sorted_scores[n // 2]

print("平均分：", avg)
print("最高3个成绩：", top3)
print("最低3个成绩：", low3)
print("中位数：", median)