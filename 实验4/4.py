# 实验4：图书类 + 图书馆类（类的组合）

class Book:
    """图书类"""

    def __init__(self, bid, title, author):
        self.bid = bid                # 书号
        self.title = title            # 书名
        self.author = author          # 作者
        self.is_borrowed = False      # 是否借出，默认在馆

    def borrow(self):
        """借出图书"""
        if self.is_borrowed:
            print(f"《{self.title}》已被借出，借阅失败！")
            return False
        self.is_borrowed = True
        print(f"《{self.title}》借出成功。")
        return True

    def back(self):
        """归还图书"""
        if not self.is_borrowed:
            print(f"《{self.title}》本来就在馆，无需归还。")
            return False
        self.is_borrowed = False
        print(f"《{self.title}》归还成功。")
        return True

    def show(self):
        """打印单本书的信息"""
        state = "已借出" if self.is_borrowed else "在馆"
        print(f"书号:{self.bid:<6} 书名:《{self.title}》   "
              f"作者:{self.author:<6} 状态:{state}")


class Library:
    """图书馆类：内部保存一个图书列表"""

    def __init__(self):
        self.books = []               # 组合：Library 里装着 Book 对象

    def add_book(self, book):
        """添加图书"""
        self.books.append(book)
        print(f"已添加图书：《{book.title}》")

    def search_by_id(self, bid):
        """按书号查找，找到返回 Book 对象，找不到返回 None"""
        for b in self.books:
            if b.bid == bid:
                return b
        return None

    def show_all(self):
        """列出全部图书"""
        if not self.books:
            print("图书馆中暂无图书。")
            return
        print("-" * 60)
        for b in self.books:
            b.show()
        print("-" * 60)


# ---------------- 主流程 ----------------
print("========== 实验4：图书管理 ==========")

lib = Library()

# 1. 添加 3 本书
lib.add_book(Book("B001", "Python编程从入门到实践", "Eric Matthes"))
lib.add_book(Book("B002", "算法导论", "Cormen"))
lib.add_book(Book("B003", "活着", "余华"))

# 2. 查询某本书并借出
print("\n--- 查询书号 B002 ---")
book = lib.search_by_id("B002")
if book:
    book.show()
    print("\n--- 借出 ---")
    book.borrow()
    print("\n--- 借出后再次查询 ---")
    book = lib.search_by_id("B002")
    book.show()
else:
    print("没有找到这本书。")

# 3. 归还图书
print("\n--- 归还 B002 ---")
book = lib.search_by_id("B002")
if book:
    book.back()

# 4. 展示全部图书
print("\n--- 全部图书列表 ---")
lib.show_all()