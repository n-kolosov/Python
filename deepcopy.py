import copy
x = [1, [2, 3, 4, 5]]
y = list(x)
print(x is y)
y[1][1] = 100
print(x, y)

m = [1, [2, 3, 4, 5]]
n = copy.deepcopy(m)
print(m is n)
n[1][1] = 100
print(m, n)