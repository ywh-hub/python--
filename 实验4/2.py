# 实验2：矩形类，含静态方法校验
class Rectangle:
    """矩形类"""

    def __init__(self, a, b):
        # 用静态方法做参数校验，不合法就不允许创建
        if not Rectangle.is_valid(a, b):
            raise ValueError(f"长和宽必须都大于0，收到：a={a}, b={b}")
        self.a = a  # 长
        self.b = b  # 宽

    # ---------- 实例方法 ----------
    def area(self):
        """面积"""
        return self.a * self.b

    def perimeter(self):
        """周长"""
        return 2 * (self.a + self.b)

    def is_square(self):
        """是否正方形"""
        return abs(self.a - self.b) < 1e-9   # 浮点数用极小值比较更稳妥

    # ---------- 静态方法 ----------
    @staticmethod
    def is_valid(a, b):
        """判断长宽是否合法（与具体对象无关，所以用静态方法）"""
        return a > 0 and b > 0


# ---------------- 主程序 ----------------
print("========== 实验2：矩形类 ==========")
print("请输入矩形的长和宽（用空格分隔），直接回车结束：")

while True:
    line = input("长 宽：").strip()
    if line == "":
        break

    # 先处理输入格式错误
    try:
        a, b = map(float, line.split())
    except ValueError:
        print("输入格式错误，请输入两个数字，用空格分隔。")
        continue

    # 再处理参数不合法的情况
    try:
        rect = Rectangle(a, b)
    except ValueError as e:
        print("创建失败：", e)
        continue

    # 创建成功，输出信息
    print(f"长={rect.a:g}  宽={rect.b:g}  "
          f"面积={rect.area():.2f}  周长={rect.perimeter():.2f}  "
          f"是正方形吗？{rect.is_square()}")

print("程序结束。")