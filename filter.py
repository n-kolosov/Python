def func(elem):
    return elem >= 0
arr = [-1, 2, -3, 4, 0, -20, 10]
print(list(filter(func, arr))) #filter возвращает значения, соответствующие критерию из func

arr = [-1, 2, -3, 4, 0, -20, 10]
print(list(map(func, arr))) #map возвращает True или False в зависимости от того, соответствует ли элемент критерию из func

arr = [-1, 2, -3, 4, 0, -20, 10]
arr = [i for i in arr if func(i)]
print(arr)