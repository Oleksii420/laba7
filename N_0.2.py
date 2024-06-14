#a
import math

def compute_a(k, x):
    return x**k / k

def generator_a(x):
    k = 1
    while True:
        yield x**k / k
        k += 1


def compute_b(k, x):
    return ((-1)**k * x**k) / k

def generator_b(x):
    k = 1
    while True:
        yield ((-1)**k * x**k) / k
        k += 1

def compute_c(k, x):
    return ((-1)**k * x**k) / math.factorial(k**2 + k)

def generator_c(x):
    k = 0
    while True:
        yield ((-1)**k * x**k) / math.factorial(k**2 + k)
        k += 1

def compute_d(k, x):
    return x**(2*k) / math.factorial(2*k)

def generator_d(x):
    k = 0
    while True:
        yield x**(2*k) / math.factorial(2*k)
        k += 1

def compute_e(k, x):
    return ((-1)**k * x**(2*k)) / math.factorial(2*k)

def generator_e(x):
    k = 0
    while True:
        yield ((-1)**k * x**(2*k)) / math.factorial(2*k)
        k += 1


def compute_f(k, x):
    return x**(2*k+1) / math.factorial(2*k+1)

def generator_f(x):
    k = 0
    while True:
        yield x**(2*k+1) / math.factorial(2*k+1)
        k += 1

k = 5
x = 2
print(compute_a(k, x))

gen_a = generator_a(x)
for el in range(k):
    term_a = next(gen_a)
print("a:", term_a)

print(compute_b(k, x))

gen_b = generator_b(x)
for el in range(k):
    term_b = next(gen_b)
print("b:", term_b)

print(compute_c(k, x))

gen_c = generator_c(x)
for el in range(k):
    term_c = next(gen_c)
print("c:", term_c)

print(compute_d(k, x))

gen_d = generator_d(x)
for el in range(k):
    term_d = next(gen_d)
print("d:", term_d)
