def summa(*t):
    res = 0
    for i in t:
        res += i
    return res
print(summa(10, 20))
print(summa(100, 200, 20, 4))

def summa(x, y=5, *t):
    res = x + y
    for i in t:
        res += i
    return res
print(summa(10))
print(summa(10, 20, 30))

def func(**d):
    for i in d:
        print("{0} => {1}".format(i, d[i]), end=" ")
func(a=1, b=2, c=3)