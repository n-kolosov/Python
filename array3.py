arr = [[1, 2], [3, 4], [5, 6]]
arr = [j*10 for i in arr for j in i if j % 2 == 0]
print(arr)

arr = []
for i in [[1, 2], [3, 4], [5, 6]]:
    for j in i:
        if j % 2 == 0:
            arr.append(j*10)
print(arr)