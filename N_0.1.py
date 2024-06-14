def sqrt_series(n):
    x = 2 ** 0.5
    for el in range(1, n):
        x = (2 + x) ** 0.5
    return x

n = 5
print(sqrt_series(n))
