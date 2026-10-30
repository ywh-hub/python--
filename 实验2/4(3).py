scores = {
    "Zhang San": 45,
    "Li si": 78,
    "WangWu": 40,
    "Zhou Liu": 96,
    "Zhao Qi": 65,
    "Sun Ba": 90,
    "Zheng Jiu": 78,
    "Wu Shi": 99,
    "Dong Shiyi": 60
}

max_score = max(scores.values())
min_score = min(scores.values())
avg_score = sum(scores.values()) / len(scores)

# 找出所有最高分同学
top_students = [name for name, score in scores.items() if score == max_score]

print("最高分：", max_score)
print("最低分：", min_score)
print("平均分：", avg_score)
print("最高分同学：", top_students)