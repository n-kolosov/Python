from functools import reduce
def func(x, y):
    print("({0}, {1})".format(x, y), end=" ")
    return x + y

arr = [1, 2, 3, 4, 5]
summa = reduce(func, arr)
print(summa)
summa = reduce(func, arr, 10)
print(summa)
summa = reduce(func, [], 10)
print(summa)