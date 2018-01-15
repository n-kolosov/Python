arr = [1, 2, 1, 2, 1]
print(arr.index(1), arr.index(2), arr.index(1, 1), arr.index(1, 3, 5))
try:
    print(arr.index(4))
except ValueError:
    print("Не найден элемент со значением 4")