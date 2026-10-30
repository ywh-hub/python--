score = float(input("请输入百分制成绩："))

if score >= 90 and score <= 100:
    print("优秀")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 70 and score < 80:
    print("中等")
elif score >= 60 and score < 70:
    print("及格")
elif score >= 0 and score < 60:
    print("不及格")
else:
    print("非法数据")