arr = [1, 2, 3]
print(arr + [4, 5, 6]) #возвращает новый список
print(arr)
arr += [4, 5, 6] #изменяет существующий список
print(arr)

arr = [1, 2, 3]
arr[len(arr):] = [4, 5, 6]
print(arr)