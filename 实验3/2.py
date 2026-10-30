import os
import re

COURSES = ["大学英语", "高等数学", "大学物理", "地理信息学", "Python程序设计", "大学体育"]

def load_students(path="Student.txt"):
    students = {}
    if not os.path.exists(path):
        return students

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            p = [x.strip() for x in line.split(",")]
            if len(p) < 9:
                continue

            sid = p[0]
            hobbies = set(h for h in re.split(r"[;；]", p[8]) if h)
            students[sid] = {
                "学号": sid,
                "姓名": p[1],
                "性别": p[2],
                "年龄": int(p[3]),
                "身高": float(p[4]),
                "籍贯": p[5],
                "班级": p[6],
                "党员否": p[7],
                "兴趣爱好": hobbies
            }
    return students


def load_scores(path="scores.txt"):
    scores = {}
    if not os.path.exists(path):
        return scores

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            p = [x.strip() for x in line.split(",")]
            if len(p) < 7:
                continue
            sid = p[0]
            scores[sid] = dict(zip(COURSES, map(float, p[1:7])))
    return scores


def find_student(key, students, scores):
    """按学号或姓名查找学生全部信息"""
    key = str(key)
    result = []
    for sid, info in students.items():
        if key == sid or key == info["姓名"]:
            result.append({
                "基本信息": info,
                "成绩": scores.get(sid, {})
            })
    return result


def course_statistics(students, scores):
    """每门课的平均分、最高分、最低分、不及格人数"""
    result = {}
    for course in COURSES:
        values = [
            scores[sid][course]
            for sid in scores
            if sid in students and course in scores[sid]
        ]
        if values:
            result[course] = {
                "平均分": sum(values) / len(values),
                "最高分": max(values),
                "最低分": min(values),
                "不及格人数": sum(v < 60 for v in values)
            }
    return result


def overall_statistics(students, scores):
    """所有学生所有课程的最高分、最低分；每个学生不及格门数"""
    all_values = []
    fail_counts = {}

    for sid in students:
        stu_scores = scores.get(sid, {})
        values = [stu_scores[c] for c in COURSES if c in stu_scores]
        all_values.extend(values)
        fail_counts[sid] = sum(v < 60 for v in values)

    return {
        "所有课程最高分": max(all_values) if all_values else None,
        "所有课程最低分": min(all_values) if all_values else None,
        "每个学生不及格门数": fail_counts
    }


def common_hobby_pairs(students):
    """具有共同爱好的学生对"""
    ids = list(students.keys())
    result = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            common = students[a]["兴趣爱好"] & students[b]["兴趣爱好"]
            if common:
                result.append((a, b, common))
    return result


def fully_different_pairs(students):
    """任意两个学生之间没有共同爱好的学生对"""
    ids = list(students.keys())
    result = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            if not (students[a]["兴趣爱好"] & students[b]["兴趣爱好"]):
                result.append((a, b))
    return result


def students_with_no_common_hobby(students):
    """某个学生与其他所有学生都没有共同爱好"""
    ids = list(students.keys())
    result = []
    for sid in ids:
        if all(
            not (students[sid]["兴趣爱好"] & students[other]["兴趣爱好"])
            for other in ids if other != sid
        ):
            result.append(sid)
    return result


def all_hobbies(students):
    """统计所有爱好"""
    result = set()
    for info in students.values():
        result |= info["兴趣爱好"]
    return result


if __name__ == "__main__":
    students = load_students()
    scores = load_scores()

    print("查找张三：", find_student("张三", students, scores))
    print("各门课统计：", course_statistics(students, scores))
    print("总体统计：", overall_statistics(students, scores))
    print("有共同爱好的学生对：", common_hobby_pairs(students))
    print("爱好完全不同的学生对：", fully_different_pairs(students))
    print("与其他学生均无共同爱好的学生：", students_with_no_common_hobby(students))
    print("所有爱好：", all_hobbies(students))