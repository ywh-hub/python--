from datetime import date, timedelta
from collections import Counter


def is_special_date(d):
    s = d.strftime("%Y%m%d")
    if len(s) != 8:
        return False
    c = Counter(s)
    # 8个字符，7种不同数字，说明恰有一个数字重复一次
    return len(c) == 7 and max(c.values()) == 2


def nearest_three_special_dates(today=None):
    if today is None:
        today = date.today()

    found = []
    offset = 0

    while len(found) < 3:
        if offset == 0:
            candidates = [today]
        else:
            candidates = [
                today - timedelta(days=offset),
                today + timedelta(days=offset)
            ]

        for d in candidates:
            if is_special_date(d):
                found.append((abs((d - today).days), d))

        offset += 1

    found.sort(key=lambda x: (x[0], x[1]))
    return found[:3]


if __name__ == "__main__":
    result = nearest_three_special_dates()
    for dist, d in result:
        print(d, d.strftime("%Y%m%d"), "距离今天", dist, "天")