# 实验1：学生类的设计
class Student:
    """学生类：记录学号、姓名、语文、数学成绩"""

    def __init__(self, sid, name, chinese, math):
        # 实例属性
        self.sid = sid          # 学号
        self.name = name        # 姓名
        self.chinese = chinese  # 语文成绩
        self.math = math        # 数学成绩

    def get_avg(self):
        """返回两门课的平均分"""
        return (self.chinese + self.math) / 2

    def show_info(self):
        """格式化打印学生全部信息"""
        print(f"学号:{self.sid:<6} 姓名:{self.name:<5} "
              f"语文:{self.chinese:<5} 数学:{self.math:<5} "
              f"平均分:{self.get_avg():.2f}")

    def modify_score(self, subject, score):
        """修改成绩：subject 只能是 '语文' 或 '数学'"""
        if subject == "语文":
            self.chinese = score
        elif subject == "数学":
            self.math = score
        else:
            print("科目只能填 '语文' 或 '数学'！")
            return
        print(f"已把 {self.name} 的{subject}成绩改为 {score}")


# ---------------- 主程序 ----------------
print("========== 实验1：学生类 ==========")
s1 = Student("2024001", "张三", 85, 92)
s2 = Student("2024002", "李四", 78, 66)

print("--- 修改前 ---")
s1.show_info()
s2.show_info()

# 修改张三的成绩
s1.modify_score("语文", 95)
s1.modify_score("数学", 88)

print("--- 修改后 ---")
s1.show_info()
s2.show_info()