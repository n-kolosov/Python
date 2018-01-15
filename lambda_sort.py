arr = ["Единица", "Двойка", "Тройка", "Четвёрка"]
arr.sort(key = lambda s: s.lower())
for i in arr:
    print(i, end=" ")