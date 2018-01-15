arr = [1, 2, 3, 4]
for i in arr: i += 10
print(arr)

for i in range(len(arr)): arr[i] += 10
print(arr)

arr = [1, 2, 3, 4]
for i, elem in enumerate(arr): arr[i] **= 2
print(arr)

arr = [1, 2, 3, 4]
arr = [i*2 for i in arr]
print(arr)

arr = [1, 2, 3, 4]
arr = [i*10 for i in arr if i % 2 == 0]
print(arr)