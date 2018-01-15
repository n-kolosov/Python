l = list()
print(l)

l = list("String")
print(l)

l = list((1, 2, 3, 4, 5)) #передаём кортеж в оператор list
print(l)

arr = [1, "str", 3, 4]
print(arr)

arr = []
arr.append(1) #добавление элемента массива при помощи оператора append
arr.append("str")
print(arr)

x = y = [1, 2]
print(x is y)

x, y = [1, 2], [1, 2]
print(x is y)

x = [1, 2, 3, 4, 5]
y = list(x)
print(y)
print(x is y)
y[1] = 100
print(x, y)