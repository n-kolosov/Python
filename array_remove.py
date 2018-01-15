arr = [1, 2, 3, 1, 1]
arr.remove(1) #удаляет первый найденный элемент, содержащий указанное значение
print(arr)
try:
    arr.remove(5)
except ValueError:
    print("Элемент со значением 5 не найден в массиве")