def sum_a(n):
    S_n = 0
    for k in range(1, n + 1):
        S_n += 1 / (k * (k + 1))
    return S_n

n = 5
print("a:", sum_a(n))


def sum_b(n):
    S_n = 0
    for k in range(1, n + 1):
        S_n += ((-1) ** (k - 1)) * k / (k + 1)
    return S_n

n = 5
print("b:", sum_b(n))
