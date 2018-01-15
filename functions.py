def print_ok():
    print("Успешно")
print_ok()

def printn(n = 5):
    print(n)
printn()
printn(10)

def summa(x = 5, y = 10):
    """Суммирование двух чисел"""
    return x + y
print(summa())
print(summa(50, 20))

f = summa
v = f(10, 20)
print(v)

def func(f, a, b):
    return f(a, b)
v = func(summa, 30, 70)
print(v)

print(dir(summa()))

def summa(a, b, c):
    return a + b +c
t1, arr = (1, 2, 3), [4, 5, 6]
print(summa(*t1))
print(summa(*arr))
d1 = {"a": 1, "b": 2, "c": 3}
print(summa(**d1))