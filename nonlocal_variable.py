def func1(a):
    x = a
    def func2(b):
        nonlocal x
        print(x)
        x = b
    return func2

f = func1(10)
f(5)
f(12)
f(3)