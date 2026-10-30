# 多项式加法
def poly_add(p, q):
    n = max(len(p), len(q))
    result = [0] * n

    for i in range(len(p)):
        result[i] += p[i]

    for i in range(len(q)):
        result[i] += q[i]

    return result

# 多项式乘法
def poly_mul(p, q):
    result = [0] * (len(p) + len(q) - 1)

    for i in range(len(p)):
        for j in range(len(q)):
            result[i + j] += p[i] * q[j]

    return result

# 简单打印多项式
def show_poly(p):
    terms = []
    for i, c in enumerate(p):
        if c != 0:
            if i == 0:
                terms.append(str(c))
            elif i == 1:
                terms.append(f"{c}x")
            else:
                terms.append(f"{c}x^{i}")

    if not terms:
        return "0"
    return " + ".join(terms)

p = [1, 2, 3]   # 1 + 2x + 3x^2
q = [2, 1]      # 2 + x

print("p =", show_poly(p))
print("q =", show_poly(q))
print("加法：", show_poly(poly_add(p, q)))
print("乘法：", show_poly(poly_mul(p, q)))