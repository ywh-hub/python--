# 实验3：图形继承（父类 Shape，子类 Circle / Triangle）
import math


class Shape:
    """图形基类：定义统一接口（抽象风格）"""

    def get_area(self):
        pass        # 占位，交给子类重写

    def show(self):
        pass        # 占位，交给子类重写


class Circle(Shape):
    """圆形"""

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2      # 圆面积 πr²

    def show(self):
        print(f"[圆形] 半径 = {self.r:g}")


class Triangle(Shape):
    """三角形"""

    def __init__(self, base, height):
        self.base = base      # 底
        self.height = height  # 高

    def get_area(self):
        return 0.5 * self.base * self.height   # 三角形面积 底×高÷2

    def show(self):
        print(f"[三角形] 底 = {self.base:g}，高 = {self.height:g}")


# ---------------- 主程序：体会多态 ----------------
print("========== 实验3：图形继承与多态 ==========")

# 把不同子类对象都放进同一个列表
shapes = [
    Circle(3),
    Triangle(4, 5),
    Circle(1.5),
    Triangle(6, 2.5),
]

for s in shapes:
    s.show()                                  # 同一个调用，不同表现
    print(f"        面积 = {s.get_area():.2f}")