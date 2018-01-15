x = int(input("Введите x: "))
y = int(input("Введите y: "))
f = lambda x, y: x + y
print(f(x, y))

f1 = lambda: 10 + 20
f2 = lambda x, y: x + y
f3 = lambda x, y, z: x + y + z
print(f1(), f2(10, 20), f3(1, 2, 3))

f = lambda x, y = 5: x + y
print(f(1))
print(f(1, 1))