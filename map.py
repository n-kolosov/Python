def func(elem):
    return elem + 10
print(func(1))

arr = [1, 2, 3, 4, 5]
print(list(map(func, arr)))

def func(e1, e2, e3):
    return e1 + e2 + e3
arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20, 30, 40, 50]
arr3 = [100, 200, 300, 400, 500]
print(list(map(func, arr1, arr2, arr3)))

arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20]
arr3 = [100, 200, 300]
print(list(map(func, arr1, arr2, arr3)))